# Stage 1 — context extension

## Goal and placement

Extend the approved base checkpoint to the release context length before
short-sequence SFT. The default production target should be 128k unless WP4
explicitly approves 256k and the 256k evaluation/compute cost.

## Confirmed data and artifacts

| Asset | State | Role |
| --- | --- | --- |
| [Jouni Luoma LUMI long-context blend and runs](../datasets/lumi-long-context-sample/README.md) | Completed 16k/64k/128k lineage; directly verified | Primary reproducible baseline and LUMI data source |
| [Multilingual streamed long-context v2](../datasets/birgermoell-oellm-longctx-tokenized-streamed-all-v2/README.md) | Public | Portable multilingual Megatron-ready candidate |
| [Natural 128k/256k pilot](../datasets/birgermoell-oellm-longctx-tokenized-natural-128k-256k-pilot-v1/README.md) | Public | Natural long-document ablation |
| [Structured 128k/256k](../datasets/birgermoell-oellm-longctx-tokenized-structured-128k-256k-v1/README.md) | Public | Technical/structured ablation |
| [Superlong 512k–2M](../datasets/birgermoell-oellm-longctx-tokenized-superlong-512k-1m-2m-v2/README.md) | Public | Research beyond flagship target; not a default production input |
| HPLT/FinePDFs/Wikipedia/ArXiv/math/code components | Present inside Jouni blend | Source-family and language balancing |

### Retention candidates for the later SFT handoff

| Asset | Confirmed facts | Blocker before use |
| --- | --- | --- |
| [LUMI English–Finnish long-context SFT](../datasets/lumi-long-context-eng-fin-sft/README.md) | 18.3 GB JSONL plus 16.6 GB Megatron binary; Llama-3-style conversations | No source manifest, token-length distribution, license record, or verified assistant-only mask |
| [BookSum on LUMI](../datasets/lumi-booksum/README.md) | Public long-form summarization source with local train/validation/test JSONL | Input content is absent for some rows and source-text rights require review |
| [ChatQA2](../datasets/nvidia-chatqa2-long-sft-data/README.md), [LongAlign](../datasets/thudm-longalign-10k/README.md), and [LongAlpaca](../datasets/yukang-longalpaca-12k/README.md) | Public candidate families | Need revisions, licenses, length distributions, deduplication, and a project freeze |

Candidates such as FineWeb-2, CulturaX, The Stack v2, EUR-Lex,
LongAlign, LongAlpaca, and ChatQA2 should not enter the production mix until
their exact revision, license, length statistics, and deduplication status are
approved.

## Validated LUMI baseline

The directly inspected Prelude 9B lineage used packed pretraining with
document-isolated attention and the OpenEuroLLM 256k tokenizer:

| Phase | Sequence | RoPE base | Global batch | Budget | Start |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 16,384 | 1,000,000 | 512 sequences | about 5B tokens / 597 iterations | Prelude `iter_0830400` |
| 2 | 65,536 | 2,500,000 | 128 sequences | 29.36B tokens / 3,500 iterations | Phase 1 |
| 3 | 131,072 | 5,000,000 | 64 sequences | 16.78B tokens / 2,000 iterations | Phase 2 |

Phases 2 and 3 used TP=2, PP=2, CP=8 on 64 LUMI nodes, micro-batch 1,
roughly 8.4M tokens per iteration, peak LR `1e-6`, minimum LR `1e-8`,
100 warmup iterations, and a 500-iteration linear WSD cooldown. Treat these as
a confirmed baseline for a 9B Qwen3-like model, not universal hyperparameters
for every architecture.

## Proposed production procedure

1. **Pin the start.** Select the final approved Prelude checkpoint, convert it
   to the required Megatron layout, and record parity against its HF form.
2. **Freeze the blend.** Reuse Jouni's 152-prefix blend for the reproduction
   baseline. Record every weight, file size, checksum, tokenizer revision, and
   `.stats.txt` summary in the run manifest.
3. **Smoke-test 16k.** Run 20 steps, save, resume for 20 steps, convert to HF,
   and evaluate short-context parity.
4. **Run the curriculum.** Use 16k -> 64k -> 128k rather than jumping directly
   from 4k. Match tokens per iteration across phases when memory permits.
5. **Checkpoint frequently.** Keep the phase start, pre-cooldown, and final
   checkpoints. A failed final evaluation must not require repeating the whole
   phase.
6. **Evaluate every phase.** Run base capability and multilingual suites plus
   RULER/needle/retrieval tests at 4k, 16k, 32k, 64k, and the phase target.
7. **Convert and freeze.** Promote one HF and one Megatron checkpoint together
   with conversion parity results.
8. **Decide 256k explicitly.** A proposed 256k phase can use a 10,000,000 RoPE
   base and the same curriculum principles, but it is not yet a confirmed
   production recipe. Do not spend the allocation until the 128k checkpoint
   passes the common gate and 256k is a product requirement.

## Data-mixture checks

The current blend targets about 80% English/code/math/science and 20%
multilingual European data. Before reproducing it:

- report actual sampled tokens, not configured weights;
- ensure the long-token share is not dominated by a few English/PDF/code
  sources;
- cap near-duplicate books, boilerplate, and generated MultiSynt templates;
- inspect OCR/PDF quality by language;
- compare a no-synthetic and no-code ablation on a smaller checkpoint; and
- preserve source identity so later analyses can remove a problematic prefix.

## Exit gate

Stage 1 passes only if:

- loss and throughput are stable and all intended token budgets were consumed;
- checkpoint save/resume and HF conversion pass;
- short-context and multilingual capability stay within an agreed regression
  budget relative to the start checkpoint;
- target-length RULER/retrieval results improve materially over the start;
- the exact dataset, container, code, jobs, and checkpoints are under shared
  project storage; and
- one of the retention strategies below passes a pilot before full SFT begins.

## Mandatory retention experiment

Before Stage 2, compare at least two approaches on a small checkpoint:

1. mixed SFT with 10–20% of optimizer tokens in 64k/128k long instruction or
   replay sequences; or
2. short SFT followed by a small low-LR long-context recovery phase.

The current common framework does not yet support a clean mixed CLM +
assistant-only SFT objective. The LUMI English–Finnish asset is a concrete
retention candidate, but it is not yet known how much of it is actually 64k or
128k, whether its binary trains all tokens, or which sources and licenses it
contains. It also covers only two declared languages. This remains a P0 blocker
for a flagship 128k multilingual chat model even though the context-extension
run itself is ready.

## Missing

- A shared immutable copy of Jouni's blend and selected checkpoints.
- A reproduced lineage from the final approved Prelude checkpoint.
- A multilingual long-context evaluation suite with protected data.
- A validated, licensed, assistant-masked freeze of the English–Finnish long-SFT
  candidate plus broader European 64k/128k instruction coverage.
- A signed 128k versus 256k release decision.
