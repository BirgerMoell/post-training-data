---
name: "LUMI AM DeepSeek-R1 think mixture"
slug: "lumi-am-deepseek-r1-think"
version: "0.0.0"
catalogue_status: "P"
training_types: ["reasoning-sft"]
status_key: "staged"
status: "Staged on LUMI — lineage and trace policy required"
language_keys: ["en","code"]
language_codes: ["eng_Latn","zxx_Zyyy"]
languages: "English observed; code included; full distribution unmeasured"
purpose: "Large reasoning-trace SFT candidate spanning math, code, constraints, science, and multi-turn tasks"
source_type: "Derived reasoning JSONL and Megatron binary"
priority: "P1"
curator: "“AM” preparer not identified in the artifact"
license_access: "Unknown; LUMI access only"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Megatron_format/am-deepseek-r1-think"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 by direct LUMI inspection"
confidence: "High for files/format; low for provenance/correctness"
source_sheet_row: null
---

# LUMI AM DeepSeek-R1 think mixture

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI — lineage and trace policy required  
> **Training use:** reasoning-sft  
> **Recorded languages:** English observed; code included; full distribution unmeasured

## <a id="background">Background</a>

This is a large, already-combined reasoning mixture. Samples explicitly contain
`<think>...</think>` reasoning followed by a final response, so training on it
would teach visible reasoning traces unless the format and loss policy are
changed. The directory name is not enough to establish the generating model,
source datasets, licenses, filters, or correctness.

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/am-deepseek-r1-think`
- **Combined JSONL:** `combined_shuffled.jsonl` — 40,216,571,410 bytes
- **Components:** `math.jsonl` 15,388,498,062; `code.jsonl` 9,885,664,510;
  `other.jsonl` 8,886,239,687; `multiturn.jsonl` 3,449,413,289;
  `science.jsonl` 2,140,711,129; `if.jsonl` 466,044,733 bytes
- **Megatron binary:** `processed_datasets/combined_shuffled.jsonl_text_document.bin` — 44,850,915,892 bytes
- **Megatron index:** `processed_datasets/combined_shuffled.jsonl_text_document.idx` — 51,719,302 bytes
- **Evidence:** Direct read-only LUMI inspection on 2026-08-18

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

### Observed format evidence

Each inspected file contains a pre-rendered `text` field with Llama-3 role
markers and visible think blocks. Treat the six component files as separate
sources during analysis; do not train from `combined_shuffled.jsonl` until the
mixture weights can be reconstructed.

For a pilot, independently verify final answers, run code in a sandbox, test
instruction constraints, reject incomplete/leaked traces, and deduplicate
against reasoning evaluations. Compare visible-trace, final-answer-only, and
masked-trace policies. Add 20–30% general multilingual replay rather than
running the 40 GB mix alone.

## <a id="metadata">Available Metadata</a>

| Field | Status |
| --- | --- |
| Identity and intended post-training use | Recorded in this entry |
| Public and project-storage locations | Recorded when known; verify before use |
| Operational owner, priority, and confidence | Recorded from the project data register or repository evidence |
| Schema, columns, and splits | See source and structure evidence; inventory if absent |
| Immutable revision and checksums | Required for a production manifest; may still be missing |
| License and access | Unknown; LUMI access only |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |
| `zxx_Zyyy` | — | — | — | — | — |

Recorded coverage: English observed; code included; full distribution unmeasured

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/am-deepseek-r1-think`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for files/format; low for provenance/correctness

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Unknown; LUMI access only

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

### Operational state and ownership

- **Owner / lead:** “AM” preparer not identified in the artifact
- **Source type:** Derived reasoning JSONL and Megatron binary
- **Priority:** P1
- **License / access:** Unknown; LUMI access only
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for files/format; low for provenance/correctness

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

“AM” preparer not identified in the artifact

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Recover the generator/source manifest and verify a stratified sample with
task-appropriate checkers before any production reasoning run.
