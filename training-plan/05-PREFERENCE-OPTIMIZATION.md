# Stage 5 — preference optimization

## Goal

Improve response selection, instruction adherence, style, and safety while
preserving multilingual, reasoning, tool, and long-context capabilities.

## Available data

| Source | State | Role |
| --- | --- | --- |
| [Dolci Instruct DPO translated](../datasets/openeurollm-dolci-instruct-dpo-translated/README.md) | Public; 11 European languages plus English config | Primary multilingual preference candidate |
| [SmolTalk2 decontaminated](../datasets/openeurollm-smoltalk2-decontaminated/README.md) | Public | Primary decontaminated general preference source |
| [Dolci Instruct DPO](../datasets/allenai-dolci-instruct-dpo/README.md) | Used in completed run; on LUMI | English control/reproduction |
| [HelpSteer3](../datasets/nvidia-helpsteer3/README.md) | Candidate; on LUMI | Attribute-based quality and preference ablation |
| [UltraFeedback](../datasets/ultrafeedback/README.md) | Candidate; on LUMI | Broad English preference data after license/decontamination review |
| [Exam DPO artifact](../datasets/exam-dpo-parquet/README.md) | Configured/runnable | Verifiable multilingual domain preference branch |
| [Medical DPO artifact](../datasets/medical-dpo-parquet/README.md) | Staged on LUMI | Swedish medical branch, not general flagship data |
| [Qwen multilingual DPO artifact](../datasets/qwen35-9b-multiling-dpo-parquet/README.md) | Configured/runnable | Pipeline control; verify model-template portability |
| [OpenR1-Math-220k on LUMI](../datasets/lumi-openr1-math-220k/README.md) | Staged; multiple scored traces upstream | Math-only pair construction after revision, verifier, and margin checks |

## Data acceptance checks

For every row:

- chosen and rejected responses must share the same rendered prompt prefix;
- chosen must still be preferable after translation;
- neither response may contain leaked judge text, reward, benchmark answer, or
  generator metadata;
- length and formatting differences must not be the sole preference signal;
- safety pairs must have an explicit policy rationale or category;
- language ID must match the intended configuration; and
- duplicates across SFT and preference data must be measured and intentional.

## Proposed pilot mixture

Measure by rendered tokens across both responses:

| Component | Starting share |
| --- | ---: |
| Translated Dolci DPO | 40% |
| Decontaminated SmolTalk2 | 30% |
| Approved English quality/preference data | 15% |
| Exam, tool, medical, or other targeted pairs | 10% |
| Explicit safety/refusal pairs | 5% |

The safety share cannot be filled today by a production multilingual source;
for the flagship this is a blocker, not permission to omit safety. Targeted
domain pairs should be excluded from the general checkpoint if they cause
specialist behavior on ordinary prompts.

Within the translated component, balance languages explicitly. Compare native
or English preference judgments with back-translated and bilingual human
audits before scaling.

## Proposed DPO procedure

1. Start from the selected Stage 4 integration checkpoint and keep its tokenizer
   and chat template unchanged.
2. Freeze a dev set stratified by language, source, capability, and preference
   margin.
3. Use the common TRL DPO path for the first integration build. Its checked-in
   starting configuration uses LR `5e-7`, BF16, effective batch 4, 10% warmup,
   and a 2,048-token ceiling.
4. Run a small sweep over beta/loss settings because project examples differ
   substantially: compare beta `0.1`, `1.0`, and `5.0`, plus one alternative
   loss such as IPO or hinge. Match optimizer tokens and generation settings.
5. Compare 2k and 4k maximum lengths. Longer preference context should be a
   separate experiment because memory and reference-model cost grow quickly.
6. Evaluate intermediate checkpoints; stop if reward accuracy rises while
   external quality, multilingual, or long-context gates regress.
7. Keep the explicit SFT reference checkpoint and record whether the DPO
   reference model was explicit or implicit.

SimPO artifacts exist in the wider project, but the common OpenEuroLLM
post-training repository currently implements SFT and DPO. Treat SimPO as a
separate backend experiment until its loss, config, and checkpoint handoff are
integrated and reviewed.

## Exit gate

- Held-out preference accuracy improves by source and language.
- ArenaHard-EU/battle evaluation improves without English or low-resource
  language collapse.
- Reasoning answer accuracy and tool-call validity do not regress.
- Safety behavior improves on a protected policy-aligned set.
- 4k/32k/64k/128k retention gates pass.
- The selected loss/beta is justified by a matched-compute sweep.

## Missing

- Human validation that translated preferences preserve ranking.
- Broad preference data for Dutch, Portuguese, and the 11 EU languages that
  only have targeted repair coverage.
- A production multilingual safety preference set.
- Long-context preference pairs and a retention-safe DPO recipe.
- Common support and reproduction tests for SimPO or other reference-free
  methods.
