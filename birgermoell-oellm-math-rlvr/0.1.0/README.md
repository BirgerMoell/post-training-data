---
name: "birgermoell/oellm-math-rlvr"
slug: "birgermoell-oellm-math-rlvr"
version: "0.1.0"
catalogue_status: "P"
training_types: ["reinforcement-learning"]
status_key: "used-in-completed-run"
status: "Used in completed run"
language_keys: ["multilingual"]
language_codes: ["mul_Zyyy"]
languages: "24 EU languages"
purpose: "Deterministic procedural mathematics for RLVR"
source_type: "HF dataset and deterministic generator"
priority: "P0"
curator: "Birger"
license_access: "Apache-2.0"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-math-rlvr"
lumi_location: "/scratch/project_465002530/training/collection/post-training/2026q3/birgermoell-oellm-math-rlvr/release/0ffc9d6c"
data_format: "Parquet"
compression: "Snappy"
statistics: {"bytes":92260850,"documents":1000000,"segments":1000000,"characters":null,"tokens":null}
last_verified: "2026-09-17"
confidence: "High"
source_sheet_row: null
---

# birgermoell/oellm-math-rlvr

**[PUBLISHED] (Version 0.1.0; September 2026)**

## <a id="background">Background</a>

One million deterministic procedural mathematics prompts spanning 28 families
and 24 EU languages. Rewards use versioned integer- or rational-equivalence
verifiers; aligned translations share semantic groups.

## <a id="sources">Data Sources</a>

- Pinned Hub revision: `0ffc9d6dc82717c25733b3172f4dbd63e48bab68`
- Generation: deterministic project generators, not copied benchmark text

## <a id="statistics">Structure & Statistics</a>

949,289 train, 25,685 validation, and 25,026 test rows; 92,260,850 Parquet
bytes in the three release shards.

## <a id="metadata">Available Metadata</a>

Stable IDs, semantic groups, language, family, difficulty prior, generation
seed, verifier/version, canonical answer, source/license, and hashes.

## <a id="languages">European Language Support</a>

English plus 23 other official EU languages. The release contains 10,000 rows
for each non-English language and 770,000 English rows.

## <a id="access">Access Information</a>

The full release, manifest, license, and hashes are mirrored at the frontmatter
LUMI path. The public source is linked above.

## <a id="use">Terms of Use</a>

Apache-2.0.

## <a id="post-training-use">Post-Training Use & Readiness</a>

Use model-specific rollout calibration rather than the stored difficulty label
to select the learnable frontier. Only `messages` is policy-visible;
`ground_truth`, generator parameters, and verifier metadata stay in the reward
service. Validation/test never enter learner updates.

## <a id="quality">Quality, Safety & Exclusions</a>

Deterministic regeneration and semantic-group splitting reduce leakage. Native
language sampling remains a promotion gate.

## <a id="curator">Catalogue Curator</a>

Birger.

## <a id="notes">Notes and Next Action</a>

Run eight-sample pass-rate profiles for the entering checkpoint, then build a
family- and language-balanced non-degenerate training pool.
