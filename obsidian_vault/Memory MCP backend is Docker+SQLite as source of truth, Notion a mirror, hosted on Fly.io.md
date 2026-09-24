---
title: "Memory MCP backend is Docker+SQLite as source of truth, Notion a mirror, hosted on Fly.io"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 3
summary: "For a standalone memory-context MCP server design, the council unanimously rejected Notion as the primary backend (roughly 3 requests/second, no full-text search) and rejected Vercel as a host (server"
tags: [knowledge, agent-memory, conf/high, durable, memory-mcp, sqlite, notion, fly-io]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# Memory MCP backend is Docker+SQLite as source of truth, Notion a mirror, hosted on Fly.io

## What it is

For a standalone memory-context MCP server design, the council unanimously rejected Notion as the primary backend (roughly 3 requests/second, no full-text search) and rejected Vercel as a host (serverless timeouts fight persistent MCP streaming connections). SQLite in a Docker container is the system of record; a notion_sync.py script does incremental watermarked upserts and a compose service mirrors to Notion every 15 minutes, with Litestream providing continuous S3 replication. Fly.io was chosen to host it as an always-on machine (auto-stop explicitly disabled, since cold starts break MCP connections) over Oracle Cloud Always Free (runner-up) and rejected options Render free tier, Cloud Run, and Railway. The three Notion table schemas that this system and others must match exactly are fixed: Memory (Fact/Category/Details/Source/Last updated), Tasks (Task/Status/Priority/Due/Source), Contacts (Name/Company-Role/Last message summary/Last contact/Status/Follow-up).

## Why it matters

This is a different, standalone memory-MCP design from the notion-memory server actually in use for this knowledge base - anyone building or resuming it needs the backend/host choice and the exact schema contract.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Memory context MCP architecture
- Browser bridge and Notion MCP integration

---

Part of [[MOC - Agent Memory]] · [[Home]]
