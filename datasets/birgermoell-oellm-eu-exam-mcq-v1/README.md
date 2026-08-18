---
name: "birgermoell/oellm-eu-exam-mcq-v1"
slug: "birgermoell-oellm-eu-exam-mcq-v1"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual","code"]
languages: "35 language codes"
purpose: "European exam rewards and preference pairs"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/exam_mcq/oellm-eu-exam-mcq-v1"
source_sheet_row: 49
---

# birgermoell/oellm-eu-exam-mcq-v1

> **State:** Used in completed run  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** 35 language codes

## What it is for

European exam rewards and preference pairs

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/exam_mcq/oellm-eu-exam-mcq-v1`
- **Upstream / parent:** 28 source registry entries
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_EXAM_MCQ_DATASET.md>)
- **Seed inventory:** [Data tab, row 49](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A49:Q49>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Mixed; row-filterable
- **Last verified:** 2026-06-23
- **Confidence:** High

## Notes and next action

582,983 GRPO rows; 1,936,764 DPO pairs.

