---
name: "FineWeb-2"
slug: "fineweb-2"
training_types: ["long-context-extension"]
status_key: "candidate"
status: "Candidate"
language_keys: ["multilingual"]
languages: "European multilingual"
purpose: "Multilingual web text"
public_location: "https://huggingface.co/datasets/HuggingFaceFW/fineweb-2"
lumi_location: ""
source_sheet_row: 93
---

# FineWeb-2

> **State:** Candidate  
> **Training use:** Long-context extension  
> **Languages:** European multilingual

## What it is for

Multilingual web text

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/HuggingFaceFW/fineweb-2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** FineWeb-2
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 93](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A93:Q93>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-07-01
- **Confidence:** High

## Notes and next action

Compare/deduplicate against HPLT/CulturaX.

