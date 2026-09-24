---
title: "Speculative decoding and attention-kernel research for faster inference"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Technique"
confidence: low
durability: durable
evidence: 4
summary: "z-lab's DFlash applies block-diffusion-based speculative decoding to speed up LLM token generation; Qwen's FlashQLA is a CUDA/TileLang kernel library for faster linear-attention computation, in the sp"
tags: [knowledge, model-serving-local-inference, conf/low, durable, speculative-decoding, attention-kernel, inference-speed, cuda]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Speculative decoding and attention-kernel research for faster inference

## What it is

z-lab's DFlash applies block-diffusion-based speculative decoding to speed up LLM token generation; Qwen's FlashQLA is a CUDA/TileLang kernel library for faster linear-attention computation, in the spirit of FlashAttention.

## Why it matters

Relevant when optimizing inference throughput or latency for a self-hosted model rather than accepting default generation speed.

## Provenance

- Confidence **low** · durability **durable** · supported by **4** archived item(s).
- Low confidence: the only evidence was a creator's headline. Treat as a lead, not a fact.

## Sources

- https://github.com/z-lab/dflash
- https://github.com/QwenLM/FlashQLA

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
