---
name: "openeurollm/jeopardy"
slug: "openeurollm-jeopardy"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Evaluation-only — do not train"
language_keys: ["en"]
languages: "en"
purpose: "2,117-example continuation evaluation set"
public_location: "https://huggingface.co/datasets/openeurollm/jeopardy"
lumi_location: ""
source_sheet_row: null
---

# openeurollm/jeopardy

> **State:** Evaluation-only — do not train
> **Training use:** Evaluation holdout
> **Languages:** English

## What it is for

An OpenEuroLLM evaluation artifact with 2,117 test examples and the fields
`context`, `continuation`, and `category`. It is useful for checkpoint
comparison and must remain outside every training and synthetic-generation
input.

## Where to find it

- **Public source:** [Hugging Face](https://huggingface.co/datasets/openeurollm/jeopardy)
- **Pinned revision observed 2026-08-18:** `42adb432a2a623f16ed66a8d002a810664255224`
- **LUMI artifact:** Not recorded

## How to use it

Load only the `test` split. Add its prompts and continuations to the
decontamination index before freezing any SFT, DPO, or RL data. Report the
exact revision and scoring method with results.

## State and ownership

- **Owner / lead:** OpenEuroLLM evaluation team
- **Source type:** Hugging Face evaluation dataset
- **License / access:** Public; dataset card does not currently declare a license
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## Notes and next action

Document the canonical metric and connect it to the common checkpoint gate.
