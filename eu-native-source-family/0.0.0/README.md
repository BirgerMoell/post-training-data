---
name: "EU native source family"
slug: "eu-native-source-family"
version: "0.0.0"
catalogue_status: "D"
training_types: ["instruction-sft"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
language_codes: []
languages: "European languages"
purpose: "Native grounded prompt/response creation"
source_type: "Public source family"
priority: "P1"
curator: "T4.6 data team"
license_access: "Mixed; source-level review"
public_location: "https://data.europa.eu/"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-11"
confidence: "Medium"
source_sheet_row: 22
---

# EU native source family

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Planned  
> **Training use:** instruction-sft  
> **Recorded languages:** European languages

## <a id="background">Background</a>

Native grounded prompt/response creation

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://data.europa.eu/>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** data.europa.eu; EUR-Lex; DGT/JRC; EU Bookshop; national portals; Wikimedia/Wikisource; exams
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **Seed inventory:** [Data tab, row 22](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A22:Q22>)

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
| License and access | Mixed; source-level review |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: European languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://data.europa.eu/>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 22](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A22:Q22>)
- **Last verified:** 2026-08-11
- **Confidence:** Medium

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed; source-level review

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** Public source family
- **Priority:** P1
- **License / access:** Mixed; source-level review
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6 data team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Split into manifests by jurisdiction, language, domain and license.
