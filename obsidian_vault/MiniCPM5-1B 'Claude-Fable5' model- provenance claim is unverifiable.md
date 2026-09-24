---
title: "MiniCPM5-1B 'Claude-Fable5' model: provenance claim is unverifiable"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "A GGUF-quantized 1B fine-tune on HuggingFace claiming training on 'Fable 5 traces' (implying Claude/Fable 5 distillation) has no dataset card, no eval benchmarks, and an unverified org -- and sits ins"
tags: [knowledge, evaluation-observability, conf/high, durable, provenance, huggingface, claude, model-verification]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# MiniCPM5-1B 'Claude-Fable5' model: provenance claim is unverifiable

## What it is

A GGUF-quantized 1B fine-tune on HuggingFace claiming training on 'Fable 5 traces' (implying Claude/Fable 5 distillation) has no dataset card, no eval benchmarks, and an unverified org -- and sits inside a documented wave of satirical/hype-bait uploads riding the Claude Fable 5 name post-launch. Cisco's open-source Model Provenance Kit (April 2026) can confirm shared lineage between two checkpoints by fingerprinting architecture/tokenizer/weights, but it cannot verify a closed-model-distillation claim like this one, since that needs teacher-side watermarking, not retroactive weight comparison.

## Why it matters

A concrete case for treating any unsubstantiated 'trained on Claude/Fable 5 outputs' claim as unverifiable rather than evidence of real distillation.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- HuggingFace model provenance analysis session

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
