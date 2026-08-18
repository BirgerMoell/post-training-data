---
name: "birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2"
slug: "birgermoell-oellm-longctx-tokenized-superlong-512k-1m-2m-v2"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "published"
status: "Published / available"
language_keys: ["en","sv","de","es","fr","pl"]
languages: "en,sv,de,fr,es,pl"
purpose: "Superlong context extension"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2"
lumi_location: ""
source_sheet_row: 84
---

# birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2

> **State:** Published / available  
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** en,sv,de,fr,es,pl

## What it is for

Superlong context extension

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Natural/structured + hard dependencies
- **Evidence:** [evidence](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2>)
- **Seed inventory:** [Data tab, row 84](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A84:Q84>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- For continued pretraining or Megatron use, record the text field, tokenizer revision, sequence length, packing policy, and the exact derived artifact.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger / long-context team
- **Source type:** HF dataset
- **Priority:** P3
- **License / access:** Mixed upstream
- **Last verified:** 2026-06-25
- **Confidence:** High

## Notes and next action

Separate from instruction post-training.

