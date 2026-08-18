# OpenEuroLLM Post-Training Data

A human-first catalogue of data sources and artifacts used or considered for OpenEuroLLM post-training.

This repository answers five practical questions:

1. What data do we have?
2. Which part of training can it be used for?
3. Which languages does it cover?
4. Where can it be found?
5. What is its current state and next action?

The initial catalogue was seeded from the OpenEuroLLM post-training data register on 2026-08-18. Each dataset or product has its own page and can be updated through an ordinary pull request.

## Browse the catalogue

- [By training type](training-types/README.md)
- [By language](languages/README.md)
- [By state](status/README.md)
- [All datasets and products](CATALOGUE.md)
- [Storage locations](storage/README.md)

## How this repository is organised

```text
datasets/<dataset>/README.md        One page per data source or artifact
training-types/<type>/README.md     SFT, preference, RLVR, long context, etc.
languages/<language>/README.md      Language-oriented views
status/<state>/README.md            Used, available, candidate, planned, etc.
storage/README.md                   Shared storage roots and conventions
```

The indexes are generated from the small metadata block at the top of each dataset page:

```bash
python3 scripts/build_indexes.py
python3 scripts/build_indexes.py --check
```

## Reading a dataset page

Each page contains:

- **What it is for** — the training stage and capability.
- **Where to find it** — upstream/public location and known LUMI artifact.
- **How to use it** — the expected training shape and basic checks.
- **State** — availability, ownership, access/licensing, and confidence.
- **Next action** — what is still missing before production use.

A path means “known to have existed at the verification date,” not a promise that it is still present. Verify LUMI paths and pin public dataset revisions before production runs.

## Scope

The catalogue covers instruction SFT, reasoning SFT, preference optimization, RLVR/GRPO, tools and agents, long-context extension, continued pretraining used in post-training sequences, language repair, domain specialization, safety data, filtering support, and evaluation holdouts.

Evaluation-only entries are deliberately included so that they are visible and kept out of training.

## Related repositories

- [OpenEuroLLM/post-training](https://github.com/OpenEuroLLM/post-training)
- [OpenEuroLLM/training-data-collection](https://github.com/OpenEuroLLM/training-data-collection)
- [OpenEuroLLM/training-data-catalogue](https://github.com/OpenEuroLLM/training-data-catalogue)
- [OpenEuroLLM/post-training-decontamination](https://github.com/OpenEuroLLM/post-training-decontamination)

See [CONTRIBUTING.md](CONTRIBUTING.md) to add or update an entry and [MIRRORING.md](MIRRORING.md) for the future OpenEuroLLM mirror.

