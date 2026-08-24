---
name: "OLMo gzip decontamination filter"
slug: "olmo-gzip-decontamination-filter"
version: "0.0.0"
catalogue_status: "P"
training_types: ["data-quality-and-filtering"]
status_key: "supporting"
status: "Supporting / filtering"
language_keys: ["multilingual"]
language_codes: []
languages: "language-agnostic"
purpose: "Long-context filtering method"
source_type: "Processing method"
priority: "P1"
curator: "T4.6 data team"
license_access: "Code terms to verify"
public_location: ""
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-07-01"
confidence: "High"
source_sheet_row: 101
---

# OLMo gzip decontamination filter

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Supporting / filtering  
> **Training use:** data-quality-and-filtering  
> **Recorded languages:** language-agnostic

## <a id="background">Background</a>

Long-context filtering method

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** OLMo filter
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 101](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A101:Q101>)

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
| License and access | Code terms to verify |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: language-agnostic

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 101](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A101:Q101>)
- **Last verified:** 2026-07-01
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Code terms to verify

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Use this primarily as annotations, filters, or processing support unless the page explicitly identifies trainable text.

### Operational state and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** Processing method
- **Priority:** P1
- **License / access:** Code terms to verify
- **Last verified:** 2026-07-01
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6 data team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Record config/hash and output manifests.
