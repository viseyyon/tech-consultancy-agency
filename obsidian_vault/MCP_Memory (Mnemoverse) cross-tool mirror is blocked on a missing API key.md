---
title: "MCP_Memory (Mnemoverse) cross-tool mirror is blocked on a missing API key"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Caveat"
confidence: medium
durability: ephemeral
evidence: 1
summary: "The MCP_Memory server would give memory shared across Claude, ChatGPT, Cursor and VS Code via memory_write/memory_read/memory_stats, but every call currently fails with 'MNEMOVERSE_API_KEY is required"
tags: [knowledge, agent-memory, conf/medium, ephemeral, mnemoverse, cross-tool-memory, blocked, api-key]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# MCP_Memory (Mnemoverse) cross-tool mirror is blocked on a missing API key

## What it is

The MCP_Memory server would give memory shared across Claude, ChatGPT, Cursor and VS Code via memory_write/memory_read/memory_stats, but every call currently fails with "MNEMOVERSE_API_KEY is required for this operation." Until a free key from console.mnemoverse.com is obtained and set in the MCP client config, the Notion mirror plus local memory/ files remain the only two copies, and the sync task skips this leg with a one-line note rather than failing.

## Why it matters

Not knowing this is blocked leads to assuming cross-tool memory sync is happening when it silently is not.

## Provenance

- Confidence **medium** · durability **ephemeral** · supported by **1** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- Cowork - Notion to Claude knowledge sync

---

Part of [[MOC - Agent Memory]] · [[Home]]
