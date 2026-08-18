---
name: "qwen35-9b-multiling-dpo-parquet"
slug: "qwen35-9b-multiling-dpo-parquet"
training_types: ["preference-optimization"]
status_key: "configured-runnable"
status: "Configured / runnable"
language_keys: ["fi","sv","da","no","is","multilingual"]
languages: "fi,sv,da,no,is + multilingual"
purpose: "Nordic/multilingual DPO mix"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b_multilingual.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-multiling-dpo-parquet/train.parquet"
source_sheet_row: 40
---

# qwen35-9b-multiling-dpo-parquet

> **State:** Configured / runnable  
> **Training use:** Preference optimization  
> **Languages:** fi,sv,da,no,is + multilingual

## What it is for

Nordic/multilingual DPO mix

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b_multilingual.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-multiling-dpo-parquet/train.parquet`
- **Upstream / parent:** LUMI DPOTrainer_format
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_run2_data.py>)
- **Seed inventory:** [Data tab, row 40](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A40:Q40>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Source manifest required
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Resolve exact shares and licenses.

