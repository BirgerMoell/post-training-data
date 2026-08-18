---
name: "open-thoughts/OpenThoughts-114k"
slug: "open-thoughts-openthoughts-114k"
training_types: ["reasoning-sft"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
languages: "primarily en"
purpose: "Reference reasoning baseline"
public_location: "https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k"
lumi_location: ""
source_sheet_row: 31
---

# open-thoughts/OpenThoughts-114k

> **State:** Candidate  
> **Training use:** Reasoning SFT  
> **Languages:** primarily en

## What it is for

Reference reasoning baseline

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** OpenThoughts
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/z11nnkw3f3dq8cux4jw6n4733h>)
- **Seed inventory:** [Data tab, row 31](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A31:Q31>)

## How to use it

- For reasoning SFT, preserve the relationship between the reasoning trace and final answer, and sample correctness before mixing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify card
- **Last verified:** 2026-06-15
- **Confidence:** High

## Notes and next action

Use as baseline; OLMo/Dolci is full sequence reference.

