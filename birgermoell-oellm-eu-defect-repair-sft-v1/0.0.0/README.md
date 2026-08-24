---
name: "birgermoell/oellm-eu-defect-repair-sft-v1"
slug: "birgermoell-oellm-eu-defect-repair-sft-v1"
version: "0.0.0"
catalogue_status: "P"
training_types: ["language-repair"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["fi","da","is","pl","ro","bg","et","ga","mt","hr","sl","lt","lv","hu","sk"]
language_codes: ["fin_Latn","dan_Latn","isl_Latn","pol_Latn","ron_Latn","bul_Cyrl","est_Latn","ekk_Latn","gle_Latn","mlt_Latn","hrv_Latn","slv_Latn","lit_Latn","lav_Latn","ltg_Latn","lvs_Latn","hun_Latn","slk_Latn"]
languages: "is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi"
purpose: "Weak-language degeneration repair"
source_type: "HF + LUMI dataset"
priority: "P1"
curator: "Birger"
license_access: "CC-BY-SA-4.0 / GFDL"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-defect-repair-sft-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/eu-defect-repair-parquet/train.parquet"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-06-25"
confidence: "High"
source_sheet_row: 98
---

# birgermoell/oellm-eu-defect-repair-sft-v1

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** language-repair  
> **Recorded languages:** is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi

## <a id="background">Background</a>

Weak-language degeneration repair

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-defect-repair-sft-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/eu-defect-repair-parquet/train.parquet`
- **Upstream / parent:** Wikipedia 20231101
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/DEFECT_REPAIR_SFT_DATASET.md>)
- **Seed inventory:** [Data tab, row 98](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A98:Q98>)

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
| License and access | CC-BY-SA-4.0 / GFDL |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `fin_Latn` | — | — | — | — | — |
| `dan_Latn` | — | — | — | — | — |
| `isl_Latn` | — | — | — | — | — |
| `pol_Latn` | — | — | — | — | — |
| `ron_Latn` | — | — | — | — | — |
| `bul_Cyrl` | — | — | — | — | — |
| `est_Latn` | — | — | — | — | — |
| `ekk_Latn` | — | — | — | — | — |
| `gle_Latn` | — | — | — | — | — |
| `mlt_Latn` | — | — | — | — | — |
| `hrv_Latn` | — | — | — | — | — |
| `slv_Latn` | — | — | — | — | — |
| `lit_Latn` | — | — | — | — | — |
| `lav_Latn` | — | — | — | — | — |
| `ltg_Latn` | — | — | — | — | — |
| `lvs_Latn` | — | — | — | — | — |
| `hun_Latn` | — | — | — | — | — |
| `slk_Latn` | — | — | — | — | — |

Recorded coverage: is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/birgermoell/oellm-eu-defect-repair-sft-v1>)
- **LUMI or project artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/eu-defect-repair-parquet/train.parquet`
- **Source register:** [Data register row 98](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A98:Q98>)
- **Last verified:** 2026-06-25
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

CC-BY-SA-4.0 / GFDL

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Inspect the recorded source and evidence, select an exact version, and document any conversion before training.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** HF + LUMI dataset
- **Priority:** P1
- **License / access:** CC-BY-SA-4.0 / GFDL
- **Last verified:** 2026-06-25
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Used 3× as targeted repair shard.
