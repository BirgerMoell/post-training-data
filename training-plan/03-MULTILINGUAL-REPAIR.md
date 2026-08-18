# Stage 3 — multilingual coverage and language repair

## Goal

Repair weak languages without turning the flagship into a collection of narrow
language adapters. This stage begins from the general SFT checkpoint and keeps
English/general replay while explicitly balancing European languages.

## Available data

### Broad instruction data

- [Dolci Instruct translated](../datasets/openeurollm-dolci-instruct-sft-translated/README.md):
  `cs,de,el,es,fi,fr,it,nl,pl,ro,sv,uk`.
- [EU-Instruct-Synthetic](../datasets/openeurollm-eu-instruct-synthetic/README.md):
  `cs,de,el,es,fr,it,nl,pl,pt,ro,uk`.
- Original/decontaminated English Dolci for replay.

Their union provides broad general SFT for English plus 13 European languages:
`cs,de,el,es,fi,fr,it,nl,pl,pt,ro,sv,uk`.

### Targeted repair data

- [OpenEuroLLM EU defect-repair SFT v1](../datasets/birgermoell-oellm-eu-defect-repair-sft-v1/README.md):
  `is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi`.
- [Per-language Wikipedia](../datasets/per-language-wikipedia/README.md):
  continued-pretraining/reference text for language repair, not a substitute
  for instruction conversations.
- [AutoIF-FI](../datasets/lumiopen-autoif-fi/README.md): Finnish
  instruction/constraint candidate.
- [LUMI Poro2 instruction data](../datasets/lumi-poro2-instruction-data/README.md):
  4.65 GB pre-rendered corpus with Finnish samples; use only after source,
  license, language-distribution, and loss-mask validation.
- The planned `oellm-eu-native-instruct-v1` family is not yet available.

## Proposed two-pass procedure

### Pass A — balanced multilingual general SFT

Run a matched-compute ratio sweep:

- 75% English / 25% European;
- 50% English / 50% European; and
- 25% English / 75% European.

Within the European share, use temperature-smoothed language sampling and set a
minimum trainable-token floor per language. Report actual tokens per language;
equal row counts are not equal training exposure.

Select the checkpoint from a Pareto analysis over English, high-resource EU,
low-resource EU, instruction following, and long-context retention. Do not
select on the multilingual average alone.

### Pass B — defect repair

1. Diagnose weak languages on protected evaluation prompts.
2. Include only repair categories with a measured defect: script mixing,
   untranslated output, grammar, morphology, instruction noncompliance, or
   language refusal.
3. Use a low LR and cap each repair language so narrow templates cannot
   dominate.
4. Keep 40–60% general multilingual replay by trainable tokens.
5. Save checkpoints frequently and stop when the target defect improves or
   general capability begins to regress.

The 40–60% replay range is a proposed starting point, not a completed recipe.

## Native-versus-translated requirement

For each language, label the source as native, translated, synthetic-native,
or uncertain. Build evaluation slices for translationese, local entities,
regional knowledge, idiom, formality, and code-switching. A language is not
"covered" merely because machine-translated SFT exists.

## Exit gate

- Every claimed language has a minimum reviewed token budget and at least 100
  human-inspected formatted examples across its sources.
- Repair-set improvements reproduce on held-out native evaluation, not only on
  generated repair templates.
- English, neighboring languages, reasoning, safety, and long-context metrics
  remain inside agreed regression limits.
- The selected ratio and temperature are recorded with per-language tokens.
- Languages with only narrow repair data are explicitly described as limited
  coverage in the model card.

## Missing

The following EU official languages currently have targeted repair material
but not broad general instruction coverage comparable to Dolci translated:
`bg,hr,da,et,ga,hu,lv,lt,mt,sk,sl`. Native instruction data is also thin or
unverified for many nominally covered languages. Reasoning, preference,
tool-use, safety, and long-context instruction coverage are substantially
narrower; see [LANGUAGE_COVERAGE.md](LANGUAGE_COVERAGE.md).
