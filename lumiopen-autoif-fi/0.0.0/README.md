---
name: "LumiOpen/AutoIF-FI"
slug: "lumiopen-autoif-fi"
version: "0.0.0"
catalogue_status: "D"
training_types: ["instruction-sft","preference-optimization","reinforcement-learning"]
status_key: "candidate"
status: "Candidate"
language_keys: ["fi"]
language_codes: ["fin_Latn"]
languages: "fi"
purpose: "Finnish verifiable instruction following"
source_type: "HF dataset"
priority: "P2"
curator: "LumiOpen / T4.6"
license_access: "Public; verify card"
public_location: "https://huggingface.co/datasets/LumiOpen/AutoIF-FI"
lumi_location: ""
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-05-11"
confidence: "High"
source_sheet_row: 20
---

# LumiOpen/AutoIF-FI

**[DRAFT] (Version 0.0.0; August 2026)**

> **Operational state:** Candidate  
> **Training use:** instruction-sft, preference-optimization, reinforcement-learning  
> **Recorded languages:** fi

## <a id="background">Background</a>

Finnish verifiable instruction following

## <a id="sources">Data Sources</a>

- **Public or upstream:** [source](<https://huggingface.co/datasets/LumiOpen/AutoIF-FI>)
- **LUMI or other artifact:** Not recorded
- **Upstream / parent:** AutoIF-FI
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/b3mkcaxhybyq5jzyte1r399iye>)
- **Seed inventory:** [Data tab, row 20](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A20:Q20>)

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
| `fin_Latn` | — | — | — | — | — |

Recorded coverage: fi

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/LumiOpen/AutoIF-FI>)
- **LUMI or project artifact:** Not recorded
- **Source register:** [Data register row 20](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A20:Q20>)
- **Last verified:** 2026-05-11
- **Confidence:** High

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Public; verify card

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

- For SFT, confirm the selected split and normalize examples to the conversation format expected by the model's chat template.
- For preference training, verify that each example has an aligned prompt plus chosen and rejected responses, and confirm how translated preferences were produced.
- For RLVR/GRPO, identify the prompt, reference answer, and deterministic verifier or reward before including the source.
- Pin an immutable public revision and record the exact configuration and split used.

### Operational state and ownership

- **Owner / lead:** LumiOpen / T4.6
- **Source type:** HF dataset
- **Priority:** P2
- **License / access:** Public; verify card
- **Last verified:** 2026-05-11
- **Confidence:** High

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

LumiOpen / T4.6

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Reported stronger than translated Tülu persona IF.
