---
name: "openeurollm/EU-Instruct-Synthetic"
slug: "openeurollm-eu-instruct-synthetic"
version: "0.0.0"
catalogue_status: "P"
training_types: ["instruction-sft"]
status_key: "published"
status: "Published / available"
language_keys: ["cs","de","el","es","fr","it","nl","pl","pt","ro","uk"]
language_codes: ["ces_Latn","deu_Latn","ell_Grek","spa_Latn","fra_Latn","ita_Latn","nld_Latn","pol_Latn","por_Latn","ron_Latn","ukr_Cyrl"]
languages: "cs,de,el,es,fr,it,nl,pl,pt,ro,uk"
purpose: "Large multilingual synthetic instructions"
source_type: "HF dataset"
priority: "P1"
curator: "Abhash / T4.6"
license_access: "Public; verify card"
public_location: "https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 through the Hugging Face API"
confidence: "High"
source_sheet_row: 12
---

# openeurollm/EU-Instruct-Synthetic

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Published / available  
> **Training use:** instruction-sft  
> **Recorded languages:** cs,de,el,es,fr,it,nl,pl,pt,ro,uk

## <a id="background">Background</a>

Approximately 1.5 million single-turn synthetic instruction/response pairs for
11 European languages. The public dataset uses `messages` and `language`
columns and is Apache-2.0 licensed.

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic>)
- **Pinned revision observed 2026-08-18:** `c13be5d71144feb1007708aae2a8c2d823f8e59a`
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Synthetic IF pipeline
- **Evidence:** [evidence](<https://github.com/OpenEuroLLM/Taskboard/issues/345>)
- **Seed inventory:** [Data tab, row 12](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A12:Q12>)

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
| License and access | Public; verify card |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ces_Latn` | — | — | — | — | — |
| `deu_Latn` | — | — | — | — | — |
| `ell_Grek` | — | — | — | — | — |
| `spa_Latn` | — | — | — | — | — |
| `fra_Latn` | — | — | — | — | — |
| `ita_Latn` | — | — | — | — | — |
| `nld_Latn` | — | — | — | — | — |
| `pol_Latn` | — | — | — | — | — |
| `por_Latn` | — | — | — | — | — |
| `ron_Latn` | — | — | — | — | — |
| `ukr_Cyrl` | — | — | — | — | — |

Recorded coverage: cs,de,el,es,fr,it,nl,pl,pt,ro,uk

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openeurollm/EU-Instruct-Synthetic>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 12](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A12:Q12>)
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Public; verify card

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Use the `all` configuration for a common multilingual pool or the per-language
  configurations for explicit language weighting.
- Apply the model's exact chat template and train only assistant response tokens.
- Sample constraint-following correctness, language purity, translationese,
  factuality, and synthetic-template duplication before assigning production weight.
- Pin the revision, configuration, split, chat template, and row counts.

### Operational state and ownership

- **Owner / lead:** Abhash / T4.6
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Public; verify card
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Abhash / T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

1,497,276 pairs are reported by the source inventory. This is strong breadth
data but should not be the only source for any language: pair it with translated
Dolci and native or human-authored material, then validate the mix per language.
