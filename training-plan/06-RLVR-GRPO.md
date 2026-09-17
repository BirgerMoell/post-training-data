# Stage 6 — RLVR / GRPO

## Decision

RLVR is **runnable now on LUMI**. It is not implemented in the common
`OpenEuroLLM/post-training` trainer, so the execution control plane is
[`BirgerMoell/oellm-rlvr`](https://github.com/BirgerMoell/oellm-rlvr):

- TMAX/Open-Instruct for online math RLVR using DAPO, CISPO, DPPO, or TVPO
  losses;
- a pinned verl OPD adapter for alternate online-policy experiments; and
- SkyRL plus Harbor for code and agentic environments.

This repository owns source governance, immutable release identities, mix
manifests, and the stage plan. LUMI owns the large bytes. `oellm-rlvr` owns
rollout, verifier, training, checkpoint/resume, and run-evidence code. A source
can therefore be available without being promoted: use the states **ready**,
**qualify**, and **catalogue**, not a blanket “blocked” label.

## Shared LUMI inventory

Root:

```text
/scratch/project_465002530/training/collection/post-training/2026q3
```

| State | Asset | Learner rows | Immutable identity | Shared directory | Intended use |
| --- | --- | ---: | --- | --- | --- |
| Ready for rollout profiling | `birgermoell/oellm-math-rlvr` | 949,289 train | `0ffc9d6dc82717c25733b3172f4dbd63e48bab68` | `birgermoell-oellm-math-rlvr/release/0ffc9d6c` | EU24 procedural math; integer/rational exact rewards |
| Ready for smoke | `open-r1/DAPO-Math-17k-Processed` | 12,700 train + 256 calibration + 1,024 evaluation | `31dd309567e3da778038cc87d868b6097a3ccf68` | `open-r1-dapo-math-17k-processed/release/31dd3095` | Hard English competition-math anchor |
| Ready for rollout profiling | OpenEuroLLM multilingual reasoning signal | 2,176 train + 72 profile + 144 evaluation | generated 2026-09-14; language registry `2f3bdf8…` | `oellm-multilingual-reasoning-signal/release/20260914` | Answer + target-language + format reward in 34 gated macro-languages |
| Qualify code sandbox | `birgermoell/oellm-code-rlvr` | 95,099 train | `e1cae7711049e3b5ff021fb3e9c752424882998c` | `birgermoell-oellm-code-rlvr/release/e1cae771` | Procedural Python with 10–13 hidden tests |
| Qualify tool parser | `birgermoell/oellm-eu-tooluse-v1` | 66,366 train | `b131d571a9f31a4ba4e518f2edce9bd1fcb0190b` | `birgermoell-oellm-eu-tooluse-v1/release/b131d571` | Exact tool name/arguments plus no-call abstention |
| Qualify subsets | AllenAI mixed constraints | 29,946 source rows | `7dbd180f5440c0b90f2944e6efea934b85437a95` | `allenai-rlvr-gsm-math-if-mixed-constraints/source/7dbd180f` | Prefer the IF slice; avoid duplicating DAPO/GSM math |
| Catalogue/qualify | `LumiOpen/AutoIF-FI` | 30,000 source train rows | `abeaec4f62f5f875810de0514176d9a5fc0506ea` | `lumiopen-autoif-fi/source/abeaec4f` | Finnish constraints after license and verifier-code vetting |
| Opt-in only | `birgermoell/oellm-eu-human-benchmarks-grpo` | 99,079 train | `f96729b537a7f57f871a067568b11a6a319c0d0d` | `birgermoell-oellm-eu-human-benchmarks-grpo/release/f96729b5` | Human multilingual exact rewards with explicit benchmark contamination |

The public-source mirrors retain their cards/licenses beside the pinned bytes.
Collection metadata in `collection/pilot/` records exact file hashes and the
remaining promotion checks. Do not infer approval from physical availability.

### Existing experiment evidence

The `oellm-rlvr` workspace also retains assets that already informed runtime
qualification:

- `/scratch/project_465002530/users/bmoell/oellm-rlvr/data/sources/oellm-math-rlvr-0ffc9d6c.parquet`
  — the full 949,289-row training split used to build prior pilots;
- `/scratch/project_465002530/users/bmoell/oellm-rlvr/data/eu-math-qwen35-20260914`
  — 2,944 EU-language rows plus 2,048 disjoint English replay rows;
- `/scratch/project_465002530/users/bmoell/oellm-rlvr/data/gsm8k-main-740312ad`
  — 7,473 prompt-only train rows, 64 calibration rows, and 1,255 primary
  evaluation rows; and
- the multilingual reasoning profile/challenge/signal artifacts and completed
  Qwen rollout/evaluation evidence under the same workspace.

These are evidence and reproducibility inputs, not additional mixture weight.
The shared releases above are the canonical paths for new runs.

## Deliberate exclusions

Do not use the existing `oellm-eu-exam-mcq-v1` GRPO files as a default source.
The live files contain 381,597 rows while their adjacent manifest reports a
different total, and the train split includes protected or ambiguous sources:
31,500 Belebele rows, 15,420 rows with unknown/missing license metadata, and
1,006 Swedish medical-exam rows with unresolved redistribution status. The
cleaner human-benchmark collection is available only as an opt-in replacement
with row-level licenses and an explicit contamination warning.

Also keep ArenaHard-EU, the project evaluation holdouts, current coding
benchmarks, DAPO calibration/evaluation, and every release validation/test
split out of learner updates.

## First checkpoint and executable smoke

Start from:

```text
Neonkraft/oellm-9b-256k-theta64m-prelude-anneal300b-instruct-sft
revision 85bf18fb4f0bee6ac6270f06b1d1c6b3be200f31
```

The executable config is
`oellm-rlvr/configs/lumi-grpo-dapo-oellm9b-instruct-sft-smoke.yaml`. It uses two
LUMI nodes, eight GCDs per node, 8 unique prompts × 8 samples, 1,024 response
tokens, learning rate `5e-7`, 128 episodes, ZeRO-3, and the DAPO loss. Its
dataset path points to the shared DAPO release.

An earlier attempt (LUMI job `22099315`) completed two-node ROCm/Ray preflight
and reached trainer argument parsing, then stopped before rollouts because the
config supplied the obsolete loss name `grpo`; the pinned backend accepts
`dapo`, `cispo`, `dppo`, or `tvpo`. The checked-in config now uses `dapo`.
This was a configuration failure, not evidence about the checkpoint or data.

## Run sequence

### 0. Freeze and validate

1. Verify the starting checkpoint manifest and local model hash.
2. Re-hash the selected Parquet/JSONL file against collection metadata.
3. Run verifier unit tests without a model.
4. Confirm that only prompt/messages reach the policy process. Ground truth,
   hidden tests, reference solutions, and verifier secrets stay in the reward
   process.
5. Fix the mix manifest, backend commit, container, seed, chat template,
   tokenizer, and exact generation settings in the run manifest.

### 1. Rollout-only calibration

Generate eight completions per prompt on held-out profile/calibration rows.
Record per source, family, language, and length bucket:

- pass rate and reward standard deviation;
- zero-variance prompt fraction;
- parser/format failure rate;
- truncation rate and response-length distribution;
- verifier timeout, exception, and infrastructure-error rates; and
- duplicated completions and obvious reward-hacking patterns.

Prefer prompts whose pass rate is approximately 0.05–0.80 and whose sample
group has non-zero reward variance. Retain easier/harder rows for diagnostics;
do not repeatedly update on groups that provide no policy-gradient signal.

### 2. DAPO engineering smoke

Run `rlvr-dapo-smoke-v1` for 128 episodes. Require:

- at least one optimizer step and one successful learner-to-vLLM weight sync;
- finite loss/KL/entropy and gradients;
- checkpoint plus trainer-state save and resume;
- deterministic dataset order for the fixed seed;
- zero verifier infrastructure errors; and
- saved rollouts sufficient to reproduce every reward.

This is a pipeline test, not a model-quality result. Compare it with a
rollout-only/no-update control using identical prompts and generation seeds.

### 3. Multilingual mathematics pilot

Use `rlvr-multilingual-math-v1`. Its submitted-prompt proportions are roughly
41% procedural EU24 math, 35% hard English DAPO, and 24% 34-language symbolic
reasoning. Reweight actual optimizer groups by *successful, non-degenerate
verifier execution*, while keeping per-language and generator-family floors.

Start with 100 optimizer steps, checkpoint every 10–20 steps, and evaluate the
parent plus each checkpoint on untouched release holdouts and project
evaluation suites. Escalate only if reward gains agree with held-out exact
accuracy and language/format compliance.

### 4. Capability branches

Add one verifier family at a time:

1. **Code:** qualify the network-disabled sandbox, re-run reference programs,
   audit timeout/OOM classification, then profile the procedural code release.
2. **Instruction constraints:** extract and qualify AllenAI IF constraints.
   For AutoIF-FI, map audited constraint IDs to packaged verifier functions;
   never execute arbitrary row-provided `eval_funcs`.
3. **Tool use:** test the target model's parser on calls and abstentions. Reward
   no-call gold with exact abstention; for calls, separately score valid JSON,
   correct function name, and exact normalized arguments.
4. **Human benchmark prompts:** only in a named, opt-in branch whose report
   lists every contaminated upstream benchmark and preserves row-level terms.

Only after isolated branches pass should the draft
`rlvr-capability-qualification-v1` pool be used. Do not interpret its static
weights as final optimizer proportions; recalibrate them for the entering
checkpoint.

### 5. Agentic phase

Use the already-qualified SkyRL/Harbor LUMI path for multi-turn environments.
Require oracle tests, deterministic environment images, bounded tools/network,
trajectory schemas, replayable rewards, and a failure taxonomy before mixing
agentic updates with single-turn RLVR.

## Reward contracts

| Family | Required reward behavior |
| --- | --- |
| Math | Parse the final answer and apply versioned numeric/symbolic equivalence; formatting can be a small separate signal, never a substitute for correctness. |
| Multilingual reasoning | Correct answer **and** target-language compliance **and** the declared think/box format. Report each component separately. |
| Code | Run hidden tests in the sandbox. Wrong answer/syntax/test failure = zero task reward; infrastructure failures are logged separately and excluded from policy signal. |
| Constraints | Package audited deterministic checkers by verifier ID. Do not import or execute code stored in a dataset row. |
| Tools | Parse structured calls, normalize arguments, score exact schema/name/arguments, and include explicit no-call examples. |
| Human QA/MCQ | Exact letter, normalized exact-match set, or numeric equivalence as declared per row. Ambiguous multi-answer items are excluded. |

Free-form LLM judges are not “verifiable” rewards. If a judge is later added
for style, measure disagreement and bias by language and keep it out of the
core correctness reward.

## Evaluation and promotion gates

Every branch has a matched no-RL control and uses the same decode settings for
parent/candidate comparisons. Promotion requires:

- reward improvement accompanied by held-out exact-accuracy improvement;
- no regression beyond the signed tolerance on general instruction,
  multilingual, safety, and long-context retention gates;
- stable KL, entropy, sequence length, and response diversity;
- no increase in parser failures, answer leakage, language switching, reward
  hacking, or test memorization;
- restart/resume that preserves data order, optimizer state, and reward
  behavior; and
- a retained bundle containing config, source/release manifests, collection
  commit, backend/container commits, SLURM script, environment capture, logs,
  rollouts, verifier outputs, checkpoints, and evaluation deltas.

### State transitions

- **Ready:** immutable bytes, documented verifier, unit tests, and protected
  splits exist.
- **Qualify:** run the entering checkpoint's rollout profile and capability-
  specific infrastructure test.
- **Pilot:** complete the small online update plus resume and held-out gates.
- **Approved:** requires reviewed legal/data governance and signed evaluation
  evidence; physical LUMI availability alone is insufficient.

## Scale-up catalogue

After the above loop is stable, consider DeepScaleR-Preview, a one-prompt-per-
problem view of OpenR1-Math-220k, and OpenMathReasoning as larger mathematics
pools. Admit them only after immutable pinning, prompt-level deduplication,
evaluation decontamination, license review, and checkpoint-specific pass-rate
profiling. Prefer the project-generated code release over public code-RLVR
collections with unclear terms or unvetted executable tests.
