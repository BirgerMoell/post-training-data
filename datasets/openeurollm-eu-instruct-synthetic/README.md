---
name: "openeurollm/EU-Instruct-Synthetic"
slug: "openeurollm-eu-instruct-synthetic"
training_types: ["instruction-sft"]
status_key: "published"
status: "Published / available"
language_keys: ["multilingual"]
languages: "11 European languages"
purpose: "Large multilingual synthetic instructions"
public_location: "https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic"
lumi_location: ""
source_sheet_row: 12
---

# openeurollm/EU-Instruct-Synthetic

> **State:** Published / available  
> **Training use:** Instruction SFT  
> **Languages:** 11 European languages

## What it is for

Large multilingual synthetic instructions

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Synthetic IF pipeline
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/345>)
- **Seed inventory:** [Data tab, row 12](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A12:Q12>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Abhash / T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Public; verify card
- **Last verified:** 2026-07-14
- **Confidence:** High

## Notes and next action

1,497,276 unique pairs; run quality and contamination sampling.

