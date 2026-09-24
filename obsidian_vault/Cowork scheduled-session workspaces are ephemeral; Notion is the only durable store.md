---
title: "Cowork scheduled-session workspaces are ephemeral; Notion is the only durable store"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 3
summary: "Every scheduled Cowork run gets a brand-new local_<uuid>/outputs folder; a local file such as memory/notion-sync-manifest.md or a CLAUDE.md mirror written by one run is invisible to the next. Any proc"
tags: [knowledge, agent-memory, conf/high, durable, cowork, ephemeral, notion, scheduled-tasks]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# Cowork scheduled-session workspaces are ephemeral; Notion is the only durable store

## What it is

Every scheduled Cowork run gets a brand-new local_<uuid>/outputs folder; a local file such as memory/notion-sync-manifest.md or a CLAUDE.md mirror written by one run is invisible to the next. Any process needing state across runs (a sync watermark, a rebuilt topic file) must treat Notion itself as the sole durable tier and be able to rebuild the local mirror from scratch every time, deriving watermarks from Notion's own "Last updated" fields or a dedicated Notion-resident record rather than a local manifest.

## Why it matters

Relying on a local file to carry state between scheduled fires has repeatedly produced runs that silently start from nothing, believing they have context they don't.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Cowork - notion-claude-two-way-sync
- Cowork - Notion to Claude knowledge sync

---

Part of [[MOC - Agent Memory]] · [[Home]]
