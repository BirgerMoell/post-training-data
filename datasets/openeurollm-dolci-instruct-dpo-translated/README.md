---
name: "openeurollm/Dolci-Instruct-DPO-translated"
slug: "openeurollm-dolci-instruct-dpo-translated"
training_types: ["preference-optimization"]
status_key: "published"
status: "Published / available"
language_keys: ["cs","de","el","es","fi","fr","it","pl","ro","sv","uk"]
languages: "cs,de,el,es,fi,fr,it,pl,ro,sv,uk (+ en config)"
purpose: "Multilingual preference alignment"
public_location: "https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated"
lumi_location: ""
source_sheet_row: 39
---

# openeurollm/Dolci-Instruct-DPO-translated

> **State:** Published / available  
> **Training use:** Preference optimization  
> **Languages:** cs,de,el,es,fi,fr,it,pl,ro,sv,uk (+ English configuration)

## What it is for

Multilingual preference alignment

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated>)
- **Pinned revision observed 2026-08-18:** `b231fb0cc857840d4731b180cc910d5f5d1f523e`
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci DPO + translation
- **Evidence:** [evidence](<https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated>)
- **Seed inventory:** [Data tab, row 39](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A39:Q39>)

## How to use it

- Load one configuration per language and retain the prompt/chosen/rejected
  relationship through templating.
- Verify that translation did not reverse or erase the preference margin,
  especially for style- and safety-sensitive pairs.
- Pin the revision, configurations, split, template, maximum lengths, and the
  sampled row count after filtering.

## State and ownership

- **Owner / lead:** OpenEuroLLM / MultiSynt
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Inherited + translation provenance
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## Notes and next action

Validate preference consistency after translation.
