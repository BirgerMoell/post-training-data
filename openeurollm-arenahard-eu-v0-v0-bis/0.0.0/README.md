---
name: "openeurollm/ArenaHard-EU-v0 / v0-bis"
slug: "openeurollm-arenahard-eu-v0-v0-bis"
version: "0.0.0"
catalogue_status: "P"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Eval-only — do not train"
language_keys: ["multilingual"]
language_codes: []
languages: "European languages"
purpose: "Arena-style EU evaluation"
source_type: "HF family"
priority: "N/A"
curator: "Evaluation team"
license_access: "Public; eval only"
public_location: "https://huggingface.co/datasets/openeurollm/ArenaHard-EU-v0"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "High"
source_sheet_row: 107
---

# openeurollm/ArenaHard-EU-v0 / v0-bis

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Eval-only — do not train  
> **Training use:** evaluation-holdouts  
> **Recorded languages:** European languages

## <a id="background">Background</a>

Arena-style EU evaluation

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/ArenaHard-EU-v0>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** ArenaHard EU
- **Evidence:** [evidence](<https://huggingface.co/datasets/openeurollm/ArenaHard-EU-v0>)
- **Seed inventory:** [Data tab, row 107](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A107:Q107>)

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
| License and access | Public; eval only |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: European languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openeurollm/ArenaHard-EU-v0>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 107](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A107:Q107>)
- **Last verified:** 2026-08-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Public; eval only

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Keep this resource out of training, retrieval augmentation, data generation prompts, and model-selection feedback loops.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** Evaluation team
- **Source type:** HF family
- **Priority:** N/A
- **License / access:** Public; eval only
- **Last verified:** 2026-08-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

**Protected evaluation artifact: never use for training.** Keep all prompts, answers, translations, and derived variants out of SFT, preference, RLVR, continued-pretraining, RAG, and synthetic-data generation inputs. Add stable identifiers and content hashes to the decontamination registry before every training freeze.

## <a id="curator">Catalogue Curator</a>

Evaluation team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Keep out of training and model-selection leaks.
