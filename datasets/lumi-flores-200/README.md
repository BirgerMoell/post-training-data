---
name: "FLORES-200 / FLORES+ evaluation copy on LUMI"
slug: "lumi-flores-200"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Evaluation-only — do not train"
language_keys: ["bg","cs","da","de","el","en","es","et","fi","fr","ga","hr","hu","is","it","lt","lv","mt","nl","no","pl","pt","ro","sk","sl","sv"]
languages: "26 European language files plus FLORES+ combined dev/devtest"
purpose: "Parallel multilingual translation and language-retention evaluation"
public_location: "https://huggingface.co/datasets/openlanguagedata/flores_plus"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/FLORES-200"
source_sheet_row: null
---

# FLORES-200 / FLORES+ evaluation copy on LUMI

> **State:** Evaluation-only — do not train
> **Training use:** Multilingual evaluation holdout
> **Languages:** 26 European per-language files plus combined FLORES+

## What it is for

This local copy provides aligned development and development-test material for
translation and multilingual retention checks. It is especially useful for a
single repeatable language gate after each training stage. It is not an
instruction dataset and must not enter training or synthetic prompt generation.

## Where to find it

- **Public/upstream:** FLORES+ link recorded above; the exact local build revision is not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/FLORES-200`
- **Combined files:** `floresplus_dev.jsonl` — 135,375,515 bytes;
  `floresplus_devtest.jsonl` — 134,001,541 bytes
- **Per-language files:** `{iso}-dev.jsonl`, `{iso}-devtest.jsonl`, and text counterparts
- **Observed JSON fields:** `id`, `text`, ISO/glottocode/script metadata,
  domain, topic, URL, hyperlink/image flags, and update date
- **Evidence:** Direct read-only LUMI inspection on 2026-08-18

## How to use it

Pin the upstream/local lineage, freeze the devtest IDs, and build consistent
translation directions from aligned IDs. Report results per language and
direction with the exact prompting/scoring code. Add every source and target
string to the decontamination index before any SFT, preference, or RLVR freeze.

## State and ownership

- **Owner / lead:** Evaluation team
- **Source type:** Local evaluation copy
- **Priority:** P0 protected holdout
- **License / access:** Verify exact FLORES/FLORES+ release terms
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for files; medium for local lineage

## Notes and next action

Record the upstream revision and alignment script, then make this part of the
common per-language checkpoint gate.
