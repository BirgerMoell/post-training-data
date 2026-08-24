---
name: "EuroBlocks-SFT-Synthetic-1124"
slug: "euroblocks-sft-synthetic-1124"
version: "0.0.0"
catalogue_status: "P"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
language_codes: []
languages: "EU multilingual"
purpose: "EU-language instruction backbone"
source_type: "LUMI shared dataset"
priority: "P1"
curator: "T4.6 / Birger"
license_access: "Internal/shared; license manifest needed"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/multiling/EuroBlocks-SFT-Synthetic-1124"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "High"
source_sheet_row: 6
---

# EuroBlocks-SFT-Synthetic-1124

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** instruction-sft  
> **Recorded languages:** EU multilingual

## <a id="background">Background</a>

EU-language instruction backbone

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/multiling/EuroBlocks-SFT-Synthetic-1124`
- **Upstream / parent:** EuroBlocks synthetic
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml>)
- **Seed inventory:** [Data tab, row 6](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A6:Q6>)

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
| License and access | Internal/shared; license manifest needed |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: EU multilingual

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/multiling/EuroBlocks-SFT-Synthetic-1124`
- **Source register:** [Data register row 6](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A6:Q6>)
- **Last verified:** 2026-08-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Internal/shared; license manifest needed

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** T4.6 / Birger
- **Source type:** LUMI shared dataset
- **Priority:** P1
- **License / access:** Internal/shared; license manifest needed
- **Last verified:** 2026-08-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6 / Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

161k rows used; verify canonical upstream ID and terms.
