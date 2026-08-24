# Dataset ingestion

This workflow adapts the [OpenEuroLLM training-data catalogue ingestion process](https://github.com/OpenEuroLLM/training-data-catalogue/blob/main/DATASET-INGESTION.md) to instruction, preference, reasoning, RLVR, tool-use, long-context, specialization, filtering, and evaluation artifacts.

## 1. Nominate and scope

Open a dataset-nomination issue before adding a new source. Record:

- intended stage and capability;
- source owner, upstream URL, revision, configuration, and split;
- European-language coverage;
- license/access and personal-data concerns;
- expected format, size, and storage location;
- contamination relationship to protected evaluations; and
- proposed curator and acceptance gate.

Choose a stable slug and version. Reuse a pinned upstream semantic version when possible; otherwise begin at `0.0.0`.

## 2. Acquire without losing provenance

- Download or copy the exact selected revision.
- Preserve upstream manifests, checksums, dataset cards, licenses, and transformation scripts.
- Record retrieval time and the identity of the materialized configuration and split.
- Never commit credentials, signed URLs, personal tokens, or unreviewed sensitive examples.
- Treat personal LUMI scratch and flash locations as working evidence, not durable release storage.

The official training catalogue currently records shared roots at `/appl/local/openeurollm/training/catalogue/` on LUMI and `/leonardo_work/OELLM_Catalog/training/` on Leonardo. A durable post-training release root has not yet been agreed in this repository; continue recording exact inspected locations until project governance selects one.

## 3. Normalize and manifest

Use UTF-8 JSON Lines compressed with Zstandard for a canonical row-based export when feasible. Post-training artifacts may additionally require Parquet, conversation JSONL, Megatron `.bin`/`.idx`, preference pairs, verifier specifications, or packed length tiers.

Every derived artifact should have a manifest containing:

- source revision, configuration, and split;
- transformation code commit and command;
- schema and field semantics;
- conversation template and loss-mask policy where relevant;
- tokenizer name, revision, vocabulary, and special-token mapping for tokenized data;
- row/document counts, byte size, and checksums;
- language-identification method and per-language counts; and
- retained, filtered, and rejected counts with reason codes.

Compute the normalized catalogue token total with the common official catalogue tokenizer, currently Gemma 3. If the artifact is also counted with its training tokenizer, label that as a separate training statistic and pin both revisions.

Do not substitute a tokenized artifact across tokenizers or model chat templates without rebuilding it.

## 4. Run post-training quality gates

The curator records results for the gates that apply:

1. **License and access:** component-level terms, redistribution, commercial use, attribution, and access restrictions.
2. **Privacy and safety:** PII, secrets, harmful content, minors, medical/legal sensitivity, and source-specific redactions.
3. **Integrity:** parse success, schema conformance, missing fields, encoding, truncation, duplicates, and checksums.
4. **Language quality:** ISO 639-3/script identification, language balance, code-switching, translationese, and native-source depth.
5. **Task quality:** instruction-response coherence, preference validity, reasoning correctness, tool schema/execution validity, or verifier determinism.
6. **Contamination:** exact and fuzzy overlap against protected evaluations, model-generated benchmark leakage, and source-family duplication.
7. **Capability balance:** stage-specific mixture contribution and regression risk for English, multilingual, safety, short-context, and base-model capabilities.

For synthetic or model-generated data, also record generator model, prompt/template version, decoding settings, judge/filter models, and retained acceptance rate.

## 5. Protect evaluation artifacts

Evaluation-only material follows a separate path:

- set `status_key` to `eval-only` and include `evaluation-holdouts` in `training_types`;
- publish stable IDs and hashes to the decontamination process without exposing restricted answers unnecessarily;
- exclude prompts, answers, translations, paraphrases, retrieval corpora, and synthetic derivatives from every training and generation source;
- restrict access when benchmark terms require it; and
- document the evaluation owner, freeze date, prompt/scoring version, and allowed reporting granularity.

## 6. Write the versioned entry

Copy `etc/skeleton.md` to `<dataset>/<version>/README.md`. Complete every section, using `null` for unmeasured normalized statistics rather than zero. Preserve evidence links and the spreadsheet row where applicable.

Set the catalogue lifecycle independently of operational readiness:

- `D` while important evidence or scope is incomplete;
- `P` when the entry is reviewable and its claims are supported; or
- `E` when retained only for provenance.

## 7. Publish and verify

Run:

```bash
python3 scripts/build_indexes.py
python3 scripts/build_indexes.py --check
```

The check validates version paths, required fields, lifecycle values, language identifiers, normalized-statistic types, canonical section anchors, generated indexes, and local Markdown links.

Open a pull request with the completed checklist. A production training manifest should link the exact catalogue version, not only the dataset family or rolling upstream page.
