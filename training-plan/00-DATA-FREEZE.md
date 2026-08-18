# Stage 0 — data freeze, holdout protection, and readiness

## Goal

Produce a reviewable set of immutable inputs for one integration build. This
stage ends before any GPU training starts.

## Available inputs

- Public decontaminated releases: Dolci Instruct/Think,
  Nemotron-Post-Training-v2, SmolTalk2, Open-PerfectBlend,
  Orca-AgentInstruct, and LMSYS Chat.
- [OpenEuroLLM contaminated-document support set](../datasets/openeurollm-contaminated-documents/README.md).
- [OpenEuroLLM post-training decontamination](https://github.com/OpenEuroLLM/post-training-decontamination),
  which provides n-gram search through Elasticsearch.
- Evaluation-only assets including
  [European holdouts](../datasets/birgermoell-oellm-eu-eval-holdouts-v1/README.md),
  [ArenaHard-EU](../datasets/openeurollm-arenahard-eu-v0-v0-bis/README.md),
  [Jeopardy](../datasets/openeurollm-jeopardy/README.md), Global-MMLU,
  MMMLU, Belebele, XCOPA, and EXAMS-QA.
- LUMI shared post-training candidates under
  `/scratch/project_462000963/datasets/posttraining_data`.
- Individually inspected LUMI candidates for
  [English–Finnish long SFT](../datasets/lumi-long-context-eng-fin-sft/README.md),
  [Poro2 Finnish instruction data](../datasets/lumi-poro2-instruction-data/README.md),
  [OpenR1 Math](../datasets/lumi-openr1-math-220k/README.md),
  [AM reasoning traces](../datasets/lumi-am-deepseek-r1-think/README.md), and
  [Glaive code](../datasets/lumi-glaive-code-assistant-v3/README.md). Their
  existence is confirmed, but each unresolved lineage/license field remains a
  freeze blocker.

## Required freeze record

For every selected dataset or derived shard, record:

| Item | Required value |
| --- | --- |
| Identity | Catalogue slug and human-readable name |
| Origin | Public URL or cluster source path |
| Version | Git/Hugging Face commit, release, or retrieval date |
| Selection | Configuration, split, source subset, filters, and sampling weight |
| Format | Raw columns and final training role: CLM, SFT, preference, RLVR, or evaluation |
| Counts | Rows/documents, total tokens, trainable tokens, and length percentiles |
| Language | Detected and declared language counts after filtering |
| Integrity | File sizes and SHA-256 checksums |
| Legal | License/source terms and named approval owner |
| Privacy/safety | PII scan, unsafe-content handling, and exclusions |
| Contamination | Protected benchmark revisions, search settings, and removed rows |
| Derivation | Build script commit, tokenizer, chat template, seed, and output path |

This can be Markdown plus generated JSON; the important requirement is that a
reviewer can reconstruct the exact bytes used by training.

## Procedure

1. **Declare protected evaluations.** Pin benchmark revisions first. Add all
   prompts, reference answers, and hidden-test proxies to the decontamination
   index. Keep benchmark data outside trainable storage roots.
2. **Resolve licenses and access.** Assign an owner to every mixed or unclear
   source. A public download is not by itself approval for model training or
   redistribution.
3. **Normalize without losing provenance.** Retain `source_dataset`,
   `source_revision`, language, original row identifier, and transformation
   version in the derived manifest.
4. **Deduplicate across stages.** Remove exact and near-duplicate prompts across
   SFT, preference, RLVR, and evaluation. Keep intentional replay documented.
5. **Inspect formatted examples.** For every source, render at least 100 random
   examples with the target tokenizer/template and inspect truncation, role
   boundaries, tool-call encoding, and trainable-token masks.
6. **Measure the final mix.** Report weights by source, language, capability,
   sequence-length bucket, and trainable tokens—not only examples.
7. **Materialize immutable artifacts.** Place the freeze under a shared project
   root; make training consume only that root or a pinned public revision.

## Exit gate

Do not start Stage 1 or Stage 2 until:

- all selected sources have immutable revisions or checksummed cluster files;
- evaluation contamination reports exist;
- train/dev splits are fixed and non-overlapping;
- licenses and access have named owners;
- data statistics and random human samples have been reviewed;
- the base model, tokenizer, chat template, code commit, and container digest
  are pinned; and
- the next stage can run offline from the frozen artifacts.

## Missing today

The catalogue has locations, but no single production freeze manifest combines
the exact versions, hashes, accepted licenses, post-filter counts, and
cross-stage duplicate map. This is a P0 release blocker.
