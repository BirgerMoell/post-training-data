---
name: "allenai/Dolci-Instruct-DPO"
slug: "allenai-dolci-instruct-dpo"
training_types: ["preference-optimization"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "primarily en"
purpose: "Reference preference corpus"
public_location: "https://huggingface.co/datasets/allenai/Dolci-Instruct-DPO"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/DPOTrainer_format/eng/Dolci-Instruct-DPO"
source_sheet_row: 38
---

# allenai/Dolci-Instruct-DPO

> **State:** Used in completed run  
> **Training use:** Preference optimization  
> **Languages:** primarily en

## What it is for

Reference preference corpus

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/Dolci-Instruct-DPO>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/DPOTrainer_format/eng/Dolci-Instruct-DPO`
- **Upstream / parent:** Dolci
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/qhn43w9qii8wdyoipb4pxjgcba>)
- **Seed inventory:** [Data tab, row 38](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A38:Q38>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6 / Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Verify components
- **Last verified:** 2026-05-11
- **Confidence:** High

## Notes and next action

260k proxy pairs; used in completed 9B DPO.

