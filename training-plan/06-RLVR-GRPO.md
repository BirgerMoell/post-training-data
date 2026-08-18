# Stage 6 — RLVR / GRPO

## Current decision

This stage is **blocked for the common production pipeline**. There are useful
candidate datasets, but the OpenEuroLLM `post-training` repository does not yet
provide a GRPO/RLVR backend, rollout engine, or approved verifier suite.

## Available candidate data

| Capability | Sources |
| --- | --- |
| Multilingual exams | [European exam MCQ v1](../datasets/birgermoell-oellm-eu-exam-mcq-v1/README.md), [official exam bundle](../datasets/european-official-national-exam-bundle-23-ids/README.md), EXAMS-QA |
| Mathematics | AIME/MATH/GSM sources, [OpenR1-Math-220k staged on LUMI](../datasets/lumi-openr1-math-220k/README.md), [RLVR GSM/MATH/IF mixed constraints](../datasets/allenai-rlvr-gsm-math-if-mixed-constraints/README.md), Dolci RL/Zero candidates |
| Code | [Python R1-format RLVR](../datasets/allenai-rlvr-code-data-python-r1-format-filtered/README.md) |
| Instruction constraints | IFEval-style sources and [AutoIF-FI](../datasets/lumiopen-autoif-fi/README.md) |
| Tools | [EU tool-use v1](../datasets/birgermoell-oellm-eu-tooluse-v1/README.md) and execution-grounded subsets of tool datasets |
| Medical | [EU medical post-train v1](../datasets/birgermoell-oellm-eu-medical-posttrain-v1/README.md), for a separate specialist branch only |

Global-MMLU, MMMLU, Belebele, XCOPA, ArenaHard-EU, Jeopardy, and the European
evaluation holdouts are protected evaluations. They must not be silently
converted into RL prompts.

## Required verifier contract

Before any policy training, each RL item must provide:

- a stable item identifier and provenance;
- prompt and language;
- canonical answer or executable test;
- deterministic verifier version and timeout;
- reward range and partial-credit rule;
- parser failure behavior;
- contamination status;
- train/dev/test partition; and
- a manual audit result for ambiguous or multi-answer items.

Verifier families:

- exact/numeric equivalence for math and MCQ;
- unit tests in an isolated sandbox for code;
- schema plus execution checks for tool calls;
- deterministic constraint checkers for instruction following; and
- expert-reviewed rules for medical tasks. Do not use free-form judge rewards
  as "verifiable" without measuring judge error and bias by language.

## Proposed engineering sequence

1. Select the RL backend and rollout engine; document supported model sizes,
   clusters, checkpoint formats, and failure recovery.
2. Implement verifier unit tests and run them without a model.
3. Build a 1,000-item smoke mixture spanning math, code, exams, constraints,
   and tools; keep every evaluation benchmark out.
4. Run rollout-only inference and inspect reward distributions, parser failures,
   timeouts, reward hacking, and language imbalance.
5. Run a small-model 100-step GRPO pilot with checkpoint/resume.
6. Compare policy outputs against SFT/DPO start using identical sampling.
7. Scale to 7–9B only after KL, entropy, reward, and external evaluation remain
   stable.
8. Add capability groups one at a time. Keep a no-RL control at matched compute.

## Proposed first mixture

For the engineering pilot only:

- 35% math;
- 20% code;
- 20% multilingual exams;
- 15% instruction constraints; and
- 10% tool execution.

Balance by successful verifier executions, not submitted prompts. Cap any item
family with high timeout or parser-failure rates. This is a diagnostic mix, not
a flagship recipe.

## Exit gate

- Verifiers have unit tests and documented false-positive/false-negative audits.
- Rollout and training jobs resume without changing data order or rewards.
- Reward rises together with held-out external accuracy; no reward hacking is
  visible in manual samples.
- English and European language rewards are calibrated separately.
- General, safety, reasoning, tool, and long-context gates pass.
- The no-RL control demonstrates that gains are not merely extra supervised
  tokens or sampling variance.

## Missing

- Common OpenEuroLLM GRPO/RLVR implementation and cluster recipes.
- Approved rollout engine and inference/training checkpoint bridge.
- Versioned verifier package for math, code, exams, constraints, and tools.
- Multilingual RL prompts and verifier audits beyond the current exam coverage.
- Policy for chain-of-thought storage and release.
- Safety-focused verifiable tasks and reward-hacking monitoring.
