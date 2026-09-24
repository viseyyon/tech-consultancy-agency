---
title: "NPU-Accelerated On-Device Inference via LiteRT"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 1
summary: "Google's LiteRT is positioned as the path to run meaningfully larger models on-device (mobile/desktop/IoT) by targeting NPU acceleration directly; Google cites partners running roughly 25x larger mode"
tags: [knowledge, model-serving-local-inference, conf/medium, durable, on-device, npu, litert, edge-inference]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# NPU-Accelerated On-Device Inference via LiteRT

## What it is

Google's LiteRT is positioned as the path to run meaningfully larger models on-device (mobile/desktop/IoT) by targeting NPU acceleration directly; Google cites partners running roughly 25x larger models on-device without the battery/latency hit of CPU/GPU-only inference.

## Why it matters

Relevant when deciding whether an inference workload needs a cloud model call at all versus running locally on NPU-equipped hardware.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- https://developers.googleblog.com/building-real-world-on-device-ai-with-litert-and-npu

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
