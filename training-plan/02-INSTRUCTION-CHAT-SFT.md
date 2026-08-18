# Stage 2 — general instruction following and chat SFT

## Goal

Turn the context-extended base into a useful assistant without losing base
multilingual knowledge or long-context capability. Produce a general SFT
checkpoint that can feed multilingual repair, reasoning/tool branches, and
preference optimization.

## Available data

| Source | State | Recommended role |
| --- | --- | --- |
| [Dolci-Instruct-SFT decontaminated](../datasets/openeurollm-dolci-instruct-sft-decontaminated/README.md) | Public | Primary English instruction source |
| [Dolci Instruct tokenized](../datasets/openeurollm-dolci-instruct-sft-tokenized/README.md) | Public, OLMo-core-specific | OLMo reproduction only; 2.15M examples, 1.7B tokens |
| [Dolci Instruct translated](../datasets/openeurollm-dolci-instruct-sft-translated/README.md) | Public, 12 languages | Main translated European source |
| [EU-Instruct-Synthetic](../datasets/openeurollm-eu-instruct-synthetic/README.md) | Public, 1.5M pairs in 11 languages | Constraint-following breadth after quality filtering |
| [Open-PerfectBlend decontaminated](../datasets/openeurollm-open-perfectblend-decontaminated/README.md) | Public | Diverse instruction/chat replay |
| [Orca-AgentInstruct decontaminated](../datasets/openeurollm-orca-agentinstruct-1m-v1-decontaminated/README.md) | Public | Complex instructions; keep tool-specific rows for Stage 4 |
| [LMSYS Chat 1M decontaminated](../datasets/openeurollm-lmsys-chat-1m-decontaminated/README.md) | Public and on LUMI | Multi-turn style and real-user distribution; apply privacy/toxicity filters |
| [Tulu-3 SFT mixture](../datasets/allenai-tulu-3-sft-mixture/README.md) | Used in completed run | Reproduction/control mixture |
| [EuroBlocks synthetic SFT](../datasets/euroblocks-sft-synthetic-1124/README.md) | Used in completed run on LUMI | European multilingual control; provenance review required |
| [LUMI Poro2 instruction data](../datasets/lumi-poro2-instruction-data/README.md) | 4.65 GB JSONL plus Megatron binary; Finnish observed | Finnish replay/ablation only after provenance, license, and language audit |
| [LUMI English–Finnish long-context SFT](../datasets/lumi-long-context-eng-fin-sft/README.md) | 18.3 GB JSONL plus Megatron binary | P0 retention experiment; not approved until lineage, lengths, and loss mask pass |

## Proposed v0 mixture

The following is a pilot starting point measured by **trainable assistant
tokens**, not rows:

| Component | Share | Notes |
| --- | ---: | --- |
| English decontaminated general SFT | 35% | Dolci plus a capped share of Open-PerfectBlend |
| Dolci translated | 35% | Balance languages explicitly; do not sample by raw dataset size |
| EU-Instruct-Synthetic | 15% | Keep only rows passing language, constraint, duplication, and quality checks |
| Multi-turn conversation | 10% | LMSYS/other approved chat; retain only privacy-safe rows |
| Native/repair seed | 5% | High-confidence native items and defect-repair examples; a validated Poro2 subset can enter here |

Run 75:25, 50:50, and 25:75 English:European ablations by adjusting the
first two/three components. Public OpenEuroLLM OLMo-3 experiments show that a
25% English / 75% EU continued-SFT mix improved non-English Elo but reduced
English Elo, so the flagship ratio must be chosen from the multilingual/English
Pareto curve rather than assumed
([model card](https://huggingface.co/openeurollm/OLMo-3-7B-Dolci-Translated-A-25EN)).

For a release claiming 128k, reserve 10–20% of total optimizer tokens for the
retention strategy selected in Stage 1, reducing the five shares
proportionally. Test the staged English–Finnish long-SFT asset as the first
candidate, but do not promote it without measured 64k/128k tokens and a verified
assistant mask. This overlay is not optional for the flagship run.

## Proposed training procedure

1. Start from the Stage 1 checkpoint; do not silently switch to the
   short-context base.
2. Normalize all sources to the target model's conversation/tool representation
   while retaining source and language metadata.
3. Apply one reviewed chat template. Train assistant response tokens only.
4. Start a 7–9B full-finetune pilot from the common TRL configuration:
   BF16, gradient checkpointing, peak LR near `2e-5`, 3% warmup, cosine decay,
   and token-based run length. Run a short LR sweep before scaling. Do not copy
   these values to a much larger or MoE model without a stability pilot.
5. Use 32k as the normal SFT ceiling because the public Dolci tokenized
   reference was prepared at 32,768. Bucket by length and report packing waste.
6. Save evaluation checkpoints at approximately 10%, 25%, 50%, 75%, and 100%
   of the token budget. Prefer the best common-gate checkpoint over the last one.
7. Compare one epoch against a fixed-token matched-compute run. Stop if dev loss
   keeps improving while instruction or multilingual evaluation regresses.

## Required data checks

- Language ID on prompt and response separately.
- Assistant-only loss masks and zero trainable user/system tokens.
- Exact/near duplicate rate within and across sources.
- Constraint satisfaction on EU-Instruct-Synthetic.
- Translation adequacy and language naturalness on Dolci translated.
- Privacy, toxicity, and personal-data sampling on conversational data.
- Per-language trainable-token totals after truncation and packing.
- Benchmark decontamination using the Stage 0 protected index.

## Exit gate

- Instruction following and chat quality improve against the Stage 1 model.
- English and each reported European-language group stay inside agreed
  regression limits.
- 4k/32k/64k/128k retention tests pass; a failure blocks Stage 3.
- The selected English:EU ratio has an ablation report.
- The output checkpoint, frozen data mix, chat template, trainable-token masks,
  code/container, logs, and evaluations are retained together.

## Missing

- Approval evidence for the staged English–Finnish long-context data and broad
  European long-SFT/replay coverage beyond English/Finnish.
- Safe generation-mask support for ChatML, Tulu3, and Apertus templates in the
  common framework.
- Broad native instruction data for the official languages currently covered
  only by the repair set.
- A human-reviewed quality report for EU-Instruct-Synthetic and translated
  Dolci by language.
