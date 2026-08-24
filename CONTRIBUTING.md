# Contributing

Keep entries useful to someone deciding whether a dataset can enter a real post-training run. Prefer immutable revisions, concrete locations, reproducible counts, commands, limitations, and evidence over general descriptions.

Read [catalogue conventions](CATALOGUE-CONVENTIONS.md) and the [dataset ingestion workflow](DATASET-INGESTION.md) before adding a source.

## Nominate and add a dataset

1. Open a dataset-nomination issue and agree the intended scope, owner, lifecycle, and evaluation-contamination boundary.
2. Choose `<dataset>/<version>/README.md`. Reuse a pinned upstream semantic version; use `0.0.0` when no stable version has been selected.
3. Copy `etc/skeleton.md` into the versioned path.
4. Complete the JSON frontmatter and all canonical sections. Preserve unknown measurements as `null`, never zero.
5. Use ISO 639-3 plus ISO 15924 language identifiers from [LANGUAGES.md](LANGUAGES.md).
6. Run `python3 scripts/build_indexes.py`.
7. Run `python3 scripts/build_indexes.py --check`.
8. Open a pull request and link the nomination issue and supporting evidence.

Do not edit generated pages under `training-types/`, `languages/`, `status/`, or `catalogue-status/` by hand.

## Update a capability playbook

The canonical capability records are the JSON manifests under `capabilities/<capability>/`:

- update `capability.json` when scope, priority, lead, or release-decision class changes;
- update `training-data.json` when a source is nominated, promoted, held, or excluded for that capability; and
- update `evaluation.json` when a benchmark, target, separation boundary, cadence, or release gate changes.

External sources cannot be promoted to `use` before a versioned catalogue
entry records provenance, immutable revision, terms, quality evidence, and the
evaluation-contamination boundary. Evaluation-only entries and all prompt,
answer, translation, paraphrase, retrieval, and synthetic derivatives remain
outside training and calibration.

Run `python3 scripts/build_capability_indexes.py` to regenerate the capability
README files and target matrix. Do not edit those generated Markdown views by
hand. Then run both `--check` commands before opening a pull request.

## Update a dataset

Update the current version when a statement is clarified without changing the identity of the artifact. Add a new version when the selected upstream release, split, transformation, schema, tokenizer, filtering policy, or protected-evaluation boundary changes materially.

Update an entry when any of these change:

- a public or project-storage location is added, moved, or removed;
- a dataset is used in a completed or research run;
- licensing, redistribution, commercial-use, or access information becomes clearer;
- a canonical revision, configuration, split, tokenizer, or derived artifact is selected;
- normalized bytes/documents/segments/characters/tokens are reproduced;
- a quality, contamination, privacy, safety, or language-balance check is completed;
- a candidate becomes production-ready; or
- a version is deprecated or superseded.

Never silently rewrite published provenance. If an artifact's identity changes, create a new version and retain the old entry as `E` when it remains useful for reproducibility.

## Catalogue lifecycle

Use one `catalogue_status` value:

- `D` — draft entry;
- `P` — published entry; or
- `E` — deprecated entry retained for provenance.

This status describes the catalogue page, not approval for training.

## Operational state

Use one `status_key` value:

- `used-in-completed-run`
- `used-in-research`
- `published`
- `configured-runnable`
- `staged`
- `candidate`
- `planned`
- `supporting`
- `needs-verification`
- `historical`
- `eval-only`

“Used” requires evidence of the run. “Staged” means a concrete artifact was inspected. “Published” means others can obtain the data. None of these implies legal, privacy, safety, quality, contamination, or production approval.

Evaluation-only sources must use `eval-only`, include the `evaluation-holdouts` training type, say **never train** prominently, and describe the decontamination controls for prompts, answers, translations, paraphrases, retrieval sources, and synthetic derivatives.

## Statistics and formats

- Record byte, document, segment, character, and token totals as non-negative integers only after reproducing them.
- Name the canonical content field and what “document” and “segment” mean for the artifact.
- Use the common catalogue tokenizer, currently Gemma 3, for normalized token counts and pin its revision. Label training-tokenizer counts separately.
- Prefer a UTF-8 JSON Lines plus Zstandard interchange artifact where a row-based representation fits.
- Document Parquet, conversation JSONL, Megatron `.bin`/`.idx`, preference, verifier, packed-context, and other training-specific derivatives separately.
- Record checksums and the transformation command/commit for production artifacts.

## Locations

- Link public data directly and pin immutable revisions.
- Put LUMI and other filesystem paths in backticks.
- Never commit credentials or signed download URLs.
- Record the date on which a location was last verified.
- If an artifact exists in a personal directory, identify the responsible owner and intended shared destination.

## Update the training plan

Training-stage pages are hand-maintained under `training-plan/`. When changing a proposed mixture or gate:

- state whether it is confirmed, runnable, proposed, or blocked;
- link the exact versioned dataset entries and evidence;
- distinguish completed-run hyperparameters from pilot suggestions;
- update `training-plan/DATA_GAPS.md` when a blocker is opened or closed;
- update `training-plan/LANGUAGE_COVERAGE.md` when capability depth changes;
- run the catalogue check, which also validates relative Markdown links; and
- include the evaluation evidence required by the stage's exit gate.
