---
name: "medical-dpo-parquet"
slug: "medical-dpo-parquet"
training_types: ["preference-optimization","medical"]
status_key: "staged"
status: "Staged on LUMI"
language_keys: ["sv"]
languages: "sv / mixed"
purpose: "Medical preference pairs"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_medical_data.py"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/medical-dpo-parquet/train.parquet"
source_sheet_row: 65
---

# medical-dpo-parquet

> **State:** Staged on LUMI  
> **Training use:** Preference optimization, Medical specialization  
> **Languages:** sv / mixed

## What it is for

Medical preference pairs

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_medical_data.py>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/medical-dpo-parquet/train.parquet`
- **Upstream / parent:** oellm-eu-medical-posttrain-v1
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_medical_data.py>)
- **Seed inventory:** [Data tab, row 65](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A65:Q65>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Treat medical data as a separate research track and complete source, privacy, and license review before use.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P3
- **License / access:** License review pending
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

No confirmed mainline recipe.

