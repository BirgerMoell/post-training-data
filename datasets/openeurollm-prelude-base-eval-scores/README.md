---
name: "openeurollm/prelude-base-eval-scores"
slug: "openeurollm-prelude-base-eval-scores"
training_types: ["evaluation-holdouts"]
status_key: "supporting"
status: "Supporting evaluation artifact"
language_keys: ["multilingual"]
languages: "multilingual"
purpose: "Prelude baseline and multilingual evaluation scores"
public_location: "https://huggingface.co/datasets/openeurollm/prelude-base-eval-scores"
lumi_location: ""
source_sheet_row: null
---

# openeurollm/prelude-base-eval-scores

> **State:** Supporting evaluation artifact
> **Training use:** Checkpoint comparison; never training data
> **Languages:** Multilingual

## What it is for

Published score tables for the Prelude base lineage. Use them as a baseline
when judging whether context extension or post-training regresses base and
multilingual capabilities.

## Where to find it

- **Public source:** [Hugging Face](https://huggingface.co/datasets/openeurollm/prelude-base-eval-scores)
- **Files:** `scores.parquet`, `multilingual_scores.parquet`
- **Pinned revision observed 2026-08-18:** `624e5bd33794953349f34d7127c87e1c950803fb`
- **LUMI artifact:** Not recorded

## How to use it

Treat the rows as reference results, not examples. Match model revision,
evaluation harness revision, task version, prompt/template, shot count, and
scoring settings before comparing a new checkpoint.

## State and ownership

- **Owner / lead:** OpenEuroLLM evaluation team
- **Source type:** Hugging Face result artifact
- **License / access:** Public; no license declared in the API metadata
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## Notes and next action

Add a model-card description and a stable mapping from score rows to the exact
evaluation commands that produced them.
