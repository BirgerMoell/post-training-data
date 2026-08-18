---
name: "OpenAssistant / OASST2"
slug: "openassistant-oasst2"
training_types: ["instruction-sft"]
status_key: "used-in-research"
status: "Used in research run"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Open assistant conversations"
public_location: "https://huggingface.co/datasets/OpenAssistant/oasst2"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format"
source_sheet_row: 15
---

# OpenAssistant / OASST2

> **State:** Used in research run  
> **Training use:** Instruction SFT  
> **Languages:** multilingual

## What it is for

Open assistant conversations

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/OpenAssistant/oasst2>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format`
- **Upstream / parent:** OpenAssistant
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/186>)
- **Seed inventory:** [Data tab, row 15](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A15:Q15>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** HF dataset
- **Priority:** P3
- **License / access:** Apache-2.0 dataset; inspect rows
- **Last verified:** 2026-07-21
- **Confidence:** High

## Notes and next action

No clear gain in tested diversity mix.

