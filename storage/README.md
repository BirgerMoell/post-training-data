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

It contains SFT/DPO-formatted data and other staged candidates. Treat folder names as leads until the exact files, source revision, license, and row counts have been confirmed.

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

