---
name: "nvidia/ChatQA2-Long-SFT-data"
slug: "nvidia-chatqa2-long-sft-data"
training_types: ["long-context-extension"]
status_key: "planned"
status: "Planned"
language_keys: ["en"]
languages: "primarily en"
purpose: "Long QA/instruction data"
public_location: "https://huggingface.co/datasets/nvidia/ChatQA2-Long-SFT-data"
lumi_location: ""
source_sheet_row: 85
---

# nvidia/ChatQA2-Long-SFT-data

> **State:** Planned  
> **Training use:** Long-context extension  
> **Languages:** primarily en

## What it is for

Long QA/instruction data

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/ChatQA2-Long-SFT-data>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** ChatQA2 Long SFT
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_data_lumi.sh>)
- **Seed inventory:** [Data tab, row 85](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A85:Q85>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

P2 staging candidate.

