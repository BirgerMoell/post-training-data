---
name: "EXAMS-QA"
slug: "exams-qa"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
languages: "14 European languages"
purpose: "Multilingual school exams"
public_location: "https://github.com/mhardalov/exams-qa"
lumi_location: ""
source_sheet_row: 51
---

# EXAMS-QA

> **State:** Used in completed run  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** 14 European languages

## What it is for

Multilingual school exams

## Where to find it

- **Public or upstream:** [source](<https://github.com/mhardalov/exams-qa>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** mhardalov/exams-qa
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_EXAM_MCQ_DATASET.md>)
- **Seed inventory:** [Data tab, row 51](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A51:Q51>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** GitHub source
- **Priority:** P1
- **License / access:** CC-BY-SA-4.0
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

19,058 rows in current build.

