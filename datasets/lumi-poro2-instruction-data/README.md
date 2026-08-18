---
name: "LUMI Poro2 instruction data"
slug: "lumi-poro2-instruction-data"
training_types: ["instruction-sft","language-repair"]
status_key: "staged"
status: "Staged on LUMI — provenance required"
language_keys: ["fi"]
languages: "Finnish observed; full distribution unmeasured"
purpose: "Finnish instruction-following and multilingual-replay candidate"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Megatron_format/poro2-instruction-data"
source_sheet_row: null
---

# LUMI Poro2 instruction data

> **State:** Staged on LUMI — provenance required
> **Training use:** Instruction SFT and Finnish repair
> **Languages:** Finnish observed; measure the complete distribution

## What it is for

A substantial pre-rendered instruction corpus associated with the Poro2 work.
Observed samples contain Finnish instructions and answers. It is a candidate
for Finnish replay or a Finnish-focused SFT ablation, not yet a project-wide
general SFT source.

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Megatron_format/poro2-instruction-data`
- **Source JSONL:** `regular_sft_dataset.jsonl` — 4,649,835,816 bytes
- **Megatron binary:** `processed_regular_dataset/regular_sft_dataset.jsonl_text_document.bin` — 5,016,149,788 bytes
- **Megatron index:** `processed_regular_dataset/regular_sft_dataset.jsonl_text_document.idx` — 28,153,682 bytes
- **Evidence:** Direct read-only LUMI inspection on 2026-08-18

## Observed format and use

The JSONL contains one `text` field rendered with Llama-3 role tokens. Before
training, recover its input-source manifest and chat-template code, measure
trainable tokens and languages, and inspect Finnish naturalness. The existing
Megatron binary appears to be plain text-document data; rebuild it if
assistant-only loss is required. Remove any fixed 2024 date/system prompt when
adapting it to Prelude.

Use it as a capped Finnish component in the Stage 2 or Stage 3 ratio sweep.
Keep a native Finnish dev set outside the training shard and compare against a
matched translated-Dolci control.

## State and ownership

- **Owner / lead:** Poro2 data preparer not recorded
- **Source type:** Derived LUMI JSONL and Megatron binary
- **Priority:** P1
- **License / access:** Unknown; LUMI access only
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for location/format; low for lineage and license

## Notes and next action

Locate the build recipe, source list, accepted licenses, tokenizer, row/token
counts, and completed-run evidence before adding it to a production freeze.
