---
title: "Claude Code connects to Vantiva's Azure AI Foundry-hosted Claude models via ANTHROPIC_FOUNDRY_API_KEY or Azure Entra ID"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Claim"
confidence: medium
durability: durable
evidence: 1
summary: "Enterprise Claude access at Vantiva runs through Microsoft Foundry deployments (East US2 or Sweden Central) of Opus 4.5, Sonnet 4.5, Haiku 4.5, and Opus 4.1, via two auth paths: API key (ANTHROPIC_FOU"
tags: [knowledge, environment-tooling-state, conf/medium, durable, claude-code, azure-ai-foundry, entra-id, vantiva]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Claude Code connects to Vantiva's Azure AI Foundry-hosted Claude models via ANTHROPIC_FOUNDRY_API_KEY or Azure Entra ID

## What it is

Enterprise Claude access at Vantiva runs through Microsoft Foundry deployments (East US2 or Sweden Central) of Opus 4.5, Sonnet 4.5, Haiku 4.5, and Opus 4.1, via two auth paths: API key (ANTHROPIC_FOUNDRY_API_KEY) or Azure Entra ID (SDK default credential chain when the key is unset), the latter recommended for enterprise use. Required Azure RBAC roles are 'Azure AI User' and 'Cognitive Services User'; configuration persists via ~/.claude/settings.json and the VS Code extension settings.

## Why it matters

This is the exact connection and auth setup needed to use Claude Code with Vantiva's enterprise-hosted models, including the recommended Entra ID path and required RBAC roles.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
