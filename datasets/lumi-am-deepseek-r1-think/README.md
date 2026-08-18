---
name: "LUMI AM DeepSeek-R1 think mixture"
slug: "lumi-am-deepseek-r1-think"
training_types: ["reasoning-sft"]
status_key: "staged"
status: "Staged on LUMI — lineage and trace policy required"
language_keys: ["en","code"]
languages: "English observed; code included; full distribution unmeasured"
purpose: "Large reasoning-trace SFT candidate spanning math, code, constraints, science, and multi-turn tasks"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Megatron_format/am-deepseek-r1-think"
source_sheet_row: null
---

# LUMI AM DeepSeek-R1 think mixture

> **State:** Staged on LUMI — lineage and trace policy required
> **Training use:** Reasoning SFT
> **Languages:** English observed; code included

## What it is for

This is a large, already-combined reasoning mixture. Samples explicitly contain
`<think>...</think>` reasoning followed by a final response, so training on it
would teach visible reasoning traces unless the format and loss policy are
changed. The directory name is not enough to establish the generating model,
source datasets, licenses, filters, or correctness.

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/am-deepseek-r1-think`
- **Combined JSONL:** `combined_shuffled.jsonl` — 40,216,571,410 bytes
- **Components:** `math.jsonl` 15,388,498,062; `code.jsonl` 9,885,664,510;
  `other.jsonl` 8,886,239,687; `multiturn.jsonl` 3,449,413,289;
  `science.jsonl` 2,140,711,129; `if.jsonl` 466,044,733 bytes
- **Megatron binary:** `processed_datasets/combined_shuffled.jsonl_text_document.bin` — 44,850,915,892 bytes
- **Megatron index:** `processed_datasets/combined_shuffled.jsonl_text_document.idx` — 51,719,302 bytes
- **Evidence:** Direct read-only LUMI inspection on 2026-08-18

## Observed format and use

Each inspected file contains a pre-rendered `text` field with Llama-3 role
markers and visible think blocks. Treat the six component files as separate
sources during analysis; do not train from `combined_shuffled.jsonl` until the
mixture weights can be reconstructed.

For a pilot, independently verify final answers, run code in a sandbox, test
instruction constraints, reject incomplete/leaked traces, and deduplicate
against reasoning evaluations. Compare visible-trace, final-answer-only, and
masked-trace policies. Add 20–30% general multilingual replay rather than
running the 40 GB mix alone.

## State and ownership

- **Owner / lead:** “AM” preparer not identified in the artifact
- **Source type:** Derived reasoning JSONL and Megatron binary
- **Priority:** P1
- **License / access:** Unknown; LUMI access only
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for files/format; low for provenance/correctness

## Notes and next action

Recover the generator/source manifest and verify a stratified sample with
task-appropriate checkers before any production reasoning run.
