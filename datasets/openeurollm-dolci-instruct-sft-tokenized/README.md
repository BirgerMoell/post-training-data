---
name: "openeurollm/dolci-instruct-sft-tokenized"
slug: "openeurollm-dolci-instruct-sft-tokenized"
training_types: ["instruction-sft"]
status_key: "published"
status: "Published / available"
language_keys: ["en"]
languages: "primarily en"
purpose: "Tokenized ready-to-train artifact"
public_location: "https://huggingface.co/datasets/openeurollm/dolci-instruct-sft-tokenized"
lumi_location: ""
source_sheet_row: 10
---

# openeurollm/dolci-instruct-sft-tokenized

> **State:** Published / available  
> **Training use:** Instruction SFT  
> **Languages:** primarily en

## What it is for

OLMo-core-ready English instruction data: 2,152,111 examples, 1.7B total
tokens, and 789M trainable assistant tokens at a maximum sequence length of
32,768.

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/dolci-instruct-sft-tokenized>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci Instruct
- **Evidence:** [evidence](<https://huggingface.co/datasets/openeurollm/dolci-instruct-sft-tokenized>)
- **Seed inventory:** [Data tab, row 10](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A10:Q10>)

## How to use it

- This artifact is directly compatible with the OLMo-core SFT loader. It stores
  `token_ids_part_*.npy`, `labels_mask_part_*.npy`, a tokenizer directory, and
  `dataset_statistics.json`.
- Use only when the target model uses the recorded OLMo tokenizer and chat
  template. For a different base model, rebuild from the decontaminated raw
  Dolci source rather than reusing token IDs.
- Confirm that `labels_mask` trains assistant responses only and record the
  immutable dataset revision.

## State and ownership

- **Owner / lead:** OpenEuroLLM
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Inherited terms
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Ready for an OLMo-core reproduction. It is not a portable tokenized artifact
for Prelude or another tokenizer; the raw decontaminated dataset is the
portable source of truth.
