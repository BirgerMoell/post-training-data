#!/usr/bin/env python3
"""Validate post-training mix manifests and their collection releases."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MIX_ROOT = ROOT / "mixes"
REQUIRED_CHECKS = (
    "license",
    "pii",
    "safety",
    "integrity",
    "language_quality",
    "task_quality",
    "contamination",
)
CHECK_STATES = {"complete", "pending", "inapplicable"}
RELEASE_STATES = {"candidate", "approved", "deprecated"}
MIX_STATES = {"draft", "pilot", "approved", "deprecated"}
BACKENDS_BY_METHOD = {
    "sft": {"trl", "llamafactory"},
    "dpo": {"trl", "llamafactory"},
    "rlvr": {"tmax", "verl", "skyrl"},
}


def load_mapping(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot load YAML: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path.relative_to(ROOT)}: root must be a mapping")
        return None
    return value


def validate_catalogue_entry(
    metadata: dict[str, Any], path: Path, errors: list[str]
) -> None:
    reference = metadata.get("catalogue_entry")
    if not isinstance(reference, str) or not reference:
        errors.append(f"{path.relative_to(ROOT)}: catalogue_entry is required")
        return
    catalogue_path = ROOT / reference
    if not catalogue_path.is_file():
        errors.append(
            f"{path.relative_to(ROOT)}: catalogue entry does not exist: {reference}"
        )
        return
    text = catalogue_path.read_text(encoding="utf-8")
    if re.search(r"(?m)^status_key:\s*eval-only\s*$", text):
        errors.append(
            f"{path.relative_to(ROOT)}: evaluation-only data must never be selected"
        )


def validate_collection(
    path: Path,
    *,
    release_name: str,
    method: str,
    approved_mix: bool,
    errors: list[str],
) -> dict[str, Any] | None:
    metadata = load_mapping(path, errors)
    if metadata is None:
        return None
    label = path.relative_to(ROOT)
    if metadata.get("schema_version") != 1:
        errors.append(f"{label}: schema_version must be 1")
    if metadata.get("task") != method:
        errors.append(f"{label}: task must match mix method {method!r}")
    if metadata.get("training_eligible") is not True:
        errors.append(f"{label}: training_eligible must be true")
    validate_catalogue_entry(metadata, path, errors)

    checks = metadata.get("checks")
    if not isinstance(checks, dict):
        errors.append(f"{label}: checks must be a mapping")
        checks = {}
    for name in REQUIRED_CHECKS:
        check = checks.get(name)
        if not isinstance(check, dict):
            errors.append(f"{label}: checks.{name} is required")
            continue
        state = check.get("status")
        if state not in CHECK_STATES:
            errors.append(
                f"{label}: checks.{name}.status must be one of {sorted(CHECK_STATES)}"
            )
        if state == "inapplicable" and not check.get("reason"):
            errors.append(
                f"{label}: checks.{name}.reason is required when inapplicable"
            )
        if approved_mix and state not in {"complete", "inapplicable"}:
            errors.append(f"{label}: approved mix cannot use pending checks.{name}")

    releases = metadata.get("release")
    if not isinstance(releases, dict) or release_name not in releases:
        errors.append(f"{label}: unknown release {release_name!r}")
        return None
    release = releases[release_name]
    if not isinstance(release, dict):
        errors.append(f"{label}: release.{release_name} must be a mapping")
        return None
    if release.get("status") not in RELEASE_STATES:
        errors.append(
            f"{label}: release.{release_name}.status must be one of {sorted(RELEASE_STATES)}"
        )
    if approved_mix and release.get("status") != "approved":
        errors.append(f"{label}: approved mix requires an approved release")

    dataset = release.get("dataset")
    if not isinstance(dataset, dict):
        errors.append(f"{label}: release.{release_name}.dataset must be a mapping")
        return None
    for key in ("path", "split", "schema"):
        if not dataset.get(key):
            errors.append(f"{label}: release.{release_name}.dataset.{key} is required")
    dataset_path = dataset.get("path")
    if (
        isinstance(dataset_path, str)
        and not dataset_path.startswith("/")
        and not dataset.get("revision")
    ):
        errors.append(f"{label}: Hugging Face releases must pin dataset.revision")
    return dataset


def validate_mix(path: Path, errors: list[str]) -> None:
    mix = load_mapping(path, errors)
    if mix is None:
        return
    label = path.relative_to(ROOT)
    if mix.get("schema_version") != 1:
        errors.append(f"{label}: schema_version must be 1")
    status = mix.get("status")
    if status not in MIX_STATES:
        errors.append(f"{label}: status must be one of {sorted(MIX_STATES)}")
    method = mix.get("method")
    if method not in {"sft", "dpo", "rlvr"}:
        errors.append(f"{label}: method must be sft, dpo, or rlvr")
        return
    backend = mix.get("backend")
    if backend not in BACKENDS_BY_METHOD[method]:
        errors.append(
            f"{label}: backend {backend!r} is not valid for method {method!r}; "
            f"choose from {sorted(BACKENDS_BY_METHOD[method])}"
        )
    sampling = mix.get("sampling")
    if not isinstance(sampling, dict) or sampling.get("mode") != "multiplier":
        errors.append(f"{label}: sampling.mode must be multiplier")
    data = mix.get("data")
    datasets = data.get("datasets") if isinstance(data, dict) else None
    if not isinstance(datasets, list) or not datasets:
        errors.append(f"{label}: data.datasets must be a non-empty list")
        return

    names: set[str] = set()
    for index, item in enumerate(datasets):
        item_label = f"{label}: data.datasets[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{item_label} must be a mapping")
            continue
        name = item.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"{item_label}.name is required")
        elif name in names:
            errors.append(f"{item_label}: duplicate name {name!r}")
        else:
            names.add(name)
        weight = item.get("weight")
        if not isinstance(weight, (int, float)) or weight < 0:
            errors.append(f"{item_label}.weight must be a non-negative number")

        collection_ref = item.get("collection")
        if collection_ref:
            if "path" in item:
                errors.append(f"{item_label}: use collection/release or path, not both")
                continue
            protected = {
                "revision",
                "data_dir",
                "split",
                "transform",
                "schema",
                "expected_rows",
                "sha256",
                "locations",
                "llamafactory",
            }
            overridden = protected.intersection(item)
            if overridden:
                errors.append(
                    f"{item_label}: release identity fields must stay in collection metadata: "
                    f"{sorted(overridden)}"
                )
            collection_path = (path.parent / collection_ref).resolve()
            if not collection_path.is_relative_to(ROOT):
                errors.append(
                    f"{item_label}: collection metadata must be inside this repository"
                )
                continue
            dataset = validate_collection(
                collection_path,
                release_name=item.get("release", "default"),
                method=method,
                approved_mix=status == "approved",
                errors=errors,
            )
            configs = dataset.get("configs") if isinstance(dataset, dict) else None
            if configs and item.get("subset") not in configs:
                errors.append(
                    f"{item_label}: subset must name one of {sorted(configs)}"
                )
            if not configs and "subset" in item:
                errors.append(
                    f"{item_label}: subset must be declared by release dataset.configs"
                )
        else:
            for key in ("path", "revision", "split", "schema"):
                if not item.get(key):
                    errors.append(f"{item_label}.{key} is required for direct entries")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="CI-compatible alias; no files are changed"
    )
    parser.parse_args()

    errors: list[str] = []
    paths = sorted(MIX_ROOT.rglob("*.yaml"))
    for path in paths:
        validate_mix(path, errors)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(paths)} mix manifests and their collection releases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
