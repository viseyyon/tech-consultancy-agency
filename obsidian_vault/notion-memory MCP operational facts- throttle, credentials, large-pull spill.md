---
title: "notion-memory MCP operational facts: throttle, credentials, large-pull spill"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Resource"
confidence: high
durability: durable
evidence: 2
summary: "The notion-memory server (registered in claude_desktop_config.json, running from ~/mcp-servers/notion-memory/server.py) self-throttles to roughly 2.8 requests/second and must be queried sequentially,"
tags: [knowledge, mcp-tool-integration, conf/high, durable, notion, rate-limit, credentials, tool-result-spill]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# notion-memory MCP operational facts: throttle, credentials, large-pull spill

## What it is

The notion-memory server (registered in claude_desktop_config.json, running from ~/mcp-servers/notion-memory/server.py) self-throttles to roughly 2.8 requests/second and must be queried sequentially, not in parallel. Its token lives in ~/mcp-servers/notion-memory/.env and its database-id map in notion_dbs.json (overridable via NOTION_MEMORY_CONFIG). A pull large enough to exceed the single-tool-result token ceiling (roughly 100+ memory rows, ~100k+ characters) spills to a host-side temp file as one long line, which must be parsed by a script or subagent rather than read line-by-line.

## Why it matters

Querying in parallel, or assuming a large pull returns inline rather than spilling to a file Claude can't read line-by-line, both produce silent failures or truncated data.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Browser bridge and Notion MCP integration
- Cowork - notion-claude-two-way-sync

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
