---
name: "medical-sft-parquet"
slug: "medical-sft-parquet"
training_types: ["medical"]
status_key: "configured-runnable"
status: "Configured / runnable"
language_keys: ["sv"]
languages: "sv"
purpose: "Swedish explanations + MCQ replay"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_4b_medical.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/medical-sft-parquet/train.parquet"
source_sheet_row: 64
---

# medical-sft-parquet

> **State:** Configured / runnable  
> **Training use:** Medical specialization  
> **Languages:** sv

## What it is for

Swedish explanations + MCQ replay

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_4b_medical.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/medical-sft-parquet/train.parquet`
- **Upstream / parent:** oellm-eu-medical-posttrain-v1
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_4b_medical.yaml>)
- **Seed inventory:** [Data tab, row 64](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A64:Q64>)

## How to use it

- Treat medical data as a separate research track and complete source, privacy, and license review before use.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P2
- **License / access:** License review pending
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Separate medical-domain track.

