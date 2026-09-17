# Stage 5 — preference optimization

## Goal and inventory definition

Improve response selection, instruction adherence, style, and safety while
preserving multilingual, reasoning, tool, and long-context capabilities.

This inventory was verified from the `bmoell` LUMI account in
`project_465002530` on 2026-09-17. In this document, **live** means that the
concrete file was readable and its row count and schema could be inspected.
It does not mean that the dataset is approved for a flagship run.

The result is: **five logical DPO datasets are live and readable, one is in
the shared canonical collection, and zero have completed every production
approval gate in the new collection workflow.**

## Live LUMI inventory

| Dataset | Verified artifact | Rows | Shape | Recommended role |
| --- | --- | ---: | --- | --- |
| [Dolci Instruct DPO translated](../openeurollm-dolci-instruct-dpo-translated/0.0.0/README.md) | `/scratch/project_465002530/training/collection/post-training/2026q3/openeurollm-dolci-instruct-dpo-translated/release/candidate-a57841a6` | 1,378,293 | Canonical unrendered `id, language, prompt, chosen, rejected, source_revision`; 12 configurations | Primary multilingual backbone after the remaining quality gates |
| [HelpSteer3](../nvidia-helpsteer3/0.0.0/README.md) | `/scratch/project_465002530/users/bmoell/helpsteer3-dpo/artifacts/data` | 38,459 train + 2,017 validation | Gzip JSONL with `context`, two responses, and signed preference strength | High-quality English anchor, diagnostic set, and reward-model source |
| [Qwen 3.5 9B historical DPO](../qwen35-9b-dpo-parquet/0.0.0/README.md) | `/scratch/project_465002530/users/bmoell/posttrain-data/qwen35-9b-dpo-parquet/train.parquet` | 259,922 | Nested full-conversation `chosen` and `rejected`; no explicit prompt column | Reproduction/control only; normalize and sanitize before reuse |
| [Exam DPO artifact](../exam-dpo-parquet/0.0.0/README.md) | `/scratch/project_465002530/users/bmoell/posttrain-data/exam-dpo-parquet/train.parquet` | 1,089,256 | String `prompt, chosen, rejected`; 35 language codes upstream | Capped correctness/capability branch after source-family and license review |
| [Medical DPO artifact](../medical-dpo-parquet/0.0.0/README.md) | `/scratch/project_465002530/users/bmoell/posttrain-data/medical-dpo-parquet/train.parquet` | 3,380 | String `prompt, chosen, rejected`; Swedish/mixed | Separate medical research branch only |

The exam source also has fixed DPO validation and test JSONL files under
`/scratch/project_465002530/users/bmoell/qwen35-posttrain/data/exam_mcq/oellm-eu-exam-mcq-v1`.
They are splits of the same logical dataset, not additional training sources.

### Integrity evidence

| Artifact | SHA-256 |
| --- | --- |
| HelpSteer3 train | `32b52e1d378f8dab1e4c9ae549da49a5d6fc0875aeafe3f9139e6053beb906bb` |
| HelpSteer3 validation | `cd0d8b6efd7869a44c1b5ff91701232062555829b3c838abfd770d7dab6c7861` |
| Historical Qwen 3.5 9B DPO Parquet | `dcfe21130872058f82ea285803815ee1c4b06708c606639fb5790f496ad2e7b6` |
| Exam DPO Parquet | `70ef651a0baa4b04a42514ec7ed3c9647bcd367f1add58d6fce900fcfded42cc` |
| Medical DPO Parquet | `ad451963e35f4090df332cfdf6211a9494b23cc1e7b01691ca3cccbaa2b4ac88` |

The translated Dolci release has a per-file manifest in its collection counts
directory; its manifest digest is
`8743398a990908b75bd8db9ddc77427c2456c9c76a0d82eb788d65519a128970`.

## Recorded but not currently usable

- `qwen35-9b-multiling-dpo-parquet/train.parquet` is absent from its recorded
  `project_465002530` path. Its build also depends on source directories that
  are not currently readable. It is not a live dataset.
- The recorded `project_462000963` copies of original Dolci DPO,
  UltraFeedback, HelpSteer3, and the wider `DPOTrainer_format` tree return
  `Permission denied` for the current account. They may still exist, but must
  be copied or access-granted before they can be scheduled from this project.
- SmolTalk2 and other public Hugging Face candidates remain catalogue sources,
  not verified LUMI-local DPO releases in this inventory.

Do not silently fall back to Hugging Face during an offline LUMI job. A run
must resolve every input to a readable immutable LUMI artifact before
submission.

## Dataset roles and exclusions

### 1. Multilingual backbone: translated Dolci

Use the shared canonical release as the main integration source after PII,
safety, language-quality, task-quality, preference-consistency, and
contamination checks are complete. Sample across language configurations with
square-root or temperature balancing, cap any one language at 25% of the
Dolci allocation, and never oversample a small configuration by more than 2x.

Translations of one source example share semantic ancestry. Split and dedupe
on stable source/semantic identity rather than row identity so parallel
translations cannot leak across train and evaluation or be multiplied
unintentionally.

### 2. English quality anchor: HelpSteer3

Promote the pinned personal staging into the shared collection without
changing its train/validation split. The existing transform correctly maps a
negative score to response 1, a positive score to response 2, and retains the
absolute value as `preference_strength`.

The train split contains 2,160 ties and the validation split 97 ties. Exclude
those rows from DPO, leaving 36,299 train and 1,920 validation pairs. Keep the
ties in a separate reward-model or calibration release; do not invent an
ordering. Report results by strength 1/2/3 as well as in aggregate.

### 3. Historical English control: Qwen 3.5 9B DPO

Use this only to reproduce the completed English run or as a matched-compute
control. It descends from Dolci DPO and therefore must not be mixed with the
translated Dolci English configuration without source-aware deduplication.
Before reuse, strip unneeded conversation metadata, recover an explicit shared
prompt, produce canonical unrendered pairs, and attach component provenance
and license evidence.

### 4. Capability slice: exam DPO

Keep the upstream validation and test splits protected. Rebuild the training
release with source-family grouping, license allowlisting, benchmark
contamination checks, and semantic deduplication across languages. Its size
must not allow synthetic exam formatting to dominate general alignment. Use
it first as a 5% capped ablation, or as a separate specialist checkpoint, and
promote it only if exam gains do not reduce open-ended instruction quality.

### 5. Specialist slice: medical DPO

Keep medical data out of the general flagship mix until license, privacy,
clinical-safety, and provenance reviews are complete. Run it as a separate
specialist branch with medical evaluation and explicit regression checks on
ordinary prompts. Its small size makes it unsuitable as evidence for broad
preference improvement.

## Run ladder

All stages start from the same SFT checkpoint, tokenizer, and chat template.
Match optimizer tokens, seed, maximum length, and evaluation generation
settings when comparing sources.

### A. Pipeline smoke test

Use
[`mixes/pilots/dpo-dolci-eu-qwen3-smoke-v1.yaml`](../mixes/pilots/dpo-dolci-eu-qwen3-smoke-v1.yaml).
It samples 0.1% each from English, German, Finnish, and Swedish. Its only
purpose is to validate loading, templating, truncation, reference log-probs,
checkpointing, and restart behavior; it is not a quality experiment.

### B. Matched single-source ablations

Run three equal-token experiments:

1. translated Dolci only, language-balanced;
2. HelpSteer3 only, excluding ties; and
3. the normalized historical English artifact as a control.

Start with sigmoid DPO, beta `0.1`, LR `5e-7`, BF16, an 8,192-token ceiling,
and truncation-by-dropping the whole pair. Compare beta `0.05`, `0.1`, and
`0.2` only after the baseline is healthy. Record retained pairs and rendered
tokens after every filter; raw row counts are not comparable training budgets.

### C. General multilingual candidate

After the ablations and data gates, use this initial **rendered-token** target:

| Component | Starting share | Constraint |
| --- | ---: | --- |
| Translated Dolci | 80% | Language-balanced; one-language cap 25%; oversampling cap 2x |
| HelpSteer3 | 15% | Fixed train split; no ties; report score-strength slices |
| Exam DPO | 5% | License-approved source families only; no held-out splits |
| Historical Qwen DPO | 0% | Control only; overlaps Dolci ancestry |
| Medical DPO | 0% | Separate specialist branch |

Treat these as starting points, not approved flagship weights. Freeze the
realized row/token composition in `data-mix.lock.yaml` and promote the mix
only after matched-compute evaluation. If an explicit multilingual safety
source has not passed its own gates, the candidate is incomplete rather than
implicitly safe.

### D. Specialist branches

Run exam and medical specialization separately from the general candidate.
Prefer a short second DPO stage or adapter experiment. Merge a specialist
branch into a general release only if both specialist gains and general,
multilingual, safety, and calibration gates pass.

## Promotion and storage plan

No production run should train directly from `/users/bmoell`. For every
retained source:

1. pin the public revision or the exact source checksums;
2. create `collection/<cycle>/<slug>/metadata.yaml` in this repository;
3. materialize canonical unrendered Parquet under
   `/scratch/project_465002530/training/collection/post-training/<cycle>/<slug>`;
4. store source, sparse quality and contamination overlays, release shards,
   counts, and manifests as separate immutable layers;
5. complete license, PII, safety, integrity, language-quality, task-quality,
   and contamination gates;
6. reference only a named collection release from a committed mix manifest;
7. write the resolved paths, revisions, checksums, filters, sample counts, and
   rendered-token composition into the run lock file.

Migration order:

1. HelpSteer3, because it is small, pinned, already configured, and provides a
   strong English diagnostic.
2. Exam DPO, after source-family/license and protected-split reconstruction.
3. Historical Qwen DPO only if the reproduction control is still needed.
4. Medical DPO after its separate governance review.
5. Project-462 sources only after access is restored and their provenance is
   reconciled; do not copy them blindly into the production collection.

## Data acceptance checks

For every pair:

- chosen and rejected responses share the same unrendered prompt;
- the chosen response remains preferable after translation;
- neither response contains leaked judge text, reward, benchmark answer, or
  generator metadata;
- preference is not explained only by length, truncation, or formatting;
- language ID matches the intended configuration;
- identical or empty responses are rejected with a recorded reason;
- semantic/source IDs cannot cross train, validation, or protected evaluation;
- overlap across SFT and preference data is measured and intentional; and
- component license, privacy, and safety decisions are recorded, not merely
  inherited from an aggregate dataset card.

## Model and run exit gates

- Held-out preference accuracy and reward margin improve by source, language,
  domain, and HelpSteer preference strength.
- Chosen and rejected rewards move in the intended direction without a large
  KL or response-length shortcut relative to the SFT parent.
- ArenaHard-EU or equivalent battle evaluation improves without English or
  low-resource-language collapse.
- Reasoning accuracy, exam holdouts, tool-call validity, and factuality do not
  regress outside their predeclared tolerance.
- Safety behavior improves on a protected policy-aligned set.
- 4k/32k/64k/128k retention gates pass for the target checkpoint family.
- The final loss, beta, source shares, and stopping checkpoint are justified by
  matched-compute runs rather than training loss alone.

## Immediate actions

- Materialize and register a shared canonical HelpSteer3 release, keeping ties
  as reward-model-only data.
- Complete the remaining translated Dolci overlays and run the four-language
  smoke manifest.
- Reconstruct exam source-family manifests and lock protected splits before an
  exam ablation.
- Mark the missing Qwen multilingual artifact as non-runnable until rebuilt.
- Request access to, or an approved transfer from, `project_462000963` before
  considering original Dolci, UltraFeedback, or the older shared HelpSteer3
  copy.
