---
name: "The Stack v2"
slug: "the-stack-v2"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "candidate"
status: "Candidate"
language_keys: ["code"]
languages: "code"
purpose: "Long code/repository context"
public_location: "https://huggingface.co/datasets/bigcode/the-stack-v2"
lumi_location: ""
source_sheet_row: 95
---

# The Stack v2

> **State:** Candidate  
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** code

## What it is for

Long code/repository context

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/bigcode/the-stack-v2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** The Stack v2
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 95](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A95:Q95>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- For continued pretraining or Megatron use, record the text field, tokenizer revision, sequence length, packing policy, and the exact derived artifact.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Long-context team
- **Source type:** HF dataset
- **Priority:** P3
- **License / access:** Mixed code licenses
- **Last verified:** 2026-07-01
- **Confidence:** High

## Notes and next action

License filtering and secret scanning required.

