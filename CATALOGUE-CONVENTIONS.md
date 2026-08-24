# Catalogue conventions

This repository follows the structure of the [OpenEuroLLM training-data catalogue](https://github.com/OpenEuroLLM/training-data-catalogue) while adding fields needed to make post-training decisions. The alignment baseline is official catalogue commit [`2f3bdf8`](https://github.com/OpenEuroLLM/training-data-catalogue/commit/2f3bdf8457d76cf032440b76a3dc86ea69c72405), inspected on 2026-08-24.

## Shared conventions

| Convention | Rule in this repository |
| --- | --- |
| Entry path | `<dataset>/<version>/README.md` |
| Initial version | Use the exact upstream release when it is pinned; otherwise use `0.0.0` |
| Catalogue lifecycle | `D` draft, `P` published, `E` deprecated |
| Required sections | Background, Data Sources, Structure & Statistics, Available Metadata, European Language Support, Access Information, Terms of Use, and Catalogue Curator |
| Language identifiers | ISO 639-3 plus ISO 15924, such as `swe_Latn` and `ell_Grek` |
| Comparable statistics | Bytes, documents, segments, characters, and tokens |
| Interchange format | UTF-8 JSON Lines compressed with Zstandard where a row-based canonical export is appropriate |
| Contribution path | Nomination issue, scoped ingestion, versioned entry, generated-index check, pull request |

## Catalogue lifecycle versus operational readiness

The official D/P/E lifecycle describes the documentation entry. The spreadsheet states describe the underlying artifact and its use in the post-training programme. They answer different questions and must not be collapsed.

| Catalogue lifecycle | Meaning | Current default mapping |
| --- | --- | --- |
| `D` — Draft | Entry is incomplete, proposed, or awaiting verification | `candidate`, `planned`, `needs-verification` |
| `P` — Published | Entry is available as reviewed catalogue documentation | `used-in-completed-run`, `used-in-research`, `published`, `configured-runnable`, `staged`, `supporting`, `eval-only` |
| `E` — Deprecated | Entry remains for provenance but should not be selected by default | `historical` |

Publishing an entry does not approve the data for training. License/access, privacy, safety, quality, language balance, contamination, and reproducibility gates remain separate. An `eval-only` entry can be `P` because its exclusion requirements are published and must be visible.

## Version policy

- Reuse a stable upstream semantic version only when the exact release is selected and documented.
- Use `0.0.0` when the upstream source is rolling, the revision is unpinned, the entry represents a local artifact without a release, or the exact version still needs verification.
- Do not silently replace a published version. Add `<dataset>/<new-version>/README.md`, update its evidence, and deprecate the superseded entry when appropriate.
- Pin immutable source revisions, configurations, splits, tokenizer revisions, transformation commits, and checksums in the entry before a flagship run.

All 114 entries were migrated to `0.0.0` because the seed register did not consistently pin upstream releases. The version directory therefore records catalogue honesty, not a claim that every upstream dataset calls itself version 0.0.0.

## Post-training extensions

Every entry retains the spreadsheet fields needed for run planning:

- training type and intended capability;
- operational status, priority, owner/curator, and confidence;
- public and LUMI/project locations;
- license/access state and last verification date;
- spreadsheet source row when one exists; and
- quality, safety, evaluation-exclusion, and next-action guidance.

Generated views under `training-types/`, `languages/`, `status/`, and `catalogue-status/` are navigation aids. The versioned entry is authoritative.

## Statistics and token counts

Use integers for normalized statistics. `null` means not measured or not reproducibly verified; it must never be read as zero.

- **Bytes:** uncompressed UTF-8 payload bytes for the canonical content field or clearly documented artifact bytes.
- **Documents:** independently sourced documents or top-level records.
- **Segments:** training records after segmentation, conversation extraction, or packing, with the exact unit documented.
- **Characters:** Unicode character count for the canonical text representation.
- **Tokens:** count under the common catalogue tokenizer, currently Gemma 3. Record its immutable revision. Training-tokenizer counts may be added as clearly labelled post-training evidence, but must not replace the comparable catalogue total.

Post-training formats can include conversation JSONL, Parquet, Megatron `.bin`/`.idx`, preference pairs, verifier records, or task-specific bundles. Keep a canonical row-based manifest/export where feasible, and document every derived training artifact separately.

## Deliberate repository additions

The official catalogue focuses on normalized pretraining corpora. This repository additionally includes:

- derived and tokenized training artifacts;
- preference, reasoning, tool-use, RLVR, and long-context sources;
- filtering and decontamination resources;
- protected evaluation holdouts, explicitly marked never to train; and
- a stage-by-stage training plan.

These additions preserve post-training decision context without changing the official entry topology or lifecycle vocabulary.
