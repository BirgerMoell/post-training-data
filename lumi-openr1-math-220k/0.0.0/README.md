---
name: "OpenR1-Math-220k staged on LUMI"
slug: "lumi-openr1-math-220k"
version: "0.0.0"
catalogue_status: "P"
training_types: ["reasoning-sft","preference-optimization","reinforcement-learning"]
status_key: "staged"
status: "Staged on LUMI — local revision not pinned"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "English"
purpose: "Verified-trace math SFT, preference-pair construction, and RLVR prompt seed"
source_type: "Public dataset with local JSONL materialization"
priority: "P1"
curator: "Open R1 upstream; OpenEuroLLM stage owner unassigned"
license_access: "Apache-2.0 upstream; verify local derivation"
public_location: "https://huggingface.co/datasets/open-r1/OpenR1-Math-220k"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/OpenR1-Math-220k"
data_format: null
compression: null
statistics: {"bytes":null,"documents":null,"segments":null,"characters":null,"tokens":null}
last_verified: "2026-08-18"
confidence: "High for upstream and local files; medium for their lineage"
source_sheet_row: null
---

# OpenR1-Math-220k staged on LUMI

**[PUBLISHED] (Version 0.0.0; August 2026)**

> **Operational state:** Staged on LUMI — local revision not pinned  
> **Training use:** reasoning-sft, preference-optimization, reinforcement-learning  
> **Recorded languages:** English

## <a id="background">Background</a>

OpenR1-Math-220k provides math problems with multiple DeepSeek-R1-generated
reasoning traces and correctness metadata. The public card describes 220k
problems, a recommended `default` subset of about 94k problems, and verification
with Math Verify for most samples. It is suitable for reasoning SFT after trace
selection, pair construction from trace scores, or prompts for verifier-based
training.

## <a id="sources">Data Sources</a>

- **Public source:** [open-r1/OpenR1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k)
- **Current public revision observed 2026-08-18:** `e4e141ec9dea9f8326f4d347be56105859b2bd68`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/OpenR1-Math-220k`
- **Local default JSONL:** `default-train.jsonl` — 5,116,576,246 bytes
- **Local sample:** `default-train-sample-10.jsonl` — 602,414 bytes
- **Observed columns:** `answer`, correctness fields, finish reasons,
  generations, IDs, messages, problem/source types, solution, and source
- **Evidence:** Direct read-only LUMI inspection and public dataset card on 2026-08-18

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
| License and access | Apache-2.0 upstream; verify local derivation |

## <a id="languages">European Language Support</a>

| Code(s) | Documents | Segments | Tokens | Length | Characters |
| --- | ---: | ---: | ---: | ---: | ---: |
| `eng_Latn` | — | — | — | — | — |

Recorded coverage: English

Language codes use ISO 639-3 plus ISO 15924, matching the OpenEuroLLM training-data catalogue convention. Broad multilingual entries remain unenumerated until their per-language composition is measured.

## <a id="access">Access Information</a>

- **Public or upstream:** [public or upstream](<https://huggingface.co/datasets/open-r1/OpenR1-Math-220k>)
- **LUMI or project artifact:** `/scratch/project_462000963/datasets/posttraining_data/OpenR1-Math-220k`
- **Source register:** Catalogue-only discovery; no seed-register row
- **Last verified:** 2026-08-18
- **Confidence:** High for upstream and local files; medium for their lineage

A recorded path means that the artifact existed at the verification date. Recheck storage, access permissions, revision, configuration, split, and checksums before a run.

## <a id="use">Terms of Use</a>

Apache-2.0 upstream; verify local derivation

Verify the terms of every upstream component and transformed artifact before use; this catalogue statement is operational metadata, not legal clearance.

## <a id="post-training-use">Post-Training Use & Readiness</a>

1. Re-materialize the chosen `default` revision or prove the local JSONL's
   lineage with a checksum and build record. The current public revision is not
   necessarily the revision that produced the local file.
2. Keep only complete, independently verified traces and one held-out dev set
   stratified by source and problem type.
3. For SFT, select or sample correct traces rather than multiplying nearly
   identical problems unintentionally. Decide whether think tokens are visible,
   masked, or removed.
4. For DPO, construct chosen/rejected pairs only when the score difference is
   meaningful and the final answer/verifier agrees.
5. For RLVR, train on prompts only and keep the reference answer plus verifier
   outside the model input. Pin the Math Verify version and sandbox limits.
6. Decontaminate against AIME, GSM, MATH, exams, and every protected math set.

### Operational state and ownership

- **Owner / lead:** Open R1 upstream; OpenEuroLLM stage owner unassigned
- **Source type:** Public dataset with local JSONL materialization
- **Priority:** P1
- **License / access:** Apache-2.0 upstream; verify local derivation
- **Last verified:** 2026-08-18
- **Confidence:** High for upstream and local files; medium for their lineage

## <a id="quality">Quality, Safety & Exclusions</a>

Before production use, record license/access approval, privacy and PII review, quality filters, deduplication, benchmark-contamination checks, language-balance results, and any excluded subsets. A published catalogue entry is not by itself a legal, safety, or quality approval.

## <a id="curator">Catalogue Curator</a>

Open R1 upstream; OpenEuroLLM stage owner unassigned

This is the recorded operational owner or lead. Catalogue review and release approval may be assigned separately.

## <a id="notes">Notes and Next Action</a>

Pin the exact local derivation, then compare this source with Dolci Think and
the LUMI AM mixture on matched, decontaminated math tokens.
