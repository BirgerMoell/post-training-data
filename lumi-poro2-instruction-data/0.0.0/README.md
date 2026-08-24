---
name: "LUMI Poro2 instruction data"
slug: "lumi-poro2-instruction-data"
version: "0.0.0"
catalogue_status: "P"
training_types: ["instruction-sft","language-repair"]
status_key: "staged"
status: "Staged on LUMI — provenance required"
language_keys: ["fi"]
language_codes: ["fin_Latn"]
languages: "Finnish observed; full distribution unmeasured"
purpose: "Finnish instruction-following and multilingual-replay candidate"
source_type: "Derived LUMI JSONL and Megatron binary"
priority: "P1"
curator: "Poro2 data preparer not recorded"
license_access: "Unknown; LUMI access only"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Megatron_format/poro2-instruction-data"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 by direct LUMI inspection"
confidence: "High for location/format; low for lineage and license"
source_sheet_row: null
---

# LUMI Poro2 instruction data

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI — provenance required  
> **Training use:** instruction-sft, language-repair  
> **Recorded languages:** Finnish observed; full distribution unmeasured

## <a id="background">Background</a>

A substantial pre-rendered instruction corpus associated with the Poro2 work.
Observed samples contain Finnish instructions and answers. It is a candidate
for Finnish replay or a Finnish-focused SFT ablation, not yet a project-wide
general SFT source.

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/poro2-instruction-data`
- **Source JSONL:** `regular_sft_dataset.jsonl` — 4,649,835,816 bytes
- **Megatron binary:** `processed_regular_dataset/regular_sft_dataset.jsonl_text_document.bin` — 5,016,149,788 bytes
- **Megatron index:** `processed_regular_dataset/regular_sft_dataset.jsonl_text_document.idx` — 28,153,682 bytes
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

The JSONL contains one `text` field rendered with Llama-3 role tokens. Before
training, recover its input-source manifest and chat-template code, measure
trainable tokens and languages, and inspect Finnish naturalness. The existing
Megatron binary appears to be plain text-document data; rebuild it if
assistant-only loss is required. Remove any fixed 2024 date/system prompt when
adapting it to Prelude.

Use it as a capped Finnish component in the Stage 2 or Stage 3 ratio sweep.
Keep a native Finnish dev set outside the training shard and compare against a
matched translated-Dolci control.

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
| `fin_Latn` | — | — | — | — | — |

Recorded coverage: Finnish observed; full distribution unmeasured

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/poro2-instruction-data`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for location/format; low for lineage and license

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Unknown; LUMI access only

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

### Operational state and ownership

- **Owner / lead:** Poro2 data preparer not recorded
- **Source type:** Derived LUMI JSONL and Megatron binary
- **Priority:** P1
- **License / access:** Unknown; LUMI access only
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for location/format; low for lineage and license

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Poro2 data preparer not recorded

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Locate the build recipe, source list, accepted licenses, tokenizer, row/token
counts, and completed-run evidence before adding it to a production freeze.
