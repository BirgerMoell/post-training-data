---
name: "Per-language Wikipedia"
slug: "per-language-wikipedia"
training_types: ["long-context-extension","language-repair"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["unspecified"]
languages: "15 repair languages + EU"
purpose: "Native text and weak-language repair"
public_location: "https://huggingface.co/datasets/wikimedia/wikipedia"
lumi_location: ""
source_sheet_row: 94
---

# Per-language Wikipedia

> **State:** Used in completed run  
> **Training use:** Long-context extension, Language repair  
> **Languages:** 15 repair languages + EU

## What it is for

Native text and weak-language repair

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/wikimedia/wikipedia>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** wikimedia/wikipedia 20231101
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/DEFECT_REPAIR_SFT_DATASET.md>)
- **Seed inventory:** [Data tab, row 94](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A94:Q94>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger / T4.6
- **Source type:** HF/Wikimedia source
- **Priority:** P1
- **License / access:** CC-BY-SA-4.0 / GFDL
- **Last verified:** 2026-06-25
- **Confidence:** High

## Notes and next action

Used for defect repair; planned for long-context.

