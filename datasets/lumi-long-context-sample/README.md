---
name: "LUMI long-context sample"
slug: "lumi-long-context-sample"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "staged"
status: "Staged on LUMI"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Shared long-context data/statistics"
public_location: ""
lumi_location: "/flash/project_465002530/preprocessed/oellm-v1-256k/long-ctx-sample"
source_sheet_row: 80
---

# LUMI long-context sample

> **State:** Staged on LUMI  
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** multilingual

## What it is for

Shared long-context data/statistics

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/flash/project_465002530/preprocessed/oellm-v1-256k/long-ctx-sample`
- **Upstream / parent:** Long-context pipeline
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/w58oa46znjdsureg74gsms489h>)
- **Seed inventory:** [Data tab, row 80](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A80:Q80>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- For continued pretraining or Megatron use, record the text field, tokenizer revision, sequence length, packing policy, and the exact derived artifact.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Jouni / long-context team
- **Source type:** LUMI artifact
- **Priority:** P1
- **License / access:** LUMI access
- **Last verified:** 2026-06-22
- **Confidence:** High

## Notes and next action

Outputs: /flash/project_465002530/users/luomajou/oellm-long-ctx.

