---
name: "WildChat"
slug: "wildchat"
training_types: ["instruction-sft"]
status_key: "used-in-research"
status: "Used in research run"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Conversational diversity"
public_location: "https://huggingface.co/datasets/allenai/WildChat-1M"
lumi_location: ""
source_sheet_row: 14
---

# WildChat

> **State:** Used in research run  
> **Training use:** Instruction SFT  
> **Languages:** multilingual

## What it is for

Conversational diversity

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/WildChat-1M>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** WildChat
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/186>)
- **Seed inventory:** [Data tab, row 14](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A14:Q14>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** HF dataset
- **Priority:** P3
- **License / access:** Privacy/terms review
- **Last verified:** 2026-07-21
- **Confidence:** High

## Notes and next action

No clear gain in tested mix; keep as ablation evidence.

