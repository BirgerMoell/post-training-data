# Inventory sources

The initial catalogue was assembled from:

- [OpenEuroLLM post-training data register](https://docs.google.com/spreadsheets/d/1hFFDRk_JdjbQCCv3zsemKulSnMyk_fBQIfKPSzSaP9M/edit?gid=1339797209#gid=1339797209), Data tab, read on 2026-08-18.
- [OpenEuroLLM/post-training](https://github.com/OpenEuroLLM/post-training).
- [OpenEuroLLM/training-data-collection](https://github.com/OpenEuroLLM/training-data-collection).
- [OpenEuroLLM/training-data-catalogue](https://github.com/OpenEuroLLM/training-data-catalogue).
- [OpenEuroLLM datasets on Hugging Face](https://huggingface.co/openeurollm/datasets).
- Live repository inspection on 2026-08-18 at `post-training@f330661`,
  `instruction-tuning-scripts@c14ecfe`,
  `Megatron-Bridge-LUMI@1ebec5c`, and
  `post-training-decontamination@1029de2`.
- Direct read-only inspection of OpenEuroLLM LUMI paths on 2026-08-18,
  including Jouni Luoma's long-context sample, training recipes, caches, and
  completed 16k/64k/128k checkpoints, plus the shared post-training tree at
  `/scratch/project_462000963/datasets/posttraining_data`. The latter inspection
  verified concrete long-SFT, Poro2, OpenR1, AM reasoning, Glaive code, BookSum,
  FLORES, and Tatoeba files; individual pages state what remains unverified.
- OpenEuroLLM Mattermost posts indexed through 2026-08-18. Member-only evidence
  links are retained where they document internal decisions or cluster artifacts.

Dataset pages retain their row-level evidence links and verification dates. The source spreadsheet was treated as read-only.

Public inventories are refreshed separately from the original sheet. At the
2026-08-18 refresh, the OpenEuroLLM Hugging Face organization listed 25 datasets;
new evaluation artifacts are recorded in this repository as evaluation-only.
Public revisions for OpenR1-Math-220k, Glaive Code Assistant v3, and BookSum
were queried on the same date. A current upstream revision is not treated as
proof that an older unpinned LUMI conversion came from those bytes.
