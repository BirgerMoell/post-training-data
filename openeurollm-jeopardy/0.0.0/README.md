---
name: "openeurollm/jeopardy"
slug: "openeurollm-jeopardy"
version: "0.0.0"
catalogue_status: "P"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Evaluation-only — do not train"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "en"
purpose: "2,117-example continuation evaluation set"
source_type: "Hugging Face evaluation dataset"
priority: "Unset"
curator: "OpenEuroLLM evaluation team"
license_access: "Public; dataset card does not currently declare a license"
public_location: "https://huggingface.co/datasets/openeurollm/jeopardy"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 through the Hugging Face API"
confidence: "High"
source_sheet_row: null
---

# openeurollm/jeopardy

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Evaluation-only — do not train  
> **Training use:** evaluation-holdouts  
> **Recorded languages:** en

## <a id="background">Background</a>

An OpenEuroLLM evaluation artifact with 2,117 test examples and the fields
`context`, `continuation`, and `category`. It is useful for checkpoint
comparison and must remain outside every training and synthetic-generation
input.

## <a id="sources">Data Sources</a>

- **Public source:** [Hugging Face](https://huggingface.co/datasets/openeurollm/jeopardy)
- **Pinned revision observed 2026-08-18:** `42adb432a2a623f16ed66a8d002a810664255224`
- **LUMI artifact:** Not recorded

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
| License and access | Public; dataset card does not currently declare a license |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openeurollm/jeopardy>)
- **LUMI or project artifact:** Not recorded
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Public; dataset card does not currently declare a license

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Load only the `test` split. Add its prompts and continuations to the
decontamination index before freezing any SFT, DPO, or RL data. Report the
exact revision and scoring method with results.

### Operational state and ownership

- **Owner / lead:** OpenEuroLLM evaluation team
- **Source type:** Hugging Face evaluation dataset
- **License / access:** Public; dataset card does not currently declare a license
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

**Protected evaluation artifact: never use for training.** Keep all prompts, answers, translations, and derived variants out of SFT, preference, RLVR, continued-pretraining, RAG, and synthetic-data generation inputs. Add stable identifiers and content hashes to the decontamination registry before every training freeze.

## <a id="curator">Catalogue Curator</a>

OpenEuroLLM evaluation team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Document the canonical metric and connect it to the common checkpoint gate.
