---
name: "Europarl"
slug: "europarl"
training_types: ["long-context-extension"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
languages: "EU multilingual"
purpose: "Parliament transcripts/xling tasks"
public_location: "https://www.statmt.org/europarl/"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/EuroParl"
source_sheet_row: 89
---

# Europarl

> **State:** Planned  
> **Training use:** Long-context extension  
> **Languages:** EU multilingual

## What it is for

Parliament transcripts/xling tasks

## Where to find it

- **Public or upstream:** [source](<https://www.statmt.org/europarl/>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/EuroParl`
- **Upstream / parent:** European Parliament
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 89](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A89:Q89>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Long-context team
- **Source type:** Public corpus
- **Priority:** P1
- **License / access:** Verify corpus terms
- **Last verified:** 2026-07-01
- **Confidence:** High

## Notes and next action

Pin version and language pairs.

