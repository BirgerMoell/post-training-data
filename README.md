# OpenEuroLLM Post-Training Data

A human-first catalogue of data sources and artifacts used or considered for OpenEuroLLM post-training.

This repository answers five practical questions:

1. What data do we have?
2. Which part of training can it be used for?
3. Which languages does it cover?
4. Where can it be found?
5. What is its current state and next action?

The initial catalogue was seeded from the OpenEuroLLM post-training data register on 2026-08-18. Each dataset or product has its own page and can be updated through an ordinary pull request.

## Data available by training stage

This is the quickest view of the data currently available to the project.
`Used` means there is evidence of a completed or research run, `published`
means the data can be obtained publicly, and `staged` means a concrete LUMI
artifact was inspected. Follow a dataset link for its exact path, format,
revision, size, and usage notes.

| Training stage / capability | Main data available | Language coverage | State and storage |
| --- | --- | --- | --- |
| **Context extension / continued pretraining** | [Jouni Luoma long-context blend](datasets/lumi-long-context-sample/README.md); [streamed multilingual long context](datasets/birgermoell-oellm-longctx-tokenized-streamed-all-v2/README.md); [natural 128k/256k pilot](datasets/birgermoell-oellm-longctx-tokenized-natural-128k-256k-pilot-v1/README.md); [structured 128k/256k](datasets/birgermoell-oellm-longctx-tokenized-structured-128k-256k-v1/README.md) | European multilingual plus English, code, mathematics, and science | **Used:** 205 GB LUMI blend and completed 16k/64k/128k runs. **Published:** portable Hugging Face variants |
| **Long-context instruction / retention** | [English–Finnish long-context SFT](datasets/lumi-long-context-eng-fin-sft/README.md); [BookSum](datasets/lumi-booksum/README.md); [ChatQA2](datasets/nvidia-chatqa2-long-sft-data/README.md); [LongAlign](datasets/thudm-longalign-10k/README.md); [LongAlpaca](datasets/yukang-longalpaca-12k/README.md) | English and Finnish in the inspected LUMI blend; public candidates are mostly English | **Staged:** 18.3 GB conversation JSONL plus 16.6 GB Megatron binary on LUMI. Other sources are published candidates |
| **General instruction and chat SFT** | [Dolci SFT decontaminated](datasets/openeurollm-dolci-instruct-sft-decontaminated/README.md); [Dolci translated](datasets/openeurollm-dolci-instruct-sft-translated/README.md); [EU-Instruct-Synthetic](datasets/openeurollm-eu-instruct-synthetic/README.md); [Open-PerfectBlend](datasets/openeurollm-open-perfectblend-decontaminated/README.md); [Orca AgentInstruct](datasets/openeurollm-orca-agentinstruct-1m-v1-decontaminated/README.md); [LMSYS Chat 1M](datasets/openeurollm-lmsys-chat-1m-decontaminated/README.md); [Poro2 instruction data](datasets/lumi-poro2-instruction-data/README.md) | English plus broad SFT in `cs,de,el,es,fi,fr,it,nl,pl,pt,ro,sv,uk` | **Published:** main OpenEuroLLM datasets on Hugging Face. **Staged:** 4.65 GB Poro2 JSONL and Megatron binary on LUMI |
| **Multilingual and language repair** | [EU defect-repair SFT v1](datasets/birgermoell-oellm-eu-defect-repair-sft-v1/README.md); [per-language Wikipedia](datasets/per-language-wikipedia/README.md); [AutoIF-FI](datasets/lumiopen-autoif-fi/README.md); [Poro2 instruction data](datasets/lumi-poro2-instruction-data/README.md) | Repair data in `is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi`; Poro2 and AutoIF add Finnish | **Used:** defect-repair and Wikipedia sources. **Staged/candidate:** Poro2 and AutoIF-FI |
| **Reasoning SFT** | [Dolci Think 7B](datasets/openeurollm-dolci-think-sft-7b-decontaminated/README.md); [Dolci Think 32B](datasets/openeurollm-dolci-think-sft-32b-decontaminated/README.md); [Nemotron v2 decontaminated](datasets/openeurollm-nemotron-post-training-dataset-v2-decontaminated/README.md); [OpenR1-Math-220k](datasets/lumi-openr1-math-220k/README.md); [AM R1 think mixture](datasets/lumi-am-deepseek-r1-think/README.md); [Finnish distilled math](datasets/finnish-deepseek-distilled-math-corpus/README.md); [OpenThoughts2](datasets/open-thoughts-openthoughts2-1m/README.md) | Primarily English, with a Finnish seed and planned multilingual translations | **Published:** Dolci/Nemotron/OpenThoughts. **Staged:** 5.12 GB OpenR1 Math and 40.2 GB AM reasoning mix on LUMI |
| **Code SFT** | [Glaive Code Assistant v3](datasets/lumi-glaive-code-assistant-v3/README.md); [Python R1-format RLVR data](datasets/allenai-rlvr-code-data-python-r1-format-filtered/README.md); code components in the [AM reasoning mixture](datasets/lumi-am-deepseek-r1-think/README.md) | English instructions across many programming languages | **Staged:** 1.92 GB Glaive JSONL and 9.89 GB AM code component on LUMI. Python RLVR source is catalogued |
| **Function calling and agents** | [OpenEuroLLM function-calling mixture](datasets/openeurollm-function-calling-mixture-220/README.md); [EU tool-use v1](datasets/birgermoell-oellm-eu-tooluse-v1/README.md); [ToolACE](datasets/team-ace-toolace/README.md); [Hermes function calling](datasets/nousresearch-hermes-function-calling-v1/README.md); [Glaive function calling](datasets/glaiveai-glaive-function-calling-v2/README.md); [Nemotron Agentic](datasets/nvidia-nemotron-agentic-v1-tool-calling/README.md); [xLAM](datasets/salesforce-xlam-function-calling-60k/README.md) | Predominantly English; EU tool-use v1 is currently English | **Used:** OpenEuroLLM, EU tool-use, ToolACE, Hermes, and Glaive sources. **Candidate:** Nemotron Agentic and xLAM |
| **Preference optimization / DPO** | [Dolci DPO translated](datasets/openeurollm-dolci-instruct-dpo-translated/README.md); [SmolTalk2 decontaminated](datasets/openeurollm-smoltalk2-decontaminated/README.md); [Dolci DPO](datasets/allenai-dolci-instruct-dpo/README.md); [HelpSteer3](datasets/nvidia-helpsteer3/README.md); [UltraFeedback](datasets/ultrafeedback/README.md); [exam DPO](datasets/exam-dpo-parquet/README.md); [medical DPO](datasets/medical-dpo-parquet/README.md) | English plus translated Dolci in `cs,de,el,es,fi,fr,it,pl,ro,sv,uk`; Swedish medical data | **Published/used:** Dolci and SmolTalk2. **Staged/configured:** HelpSteer3 and project-specific Parquet artifacts on LUMI |
| **RLVR / GRPO data** | [European exam MCQ v1](datasets/birgermoell-oellm-eu-exam-mcq-v1/README.md); [official exam bundle](datasets/european-official-national-exam-bundle-23-ids/README.md); [OpenR1 Math](datasets/lumi-openr1-math-220k/README.md); [GSM/MATH/IF constraints](datasets/allenai-rlvr-gsm-math-if-mixed-constraints/README.md); [Python code](datasets/allenai-rlvr-code-data-python-r1-format-filtered/README.md); [EU tool-use v1](datasets/birgermoell-oellm-eu-tooluse-v1/README.md) | Multilingual European exams; English math/code/tools; Finnish constraints through AutoIF-FI | **Used/published/staged:** prompt and verifier-source data exists across Hugging Face and LUMI |
| **Medical specialization** | [EU medical post-train v1](datasets/birgermoell-oellm-eu-medical-posttrain-v1/README.md); [medical SFT](datasets/medical-sft-parquet/README.md); [medical DPO](datasets/medical-dpo-parquet/README.md) | Primarily Swedish, with additional multilingual source/evaluation material | **Published:** source collection. **Configured/staged:** SFT and DPO Parquet artifacts on LUMI |
| **Safety and civic training** | [OpenEuroLLM EU safety/civic v1](datasets/oellm-eu-safety-civic-v1/README.md) | Intended to be multilingual European | **Planned:** catalogue entry exists; no canonical stored training artifact yet |
| **Protected evaluation — never train** | [EU evaluation holdouts](datasets/birgermoell-oellm-eu-eval-holdouts-v1/README.md); [ArenaHard-EU](datasets/openeurollm-arenahard-eu-v0-v0-bis/README.md); [FLORES/FLORES+](datasets/lumi-flores-200/README.md); [Tatoeba en–fi](datasets/lumi-tatoeba-eng-fin/README.md); [Jeopardy](datasets/openeurollm-jeopardy/README.md); [Global-MMLU](datasets/coherelabs-global-mmlu/README.md); [MMMLU](datasets/openai-mmmlu/README.md); [Belebele](datasets/facebook-belebele/README.md); [XCOPA](datasets/cambridgeltl-xcopa/README.md); [EXAMS-QA](datasets/exams-qa/README.md) | Broad European multilingual coverage | **Evaluation-only:** public and LUMI copies are catalogued so they remain outside training |

For the complete inventory, browse [all datasets and products](CATALOGUE.md),
[training-type views](training-types/README.md), or
[language views](languages/README.md).

## Detailed training guidance

The [stage-by-stage training plan](training-plan/README.md) maps these sources
to proposed mixtures, framework handoffs, training procedures, and evaluation
gates. The table above is the recommended starting point when the immediate
question is simply what data exists.

## Browse the catalogue

- [Detailed stage-by-stage training guidance](training-plan/README.md)
- [Language coverage by capability](training-plan/LANGUAGE_COVERAGE.md)
- [By training type](training-types/README.md)
- [By language](languages/README.md)
- [By state](status/README.md)
- [All datasets and products](CATALOGUE.md)
- [Storage locations](storage/README.md)

## How this repository is organised

```text
datasets/<dataset>/README.md        One page per data source or artifact
training-types/<type>/README.md     SFT, preference, RLVR, long context, etc.
languages/<language>/README.md      Language-oriented views
status/<state>/README.md            Used, available, candidate, planned, etc.
storage/README.md                   Shared storage roots and conventions
```

The indexes are generated from the small metadata block at the top of each dataset page:

```bash
python3 scripts/build_indexes.py
python3 scripts/build_indexes.py --check
```

## Reading a dataset page

Each page contains:

- **What it is for** — the training stage and capability.
- **Where to find it** — upstream/public location and known LUMI artifact.
- **How to use it** — the expected training shape and basic checks.
- **State** — availability, ownership, access/licensing, and confidence.
- **Next action** — what is still missing before production use.

A path means “known to have existed at the verification date,” not a promise that it is still present. Verify LUMI paths and pin public dataset revisions before production runs.

## Scope

The catalogue covers instruction SFT, reasoning SFT, preference optimization, RLVR/GRPO, tools and agents, long-context extension, continued pretraining used in post-training sequences, language repair, domain specialization, safety data, filtering support, and evaluation holdouts.

Evaluation-only entries are deliberately included so that they are visible and kept out of training.

The detailed training plan distinguishes confirmed runs and artifacts from
proposed recipes. Proposed mixture weights are starting points for ablation,
not records of completed OpenEuroLLM runs.

## Related repositories

- [OpenEuroLLM/post-training](https://github.com/OpenEuroLLM/post-training)
- [OpenEuroLLM/training-data-collection](https://github.com/OpenEuroLLM/training-data-collection)
- [OpenEuroLLM/training-data-catalogue](https://github.com/OpenEuroLLM/training-data-catalogue)
- [OpenEuroLLM/post-training-decontamination](https://github.com/OpenEuroLLM/post-training-decontamination)

See [CONTRIBUTING.md](CONTRIBUTING.md) to add or update an entry and [MIRRORING.md](MIRRORING.md) for the future OpenEuroLLM mirror.
