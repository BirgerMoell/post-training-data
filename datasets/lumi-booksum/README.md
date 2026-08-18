---
name: "BookSum staged on LUMI"
slug: "lumi-booksum"
training_types: ["long-context-extension","instruction-sft"]
status_key: "staged"
status: "Staged on LUMI — content and legal review required"
language_keys: ["en"]
languages: "English"
purpose: "Long-document summarization SFT and retention evaluation candidate"
public_location: "https://huggingface.co/datasets/kmfoda/booksum"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/booksum"
source_sheet_row: null
---

# BookSum staged on LUMI

> **State:** Staged on LUMI — content and legal review required
> **Training use:** Long-document summarization SFT or protected evaluation
> **Languages:** English

## What it is for

BookSum contains human-written summaries of long-form narrative text at
paragraph, chapter, and book granularity. It is relevant to long-context
summarization, but some aggregate rows have `content: null` and carry paths or
nested summary metadata rather than a ready prompt/answer pair. Its legal note
also requires a source-rights review beyond the repository's code license.

## Where to find it

- **Public source:** [kmfoda/booksum](https://huggingface.co/datasets/kmfoda/booksum)
- **Current public revision observed 2026-08-18:** `c62321036e5647db5767ecaff139912b554dc938`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/booksum`
- **Local splits:** `train.jsonl` 302,446,961; `validation.jsonl` 41,400,965;
  `test.jsonl` 44,443,940 bytes
- **Downloader:** `download.py` streams `kmfoda/booksum` without a revision
- **Observed fields:** content/chapter paths and lengths, summary text/metadata,
  IDs, aggregation flag, and source
- **Evidence:** Direct read-only LUMI inspection and public dataset card on 2026-08-18

## How to use it

First decide whether BookSum is training data or a protected long-summarization
evaluation; it cannot be both for the same release. Resolve source-text rights,
reconstruct only rows with accessible input text, parse nested summary fields,
and measure lengths with the target tokenizer. For SFT, format a neutral
summarization instruction and train only on the summary response. Keep official
validation/test IDs protected and deduplicate books across splits.

## State and ownership

- **Owner / lead:** Unassigned
- **Source type:** Public dataset with local JSONL materialization
- **Priority:** P2 candidate
- **License / access:** Code is BSD-3-Clause; source-content rights need review
- **Last verified:** 2026-08-18
- **Confidence:** High for location; low for production eligibility

## Notes and next action

Do not include this in a freeze until the legal decision and content
reconstruction report are recorded.
