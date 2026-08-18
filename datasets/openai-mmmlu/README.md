---
name: "openai/MMMLU"
slug: "openai-mmmlu"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Multilingual MMLU-style MCQs"
public_location: "https://huggingface.co/datasets/openai/MMMLU"
lumi_location: ""
source_sheet_row: 53
---

# openai/MMMLU

> **State:** Used in completed run  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** multilingual

## What it is for

Multilingual MMLU-style MCQs

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openai/MMMLU>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** MMMLU
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_exam_mcq_dataset.py>)
- **Seed inventory:** [Data tab, row 53](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A53:Q53>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** MIT
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Audit translation quality and leakage.

