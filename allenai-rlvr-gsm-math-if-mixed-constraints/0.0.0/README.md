---
name: "allenai/RLVR-GSM-MATH-IF-Mixed-Constraints"
slug: "allenai-rlvr-gsm-math-if-mixed-constraints"
version: "0.0.0"
catalogue_status: "D"
training_types: ["reinforcement-learning"]
status_key: "staged"
status: "Staged"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "primarily en"
purpose: "Verifiable math + IF rewards"
source_type: "HF dataset"
priority: "P1"
curator: "T4.6"
license_access: "ODC-BY-1.0 aggregate; subset terms apply"
public_location: "https://huggingface.co/datasets/allenai/RLVR-GSM-MATH-IF-Mixed-Constraints"
lumi_location: "/scratch/project_465002530/training/collection/post-training/2026q3/allenai-rlvr-gsm-math-if-mixed-constraints/source/7dbd180f"
data_format: "Parquet"
compression: "Snappy"
statistics: {"bytes":16533143,"documents":29946,"segments":29946,"characters":null,"tokens":null}
last_verified: "2026-09-17"
confidence: "High"
source_sheet_row: 57
---

# allenai/RLVR-GSM-MATH-IF-Mixed-Constraints

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Staged
> **Training use:** reinforcement-learning  
> **Recorded languages:** primarily en

## <a id="background">Background</a>

Verifiable math + IF rewards

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/allenai/RLVR-GSM-MATH-IF-Mixed-Constraints>)
- **LUMI or other artifact:** `/scratch/project_465002530/training/collection/post-training/2026q3/allenai-rlvr-gsm-math-if-mixed-constraints/source/7dbd180f`
- **Upstream / parent:** RLVR constraints
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/scripts/stage_data_lumi.sh>)
- **Seed inventory:** [Data tab, row 57](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A57:Q57>)

## <a id="statistics">Structure & Statistics</a>

The pinned source revision contains 29,946 rows in one Parquet shard.

| Measure | Value |
| --- | ---: |
| Bytes | 16,533,143 |
| Documents | 29,946 |
| Segments | 29,946 |
| Characters | — |
| Tokens | — |
| Data format | Parquet |
| Compression | Snappy |

## <a id="metadata">Available Metadata</a>

| Field | Status |
| --- | --- |
| Identity and intended post-training use | Recorded in this entry |
| Public and project-storage locations | Recorded when known; verify before use |
| Operational owner, priority, and confidence | Recorded from the project data register or repository evidence |
| Schema, columns, and splits | See source and structure evidence; inventory if absent |
| Immutable revision and checksums | Required for a production manifest; may still be missing |
| License and access | ODC-BY-1.0 aggregate; separate subset terms apply |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: primarily en

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/allenai/RLVR-GSM-MATH-IF-Mixed-Constraints>)
- **LUMI or project artifact:** `/scratch/project_465002530/training/collection/post-training/2026q3/allenai-rlvr-gsm-math-if-mixed-constraints/source/7dbd180f`
- **Source register:** [Data register row 57](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A57:Q57>)
- **Last verified:** 2026-09-17
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

ODC-BY-1.0 for the aggregate; different terms apply to subsets. Review the
included license files before production promotion.

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** ODC-BY-1.0 aggregate; subset terms apply
- **Last verified:** 2026-09-17
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Pinned revision `7dbd180f5440c0b90f2944e6efea934b85437a95` is staged with
SHA-256 `d4ff1f9c054129bfad71876be125c58c5eb18b4d57e8729c86fcfc126f2df300`.
Qualify and prefer the instruction-following slice; the GSM8K/MATH rows
contaminate those public benchmarks and overlap the primary math curriculum.
