---
title: "Vantiva's Claude Code to Azure Foundry bridge needs no trailing slash and explicit Sonnet/Haiku model pins"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "The Claude Code-via-Azure-AI-Foundry setup (resource seren-9157-resource, model alias claude-fable-5) has verified gotchas: the base URL must be https://{resource}.services.ai.azure.com/anthropic with"
tags: [knowledge, environment-tooling-state, conf/high, durable, claude-code, azure-foundry, configuration, model-pinning]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Vantiva's Claude Code to Azure Foundry bridge needs no trailing slash and explicit Sonnet/Haiku model pins

## What it is

The Claude Code-via-Azure-AI-Foundry setup (resource seren-9157-resource, model alias claude-fable-5) has verified gotchas: the base URL must be https://{resource}.services.ai.azure.com/anthropic with no trailing slash; pinning only ANTHROPIC_DEFAULT_OPUS_MODEL is insufficient since the main agent loop and background tasks also need Sonnet and Haiku aliases pinned; the Foundry deployment name must match an actual deployment in a supported region (East US 2 or Sweden Central); and CLI version ~2.0.42 had a known bug silently ignoring Foundry environment variables entirely.

## Why it matters

Each of these silently breaks the bridge without a clear error, so they're the first things to check when a Foundry-routed Claude Code setup misbehaves; Entra ID auth via az login is the more secure alternative to a static API key.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
