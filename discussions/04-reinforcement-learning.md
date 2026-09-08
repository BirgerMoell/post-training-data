# Discussion 4 — broader reinforcement-learning data and environments

## Proposed decision

Keep broader RL blocked from the flagship until the project has a reproducible
rollout backend, versioned verifier package, checkpoint/resume test, and a
protected evaluation boundary. Static prompts are not enough: the training
artifact is the task bank **plus** environment image, tool schemas, tests,
timeouts, reward code, and retained rollout metadata.

## Candidate task banks

| Family | Starting sources | Decision |
| --- | --- | --- |
| Math | OpenR1 Math, RLVR GSM/MATH/IF constraints, Dolci RL/Zero candidates, selected Nemotron-Math-v2 problems | Pilot after answer/verifier replay and benchmark-family audit |
| Code | `allenai/rlvr-code-data-python-r1-format-filtered`, execution-filtered code tasks | Pilot only in a locked-down sandbox with licensing, secret, dependency, flaky-test, and timeout checks |
| Multilingual exams | `birgermoell/oellm-eu-exam-mcq-v1` and approved national exam sources | Use for an engineering pilot only after exact separation from evaluation; coverage is broad but task form is narrow |
| Instruction constraints | `LumiOpen/AutoIF-FI` and newly generated finite-state constraints | Pilot; extend beyond Finnish with deterministic validators |
| Tools | EU tool-use v1 and execution-grounded ToolACE/Hermes/Glaive subsets | Pilot after schemas, observations, permissions, and outcomes replay correctly |
| Agentic software tasks | [`open-thoughts/OpenThoughts-Agent-RL-5K`](https://huggingface.co/datasets/open-thoughts/OpenThoughts-Agent-RL-5K), [AgentTrove](https://huggingface.co/datasets/open-thoughts/AgentTrove), and [TaskTrove](https://huggingface.co/datasets/open-thoughts/TaskTrove) | Hold until environment bytes and verifiers are replayed; recent project notes about vacuous verifiers make reward-audit evidence mandatory |
| Medical and other high-stakes domains | EU medical post-train v1 | Separate specialist branch only, with expert-approved rewards; never general-purpose RL by default |

`OpenThoughts-Agent-RL-5K` is a useful external reference because it publishes
5,000 Apache-2.0 software tasks used for RL, while AgentTrove offers a much
larger trace pool. Neither should be ingested as a row dump: environment
reproduction and verifier validity determine whether the task is usable.

## Synthetic environment product

Create a multilingual `oellm-eu-rl-tasks-v1` with four independently versioned
families:

- **Constraints:** locally authored target-language prompts with exact
  requirements for JSON, ordering, counts, forbidden tokens, dates, and
  revision tracking.
- **Tools:** locale-aware but non-sensitive APIs (transport fixtures, unit
  conversion, public-document search, calendar arithmetic, catalogue lookup)
  with valid/invalid schemas, no-call cases, recovery, and least-privilege
  actions.
- **Grounded workflows:** synthetic document stores built from training-cleared
  sources, with answerability, citation, contradiction, and abstention rewards.
- **Code/data tasks:** hermetic repositories and fixtures with tests that fail
  before and pass after the intended change, plus adversarial tests against
  deletion, secret access, and test tampering.

Author task semantics independently in target languages where possible. A
translated environment needs localized values, formats, tool descriptions,
and expected behavior—not only a translated prompt. Keep every EUROPA item and
source-specific paraphrase outside generation prompts.

## Engineering sequence

1. Select the rollout/training backend and freeze its versions.
2. Unit-test verifiers without a model, including known wrong solutions.
3. Run rollout-only inference; inspect success, parser failure, timeout, reward
   saturation, and language imbalance.
4. Run a 100-step small-model GRPO/RL smoke test with save/resume.
5. Compare against SFT/DPO start and a token-matched no-RL control.
6. Scale to 7–9B only after KL, entropy, reward, and external evaluation are
   stable.
7. Add one capability family at a time; do not start with long-horizon agents.

For the first engineering pilot, start with 35% math, 20% code, 20%
multilingual exams, 15% instruction constraints, and 10% tool execution,
measured by successful verifier executions. This is a diagnostic mix, not a
flagship recipe.

## Verifier contract

Each task needs a stable ID and provenance; language/script; canonical answer
or executable test; immutable verifier and environment revision; reward range
and partial-credit rule; parser-failure and timeout behavior; contamination
status; train/dev/test partition; and an audit of ambiguous, multi-answer,
flaky, shortcut, or vacuous cases. The harness must detect reward by test
deletion, environment modification, answer leakage, and superficial formatting.

## Acceptance gates

- Verifier false-positive and false-negative rates pass signed thresholds for
  every family and language tier.
- Reward improvement tracks untouched external accuracy and manual quality;
  no family succeeds primarily through a shortcut.
- Runs resume without changing task order, environment, or rewards.
- EUROPA arithmetic, strict format, grounded QA, tool recovery, revision
  tracking, refusal, and minimum-language diagnostics do not regress; its
  public data remains excluded.
- General chat, reasoning, safety, tool permission, and long-context gates pass.
- The no-RL control demonstrates more than extra sampling or supervised tokens.

## Questions for the thread

1. Which rollout backend and environment format should become the common
   implementation?
2. Who owns the verifier package and its red-team tests?
3. Which exam/task families are provably disjoint from promotion evaluation?
4. What is the first non-English, non-MCQ RL task family we can ship?
