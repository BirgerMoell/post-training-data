---
name: "LUMI shared post-training catalogue"
slug: "lumi-shared-post-training-catalogue"
version: "0.0.0"
catalogue_status: "P"
training_types: ["all-stages"]
status_key: "staged"
status: "Staged on LUMI"
language_keys: ["multilingual"]
language_codes: []
languages: "many languages"
purpose: "Umbrella inventory of staged candidates"
source_type: "LUMI catalogue"
priority: "P1"
curator: "OpenEuroLLM data team"
license_access: "Mixed; LUMI access"
public_location: ""
lumi_location: "/scratch/project_462000963/datasets/posttraining_data"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 by direct LUMI inspection"
confidence: "High"
source_sheet_row: 105
---

# LUMI shared post-training catalogue

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI  
> **Training use:** all-stages  
> **Recorded languages:** many languages

## <a id="background">Background</a>

This is the landing page for the shared post-training data tree. The directory
contains hundreds of gigabytes of SFT, preference, reasoning, long-context, and
evaluation artifacts. Presence here means **available for inspection**, not
approved for training: several folders have no pinned revision, build manifest,
license decision, tokenizer record, or post-filter statistics.

## <a id="sources">Data Sources</a>

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/scratch/project_462000963/datasets/posttraining_data`
- **Upstream / parent:** SFT/DPO formats; Nemotron; EuroParl; FLORES; HPLT; HelpSteer; code/chat/longctx
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/rf4igbsis7nq5ru1yirxfzi6xc>)
- **Seed inventory:** [Data tab, row 105](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A105:Q105>)

## <a id="statistics">Structure & Statistics</a>

The normalized totals below have not yet been entered for this catalogue version. Source-specific figures in the evidence section remain useful, but should not be treated as comparable catalogue totals until reproduced.

| Measure | Value |
| --- | ---: |
| Bytes | — |
| Documents | — |
| Segments | — |
| Characters | — |
| Tokens | — |
| Data format | Not normalized |
| Compression | Not normalized |

## <a id="metadata">Available Metadata</a>

| Field | Status |
| --- | --- |
| Identity and intended post-training use | Recorded in this entry |
| Public and project-storage locations | Recorded when known; verify before use |
| Operational owner, priority, and confidence | Recorded from the project data register or repository evidence |
| Schema, columns, and splits | See source and structure evidence; inventory if absent |
| Immutable revision and checksums | Required for a production manifest; may still be missing |
| License and access | Mixed; LUMI access |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| Not enumerated | — | — | — | — | — |

Recorded coverage: many languages

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** Not recorded
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data`
- **Source register:** [Data register row 105](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A105:Q105>)
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed; LUMI access

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Start from the individually reviewed entries rather than selecting a directory
by name:

| Artifact | Stage | Current decision |
| --- | --- | --- |
| [English–Finnish long-context SFT](../../lumi-long-context-eng-fin-sft/0.0.0/README.md) | Context retention / SFT | P0 candidate; needs lineage, lengths, and loss-mask validation |
| [Poro2 instruction data](../../lumi-poro2-instruction-data/0.0.0/README.md) | Finnish SFT/repair | Staged; provenance and language audit missing |
| [AM DeepSeek-R1 think mix](../../lumi-am-deepseek-r1-think/0.0.0/README.md) | Reasoning SFT | Staged; source, correctness, and trace-policy review missing |
| [OpenR1-Math-220k](../../lumi-openr1-math-220k/0.0.0/README.md) | Reasoning/DPO/RLVR | Public upstream plus local materialization; pin local revision |
| [Glaive Code Assistant v3](../../lumi-glaive-code-assistant-v3/0.0.0/README.md) | Code SFT | Public upstream plus local materialization; execute/filter samples |
| [BookSum](../../lumi-booksum/0.0.0/README.md) | Long summarization | Legal/content reconstruction required |
| [FLORES-200/FLORES+](../../lumi-flores-200/0.0.0/README.md) | Evaluation | Protected; never train |
| [Tatoeba English–Finnish](../../lumi-tatoeba-eng-fin/0.0.0/README.md) | Evaluation | Protected; never train |

Other top-level families observed on 2026-08-18 include `SFTTrainer_format`
(about 773 GB), `DPOTrainer_format` (about 5.5 GB), HelpSteer3, Llama-Nemotron,
Nemotron v2, EuroParl, Wikipedia, FinePDFs-Edu, LMSYS Chat 1M, AlpacaEval, and
ArenaHard. They remain umbrella-level observations until an individual entry
records exact files, provenance, format, and readiness.

For any selected folder, inspect the concrete files and nearby documentation,
pin the upstream version or checksum the bytes, generate row/token/language and
length statistics, review terms, and record the exact conversion before launch.

### Operational state and ownership

- **Owner / lead:** OpenEuroLLM data team
- **Source type:** LUMI catalogue
- **Priority:** P1
- **License / access:** Mixed; LUMI access
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

OpenEuroLLM data team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Every selected file needs ID, revision, license, checksum and lineage.
