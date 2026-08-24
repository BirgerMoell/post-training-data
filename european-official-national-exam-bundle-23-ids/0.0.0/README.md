---
name: "European official/national exam bundle (23 IDs)"
slug: "european-official-national-exam-bundle-23-ids"
version: "0.0.0"
catalogue_status: "P"
training_types: ["preference-optimization","reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["en","sv","da","cs","es","it","pl","sq","bg","ca","et","sk","eu"]
language_codes: ["eng_Latn","swe_Latn","dan_Latn","ces_Latn","spa_Latn","ita_Latn","pol_Latn","sqi_Latn","als_Latn","bul_Cyrl","cat_Latn","est_Latn","ekk_Latn","slk_Latn","eus_Latn"]
languages: "sq,bg,ca,cs,da,en,es,et,eu,it,pl,sk,sv"
purpose: "Native exam/licensing/civic MCQs"
source_type: "Public/HF bundle"
priority: "P1"
curator: "Birger"
license_access: "Mixed: permissive, NC, custom, unknown"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-06-23"
confidence: "High"
source_sheet_row: 56
---

# European official/national exam bundle (23 IDs)

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Used in completed run  
> **Training use:** preference-optimization, reinforcement-learning  
> **Recorded languages:** sq,bg,ca,cs,da,en,es,et,eu,it,pl,sk,sv

## <a id="background">Background</a>

Native exam/licensing/civic MCQs

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** UHR; CKE/PES/LEK/LDEK; Danish citizenship; Estonian/Bulgarian/Albanian/Czech/Italian/Slovak/Basque/Catalan/Spanish sources
- **Evidence:** [evidence](<https://github.com/BirgerMoell/qwen35-posttrain/blob/main/data/exam_mcq/oellm-eu-exam-mcq-v1/source_registry.json>)
- **Seed inventory:** [Data tab, row 56](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A56:Q56>)

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
| License and access | Mixed: permissive, NC, custom, unknown |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |
| `swe_Latn` | — | — | — | — | — |
| `dan_Latn` | — | — | — | — | — |
| `ces_Latn` | — | — | — | — | — |
| `spa_Latn` | — | — | — | — | — |
| `ita_Latn` | — | — | — | — | — |
| `pol_Latn` | — | — | — | — | — |
| `sqi_Latn` | — | — | — | — | — |
| `als_Latn` | — | — | — | — | — |
| `bul_Cyrl` | — | — | — | — | — |
| `cat_Latn` | — | — | — | — | — |
| `est_Latn` | — | — | — | — | — |
| `ekk_Latn` | — | — | — | — | — |
| `slk_Latn` | — | — | — | — | — |
| `eus_Latn` | — | — | — | — | — |

Recorded coverage: sq,bg,ca,cs,da,en,es,et,eu,it,pl,sk,sv

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/birgermoell/oellm-eu-exam-mcq-v1>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 56](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A56:Q56>)
- **Last verified:** 2026-06-23
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Mixed: permissive, NC, custom, unknown

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** Birger
- **Source type:** Public/HF bundle
- **Priority:** P1
- **License / access:** Mixed: permissive, NC, custom, unknown
- **Last verified:** 2026-06-23
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Birger

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Use child registry; exclude unknown/NC for permissive runs.
