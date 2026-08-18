---
name: "allenai/Dolci-Think-DPO-32B"
slug: "allenai-dolci-think-dpo-32b"
training_types: ["preference-optimization"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Higher-teacher reasoning preferences"
public_location: "https://huggingface.co/datasets/allenai/Dolci-Think-DPO-32B"
lumi_location: ""
source_sheet_row: 44
---

# allenai/Dolci-Think-DPO-32B

> **State:** Candidate  
> **Training use:** Preference optimization  
> **Languages:** primarily en

## What it is for

Higher-teacher reasoning preferences

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/Dolci-Think-DPO-32B>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci Think 32B
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 44](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A44:Q44>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Measure uplift vs cost.

