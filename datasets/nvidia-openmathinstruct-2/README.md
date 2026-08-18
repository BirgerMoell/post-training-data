---
name: "nvidia/OpenMathInstruct-2"
slug: "nvidia-openmathinstruct-2"
training_types: ["reasoning-sft"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Math reasoning diversity"
public_location: "https://huggingface.co/datasets/nvidia/OpenMathInstruct-2"
lumi_location: ""
source_sheet_row: 34
---

# nvidia/OpenMathInstruct-2

> **State:** Candidate  
> **Training use:** Reasoning SFT  
> **Languages:** primarily en

## What it is for

Math reasoning diversity

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/OpenMathInstruct-2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** OpenMathInstruct 2
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 34](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A34:Q34>)

## How to use it

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Ablate against Nemotron.

