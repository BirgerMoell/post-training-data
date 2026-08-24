# Stage 4 — reasoning and tool-use SFT

## Goal

Add reasoning and tool capabilities without allowing long traces, English-only
data, or synthetic tool schemas to erase the general multilingual assistant.
Train reasoning and tool branches separately first; combine only after each
branch passes its own gate.

## Reasoning data available

| Source | State | Use |
| --- | --- | --- |
| [Dolci Think 7B decontaminated](../openeurollm-dolci-think-sft-7b-decontaminated/0.0.0/README.md) | Public | Primary English reasoning SFT branch |
| [Dolci Think 32B decontaminated](../openeurollm-dolci-think-sft-32b-decontaminated/0.0.0/README.md) | Public | Higher-capacity teacher-trace ablation |
| [Nemotron Post-Training v2 decontaminated](../openeurollm-nemotron-post-training-dataset-v2-decontaminated/0.0.0/README.md) | Public | STEM/math/reasoning mix after split review |
| [OpenThoughts 114k](../open-thoughts-openthoughts-114k/0.0.0/README.md) and [OpenThoughts2 1M](../open-thoughts-openthoughts2-1m/0.0.0/README.md) | Candidate | Correctness-filtered ablations |
| [Finnish distilled math](../finnish-deepseek-distilled-math-corpus/0.0.0/README.md) | Used in completed run | Finnish reasoning seed |
| [MultiSynt OpenThoughts translations](../multisynt-openthoughts-translations/0.0.0/README.md) | Planned | Seven-language reasoning expansion; no canonical artifact recorded |
| [OpenR1-Math-220k on LUMI](../lumi-openr1-math-220k/0.0.0/README.md) | 5.12 GB local default JSONL; public upstream | Correctness-annotated math traces after pinning local derivation |
| [AM DeepSeek-R1 think mix on LUMI](../lumi-am-deepseek-r1-think/0.0.0/README.md) | 40.2 GB combined plus six component files | Large math/code/IF/science/multi-turn candidate; lineage and verification missing |
| [Glaive Code Assistant v3 on LUMI](../lumi-glaive-code-assistant-v3/0.0.0/README.md) | 950k public rows; 1.92 GB local JSONL | Code SFT after revision pinning, deduplication, and execution filtering |

## Tool/agentic data available

| Source | State | Use |
| --- | --- | --- |
| [OpenEuroLLM function-calling mixture](../openeurollm-function-calling-mixture-220/0.0.0/README.md) | Research run | Project control mixture; locate/freeze exact artifact |
| [OpenEuroLLM EU tool-use v1](../birgermoell-oellm-eu-tooluse-v1/0.0.0/README.md) | Used in completed run | Verified execution/function-call seed |
| [ToolACE](../team-ace-toolace/0.0.0/README.md) | Used in completed run | Diverse function calling |
| [Hermes function calling](../nousresearch-hermes-function-calling-v1/0.0.0/README.md) | Used in completed run | Structured calls/control |
| [Glaive function calling](../glaiveai-glaive-function-calling-v2/0.0.0/README.md) | Used in completed run | Additional English tool breadth |
| [Nemotron Agentic/SFT Agentic](../nvidia-nemotron-agentic-v1-tool-calling/0.0.0/README.md) | Research run | Interactive-agent candidate |
| [xLAM](../salesforce-xlam-function-calling-60k/0.0.0/README.md) | Candidate | Function-call generalization |

Most tool data is English. Do not advertise multilingual tool use from this
stage without a separate evaluation and translated/native tool artifact.

## Proposed reasoning branch

Start by trainable tokens with:

- 60% decontaminated reasoning data: Dolci Think plus selected Nemotron splits;
- 20% correctness-filtered math/code sources, initially comparing pinned
  OpenR1 Math with an execution-filtered Glaive slice;
- 20% general multilingual replay from the Stage 2 freeze.

Treat the 40.2 GB AM mixture as an ablation, not an automatic addition. First
recover its component provenance and compare each component independently. A
large pre-shuffled file makes source-level weighting and failure removal harder.

Run a 7B-versus-32B Dolci trace-source ablation and a no-visible-trace variant
if the target product should not expose chain-of-thought. Verify final answers
independently of teacher traces. Use the `olmo3-think-sft` safe template only
for compatible OLMo reproduction; Prelude needs a reviewed equivalent.

## Proposed tool branch

Start by trainable tokens with:

- 50% diverse function/tool calls from ToolACE, Hermes, Glaive, and the
  OpenEuroLLM mixture;
- 20% interactive or multi-step agent trajectories;
- 30% general multilingual replay.

Deduplicate tool schemas, canonicalize argument JSON, preserve structured tool
metadata, and reject examples whose call does not validate against the
declared schema. Separate training-time tools from evaluation tools to measure
schema generalization.

## Optional integration SFT

If both branches pass, run a short low-LR integration phase starting around:

- 50% general/multilingual replay;
- 30% reasoning; and
- 20% tool/agentic.

This is a pilot mixture. Select the final weights from ablations and keep the
reasoning-only and tool-only checkpoints for diagnosis.

## Exit gate

- Reasoning gains reproduce on held-out math, code, and multilingual tasks.
- Final-answer accuracy is reported separately from trace similarity.
- Tool calls parse, validate against schemas, choose the correct tool, and
  produce correct arguments on unseen schemas.
- General instruction, multilingual, safety, and 4k–128k retention gates pass.
- Source- and language-level trainable tokens and failure categories are
  retained in the run report.

## Missing

- Canonical stored artifact for MultiSynt reasoning translations.
- Broad non-English reasoning beyond the Finnish seed.
- Source/license/correctness manifest for the staged AM mixture and immutable
  derivations for the local OpenR1 and Glaive copies.
- Multilingual tool schemas, user requests, arguments, and tool responses.
- Execution-grounded multi-step agent trajectories with safe sandboxes.
- A project decision on visible versus hidden reasoning traces.
- One common evaluation gate shared by reasoning and tool owners.
