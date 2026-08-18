---
name: "allenai/Dolci-Instruct-SFT"
slug: "allenai-dolci-instruct-sft"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "primarily en"
purpose: "Reference SFT and OLMo 3 reproduction"
public_location: "https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/Dolci-Instruct-SFT"
source_sheet_row: 8
---

# allenai/Dolci-Instruct-SFT

> **State:** Used in completed run  
> **Training use:** Instruction SFT  
> **Languages:** primarily en

## What it is for

Reference SFT and OLMo 3 reproduction

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/Dolci-Instruct-SFT`
- **Upstream / parent:** Dolci
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/335>)
- **Seed inventory:** [Data tab, row 8](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A8:Q8>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Public; verify components
- **Last verified:** 2026-08-05
- **Confidence:** High

## Notes and next action

Reference corpus for reproduced SFT pipeline.

