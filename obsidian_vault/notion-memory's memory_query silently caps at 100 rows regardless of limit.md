---
title: "notion-memory's memory_query silently caps at 100 rows regardless of limit"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "Calling memory_query with limit=200 (or any value) against the Notion-backed memory database returns at most 100 rows and reports that count as if it were the true total; the Notion API's page_size ce"
tags: [knowledge, mcp-tool-integration, conf/high, durable, notion, pagination, mcp, data-loss]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# notion-memory's memory_query silently caps at 100 rows regardless of limit

## What it is

Calling memory_query with limit=200 (or any value) against the Notion-backed memory database returns at most 100 rows and reports that count as if it were the true total; the Notion API's page_size ceiling is not paginated through. Proven by comparing filtered counts (e.g. Category=preference returned 16 via a paginated REST pull vs 7 via memory_query), costing 42% of the real memory records on prior sync runs. The fix is to bypass memory_query for bulk pulls and hit the Notion REST API directly with page_size=100, following next_cursor until has_more is false.

## Why it matters

Trusting memory_query's row count for anything but a small filtered lookup silently discards a large fraction of the real data with no error or warning.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Cowork - notion-claude-two-way-sync run 2026-08-23

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
