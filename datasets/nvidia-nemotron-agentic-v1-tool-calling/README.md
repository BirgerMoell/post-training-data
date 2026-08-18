---
name: "nvidia/Nemotron-Agentic-v1 — tool-calling"
slug: "nvidia-nemotron-agentic-v1-tool-calling"
training_types: ["tool-and-agentic"]
status_key: "used-in-research"
status: "Used in research run"
language_keys: ["en"]
languages: "primarily en"
purpose: "Agentic tool calls"
public_location: "https://huggingface.co/datasets/nvidia/Nemotron-Agentic-v1"
lumi_location: ""
source_sheet_row: 75
---

# nvidia/Nemotron-Agentic-v1 — tool-calling

> **State:** Used in research run  
> **Training use:** Tool use and agentic training  
> **Languages:** primarily en

## What it is for

Agentic tool calls

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/Nemotron-Agentic-v1>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Nemotron Agentic v1
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/220>)
- **Seed inventory:** [Data tab, row 75](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A75:Q75>)

## How to use it

- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6 function-calling
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-03
- **Confidence:** High

## Notes and next action

One of five current mixture sources.

