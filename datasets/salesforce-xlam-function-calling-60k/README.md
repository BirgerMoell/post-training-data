---
name: "Salesforce/xlam-function-calling-60k"
slug: "salesforce-xlam-function-calling-60k"
training_types: ["reinforcement-learning","tool-and-agentic"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "en"
purpose: "APIGen-style function calls"
public_location: "https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k"
lumi_location: ""
source_sheet_row: 71
---

# Salesforce/xlam-function-calling-60k

> **State:** Candidate  
> **Training use:** RLVR / GRPO / verifiable RL, Tool use and agentic training  
> **Languages:** en

## What it is for

APIGen-style function calls

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** xLAM 60k
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/build_tooluse_sft.py>)
- **Seed inventory:** [Data tab, row 71](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A71:Q71>)

## How to use it

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** Gated HF dataset
- **Priority:** P2
- **License / access:** Gated; verify terms
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Builder supports it; published v1 does not claim inclusion.

