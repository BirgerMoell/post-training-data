---
name: "CohereLabs/Global-MMLU"
slug: "coherelabs-global-mmlu"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Academic MCQ coverage"
public_location: "https://huggingface.co/datasets/CohereLabs/Global-MMLU"
lumi_location: ""
source_sheet_row: 52
---

# CohereLabs/Global-MMLU

> **State:** Used in completed run  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** multilingual

## What it is for

Academic MCQ coverage

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/CohereLabs/Global-MMLU>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Global-MMLU
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_exam_mcq_dataset.py>)
- **Seed inventory:** [Data tab, row 52](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A52:Q52>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Apache-2.0
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Check benchmark overlap.

