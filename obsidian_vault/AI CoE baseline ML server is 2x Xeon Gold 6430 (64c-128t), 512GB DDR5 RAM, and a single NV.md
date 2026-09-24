---
title: "AI CoE baseline ML server is 2x Xeon Gold 6430 (64c/128t), 512GB DDR5 RAM, and a single NVIDIA A2 16GB GPU"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 3
summary: "Vantiva's AI CoE baseline ML server is 2x Xeon Gold 6430 (64c/128t), 512GB DDR5 RAM, and a single NVIDIA A2 16GB GPU. The A2 is adequate for inference/small-scale POC but a recognized bottleneck for t"
tags: [knowledge, environment-tooling-state, conf/high, durable, hardware, gpu, ai-coe, infrastructure]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# AI CoE baseline ML server is 2x Xeon Gold 6430 (64c/128t), 512GB DDR5 RAM, and a single NVIDIA A2 16GB GPU

## What it is

Vantiva's AI CoE baseline ML server is 2x Xeon Gold 6430 (64c/128t), 512GB DDR5 RAM, and a single NVIDIA A2 16GB GPU. The A2 is adequate for inference/small-scale POC but a recognized bottleneck for training; the plan is to defer a GPU upgrade (staged RTX 4090s, later A40s) until a POC proves the approach is worth the spend.

## Why it matters

This is the real starting hardware baseline for any AI/ML project planning — training-heavy work will hit the GPU bottleneck until an upgrade is approved.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
