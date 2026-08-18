# Framework and artifact handoffs

The catalogue should guide training without forcing every stage into one file
format. The portable source of truth is the pinned raw/normalized dataset; each
framework-specific artifact is a derived product.

## What is available

| Framework | Best fit | Current OpenEuroLLM state | Input to prepare | Main limitation |
| --- | --- | --- | --- | --- |
| Megatron-LM on LUMI | Continued pretraining and long-context extension | Confirmed 16k/64k/128k packed-pretraining lineage | `.bin`/`.idx` prefixes, data weights, tokenizer, checkpoint | Current production recipe lives in a user workspace; no shared frozen manifest |
| [Megatron-Bridge-LUMI](https://github.com/OpenEuroLLM/Megatron-Bridge-LUMI) | HF/Megatron conversion, pretraining, SFT/LoRA | Qwen3 conversion and SFT support available upstream; LUMI fork exists | HF or Megatron checkpoint plus normalized SFT data | Exact flagship model recipe and cluster validation still need pinning |
| [OpenEuroLLM/post-training](https://github.com/OpenEuroLLM/post-training) with TRL | General/reasoning/tool SFT and DPO | Active, config-driven, multi-node SLURM | HF dataset with `messages` for SFT or chosen/rejected preference rows | No GRPO; several templates are intentionally blocked for SFT because assistant-only masks are unsafe |
| LlamaFactory backend in `post-training` | SFT/DPO and long-context experiments | A Jupiter-oriented 16k example exists | LlamaFactory dataset registry plus normalized conversations | The checked-in `long_sft` data is a placeholder, not an OpenEuroLLM production mix |
| OLMo-core | Reproducing Dolci Instruct/Think SFT | Published tokenized OpenEuroLLM artifacts | Premerged NumPy token IDs and label masks | Tokenized artifact is tied to its tokenizer and cannot be reused for Prelude |
| Alignment-handbook scripts | Historical SFT -> DPO reference | A Tulu-3 two-stage example exists | HF SFT and preference datasets | Not the common production pipeline and lacks later stages |

The staged LUMI `Megatron_format` corpora are mostly one-field, already-rendered
`text` JSONL with paired `.bin`/`.idx`. That makes them convenient for Megatron
CLM, but not automatically safe for instruction tuning: a normal text-document
loader trains on system and user tokens as well as assistant tokens. Any stage
requiring assistant-only loss must recover structured messages or build and
test a separate label mask rather than trusting the directory name.

## Handoff rules

### Context extension to SFT

1. Convert the selected Megatron checkpoint to Hugging Face using a pinned
   Megatron Bridge/utilities commit.
2. Compare logits on fixed prompts before and after conversion.
3. Confirm tokenizer identity, RoPE configuration, maximum positions, special
   tokens, tied embeddings, and chat template.
4. Run 4k/32k/64k/128k evaluation before SFT.
5. Keep the Megatron checkpoint until the converted model passes parity.

### Raw SFT data to TRL or LlamaFactory

1. Keep the source as pinned Parquet/Arrow/JSONL or a pinned HF dataset.
2. Normalize roles and tool metadata without flattening structured tool calls.
3. Apply the target model's chat template.
4. Verify `{% generation %}` markers and assistant-only labels. The current
   common framework only marks `olmo3-instruct-sft` and `olmo3-think-sft` as
   safe for SFT; ChatML, Tulu3, Apertus, and the legacy OLMo3 alias require a
   reviewed mask fix.
5. Record total and trainable tokens after packing/truncation.

### SFT checkpoint to DPO

1. Use the exact SFT checkpoint as policy start.
2. Preserve the same tokenizer and chat template.
3. Render prompt/chosen/rejected triples and verify prompt-prefix equality.
4. Decide whether the reference model is explicit. The common framework warns
   that an implicit reference copy can be unstable with ZeRO-3.
5. Evaluate before and after DPO using identical generation settings.

### SFT/DPO checkpoint to RLVR

This handoff is not yet implemented in the common framework. A production plan
must select and pin the RL backend, rollout engine, verifier interfaces,
checkpoint converter, and failure-recovery behavior before Stage 6 is runnable.

## Minimum framework validation

For each new model size and cluster, require:

- one-node 20-step smoke test;
- multi-node 100-step test with checkpoint/resume;
- deterministic data order for a fixed seed;
- conversion round trip with numerical comparison;
- loss-mask unit tests for every chat template;
- exact effective batch and token-budget reporting; and
- a completed small-model integration build before the flagship allocation.
