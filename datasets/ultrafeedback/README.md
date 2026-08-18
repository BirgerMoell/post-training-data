---
name: "UltraFeedback"
slug: "ultrafeedback"
training_types: ["preference-optimization"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "General preference baseline"
public_location: "https://huggingface.co/datasets/openbmb/UltraFeedback"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/DPOTrainer_format/eng/Ultrafeedback"
source_sheet_row: 46
---

# UltraFeedback

> **State:** Candidate  
> **Training use:** Preference optimization  
> **Languages:** primarily en

## What it is for

General preference baseline

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openbmb/UltraFeedback>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/DPOTrainer_format/eng/Ultrafeedback`
- **Upstream / parent:** UltraFeedback
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 46](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A46:Q46>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF/LUMI dataset
- **Priority:** P3
- **License / access:** Exact variant to confirm
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## Notes and next action

Record exact processing/decontamination.

