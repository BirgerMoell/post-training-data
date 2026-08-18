---
name: "Tatoeba MT Challenge English–Finnish holdout on LUMI"
slug: "lumi-tatoeba-eng-fin"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Evaluation-only — do not train"
language_keys: ["en","fi"]
languages: "English, Finnish"
purpose: "English–Finnish translation and retention evaluation"
public_location: "https://github.com/Helsinki-NLP/Tatoeba-Challenge"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/Tatoeba/eng-fin"
source_sheet_row: null
---

# Tatoeba MT Challenge English–Finnish holdout on LUMI

> **State:** Evaluation-only — do not train
> **Training use:** English–Finnish translation holdout
> **Languages:** English and Finnish

## What it is for

A small, versioned English–Finnish translation check that complements broad
FLORES evaluation and can detect Finnish regressions after SFT or preference
optimization. The local directory contains only dev/test artifacts, which
should stay protected.

## Where to find it

- **Upstream:** [Helsinki-NLP/Tatoeba-Challenge](https://github.com/Helsinki-NLP/Tatoeba-Challenge)
- **Local package:** `eng-fin`, version `v2023-09-26`, based on Tatoeba corpus `v2023-04-12`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/Tatoeba/eng-fin`
- **Dev:** `dev.src` 2,303,326 bytes; `dev.trg` 2,565,292 bytes
- **Test:** `test.src` 401,576 bytes; `test.trg` 444,385 bytes
- **Evidence:** Local `README.md` and direct read-only inspection on 2026-08-18

## How to use it

Freeze the paired IDs and infer direction from `langids` rather than assuming
all rows have the same source language. Score both English-to-Finnish and
Finnish-to-English when supported, report paired-bootstrap confidence, and add
both sides to the decontamination index. Never use these dev/test files for
training, demonstrations, or synthetic generation.

## State and ownership

- **Owner / lead:** Evaluation team
- **Source type:** Versioned local evaluation package
- **Priority:** P1 protected holdout
- **License / access:** CC-BY-NC-SA-4.0 as recorded in the local README
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

## Notes and next action

Add a pinned scoring command and baseline scores for the approved Prelude base.
