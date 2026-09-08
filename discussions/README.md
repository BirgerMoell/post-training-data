# Post-training dataset decision discussions

These five briefs are the durable source for GitHub Discussions about the next
post-training data freeze. They start from the repository catalogue and the
`Data` tab of the [OpenEuroLLM post-training register](https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209),
but they are decisions rather than another undifferentiated dataset list.

| Discussion | Decision to make |
| --- | --- |
| [Long-context extension](01-long-context-extension.md) | Which continued-pretraining and long-instruction sources qualify 128K first, with 256K and 512K+ kept as explicit promotions |
| [SFT and reasoning](02-sft-and-reasoning.md) | Which general, multilingual, and verified-reasoning sources form the assistant backbone |
| [DPO and GRPO](03-dpo-and-grpo.md) | How to combine offline preference data with a narrow verifier-backed GRPO bridge |
| [Reinforcement learning](04-reinforcement-learning.md) | Which task banks, environments, and verifiers are mature enough for broader online RL |
| [Safety](05-safety.md) | How to materialize the missing multilingual safety/civic SFT and preference products |

## Shared objective

The model should improve across the 36 languages in [EUROPA Eval](https://birgermoell.github.io/europa-eval/):
Bulgarian, Czech, Danish, German, Greek, English, Estonian, Finnish, French,
Irish, Croatian, Hungarian, Italian, Latvian, Lithuanian, Maltese, Dutch,
Polish, Portuguese, Romanian, Slovak, Slovene, Spanish, Swedish, Catalan,
Basque, Galician, Bosnian, Georgian, Macedonian, Albanian, Serbian, Turkish,
Ukrainian, Icelandic, and Norwegian.

EUROPA's public v0.1 pilot has 12 parallel capability templates per language:
reading, arithmetic, grounded answering, calibrated abstention, structured
output, strict instruction following, tool recovery, a surface calculation,
summarization, translation, harmful-request refusal, and revision tracking.
It is a public development and translation-review set, not training data and
not a statistically complete leaderboard. No prompt, answer, translation,
paraphrase, source document, or generator prompt derived from it may enter a
training, preference, rollout, retrieval, or synthetic-data pipeline. Stage
promotion should use a separately frozen protected suite while EUROPA remains
a transparent regression diagnostic.

## Common decision vocabulary

- **Use**: evidence is strong enough to enter the first frozen mix after exact
  revision, checksum, license, and transformation manifests are recorded.
- **Pilot**: include in a controlled ablation, never by default; promotion
  requires the gates named in the relevant discussion.
- **Hold**: do not train on it yet. It may still be useful for threat discovery,
  taxonomy design, or source ideas.
- **Evaluation-only**: exclude it and its semantic derivatives from every
  training stage.

## Non-negotiable data contract

Every admitted source must record the immutable upstream revision, split and
row IDs; source-level license and access decision; native, translated, or
synthetic status; ISO 639-3 plus script; rendered-token and length statistics;
exact/fuzzy/semantic deduplication; personally identifiable information and
secret scans; benchmark-family overlap; generator, judge, and verifier
versions; accepted/rejected counts; and checksums for the final bytes.

Mixture weights are measured in rendered trainable tokens, not rows. Results
must be reported by source family, language, script, length/difficulty bucket,
and the weakest language—not only as a global mean.

## Cross-stage experiment contract

1. Freeze a common base and protected evaluation manifest.
2. Evaluate the base, then every stage checkpoint, under identical decoding.
3. Keep matched-compute controls: no-new-source, no-synthetic, English-only,
   native-only where possible, translated-only, and no-RL.
4. Reject a stage that improves its local objective while materially degrading
   another capability, the minimum-language score, refusal calibration, or
   short/long-context retention.
5. Publish the selected and rejected recipes with their manifests. Negative
   ablations are part of the evidence.

## Proposed order

`base → context extension → general/multilingual SFT → reasoning integration → DPO → narrow GRPO → broader RL → safety integration/recovery`

Safety examples and gates are present throughout; the last step is integration
and recovery, not the first time safety is considered. The exact order between
DPO, GRPO, and safety should remain an ablation if an intermediate checkpoint
shows capability interference.
