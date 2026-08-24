---
name: "oellm-eu-reasoning-v1"
slug: "oellm-eu-reasoning-v1"
version: "0.0.0"
catalogue_status: "D"
training_types: ["reasoning-sft"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
language_codes: []
languages: "European languages"
purpose: "Planned European reasoning product"
source_type: "Planned product"
priority: "P1"
curator: "T4.6 data team"
license_access: "Source-level licenses required"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "High"
source_sheet_row: 36
---

# oellm-eu-reasoning-v1

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Planned  
> **Training use:** reasoning-sft  
> **Recorded languages:** European languages

## <a id="background">Background</a>

Planned European reasoning product

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci Think; OpenThoughts; math; native generation
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **Seed inventory:** [Data tab, row 36](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A36:Q36>)

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
| License and access | Source-level licenses required |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: European languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 36](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A36:Q36>)
- **Last verified:** 2026-08-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Source-level licenses required

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** Planned product
- **Priority:** P1
- **License / access:** Source-level licenses required
- **Last verified:** 2026-08-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6 data team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Define verification, teacher provenance and language quotas.
