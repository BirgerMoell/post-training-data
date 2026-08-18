---
name: "glaiveai/glaive-function-calling-v2"
slug: "glaiveai-glaive-function-calling-v2"
training_types: ["reinforcement-learning","tool-and-agentic"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
languages: "en"
purpose: "Tool backbone + abstentions"
public_location: "https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2"
lumi_location: ""
source_sheet_row: 68
---

# glaiveai/glaive-function-calling-v2

> **State:** Used in completed run  
> **Training use:** RLVR / GRPO / verifiable RL, Tool use and agentic training  
> **Languages:** en

## What it is for

Tool backbone + abstentions

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Glaive v2
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/dataset_cards/oellm-eu-tooluse-v1-README.md>)
- **Seed inventory:** [Data tab, row 68](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A68:Q68>)

## How to use it

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Apache-2.0
- **Last verified:** 2026-07-02
- **Confidence:** High

## Notes and next action

50k kept plus refusal examples.

