# Mirroring to OpenEuroLLM

This repository starts in a private personal GitHub account so the structure and initial inventory can be refined quickly.

It is ready to mirror into the OpenEuroLLM organization when:

- owners of the main training areas have reviewed their entries;
- sensitive internal paths and notes have been reviewed;
- evaluation-only sources are clearly marked;
- public links and important LUMI locations have been checked;
- licensing/access wording distinguishes known facts from pending review;
- the generated indexes pass `python3 scripts/build_indexes.py --check`;
- repository ownership and update responsibility are agreed.

The preferred organization repository name is `OpenEuroLLM/post-training-data`.

The Git history can be preserved by adding the organization repository as a second remote and pushing the default branch. The private repository can then remain an upstream working copy or be archived, depending on project governance.

