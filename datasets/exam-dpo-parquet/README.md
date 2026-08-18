---
name: "exam-dpo-parquet"
slug: "exam-dpo-parquet"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "configured-runnable"
status: "Configured / runnable"
language_keys: ["multilingual","code"]
languages: "35 language codes"
purpose: "Exam correctness preference pairs"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/simpo_qwen35_9b_exam.yaml"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/exam-dpo-parquet/train.parquet"
source_sheet_row: 50
---

# exam-dpo-parquet

> **State:** Configured / runnable  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** 35 language codes

## What it is for

Exam correctness preference pairs

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/simpo_qwen35_9b_exam.yaml>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/exam-dpo-parquet/train.parquet`
- **Upstream / parent:** oellm-eu-exam-mcq-v1
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/simpo_qwen35_9b_exam.yaml>)
- **Seed inventory:** [Data tab, row 50](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A50:Q50>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** Derived LUMI artifact
- **Priority:** P1
- **License / access:** Mixed upstream; filter licenses
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

SimPO configs exist for 2B/4B/9B/256k.

