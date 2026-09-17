#!/usr/bin/env python3
"""Build a model-independent DPO Parquet release from a pinned Hub snapshot.

The source directory is expected to use one subdirectory per language/config.
Each subdirectory may contain JSONL files with string completions or Parquet
files with conversational completions.  The output always has this schema:

    id, language, prompt, chosen, rejected, source_revision

where prompt/chosen/rejected are unrendered lists of ``{role, content}``
messages.  The builder applies only structural eligibility filters.  Broader
PII, safety, language-quality, task-quality, and contamination decisions stay
as explicit catalogue gates.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator

import pyarrow as pa
import pyarrow.parquet as pq


MESSAGE = pa.struct(
    [
        pa.field("role", pa.string(), nullable=False),
        pa.field("content", pa.large_string(), nullable=False),
    ]
)
RELEASE_SCHEMA = pa.schema(
    [
        pa.field("id", pa.large_string(), nullable=False),
        pa.field("language", pa.string(), nullable=False),
        pa.field("prompt", pa.list_(MESSAGE), nullable=False),
        pa.field("chosen", pa.list_(MESSAGE), nullable=False),
        pa.field("rejected", pa.list_(MESSAGE), nullable=False),
        pa.field("source_revision", pa.string(), nullable=False),
    ]
)
REJECTION_SCHEMA = pa.schema(
    [
        pa.field("id", pa.large_string()),
        pa.field("language", pa.string(), nullable=False),
        pa.field("source_row", pa.int64(), nullable=False),
        pa.field("reason", pa.string(), nullable=False),
    ]
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-id", required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--release-dir", type=Path, required=True)
    parser.add_argument("--quality-dir", type=Path, required=True)
    parser.add_argument("--counts-dir", type=Path, required=True)
    parser.add_argument("--languages", nargs="+", required=True)
    parser.add_argument("--rows-per-shard", type=int, default=50_000)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc


def iter_parquet(path: Path, batch_size: int = 4096) -> Iterator[dict[str, Any]]:
    parquet = pq.ParquetFile(path)
    for batch in parquet.iter_batches(batch_size=batch_size):
        yield from batch.to_pylist()


def source_files(source_dir: Path, language: str) -> list[Path]:
    language_dir = source_dir / language
    files = sorted(language_dir.glob("*.parquet"))
    files.extend(sorted(language_dir.glob("*.jsonl")))
    if not files:
        raise FileNotFoundError(f"No Parquet or JSONL files under {language_dir}")
    return files


def iter_source_rows(files: Iterable[Path]) -> Iterator[dict[str, Any]]:
    for path in files:
        if path.suffix == ".parquet":
            yield from iter_parquet(path)
        elif path.suffix == ".jsonl":
            yield from iter_jsonl(path)
        else:
            raise ValueError(f"Unsupported source file: {path}")


def normalize_messages(value: Any, *, completion: bool) -> list[dict[str, str]]:
    if isinstance(value, str):
        if not completion:
            raise ValueError("prompt_is_string")
        messages = [{"role": "assistant", "content": value}]
    elif isinstance(value, list):
        messages = value
    else:
        raise ValueError("not_string_or_message_list")

    normalized: list[dict[str, str]] = []
    for message in messages:
        if not isinstance(message, dict):
            raise ValueError("message_is_not_object")
        role = message.get("role")
        content = message.get("content")
        if not isinstance(role, str) or not role.strip():
            raise ValueError("invalid_message_role")
        if not isinstance(content, str):
            raise ValueError("invalid_message_content")
        normalized.append({"role": role, "content": content})

    if not normalized:
        raise ValueError("empty_message_list")
    if not any(message["content"].strip() for message in normalized):
        raise ValueError("empty_message_content")
    return normalized


def write_parquet(rows: list[dict[str, Any]], path: Path, schema: pa.Schema) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pylist(rows, schema=schema)
    pq.write_table(
        table,
        path,
        compression="zstd",
        compression_level=6,
        use_dictionary=True,
        write_statistics=True,
    )


def build_language(
    *,
    language: str,
    files: list[Path],
    release_dir: Path,
    quality_dir: Path,
    revision: str,
    rows_per_shard: int,
) -> dict[str, Any]:
    seen_ids: set[str] = set()
    kept: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    rejection_counts: Counter[str] = Counter()
    output_files: list[Path] = []
    input_rows = 0

    def reject(row_id: str | None, source_row: int, reason: str) -> None:
        rejected.append(
            {
                "id": row_id,
                "language": language,
                "source_row": source_row,
                "reason": reason,
            }
        )
        rejection_counts[reason] += 1

    def flush() -> None:
        if not kept:
            return
        shard_index = len(output_files)
        destination = release_dir / language / f"train-{shard_index:05d}.parquet"
        write_parquet(kept, destination, RELEASE_SCHEMA)
        output_files.append(destination)
        kept.clear()

    for source_row, row in enumerate(iter_source_rows(files)):
        input_rows += 1
        raw_id = row.get("id")
        row_id = raw_id if isinstance(raw_id, str) and raw_id else None
        if row_id is None:
            reject(None, source_row, "missing_id")
            continue
        if row_id in seen_ids:
            reject(row_id, source_row, "duplicate_id_within_config")
            continue
        seen_ids.add(row_id)

        try:
            prompt = normalize_messages(row.get("prompt"), completion=False)
            chosen = normalize_messages(row.get("chosen"), completion=True)
            rejected_messages = normalize_messages(row.get("rejected"), completion=True)
        except ValueError as exc:
            reject(row_id, source_row, f"invalid_structure:{exc}")
            continue

        if chosen == rejected_messages:
            reject(row_id, source_row, "identical_preference_pair")
            continue

        kept.append(
            {
                "id": row_id,
                "language": language,
                "prompt": prompt,
                "chosen": chosen,
                "rejected": rejected_messages,
                "source_revision": revision,
            }
        )
        if len(kept) >= rows_per_shard:
            flush()
    flush()

    rejection_path = quality_dir / "structural-rejections" / f"{language}.parquet"
    if rejected:
        write_parquet(rejected, rejection_path, REJECTION_SCHEMA)

    return {
        "input_rows": input_rows,
        "release_rows": input_rows - sum(rejection_counts.values()),
        "rejection_counts": dict(sorted(rejection_counts.items())),
        "source_files": [str(path) for path in files],
        "release_files": [str(path.relative_to(release_dir)) for path in output_files],
        "rejection_file": (
            str(rejection_path.relative_to(quality_dir)) if rejected else None
        ),
    }


def write_dataset_card(path: Path, languages: list[str], repo_id: str, revision: str) -> None:
    config_lines: list[str] = []
    for language in languages:
        config_lines.extend(
            [
                f"- config_name: {language}",
                "  data_files:",
                "  - split: train",
                f"    path: {language}/train-*.parquet",
            ]
        )
    contents = "\n".join(
        [
            "---",
            "configs:",
            *config_lines,
            "license: apache-2.0",
            "task_categories:",
            "- text-generation",
            "---",
            "",
            "# Dolci Instruct DPO translated — LUMI candidate release",
            "",
            f"Source: `{repo_id}` at immutable revision `{revision}`.",
            "",
            "Rows use the canonical unrendered DPO schema: `id`, `language`,",
            "`prompt`, `chosen`, `rejected`, and `source_revision`. Prompt and",
            "completion fields are lists of `{role, content}` messages.",
            "",
            "This is a structurally validated candidate, not an approved release.",
            "PII, safety, language-quality, task-quality, and contamination gates",
            "remain tracked in the collection metadata.",
            "",
        ]
    )
    path.write_text(contents, encoding="utf-8")


def main() -> None:
    args = parse_args()
    if args.rows_per_shard <= 0:
        raise ValueError("--rows-per-shard must be positive")
    if not args.source_dir.is_dir():
        raise FileNotFoundError(args.source_dir)

    targets = [args.release_dir, args.quality_dir, args.counts_dir]
    for target in targets:
        if target.exists():
            raise FileExistsError(f"Refusing to overwrite existing output: {target}")

    build_suffix = f".building-{os.getpid()}"
    build_release = args.release_dir.with_name(args.release_dir.name + build_suffix)
    build_quality = args.quality_dir.with_name(args.quality_dir.name + build_suffix)
    build_counts = args.counts_dir.with_name(args.counts_dir.name + build_suffix)
    for path in (build_release, build_quality, build_counts):
        path.mkdir(parents=True, exist_ok=False)

    try:
        language_stats: dict[str, Any] = {}
        for language in args.languages:
            files = source_files(args.source_dir, language)
            language_stats[language] = build_language(
                language=language,
                files=files,
                release_dir=build_release,
                quality_dir=build_quality,
                revision=args.revision,
                rows_per_shard=args.rows_per_shard,
            )

        write_dataset_card(build_release / "README.md", args.languages, args.repo_id, args.revision)

        release_files = sorted(path for path in build_release.rglob("*") if path.is_file())
        quality_files = sorted(path for path in build_quality.rglob("*") if path.is_file())
        source_paths = sorted(
            {Path(path) for stats in language_stats.values() for path in stats["source_files"]}
        )
        manifest = {
            "schema_version": 1,
            "repo_id": args.repo_id,
            "revision": args.revision,
            "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "builder": {
                "path": str(Path(__file__).resolve()),
                "sha256": sha256_file(Path(__file__).resolve()),
            },
            "release_schema": str(RELEASE_SCHEMA),
            "structural_filters": [
                "missing_id",
                "duplicate_id_within_config",
                "invalid prompt/chosen/rejected message structure",
                "identical_preference_pair",
            ],
            "pending_gates": [
                "pii",
                "safety",
                "language_quality",
                "task_quality",
                "contamination",
            ],
            "languages": language_stats,
            "source_files": [
                {
                    "path": str(path),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
                for path in source_paths
            ],
            "release_files": [
                {
                    "path": str(path.relative_to(build_release)),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
                for path in release_files
            ],
            "quality_files": [
                {
                    "path": str(path.relative_to(build_quality)),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
                for path in quality_files
            ],
        }
        manifest_path = build_counts / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        (build_counts / "_SUCCESS").write_text(
            f"{args.repo_id}@{args.revision}\n", encoding="utf-8"
        )

        build_release.rename(args.release_dir)
        build_quality.rename(args.quality_dir)
        build_counts.rename(args.counts_dir)
    except Exception:
        for path in (build_release, build_quality, build_counts):
            if path.exists():
                shutil.rmtree(path)
        raise


if __name__ == "__main__":
    main()
