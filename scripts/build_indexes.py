#!/usr/bin/env python3
"""Build and validate the human-facing catalogue indexes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "datasets"

TYPE_LABELS = {
    "instruction-sft": "Instruction SFT",
    "reasoning-sft": "Reasoning SFT",
    "preference-optimization": "Preference optimization",
    "reinforcement-learning": "RLVR / GRPO / verifiable RL",
    "tool-and-agentic": "Tool use and agentic training",
    "long-context-extension": "Long-context extension",
    "continued-pretraining": "Continued pretraining",
    "medical": "Medical specialization",
    "safety-and-civic": "Safety and civic training",
    "language-repair": "Language repair",
    "data-quality-and-filtering": "Data quality, filtering, and decontamination",
    "evaluation-holdouts": "Evaluation holdouts",
    "all-stages": "All stages",
}

LANGUAGE_LABELS = {
    "multilingual": "Multilingual and European language groups",
    "code": "Code",
    "unspecified": "Unspecified",
    "en": "English",
    "fi": "Finnish",
    "sv": "Swedish",
    "da": "Danish",
    "no": "Norwegian",
    "is": "Icelandic",
    "cs": "Czech",
    "de": "German",
    "el": "Greek",
    "es": "Spanish",
    "fr": "French",
    "it": "Italian",
    "nl": "Dutch",
    "pl": "Polish",
    "ro": "Romanian",
    "uk": "Ukrainian",
    "sq": "Albanian",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "et": "Estonian",
    "eu": "Basque",
    "ga": "Irish",
    "mt": "Maltese",
    "hr": "Croatian",
    "sl": "Slovenian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "hu": "Hungarian",
    "sk": "Slovak",
}

STATUS_LABELS = {
    "used-in-completed-run": "Used in a completed run",
    "used-in-research": "Used in a research run",
    "published": "Published / available",
    "configured-runnable": "Configured / runnable",
    "staged": "Staged",
    "candidate": "Candidate",
    "planned": "Planned",
    "supporting": "Supporting / filtering",
    "needs-verification": "Needs verification",
    "historical": "Historical / superseded",
    "eval-only": "Evaluation-only — do not train",
}

REQUIRED = {
    "name",
    "slug",
    "training_types",
    "status_key",
    "status",
    "language_keys",
    "languages",
    "purpose",
    "public_location",
    "lumi_location",
    "source_sheet_row",
}


def parse_frontmatter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing opening frontmatter marker")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: missing closing frontmatter marker") from exc

    metadata: dict = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"{path}: invalid frontmatter line: {line!r}")
        try:
            metadata[key.strip()] = json.loads(value.strip())
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"{path}: frontmatter values must use JSON syntax: {line!r}"
            ) from exc
    return metadata


def load_entries() -> list[dict]:
    entries: list[dict] = []
    errors: list[str] = []
    seen_slugs: set[str] = set()

    for path in sorted(DATASETS.glob("*/README.md")):
        if path.parent.name.startswith("_"):
            continue
        try:
            item = parse_frontmatter(path)
            missing = REQUIRED - item.keys()
            if missing:
                errors.append(f"{path}: missing {sorted(missing)}")
                continue
            if item["slug"] != path.parent.name:
                errors.append(
                    f"{path}: slug {item['slug']!r} does not match folder name"
                )
            if item["slug"] in seen_slugs:
                errors.append(f"{path}: duplicate slug {item['slug']!r}")
            seen_slugs.add(item["slug"])
            if not isinstance(item["training_types"], list) or not item["training_types"]:
                errors.append(f"{path}: training_types must be a non-empty list")
            for key in item.get("training_types", []):
                if key not in TYPE_LABELS:
                    errors.append(f"{path}: unknown training type {key!r}")
            if item["status_key"] not in STATUS_LABELS:
                errors.append(f"{path}: unknown status_key {item['status_key']!r}")
            if not isinstance(item["language_keys"], list) or not item["language_keys"]:
                errors.append(f"{path}: language_keys must be a non-empty list")
            entries.append(item)
        except ValueError as exc:
            errors.append(str(exc))

    if errors:
        raise ValueError("\n".join(errors))
    if not entries:
        raise ValueError("No dataset entries found")
    return sorted(entries, key=lambda item: item["name"].casefold())


def clean(value: object) -> str:
    return str(value or "—").replace("|", "\\|").replace("\n", " ").strip() or "—"


def dataset_link(item: dict, prefix: str) -> str:
    return f"[{clean(item['name'])}]({prefix}datasets/{item['slug']}/README.md)"


def type_text(item: dict) -> str:
    return ", ".join(TYPE_LABELS[key] for key in item["training_types"])


def locations(item: dict) -> str:
    parts: list[str] = []
    if item["public_location"]:
        parts.append(f"[public](<{item['public_location']}>)")
    if item["lumi_location"]:
        parts.append("LUMI")
    return " · ".join(parts) or "Not recorded"


def generated_note() -> str:
    return (
        "> Generated from the metadata at the top of each dataset page. "
        "Run `python3 scripts/build_indexes.py` after changing an entry.\n"
    )


def table_header(columns: list[str]) -> str:
    return (
        "| " + " | ".join(columns) + " |\n"
        + "| " + " | ".join("---" for _ in columns) + " |\n"
    )


def build_outputs(entries: list[dict]) -> dict[Path, str]:
    outputs: dict[Path, str] = {}

    catalogue = [
        "# Complete catalogue\n",
        generated_note(),
        f"\n{len(entries)} datasets, artifacts, products, and support resources are currently listed.\n\n",
        table_header(["Dataset / product", "Training use", "State", "Languages", "Locations"]),
    ]
    for item in entries:
        catalogue.append(
            f"| {dataset_link(item, '')} | {clean(type_text(item))} | "
            f"{clean(item['status'])} | {clean(item['languages'])} | {locations(item)} |\n"
        )
    outputs[ROOT / "CATALOGUE.md"] = "".join(catalogue)

    type_groups = {
        key: [item for item in entries if key in item["training_types"]]
        for key in TYPE_LABELS
    }
    type_overview = ["# Browse by training type\n", generated_note(), "\n"]
    for key, label in TYPE_LABELS.items():
        type_overview.append(
            f"- [{label}]({key}/README.md) — {len(type_groups[key])} entries\n"
        )
        body = [
            f"# {label}\n",
            generated_note(),
            f"\n{len(type_groups[key])} entries.\n\n",
            table_header(["Dataset / product", "State", "Languages", "Purpose", "Locations"]),
        ]
        for item in type_groups[key]:
            body.append(
                f"| {dataset_link(item, '../../')} | {clean(item['status'])} | "
                f"{clean(item['languages'])} | {clean(item['purpose'])} | {locations(item)} |\n"
            )
        outputs[ROOT / "training-types" / key / "README.md"] = "".join(body)
    outputs[ROOT / "training-types" / "README.md"] = "".join(type_overview)

    language_keys = sorted(
        {key for item in entries for key in item["language_keys"]},
        key=lambda key: LANGUAGE_LABELS.get(key, key).casefold(),
    )
    language_overview = ["# Browse by language\n", generated_note(), "\n"]
    for key in language_keys:
        label = LANGUAGE_LABELS.get(key, key.upper())
        group = [item for item in entries if key in item["language_keys"]]
        language_overview.append(
            f"- [{label}]({key}/README.md) — {len(group)} entries\n"
        )
        body = [
            f"# {label}\n",
            generated_note(),
            (
                "\nEntries are grouped from the language description recorded on each page. "
                "Broad multilingual entries may not enumerate every included language.\n\n"
            ),
            table_header(["Dataset / product", "Training use", "State", "Recorded coverage"]),
        ]
        for item in group:
            body.append(
                f"| {dataset_link(item, '../../')} | {clean(type_text(item))} | "
                f"{clean(item['status'])} | {clean(item['languages'])} |\n"
            )
        outputs[ROOT / "languages" / key / "README.md"] = "".join(body)
    outputs[ROOT / "languages" / "README.md"] = "".join(language_overview)

    status_overview = ["# Browse by state\n", generated_note(), "\n"]
    for key, label in STATUS_LABELS.items():
        group = [item for item in entries if item["status_key"] == key]
        status_overview.append(
            f"- [{label}]({key}/README.md) — {len(group)} entries\n"
        )
        body = [
            f"# {label}\n",
            generated_note(),
            f"\n{len(group)} entries.\n\n",
            table_header(["Dataset / product", "Training use", "Languages", "Locations"]),
        ]
        for item in group:
            body.append(
                f"| {dataset_link(item, '../../')} | {clean(type_text(item))} | "
                f"{clean(item['languages'])} | {locations(item)} |\n"
            )
        outputs[ROOT / "status" / key / "README.md"] = "".join(body)
    outputs[ROOT / "status" / "README.md"] = "".join(status_overview)

    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated indexes are missing or out of date.",
    )
    args = parser.parse_args()

    try:
        entries = load_entries()
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    outputs = build_outputs(entries)
    if args.check:
        stale: list[str] = []
        for path, expected in outputs.items():
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        if stale:
            print("Generated indexes are out of date:", file=sys.stderr)
            for path in stale:
                print(f"  - {path}", file=sys.stderr)
            print("Run: python3 scripts/build_indexes.py", file=sys.stderr)
            return 1
        print(f"Catalogue is valid: {len(entries)} entries, {len(outputs)} indexes")
        return 0

    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(outputs)} indexes for {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

