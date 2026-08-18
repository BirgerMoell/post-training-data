---
name: "THUDM/LongAlign-10k"
slug: "thudm-longalign-10k"
training_types: ["long-context-extension"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Long instruction alignment"
public_location: "https://huggingface.co/datasets/THUDM/LongAlign-10k"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/LongAlign-10k"
source_sheet_row: 86
---

# THUDM/LongAlign-10k

> **State:** Candidate  
> **Training use:** Long-context extension  
> **Languages:** primarily en

## What it is for

Long instruction alignment

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/THUDM/LongAlign-10k>)
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/eng/LongAlign-10k`
- **Upstream / parent:** LongAlign
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 86](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A86:Q86>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF/LUMI dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Compare with ChatQA2 and native EU tasks.

