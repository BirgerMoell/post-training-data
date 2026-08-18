---
name: "nvidia/HelpSteer3"
slug: "nvidia-helpsteer3"
training_types: ["preference-optimization"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Preference/RM candidate"
public_location: "https://huggingface.co/datasets/nvidia/HelpSteer3"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/HelpSteer3"
source_sheet_row: 47
---

# nvidia/HelpSteer3

> **State:** Candidate  
> **Training use:** Preference optimization  
> **Languages:** primarily en

## What it is for

Preference/RM candidate

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/HelpSteer3>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/HelpSteer3`
- **Upstream / parent:** HelpSteer3
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/230>)
- **Seed inventory:** [Data tab, row 47](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A47:Q47>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** LUMI shared dataset
- **Priority:** P3
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## Notes and next action

Available on LUMI; not confirmed in main recipe.

