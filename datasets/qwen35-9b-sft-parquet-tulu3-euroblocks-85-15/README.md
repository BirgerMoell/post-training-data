---
name: "qwen35-9b-sft-parquet (tulu3-euroblocks-85-15)"
slug: "qwen35-9b-sft-parquet-tulu3-euroblocks-85-15"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en","multilingual"]
languages: "EU multilingual + en"
purpose: "Main EU instruction mix + English replay"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-sft-parquet/train.parquet"
source_sheet_row: 5
---

# qwen35-9b-sft-parquet (tulu3-euroblocks-85-15)

> **State:** Used in completed run  
> **Training use:** Instruction SFT  
> **Languages:** EU multilingual + en

## What it is for

Main EU instruction mix + English replay

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-sft-parquet/train.parquet`
- **Upstream / parent:** EuroBlocks + Tülu-3
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/model_cards/qwen35-9b-eu-sft-README.md>)
- **Seed inventory:** [Data tab, row 5](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A5:Q5>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger Moëll
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Mixed upstream; review
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

~1.08M examples; completed 9B proof run. Preserve exact manifest and weights.

