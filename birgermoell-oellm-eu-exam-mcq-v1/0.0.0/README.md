---
name: "birgermoell/oellm-eu-exam-mcq-v1"
slug: "birgermoell-oellm-eu-exam-mcq-v1"
version: "0.0.0"
catalogue_status: "P"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual","code"]
language_codes: ["zxx_Zyyy"]
languages: "35 language codes"
purpose: "European exam rewards and preference pairs"
source_type: "HF dataset"
priority: "P1"
curator: "Birger"
license_access: "Mixed; row-filterable"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/exam_mcq/oellm-eu-exam-mcq-v1"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-06-23"
confidence: "High"
source_sheet_row: 49
---

# birgermoell/oellm-eu-exam-mcq-v1

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** preference-optimization, reinforcement-learning  
> **Recorded languages:** 35 language codes

## <a id="background">Background</a>

European exam rewards and preference pairs

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/exam_mcq/oellm-eu-exam-mcq-v1`
- **Upstream / parent:** 28 source registry entries
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/docs/EU_EXAM_MCQ_DATASET.md>)
- **Seed inventory:** [Data tab, row 49](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A49:Q49>)

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
| License and access | Mixed; row-filterable |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `zxx_Zyyy` | — | — | — | — | — |

Recorded coverage: 35 language codes

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1>)
- **LUMI or project artifact:** `/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/exam_mcq/oellm-eu-exam-mcq-v1`
- **Source register:** [Data register row 49](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A49:Q49>)
- **Last verified:** 2026-06-23
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed; row-filterable

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Mixed; row-filterable
- **Last verified:** 2026-06-23
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

582,983 GRPO rows; 1,936,764 DPO pairs.
