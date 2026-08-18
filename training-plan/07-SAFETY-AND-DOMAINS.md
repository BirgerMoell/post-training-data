# Stage 7 — safety integration and domain branches

## Goal

Create a production-safe general checkpoint and optional specialist branches.
Safety is not a late patch: safety examples and evaluations must be present in
Stages 2, 5, and 6. This stage performs the dedicated safety integration and
keeps specialist data from silently redefining the flagship model.

## Current data

### Safety and civic

The catalogue contains a planned
[`oellm-eu-safety-civic-v1`](../datasets/oellm-eu-safety-civic-v1/README.md),
but no canonical production artifact. ArenaHard-EU and battle annotations are
evaluation/feedback assets, not a complete safety training set.

This means the flagship safety stage is currently blocked.

### Medical branch

| Asset | State | Use |
| --- | --- | --- |
| [EU medical post-train v1](../datasets/birgermoell-oellm-eu-medical-posttrain-v1/README.md) | Public and on LUMI | Source collection and evaluation/branch data |
| [Medical SFT Parquet](../datasets/medical-sft-parquet/README.md) | Configured/runnable | Swedish medical SFT branch |
| [Medical DPO Parquet](../datasets/medical-dpo-parquet/README.md) | Staged | Swedish/mixed medical preference branch |

Medical data is currently strongest in Swedish. It is insufficient for a
pan-European medical claim and must not be merged into the general checkpoint
without measuring false medical authority and non-medical behavior.

## Required safety data families

For each claimed language and deployment profile, the production freeze needs:

- harmful-request refusal and safe redirection;
- benign prompts that resemble harmful requests, to prevent over-refusal;
- privacy and personal-data handling;
- self-harm and crisis response;
- cybersecurity dual-use boundaries;
- medical/legal/financial uncertainty and escalation;
- civic/election information, political neutrality, and local institutions;
- hate/harassment and protected-class robustness;
- child safety; and
- jailbreak, prompt-injection, tool misuse, and data-exfiltration scenarios.

Each item requires policy category, locale/language, expected behavior,
provenance, and review status. Translate only after the policy intent is stable,
then audit by native speakers.

## Proposed safety sequence

1. Write and approve the policy taxonomy before generating training data.
2. Build protected evaluation first; keep it out of generation prompts and
   training corpora.
3. Create paired safe/unsafe and benign-neighbor examples in priority languages.
4. Run safety SFT with at least 50% general multilingual replay in the first
   pilot to control over-refusal.
5. Add safety preference data in a short DPO phase using the selected Stage 5
   settings.
6. If tool use is enabled, add sandboxed prompt-injection and least-privilege
   tests.
7. Evaluate helpfulness, refusal precision/recall, language consistency, and
   jailbreak robustness separately.

The 50% replay floor is a conservative pilot setting, not a confirmed recipe.

## Domain branch procedure

1. Branch from the final general or safety-integrated checkpoint.
2. Freeze domain-specific training and evaluation separately.
3. Keep 30–50% general/safety replay during domain SFT.
4. Run domain preference or RL only with expert-valid rewards.
5. Publish a separate model identifier and capability/risk statement.
6. Merge back into the flagship only after a controlled ablation proves a net
   benefit without broad regressions.

## Exit gate

- Safety policy and dataset owners approve all production categories.
- Native-speaker audits cover every claimed language group.
- Refusal precision and recall meet signed thresholds, including benign-neighbor
  tests.
- Tool and long-context prompt-injection tests pass when applicable.
- Medical or other specialist branches pass expert evaluation and remain
  clearly separated from the general release.

## Missing

- Canonical multilingual safety/civic SFT and preference artifacts.
- European policy taxonomy and native-speaker review coverage.
- Long-context and tool-agent safety data.
- Pan-European medical data and expert-reviewed evaluations.
- A release decision on whether any domain branch should feed the flagship.
