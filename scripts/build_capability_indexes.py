#!/usr/bin/env python3
"""Validate capability manifests and build their human-readable review views."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAP_ROOT = ROOT / "capabilities"
TRAINING_DECISIONS = {"use", "pilot", "candidate", "hold", "exclude"}
GATE_CLASSES = {"release", "headline", "diagnostic", "non-compensatory"}


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: top level must be an object")
    return value


def parse_catalogue_frontmatter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path.relative_to(ROOT)}: missing catalogue frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: unclosed catalogue frontmatter") from exc
    result: dict = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, marker, value = line.partition(":")
        if not marker:
            raise ValueError(f"{path.relative_to(ROOT)}: invalid frontmatter line")
        result[key.strip()] = json.loads(value.strip())
    return result


def require_fields(value: dict, fields: set[str], path: Path, errors: list[str]) -> None:
    missing = fields - value.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing fields {sorted(missing)}")


def validate_catalogue_link(
    relative: str | None, context: Path, errors: list[str]
) -> tuple[Path | None, dict | None]:
    if relative is None:
        return None, None
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"{context.relative_to(ROOT)}: missing catalogue entry {relative!r}")
        return path, None
    try:
        return path, parse_catalogue_frontmatter(path)
    except (ValueError, json.JSONDecodeError) as exc:
        errors.append(str(exc))
        return path, None


def target_text(target: dict) -> str:
    committed = target.get("committed")
    stretch = target.get("stretch")
    committed_text = "TBD" if committed is None else str(committed)
    stretch_text = "TBD" if stretch is None else str(stretch)
    return f"{committed_text} / {stretch_text}"


def render_capability_readme(capability: dict, training: dict, evaluation: dict) -> str:
    lead = capability["lead"] or "Unassigned"
    lines = [
        f"# {capability['title']}",
        "",
        f"**Priority:** {capability['priority']}  ",
        f"**State:** {capability['state']}  ",
        f"**Lead:** {lead}  ",
        f"**Release decision:** {capability['release_decision']}",
        "",
        capability["scope"],
        "",
        f"**Model promise:** {capability['promise']}",
        "",
        "## Training route",
        "",
    ]
    lines.extend(f"- {item}" for item in capability["training_route"])
    lines.extend([
        "",
        "## Training data decisions",
        "",
        "| Source | Decision | Trainable | Stage(s) | Role |",
        "| --- | --- | --- | --- | --- |",
    ])
    for source in training["sources"]:
        if source.get("catalogue_entry"):
            source_label = f"[{source['name']}](../../{source['catalogue_entry']})"
        elif source.get("source_url"):
            source_label = f"[{source['name']}]({source['source_url']})"
        else:
            source_label = source["name"]
        stages = ", ".join(source["stages"]) or "—"
        roles = ", ".join(source["roles"])
        lines.append(
            f"| {source_label} | `{source['decision']}` | "
            f"{'yes' if source['trainable'] else 'no'} | {stages} | {roles} |"
        )
    lines.extend([
        "",
        "See [training-data.json](training-data.json) for source rationale, required gates, language scope, overlap risk, mixing guidance, and gaps.",
        "",
        "## Evaluation plan",
        "",
        "| Suite | Class | Gate eligible | Metric | 9B committed / stretch | 30B committed / stretch |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for suite in evaluation["suites"]:
        if suite.get("source_url"):
            suite_label = f"[{suite['name']}]({suite['source_url']})"
        else:
            suite_label = suite["name"]
        for index, metric in enumerate(suite["metrics"]):
            shown_suite = suite_label if index == 0 else "↳"
            lines.append(
                f"| {shown_suite} | `{suite['gate_class']}` | "
                f"{'yes' if suite['gate_eligible'] else 'no'} | "
                f"{metric['name']} ({metric['operator']}) | "
                f"{target_text(metric['targets']['9b'])} | "
                f"{target_text(metric['targets']['30b'])} |"
            )
    lines.extend([
        "",
        "See [evaluation.json](evaluation.json) for separation evidence, runners, cadence, stress slices, and known gaps.",
        "",
        "## Open gaps",
        "",
    ])
    lines.extend(f"- {gap}" for gap in sorted(set(training["gaps"] + evaluation["gaps"])))
    lines.extend([
        "",
        "## Canonical records",
        "",
        "- [Capability charter](capability.json)",
        "- [Training-data manifest](training-data.json)",
        "- [Evaluation manifest](evaluation.json)",
        f"- [Spreadsheet tab](https://docs.google.com/spreadsheets/d/{capability['spreadsheet']['id']}/edit#gid={capability['spreadsheet']['gid']})",
        "",
        "This page is generated by `python3 scripts/build_capability_indexes.py`; edit the JSON manifests instead.",
        "",
    ])
    return "\n".join(lines)


def render_root_readme(records: list[tuple[dict, dict, dict]]) -> str:
    lines = [
        "# Capability playbooks",
        "",
        "This directory turns the planning spreadsheet into reviewable, machine-readable training and evaluation decisions. It sits above the versioned dataset catalogue: catalogue entries describe artifacts; these playbooks decide how an artifact may be used for a capability and what evidence promotes a checkpoint.",
        "",
        "Every capability folder contains a charter, a training-data manifest, an evaluation manifest, and this generated human view. All evaluation plans inherit the [shared evaluation policy](_shared/evaluation-policy.json), including the protected-evaluation boundary and cross-language regression gates.",
        "",
        "| Capability | Priority | Lead | Training sources | Trainable now | Eval suites | Gate-eligible suites |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for capability, training, evaluation in records:
        lines.append(
            f"| [{capability['title']}]({capability['id']}/README.md) | "
            f"{capability['priority']} | {capability['lead'] or 'Unassigned'} | "
            f"{len(training['sources'])} | {sum(source['trainable'] for source in training['sources'])} | "
            f"{len(evaluation['suites'])} | {sum(suite['gate_eligible'] for suite in evaluation['suites'])} |"
        )
    lines.extend([
        "",
        "## Review workflow",
        "",
        "1. Add or update a versioned catalogue entry before promoting an external source to `use`.",
        "2. Record the capability-specific role, stage, decision, required gates, and overlap risk in `training-data.json`.",
        "3. Freeze evaluation identity and separation evidence before setting `gate_eligible: true`.",
        "4. Record an immutable base-model baseline before treating provisional absolute targets as final.",
        "5. Run `python3 scripts/build_capability_indexes.py` and `python3 scripts/build_indexes.py --check`.",
        "",
        "See [the data model](DATA-MODEL.md), [the target matrix](MATRIX.md), and the [multilingual tier registry](multilingual/language-tiers.json).",
        "",
        "This page is generated by `python3 scripts/build_capability_indexes.py`; edit the JSON manifests instead.",
        "",
    ])
    return "\n".join(lines)


def render_matrix(records: list[tuple[dict, dict, dict]]) -> str:
    lines = [
        "# Capability target matrix",
        "",
        "This generated view collects numeric targets from every evaluation manifest. `TBD` means the metric is structured but needs an immutable base-checkpoint baseline or an approved operating SLO.",
        "",
        "| Capability | Suite | Metric | Direction | 9B committed | 30B committed | Stretch | Gate |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for capability, _training, evaluation in records:
        for suite in evaluation["suites"]:
            for metric in suite["metrics"]:
                nine = metric["targets"]["9b"]
                thirty = metric["targets"]["30b"]
                stretch = thirty["stretch"] if thirty["stretch"] is not None else nine["stretch"]
                lines.append(
                    f"| [{capability['title']}]({capability['id']}/README.md) | {suite['name']} | "
                    f"{metric['name']} | `{metric['operator']}` | "
                    f"{nine['committed'] if nine['committed'] is not None else 'TBD'} | "
                    f"{thirty['committed'] if thirty['committed'] is not None else 'TBD'} | "
                    f"{stretch if stretch is not None else 'TBD'} | "
                    f"{suite['gate_class']}{'' if suite['gate_eligible'] else ' (diagnostic pending separation)'} |"
                )
    lines.extend(["", "Generated from the nine `evaluation.json` manifests.", ""])
    return "\n".join(lines)


def load_and_validate() -> list[tuple[dict, dict, dict]]:
    index_path = CAP_ROOT / "index.json"
    index = load_json(index_path)
    require = {"schema_version", "updated", "capabilities"}
    errors: list[str] = []
    require_fields(index, require, index_path, errors)
    records: list[tuple[dict, dict, dict]] = []
    seen_ids: set[str] = set()

    for item in index.get("capabilities", []):
        capability_id = item.get("id")
        folder = CAP_ROOT / item.get("path", "")
        capability_path = folder / "capability.json"
        training_path = folder / "training-data.json"
        evaluation_path = folder / "evaluation.json"
        try:
            capability = load_json(capability_path)
            training = load_json(training_path)
            evaluation = load_json(evaluation_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        require_fields(capability, {"schema_version", "id", "title", "priority", "state", "scope", "promise", "training_route", "release_decision", "spreadsheet"}, capability_path, errors)
        require_fields(training, {"schema_version", "capability_id", "updated", "selection_principles", "sources", "mixing_guidance", "gaps"}, training_path, errors)
        require_fields(evaluation, {"schema_version", "capability_id", "updated", "inherits", "suites", "stress_slices", "gaps"}, evaluation_path, errors)
        if not capability_id or capability_id in seen_ids:
            errors.append(f"{index_path.relative_to(ROOT)}: duplicate or empty capability id {capability_id!r}")
        seen_ids.add(capability_id)
        if capability.get("id") != capability_id or training.get("capability_id") != capability_id or evaluation.get("capability_id") != capability_id:
            errors.append(f"{folder.relative_to(ROOT)}: capability ids do not agree with index")
        if item.get("priority") != capability.get("priority"):
            errors.append(f"{folder.relative_to(ROOT)}: priority does not agree with index")

        trainable_catalogue: set[str] = set()
        source_ids: set[str] = set()
        for source in training.get("sources", []):
            require_fields(source, {"id", "name", "source_kind", "decision", "trainable", "stages", "roles", "language_scope", "reason", "required_gates", "eval_overlap_risk"}, training_path, errors)
            source_id = source.get("id")
            if source_id in source_ids:
                errors.append(f"{training_path.relative_to(ROOT)}: duplicate source id {source_id!r}")
            source_ids.add(source_id)
            decision = source.get("decision")
            if decision not in TRAINING_DECISIONS:
                errors.append(f"{training_path.relative_to(ROOT)}: invalid decision {decision!r}")
            if source.get("trainable") and decision in {"hold", "exclude"}:
                errors.append(f"{training_path.relative_to(ROOT)}: {source_id} is trainable but decision is {decision}")
            if decision == "use" and not source.get("catalogue_entry"):
                errors.append(f"{training_path.relative_to(ROOT)}: external source {source_id} cannot be `use` before catalogue nomination")
            _, metadata = validate_catalogue_link(source.get("catalogue_entry"), training_path, errors)
            if metadata and metadata.get("status_key") == "eval-only" and source.get("trainable"):
                errors.append(f"{training_path.relative_to(ROOT)}: evaluation-only catalogue source {source_id} cannot be trainable")
            if source.get("trainable") and source.get("catalogue_entry"):
                trainable_catalogue.add(source["catalogue_entry"])

        suite_ids: set[str] = set()
        for suite in evaluation.get("suites", []):
            require_fields(suite, {"id", "name", "type", "primary", "gate_class", "gate_eligible", "separation_evidence", "runner", "language_scope", "metrics", "cadence"}, evaluation_path, errors)
            suite_id = suite.get("id")
            if suite_id in suite_ids:
                errors.append(f"{evaluation_path.relative_to(ROOT)}: duplicate suite id {suite_id!r}")
            suite_ids.add(suite_id)
            if suite.get("gate_class") not in GATE_CLASSES:
                errors.append(f"{evaluation_path.relative_to(ROOT)}: invalid gate class for {suite_id}")
            if not suite.get("separation_evidence", "").strip():
                errors.append(f"{evaluation_path.relative_to(ROOT)}: {suite_id} lacks separation evidence")
            if not suite.get("metrics"):
                errors.append(f"{evaluation_path.relative_to(ROOT)}: {suite_id} has no metrics")
            validate_catalogue_link(suite.get("catalogue_entry"), evaluation_path, errors)
            if suite.get("gate_eligible") and suite.get("catalogue_entry") in trainable_catalogue:
                errors.append(f"{evaluation_path.relative_to(ROOT)}: gate-eligible suite {suite_id} reuses trainable catalogue entry")
            for metric in suite.get("metrics", []):
                require_fields(metric, {"id", "name", "unit", "direction", "operator", "targets"}, evaluation_path, errors)
                targets = metric.get("targets", {})
                if set(targets) != {"9b", "30b"}:
                    errors.append(f"{evaluation_path.relative_to(ROOT)}: {suite_id}/{metric.get('id')} must define 9b and 30b")
                for size, target in targets.items():
                    if not isinstance(target, dict) or set(target) != {"committed", "stretch"}:
                        errors.append(f"{evaluation_path.relative_to(ROOT)}: {suite_id}/{metric.get('id')}/{size} needs committed and stretch")

        records.append((capability, training, evaluation))

    if len(records) != len(index.get("capabilities", [])):
        errors.append("capabilities/index.json: one or more capability records could not be loaded")
    if errors:
        raise ValueError("\n".join(errors))
    return records


def expected_outputs(records: list[tuple[dict, dict, dict]]) -> dict[Path, str]:
    result = {
        CAP_ROOT / "README.md": render_root_readme(records),
        CAP_ROOT / "MATRIX.md": render_matrix(records),
    }
    for capability, training, evaluation in records:
        result[CAP_ROOT / capability["id"] / "README.md"] = render_capability_readme(capability, training, evaluation)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated views are stale")
    args = parser.parse_args()
    try:
        records = load_and_validate()
        outputs = expected_outputs(records)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    stale: list[str] = []
    for path, content in outputs.items():
        normalized = content.rstrip() + "\n"
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != normalized:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(normalized, encoding="utf-8")
    if stale:
        print("Stale generated capability views:\n" + "\n".join(stale), file=sys.stderr)
        return 1
    print(f"Validated {len(records)} capabilities and {len(outputs)} generated views.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
