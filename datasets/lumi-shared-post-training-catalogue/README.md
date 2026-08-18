---
name: "LUMI shared post-training catalogue"
slug: "lumi-shared-post-training-catalogue"
training_types: ["all-stages"]
status_key: "staged"
status: "Staged on LUMI"
language_keys: ["multilingual"]
languages: "many languages"
purpose: "Umbrella inventory of staged candidates"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data"
source_sheet_row: 105
---

# LUMI shared post-training catalogue

> **State:** Staged on LUMI  
> **Training use:** All stages  
> **Languages:** many languages

## What it is for

This is the landing page for the shared post-training data tree. The directory
contains hundreds of gigabytes of SFT, preference, reasoning, long-context, and
evaluation artifacts. Presence here means **available for inspection**, not
approved for training: several folders have no pinned revision, build manifest,
license decision, tokenizer record, or post-filter statistics.

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data`
- **Upstream / parent:** SFT/DPO formats; Nemotron; EuroParl; FLORES; HPLT; HelpSteer; code/chat/longctx
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/rf4igbsis7nq5ru1yirxfzi6xc>)
- **Seed inventory:** [Data tab, row 105](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A105:Q105>)

## How to use it

Start from the individually reviewed entries rather than selecting a directory
by name:

| Artifact | Stage | Current decision |
| --- | --- | --- |
| [English–Finnish long-context SFT](../lumi-long-context-eng-fin-sft/README.md) | Context retention / SFT | P0 candidate; needs lineage, lengths, and loss-mask validation |
| [Poro2 instruction data](../lumi-poro2-instruction-data/README.md) | Finnish SFT/repair | Staged; provenance and language audit missing |
| [AM DeepSeek-R1 think mix](../lumi-am-deepseek-r1-think/README.md) | Reasoning SFT | Staged; source, correctness, and trace-policy review missing |
| [OpenR1-Math-220k](../lumi-openr1-math-220k/README.md) | Reasoning/DPO/RLVR | Public upstream plus local materialization; pin local revision |
| [Glaive Code Assistant v3](../lumi-glaive-code-assistant-v3/README.md) | Code SFT | Public upstream plus local materialization; execute/filter samples |
| [BookSum](../lumi-booksum/README.md) | Long summarization | Legal/content reconstruction required |
| [FLORES-200/FLORES+](../lumi-flores-200/README.md) | Evaluation | Protected; never train |
| [Tatoeba English–Finnish](../lumi-tatoeba-eng-fin/README.md) | Evaluation | Protected; never train |

Other top-level families observed on 2026-08-18 include `SFTTrainer_format`
(about 773 GB), `DPOTrainer_format` (about 5.5 GB), HelpSteer3, Llama-Nemotron,
Nemotron v2, EuroParl, Wikipedia, FinePDFs-Edu, LMSYS Chat 1M, AlpacaEval, and
ArenaHard. They remain umbrella-level observations until an individual entry
records exact files, provenance, format, and readiness.

For any selected folder, inspect the concrete files and nearby documentation,
pin the upstream version or checksum the bytes, generate row/token/language and
length statistics, review terms, and record the exact conversion before launch.

## State and ownership

- **Owner / lead:** OpenEuroLLM data team
- **Source type:** LUMI catalogue
- **Priority:** P1
- **License / access:** Mixed; LUMI access
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

## Notes and next action

Every selected file needs ID, revision, license, checksum and lineage.
