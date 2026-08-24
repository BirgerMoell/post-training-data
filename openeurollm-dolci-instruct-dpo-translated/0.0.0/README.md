---
name: "openeurollm/Dolci-Instruct-DPO-translated"
slug: "openeurollm-dolci-instruct-dpo-translated"
version: "0.0.0"
catalogue_status: "P"
training_types: ["preference-optimization"]
status_key: "published"
status: "Published / available"
language_keys: ["cs","de","el","es","fi","fr","it","pl","ro","sv","uk"]
language_codes: ["ces_Latn","deu_Latn","ell_Grek","spa_Latn","fin_Latn","fra_Latn","ita_Latn","pol_Latn","ron_Latn","swe_Latn","ukr_Cyrl"]
languages: "cs,de,el,es,fi,fr,it,pl,ro,sv,uk (+ en config)"
purpose: "Multilingual preference alignment"
source_type: "HF dataset"
priority: "P1"
curator: "OpenEuroLLM / MultiSynt"
license_access: "Inherited + translation provenance"
public_location: "https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 through the Hugging Face API"
confidence: "High"
source_sheet_row: 39
---

# openeurollm/Dolci-Instruct-DPO-translated

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Published / available  
> **Training use:** preference-optimization  
> **Recorded languages:** cs,de,el,es,fi,fr,it,pl,ro,sv,uk (+ en config)

## <a id="background">Background</a>

Multilingual preference alignment

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated>)
- **Pinned revision observed 2026-08-18:** `b231fb0cc857840d4731b180cc910d5f5d1f523e`
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** Dolci DPO + translation
- **Evidence:** [evidence](<https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated>)
- **Seed inventory:** [Data tab, row 39](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A39:Q39>)

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
| License and access | Inherited + translation provenance |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ces_Latn` | — | — | — | — | — |
| `deu_Latn` | — | — | — | — | — |
| `ell_Grek` | — | — | — | — | — |
| `spa_Latn` | — | — | — | — | — |
| `fin_Latn` | — | — | — | — | — |
| `fra_Latn` | — | — | — | — | — |
| `ita_Latn` | — | — | — | — | — |
| `pol_Latn` | — | — | — | — | — |
| `ron_Latn` | — | — | — | — | — |
| `swe_Latn` | — | — | — | — | — |
| `ukr_Cyrl` | — | — | — | — | — |

Recorded coverage: cs,de,el,es,fi,fr,it,pl,ro,sv,uk (+ en config)

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openeurollm/Dolci-Instruct-DPO-translated>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 39](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A39:Q39>)
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Inherited + translation provenance

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- Load one configuration per language and retain the prompt/chosen/rejected
  relationship through templating.
- Verify that translation did not reverse or erase the preference margin,
  especially for style- and safety-sensitive pairs.
- Pin the revision, configurations, split, template, maximum lengths, and the
  sampled row count after filtering.

### Operational state and ownership

- **Owner / lead:** OpenEuroLLM / MultiSynt
- **Source type:** HF dataset
- **Priority:** P1
- **License / access:** Inherited + translation provenance
- **Last verified:** 2026-08-18 through the Hugging Face API
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

OpenEuroLLM / MultiSynt

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Validate preference consistency after translation.
