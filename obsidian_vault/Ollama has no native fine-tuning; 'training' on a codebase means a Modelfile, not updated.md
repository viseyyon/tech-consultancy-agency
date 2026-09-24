---
title: "Ollama has no native fine-tuning; 'training' on a codebase means a Modelfile, not updated weights"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "When asked to 'train' an Ollama-based senior-developer model on a specific codebase (ossAT, MongoDB/Docker app), the actual mechanism was a Modelfile defining a system prompt and domain knowledge, not"
tags: [knowledge, model-serving-local-inference, conf/medium, durable, ollama, fine-tuning, modelfile, local-inference]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Ollama has no native fine-tuning; 'training' on a codebase means a Modelfile, not updated weights

## What it is

When asked to 'train' an Ollama-based senior-developer model on a specific codebase (ossAT, MongoDB/Docker app), the actual mechanism was a Modelfile defining a system prompt and domain knowledge, not real weight-level fine-tuning -- Ollama itself doesn't support direct fine-tuning.

## Why it matters

Any future request to 'train the model on our repo' via Ollama needs to be reframed as Modelfile/context engineering, or routed to a real fine-tuning pipeline (e.g. QLoRA) if weight updates are actually required.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
