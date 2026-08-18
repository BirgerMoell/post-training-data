---
name: "HPLT v2"
slug: "hplt-v2"
training_types: ["long-context-extension"]
status_key: "candidate"
status: "Candidate"
language_keys: ["multilingual"]
languages: "European multilingual"
purpose: "Large multilingual web data"
public_location: "https://hplt-project.org/datasets/v2.0"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/HLPT_data_v2"
source_sheet_row: 91
---

# HPLT v2

> **State:** Candidate  
> **Training use:** Long-context extension  
> **Languages:** European multilingual

## What it is for

Large multilingual web data

## Where to find it

- **Public or upstream:** [source](<https://hplt-project.org/datasets/v2.0>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/HLPT_data_v2`
- **Upstream / parent:** HPLT v2
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 91](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A91:Q91>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** Public dataset
- **Priority:** P2
- **License / access:** Web terms/PII filtering
- **Last verified:** 2026-07-01
- **Confidence:** High

## Notes and next action

LUMI folder spelling is HLPT; verify contents.

