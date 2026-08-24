---
name: "THUDM/LongAlign-10k"
slug: "thudm-longalign-10k"
version: "0.0.0"
catalogue_status: "D"
training_types: ["long-context-extension"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "primarily en"
purpose: "Long instruction alignment"
source_type: "HF/LUMI dataset"
priority: "P2"
curator: "T4.6"
license_access: "Verify card"
public_location: "https://huggingface.co/datasets/THUDM/LongAlign-10k"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/LongAlign-10k"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "High"
source_sheet_row: 86
---

# THUDM/LongAlign-10k

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Candidate  
> **Training use:** long-context-extension  
> **Recorded languages:** primarily en

## <a id="background">Background</a>

Long instruction alignment

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/THUDM/LongAlign-10k>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/LongAlign-10k`
- **Upstream / parent:** LongAlign
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 86](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A86:Q86>)

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
| License and access | Verify card |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: primarily en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/THUDM/LongAlign-10k>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/LongAlign-10k`
- **Source register:** [Data register row 86](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A86:Q86>)
- **Last verified:** 2026-08-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Verify card

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** T4.6
- **Source type:** HF/LUMI dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Compare with ChatQA2 and native EU tasks.
