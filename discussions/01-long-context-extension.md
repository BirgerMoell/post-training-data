# Discussion 1 — long-context extension data

## Proposed decision

Qualify **128K as the release target**, treat 256K as a separately gated
checkpoint, and keep 512K–2M as research. Reproduce the existing Jouni Luoma
16K → 64K → 128K lineage before changing the data blend. In parallel, build a
new multilingual long-instruction product from native European documents; the
current English–Finnish long SFT is not enough for a 36-language claim.

## Use in the first freeze

- The catalogued 205 GB Jouni long-context blend is the reproduction control.
  Freeze all 152 prefixes, weights, tokenizer revision, document-boundary
  policy, checksums, and token statistics before reuse.
- `birgermoell/oellm-longctx-tokenized-streamed-all-v2` is the portable
  multilingual transport candidate after its component provenance and
  tokenizer namespace are pinned.
- The natural 128K/256K and structured 128K/256K artifacts are two distinct
  ablation arms. Do not merge them until document-type and duplicate analysis
  shows the contribution of each.
- Per-language Wikipedia and approved native public documents may provide
  fluency replay and natural long spans, especially for languages dominated by
  translated instruction data.

The published OpenEuroLLM 128K base checkpoints and
[`openeurollm/oellm-9b-256k-sft`](https://huggingface.co/openeurollm/oellm-9b-256k-sft)
provide valuable empirical controls. The latter shows that 4K SFT can retain
single-needle retrieval, but its card also says broader long-document
comprehension and reasoning are unestablished. That distinction should define
the next data work.

## Pilot or hold

| Source | Decision | Why / gate |
| --- | --- | --- |
| EUR-Lex and MultiEURLEX; Europarl; national parliament, court, government, public-broadcast, and open textbook sources | Pilot | Best route to native long documents; require per-jurisdiction terms, PII handling, versioned IDs, and document-family deduplication |
| FineWeb-2, HPLT v2, CulturaX | Pilot for continued pretraining | Useful breadth, but admit only quality-filtered, language-verified, license-reviewed, decontaminated slices; measure overlap among the three |
| The Stack v2 | Pilot for a code branch | Require source-license filtering, secret scanning, repository deduplication, and a separate code-retention gate |
| LongAlign-10k and LongAlpaca-12k | Pilot | English baselines only; accept only if they add value beyond project-native synthetic tasks |
| NVIDIA ChatQA2 Long SFT | Hold for a redistributable flagship mix | The dataset card is English-only and non-commercial, with OpenAI-generated components; it is useful as a recipe reference, not an automatic production input |
| Superlong 512K/1M/2M v2 | Hold from the release path | Promote only after 128K and 256K quality, compute, memory, and serving gates pass |

## Synthetic product to build

Create `oellm-eu-longctx-instruct-v1` from native documents in every target
language, keeping the source document and generated supervision under separate
licenses. Each document family should produce:

- answerable and deliberately unanswerable grounded QA;
- evidence retrieval at beginning, middle, and end positions;
- multi-document comparison, contradiction, and timeline synthesis;
- concise and structured extraction with exact source spans;
- long-form summarization with section coverage and factuality checks;
- revision tracking across two dated versions; and
- long-context prompt-injection and conflicting-instruction examples, reviewed
  jointly with the safety discussion.

Generate questions from source-grounded schemas, not from EUROPA prompts.
Require answer-span or structured verifier checks where possible, bilingual or
native review on a stratified sample, and fresh protected source documents for
evaluation. Record target depth, total length, relevant-token density, number
of documents, and distractor language for every item.

## First experiment matrix

1. Reproduce the frozen Jouni blend and curriculum.
2. Compare natural-only, structured-only, and a token-matched natural +
   structured blend at 64K and 128K.
3. Add the same short multilingual replay to every arm.
4. After context extension, compare short-only SFT, mixed short/long SFT, and a
   short-SFT-then-long-recovery phase.
5. Promote 256K only if the selected 128K recipe is stable and the serving
   budget is accepted.

## Acceptance gates

- RULER/needle retrieval is at least 95% through the advertised length, while
  being treated as a precondition rather than the headline result.
- LongBench v2, MRCR, and a protected multilingual synthesis set improve by
  length, position, task type, and language.
- EUROPA grounded QA, abstention, summarization, structured output, and
  revision tracking do not regress by more than the signed tolerance, and the
  minimum-language score is preserved.
- Short-context instruction/reasoning loss is no more than two percentage
  points in any priority language.
- Training, conversion, resume, and production-like serving succeed with
  recorded memory, throughput, time-to-first-token, and OOM rates.

## Questions for the thread

1. Is 128K the flagship target, or is 256K a hard product requirement?
2. Which native document families have an owner and a clear training-use
   decision today?
3. Which long-SFT strategy should be the control: mixed length, interleaved
   recovery, or a final recovery stage?
4. Who owns the protected multilingual long-context suite?
