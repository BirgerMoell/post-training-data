# OpenEuroLLM Post-Training Data

A human-first catalogue of data sources and artifacts used or considered for OpenEuroLLM post-training. Its entry layout, versioning, lifecycle, language identifiers, and statistics fields follow the [OpenEuroLLM training-data catalogue](https://github.com/OpenEuroLLM/training-data-catalogue).

This repository answers five practical questions:

1. What data do we have?
2. Which part of training can it be used for?
3. Which languages does it cover?
4. Where can it be found?
5. What is its current state and next action?

The catalogue contains 114 versioned entries: 104 seeded from the [OpenEuroLLM post-training data register](https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209) and 10 later LUMI/Hugging Face discoveries. Each source or product has its own versioned page and can be updated through an ordinary pull request.

Two states are intentionally kept separate:

- **Catalogue lifecycle:** `D` draft, `P` published, or `E` deprecated, matching the official training-data catalogue.
- **Operational readiness:** used, staged, candidate, planned, evaluation-only, and the other post-training states already maintained in the spreadsheet.

`P` means that the catalogue entry is published; it does not by itself mean that the data is approved for a flagship training run. See [catalogue conventions](CATALOGUE-CONVENTIONS.md) for the precise mapping.

## Data available by training stage

This is the quickest view of the data currently available to the project.
`Used` means there is evidence of a completed or research run, `published`
means the data can be obtained publicly, and `staged` means a concrete LUMI
artifact was inspected. Follow a dataset link for its exact path, format,
revision, size, and usage notes.

| Training stage / capability | Main data available | Language coverage | State and storage |
| --- | --- | --- | --- |
| **Context extension / continued pretraining** | [Jouni Luoma long-context blend](lumi-long-context-sample/0.0.0/README.md); [streamed multilingual long context](birgermoell-oellm-longctx-tokenized-streamed-all-v2/0.0.0/README.md); [natural 128k/256k pilot](birgermoell-oellm-longctx-tokenized-natural-128k-256k-pilot-v1/0.0.0/README.md); [structured 128k/256k](birgermoell-oellm-longctx-tokenized-structured-128k-256k-v1/0.0.0/README.md); [superlong 512k/1M/2M v2](birgermoell-oellm-longctx-tokenized-superlong-512k-1m-2m-v2/0.0.0/README.md) | European multilingual plus English, code, mathematics, and science | **Used:** 205 GB LUMI blend and completed 16k/64k/128k runs. **Published:** portable Hugging Face variants, including a 5.84 GB 512k/1M/2M Megatron artifact |
| **Long-context instruction / retention** | [English–Finnish long-context SFT](lumi-long-context-eng-fin-sft/0.0.0/README.md); [BookSum](lumi-booksum/0.0.0/README.md); [ChatQA2](nvidia-chatqa2-long-sft-data/0.0.0/README.md); [LongAlign](thudm-longalign-10k/0.0.0/README.md); [LongAlpaca](yukang-longalpaca-12k/0.0.0/README.md) | English and Finnish in the inspected LUMI blend; public candidates are mostly English | **Staged:** 18.3 GB conversation JSONL plus 16.6 GB Megatron binary on LUMI. Other sources are published candidates |
| **General instruction and chat SFT** | [Dolci SFT decontaminated](openeurollm-dolci-instruct-sft-decontaminated/0.0.0/README.md); [Dolci translated](openeurollm-dolci-instruct-sft-translated/0.0.0/README.md); [EU-Instruct-Synthetic](openeurollm-eu-instruct-synthetic/0.0.0/README.md); [Open-PerfectBlend](openeurollm-open-perfectblend-decontaminated/0.0.0/README.md); [Orca AgentInstruct](openeurollm-orca-agentinstruct-1m-v1-decontaminated/0.0.0/README.md); [LMSYS Chat 1M](openeurollm-lmsys-chat-1m-decontaminated/0.0.0/README.md); [Poro2 instruction data](lumi-poro2-instruction-data/0.0.0/README.md) | English plus broad SFT in `cs,de,el,es,fi,fr,it,nl,pl,pt,ro,sv,uk` | **Published:** main OpenEuroLLM datasets on Hugging Face. **Staged:** 4.65 GB Poro2 JSONL and Megatron binary on LUMI |
| **Multilingual and language repair** | [EU defect-repair SFT v1](birgermoell-oellm-eu-defect-repair-sft-v1/0.0.0/README.md); [per-language Wikipedia](per-language-wikipedia/0.0.0/README.md); [AutoIF-FI](lumiopen-autoif-fi/0.0.0/README.md); [Poro2 instruction data](lumi-poro2-instruction-data/0.0.0/README.md) | Repair data in `is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi`; Poro2 and AutoIF add Finnish | **Used:** defect-repair and Wikipedia sources. **Staged/candidate:** Poro2 and AutoIF-FI |
| **Reasoning SFT** | [Dolci Think 7B](openeurollm-dolci-think-sft-7b-decontaminated/0.0.0/README.md); [Dolci Think 32B](openeurollm-dolci-think-sft-32b-decontaminated/0.0.0/README.md); [Nemotron v2 decontaminated](openeurollm-nemotron-post-training-dataset-v2-decontaminated/0.0.0/README.md); [OpenR1-Math-220k](lumi-openr1-math-220k/0.0.0/README.md); [AM R1 think mixture](lumi-am-deepseek-r1-think/0.0.0/README.md); [Finnish distilled math](finnish-deepseek-distilled-math-corpus/0.0.0/README.md); [OpenThoughts2](open-thoughts-openthoughts2-1m/0.0.0/README.md) | Primarily English, with a Finnish seed and planned multilingual translations | **Published:** Dolci/Nemotron/OpenThoughts. **Staged:** 5.12 GB OpenR1 Math and 40.2 GB AM reasoning mix on LUMI |
| **Code SFT** | [Glaive Code Assistant v3](lumi-glaive-code-assistant-v3/0.0.0/README.md); [Python R1-format RLVR data](allenai-rlvr-code-data-python-r1-format-filtered/0.0.0/README.md); code components in the [AM reasoning mixture](lumi-am-deepseek-r1-think/0.0.0/README.md) | English instructions across many programming languages | **Staged:** 1.92 GB Glaive JSONL and 9.89 GB AM code component on LUMI. Python RLVR source is catalogued |
| **Function calling and agents** | [OpenEuroLLM function-calling mixture](openeurollm-function-calling-mixture-220/0.0.0/README.md); [EU tool-use v1](birgermoell-oellm-eu-tooluse-v1/0.0.0/README.md); [ToolACE](team-ace-toolace/0.0.0/README.md); [Hermes function calling](nousresearch-hermes-function-calling-v1/0.0.0/README.md); [Glaive function calling](glaiveai-glaive-function-calling-v2/0.0.0/README.md); [Nemotron Agentic](nvidia-nemotron-agentic-v1-tool-calling/0.0.0/README.md); [xLAM](salesforce-xlam-function-calling-60k/0.0.0/README.md) | Predominantly English; EU tool-use v1 is currently English | **Used:** OpenEuroLLM, EU tool-use, ToolACE, Hermes, and Glaive sources. **Candidate:** Nemotron Agentic and xLAM |
| **Preference optimization / DPO** | [Dolci DPO translated](openeurollm-dolci-instruct-dpo-translated/0.0.0/README.md); [SmolTalk2 decontaminated](openeurollm-smoltalk2-decontaminated/0.0.0/README.md); [Dolci DPO](allenai-dolci-instruct-dpo/0.0.0/README.md); [HelpSteer3](nvidia-helpsteer3/0.0.0/README.md); [UltraFeedback](ultrafeedback/0.0.0/README.md); [exam DPO](exam-dpo-parquet/0.0.0/README.md); [medical DPO](medical-dpo-parquet/0.0.0/README.md) | English plus translated Dolci in `cs,de,el,es,fi,fr,it,pl,ro,sv,uk`; Swedish medical data | **Published/used:** Dolci and SmolTalk2. **Staged/configured:** HelpSteer3 and project-specific Parquet artifacts on LUMI |
| **RLVR / GRPO data** | [European exam MCQ v1](birgermoell-oellm-eu-exam-mcq-v1/0.0.0/README.md); [official exam bundle](european-official-national-exam-bundle-23-ids/0.0.0/README.md); [OpenR1 Math](lumi-openr1-math-220k/0.0.0/README.md); [GSM/MATH/IF constraints](allenai-rlvr-gsm-math-if-mixed-constraints/0.0.0/README.md); [Python code](allenai-rlvr-code-data-python-r1-format-filtered/0.0.0/README.md); [EU tool-use v1](birgermoell-oellm-eu-tooluse-v1/0.0.0/README.md) | Multilingual European exams; English math/code/tools; Finnish constraints through AutoIF-FI | **Used/published/staged:** prompt and verifier-source data exists across Hugging Face and LUMI |
| **Medical specialization** | [EU medical post-train v1](birgermoell-oellm-eu-medical-posttrain-v1/0.0.0/README.md); [medical SFT](medical-sft-parquet/0.0.0/README.md); [medical DPO](medical-dpo-parquet/0.0.0/README.md) | Primarily Swedish, with additional multilingual source/evaluation material | **Published:** source collection. **Configured/staged:** SFT and DPO Parquet artifacts on LUMI |
| **Safety and civic training** | [OpenEuroLLM EU safety/civic v1](oellm-eu-safety-civic-v1/0.0.0/README.md) | Intended to be multilingual European | **Planned:** catalogue entry exists; no canonical stored training artifact yet |
| **Protected evaluation — never train** | [EU evaluation holdouts](birgermoell-oellm-eu-eval-holdouts-v1/0.0.0/README.md); [ArenaHard-EU](openeurollm-arenahard-eu-v0-v0-bis/0.0.0/README.md); [FLORES/FLORES+](lumi-flores-200/0.0.0/README.md); [Tatoeba en–fi](lumi-tatoeba-eng-fin/0.0.0/README.md); [Jeopardy](openeurollm-jeopardy/0.0.0/README.md); [Global-MMLU](coherelabs-global-mmlu/0.0.0/README.md); [MMMLU](openai-mmmlu/0.0.0/README.md); [Belebele](facebook-belebele/0.0.0/README.md); [XCOPA](cambridgeltl-xcopa/0.0.0/README.md); [EXAMS-QA](exams-qa/0.0.0/README.md) | Broad European multilingual coverage | **Evaluation-only:** public and LUMI copies are catalogued so they remain outside training |

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
- [European language identifiers](LANGUAGES.md)
- [By catalogue lifecycle](catalogue-status/README.md)
- [By operational state](status/README.md)
- [All datasets and products](CATALOGUE.md)
- [Storage locations](storage/README.md)
- [Catalogue conventions](CATALOGUE-CONVENTIONS.md)
- [Dataset ingestion workflow](DATASET-INGESTION.md)

## How this repository is organised

```text
<dataset>/<version>/README.md       Versioned catalogue entry (official layout)
etc/skeleton.md                     Required entry structure and metadata
training-types/<type>/README.md     SFT, preference, RLVR, long context, etc.
languages/<language>/README.md      Language-oriented views
catalogue-status/<D|P|E>/           Official catalogue lifecycle views
status/<state>/README.md            Post-training operational-readiness views
storage/README.md                   Shared storage roots and conventions
```

The indexes are generated from the small metadata block at the top of each dataset page:

```bash
python3 scripts/build_indexes.py
python3 scripts/build_indexes.py --check
```

## Reading a dataset page

Each page contains the official catalogue sections plus post-training extensions:

- **Background and Data Sources** — purpose, provenance, upstream material, and evidence.
- **Structure & Statistics and Available Metadata** — comparable counts, formats, schema, and missing inventory work.
- **European Language Support** — ISO 639-3 plus ISO 15924 identifiers and per-language statistics where known.
- **Access Information and Terms of Use** — public/project locations, verification date, and license/access status.
- **Post-Training Use & Readiness** — training shape, operational status, owner, confidence, and acceptance gates.
- **Quality, Safety & Exclusions** — contamination, privacy, legal, safety, and protected-evaluation requirements.
- **Catalogue Curator and Next Action** — accountable lead and unresolved work.

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
