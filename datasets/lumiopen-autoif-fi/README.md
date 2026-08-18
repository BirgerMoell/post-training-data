---
name: "LumiOpen/AutoIF-FI"
slug: "lumiopen-autoif-fi"
training_types: ["instruction-sft","preference-optimization","reinforcement-learning"]
status_key: "candidate"
status: "Candidate"
language_keys: ["fi"]
languages: "fi"
purpose: "Finnish verifiable instruction following"
public_location: "https://huggingface.co/datasets/LumiOpen/AutoIF-FI"
lumi_location: ""
source_sheet_row: 20
---

# LumiOpen/AutoIF-FI

> **State:** Candidate  
> **Training use:** Instruction SFT, Preference optimization, RLVR / GRPO / verifiable RL  
> **Languages:** fi

## What it is for

Finnish verifiable instruction following

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/LumiOpen/AutoIF-FI>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** AutoIF-FI
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/b3mkcaxhybyq5jzyte1r399iye>)
- **Seed inventory:** [Data tab, row 20](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A20:Q20>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** LumiOpen / T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Public; verify card
- **Last verified:** 2026-05-11
- **Confidence:** High

## Notes and next action

Reported stronger than translated Tülu persona IF.

