---
name: "openeurollm/prelude-base-eval-scores"
slug: "openeurollm-prelude-base-eval-scores"
version: "0.0.0"
catalogue_status: "P"
training_types: ["evaluation-holdouts"]
status_key: "supporting"
status: "Supporting evaluation artifact"
language_keys: ["multilingual"]
language_codes: []
languages: "multilingual"
purpose: "Prelude baseline and multilingual evaluation scores"
source_type: "Hugging Face result artifact"
priority: "Unset"
curator: "OpenEuroLLM evaluation team"
license_access: "Public; no license declared in the API metadata"
public_location: "https://huggingface.co/datasets/openeurollm/prelude-base-eval-scores"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 through the Hugging Face API"
confidence: "High"
source_sheet_row: null
---

# openeurollm/prelude-base-eval-scores

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Supporting evaluation artifact  
> **Training use:** evaluation-holdouts  
> **Recorded languages:** multilingual

## <a id="background">Background</a>

Published score tables for the Prelude base lineage. Use them as a baseline
when judging whether context extension or post-training regresses base and
multilingual capabilities.

## <a id="sources">Data Sources</a>

- **Public source:** [Hugging Face](https://huggingface.co/datasets/openeurollm/prelude-base-eval-scores)
- **Files:** `scores.parquet`, `multilingual_scores.parquet`
- **Pinned revision observed 2026-08-18:** `624e5bd33794953349f34d7127c87e1c950803fb`
- **LUMI artifact:** Not recorded

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
| License and access | Public; no license declared in the API metadata |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: multilingual

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openeurollm/prelude-base-eval-scores>)
- **LUMI or project artifact:** Not recorded
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Public; no license declared in the API metadata

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Treat the rows as reference results, not examples. Match model revision,
evaluation harness revision, task version, prompt/template, shot count, and
scoring settings before comparing a new checkpoint.

### Operational state and ownership

- **Owner / lead:** OpenEuroLLM evaluation team
- **Source type:** Hugging Face result artifact
- **License / access:** Public; no license declared in the API metadata
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

OpenEuroLLM evaluation team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Add a model-card description and a stable mapping from score rows to the exact
evaluation commands that produced them.
