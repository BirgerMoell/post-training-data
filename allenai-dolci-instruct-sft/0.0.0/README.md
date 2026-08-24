---
name: "allenai/Dolci-Instruct-SFT"
slug: "allenai-dolci-instruct-sft"
version: "0.0.0"
catalogue_status: "P"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "primarily en"
purpose: "Reference SFT and OLMo 3 reproduction"
source_type: "HF dataset"
priority: "P1"
curator: "T4.6"
license_access: "Public; verify components"
public_location: "https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/Dolci-Instruct-SFT"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-05"
confidence: "High"
source_sheet_row: 8
---

# allenai/Dolci-Instruct-SFT

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** instruction-sft  
> **Recorded languages:** primarily en

## <a id="background">Background</a>

Reference SFT and OLMo 3 reproduction

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/Dolci-Instruct-SFT`
- **Upstream / parent:** Dolci
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/335>)
- **Seed inventory:** [Data tab, row 8](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A8:Q8>)

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
| License and access | Public; verify components |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: primarily en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/Dolci-Instruct-SFT`
- **Source register:** [Data register row 8](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A8:Q8>)
- **Last verified:** 2026-08-05
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Public; verify components

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Public; verify components
- **Last verified:** 2026-08-05
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Reference corpus for reproduced SFT pipeline.
