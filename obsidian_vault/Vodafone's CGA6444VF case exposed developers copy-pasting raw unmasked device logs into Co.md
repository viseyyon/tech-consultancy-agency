---
title: "Vodafone's CGA6444VF case exposed developers copy-pasting raw unmasked device logs into Copilot"
type: knowledge-entry
domain: "Project State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 3
summary: "A Vodafone compliance query over WiFi PSK exposure in NVRAM triage logs revealed two live AI usage pathways at Vantiva: Path A is uncontrolled — developers copy-pasting raw triage logs (WiFi PSKs, cli"
tags: [knowledge, project-state, conf/high, durable, vodafone, shadow-ai, pii-exposure, copilot]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Vodafone's CGA6444VF case exposed developers copy-pasting raw unmasked device logs into Copilot

## What it is

A Vodafone compliance query over WiFi PSK exposure in NVRAM triage logs revealed two live AI usage pathways at Vantiva: Path A is uncontrolled — developers copy-pasting raw triage logs (WiFi PSKs, client MACs, WAN IPs) directly into Copilot Standard/GitHub Copilot with no redaction, audit trail, or RBAC; Path B is the AI team's governed flow — agent-mediated with field-level masking, MCP Registry content scanning, and JWT audit trails.

## Why it matters

Path A is tool-approved under AUP section 2.9.1 but data-handling non-compliant under section 2.9.3 — a real gap that was the honest finding briefed to Legal, Cloud AI, Security/VSO, and Sales.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
