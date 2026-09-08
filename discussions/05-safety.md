# Discussion 5 — multilingual safety data

## Proposed decision

Materialize `oellm-eu-safety-civic-v1` before the flagship data freeze. Today
the register has a planned product but no canonical multilingual training
artifact, so safety remains the largest data blocker. Build safety SFT and
preference sets together with protected evaluation, but keep their prompts,
documents, and semantic derivatives strictly separate.

Safety must optimize two behaviors at once: refusing or safely redirecting
genuinely harmful requests, and fully helping with benign requests that share
surface words with harmful topics. An English refusal dataset translated 35
times is not a European safety programme.

## Existing and external sources

| Source | Decision | Intended use / blocker |
| --- | --- | --- |
| Planned `oellm-eu-safety-civic-v1` | Build first | Canonical project product; needs an owner, policy taxonomy, language quotas, evaluator, and red-team holdout |
| OASST2 and approved general SFT | Use as helpfulness replay | Prevent blanket refusal; apply PII, unsafe-content, and language-quality filters |
| WildChat | Hold for threat discovery | Mine failure patterns only after privacy/terms review; raw conversations are not safe target behavior |
| [`allenai/wildguardmix`](https://huggingface.co/datasets/allenai/wildguardmix) | Pilot for taxonomy/classifier work | English, gated, ODC-BY, and contains harmful material; do not treat classifier labels as safe assistant completions |
| [`PKU-Alignment/PKU-SafeRLHF`](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF) | Pilot English preference baseline | Audit taxonomy, labels, license, cultural assumptions, and overlap; it does not solve European-language coverage |
| [`NASK-PIB/RefusEU`](https://huggingface.co/datasets/NASK-PIB/RefusEU) | Hold pending license | Particularly relevant 12-language refusal/preference research, but the current card leaves the release license unspecified and includes an eval split that must stay protected |
| [`stindardlogic/multilang-refusal-dpo-3k`](https://huggingface.co/datasets/stindardlogic/multilang-refusal-dpo-3k) | Small pilot candidate | Apache-2.0 pairs in five European languages focused on over-refusal; verify provenance, native quality, policy coverage, and synthetic artifacts |
| [`OpenLLM-France/Luciole-PostTraining-Dataset-1.1`](https://huggingface.co/datasets/OpenLLM-France/Luciole-PostTraining-Dataset-1.1) | Pilot source-family ablation | CC BY-SA 4.0 open post-training mix with safety pairs and dual-judge agreement; currently primarily English, so inspect the safety subset and parent overlap |
| Medical/counselling/compassion datasets | Hold | No inclusion without consent/privacy provenance, expert review, license, uncertainty labels, and a separate clinical-safety case |

HarmBench, XSTest, StrongREJECT, ArenaHard-EU, EUROPA, and any protected
project red-team suite are evaluation-only. Training data may share a policy
taxonomy, but not prompts, paraphrases, attack strings, source documents,
translations, or generator seeds.

## Product schema and coverage

Every training item should record language, script, locale, risk taxonomy,
direct/indirect and single/multi-turn framing, benign/harmful status, expected
behavior, allowed helpful content, refusal/redirection style, policy rationale,
native/translated/synthetic provenance, generator and reviewer identities, and
cross-split semantic-dedup evidence.

Cover at least:

- harmful requests plus useful safe alternatives;
- benign neighbors and dual-use requests to calibrate over-refusal;
- privacy, personal-data handling, and secret exfiltration;
- self-harm, crisis response, delusion reinforcement, manipulation, and
  parasocial dependency;
- cyber, CBRN, fraud, and other capability-scaled misuse;
- medical, legal, and financial uncertainty and escalation;
- civic/election information, political neutrality, and local institutions;
- hate/harassment, sexual and child safety;
- jailbreaks, role-play, multilingual code-switching, and obfuscation; and
- prompt injection, tool misuse, long-context hidden instructions, and
  irreversible-action permission checks.

Use native scenario authors for civic, health-system, and culturally dependent
items. Translation is acceptable for stable policy semantics, followed by a
native safety review. Synthetic generation should create paired harmful and
benign-neighbor prompts, several candidate responses, and explicit failure
counterexamples. At least two calibrated reviewers should adjudicate ambiguous
or high-severity items.

## Training plan

1. Approve the policy taxonomy and protected eval before generation.
2. Run safety SFT with at least 50% general multilingual helpfulness replay in
   the first pilot.
3. Run a short multilingual safety DPO phase with preference margins and
   bilingual audits.
4. If tools or 128K context are released, add dedicated permission,
   prompt-injection, and indirect-harm recovery data.
5. Compare safety-before-DPO, safety-after-DPO, and final safety-recovery
   checkpoints at matched tokens.
6. Keep high-stakes domain branches separate unless a controlled ablation and
   governance decision support integration.

The replay floor is a conservative pilot, not a final ratio. Report the
helpfulness/refusal frontier rather than selecting a checkpoint on refusal rate
alone.

## Acceptance gates

- Native-reviewed coverage exists for every claimed language tier, with a
  published gap if any target language is not ready.
- HarmBench/StrongREJECT attack success, XSTest/benign-neighbor over-refusal,
  multi-turn psychological harm, privacy, and tool-permission gates pass by
  language and category.
- EUROPA harmful-request refusal and ordinary helpfulness-related capabilities
  do not regress, while its public rows remain evaluation-only.
- Critical high-severity failures are zero in the protected release review.
- Helpful safe completions are preferred over terse refusal when meaningful
  assistance is allowed.
- The model does not switch to English, reveal policy boilerplate, or become
  more permissive under code-switching, long context, role-play, or tool use.
- External specialist review covers dangerous-capability areas appropriate to
  the model's capability level.

## Questions for the thread

1. Who is the accountable safety-data and policy owner?
2. Which languages and risk categories form the first native-review tranche?
3. Can RefusEU obtain a clear training/release license and a clean separation
   between its train and evaluation material?
4. Which deployment capabilities—tools, browsing, code execution, 128K/256K—
   must the first safety artifact cover?
