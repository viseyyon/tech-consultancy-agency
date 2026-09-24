---
title: "CPE telemetry masking uses six defense-in-depth levels, fail-closed at the firmware logger"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "The RDK-B CPE customer-data masking architecture spans six defense-in-depth levels: firmware-level redaction (RDK-B logger macros, HMAC pseudonymization), pre-upload telemetry filtering (Telemetry 2.0"
tags: [knowledge, security-guardrails, conf/high, durable, pii-masking, rdk-b, fail-closed, telemetry]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# CPE telemetry masking uses six defense-in-depth levels, fail-closed at the firmware logger

## What it is

The RDK-B CPE customer-data masking architecture spans six defense-in-depth levels: firmware-level redaction (RDK-B logger macros, HMAC pseudonymization), pre-upload telemetry filtering (Telemetry 2.0/XConf), operator collector redaction (OpenTelemetry), medallion storage tiers (Bronze/Silver/Gold), a pre-AI ingestion gateway (Microsoft Presidio with per-operator CPE recognizers for Comcast/Rogers/Sky/Vodafone/BT/Charter), and LLM boundary guardrails. The firmware-level pii_logger_init is deliberately fail-closed: if the device key can't load from secure storage, every transform returns REDACTED rather than falling back to raw logging.

## Why it matters

This inverts typical graceful degradation so the safe failure mode is 'no log information' rather than 'leaked PII' — a design principle worth reusing anywhere else PII could leak through a failure path.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
