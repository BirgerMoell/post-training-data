---
name: "allenai/Dolci-Instruct-SFT-Tool-Use"
slug: "allenai-dolci-instruct-sft-tool-use"
training_types: ["tool-and-agentic"]
status_key: "planned"
status: "Planned"
language_keys: ["en"]
languages: "primarily en"
purpose: "Dolci tool-use reference"
public_location: "https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT-Tool-Use"
lumi_location: ""
source_sheet_row: 72
---

# allenai/Dolci-Instruct-SFT-Tool-Use

> **State:** Planned  
> **Training use:** Tool use and agentic training  
> **Languages:** primarily en

## What it is for

Dolci tool-use reference

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT-Tool-Use>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci Tool Use
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_data_lumi.sh>)
- **Seed inventory:** [Data tab, row 72](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A72:Q72>)

## How to use it

- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

P2 staging candidate.

