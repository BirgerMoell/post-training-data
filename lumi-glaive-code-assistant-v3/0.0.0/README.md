---
name: "Glaive Code Assistant v3 staged on LUMI"
slug: "lumi-glaive-code-assistant-v3"
version: "0.0.0"
catalogue_status: "P"
training_types: ["reasoning-sft"]
status_key: "staged"
status: "Staged on LUMI — conversion revision not pinned"
language_keys: ["en","code"]
language_codes: ["eng_Latn","zxx_Zyyy"]
languages: "English prompts and multilingual programming languages"
purpose: "Synthetic code-instruction SFT candidate"
source_type: "Public synthetic dataset with local JSONL materialization"
priority: "P1"
curator: "Glaive AI upstream; OpenEuroLLM stage owner unassigned"
license_access: "Apache-2.0 upstream"
public_location: "https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/glaive-code-assistant-v3"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18"
confidence: "High"
source_sheet_row: null
---

# Glaive Code Assistant v3 staged on LUMI

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI — conversion revision not pinned  
> **Training use:** reasoning-sft  
> **Recorded languages:** English prompts and multilingual programming languages

## <a id="background">Background</a>

The public dataset contains 950,384 synthetic code problems and answers. It can
add broad code-generation and code-explanation coverage to the reasoning branch,
but it is not execution-verified and should not dominate a general assistant.

## <a id="sources">Data Sources</a>

- **Public source:** [glaiveai/glaive-code-assistant-v3](https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3)
- **Current public revision observed 2026-08-18:** `31a2e16324e6712f212d4361a768fc49295becff`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/glaive-code-assistant-v3`
- **Local JSONL:** `train.jsonl` — 1,920,598,441 bytes
- **Observed columns:** `question`, `answer`
- **Downloader:** `download.py` calls `load_dataset("glaiveai/glaive-code-assistant-v3", streaming=True)` without a revision
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
| License and access | Apache-2.0 upstream |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |
| `zxx_Zyyy` | — | — | — | — | — |

Recorded coverage: English prompts and multilingual programming languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/glaive-code-assistant-v3`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Apache-2.0 upstream

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Re-download at a pinned revision or checksum the existing JSONL, normalize
question/answer into structured messages, and create a deterministic dev split.
Detect programming language and task type, cap repeated templates, compile or
execute supported answers in an isolated sandbox, and remove benchmark or
repository leakage where feasible. Use it as one capped component of the code
branch with general multilingual replay; do not treat prose-style answers as
proof of functional correctness.

### Operational state and ownership

- **Owner / lead:** Glaive AI upstream; OpenEuroLLM stage owner unassigned
- **Source type:** Public synthetic dataset with local JSONL materialization
- **Priority:** P1
- **License / access:** Apache-2.0 upstream
- **Last verified:** 2026-08-18
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Glaive AI upstream; OpenEuroLLM stage owner unassigned

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Pin the conversion revision and generate compile/test success rates by language
before assigning it a production mixture weight.
