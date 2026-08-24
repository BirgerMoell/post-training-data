---
name: "The Stack v2"
slug: "the-stack-v2"
version: "0.0.0"
catalogue_status: "D"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "candidate"
status: "Candidate"
language_keys: ["code"]
language_codes: ["zxx_Zyyy"]
languages: "code"
purpose: "Long code/repository context"
source_type: "HF dataset"
priority: "P3"
curator: "Long-context team"
license_access: "Mixed code licenses"
public_location: "https://huggingface.co/datasets/bigcode/the-stack-v2"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-07-01"
confidence: "High"
source_sheet_row: 95
---

# The Stack v2

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Candidate  
> **Training use:** long-context-extension, continued-pretraining  
> **Recorded languages:** code

## <a id="background">Background</a>

Long code/repository context

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/bigcode/the-stack-v2>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** The Stack v2
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/339>)
- **Seed inventory:** [Data tab, row 95](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A95:Q95>)

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
| License and access | Mixed code licenses |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `zxx_Zyyy` | — | — | — | — | — |

Recorded coverage: code

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/bigcode/the-stack-v2>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 95](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A95:Q95>)
- **Last verified:** 2026-07-01
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed code licenses

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Measure sequence-length distribution and decide whether this is instruction data or continued-pretraining text before tokenization and packing.
- For continued pretraining or Megatron use, record the text field, tokenizer revision, sequence length, packing policy, and the exact derived artifact.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** Long-context team
- **Source type:** HF dataset
- **Priority:** P3
- **License / access:** Mixed code licenses
- **Last verified:** 2026-07-01
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Long-context team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

License filtering and secret scanning required.
