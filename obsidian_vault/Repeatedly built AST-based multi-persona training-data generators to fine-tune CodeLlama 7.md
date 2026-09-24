---
title: "Repeatedly built AST-based multi-persona training-data generators to fine-tune CodeLlama 7B for OEM code review"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 4
summary: "Across at least four conversations in July-August 2025, the same architecture was iterated: use AST analysis (not regex/embeddings) to extract code structure, then generate fine-tuning data training C"
tags: [knowledge, model-serving-local-inference, conf/high, durable, codellama, fine-tuning, ast, multi-persona]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Repeatedly built AST-based multi-persona training-data generators to fine-tune CodeLlama 7B for OEM code review

## What it is

Across at least four conversations in July-August 2025, the same architecture was iterated: use AST analysis (not regex/embeddings) to extract code structure, then generate fine-tuning data training CodeLlama 7B to review code from four personas simultaneously (architect, senior developer, security officer, code reviewer) with an AI feedback loop scoring sample quality. Domain-specific pattern detection covered automotive (AUTOSAR/ISO 26262/MISRA), embedded (RTOS/HAL/BSP), industrial (OPC-UA/Modbus/PLC), IoT (MQTT/CoAP/LwM2M), and medical (IEC 62304/DICOM/HL7); later iterations added curriculum learning, quality-weighted loss, and local model-shard caching.

## Why it matters

This is his most recurring technical project theme in this batch, so future requests about multi-persona code review fine-tuning should be recognized as continuing this line rather than a new idea.

## Provenance

- Confidence **high** · durability **durable** · supported by **4** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
