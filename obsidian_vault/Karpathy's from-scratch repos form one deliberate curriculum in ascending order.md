---
title: "Karpathy's from-scratch repos form one deliberate curriculum in ascending order"
type: knowledge-entry
domain: "Learning Path"
entry-type: "Resource"
confidence: high
durability: durable
evidence: 7
summary: "Seven of his repositories build on each other rather than standing alone: micrograd (a scalar autograd engine, ~17k stars) teaches backpropagation; makemore adds character-level autoregression; minGPT"
tags: [knowledge, learning-path, conf/high, durable, karpathy, curriculum, from-scratch, llm-training]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Learning Path]]"]
---

# Karpathy's from-scratch repos form one deliberate curriculum in ascending order

## What it is

Seven of his repositories build on each other rather than standing alone: micrograd (a scalar autograd engine, ~17k stars) teaches backpropagation; makemore adds character-level autoregression; minGPT is a minimal PyTorch GPT; nanoGPT is the trainable production-minimal version (~62k); build-nanogpt is the recorded lecture that constructs it; nanochat (~57k) assembles a full ChatGPT-style system on a small budget; llm.c (~31k) drops to raw C and CUDA once the concepts are settled.

## Why it matters

Working them in this order gives a mechanical understanding of LLM training that no course summary conveys - and it is the cheapest route from 'I call LLM APIs' to 'I know what happens inside'.

## Provenance

- Confidence **high** · durability **durable** · supported by **7** archived item(s).

## Sources

- https://github.com/karpathy/micrograd
- https://github.com/karpathy/nanoGPT
- https://github.com/karpathy/nanochat
- https://github.com/karpathy/llm.c

---

Part of [[MOC - Learning Path]] · [[Home]]
