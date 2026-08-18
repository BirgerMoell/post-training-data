---
name: "open-thoughts/OpenThoughts2-1M"
slug: "open-thoughts-openthoughts2-1m"
training_types: ["reasoning-sft"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Large reasoning expansion"
public_location: "https://huggingface.co/datasets/open-thoughts/OpenThoughts2-1M"
lumi_location: ""
source_sheet_row: 33
---

# open-thoughts/OpenThoughts2-1M

> **State:** Candidate  
> **Training use:** Reasoning SFT  
> **Languages:** primarily en

## What it is for

Large reasoning expansion

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/open-thoughts/OpenThoughts2-1M>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** OpenThoughts2
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/SOURCES.md>)
- **Seed inventory:** [Data tab, row 33](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A33:Q33>)

## How to use it

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Sample correctness and deduplicate.

