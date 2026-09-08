# Discussion 3 — DPO and a narrow GRPO bridge

## Scope and proposed decision

This thread covers offline preference optimization and the first short-horizon,
verifier-backed GRPO experiments. Broader environment and agentic RL belongs in
[Discussion 4](04-reinforcement-learning.md).

Use translated Dolci DPO plus decontaminated SmolTalk2 as the first multilingual
preference control. Treat GRPO as a gated bridge for exact-format, math, exam,
and tool-call tasks—not as a replacement for a working preference dataset.

## DPO sources

| Source | Decision | Role / gate |
| --- | --- | --- |
| `openeurollm/Dolci-Instruct-DPO-translated` | Use after freeze | Primary 11-language preference source; audit whether translation preserves the chosen/rejected ordering |
| `openeurollm/smoltalk2-decontaminated` | Use as English control | General helpfulness/style; measure length bias, verbosity, sycophancy, and source composition |
| `allenai/Dolci-Instruct-DPO` | Reproduction control | Existing completed-run evidence; deduplicate against translated and derived variants |
| multilingual exam DPO / SimPO artifacts | Pilot branch | Strong exact-answer signal but narrow MCQ behavior; isolate from general chat and from protected exam evaluation |
| HelpSteer3 and UltraFeedback | Pilot | Attribute/preference diversity after revision, licensing, decontamination, and length-bias review |
| Dolci Think DPO 7B/32B | Pilot | Reasoning preference ablation; require final-answer checks and a matched no-trace control |
| French Compar:IA [`Millesime-2026-comparIA-DPO`](https://huggingface.co/datasets/borekboissy/Millesime-2026-comparIA-DPO) | Pilot candidate | Native human arena signal for French; verify consent, license, filtering, model-pair bias, and overlap before nomination |
| [`NASK-PIB/RefusEU`](https://huggingface.co/datasets/NASK-PIB/RefusEU) | Hold | Promising safety preferences across 12 European languages, but its current card does not specify a release license; do not train until terms and eval separation are resolved |

## Pair-generation product

Build `oellm-eu-preference-v1` from prompts that are independent of protected
evaluation. For each prompt:

1. sample multiple candidates from diverse checkpoints and decoding settings;
2. remove exact/near duplicates and responses with leaked judge metadata;
3. apply deterministic validators for language, schema, citations, math, code,
   constraints, and tool calls;
4. obtain two independent bilingual rankings plus a calibrated human audit;
5. retain ties and disagreement as data-quality evidence rather than forcing a
   pair; and
6. record preference margin, response lengths, judge identities, policy slice,
   and whether the prompt/response was native, translated, or synthetic.

Preference pairs should include helpful direct answers, correction, concise
format following, uncertainty, safe refusal/redirection, and benign neighbors
that prevent over-refusal. Translate prompts and responses together only when
both candidates remain plausible and their ranking survives bilingual review.

## First DPO experiment

Starting token shares for a matched-compute pilot:

- 40% translated Dolci DPO;
- 30% decontaminated SmolTalk2;
- 15% approved English quality/preference data;
- 10% targeted exam/tool/reasoning pairs; and
- 5% policy-approved safety/refusal pairs.

The final 5% is a blocker if no approved safety source exists; it is not
permission to silently omit safety. Sweep beta/loss settings and compare DPO
with one reference-free method only after its implementation is reproducible.

## Narrow GRPO pilot

Begin with a 1,000-item rollout mixture whose rewards are deterministic and
unit-tested:

- exact/numeric equivalence for math and clean exam items;
- JSON/schema/constraint checks for EUROPA-like skills using newly generated
  prompts, never EUROPA rows;
- execution for sandboxed code and tool calls; and
- explicit parser-failure and timeout penalties.

Balance by **successful verifier executions**, not submitted prompts. Run
rollout-only diagnostics before updating weights, report reward distributions
by language, and compare with a token-matched extra-SFT control. Free-form
judge reward does not qualify as verifiable until error and language bias are
measured.

## Acceptance gates

- Preference accuracy improves on a frozen dev set by source, language,
  capability, and margin, without a length-only shortcut.
- Human or bilingual audit confirms translated pair order at a signed rate.
- EUROPA strict format, structured extraction, grounded QA, summarization,
  safety, and minimum-language results do not regress; public prompts remain
  evaluation-only.
- GRPO reward correlates with untouched external task accuracy and manual
  review shows no reward hacking.
- Reasoning correctness, tool validity, safety, and 128K retention pass after
  both DPO and GRPO.
- A matched no-preference/no-GRPO control makes the causal gain credible.

## Questions for the thread

1. Is translated Dolci DPO the primary multilingual control, or should the
   first run be limited to languages with completed bilingual audits?
2. Which preference loss and maximum sequence length are supported in the
   common pipeline?
3. Which exact task families are safe to reuse for GRPO without compromising
   the project evaluation suite?
4. Who owns preference-judge calibration per language?
