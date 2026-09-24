---
title: "notion-memory MCP server hangs ~4 minutes then times out when crashed, not on a query error"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 6
summary: "Across at least six sessions (July 3, 6, 16, 17), every notion-memory memory_query/memory_upsert call hitting a crashed local server hung for approximately four minutes before timing out with no respo"
tags: [knowledge, mcp-tool-integration, conf/high, durable, notion-memory, mcp-server, timeout, reliability]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# notion-memory MCP server hangs ~4 minutes then times out when crashed, not on a query error

## What it is

Across at least six sessions (July 3, 6, 16, 17), every notion-memory memory_query/memory_upsert call hitting a crashed local server hung for approximately four minutes before timing out with no response — distinct from a syntax or auth error. Retrying the identical call without restarting the server reliably reproduces the same timeout; a soft connector toggle sometimes isn't enough since a hung child process can survive it.

## Why it matters

The reliable pattern is to run a cheap memory_query first to confirm liveness before attempting a write, and fall back to saving the payload as a local markdown file in /mnt/user-data/outputs/ so nothing is lost while the server is down.

## Provenance

- Confidence **high** · durability **durable** · supported by **6** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
