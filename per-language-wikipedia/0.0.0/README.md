---
name: "Per-language Wikipedia"
slug: "per-language-wikipedia"
version: "0.0.0"
catalogue_status: "P"
training_types: ["long-context-extension","language-repair"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["unspecified"]
language_codes: ["und_Zyyy"]
languages: "15 repair languages + EU"
purpose: "Native text and weak-language repair"
source_type: "HF/Wikimedia source"
priority: "P1"
curator: "Birger / T4.6"
license_access: "CC-BY-SA-4.0 / GFDL"
public_location: "https://huggingface.co/datasets/wikimedia/wikipedia"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-06-25"
confidence: "High"
source_sheet_row: 94
---

# Per-language Wikipedia

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** long-context-extension, language-repair  
> **Recorded languages:** 15 repair languages + EU

## <a id="background">Background</a>

Native text and weak-language repair

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/wikimedia/wikipedia>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** wikimedia/wikipedia 20231101
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/DEFECT_REPAIR_SFT_DATASET.md>)
- **Seed inventory:** [Data tab, row 94](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A94:Q94>)

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
| `und_Zyyy` | — | — | — | — | — |

Recorded coverage: 15 repair languages + EU

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/wikimedia/wikipedia>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 94](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A94:Q94>)
- **Last verified:** 2026-06-25
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

CC-BY-SA-4.0 / GFDL

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** Birger / T4.6
- **Source type:** HF/Wikimedia source
- **Priority:** P1
- **License / access:** CC-BY-SA-4.0 / GFDL
- **Last verified:** 2026-06-25
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger / T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Used for defect repair; planned for long-context.
