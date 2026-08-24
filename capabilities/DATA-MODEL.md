# Capability data model

This directory is the decision layer above the versioned dataset catalogue. The catalogue records what an artifact is; a capability manifest records why it may enter a specific training recipe and how the resulting model is judged.

Each capability has three canonical files:

- `capability.json` — scope, promise, priority, lead, lifecycle, and release-decision type;
- `training-data.json` — source-by-source decisions, stages, roles, language scope, quality gates, and evaluation-overlap risk; and
- `evaluation.json` — protected and public suites, metric direction, 9B/30B/stretch targets, cadence, and known gaps.

The JSON files are canonical. The generated `README.md` files are review views. Dataset metadata remains canonical in `<dataset>/<version>/README.md`; manifests link to it rather than duplicating sizes, licenses, or locations.

## Decision semantics

Training-source decisions progress as `hold` → `candidate` → `pilot` → `use`. `exclude` is terminal unless new evidence changes the decision. External sources cannot be marked `use` until they have a catalogue entry with pinned revision, terms, provenance, quality results, and an explicit contamination boundary.

`trainable: false` is required for red-team discovery corpora, protected evaluation, unresolved-license sources, and sources being tracked only as evidence. A source with `eval_overlap_risk: prohibited` must never enter training, retrieval augmentation during evaluation, prompt generation, translation, paraphrasing, or synthetic-data derivation.

## Evaluation semantics

`gate_eligible` describes whether a particular suite can decide promotion. It is separate from `primary`: a public benchmark may be a primary headline metric while remaining diagnostic after overlap. `release` and `non-compensatory` gates can block promotion; `headline` measures the model promise; `diagnostic` localizes regressions.

All capabilities inherit [_shared/evaluation-policy.json](_shared/evaluation-policy.json). In particular, the model must improve on the declared parent, no priority language may lose more than two points, and reports must expose macro, p10, and minimum-language results.

## Adding information

1. Add or update the versioned dataset catalogue entry first.
2. Reference that exact path from one or more `training-data.json` files.
3. Record the intended stage and role; do not infer approval from catalogue lifecycle.
4. Add the evaluation suite and its separation evidence before setting `gate_eligible: true`.
5. Run `python3 scripts/build_capability_indexes.py` and both repository checks.

Unassigned leads stay `null`; unknown targets stay `null`. Do not encode guesses as owners or zeroes.
