---
name: "oellm-eu-tool-agent-v1"
slug: "oellm-eu-tool-agent-v1"
training_types: ["reinforcement-learning","tool-and-agentic"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
languages: "European languages"
purpose: "Planned multilingual tool product"
public_location: "https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md"
lumi_location: ""
source_sheet_row: 79
---

# oellm-eu-tool-agent-v1

> **State:** Planned  
> **Training use:** RLVR / GRPO / verifiable RL, Tool use and agentic training  
> **Languages:** European languages

## What it is for

Planned multilingual tool product

## Where to find it

- **Public or upstream:** [source](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Public APIs + verified calls
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **Seed inventory:** [Data tab, row 79](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A79:Q79>)

## How to use it

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6 agentic data team
- **Source type:** Planned product
- **Priority:** P1
- **License / access:** API/PII review required
- **Last verified:** 2026-08-11
- **Confidence:** High

## Notes and next action

Preserve exact schemas and deterministic rewards.

