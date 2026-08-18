# Language coverage by capability

This page distinguishes broad data from narrow repair or evaluation coverage.
The matrix describes the catalogue as of 2026-08-18; it does not guarantee that
all listed rows have passed quality or legal approval.

| Capability | Strongest confirmed coverage | Thin or missing coverage |
| --- | --- | --- |
| General instruction SFT | English plus `cs,de,el,es,fi,fr,it,nl,pl,pt,ro,sv,uk` from Dolci translated and EU-Instruct-Synthetic | `bg,hr,da,et,ga,hu,lv,lt,mt,sk,sl` lack comparable broad general SFT |
| Targeted repair | `is,ga,mt,et,hr,sl,lt,lv,da,hu,sk,bg,ro,pl,fi` | Narrow defect templates do not establish general assistant quality |
| Continued pretraining / long context | Jouni blend includes broad European HPLT/FinePDFs/OPUS/MultiSynt sources plus English/code/math/science; an 18.3 GB English–Finnish long-SFT candidate is staged | Candidate lengths/masks/lineage are unverified; broad European instruction-level 64k/128k coverage and multilingual long-context evaluation are missing |
| Reasoning SFT | Primarily English; Finnish seed exists; OpenR1 and a 40.2 GB local think mix add English breadth | Canonical multilingual reasoning translations are not stored; most languages missing; local mixture lineage unverified |
| Tool/agentic SFT | Primarily English; EU tool-use v1 is currently English | Multilingual schemas, requests, arguments, observations, and execution evals missing |
| Preference optimization | `cs,de,el,es,fi,fr,it,pl,ro,sv,uk` plus English in translated Dolci DPO | Dutch, Portuguese, and repair-only languages missing; preference fidelity unverified |
| RLVR/GRPO | Multilingual exam MCQ reaches many languages; Finnish AutoIF candidate | Common verifiers/backend missing; coverage is task-specific rather than broad |
| Safety/civic | No production set | Missing across all release languages |
| Medical | Swedish SFT/DPO pilot; some multilingual exam/eval sources | Pan-European specialist data and expert validation missing |
| Evaluation | EU holdouts span 38 language codes; Belebele, Global-MMLU/MMMLU, XCOPA, ArenaHard-EU, FLORES/FLORES+, and English–Finnish Tatoeba | Multilingual long-context, tool, safety, and native cultural evaluation remain incomplete |

## EU official-language view

The union of broad SFT and targeted repair touches all 24 EU official
languages, but the depth is not comparable:

- **Broad general SFT:** English plus `cs,de,el,es,fi,fr,it,nl,pl,pt,ro,sv`.
  Ukrainian is also covered but is not an EU official language. Bulgarian is
  present in repair and long-context text, but not in the broad instruction union.
- **Repair-only or mostly repair:** `bg,hr,da,et,ga,hu,lv,lt,mt,sk,sl`.
- **English:** strong general coverage but must be capped so it does not dominate
  multilingual stages.

## Minimum evidence before claiming a language

For each advertised language, require:

1. source and trainable-token totals by stage;
2. native-versus-translated/synthetic composition;
3. at least 100 inspected formatted examples per major source;
4. protected native evaluation for general instruction and local knowledge;
5. safety evaluation reviewed by a native speaker;
6. long-context evaluation if the model advertises the target length in that
   language; and
7. a model-card limitation when reasoning, tools, preference, or safety are not
   supported to the same depth as English.

## Next data work by priority

1. Build broad native/general instruction data for the 11 repair-only EU
   languages.
2. Materialize the planned seven-language reasoning translations and extend to
   repair-only languages.
3. Create multilingual tool schemas and execution-grounded conversations.
4. Build preference pairs and safety data with bilingual/native review.
5. Create a protected multilingual long-context benchmark across length
   buckets and document types.
