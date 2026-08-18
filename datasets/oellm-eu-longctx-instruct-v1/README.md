---
name: "oellm-eu-longctx-instruct-v1"
slug: "oellm-eu-longctx-instruct-v1"
training_types: ["long-context-extension"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
languages: "European languages"
purpose: "Planned multilingual long-doc product"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md"
lumi_location: ""
source_sheet_row: 97
---

# oellm-eu-longctx-instruct-v1

> **State:** Planned  
> **Training use:** Long-context extension  
> **Languages:** European languages

## What it is for

Planned multilingual long-doc product

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** EUR-Lex; Europarl; national/web sources
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **Seed inventory:** [Data tab, row 97](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A97:Q97>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6 long-context team
- **Source type:** Planned product
- **Priority:** P1
- **License / access:** Source-level licenses required
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Target QA, summarization, retrieval and full-span use.

