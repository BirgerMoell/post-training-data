---
name: "birgermoell/oellm-eu-eval-holdouts-v1"
slug: "birgermoell-oellm-eu-eval-holdouts-v1"
version: "0.0.0"
catalogue_status: "P"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Eval-only — do not train"
language_keys: ["multilingual"]
language_codes: []
languages: "38 languages"
purpose: "Canary post-training evaluation"
source_type: "HF dataset"
priority: "N/A"
curator: "Birger"
license_access: "CC0-1.0"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-eval-holdouts-v1"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-06-22"
confidence: "High"
source_sheet_row: 106
---

# birgermoell/oellm-eu-eval-holdouts-v1

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Eval-only — do not train  
> **Training use:** evaluation-holdouts  
> **Recorded languages:** 38 languages

## <a id="background">Background</a>

Canary post-training evaluation

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-eval-holdouts-v1>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Synthetic canary eval
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EVAL_HOLDOUTS.md>)
- **Seed inventory:** [Data tab, row 106](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A106:Q106>)

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
| License and access | CC0-1.0 |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: 38 languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/birgermoell/oellm-eu-eval-holdouts-v1>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 106](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A106:Q106>)
- **Last verified:** 2026-06-22
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

CC0-1.0

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Keep this resource out of training, retrieval augmentation, data generation prompts, and model-selection feedback loops.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** N/A
- **License / access:** CC0-1.0
- **Last verified:** 2026-06-22
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

**Protected evaluation artifact: never use for training.** Keep all prompts, answers, translations, and derived variants out of SFT, preference, RLVR, continued-pretraining, RAG, and synthetic-data generation inputs. Add stable identifiers and content hashes to the decontamination registry before every training freeze.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Exclude from training, RAG, tuning and generation prompts.
