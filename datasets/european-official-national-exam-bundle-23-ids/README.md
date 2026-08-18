---
name: "European official/national exam bundle (23 IDs)"
slug: "european-official-national-exam-bundle-23-ids"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en","sv","da","cs","es","it","pl","sq","bg","ca","et","sk","eu"]
languages: "sq,bg,ca,cs,da,en,es,et,eu,it,pl,sk,sv"
purpose: "Native exam/licensing/civic MCQs"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1"
lumi_location: ""
source_sheet_row: 56
---

# European official/national exam bundle (23 IDs)

> **State:** Used in completed run  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** sq,bg,ca,cs,da,en,es,et,eu,it,pl,sk,sv

## What it is for

Native exam/licensing/civic MCQs

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** UHR; CKE/PES/LEK/LDEK; Danish citizenship; Estonian/Bulgarian/Albanian/Czech/Italian/Slovak/Basque/Catalan/Spanish sources
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/exam_mcq/oellm-eu-exam-mcq-v1/source_registry.json>)
- **Seed inventory:** [Data tab, row 56](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A56:Q56>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** Public/HF bundle
- **Priority:** P1
- **License / access:** Mixed: permissive, NC, custom, unknown
- **Last verified:** 2026-06-23
- **Confidence:** High

## Notes and next action

Use child registry; exclude unknown/NC for permissive runs.

