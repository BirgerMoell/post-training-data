# Post-training data mixes

This directory contains reusable data-selection manifests. SFT/DPO manifests
are consumed by
[`OpenEuroLLM/post-training`](https://github.com/OpenEuroLLM/post-training);
RLVR manifests are the reviewed data-selection input for
[`BirgerMoell/oellm-rlvr`](https://github.com/BirgerMoell/oellm-rlvr). They
select data only; model, optimizer, RoPE, sequence length, SLURM, container,
checkpoint, rollout, and reward settings remain in the ordinary run YAML.

## Use with the post-training framework

Reference a mix from a normal run configuration:

```yaml
method: sft
backend: trl

data:
  mix_manifest: ../post-training-data/mixes/pilots/sft-instruct-smoke-v1.yaml
  location: null  # or lumi / leonardo when the manifest records that mirror
```

Each entry normally selects a named release from a committed collection
`metadata.yaml`:

```yaml
datasets:
  - name: dolci_translated_sv
    collection: ../../collection/pilot/openeurollm-dolci-instruct-sft-translated/metadata.yaml
    release: candidate
    subset: sv
    weight: 0.001
```

The framework resolves that release into its existing `data.datasets`
objects. Direct `path` entries remain supported for compatibility, but a
collection reference is the preferred reviewed form. The frozen run config
remains self-contained and the run directory receives `data-mix.lock.yaml`
with the mix plus collection metadata digests, check states, immutable
revisions, and resolved paths.

For LlamaFactory, the same reference generates the existing
`dataset_info.json` and sets `llamafactory.dataset_dir` and
`llamafactory.dataset`. Dataset-specific LlamaFactory field mappings are kept
under each entry's `llamafactory` key.

## Weight semantics

`sampling.mode: multiplier` deliberately matches the current framework:

- `weight: 1.0` retains the complete split after transformation and filtering;
- a value below one undersamples it; and
- a value above one oversamples it.

Weights are not normalized mixture percentages. The realized mixture depends
on the number of rows that survive each dataset's transform and method-specific
filter. Run `scripts/data.py inspect` and `scripts/data.py token-stats` before a
large job and record the realized sample/token composition.

The pilot manifests are smoke-test selections, not approved flagship recipes.
For online RLVR, weights describe submitted prompts before rollout filtering.
Record the realized optimizer composition after verifier execution and
zero-variance filtering; it can differ materially from the static input mix.

## Validation

```bash
python3 scripts/validate_mixes.py
python3 scripts/validate_mixes.py --check
```

The mix schema is documented in [schema.json](schema.json), and release
metadata in [collection/schema.json](../collection/schema.json). A release
must pin an immutable revision for every Hugging Face artifact, link its
versioned catalogue entry when one exists, and must never select an
evaluation-only entry. An `approved` mix accepts only `approved` releases whose
license, PII, safety, integrity, language, task-quality, and contamination
checks are `complete` or explicitly `inapplicable` with a reason.
