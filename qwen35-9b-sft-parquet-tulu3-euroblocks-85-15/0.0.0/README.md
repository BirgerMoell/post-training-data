---
name: "qwen35-9b-sft-parquet (tulu3-euroblocks-85-15)"
slug: "qwen35-9b-sft-parquet-tulu3-euroblocks-85-15"
version: "0.0.0"
catalogue_status: "P"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en","multilingual"]
language_codes: ["eng_Latn"]
languages: "EU multilingual + en"
purpose: "Main EU instruction mix + English replay"
source_type: "Derived LUMI artifact"
priority: "P1"
curator: "Birger Moëll"
license_access: "Mixed upstream; review"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-sft-parquet/train.parquet"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "High"
source_sheet_row: 5
---

# qwen35-9b-sft-parquet (tulu3-euroblocks-85-15)

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** instruction-sft  
> **Recorded languages:** EU multilingual + en

## <a id="background">Background</a>

Main EU instruction mix + English replay

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-sft-parquet/train.parquet`
- **Upstream / parent:** EuroBlocks + Tülu-3
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/model_cards/qwen35-9b-eu-sft-README.md>)
- **Seed inventory:** [Data tab, row 5](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A5:Q5>)

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
| License and access | Mixed upstream; review |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: EU multilingual + en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml>)
- **LUMI or project artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-sft-parquet/train.parquet`
- **Source register:** [Data register row 5](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A5:Q5>)
- **Last verified:** 2026-08-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed upstream; review

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger Moëll
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Mixed upstream; review
- **Last verified:** 2026-08-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger Moëll

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

~1.08M examples; completed 9B proof run. Preserve exact manifest and weights.
