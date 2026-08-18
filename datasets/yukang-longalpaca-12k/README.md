---
name: "Yukang/LongAlpaca-12k"
slug: "yukang-longalpaca-12k"
training_types: ["long-context-extension"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Long instruction candidate"
public_location: "https://huggingface.co/datasets/Yukang/LongAlpaca-12k"
lumi_location: ""
source_sheet_row: 87
---

# Yukang/LongAlpaca-12k

> **State:** Candidate  
> **Training use:** Long-context extension  
> **Languages:** primarily en

## What it is for

Long instruction candidate

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/Yukang/LongAlpaca-12k>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** LongAlpaca
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 87](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A87:Q87>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P3
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Use only if incremental.

