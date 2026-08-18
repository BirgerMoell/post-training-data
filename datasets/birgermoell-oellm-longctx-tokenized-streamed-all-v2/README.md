---
name: "birgermoell/oellm-longctx-tokenized-streamed-all-v2"
slug: "birgermoell-oellm-longctx-tokenized-streamed-all-v2"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "published"
status: "Published / available"
language_keys: ["multilingual"]
languages: "34 European languages"
purpose: "Megatron-ready multilingual artifact"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-streamed-all-v2"
lumi_location: ""
source_sheet_row: 81
---

# birgermoell/oellm-longctx-tokenized-streamed-all-v2

> **State:** Published / available  
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** 34 European languages

## What it is for

Megatron-ready multilingual artifact

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-streamed-all-v2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** finepdfs-edu
- **Evidence:** [evidence](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-streamed-all-v2>)
- **Seed inventory:** [Data tab, row 81](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A81:Q81>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- For continued pretraining or Megatron use, record the text field, tokenizer revision, sequence length, packing policy, and the exact derived artifact.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger / long-context team
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Mixed upstream
- **Last verified:** 2026-05-28
- **Confidence:** High

## Notes and next action

Tokenized transport; pin tokenizer/run namespace.

