---
name: "EUR-Lex / MultiEURLEX"
slug: "eur-lex-multieurlex"
version: "0.0.0"
catalogue_status: "D"
training_types: ["long-context-extension"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
language_codes: []
languages: "23+ EU languages"
purpose: "Native long legal documents"
source_type: "EU source family"
priority: "P1"
curator: "Long-context team"
license_access: "EU terms; review"
public_location: "https://eur-lex.europa.eu/"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-07-01"
confidence: "High"
source_sheet_row: 88
---

# EUR-Lex / MultiEURLEX

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Planned  
> **Training use:** long-context-extension  
> **Recorded languages:** 23+ EU languages

## <a id="background">Background</a>

Native long legal documents

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://eur-lex.europa.eu/>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** EUR-Lex / MultiEURLEX
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 88](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A88:Q88>)

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
| License and access | EU terms; review |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: 23+ EU languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://eur-lex.europa.eu/>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 88](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A88:Q88>)
- **Last verified:** 2026-07-01
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

EU terms; review

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** Long-context team
- **Source type:** EU source family
- **Priority:** P1
- **License / access:** EU terms; review
- **Last verified:** 2026-07-01
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Long-context team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Top planned source; preserve IDs and versions.
