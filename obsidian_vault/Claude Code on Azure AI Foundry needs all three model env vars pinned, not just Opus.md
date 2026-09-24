---
title: "Claude Code on Azure AI Foundry needs all three model env vars pinned, not just Opus"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "ANTHROPIC_DEFAULT_OPUS_MODEL, ANTHROPIC_DEFAULT_SONNET_MODEL, and ANTHROPIC_DEFAULT_HAIKU_MODEL must all be pinned to exact Foundry deployment names. Leaving any unpinned lets Claude Code fall back to"
tags: [knowledge, environment-tooling-state, conf/high, durable, azure-ai-foundry, claude-code, model-pinning, environment-variables]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Claude Code on Azure AI Foundry needs all three model env vars pinned, not just Opus

## What it is

ANTHROPIC_DEFAULT_OPUS_MODEL, ANTHROPIC_DEFAULT_SONNET_MODEL, and ANTHROPIC_DEFAULT_HAIKU_MODEL must all be pinned to exact Foundry deployment names. Leaving any unpinned lets Claude Code fall back to a model alias that may not exist in the Foundry account, breaking existing users on a new Anthropic release. Verify with `/status` in Claude Code.

## Why it matters

An unpinned model variable can silently break Claude Code for all users at the next Anthropic model release.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
