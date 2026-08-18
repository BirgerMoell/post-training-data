---
name: "nvidia/Llama-Nemotron-Post-Training-Dataset"
slug: "nvidia-llama-nemotron-post-training-dataset"
training_types: ["reasoning-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "primarily en"
purpose: "Additional math reasoning sample"
public_location: "https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Llama-Nemotron-Post-Training-Dataset/SFT-math-sample-100k.jsonl"
source_sheet_row: 25
---

# nvidia/Llama-Nemotron-Post-Training-Dataset

> **State:** Used in completed run  
> **Training use:** Reasoning SFT  
> **Languages:** primarily en

## What it is for

Additional math reasoning sample

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/Llama-Nemotron-Post-Training-Dataset/SFT-math-sample-100k.jsonl`
- **Upstream / parent:** Llama Nemotron
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_run2_data.py>)
- **Seed inventory:** [Data tab, row 25](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A25:Q25>)

## How to use it

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger / T4.6
- **Source type:** HF/LUMI dataset
- **Priority:** P1
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

100k math sample used in derived reasoning mix.

