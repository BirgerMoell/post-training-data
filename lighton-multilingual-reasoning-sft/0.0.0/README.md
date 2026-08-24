---
name: "LightOn multilingual reasoning SFT"
slug: "lighton-multilingual-reasoning-sft"
version: "0.0.0"
catalogue_status: "D"
training_types: ["reasoning-sft"]
status_key: "candidate"
status: "Candidate"
language_keys: ["multilingual"]
language_codes: []
languages: "European languages"
purpose: "Non-English reasoning coverage"
source_type: "Internal/unpublished"
priority: "P2"
curator: "LightOn / T4.6"
license_access: "Access/terms to confirm"
public_location: ""
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "Medium"
source_sheet_row: 35
---

# LightOn multilingual reasoning SFT

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Candidate  
> **Training use:** reasoning-sft  
> **Recorded languages:** European languages

## <a id="background">Background</a>

Non-English reasoning coverage

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** LightOn artifact
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 35](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A35:Q35>)

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
| License and access | Access/terms to confirm |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: European languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 35](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A35:Q35>)
- **Last verified:** 2026-08-11
- **Confidence:** Medium

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Access/terms to confirm

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.

### Operational state and ownership

- **Owner / lead:** LightOn / T4.6
- **Source type:** Internal/unpublished
- **Priority:** P2
- **License / access:** Access/terms to confirm
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

LightOn / T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Confirm languages, counts, license and owner.
