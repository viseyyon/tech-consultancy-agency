---
title: "Shadow-AI IP exposure splits into two distinct risk classes: SLA breach vs. copyright exposure"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "Investigating a live DOCSIS-skill initiative (built by Vijayakumar Thavamani, endorsed by SVP Nirav Vaidya) surfaced two structurally different IP risks: Class A is vendor source code (Broadcom/MaxLin"
tags: [knowledge, security-guardrails, conf/high, durable, shadow-ai, ip-risk, docsis, broadcom]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Shadow-AI IP exposure splits into two distinct risk classes: SLA breach vs. copyright exposure

## What it is

Investigating a live DOCSIS-skill initiative (built by Vijayakumar Thavamani, endorsed by SVP Nirav Vaidya) surfaced two structurally different IP risks: Class A is vendor source code (Broadcom/MaxLinear) routed through GitHub Copilot Agent mode, a direct Broadcom SLA breach; Class B is CableLabs DOCSIS spec content bulk-extracted and published to a public GitHub repo (vantiva-sa/AI-Projects), a copyright/redistribution exposure rather than a vendor-contract one.

## Why it matters

Treating both as the same problem under-serves the response — each needs a different control (egress routing for Class A vs. publication review for Class B).

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
