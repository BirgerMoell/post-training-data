# Post-training data collection

This is the post-training counterpart of the pre-training
[`training-data-collection`](https://github.com/OpenEuroLLM/training-data-collection).
The same separation is kept deliberately:

```text
collection/<cycle>/<dataset>/
├── metadata.yaml       # committed: source, processing, checks, releases
├── source/             # data: pinned upstream checkout or symlinks
├── pii/                # data: document/message-level PII overlay
├── contamination/      # data: protected-evaluation overlap overlay
├── quality/            # data: language/task/safety annotations
├── release_raw/        # data: normalized output before final sharding
├── release/            # data: immutable, model-independent training rows
├── tokenized/          # data: tokenizer/chat-template-specific derivatives
└── counts/             # data: row/token/filter summaries and checksums
```

Only metadata, schemas, recipes, and small count manifests belong in Git.
Dataset bytes stay on Hugging Face and shared cluster storage. A deployment can
materialize the same relative tree below, for example,
`/scratch/project_465002530/training/collection/post-training/<cycle>/<dataset>/`.
The 2026 Q3 DPO and RLVR candidates use that shared root; personal scratch or
flash is experiment evidence, not the canonical release location.

## Contract

- `source` preserves an immutable upstream revision and provenance.
- overlays refer to stable row/message IDs and do not rewrite the source.
- `release` is produced from source plus declared overlays and is the only
  layer selected by a training mix.
- the canonical release remains unrendered structured data: `messages` for
  SFT, `prompt/chosen/rejected` for DPO, and prompt/verifier records for RLVR.
- `tokenized` is a derivative, keyed by tokenizer revision, chat template,
  loss-mask policy, sequence length, and packing code commit. It is never
  silently reused across models or templates.
- every applicability decision is explicit. A check is `complete`, `pending`,
  or `inapplicable`; `inapplicable` requires a reason.
- `training_eligible: false` is a hard stop for protected evaluation data or
  any source that must remain visible without becoming trainable.

The `dataset` object under a named release is the small interface consumed by
the current `OpenEuroLLM/post-training` configuration for SFT/DPO and by
`BirgerMoell/oellm-rlvr` for RLVR. A mix may therefore use the public Hugging
Face release on a workstation and select a local mirror via `data.location:
lumi` or `leonardo` without changing the recipe.

Pilot metadata currently points at pinned upstream candidate releases so the
integration can be exercised. Its pending checks are intentional: those
releases must not be promoted into an `approved` mix until all required gates
have been completed or explicitly judged inapplicable.

See [schema.json](schema.json) and [the template](etc/metadata.template.yaml).
