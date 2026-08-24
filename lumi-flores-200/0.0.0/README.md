---
name: "FLORES-200 / FLORES+ evaluation copy on LUMI"
slug: "lumi-flores-200"
version: "0.0.0"
catalogue_status: "P"
training_types: ["evaluation-holdouts"]
status_key: "eval-only"
status: "Evaluation-only — do not train"
language_keys: ["bg","cs","da","de","el","en","es","et","fi","fr","ga","hr","hu","is","it","lt","lv","mt","nl","no","pl","pt","ro","sk","sl","sv"]
language_codes: ["bul_Cyrl","ces_Latn","dan_Latn","deu_Latn","ell_Grek","eng_Latn","spa_Latn","est_Latn","ekk_Latn","fin_Latn","fra_Latn","gle_Latn","hrv_Latn","hun_Latn","isl_Latn","ita_Latn","lit_Latn","lav_Latn","ltg_Latn","lvs_Latn","mlt_Latn","nld_Latn","nor_Latn","nno_Latn","nob_Latn","pol_Latn","por_Latn","ron_Latn","slk_Latn","slv_Latn","swe_Latn"]
languages: "26 European language files plus FLORES+ combined dev/devtest"
purpose: "Parallel multilingual translation and language-retention evaluation"
source_type: "Local evaluation copy"
priority: "P0 protected holdout"
curator: "Evaluation team"
license_access: "Verify exact FLORES/FLORES+ release terms"
public_location: "https://huggingface.co/datasets/openlanguagedata/flores_plus"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/FLORES-200"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18 by direct LUMI inspection"
confidence: "High for files; medium for local lineage"
source_sheet_row: null
---

# FLORES-200 / FLORES+ evaluation copy on LUMI

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Evaluation-only — do not train  
> **Training use:** evaluation-holdouts  
> **Recorded languages:** 26 European language files plus FLORES+ combined dev/devtest

## <a id="background">Background</a>

This local copy provides aligned development and development-test material for
translation and multilingual retention checks. It is especially useful for a
single repeatable language gate after each training stage. It is not an
instruction dataset and must not enter training or synthetic prompt generation.

## <a id="sources">Data Sources</a>

- **Public/upstream:** FLORES+ link recorded above; the exact local build revision is not recorded
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/FLORES-200`
- **Combined files:** `floresplus_dev.jsonl` — 135,375,515 bytes;
  `floresplus_devtest.jsonl` — 134,001,541 bytes
- **Per-language files:** `{iso}-dev.jsonl`, `{iso}-devtest.jsonl`, and text counterparts
- **Observed JSON fields:** `id`, `text`, ISO/glottocode/script metadata,
  domain, topic, URL, hyperlink/image flags, and update date
- **Evidence:** Direct read-only LUMI inspection on 2026-08-18

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
| License and access | Verify exact FLORES/FLORES+ release terms |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `bul_Cyrl` | — | — | — | — | — |
| `ces_Latn` | — | — | — | — | — |
| `dan_Latn` | — | — | — | — | — |
| `deu_Latn` | — | — | — | — | — |
| `ell_Grek` | — | — | — | — | — |
| `eng_Latn` | — | — | — | — | — |
| `spa_Latn` | — | — | — | — | — |
| `est_Latn` | — | — | — | — | — |
| `ekk_Latn` | — | — | — | — | — |
| `fin_Latn` | — | — | — | — | — |
| `fra_Latn` | — | — | — | — | — |
| `gle_Latn` | — | — | — | — | — |
| `hrv_Latn` | — | — | — | — | — |
| `hun_Latn` | — | — | — | — | — |
| `isl_Latn` | — | — | — | — | — |
| `ita_Latn` | — | — | — | — | — |
| `lit_Latn` | — | — | — | — | — |
| `lav_Latn` | — | — | — | — | — |
| `ltg_Latn` | — | — | — | — | — |
| `lvs_Latn` | — | — | — | — | — |
| `mlt_Latn` | — | — | — | — | — |
| `nld_Latn` | — | — | — | — | — |
| `nor_Latn` | — | — | — | — | — |
| `nno_Latn` | — | — | — | — | — |
| `nob_Latn` | — | — | — | — | — |
| `pol_Latn` | — | — | — | — | — |
| `por_Latn` | — | — | — | — | — |
| `ron_Latn` | — | — | — | — | — |
| `slk_Latn` | — | — | — | — | — |
| `slv_Latn` | — | — | — | — | — |
| `swe_Latn` | — | — | — | — | — |

Recorded coverage: 26 European language files plus FLORES+ combined dev/devtest

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/openlanguagedata/flores_plus>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/FLORES-200`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for files; medium for local lineage

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Verify exact FLORES/FLORES+ release terms

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Pin the upstream/local lineage, freeze the devtest IDs, and build consistent
translation directions from aligned IDs. Report results per language and
direction with the exact prompting/scoring code. Add every source and target
string to the decontamination index before any SFT, preference, or RLVR freeze.

### Operational state and ownership

- **Owner / lead:** Evaluation team
- **Source type:** Local evaluation copy
- **Priority:** P0 protected holdout
- **License / access:** Verify exact FLORES/FLORES+ release terms
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High for files; medium for local lineage

## <a id="quality">Quality, Safety & Exclusions</a>

**Protected evaluation artifact: never use for training.** Keep all prompts, answers, translations, and derived variants out of SFT, preference, RLVR, continued-pretraining, RAG, and synthetic-data generation inputs. Add stable identifiers and content hashes to the decontamination registry before every training freeze.

## <a id="curator">Catalogue Curator</a>

Evaluation team

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Record the upstream revision and alignment script, then make this part of the
common per-language checkpoint gate.
