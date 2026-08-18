---
name: "nvidia/Nemotron-Post-Training-Dataset-v2"
slug: "nvidia-nemotron-post-training-dataset-v2"
training_types: ["reasoning-sft"]
status_key: "configured-runnable"
status: "Configured / runnable"
language_keys: ["en"]
languages: "primarily en"
purpose: "Current official SFT config source"
public_location: "https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Nemotron-Post-Training-Dataset-v2/math.jsonl"
source_sheet_row: 24
---

# nvidia/Nemotron-Post-Training-Dataset-v2

> **State:** Configured / runnable  
> **Training use:** Reasoning SFT  
> **Languages:** primarily en

## What it is for

Current official SFT config source

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/Nemotron-Post-Training-Dataset-v2/math.jsonl`
- **Upstream / parent:** Nemotron v2
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/post-training/blob/main/configs/trl/sft.yaml>)
- **Seed inventory:** [Data tab, row 24](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A24:Q24>)

## How to use it

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Official config selects stem; not yet final multilingual recipe.

