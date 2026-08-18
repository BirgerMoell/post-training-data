---
name: "HuggingFaceTB/smoltalk2 — Preference"
slug: "huggingfacetb-smoltalk2-preference"
training_types: ["preference-optimization"]
status_key: "configured-runnable"
status: "Configured / runnable"
language_keys: ["en"]
languages: "primarily en"
purpose: "Current official DPO config source"
public_location: "https://huggingface.co/datasets/HuggingFaceTB/smoltalk2"
lumi_location: ""
source_sheet_row: 41
---

# HuggingFaceTB/smoltalk2 — Preference

> **State:** Configured / runnable  
> **Training use:** Preference optimization  
> **Languages:** primarily en

## What it is for

Current official DPO config source

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/HuggingFaceTB/smoltalk2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** smoltalk2 Preference
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/post-training/blob/main/configs/trl/dpo.yaml>)
- **Seed inventory:** [Data tab, row 41](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A41:Q41>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Verify card
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Official config selects no-think Tülu mixture.

