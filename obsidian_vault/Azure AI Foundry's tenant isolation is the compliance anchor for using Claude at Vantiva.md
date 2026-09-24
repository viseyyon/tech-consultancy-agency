---
title: "Azure AI Foundry's tenant isolation is the compliance anchor for using Claude at Vantiva"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 2
summary: "Claude is accessed via Azure AI Foundry (Microsoft's tenant-isolated infrastructure), not the public Anthropic API. This single fact is what places Claude within Vantiva's IT/VSO-approved AI vendor fa"
tags: [knowledge, decisions-rationale, conf/high, durable, compliance, azure-ai-foundry, vantiva, tenant-isolation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Azure AI Foundry's tenant isolation is the compliance anchor for using Claude at Vantiva

## What it is

Claude is accessed via Azure AI Foundry (Microsoft's tenant-isolated infrastructure), not the public Anthropic API. This single fact is what places Claude within Vantiva's IT/VSO-approved AI vendor family, since the approved tools list (Copilot, O365 Copilot, etc.) is built entirely around the Microsoft/Azure vendor family. Public Claude, ChatGPT, Cursor, and Gemini direct access remain explicitly unapproved.

## Why it matters

Explains why Claude is compliant to use at Vantiva while other AI tools are not — using any non-Foundry Claude access would break that compliance basis.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
