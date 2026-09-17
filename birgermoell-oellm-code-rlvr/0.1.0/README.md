---
name: "birgermoell/oellm-code-rlvr"
slug: "birgermoell-oellm-code-rlvr"
version: "0.1.0"
catalogue_status: "P"
training_types: ["reinforcement-learning"]
status_key: "candidate"
status: "Candidate"
language_keys: ["en", "code"]
language_codes: ["eng_Latn", "zxx_Zyyy"]
languages: "English prompts; Python solutions"
purpose: "Deterministic Python stdin/stdout tasks with hidden tests"
source_type: "HF dataset and deterministic generator"
priority: "P0"
curator: "Birger"
license_access: "Apache-2.0"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-code-rlvr"
lumi_location: "/scratch/project_465002530/training/collection/post-training/2026q3/birgermoell-oellm-code-rlvr/release/e1cae771"
data_format: "Parquet"
compression: "Snappy"
statistics: {"bytes":91129161,"documents":100000,"segments":100000,"characters":null,"tokens":null}
last_verified: "2026-09-17"
confidence: "High"
source_sheet_row: null
---

# birgermoell/oellm-code-rlvr

**[PUBLISHED] (Version 0.1.0; September 2026)**

## <a id="background">Background</a>

100,000 deterministic Python stdin/stdout tasks across twelve balanced
generator families, with 10–13 hidden tests per task.

## <a id="sources">Data Sources</a>

- Pinned Hub revision: `e1cae7711049e3b5ff021fb3e9c752424882998c`
- Generation: deterministic project generators, not copied benchmark text

## <a id="statistics">Structure & Statistics</a>

95,099 train, 2,477 validation, and 2,424 test rows; 91,129,161 Parquet bytes.

## <a id="metadata">Available Metadata</a>

Prompts, public/hidden tests, reference programs, generator seeds/families,
mutation scores, limits, contamination groups, and verifier versions.

## <a id="languages">European Language Support</a>

English specifications and Python solutions.

## <a id="access">Access Information</a>

The full release and checksummed manifest are mirrored at the frontmatter LUMI
path and published at the linked Hub repository.

## <a id="use">Terms of Use</a>

Apache-2.0.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Qualify the LUMI execution sandbox before optimizer updates. Neither hidden
tests nor `reference_solution` may be placed in model context.

## <a id="quality">Quality, Safety & Exclusions</a>

Run completions as untrusted code with no network, read-only inputs, bounded
CPU/RAM/process count/output, and hard timeouts. Infrastructure failures are
not wrong-answer rewards.

## <a id="curator">Catalogue Curator</a>

Birger.

## <a id="notes">Notes and Next Action</a>

Re-run reference solutions and sandbox failure classification, then profile
pass rates by family and difficulty.
