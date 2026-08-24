---
name: "openeurollm/propella-annotations"
slug: "openeurollm-propella-annotations"
version: "0.0.0"
catalogue_status: "P"
training_types: ["data-quality-and-filtering"]
status_key: "published"
status: "Published / available"
language_keys: ["unspecified"]
language_codes: ["und_Zyyy"]
languages: "50+ languages"
purpose: "Quality/language annotations"
source_type: "HF + LUMI dataset"
priority: "P1"
curator: "Propella team"
license_access: "CC-BY-4.0"
public_location: "https://huggingface.co/datasets/openeurollm/propella-annotations"
lumi_location: "/scratch/project_465002530/datasets/propella-annotations"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-07-06"
confidence: "High"
source_sheet_row: 99
---

# openeurollm/propella-annotations

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Published / available  
> **Training use:** data-quality-and-filtering  
> **Recorded languages:** 50+ languages

## <a id="background">Background</a>

Quality/language annotations

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/propella-annotations>)
- **LUMI or other artifact:** `/scratch/project_465002530/datasets/propella-annotations`
- **Upstream / parent:** Propella
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/318>)
- **Seed inventory:** [Data tab, row 99](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A99:Q99>)

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
| License and access | CC-BY-4.0 |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `und_Zyyy` | — | — | — | — | — |

Recorded coverage: 50+ languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openeurollm/propella-annotations>)
- **LUMI or project artifact:** `/scratch/project_465002530/datasets/propella-annotations`
- **Source register:** [Data register row 99](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A99:Q99>)
- **Last verified:** 2026-07-06
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

CC-BY-4.0

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Use this primarily as annotations, filters, or processing support unless the page explicitly identifies trainable text.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Propella team
- **Source type:** HF + LUMI dataset
- **Priority:** P1
- **License / access:** CC-BY-4.0
- **Last verified:** 2026-07-06
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Propella team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Use as metadata/filtering, not raw text.
