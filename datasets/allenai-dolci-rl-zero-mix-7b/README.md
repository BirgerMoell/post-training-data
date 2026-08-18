---
name: "allenai/Dolci-RL-Zero-Mix-7B"
slug: "allenai-dolci-rl-zero-mix-7b"
training_types: ["reinforcement-learning"]
status_key: "planned"
status: "Planned"
language_keys: ["en"]
languages: "primarily en"
purpose: "OLMo/Dolci RL reference"
public_location: "https://huggingface.co/datasets/allenai/Dolci-RL-Zero-Mix-7B"
lumi_location: ""
source_sheet_row: 58
---

# allenai/Dolci-RL-Zero-Mix-7B

> **State:** Planned  
> **Training use:** RLVR / GRPO / verifiable RL  
> **Languages:** primarily en

## What it is for

OLMo/Dolci RL reference

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/Dolci-RL-Zero-Mix-7B>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci RL Zero
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_data_lumi.sh>)
- **Seed inventory:** [Data tab, row 58](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A58:Q58>)

## How to use it

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

P1 candidate for full OLMo 3 sequence.

