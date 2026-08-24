# Capability target matrix

This generated view collects numeric targets from every evaluation manifest. `TBD` means the metric is structured but needs an immutable base-checkpoint baseline or an approved operating SLO.

| Capability | Suite | Metric | Direction | 9B committed | 30B committed | Stretch | Gate |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| [Safety](safety/README.md) | HarmBench with StrongREJECT scoring | attack success rate | `<=` | 5 | 3 | 1 | non-compensatory |
| [Safety](safety/README.md) | XSTest safe-request refusal | safe-prompt refusal rate | `<=` | 10 | 5 | 2 | release |
| [Safety](safety/README.md) | Multi-turn psychological-harm red team | critical release failures | `<=` | 0 | 0 | 0 | non-compensatory |
| [Safety](safety/README.md) | CBRN, cyber, and loss-of-control audit | material uplift beyond comparable open-weight models | `<=` | 0 | 0 | 0 | non-compensatory (diagnostic pending separation) |
| [Multilingual](multilingual/README.md) | MMLU-ProX, EU MMLU, MMMLU, and INCLUDE | MMLU-ProX EU24 macro | `>=` | 50 | 65 | 72 | headline |
| [Multilingual](multilingual/README.md) | MMLU-ProX, EU MMLU, MMMLU, and INCLUDE | EU MMLU macro | `>=` | 70 | 78 | 82 | headline |
| [Multilingual](multilingual/README.md) | MMLU-ProX, EU MMLU, MMMLU, and INCLUDE | EU MMLU minimum language | `>=` | 55 | 65 | 72 | headline |
| [Multilingual](multilingual/README.md) | MMLU-ProX, EU MMLU, MMMLU, and INCLUDE | MMMLU EU24 macro | `>=` | 68 | 75 | 80 | headline |
| [Multilingual](multilingual/README.md) | MMLU-ProX, EU MMLU, MMMLU, and INCLUDE | INCLUDE score | `>=` | 74 | 79 | 82 | headline |
| [Multilingual](multilingual/README.md) | EuroEval leaderboard | overall leaderboard rank | `rank<=` | 10 | 5 | 3 | headline (diagnostic pending separation) |
| [Multilingual](multilingual/README.md) | WMT24++ and FLORES diagnostic | WMT24++ score | `>=` | 83.5 | 84 | 85 | diagnostic (diagnostic pending separation) |
| [Multilingual](multilingual/README.md) | Language tier and fidelity audit | response language fidelity | `>=` | 98 | 98 | 99 | release |
| [Multilingual](multilingual/README.md) | Language tier and fidelity audit | macro to minimum-language gap | `<=` | 15 | 10 | 7 | release |
| [Instruction & Chat](instruction-chat/README.md) | IFEval, IFBench, and MAXIFE | IFEval | `>=` | 75 | 85 | 90 | headline |
| [Instruction & Chat](instruction-chat/README.md) | IFEval, IFBench, and MAXIFE | IFBench | `>=` | 60 | 70 | 76 | headline |
| [Instruction & Chat](instruction-chat/README.md) | IFEval, IFBench, and MAXIFE | MAXIFE | `>=` | 80 | 85 | 88 | headline |
| [Instruction & Chat](instruction-chat/README.md) | IFEval, IFBench, and MAXIFE | valid constrained output | `>=` | 99 | 99 | 99.5 | headline |
| [Instruction & Chat](instruction-chat/README.md) | OpenEuroLLM multilingual arena | lower 95% CI of pairwise win rate | `>=` | 50 | 50 | 55 | headline |
| [Instruction & Chat](instruction-chat/README.md) | OpenEuroLLM multilingual arena | minimum-language win rate | `>=` | 45 | 45 | 50 | headline |
| [Instruction & Chat](instruction-chat/README.md) | LMArena text leaderboard | overall text leaderboard rank | `rank<=` | 200 | 100 | 50 | headline (diagnostic pending separation) |
| [Instruction & Chat](instruction-chat/README.md) | LMArena text leaderboard | arena score | `>=` | 1346 | 1425 | 1458 | headline (diagnostic pending separation) |
| [Instruction & Chat](instruction-chat/README.md) | Arena-Hard v2 | Arena-Hard v2 score | `>=` | 25 | 45 | 55 | headline (diagnostic pending separation) |
| [Instruction & Chat](instruction-chat/README.md) | Multi-turn chat quality audit | critical dialogue failures | `<=` | 0 | 0 | 0 | release |
| [Reasoning & Knowledge](reasoning-knowledge/README.md) | MGSM and PolyMath | MGSM EU24 | `>=` | 78 | 88 | 92 | headline |
| [Reasoning & Knowledge](reasoning-knowledge/README.md) | MGSM and PolyMath | PolyMath | `>=` | 55 | 68 | 72 | headline |
| [Reasoning & Knowledge](reasoning-knowledge/README.md) | MMLU-ProX and EU MMLU | MMLU-ProX EU24 macro | `>=` | 50 | 65 | 72 | headline |
| [Reasoning & Knowledge](reasoning-knowledge/README.md) | MMLU-ProX and EU MMLU | EU MMLU macro | `>=` | 70 | 78 | 82 | headline |
| [Reasoning & Knowledge](reasoning-knowledge/README.md) | AA-Omni non-hallucination | non-hallucination score | `>=` | 65 | 72 | 78 | release (diagnostic pending separation) |
| [Reasoning & Knowledge](reasoning-knowledge/README.md) | GPQA and Humanity's Last Exam diagnostics | accuracy | `>=` | TBD | TBD | TBD | diagnostic (diagnostic pending separation) |
| [Grounding & RAG](grounding-rag/README.md) | OpenEuroLLM multilingual RAG holdout | answerable correctness delta vs parent | `>=` | TBD | TBD | TBD | release |
| [Grounding & RAG](grounding-rag/README.md) | OpenEuroLLM multilingual RAG holdout | unanswerable correctness delta vs parent | `>=` | TBD | TBD | TBD | release |
| [Grounding & RAG](grounding-rag/README.md) | OpenEuroLLM multilingual RAG holdout | unsupported critical claims | `<=` | 0 | 0 | 0 | release |
| [Grounding & RAG](grounding-rag/README.md) | Citation precision, recall, and claim support | citation precision | `>=` | TBD | TBD | TBD | headline |
| [Grounding & RAG](grounding-rag/README.md) | Citation precision, recall, and claim support | citation recall | `>=` | TBD | TBD | TBD | headline |
| [Grounding & RAG](grounding-rag/README.md) | Retriever/generator attribution matrix | end-to-end correctness | `>=` | TBD | TBD | TBD | diagnostic (diagnostic pending separation) |
| [Tools & Agents](tools-agents/README.md) | Berkeley Function Calling Leaderboard v4 | BFCL v4 overall | `>=` | 60 | 67 | 70 | headline |
| [Tools & Agents](tools-agents/README.md) | τ²-bench | task success | `>=` | 65 | 75 | 80 | headline |
| [Tools & Agents](tools-agents/README.md) | BrowseComp | BrowseComp accuracy | `>=` | 25 | 50 | 60 | headline (diagnostic pending separation) |
| [Tools & Agents](tools-agents/README.md) | Protected permission and recovery tasks | unauthorized irreversible actions | `<=` | 0 | 0 | 0 | non-compensatory |
| [Long Context](long-context/README.md) | RULER and needle-in-a-haystack precondition | retrieval success through advertised context | `>=` | 95 | 95 | 99 | release |
| [Long Context](long-context/README.md) | MRCR at 128k | MRCR 128k | `>=` | 35 | 55 | 67 | headline |
| [Long Context](long-context/README.md) | LongBench v2 | LongBench v2 | `>=` | 50 | 58 | 61 | headline |
| [Long Context](long-context/README.md) | Long-context serving and short-context preservation | maximum priority-language short-context regression | `<=` | 2 | 2 | 1 | non-compensatory |
| [Coding](coding/README.md) | LiveCodeBench | pass@1 | `>=` | 55 | 70 | 80 | headline |
| [Coding](coding/README.md) | EvalPlus | pass@1 | `>=` | TBD | TBD | TBD | diagnostic (diagnostic pending separation) |
| [Coding](coding/README.md) | Protected multilingual defect-repair holdout | tasks with all tests passed | `>=` | TBD | TBD | TBD | release |
| [Coding](coding/README.md) | Secure coding audit | critical vulnerabilities introduced | `<=` | 0 | 0 | 0 | non-compensatory (diagnostic pending separation) |
| [Efficiency & Release](efficiency-release/README.md) | Quantization quality preservation | maximum macro capability loss vs BF16 | `<=` | 1 | 1 | 0.5 | non-compensatory |
| [Efficiency & Release](efficiency-release/README.md) | Quantization quality preservation | maximum priority language/capability loss | `<=` | 2 | 2 | 1 | non-compensatory |
| [Efficiency & Release](efficiency-release/README.md) | Serving latency, throughput, memory, and stability | requests meeting latency SLO | `>=` | TBD | TBD | TBD | release (diagnostic pending separation) |
| [Efficiency & Release](efficiency-release/README.md) | Serving latency, throughput, memory, and stability | out-of-memory request rate | `<=` | 0 | 0 | 0 | release (diagnostic pending separation) |
| [Efficiency & Release](efficiency-release/README.md) | Release artifact and provenance audit | required release artifacts complete | `>=` | 100 | 100 | 100 | non-compensatory |
| [Efficiency & Release](efficiency-release/README.md) | Independent evaluation reproduction | headline metrics reproduced within tolerance | `>=` | 100 | 100 | 100 | release |

Generated from the nine `evaluation.json` manifests.
