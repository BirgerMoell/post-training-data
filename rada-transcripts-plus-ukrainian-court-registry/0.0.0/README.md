---
name: "Rada transcripts + Ukrainian court registry"
slug: "rada-transcripts-plus-ukrainian-court-registry"
version: "0.0.0"
catalogue_status: "D"
training_types: ["long-context-extension"]
status_key: "planned"
status: "Planned"
language_keys: ["uk"]
language_codes: ["ukr_Cyrl"]
languages: "uk"
purpose: "Ukrainian native long documents"
source_type: "National public sources"
priority: "P2"
curator: "Ukrainian/long-context team"
license_access: "Privacy/reuse review"
public_location: ""
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-07-01"
confidence: "High"
source_sheet_row: 90
---

# Rada transcripts + Ukrainian court registry

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Planned  
> **Training use:** long-context-extension  
> **Recorded languages:** uk

## <a id="background">Background</a>

Ukrainian native long documents

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Rada + court registry
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 90](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A90:Q90>)

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
| License and access | Privacy/reuse review |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ukr_Cyrl` | — | — | — | — | — |

Recorded coverage: uk

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 90](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A90:Q90>)
- **Last verified:** 2026-07-01
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Privacy/reuse review

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.

### Operational state and ownership

- **Owner / lead:** Ukrainian/long-context team
- **Source type:** National public sources
- **Priority:** P2
- **License / access:** Privacy/reuse review
- **Last verified:** 2026-07-01
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Ukrainian/long-context team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Court data requires PII/legal filtering.
