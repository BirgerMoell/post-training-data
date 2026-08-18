# Stage 8 — integration, evaluation, and release

## Goal

Select one checkpoint lineage, demonstrate that every claimed capability
survives the full sequence, and publish enough information to reproduce the
run. OpenEuroLLM's T4.6 plan calls for common integration builds on a roughly
4–6 week cadence, initially covering context extension, instruction following,
and chat, then reasoning and tool calling
([Mattermost decision, 2026-02-24](https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/ec7c7aat1784pnsmqca6f1n5dw)).

## Checkpoint selection

Keep a checkpoint at every stage boundary:

1. approved Prelude base;
2. context-extended base;
3. general instruction/chat SFT;
4. multilingual/repair SFT;
5. reasoning branch, tool branch, and selected integration SFT;
6. preference checkpoint;
7. RLVR checkpoint, if Stage 6 is approved;
8. safety-integrated general checkpoint; and
9. any domain-specific branches.

Do not overwrite stage boundaries. If a late stage regresses, the project must
be able to restart from the last accepted checkpoint.

## Common evaluation matrix

| Gate | Data/tools already visible | Required report |
| --- | --- | --- |
| Base knowledge | Global-MMLU, MMMLU, Jeopardy, Prelude score artifact | Overall and per-language deltas from base |
| Reading and causality | Belebele, XCOPA | Per-language accuracy and confidence intervals |
| Translation retention | [LUMI FLORES-200/FLORES+](../datasets/lumi-flores-200/README.md) and [Tatoeba en–fi](../datasets/lumi-tatoeba-eng-fin/README.md) | Per-language/direction scores; exact protected IDs and upstream lineage |
| European exams | EXAMS-QA, official exam bundle, EU holdouts | Strict train/eval separation and per-source scores |
| Instruction/chat | IFEval-style tasks, ArenaHard-EU, battle annotations | Constraint categories, pairwise win rates, judge sensitivity |
| Reasoning | Held-out math/code/reasoning sets | Final answer, verifier accuracy, and trace policy |
| Tools | Unseen schemas and execution sandboxes | Tool choice, argument validity, execution success |
| Long context | RULER/needle/retrieval plus future multilingual set | 4k/16k/32k/64k/128k curves, not one aggregate |
| Safety | Protected policy-aligned multilingual suite | Refusal precision/recall, benign-neighbor, jailbreak, locale |
| Privacy/contamination | Decontamination and PII tooling | Removed overlap, residual samples, known limitations |

Run the matrix after every stage boundary on a small core suite and on the full
suite before promotion. Use the same decoding, prompts, model revision, and
harness revision for comparisons.

## Final integration options

Prefer sequential checkpoints plus a short final integration SFT over weight
merging unless weight merging is separately validated. A proposed integration
phase can use:

- 40% general instruction/chat;
- 25% multilingual/repair;
- 15% reasoning;
- 10% tool/agentic;
- 5% safety; and
- 5% long-context retention material.

These are starting shares for a small pilot. The long-context share cannot be
filled safely until the Stage 1 retention blocker is resolved; the safety share
cannot support a flagship claim until Stage 7 data exists. Do not run this mix
as a production default merely because it sums to 100%.

## Promotion gate

A checkpoint is promotable only when:

- every required stage gate passes with signed thresholds;
- results include per-language and per-capability deltas, not just averages;
- known regressions and skipped stages are stated in the model card;
- data, code, container, tokenizer, and evaluation revisions are pinned;
- cluster artifacts have shared retained copies and checksums;
- checkpoint conversion parity passes;
- licenses, privacy, and safety reviews have named approvals; and
- a clean-room reproduction command exists for the selected cluster/framework.

## Release bundle

Publish or retain together:

- HF and training-framework checkpoints;
- tokenizer, chat template, generation configuration, and RoPE settings;
- stage-by-stage data manifest with weights and token counts;
- source licenses and exclusions;
- training YAML/scripts, code commits, container digests, Slurm jobs, and logs;
- W&B/TensorBoard links or exported summaries;
- checkpoint conversion and parity report;
- complete evaluation results and harness revision;
- decontamination, PII, and safety reports; and
- model card with intended use, limitations, languages, and skipped blockers.

## Cadence

Each 4–6 week integration build should close one or more red gaps while keeping
the same core evaluation matrix. A build may be useful without being a release
candidate; label it clearly and preserve the evidence so later builds can
compare against it.
