---
name: "birgermoell/oellm-longctx-tokenized-natural-128k-256k-pilot-v1"
slug: "birgermoell-oellm-longctx-tokenized-natural-128k-256k-pilot-v1"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "published"
status: "Published / available"
language_keys: ["en","multilingual"]
languages: "en + multilingual"
purpose: "Natural 128K/256K pilot"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-natural-128k-256k-pilot-v1"
lumi_location: ""
source_sheet_row: 82
---

# birgermoell/oellm-longctx-tokenized-natural-128k-256k-pilot-v1

> **State:** Published / available  
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** en + multilingual

## What it is for

Natural 128K/256K pilot

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-natural-128k-256k-pilot-v1>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Six natural tiers
- **Evidence:** [evidence](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-natural-128k-256k-pilot-v1>)
- **Seed inventory:** [Data tab, row 82](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A82:Q82>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- For continued pretraining or Megatron use, record the text field, tokenizer revision, sequence length, packing policy, and the exact derived artifact.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger / long-context team
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Mixed upstream
- **Last verified:** 2026-06-22
- **Confidence:** High

## Notes and next action

Pilot, not final instruction mix.

