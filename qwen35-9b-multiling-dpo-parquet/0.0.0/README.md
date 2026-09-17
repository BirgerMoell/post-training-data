---
name: "qwen35-9b-multiling-dpo-parquet"
slug: "qwen35-9b-multiling-dpo-parquet"
version: "0.0.0"
catalogue_status: "D"
training_types: ["preference-optimization"]
status_key: "needs-verification"
status: "Needs verification"
language_keys: ["fi","sv","da","no","is","multilingual"]
language_codes: ["fin_Latn","swe_Latn","dan_Latn","nor_Latn","nno_Latn","nob_Latn","isl_Latn"]
languages: "fi,sv,da,no,is + multilingual"
purpose: "Nordic/multilingual DPO mix"
source_type: "Derived LUMI artifact"
priority: "P1"
curator: "Birger"
license_access: "Source manifest required"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b_multilingual.yaml"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-09-17 on LUMI; recorded artifact missing"
confidence: "High"
source_sheet_row: 40
---

# qwen35-9b-multiling-dpo-parquet

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Needs verification
> **Training use:** preference-optimization  
> **Recorded languages:** fi,sv,da,no,is + multilingual

## <a id="background">Background</a>

Nordic/multilingual DPO mix

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b_multilingual.yaml>)
- **Recorded artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-multiling-dpo-parquet/train.parquet` (not found on 2026-09-17)
- **Upstream / parent:** LUMI DPOTrainer_format
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_run2_data.py>)
- **Seed inventory:** [Data tab, row 40](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A40:Q40>)

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
| License and access | Source manifest required |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `fin_Latn` | — | — | — | — | — |
| `swe_Latn` | — | — | — | — | — |
| `dan_Latn` | — | — | — | — | — |
| `nor_Latn` | — | — | — | — | — |
| `nno_Latn` | — | — | — | — | — |
| `nob_Latn` | — | — | — | — | — |
| `isl_Latn` | — | — | — | — | — |

Recorded coverage: fi,sv,da,no,is + multilingual

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b_multilingual.yaml>)
- **LUMI or project artifact:** Not currently available. The previously
  recorded path did not exist on 2026-09-17.
- **Source register:** [Data register row 40](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A40:Q40>)
- **Last verified:** 2026-09-17 on LUMI; recorded artifact missing
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Source manifest required

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Source manifest required
- **Last verified:** 2026-09-17 on LUMI; recorded artifact missing
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

The recorded Parquet artifact is missing, and the source
`DPOTrainer_format` directories used by the build script are not readable by
the current `project_465002530` account. Restore source access, rebuild into
the shared collection, and verify exact shares and licenses before marking
this runnable again.
