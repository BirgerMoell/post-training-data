---
name: "EU native source family"
slug: "eu-native-source-family"
training_types: ["instruction-sft"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
languages: "European languages"
purpose: "Native grounded prompt/response creation"
public_location: "https://data.europa.eu/"
lumi_location: ""
source_sheet_row: 22
---

# EU native source family

> **State:** Planned  
> **Training use:** Instruction SFT  
> **Languages:** European languages

## What it is for

Native grounded prompt/response creation

## Where to find it

- **Public or upstream:** [source](<https://data.europa.eu/>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** data.europa.eu; EUR-Lex; DGT/JRC; EU Bookshop; national portals; Wikimedia/Wikisource; exams
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_DATA_STRATEGY.md>)
- **Seed inventory:** [Data tab, row 22](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A22:Q22>)

## How to use it

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** T4.6 data team
- **Source type:** Public source family
- **Priority:** P1
- **License / access:** Mixed; source-level review
- **Last verified:** 2026-08-11
- **Confidence:** Medium

## Notes and next action

Split into manifests by jurisdiction, language, domain and license.

