---
name: "EUR-Lex / MultiEURLEX"
slug: "eur-lex-multieurlex"
training_types: ["long-context-extension"]
status_key: "planned"
status: "Planned"
language_keys: ["multilingual"]
languages: "23+ EU languages"
purpose: "Native long legal documents"
public_location: "https://eur-lex.europa.eu/"
lumi_location: ""
source_sheet_row: 88
---

# EUR-Lex / MultiEURLEX

> **State:** Planned  
> **Training use:** Long-context extension  
> **Languages:** 23+ EU languages

## What it is for

Native long legal documents

## Where to find it

- **Public or upstream:** [source](<https://eur-lex.europa.eu/>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** EUR-Lex / MultiEURLEX
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 88](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A88:Q88>)

## How to use it

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- Pin an immutable public revision and record the exact configuration and split used.

## State and ownership

- **Owner / lead:** Long-context team
- **Source type:** EU source family
- **Priority:** P1
- **License / access:** EU terms; review
- **Last verified:** 2026-07-01
- **Confidence:** High

## Notes and next action

Top planned source; preserve IDs and versions.

