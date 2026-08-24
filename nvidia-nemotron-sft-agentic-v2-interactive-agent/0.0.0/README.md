---
name: "nvidia/Nemotron-SFT-Agentic-v2 — interactive-agent"
slug: "nvidia-nemotron-sft-agentic-v2-interactive-agent"
version: "0.0.0"
catalogue_status: "P"
training_types: ["tool-and-agentic"]
status_key: "used-in-research"
status: "Used in research run"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "primarily en"
purpose: "Interactive trajectories"
source_type: "HF dataset"
priority: "P2"
curator: "T4.6 function-calling"
license_access: "Verify NVIDIA terms"
public_location: "https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-03"
confidence: "High"
source_sheet_row: 76
---

# nvidia/Nemotron-SFT-Agentic-v2 — interactive-agent

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in research run  
> **Training use:** tool-and-agentic  
> **Recorded languages:** primarily en

## <a id="background">Background</a>

Interactive trajectories

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Nemotron SFT Agentic v2
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/220>)
- **Seed inventory:** [Data tab, row 76](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A76:Q76>)

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
| License and access | Verify NVIDIA terms |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: primarily en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 76](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A76:Q76>)
- **Last verified:** 2026-08-03
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Verify NVIDIA terms

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Preserve tool schemas, calls, arguments, outputs, and abstention examples; validate that the target chat template can represent them.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** T4.6 function-calling
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-08-03
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6 function-calling

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

One of five current mixture sources.
