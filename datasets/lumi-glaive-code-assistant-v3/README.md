---
name: "Glaive Code Assistant v3 staged on LUMI"
slug: "lumi-glaive-code-assistant-v3"
training_types: ["reasoning-sft"]
status_key: "staged"
status: "Staged on LUMI — conversion revision not pinned"
language_keys: ["en","code"]
languages: "English prompts and multilingual programming languages"
purpose: "Synthetic code-instruction SFT candidate"
public_location: "https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/glaive-code-assistant-v3"
source_sheet_row: null
---

# Glaive Code Assistant v3 staged on LUMI

> **State:** Staged on LUMI — conversion revision not pinned
> **Training use:** Code instruction SFT
> **Languages:** English prompts; many programming languages

## What it is for

The public dataset contains 950,384 synthetic code problems and answers. It can
add broad code-generation and code-explanation coverage to the reasoning branch,
but it is not execution-verified and should not dominate a general assistant.

## Where to find it

- **Public source:** [glaiveai/glaive-code-assistant-v3](https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3)
- **Current public revision observed 2026-08-18:** `31a2e16324e6712f212d4361a768fc49295becff`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/glaive-code-assistant-v3`
- **Local JSONL:** `train.jsonl` — 1,920,598,441 bytes
- **Observed columns:** `question`, `answer`
- **Downloader:** `download.py` calls `load_dataset("glaiveai/glaive-code-assistant-v3", streaming=True)` without a revision
- **Evidence:** Direct read-only LUMI inspection and public dataset card on 2026-08-18

## How to use it

Re-download at a pinned revision or checksum the existing JSONL, normalize
question/answer into structured messages, and create a deterministic dev split.
Detect programming language and task type, cap repeated templates, compile or
execute supported answers in an isolated sandbox, and remove benchmark or
repository leakage where feasible. Use it as one capped component of the code
branch with general multilingual replay; do not treat prose-style answers as
proof of functional correctness.

## State and ownership

- **Owner / lead:** Glaive AI upstream; OpenEuroLLM stage owner unassigned
- **Source type:** Public synthetic dataset with local JSONL materialization
- **Priority:** P1
- **License / access:** Apache-2.0 upstream
- **Last verified:** 2026-08-18
- **Confidence:** High

## Notes and next action

Pin the conversion revision and generate compile/test success rates by language
before assigning it a production mixture weight.
