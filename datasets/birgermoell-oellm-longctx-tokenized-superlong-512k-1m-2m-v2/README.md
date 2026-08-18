---
name: "birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2"
slug: "birgermoell-oellm-longctx-tokenized-superlong-512k-1m-2m-v2"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "published"
status: "Published / available"
language_keys: ["en","sv","de","es","fr","pl"]
languages: "en,sv,de,fr,es,pl"
purpose: "Megatron-ready 512k/1M/2M continuation data for superlong context extension"
public_location: "https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2"
lumi_location: ""
source_sheet_row: 84
---

# birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2

> **State:** Published / available  
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** en,sv,de,fr,es,pl

## What it is for

This is a public, ungated Megatron-LM tokenized artifact for continuation
training from a long-context checkpoint toward 512k, 1M, and 2M context
windows. It combines natural long documents, structured technical and code
sources, mathematics/science sources, and synthetic full-span dependency tasks.
It is training data, not an evaluation benchmark or instruction-SFT dataset.

### Artifact summary

| Item | Value |
| --- | ---: |
| Megatron `.bin`/`.idx` prefixes | 48 |
| Packed examples | 1,248 |
| Estimated source-side tokens | about 1.197B |
| Tokenized payload | 5,838,868,212 bytes (5.84 GB) |
| Context tiers | 512k, 1M, 2M |
| Tokenizer vocabulary | 262,144 |

The v2 extension contributes 650 of the examples and approximately 628.6M of
the estimated source-side tokens. Its additional data includes RFC/specification
continuations, Gutenberg books, arXiv, repository-packed code, Wiki/reference,
Pes2O science, open-web mathematics, Algebraic Stack/LaTeX, StarCoder file
context, and synthetic long-dependency tasks. The synthetic tasks cover
multi-hop lookup, section following, distributed aggregation, and retrieval
with evidence placed across the full context span.

### Published family mix

The checked-in `mix/data_path.args` and `mix/data_mix.json` use explicit family
weights rather than raw byte-proportional sampling:

| Family | Target share |
| --- | ---: |
| RFCs and specifications | 18% |
| Books | 14% |
| arXiv | 10% |
| Repository-packed code | 10% |
| Synthetic dependency extension | 10% |
| Synthetic recall v1 | 8% |
| StarCoder file context | 6% |
| Wiki/reference | 5% |
| Science/Pes2O | 5% |
| Open-web mathematics | 5% |
| Algebraic Stack/math LaTeX | 5% |
| Technical documentation references | 4% |

## Where to find it

- **Public artifact:** [Hugging Face dataset](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2>)
- **Pinned revision verified 2026-08-18:** `b12e0501918080ae960f825e55f784c8bf2c2eee`
- **LUMI or other artifact:** Not recorded
- **Artifact format:** `openeuro-longctx-megatron-v1`
- **Tokenizer:** OpenEuroLLM 256k Hugging Face tokenizer, vocabulary size 262,144; the build manifest does not pin its revision
- **Megatron build commit:** `d3ee058092f66045286f0c0bc8d6ce4f21d5302c`
- **Upstream / parent:** Natural/structured long sources plus synthetic hard dependencies
- **Evidence:** [evidence](<https://huggingface.co/datasets/birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2>)
- **Seed inventory:** [Data tab, row 84](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A84:Q84>)

Important files in the public artifact:

- `mix/data_path.args`, `mix/data_mix.json`, and `mix/data_mix.txt`;
- `manifests/mix_weight_summary.json` and `manifests/checksums.sha256`;
- natural-pack and synthetic train manifests;
- 512k/1M/2M GPU and curriculum recipes; and
- the scripts used to collect, pack, and extend the sources.

## How to use it

1. Start from an already validated long-context checkpoint; use this for
   continued pretraining, not assistant-only SFT.
2. Download the artifact and verify `manifests/checksums.sha256`. Record the
   pinned dataset revision above and separately pin the exact 256k tokenizer.
3. Use the supplied artifact helper to make the Megatron paths local:

   ```bash
   python -m longctx.cli artifacts download \
     --repo-id birgermoell/oellm-longctx-tokenized-superlong-512k-1m-2m-v2 \
     --output-dir ./data/oellm-superlong-512k-1m-2m-v2
   export SUPERLONG_DATA_PATH="$(cat ./data/oellm-superlong-512k-1m-2m-v2/mix/data_path.args)"
   ```

4. Pass `$SUPERLONG_DATA_PATH` to Megatron-LM as `--data-path`. Keep the
   published family weights unless the run manifest records an intentional
   ablation.
5. Train as a length curriculum—512k, then 1M, then 2M—rather than jumping from
   a short checkpoint directly to 2M. Pin each phase's RoPE settings, global
   tokens, learning-rate schedule, topology, and starting checkpoint.
6. Evaluate retrieval and full-span dependency behavior at every tier while
   checking short-context and multilingual retention.

The published artifact is already tokenized. Do not reuse it with a different
tokenizer, vocabulary, or Megatron indexed-dataset interpretation without
rebuilding from the source manifests.

## State and ownership

- **Owner / lead:** Birger / long-context team
- **Source type:** Public Hugging Face Megatron artifact
- **Priority:** P2 — superlong research and extension runs
- **License / access:** Public and ungated; license is `other`, with source-specific upstream restrictions
- **Last verified:** 2026-08-18 through the Hugging Face page, API, and public manifests
- **Confidence:** High

## Notes and next action

Use this as the explicit dataset option when a training plan extends beyond
128k/256k. Keep it separate from instruction SFT and from protected long-context
evaluation data.
