---
name: "openeurollm/EU-Instruct-Synthetic"
slug: "openeurollm-eu-instruct-synthetic"
training_types: ["instruction-sft"]
status_key: "published"
status: "Published / available"
language_keys: ["cs","de","el","es","fr","it","nl","pl","pt","ro","uk"]
languages: "cs,de,el,es,fr,it,nl,pl,pt,ro,uk"
purpose: "Large multilingual synthetic instructions"
public_location: "https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic"
lumi_location: ""
source_sheet_row: 12
---

# openeurollm/EU-Instruct-Synthetic

> **State:** Published / available  
> **Training use:** Instruction SFT  
> **Languages:** cs,de,el,es,fr,it,nl,pl,pt,ro,uk

## What it is for

Approximately 1.5 million single-turn synthetic instruction/response pairs for
11 European languages. The public dataset uses `messages` and `language`
columns and is Apache-2.0 licensed.

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic>)
- **Pinned revision observed 2026-08-18:** `c13be5d71144feb1007708aae2a8c2d823f8e59a`
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Synthetic IF pipeline
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/345>)
- **Seed inventory:** [Data tab, row 12](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A12:Q12>)

## How to use it

- Use the `all` configuration for a common multilingual pool or the per-language
  configurations for explicit language weighting.
- Apply the model's exact chat template and train only assistant response tokens.
- Sample constraint-following correctness, language purity, translationese,
  factuality, and synthetic-template duplication before assigning production weight.
- Pin the revision, configuration, split, chat template, and row counts.

## State and ownership

- **Owner / lead:** Abhash / T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Public; verify card
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## Notes and next action

1,497,276 pairs are reported by the source inventory. This is strong breadth
data but should not be the only source for any language: pair it with translated
Dolci and native or human-authored material, then validate the mix per language.
