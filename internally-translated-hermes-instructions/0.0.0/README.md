---
name: "Internally translated Hermes instructions"
slug: "internally-translated-hermes-instructions"
version: "0.0.0"
catalogue_status: "E"
training_types: ["instruction-sft"]
status_key: "historical"
status: "Historical / superseded"
language_keys: ["multilingual"]
language_codes: []
languages: "European languages"
purpose: "Translated conversation candidate"
source_type: "Internal reference"
priority: "P3"
curator: "T4.6"
license_access: "Internal; provenance review"
public_location: ""
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2025-11-13"
confidence: "Medium"
source_sheet_row: 19
---

# Internally translated Hermes instructions

**[DEPRECATED] (Version 0.0.0; August 2026)**

> **Operational state:** Historical / superseded  
> **Training use:** instruction-sft  
> **Recorded languages:** European languages

## <a id="background">Background</a>

Translated conversation candidate

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Hermes + translation
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/tmunyanqjtfrmc6rezgsx8gajo>)
- **Seed inventory:** [Data tab, row 19](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A19:Q19>)

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
| License and access | Internal; provenance review |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: European languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 19](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A19:Q19>)
- **Last verified:** 2025-11-13
- **Confidence:** Medium

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Internal; provenance review

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.

### Operational state and ownership

- **Owner / lead:** T4.6
- **Source type:** Internal reference
- **Priority:** P3
- **License / access:** Internal; provenance review
- **Last verified:** 2025-11-13
- **Confidence:** Medium

## <a id="quality">Quality, Safety & Exclusions</a>

This entry is retained for provenance and reproducibility. Do not select it for a new run without an explicit review and a replacement decision record.

## <a id="curator">Catalogue Curator</a>

T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Locate only if still useful after newer releases.
