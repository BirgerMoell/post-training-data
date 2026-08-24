---
name: "BookSum staged on LUMI"
slug: "lumi-booksum"
version: "0.0.0"
catalogue_status: "P"
training_types: ["long-context-extension","instruction-sft"]
status_key: "staged"
status: "Staged on LUMI — content and legal review required"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "English"
purpose: "Long-document summarization SFT and retention evaluation candidate"
source_type: "Public dataset with local JSONL materialization"
priority: "P2 candidate"
curator: "Unassigned"
license_access: "Code is BSD-3-Clause; source-content rights need review"
public_location: "https://huggingface.co/datasets/kmfoda/booksum"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/booksum"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18"
confidence: "High for location; low for production eligibility"
source_sheet_row: null
---

# BookSum staged on LUMI

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI — content and legal review required  
> **Training use:** long-context-extension, instruction-sft  
> **Recorded languages:** English

## <a id="background">Background</a>

BookSum contains human-written summaries of long-form narrative text at
paragraph, chapter, and book granularity. It is relevant to long-context
summarization, but some aggregate rows have `content: null` and carry paths or
nested summary metadata rather than a ready prompt/answer pair. Its legal note
also requires a source-rights review beyond the repository's code license.

## <a id="sources">Data Sources</a>

- **Public source:** [kmfoda/booksum](https://huggingface.co/datasets/kmfoda/booksum)
- **Current public revision observed 2026-08-18:** `c62321036e5647db5767ecaff139912b554dc938`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/booksum`
- **Local splits:** `train.jsonl` 302,446,961; `validation.jsonl` 41,400,965;
  `test.jsonl` 44,443,940 bytes
- **Downloader:** `download.py` streams `kmfoda/booksum` without a revision
- **Observed fields:** content/chapter paths and lengths, summary text/metadata,
  IDs, aggregation flag, and source
- **Evidence:** Direct read-only LUMI inspection and public dataset card on 2026-08-18

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
| License and access | Code is BSD-3-Clause; source-content rights need review |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: English

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/kmfoda/booksum>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/booksum`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18
- **Confidence:** High for location; low for production eligibility

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Code is BSD-3-Clause; source-content rights need review

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

First decide whether BookSum is training data or a protected long-summarization
evaluation; it cannot be both for the same release. Resolve source-text rights,
reconstruct only rows with accessible input text, parse nested summary fields,
and measure lengths with the target tokenizer. For SFT, format a neutral
summarization instruction and train only on the summary response. Keep official
validation/test IDs protected and deduplicate books across splits.

### Operational state and ownership

- **Owner / lead:** Unassigned
- **Source type:** Public dataset with local JSONL materialization
- **Priority:** P2 candidate
- **License / access:** Code is BSD-3-Clause; source-content rights need review
- **Last verified:** 2026-08-18
- **Confidence:** High for location; low for production eligibility

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Unassigned

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Do not include this in a freeze until the legal decision and content
reconstruction report are recorded.
