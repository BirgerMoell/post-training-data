---
name: "Jouni Luoma LUMI long-context blend and runs"
slug: "lumi-long-context-sample"
training_types: ["long-context-extension","continued-pretraining"]
status_key: "used-in-completed-run"
status: "Used in completed 16k/64k/128k runs"
language_keys: ["multilingual","en","code"]
languages: "European multilingual + en/code/math/science"
purpose: "Megatron-ready length-biased blend and validated context-extension lineage"
public_location: ""
lumi_location: "/flash/project_465002530/preprocessed/oellm-v1-256k/long-ctx-sample"
source_sheet_row: 80
---

# Jouni Luoma LUMI long-context blend and runs

> **State:** Used in completed 16k/64k/128k runs
> **Training use:** Long-context extension, Continued pretraining  
> **Languages:** European multilingual + English, code, mathematics, and science

## What it is for

This is the strongest confirmed long-context asset currently visible in the
project. It combines a Megatron-ready data blend with the scripts, caches,
logs, checkpoints, and converted Hugging Face artifacts used for a progressive
16k -> 64k -> 128k extension of the Prelude 9B lineage.

The data directory is approximately 205 GB and contains 152 source prefixes as
paired `.bin`/`.idx` files plus per-source `.stats.txt` files. The sampler
targeted roughly 2 million documents and 30B tokens.

### Sampling policy

| Document tier | Length | Target document share | Expected token share |
| --- | --- | ---: | ---: |
| Short | below 16k tokens | 60% | about 2–5% |
| Medium | 16k–64k tokens | 25% | about 30–35% |
| Long | at least 64k tokens | 15% | about 60–65% |

Documents were sampled length-proportionally within each tier. The training
blend is weighted at approximately 80% English/code/math/science and 20%
multilingual European data.

Source families visible in the artifact include DCLM, FinePDFs,
FinePDFs-Edu, HPLT 3, Wikipedia, ArXiv, FineMath, MegaMath, peS2o, StarCoder,
Nemotron quality bands, MultiSynt 9B/72B generations, and OPUS-MT.

## Where to find it

- **Public or upstream:** Not recorded
- **LUMI or other artifact:** `/flash/project_465002530/preprocessed/oellm-v1-256k/long-ctx-sample`
- **Upstream / parent:** Long-context pipeline
- **Evidence:** [evidence](<https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/w58oa46znjdsureg74gsms489h>)
- **Sampling scripts:** `/scratch/project_465002530/users/luomajou/idx-analysis`
- **Training workspace:** `/flash/project_465002530/users/luomajou/oellm-long-ctx`
- **Outputs:** `/scratch/project_465002530/users/luomajou/oellm-long-ctx`
- **Tokenizer:** `/scratch/project_465002530/users/pyysalos/tokenizers/openeurollm/tokenizer-256k`
- **Seed inventory:** [Data tab, row 80](<https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit#gid=1339797209&range=A80:Q80>)

## How to use it

Use this as continued-pretraining data for context extension, not as instruction
SFT. The current validated lineage uses packed pretraining with document-isolated
attention and the OpenEuroLLM 256k tokenizer.

| Phase | Sequence | RoPE base | Tokens / iterations | Completed artifact |
| --- | ---: | ---: | --- | --- |
| 1 | 16,384 | 1,000,000 | about 5B / 597 iterations | `output-prelude-iter0830400-16k-packed-eodfix/checkpoints/iter_0000597` |
| 2 | 65,536 | 2,500,000 | 29.36B / 3,500 iterations | `output-prelude-iter0830400-64k-packed-eodfix/checkpoints/iter_0003500` |
| 3 | 131,072 | 5,000,000 | 16.78B / 2,000 iterations | `output-prelude-iter0830400-128k-packed/checkpoints/iter_0002000` |

The 64k and 128k phases used TP=2, PP=2, CP=8 on 64 LUMI nodes,
micro-batch size 1, approximately 8.4M tokens per iteration, peak learning rate
`1e-6`, and a 500-iteration WSD cooldown. The 128k Hugging Face conversion is
at `output-prelude-iter0830400-128k-packed/hf-checkpoints/iter_2000`.

Before reusing the recipe:

1. Pin the starting checkpoint and tokenizer.
2. Recreate or freeze the 152-prefix `DATA_PATH` in a run manifest.
3. Check every `.bin` has a matching `.idx` and readable statistics.
4. Run a short end-to-end smoke test including checkpoint conversion.
5. Evaluate the starting checkpoint and every phase at native and target lengths.
6. Do not proceed to short-sequence SFT until a long-context retention mix and
   post-SFT evaluation gate are defined.

## State and ownership

- **Owner / lead:** Jouni / long-context team
- **Source type:** LUMI artifact
- **Priority:** P1
- **License / access:** LUMI access
- **Last verified:** 2026-08-18 by direct LUMI inspection
- **Confidence:** High

## Notes and next action

The data and 16k/64k/128k recipes are concrete and have produced completed
checkpoints. Remaining production work:

- move the chosen data/checkpoints from personal working paths to a shared,
  retained project root;
- record hashes, exact source weights, code commits, container digest, jobs,
  and evaluation results in one manifest;
- reproduce the 128k result from the final selected Prelude checkpoint;
- complete and evaluate a 256k phase if 256k is a release requirement;
- add multilingual long-context evaluation; and
- protect the capability during later SFT. Jouni reported that a 32k SFT after
  128k extension destroyed Poro-long's long-context capability
  ([Mattermost, 2026-08-17](https://mattermost.ufal.mff.cuni.cz/openeurollm/pl/fgm6gwbnybg6tpyesjeiciu5rw)).
