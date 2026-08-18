---
name: "allenai/tulu-3-sft-mixture"
slug: "allenai-tulu-3-sft-mixture"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "en"
purpose: "English capability replay"
public_location: "https://huggingface.co/datasets/allenai/tulu-3-sft-mixture"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/allenai__tulu-3-sft-mixture"
source_sheet_row: 7
---

# allenai/tulu-3-sft-mixture

> **State:** Used in completed run  
> **Training use:** Instruction SFT  
> **Languages:** en

## What it is for

English capability replay

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/tulu-3-sft-mixture>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/allenai__tulu-3-sft-mixture`
- **Upstream / parent:** Tülu 3
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml>)
- **Seed inventory:** [Data tab, row 7](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A7:Q7>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger / T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Public; inspect components
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

920k replay examples in completed mix.

