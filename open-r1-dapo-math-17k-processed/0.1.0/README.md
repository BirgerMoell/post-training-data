---
name: "open-r1/DAPO-Math-17k-Processed"
slug: "open-r1-dapo-math-17k-processed"
version: "0.1.0"
catalogue_status: "D"
training_types: ["reinforcement-learning"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en"]
language_codes: ["eng_Latn"]
languages: "en"
purpose: "Competition-math prompt pool for deterministic RLVR"
source_type: "HF dataset"
priority: "P0"
curator: "Open R1 / Birger"
license_access: "Verify upstream terms before production promotion"
public_location: "https://huggingface.co/datasets/open-r1/DAPO-Math-17k-Processed"
lumi_location: "/scratch/project_465002530/training/collection/post-training/2026q3/open-r1-dapo-math-17k-processed/release/31dd3095"
data_format: "Parquet"
compression: "Snappy"
statistics: {"bytes":3552189,"documents":13980,"segments":13980,"characters":null,"tokens":null}
last_verified: "2026-09-17"
confidence: "High"
source_sheet_row: null
---

# open-r1/DAPO-Math-17k-Processed

**[DRAFT] (Version 0.1.0; September 2026)**

## <a id="background">Background</a>

Prompt-only competition-math candidate prepared for deterministic online RLVR.

## <a id="sources">Data Sources</a>

English configuration at pinned upstream revision
`31dd309567e3da778038cc87d868b6097a3ccf68`.

## <a id="statistics">Structure & Statistics</a>

The materializer normalized 14,116 source rows into 13,980 non-conflicting
prompt groups: 12,700 train, 256 calibration, and 1,024 evaluation.

## <a id="metadata">Available Metadata</a>

Stable ID, user messages, separate ground truth, verifier style, ability,
semantic group, source revision/configuration, split seed, and file hashes.

## <a id="languages">European Language Support</a>

English.

## <a id="access">Access Information</a>

Pinned raw source and transformed release are stored at the frontmatter LUMI
path; the upstream repository is linked above.

## <a id="use">Terms of Use</a>

Verify inherited upstream terms before production promotion.

## <a id="post-training-use">Post-Training Use & Readiness</a>

The policy sees only a user message; the math verifier receives ground truth
separately. Published solution traces and source prompts are absent from all
policy artifacts.

## <a id="quality">Quality, Safety & Exclusions</a>

The release dropped 126 agreeing duplicates and all ten rows from five
conflicting prompt groups. Its three splits have zero ID overlap.

## <a id="curator">Catalogue Curator</a>

Open R1 / Birger.

## <a id="notes">Notes and Next Action</a>

Run the 256-row rollout calibration and the checked-in DAPO smoke before any
longer optimization.
