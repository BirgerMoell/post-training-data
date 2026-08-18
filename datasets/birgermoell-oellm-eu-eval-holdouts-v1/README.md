---
name: "birgermoell/oellm-eu-eval-holdouts-v1"
slug: "birgermoell-oellm-eu-eval-holdouts-v1"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Eval-only — do not train"
language_keys: ["multilingual"]
languages: "38 languages"
purpose: "Canary post-training evaluation"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-eval-holdouts-v1"
lumi_location: ""
source_sheet_row: 106
---

# birgermoell/oellm-eu-eval-holdouts-v1

> **State:** Eval-only — do not train  
> **Training use:** Evaluation holdouts  
> **Languages:** 38 languages

## What it is for

Canary post-training evaluation

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-eval-holdouts-v1>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Synthetic canary eval
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EVAL_HOLDOUTS.md>)
- **Seed inventory:** [Data tab, row 106](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A106:Q106>)

## How to use it

- Keep this resource out of training, retrieval augmentation, data generation prompts, and model-selection feedback loops.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** N/A
- **License / access:** CC0-1.0
- **Last verified:** 2026-06-22
- **Confidence:** High

## Notes and next action

Exclude from training, RAG, tuning and generation prompts.

