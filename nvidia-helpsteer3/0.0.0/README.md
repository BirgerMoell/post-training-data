---
name: "nvidia/HelpSteer3"
slug: "nvidia-helpsteer3"
version: "0.0.0"
catalogue_status: "D"
training_types: ["preference-optimization"]
status_key: "configured-runnable"
status: "Configured / runnable"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "primarily en"
purpose: "Preference/RM candidate"
source_type: "Pinned personal LUMI staging"
priority: "P1"
curator: "T4.6"
license_access: "Verify NVIDIA terms"
public_location: "https://huggingface.co/datasets/nvidia/HelpSteer3"
lumi_location: "/scratch/project_465002530/users/bmoell/helpsteer3-dpo/artifacts/data"
data_format: "Gzip JSONL"
compression: "gzip"
statistics: {"bytes":111971991,"documents":40476,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-09-17 on LUMI"
confidence: "High"
source_sheet_row: 47
---

# nvidia/HelpSteer3

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Configured / runnable
> **Training use:** preference-optimization  
> **Recorded languages:** primarily en

## <a id="background">Background</a>

Preference/RM candidate

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/nvidia/HelpSteer3>)
- **Pinned runnable staging:** `/scratch/project_465002530/users/bmoell/helpsteer3-dpo/artifacts/data`
- **Older shared catalogue path:** `/scratch/project_462000963/datasets/posttraining_data/HelpSteer3` (not readable by the current account on 2026-09-17)
- **Upstream / parent:** HelpSteer3
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/230>)
- **Seed inventory:** [Data tab, row 47](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A47:Q47>)

## <a id="statistics">Structure & Statistics</a>

The pinned staging contains the fixed Preference train and validation splits.
The DPO transform removes ties rather than inventing an ordering.

| Measure | Value |
| --- | ---: |
| Bytes | 111,971,991 |
| Documents | 40,476 raw preference rows |
| Segments | — |
| Characters | — |
| Tokens | — |
| Data format | JSONL |
| Compression | gzip |

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

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/nvidia/HelpSteer3>)
- **LUMI or project artifact:** `/scratch/project_465002530/users/bmoell/helpsteer3-dpo/artifacts/data`
- **Source register:** [Data register row 47](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A47:Q47>)
- **Last verified:** 2026-09-17 on LUMI
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Verify NVIDIA terms

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- Pin an immutable public revision and record the exact configuration and split used.
- Use the pinned train checksum `32b52e1d378f8dab1e4c9ae549da49a5d6fc0875aeafe3f9139e6053beb906bb`
  and validation checksum `cd0d8b6efd7869a44c1b5ff91701232062555829b3c838abfd770d7dab6c7861`.
- Exclude the 2,160 train ties and 97 validation ties from DPO while retaining
  them for reward-model or calibration work.

### Operational state and ownership

- **Owner / lead:** T4.6
- **Source type:** Pinned personal LUMI staging
- **Priority:** P1
- **License / access:** Verify NVIDIA terms
- **Last verified:** 2026-09-17 on LUMI
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Configured in `OpenEuroLLM/post-training` at immutable source revision
`f6d145777bcbde96137596340fab89793acd1031`. Promote the pinned files into a
shared canonical collection release before a production run.
