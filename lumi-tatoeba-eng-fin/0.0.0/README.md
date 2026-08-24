---
name: "Tatoeba MT Challenge English–Finnish holdout on LUMI"
slug: "lumi-tatoeba-eng-fin"
version: "0.0.0"
catalogue_status: "P"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Evaluation-only — do not train"
language_keys: ["en","fi"]
language_codes: ["eng_Latn","fin_Latn"]
languages: "English, Finnish"
purpose: "English–Finnish translation and retention evaluation"
source_type: "Versioned local evaluation package"
priority: "P1 protected holdout"
curator: "Evaluation team"
license_access: "CC-BY-NC-SA-4.0 as recorded in the local README"
public_location: "https://github.com/Helsinki-NLP/Tatoeba-Challenge"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Tatoeba/eng-fin"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 by direct LUMI inspection"
confidence: "High"
source_sheet_row: null
---

# Tatoeba MT Challenge English–Finnish holdout on LUMI

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Evaluation-only — do not train  
> **Training use:** evaluation-holdouts  
> **Recorded languages:** English, Finnish

## <a id="background">Background</a>

A small, versioned English–Finnish translation check that complements broad
FLORES evaluation and can detect Finnish regressions after SFT or preference
optimization. The local directory contains only dev/test artifacts, which
should stay protected.

## <a id="sources">Data Sources</a>

- **Upstream:** [Helsinki-NLP/Tatoeba-Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge)
- **Local package:** `eng-fin`, version `v2023-09-26`, based on Tatoeba corpus `v2023-04-12`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Tatoeba/eng-fin`
- **Dev:** `dev.src` 2,303,326 bytes; `dev.trg` 2,565,292 bytes
- **Test:** `test.src` 401,576 bytes; `test.trg` 444,385 bytes
- **Evidence:** Local `README.md` and direct read-only inspection on 2026-08-18

## <a id="statistics">Structure & Statistics</a>

The normalized totals below have not yet been entered for this catalogue version. Source-specific figures in the evidence section remain useful, but should not be treated as comparable catalogue totals until reproduced.

| Measure | Value |
| --- | ---: |
| Bytes | — |
| Documents | — |
| Segments | — |
| Characters | — |
| Tokens | — |
| Data format | Not normalized |
| Compression | Not normalized |

## <a id="metadata">Available Metadata</a>

| Field | Status |
| --- | --- |
| Identity and intended post-training use | Recorded in this entry |
| Public and project-storage locations | Recorded when known; verify before use |
| Operational owner, priority, and confidence | Recorded from the project data register or repository evidence |
| Schema, columns, and splits | See source and structure evidence; inventory if absent |
| Immutable revision and checksums | Required for a production manifest; may still be missing |
| License and access | CC-BY-NC-SA-4.0 as recorded in the local README |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |
| `fin_Latn` | — | — | — | — | — |

Recorded coverage: English, Finnish

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://github.com/Helsinki-NLP/Tatoeba-Challenge>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/Tatoeba/eng-fin`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

CC-BY-NC-SA-4.0 as recorded in the local README

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Freeze the paired IDs and infer direction from `langids` rather than assuming
all rows have the same source language. Score both English-to-Finnish and
Finnish-to-English when supported, report paired-bootstrap confidence, and add
both sides to the decontamination index. Never use these dev/test files for
training, demonstrations, or synthetic generation.

### Operational state and ownership

- **Owner / lead:** Evaluation team
- **Source type:** Versioned local evaluation package
- **Priority:** P1 protected holdout
- **License / access:** CC-BY-NC-SA-4.0 as recorded in the local README
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

**Protected evaluation artifact: never use for training.** Keep all prompts, answers, translations, and derived variants out of SFT, preference, RLVR, continued-pretraining, RAG, and synthetic-data generation inputs. Add stable identifiers and content hashes to the decontamination registry before every training freeze.

## <a id="curator">Catalogue Curator</a>

Evaluation team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Add a pinned scoring command and baseline scores for the approved Prelude base.
