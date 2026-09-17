---
name: "birgermoell/oellm-eu-human-benchmarks-grpo"
slug: "birgermoell-oellm-eu-human-benchmarks-grpo"
version: "0.1.0"
catalogue_status: "P"
training_types: ["reinforcement-learning"]
status_key: "candidate"
status: "Candidate"
language_keys: ["multilingual"]
language_codes: ["mul_Zyyy"]
languages: "28 European languages"
purpose: "Redistribution-audited human benchmark prompts with exact rewards"
source_type: "HF dataset"
priority: "P1"
curator: "Birger"
license_access: "Mixed row-level licenses; includes share-alike sources"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-eu-human-benchmarks-grpo"
lumi_location: "/scratch/project_465002530/training/collection/post-training/2026q3/birgermoell-oellm-eu-human-benchmarks-grpo/release/f96729b5"
data_format: "Parquet"
compression: "Snappy"
statistics: {"bytes":37693346,"documents":139164,"segments":139164,"characters":null,"tokens":null}
last_verified: "2026-09-17"
confidence: "High"
source_sheet_row: null
---

# birgermoell/oellm-eu-human-benchmarks-grpo

**[PUBLISHED] (Version 0.1.0; September 2026)**

## <a id="background">Background</a>

Redistribution-audited human benchmark prompts with exact rewards and explicit
contamination metadata.

## <a id="sources">Data Sources</a>

Eleven public human-authored or human-translated sources at pinned revisions;
aggregate revision `f96729b537a7f57f871a067568b11a6a319c0d0d`.

## <a id="statistics">Structure & Statistics</a>

139,164 rows: 99,079 train, 13,348 validation, and 26,737 test. The release
removed 6,571 exact duplicates and contains no unknown-license rows.

## <a id="metadata">Available Metadata</a>

Upstream revision, row-level license, authoring method, source split, semantic
group, contamination status, reward type, and content hash.

## <a id="languages">European Language Support</a>

Twenty-eight European languages, including 18,604 Swedish rows.

## <a id="access">Access Information</a>

Parquet shards, manifest, source register, and README are mirrored at the
frontmatter LUMI path and published at the linked Hub repository.

## <a id="use">Terms of Use</a>

Mixed row-level CC-BY, CC-BY-SA, and Apache terms; preserve every applicable
attribution/share-alike obligation.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Opt-in only and excluded from default mixes. Reserve disjoint source/group
holdouts and disclose every affected upstream benchmark.

## <a id="quality">Quality, Safety & Exclusions</a>

Training contaminates the corresponding public benchmarks; never report them
as independent post-training evidence after overlap.

## <a id="curator">Catalogue Curator</a>

Birger.

## <a id="notes">Notes and Next Action</a>

Use only in a named human-data branch after row-level terms, PII, and native
language samples are reviewed.
