---
title: "Phi-4 14B fine-tune plan for a Broadcom/Qualcomm SDK specialist assistant"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "He selected Microsoft Phi-4 14B as the strongest Ollama-compatible coding base model (cited Codeforces pass@3 of 63.6%, combined Python/C++ accuracy of 73.6%) to fine-tune into an OpenWrt/embedded dev"
tags: [knowledge, model-serving-local-inference, conf/high, durable, phi-4, lora, ollama, broadcom]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Phi-4 14B fine-tune plan for a Broadcom/Qualcomm SDK specialist assistant

## What it is

He selected Microsoft Phi-4 14B as the strongest Ollama-compatible coding base model (cited Codeforces pass@3 of 63.6%, combined Python/C++ accuracy of 73.6%) to fine-tune into an OpenWrt/embedded developer assistant specialized in Broadcom/Qualcomm SDK code. The plan uses LoRA (r=16, alpha=32, targeting q_proj/v_proj, dropout 0.1) over 1-3 epochs, then exports to GGUF for ollama import, with recommended inference settings of temperature 0.8 and top_p 0.95.

## Why it matters

Captures the specific model choice and hyperparameters he settled on for his most ambitious local fine-tuning project, avoiding redundant re-research.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- AI Automation Projects — Ollama & Phi-4 Fine-Tuning Detail

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
