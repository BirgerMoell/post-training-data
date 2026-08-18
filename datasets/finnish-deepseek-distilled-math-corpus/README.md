---
name: "Finnish DeepSeek-distilled math corpus"
slug: "finnish-deepseek-distilled-math-corpus"
training_types: ["reasoning-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["fi"]
languages: "fi"
purpose: "Finnish reasoning component"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/fin"
source_sheet_row: 27
---

# Finnish DeepSeek-distilled math corpus

> **State:** Used in completed run  
> **Training use:** Reasoning SFT  
> **Languages:** fi

## What it is for

Finnish reasoning component

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/fin`
- **Upstream / parent:** Finnish-NLP / distilled math
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_run2_data.py>)
- **Seed inventory:** [Data tab, row 27](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A27:Q27>)

## How to use it

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger / Finnish team
- **Source type:** LUMI shared dataset
- **Priority:** P1
- **License / access:** Exact upstream/license needs manifest
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## Notes and next action

Resolve file-level source IDs.

