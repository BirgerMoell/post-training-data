---
name: "Finnish DeepSeek-distilled math corpus"
slug: "finnish-deepseek-distilled-math-corpus"
version: "0.0.0"
catalogue_status: "P"
training_types: ["reasoning-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["fi"]
language_codes: ["fin_Latn"]
languages: "fi"
purpose: "Finnish reasoning component"
source_type: "LUMI shared dataset"
priority: "P1"
curator: "Birger / Finnish team"
license_access: "Exact upstream/license needs manifest"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/fin"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "Medium"
source_sheet_row: 27
---

# Finnish DeepSeek-distilled math corpus

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** reasoning-sft  
> **Recorded languages:** fi

## <a id="background">Background</a>

Finnish reasoning component

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/fin`
- **Upstream / parent:** Finnish-NLP / distilled math
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_run2_data.py>)
- **Seed inventory:** [Data tab, row 27](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A27:Q27>)

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
| License and access | Exact upstream/license needs manifest |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `fin_Latn` | — | — | — | — | — |

Recorded coverage: fi

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/fin`
- **Source register:** [Data register row 27](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A27:Q27>)
- **Last verified:** 2026-08-11
- **Confidence:** Medium

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Exact upstream/license needs manifest

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger / Finnish team
- **Source type:** LUMI shared dataset
- **Priority:** P1
- **License / access:** Exact upstream/license needs manifest
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger / Finnish team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Resolve file-level source IDs.
