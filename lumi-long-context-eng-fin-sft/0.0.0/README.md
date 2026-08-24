---
name: "LUMI English–Finnish long-context SFT blend"
slug: "lumi-long-context-eng-fin-sft"
version: "0.0.0"
catalogue_status: "P"
training_types: ["long-context-extension","instruction-sft"]
status_key: "staged"
status: "Staged on LUMI — validation required"
language_keys: ["en","fi"]
language_codes: ["eng_Latn","fin_Latn"]
languages: "en, fi (declared by directory name; distribution unmeasured)"
purpose: "Candidate long-instruction or replay data for preserving context capability during SFT"
source_type: "Derived LUMI JSONL and Megatron binary"
priority: "P0 retention candidate"
curator: "Unassigned; locate the preparer before use"
license_access: "Mixed or unknown; LUMI access only"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Megatron_format/long-context-eng-fin"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 by direct LUMI inspection"
confidence: "High for location/format; low for provenance/readiness"
source_sheet_row: null
---

# LUMI English–Finnish long-context SFT blend

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI — validation required  
> **Training use:** long-context-extension, instruction-sft  
> **Recorded languages:** en, fi (declared by directory name; distribution unmeasured)

## <a id="background">Background</a>

This is the most concrete post-context-extension retention candidate found in
the shared LUMI post-training tree. It may support either a long-sequence SFT
overlay or a low-learning-rate recovery/replay phase after short SFT. It does
not yet close the retention blocker because its source composition, sequence
lengths, licenses, loss mask, and completed-run evidence are not documented.

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/long-context-eng-fin`
- **Source JSONL:** `mixed_sft_dataset.jsonl` — 18,285,191,055 bytes
- **Megatron binary:** `processed_mixed_dataset/mixed_sft_dataset.jsonl_text_document.bin` — 16,584,019,328 bytes
- **Megatron index:** `processed_mixed_dataset/mixed_sft_dataset.jsonl_text_document.idx` — 37,981,842 bytes
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

The JSONL has one `text` field. Samples are pre-rendered with Llama-3-style
`<|start_header_id|>` role markers and include system, user, and assistant
turns. The paired `.bin`/`.idx` files are ready for Megatron's standard text
document loader, but that loader normally optimizes every token. The filenames
alone do not prove assistant-only loss or that examples are actually 64k/128k.

## <a id="metadata">Available Metadata</a>

| Field | Status |
| --- | --- |
| Identity and intended post-training use | Recorded in this entry |
| Public and project-storage locations | Recorded when known; verify before use |
| Operational owner, priority, and confidence | Recorded from the project data register or repository evidence |
| Schema, columns, and splits | See source and structure evidence; inventory if absent |
| Immutable revision and checksums | Required for a production manifest; may still be missing |
| License and access | Mixed or unknown; LUMI access only |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |
| `fin_Latn` | — | — | — | — | — |

Recorded coverage: en, fi (declared by directory name; distribution unmeasured)

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/long-context-eng-fin`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for location/format; low for provenance/readiness

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed or unknown; LUMI access only

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

1. Identify the script, inputs, tokenizer, and source weights that produced the
   JSONL and binary files. Record licenses and immutable input revisions.
2. Compute row counts, language distribution, source distribution, duplicate
   rate, and token-length percentiles with the target Prelude tokenizer.
3. Inspect at least 100 examples in every source/language/length stratum. Check
   role boundaries, stale system prompts, truncation, answer quality, and PII.
4. Decide the objective explicitly:
   - for CLM recovery/replay, the existing Megatron text documents may be usable
     after tokenizer and EOD verification;
   - for assistant-only SFT, rebuild from structured messages with a verified
     response mask. Do not assume the current `.bin` contains such a mask.
5. Freeze separate train/dev shards and remove overlap with long-context and
   multilingual evaluation.
6. Compare mixed long SFT against post-SFT recovery on a smaller checkpoint,
   evaluating 4k, 32k, 64k, and 128k after equal compute.

### Acceptance gate

Promote this asset only when at least 90% of its retained optimizer tokens are
in the intended long-length buckets, English/Finnish token shares are known,
all sources and licenses are approved, assistant masks are tested if used for
SFT, and a pilot preserves the Stage 1 long-context gain without unacceptable
short-context or multilingual regression.

### Operational state and ownership

- **Owner / lead:** Unassigned; locate the preparer before use
- **Source type:** Derived LUMI JSONL and Megatron binary
- **Priority:** P0 retention candidate
- **License / access:** Mixed or unknown; LUMI access only
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for location/format; low for provenance/readiness

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Unassigned; locate the preparer before use

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Recover the build script and generate a source/language/length manifest. Until
then this is a valuable experiment input, not an approved production dataset.
