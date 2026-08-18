---
name: "birgermoell/oellm-eu-tooluse-v1"
slug: "birgermoell-oellm-eu-tooluse-v1"
training_types: ["reinforcement-learning","tool-and-agentic"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "en"
purpose: "Qwen-native tool SFT + verifiable RL"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-tooluse-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/eu-tooluse-parquet"
source_sheet_row: 67
---

# birgermoell/oellm-eu-tooluse-v1

> **State:** Used in completed run  
> **Training use:** RLVR / GRPO / verifiable RL, Tool use and agentic training  
> **Languages:** en

## What it is for

Qwen-native tool SFT + verifiable RL

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-tooluse-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/eu-tooluse-parquet`
- **Upstream / parent:** Glaive v2 + ToolACE + Hermes
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/dataset_cards/oellm-eu-tooluse-v1-README.md>)
- **Seed inventory:** [Data tab, row 67](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A67:Q67>)

## How to use it

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Apache-2.0
- **Last verified:** 2026-07-02
- **Confidence:** High

## Notes and next action

55,077 SFT; 46,366 GRPO; ~10% completed 4B mix.

