---
name: "OpenR1-Math-220k staged on LUMI"
slug: "lumi-openr1-math-220k"
training_types: ["reasoning-sft","preference-optimization","reinforcement-learning"]
status_key: "staged"
status: "Staged on LUMI — local revision not pinned"
language_keys: ["en"]
languages: "English"
purpose: "Verified-trace math SFT, preference-pair construction, and RLVR prompt seed"
public_location: "https://huggingface.co/datasets/open-r1/OpenR1-Math-220k"
lumi_location: "/scratch/project_462000963/datasets/posttraining_data/OpenR1-Math-220k"
source_sheet_row: null
---

# OpenR1-Math-220k staged on LUMI

> **State:** Staged on LUMI — local revision not pinned
> **Training use:** Reasoning SFT, preference optimization, and RLVR prompts
> **Languages:** English

## What it is for

OpenR1-Math-220k provides math problems with multiple DeepSeek-R1-generated
reasoning traces and correctness metadata. The public card describes 220k
problems, a recommended `default` subset of about 94k problems, and verification
with Math Verify for most samples. It is suitable for reasoning SFT after trace
selection, pair construction from trace scores, or prompts for verifier-based
training.

## Where to find it

- **Public source:** [open-r1/OpenR1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k)
- **Current public revision observed 2026-08-18:** `e4e141ec9dea9f8326f4d347be56105859b2bd68`
- **LUMI directory:** `/scratch/project_462000963/datasets/posttraining_data/OpenR1-Math-220k`
- **Local default JSONL:** `default-train.jsonl` — 5,116,576,246 bytes
- **Local sample:** `default-train-sample-10.jsonl` — 602,414 bytes
- **Observed columns:** `answer`, correctness fields, finish reasons,
  generations, IDs, messages, problem/source types, solution, and source
- **Evidence:** Direct read-only LUMI inspection and public dataset card on 2026-08-18

## How to use it

1. Re-materialize the chosen `default` revision or prove the local JSONL's
   lineage with a checksum and build record. The current public revision is not
   necessarily the revision that produced the local file.
2. Keep only complete, independently verified traces and one held-out dev set
   stratified by source and problem type.
3. For SFT, select or sample correct traces rather than multiplying nearly
   identical problems unintentionally. Decide whether think tokens are visible,
   masked, or removed.
4. For DPO, construct chosen/rejected pairs only when the score difference is
   meaningful and the final answer/verifier agrees.
5. For RLVR, train on prompts only and keep the reference answer plus verifier
   outside the model input. Pin the Math Verify version and sandbox limits.
6. Decontaminate against AIME, GSM, MATH, exams, and every protected math set.

## State and ownership

- **Owner / lead:** Open R1 upstream; OpenEuroLLM stage owner unassigned
- **Source type:** Public dataset with local JSONL materialization
- **Priority:** P1
- **License / access:** Apache-2.0 upstream; verify local derivation
- **Last verified:** 2026-08-18
- **Confidence:** High for upstream and local files; medium for their lineage

## Notes and next action

Pin the exact local derivation, then compare this source with Dolci Think and
the LUMI AM mixture on matched, decontaminated math tokens.
