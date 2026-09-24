---
title: "notion-memory: memory_query OK but memory_upsert timeout means a write-token issue, not a crashed server"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "When notion-memory's memory_query (read) succeeds quickly but memory_upsert (write) hangs ~4 minutes on repeated attempts, the diagnosis is an expired/under-scoped Notion integration token or an upser"
tags: [knowledge, mcp-tool-integration, conf/high, durable, notion-memory, mcp, timeout, diagnosis]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# notion-memory: memory_query OK but memory_upsert timeout means a write-token issue, not a crashed server

## What it is

When notion-memory's memory_query (read) succeeds quickly but memory_upsert (write) hangs ~4 minutes on repeated attempts, the diagnosis is an expired/under-scoped Notion integration token or an upsert handler missing a timeout on its Notion API call — not a crashed local MCP server process. Reads can serve from cache while writes fail silently server-side.

## Why it matters

Points troubleshooting at the write-path/token issue instead of wastefully restarting the connector.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
