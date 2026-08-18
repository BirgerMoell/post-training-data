---
name: "birgermoell/oellm-eu-defect-repair-sft-v1"
slug: "birgermoell-oellm-eu-defect-repair-sft-v1"
training_types: ["language-repair"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["fi","da","is","pl","ro","bg","et","ga","mt","hr","sl","lt","lv","hu","sk"]
languages: "is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi"
purpose: "Weak-language degeneration repair"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-defect-repair-sft-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/eu-defect-repair-parquet/train.parquet"
source_sheet_row: 98
---

# birgermoell/oellm-eu-defect-repair-sft-v1

> **State:** Used in completed run  
> **Training use:** Language repair  
> **Languages:** is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi

## What it is for

Weak-language degeneration repair

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-defect-repair-sft-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/eu-defect-repair-parquet/train.parquet`
- **Upstream / parent:** Wikipedia 20231101
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/DEFECT_REPAIR_SFT_DATASET.md>)
- **Seed inventory:** [Data tab, row 98](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A98:Q98>)

## How to use it

- Inspect the recorded source and evidence, select an exact version, and document any conversion before training.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF + LUMI dataset
- **Priority:** P1
- **License / access:** CC-BY-SA-4.0 / GFDL
- **Last verified:** 2026-06-25
- **Confidence:** High

## Notes and next action

Used 3× as targeted repair shard.

