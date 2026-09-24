---
title: "Azure AI Foundry's Anthropic endpoint requires the x-api-key header, not api-key or Bearer"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "For the Azure AI Foundry Anthropic-compatible endpoint (base https://<resource>.services.ai.azure.com/anthropic/, messages endpoint {base}/v1/messages), `api-key` returns 401; `x-api-key` and `Authori"
tags: [knowledge, environment-tooling-state, conf/high, durable, azure-ai-foundry, anthropic-api, authentication, endpoint]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Azure AI Foundry's Anthropic endpoint requires the x-api-key header, not api-key or Bearer

## What it is

For the Azure AI Foundry Anthropic-compatible endpoint (base https://<resource>.services.ai.azure.com/anthropic/, messages endpoint {base}/v1/messages), `api-key` returns 401; `x-api-key` and `Authorization: Bearer` both return 200. `anthropic-version: 2023-06-01` is also required, and responses follow Anthropic's typed content-block Messages API format, not OpenAI's `choices[0].message.content`.

## Why it matters

Using the wrong auth header or expecting OpenAI-shaped responses will break any Foundry-Anthropic integration.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
