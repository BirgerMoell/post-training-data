---
name: "birgermoell/oellm-eu-medical-posttrain-v1"
slug: "birgermoell-oellm-eu-medical-posttrain-v1"
training_types: ["preference-optimization","reinforcement-learning","medical"]
status_key: "published"
status: "Published / available"
language_keys: ["sv"]
languages: "European; current SFT sv"
purpose: "Medical source registry and builds"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-medical-posttrain-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/medical"
source_sheet_row: 63
---

# birgermoell/oellm-eu-medical-posttrain-v1

> **State:** Published / available  
> **Training use:** Preference optimization, RLVR / GRPO / verifiable RL, Medical specialization  
> **Languages:** European; current SFT sv

## What it is for

Medical source registry and builds

## Where to find it

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-medical-posttrain-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/medical`
- **Upstream / parent:** Medical exam/open-answer registry
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_medical_data.py>)
- **Seed inventory:** [Data tab, row 63](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A63:Q63>)

## How to use it

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Treat medical data as a separate research track and complete source, privacy, and license review before use.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

## State and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Mixed; research-only
- **Last verified:** 2026-06-26
- **Confidence:** High

## Notes and next action

Not for clinical deployment; complete license review.

