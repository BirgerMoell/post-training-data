# Missing data and implementation blockers

This is the actionable gap register for a flagship post-training run. A gap is
closed only when an artifact, owner, acceptance check, and retained evidence
exist.

## P0 — blocks the flagship run

| Gap | Why it blocks training | Closure evidence | Suggested owner function |
| --- | --- | --- | --- |
| Immutable cross-stage data freeze | Current locations do not identify exact bytes, accepted licenses, hashes, or post-filter counts | Reviewed manifest with revisions, checksums, tokens, licenses, and decontamination report | Data/release lead |
| Long-context retention during SFT | Short 32k SFT has destroyed 128k capability in prior Poro-long experience | Small-model ablation selects a mixed-SFT or recovery strategy that passes 128k gates | Context + SFT leads |
| Multilingual long-context evaluation | The project cannot claim European 128k behavior from English-centric RULER results | Protected native multilingual suite with 4k–128k curves | Evaluation + language leads |
| Production multilingual safety/civic data | No canonical artifact exists; safety cannot be inferred from general SFT | Policy-approved SFT/preference set with native review and protected eval | Safety/legal/language leads |
| RLVR backend and verifiers | Candidate prompts exist, but the common pipeline cannot run or audit GRPO | Reproducible backend, versioned verifier package, resume test, small-model report | RL + infrastructure leads |
| Legal/license approval for mixed sources | Several cluster/public candidates have inherited, mixed, or unclear terms | Named approval and redistributability/training-use decision per source | Legal/data governance |
| Shared retained long-context artifacts | Strongest data/checkpoints live in user workspaces and flash/scratch | Shared immutable data/checkpoint root with checksums and restore plan | LUMI/release lead |

## P1 — blocks full capability or language claims

| Gap | Current evidence | Needed artifact |
| --- | --- | --- |
| Broad SFT for 11 repair-only EU languages | Defect repair exists, but no Dolci-scale general source | Native or high-quality translated/general SFT plus human review |
| Multilingual reasoning | English Dolci/Nemotron and Finnish seed; translations planned | Canonical stored translations, correctness filtering, native eval |
| Multilingual tools | Tool mixtures are predominantly English | Localized schemas, requests, arguments, tool results, unseen-schema eval |
| Preference fidelity after translation | Translated Dolci DPO is public | Bilingual audit, preference-margin consistency, per-language DPO eval |
| Long-context instruction data | An 18.3 GB English–Finnish LUMI SFT candidate exists, but its lineage, licenses, actual length buckets, and assistant mask are unknown | Validated freeze of that asset plus broader 64k/128k European retrieval, synthesis, and multi-document instructions |
| Cross-stage deduplication | Decontaminated releases exist independently | One duplicate/contamination map covering SFT, DPO, RLVR, and eval |
| Safe chat templates | Only OLMo3 instruct/think templates are marked safe for SFT in common framework | Generation-marker fixes and loss-mask tests for Prelude/ChatML/Tulu/Apertus |
| Common checkpoint gate | Many evaluation datasets exist | Signed thresholds, exact harness revision, and stage-delta dashboard |
| Native cultural/civic evaluation | Broad multilingual academic benchmarks exist | Locale-specific, current, protected evaluation with native review |

## P2 — improves robustness and maintainability

| Gap | Needed work |
| --- | --- |
| Dataset quality scorecards | Per-source language, duplication, toxicity, PII, length, and human-sample reports |
| Source ablations | No-synthetic, no-code, native-only, translated-only, and quality-tier ablations |
| Shared artifact lifecycle | Expiry/retention policy for flash, scratch, public HF, and model checkpoints |
| 70B scalability evidence | Small/9B pipeline exists; stress-test memory, conversion, and resume at larger scale |
| Reproducible SimPO/reference-free path | Integrate method, configs, tests, and matched-compute comparison into common repo |
| Automated catalogue freshness | Periodically verify URLs, HF revisions, LUMI paths, and completed-run evidence |

## What is not missing

- A strong starting long-context data blend: Jouni's LUMI blend exists and has
  produced complete 16k/64k/128k checkpoints.
- General English SFT and reasoning sources: multiple decontaminated public
  OpenEuroLLM releases exist; OpenR1 Math, Glaive code, and a large AM think mix
  are also staged on LUMI, though the latter two still need production audits.
- A first multilingual instruction base: translated Dolci and EU synthetic data
  cover a useful set of languages, and a Poro2 Finnish corpus is staged for
  validation.
- DPO infrastructure: the common post-training repository implements TRL DPO.
- Broad evaluation starting points: European holdouts, FLORES/FLORES+,
  English–Finnish Tatoeba, and other multilingual benchmarks are catalogued and
  can be protected now.

The practical focus should therefore be closing retention, safety, low-resource
capability depth, reproducibility, and RL infrastructure—not collecting another
undifferentiated list of English datasets.
