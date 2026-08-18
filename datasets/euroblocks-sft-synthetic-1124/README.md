---
name: "EuroBlocks-SFT-Synthetic-1124"
slug: "euroblocks-sft-synthetic-1124"
training_types: ["instruction-sft"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
languages: "EU multilingual"
purpose: "EU-language instruction backbone"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/multiling/EuroBlocks-SFT-Synthetic-1124"
source_sheet_row: 6
---

# EuroBlocks-SFT-Synthetic-1124

> **State:** Used in completed run  
> **Training use:** Instruction SFT  
> **Languages:** EU multilingual

## What it is for

EU-language instruction backbone

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data/SFTTrainer_format/multiling/EuroBlocks-SFT-Synthetic-1124`
- **Upstream / parent:** EuroBlocks synthetic
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/configs/sft_qwen35_9b.yaml>)
- **Seed inventory:** [Data tab, row 6](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A6:Q6>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** T4.6 / Birger
- **Source type:** LUMI shared dataset
- **Priority:** P1
- **License / access:** Internal/shared; license manifest needed
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

161k rows used; verify canonical upstream ID and terms.

