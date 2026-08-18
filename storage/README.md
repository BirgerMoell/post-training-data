# Storage locations

Dataset pages record concrete locations. This page explains the main location families currently visible in the catalogue.

## Public sources

Hugging Face is the most common public source. Production recipes should pin a dataset commit or immutable revision, along with the exact configuration and split.

GitHub repositories, EU portals, national portals, Wikimedia sources, and benchmark sites also appear. Record a version, release, commit, or retrieval date whenever possible.

## LUMI shared post-training data

A large shared collection is recorded under:

```text
/scratch/project_462000963/datasets/posttraining_data
```

It contains SFT/DPO-formatted data and other staged candidates. Treat folder names as leads until the exact files, source revision, license, and row counts have been confirmed. The [shared-catalogue page](../datasets/lumi-shared-post-training-catalogue/README.md) links the individually inspected assets and their readiness decisions.

Notable paths directly verified on 2026-08-18 include:

```text
/scratch/project_462000963/datasets/posttraining_data/Megatron_format/long-context-eng-fin
/scratch/project_462000963/datasets/posttraining_data/Megatron_format/poro2-instruction-data
/scratch/project_462000963/datasets/posttraining_data/Megatron_format/am-deepseek-r1-think
/scratch/project_462000963/datasets/posttraining_data/OpenR1-Math-220k
/scratch/project_462000963/datasets/posttraining_data/glaive-code-assistant-v3
/scratch/project_462000963/datasets/posttraining_data/booksum
/scratch/project_462000963/datasets/posttraining_data/FLORES-200
/scratch/project_462000963/datasets/posttraining_data/Tatoeba/eng-fin
```

The three `Megatron_format` samples are pre-rendered one-field `text` data.
Their `.bin`/`.idx` availability does not prove an assistant-only loss mask or
the intended tokenizer, so use the linked dataset pages before selecting them.

## OpenEuroLLM strategic-access project

Current project and derived artifacts appear under roots such as:

```text
/scratch/project_465002530/training/collection
/scratch/project_465002530/datasets
/scratch/project_465002530/users/<user>/posttrain-data
```

Personal paths can document completed experiments, but a production artifact should be copied or rebuilt in an agreed shared location.

## Flash storage

Long-context and other I/O-heavy artifacts may appear under:

```text
/flash/project_465002530
```

Flash is a working location, not the catalogue itself. Keep a reproducible source or another retained copy.

### Verified long-context assets

The following paths were read directly on LUMI on 2026-08-18:

```text
/flash/project_465002530/preprocessed/oellm-v1-256k/long-ctx-sample
/flash/project_465002530/users/luomajou/oellm-long-ctx
/scratch/project_465002530/users/luomajou/oellm-long-ctx
```

The first path is a 205 GB, 152-source Megatron `.bin`/`.idx` blend targeting
roughly 30B tokens. The working directories contain the sampling scripts,
16k/64k/128k packed-pretraining recipes, logs, caches, Megatron checkpoints,
and converted Hugging Face checkpoints. These are usable project artifacts but
remain owner working paths. Before a flagship run, copy or rebuild the selected
data and final checkpoints under a shared immutable release root and record a
manifest with sizes and checksums.

## What a useful location record contains

For a production-ready entry, record:

- exact path or public URL;
- dataset revision, configuration, and split;
- file format and expected training columns;
- row/document and token counts;
- responsible owner;
- last verification date;
- the build script or training configuration that used it.

The repository stores locations and instructions, not the dataset files.
