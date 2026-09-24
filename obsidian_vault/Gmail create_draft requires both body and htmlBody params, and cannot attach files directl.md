---
title: "Gmail create_draft requires both body and htmlBody params, and cannot attach files directly"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "Gmail's create_draft tool requires both body and htmlBody parameters -- supplying only one causes formatting loss when the draft renders in Gmail. It also has no native attachment support, requiring t"
tags: [knowledge, mcp-tool-integration, conf/medium, durable, gmail, mcp, create-draft, attachments]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Gmail create_draft requires both body and htmlBody params, and cannot attach files directly

## What it is

Gmail's create_draft tool requires both body and htmlBody parameters -- supplying only one causes formatting loss when the draft renders in Gmail. It also has no native attachment support, requiring the user to manually attach files after draft creation. Gmail:search_threads with 'from:X OR to:X' reliably surfaces prior correspondence, and Gmail:list_drafts with a 'to:X' filter helps deduplicate repeated draft-creation attempts by finding the newest one.

## Why it matters

Skipping either body param silently degrades draft formatting, and file attachments must always be flagged as a manual follow-up step for the user.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
