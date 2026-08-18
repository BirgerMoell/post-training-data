---
name: "LUMI English–Finnish long-context SFT blend"
slug: "lumi-long-context-eng-fin-sft"
training_types: ["long-context-extension","instruction-sft"]
status_key: "staged"
status: "Staged on LUMI — validation required"
language_keys: ["en","fi"]
languages: "en, fi (declared by directory name; distribution unmeasured)"
purpose: "Candidate long-instruction or replay data for preserving context capability during SFT"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Megatron_format/long-context-eng-fin"
source_sheet_row: null
---

# LUMI English–Finnish long-context SFT blend

> **State:** Staged on LUMI — validation required
> **Training use:** Long-context retention and instruction SFT
> **Languages:** English and Finnish are declared; measure the actual distribution

## What it is for

This is the most concrete post-context-extension retention candidate found in
the shared LUMI post-training tree. It may support either a long-sequence SFT
overlay or a low-learning-rate recovery/replay phase after short SFT. It does
not yet close the retention blocker because its source composition, sequence
lengths, licenses, loss mask, and completed-run evidence are not documented.

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/long-context-eng-fin`
- **Source JSONL:** `mixed_sft_dataset.jsonl` — 18,285,191,055 bytes
- **Megatron binary:** `processed_mixed_dataset/mixed_sft_dataset.jsonl_text_document.bin` — 16,584,019,328 bytes
- **Megatron index:** `processed_mixed_dataset/mixed_sft_dataset.jsonl_text_document.idx` — 37,981,842 bytes
- **Evidence:** Direct read-only LUMI inspection on 2026-08-18

## Observed format

The JSONL has one `text` field. Samples are pre-rendered with Llama-3-style
`<|start_header_id|>` role markers and include system, user, and assistant
turns. The paired `.bin`/`.idx` files are ready for Megatron's standard text
document loader, but that loader normally optimizes every token. The filenames
alone do not prove assistant-only loss or that examples are actually 64k/128k.

## How to use it

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

## Acceptance gate

Promote this asset only when at least 90% of its retained optimizer tokens are
in the intended long-length buckets, English/Finnish token shares are known,
all sources and licenses are approved, assistant masks are tested if used for
SFT, and a pilot preserves the Stage 1 long-context gain without unacceptable
short-context or multilingual regression.

## State and ownership

- **Owner / lead:** Unassigned; locate the preparer before use
- **Source type:** Derived LUMI JSONL and Megatron binary
- **Priority:** P0 retention candidate
- **License / access:** Mixed or unknown; LUMI access only
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for location/format; low for provenance/readiness

## Notes and next action

Recover the build script and generate a source/language/length manifest. Until
then this is a valuable experiment input, not an approved production dataset.
