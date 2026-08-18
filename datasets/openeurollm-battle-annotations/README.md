---
name: "openeurollm/battle-annotations"
slug: "openeurollm-battle-annotations"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Eval-only — do not train"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Battle annotations"
public_location: "https://huggingface.co/datasets/openeurollm/battle-annotations"
lumi_location: ""
source_sheet_row: 108
---

# openeurollm/battle-annotations

> **State:** Eval-only — do not train  
> **Training use:** Evaluation holdouts  
> **Languages:** multilingual

## What it is for

Battle annotations

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/battle-annotations>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Battle evaluation
- **Evidence:** [evidence](<https://huggingface.co/datasets/openeurollm/battle-annotations>)
- **Seed inventory:** [Data tab, row 108](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A108:Q108>)

## How to use it

- Keep this resource out of training, retrieval augmentation, data generation prompts, and model-selection feedback loops.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Evaluation team
- **Source type:** HF dataset
- **Priority:** N/A
- **License / access:** Public; eval only
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Do not recycle into preference pools without new holdout design.

