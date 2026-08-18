---
name: "qwen35-9b-dpo-parquet"
slug: "qwen35-9b-dpo-parquet"
training_types: ["preference-optimization"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "en"
purpose: "Completed 9B English DPO stage"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-dpo-parquet/train.parquet"
source_sheet_row: 37
---

# qwen35-9b-dpo-parquet

> **State:** Used in completed run  
> **Training use:** Preference optimization  
> **Languages:** en

## What it is for

Completed 9B English DPO stage

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/dpo_qwen35_9b.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-dpo-parquet/train.parquet`
- **Upstream / parent:** Dolci Instruct DPO
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/RUNBOOK.md>)
- **Seed inventory:** [Data tab, row 37](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A37:Q37>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Internal derivative
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

260k pairs; keep as English reference.

