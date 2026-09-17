---
name: "OpenEuroLLM multilingual reasoning signal"
slug: "oellm-multilingual-reasoning-signal"
version: "0.1.0"
catalogue_status: "D"
training_types: ["reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
language_codes: ["mul_Zyyy"]
languages: "34 European macro-languages"
purpose: "Procedural multilingual reasoning with answer, language, and format rewards"
source_type: "Project-generated Parquet"
priority: "P0"
curator: "Birger"
license_access: "Derived prompt-localization layer; retain source attribution and review"
public_location: "https://github.com/BirgerMoell/oellm-rlvr"
lumi_location: "/scratch/project_465002530/training/collection/post-training/2026q3/oellm-multilingual-reasoning-signal/release/20260914"
data_format: "Parquet"
compression: "Snappy"
statistics: {"bytes":544137,"documents":2392,"segments":2392,"characters":null,"tokens":null}
last_verified: "2026-09-17"
confidence: "High"
source_sheet_row: null
---

# OpenEuroLLM multilingual reasoning signal

**[DRAFT] (Version 0.1.0; September 2026)**

## <a id="background">Background</a>

Project-generated procedural multilingual reasoning built and qualified
through [`oellm-rlvr`](https://github.com/BirgerMoell/oellm-rlvr).

## <a id="sources">Data Sources</a>

Four symbolic generator families, pinned OpenEuroLLM language registry, and a
pinned localized-header reference.

## <a id="statistics">Structure & Statistics</a>

2,176 train, 72 profile, and 144 evaluation rows; 544,137 Parquet bytes.

## <a id="metadata">Available Metadata</a>

Generator/version, task family, language, format contract, ground truth,
reward components, source revisions, split IDs, and hashes.

## <a id="languages">European Language Support</a>

Thirty-four automatically gated European macro-languages. Galician and Maltese
are excluded from the automatic promotion gate pending stronger coverage.

## <a id="access">Access Information</a>

The checksummed release is stored at the frontmatter LUMI path; implementation
and run evidence are in the linked GitHub repository.

## <a id="use">Terms of Use</a>

Retain attribution for localized source prompts and approve aggregate release
terms before production promotion.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Reward requires correct answer, target-language compliance, and declared
think/box format. Report the three components separately.

## <a id="quality">Quality, Safety & Exclusions</a>

Train/evaluation ID overlap is zero. Use the profile split to confirm a
non-degenerate reward distribution for the entering checkpoint.

## <a id="curator">Catalogue Curator</a>

Birger.

## <a id="notes">Notes and Next Action</a>

Run native audits and the multilingual-math mix; do not automatically promote
Galician or Maltese.
