---
name: "qwen35-9b-reasoning-sft-parquet"
slug: "qwen35-9b-reasoning-sft-parquet"
version: "0.0.0"
catalogue_status: "P"
training_types: ["reasoning-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en","fi"]
language_codes: ["eng_Latn","fin_Latn"]
languages: "en,fi"
purpose: "Math/reasoning mix used in EU recipes"
source_type: "Derived LUMI artifact"
priority: "P1"
curator: "Birger"
license_access: "Internal derivative"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b_reasoning.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-reasoning-sft-parquet/train.parquet"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "High"
source_sheet_row: 23
---

# qwen35-9b-reasoning-sft-parquet

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** reasoning-sft  
> **Recorded languages:** en,fi

## <a id="background">Background</a>

Math/reasoning mix used in EU recipes

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b_reasoning.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-reasoning-sft-parquet/train.parquet`
- **Upstream / parent:** Nemotron math + Finnish distilled math
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_run2_data.py>)
- **Seed inventory:** [Data tab, row 23](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A23:Q23>)

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
| License and access | Internal derivative |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |
| `fin_Latn` | — | — | — | — | — |

Recorded coverage: en,fi

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b_reasoning.yaml>)
- **LUMI or project artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-reasoning-sft-parquet/train.parquet`
- **Source register:** [Data register row 23](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A23:Q23>)
- **Last verified:** 2026-08-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Internal derivative

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Internal derivative
- **Last verified:** 2026-08-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Pin build revision, row counts and lineage.
