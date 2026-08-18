---
name: "openeurollm/lmsys-chat-1m-decontaminated"
slug: "openeurollm-lmsys-chat-1m-decontaminated"
training_types: ["instruction-sft"]
status_key: "published"
status: "Published / available"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Decontaminated conversational data"
public_location: "https://huggingface.co/datasets/openeurollm/lmsys-chat-1m-decontaminated"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/lmsys-chat-1m"
source_sheet_row: 16
---

# openeurollm/lmsys-chat-1m-decontaminated

> **State:** Published / available  
> **Training use:** Instruction SFT  
> **Languages:** multilingual

## What it is for

Decontaminated conversational data

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/lmsys-chat-1m-decontaminated>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/lmsys-chat-1m`
- **Upstream / parent:** lmsys-chat-1m
- **Evidence:** [evidence](<https://huggingface.co/datasets/openeurollm/lmsys-chat-1m-decontaminated>)
- **Seed inventory:** [Data tab, row 16](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A16:Q16>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** OpenEuroLLM
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Privacy/terms review
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Use only after privacy and quality checks.

