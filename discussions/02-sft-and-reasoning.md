# Discussion 2 — SFT and reasoning data

## Proposed decision

Use decontaminated OpenEuroLLM instruction data as the general backbone, add
European-language data according to measured deficits, and integrate reasoning
only after a clean general SFT checkpoint exists. Do not let long English
reasoning traces dominate ordinary chat or assume that translated traces prove
native-language reasoning.

## Use in the first freeze

General SFT:

- `openeurollm/Dolci-Instruct-SFT-decontaminated` for the clean English
  backbone;
- `openeurollm/Dolci-Instruct-SFT-translated` and
  `openeurollm/EU-Instruct-Synthetic` for the current European-language base;
- the completed EuroBlocks + Tülu-3 85/15 experiment as a reproduction control,
  not a permanent ratio; and
- `birgermoell/oellm-eu-defect-repair-sft-v1` as a targeted repair shard, with
  its narrow task distribution kept separate from broad instruction claims.

Reasoning SFT:

- the decontaminated Dolci Think 7B/32B variants and decontaminated Nemotron v2
  as English controls;
- frozen OpenR1 Math and verified code slices for independently checkable
  answers; and
- the Finnish distilled-math corpus only after its exact upstream IDs,
  license, and solver checks are recovered.

The newly published
[`openeurollm/Dolci-Think-SFT-translated`](https://huggingface.co/datasets/openeurollm/Dolci-Think-SFT-translated)
is the most relevant addition beyond the spreadsheet snapshot: roughly 498K
successfully translated rows across Finnish, German, French, Italian, Dutch,
Polish, Romanian, Swedish, and Ukrainian. It should enter as a **pilot**, with
per-language correctness, trace-language, contamination, and native-review
gates—not be promoted solely because it is project-native.

## External pilot candidates

| Source | Decision | Contribution and risk |
| --- | --- | --- |
| [`lightonai/Dolci-Think-SFT-32B-Multilingual`](https://huggingface.co/datasets/lightonai/Dolci-Think-SFT-32B-Multilingual) | Pilot ablation | Large French/German/Spanish reasoning translations plus English; useful independent recipe, but overlaps the Dolci parent and requires ODC-BY and transformation review |
| [`open-thoughts/OpenThoughts3-1.2M`](https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M) | Pilot by source slice | Strong math/code/science baseline; sample final-answer correctness and avoid double counting because Dolci Think already contains an OpenThoughts3 derivative |
| [`nvidia/Nemotron-Math-v2`](https://huggingface.co/datasets/nvidia/Nemotron-Math-v2) | Pilot, English verifier seed | About 347K problems and 7M trajectories under CC BY 4.0; subsample by problem, difficulty, diversity, and verified answer rather than ingesting all trajectories |
| [`OpenLLM-France/Luciole-PostTraining-Dataset-1.1`](https://huggingface.co/datasets/OpenLLM-France/Luciole-PostTraining-Dataset-1.1) | Pilot for open-data recipe comparison | CC BY-SA 4.0 SFT/preference collection with a European provenance story, but currently primarily English and must be deduplicated against shared parents |
| OASST2 | Replay pilot | Adds human-authored multilingual dialogue; privacy, language labels, safety filtering, and overlap checks remain mandatory |
| WildChat/LMSYS chat logs | Hold from the flagship backbone | Useful for behavior discovery; privacy, consent, memorization, and weak gains in earlier ablations argue against default inclusion |

## Synthetic product to build

Build two linked products rather than translating one English pool everywhere:

1. `oellm-eu-native-instruct-v1`: grounded prompts and answers derived from
   native public documents, exams, cultural institutions, open educational
   resources, and community-authored tasks. Include strict formatting,
   correction, summarization, tool-recovery, and calibrated abstention.
2. `oellm-eu-reasoning-v1`: problems with machine-checkable final answers or
   an independent solver/judge agreement record. Preserve the original prompt,
   translated prompt, trace language, final answer, teacher identity, verifier,
   and native-review status as distinct fields.

For lower-resource languages, generate multiple candidate answers from at
least two independent teachers, verify the final answer before considering
trace style, and select on correctness plus language fidelity. Compare
fully-native reasoning against target-language prompt + English hidden
reasoning; do not make private chain-of-thought release a prerequisite for
answer quality.

## Initial ablations

- General SFT control: the completed EuroBlocks/Tülu recipe.
- Native/translated ablation: the same total tokens with native, translated,
  and synthetic shares reported separately.
- Reasoning integration: 50% general multilingual replay, 30% verified
  reasoning, and 20% structured/tool data as a starting experiment—not a
  production commitment.
- Teacher ablation: Dolci 7B versus 32B, then one OpenThoughts3/Nemotron-Math
  slice after parent-family deduplication.
- Trace ablation: visible target-language trace, hidden/English reasoning, and
  final-answer-only distillation at matched trainable tokens.

## Acceptance gates

- Improvement on protected multilingual instruction and reasoning suites,
  reported as macro, p10, and minimum language.
- EUROPA reading, arithmetic, strict formatting, translation, summarization,
  and tool recovery improve or remain within signed non-regression bounds; its
  public rows remain evaluation-only.
- At least 100 formatted examples per major source/language are reviewed, with
  native review focused on lower-resource and non-Latin-script languages.
- Final-answer accuracy is measured independently of trace similarity and
  generated-token cost.
- Source-family ablations show incremental value; large parent/derivative
  duplicates are not rewarded twice.
- Safety, refusal calibration, tool validity, and 128K retention all pass after
  reasoning integration.

## Questions for the thread

1. Which languages should receive the first native-instruction sprint?
2. Should reasoning be a separate checkpoint/branch or mandatory in the
   general assistant?
3. What trace-language and release policy should apply?
4. Who can perform solver and native-language audits for the translated Dolci
   Think pilot?
