---
title: "Tokenization has its own two-step path: minbpe then rustbpe"
type: knowledge-entry
domain: "Learning Path"
entry-type: "Resource"
confidence: high
durability: durable
evidence: 3
summary: "minbpe is clean minimal Python for the byte-pair-encoding algorithm that underlies LLM tokenization; rustbpe is described by its author as the missing tiktoken training code, in Rust. nn-zero-to-hero"
tags: [knowledge, learning-path, conf/high, durable, tokenization, bpe, karpathy, fundamentals]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Learning Path]]"]
---

# Tokenization has its own two-step path: minbpe then rustbpe

## What it is

minbpe is clean minimal Python for the byte-pair-encoding algorithm that underlies LLM tokenization; rustbpe is described by its author as the missing tiktoken training code, in Rust. nn-zero-to-hero is the lecture series that frames both.

## Why it matters

Tokenizer behaviour explains a large share of otherwise baffling model failures, and these two repos are the shortest path to actually understanding it rather than treating it as a black box.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- https://github.com/karpathy/minbpe
- https://github.com/karpathy/rustbpe
- https://github.com/karpathy/nn-zero-to-hero

---

Part of [[MOC - Learning Path]] · [[Home]]
