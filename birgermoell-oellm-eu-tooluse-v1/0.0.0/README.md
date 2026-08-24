---
name: "birgermoell/oellm-eu-tooluse-v1"
slug: "birgermoell-oellm-eu-tooluse-v1"
version: "0.0.0"
catalogue_status: "P"
training_types: ["reinforcement-learning","tool-and-agentic"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "en"
purpose: "Qwen-native tool SFT + verifiable RL"
source_type: "HF dataset"
priority: "P1"
curator: "Birger"
license_access: "Apache-2.0"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-tooluse-v1"
lumi_location: "/scratch/project_465002530/users/bmoell/posttrain-data/eu-tooluse-parquet"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-07-02"
confidence: "High"
source_sheet_row: 67
---

# birgermoell/oellm-eu-tooluse-v1

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** reinforcement-learning, tool-and-agentic  
> **Recorded languages:** en

## <a id="background">Background</a>

Qwen-native tool SFT + verifiable RL

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-tooluse-v1>)
- **LUMI or other artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/eu-tooluse-parquet`
- **Upstream / parent:** Glaive v2 + ToolACE + Hermes
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/dataset_cards/oellm-eu-tooluse-v1-README.md>)
- **Seed inventory:** [Data tab, row 67](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A67:Q67>)

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
| License and access | Apache-2.0 |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/birgermoell/oellm-eu-tooluse-v1>)
- **LUMI or project artifact:** `/scratch/project_465002530/users/bmoell/posttrain-data/eu-tooluse-parquet`
- **Source register:** [Data register row 67](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A67:Q67>)
- **Last verified:** 2026-07-02
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Apache-2.0

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.
- Verify the recorded LUMI path still exists and inspect the concrete files, counts, and neighboring documentation before launching a run.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Apache-2.0
- **Last verified:** 2026-07-02
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

55,077 SFT; 46,366 GRPO; ~10% completed 4B mix.
