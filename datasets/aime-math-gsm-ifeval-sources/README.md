---
name: "AIME / MATH / GSM / IFEval sources"
slug: "aime-math-gsm-ifeval-sources"
training_types: ["reinforcement-learning"]
status_key: "planned"
status: "Planned"
language_keys: ["en"]
languages: "primarily en"
purpose: "Targeted correctness/IF rewards"
public_location: ""
lumi_location: ""
source_sheet_row: 62
---

# AIME / MATH / GSM / IFEval sources

> **State:** Planned  
> **Training use:** RLVR / GRPO / verifiable RL  
> **Languages:** primarily en

## What it is for

Targeted correctness/IF rewards

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** AIME; MATH; GSM8K; IFEval
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 62](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A62:Q62>)

## How to use it

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** Benchmark family
- **Priority:** P2
- **License / access:** Mixed; benchmark isolation
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## Notes and next action

Keep eval holdouts disjoint.

