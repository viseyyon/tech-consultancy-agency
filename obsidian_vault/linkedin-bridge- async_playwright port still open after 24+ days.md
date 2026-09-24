---
title: "linkedin-bridge: async_playwright port still open after 24+ days"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: ephemeral
evidence: 2
summary: "linkedin-bridge has failed every tool call since 2026-07-30 (reconfirmed on at least 13 separate dates through 2026-08-23) with a Playwright sync-API-inside-asyncio fault -- a bridge-wide transport fa"
tags: [knowledge, developer-infrastructure, conf/high, ephemeral, linkedin-bridge, playwright, async, blocked]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# linkedin-bridge: async_playwright port still open after 24+ days

## What it is

linkedin-bridge has failed every tool call since 2026-07-30 (reconfirmed on at least 13 separate dates through 2026-08-23) with a Playwright sync-API-inside-asyncio fault -- a bridge-wide transport fault, not a login/2FA problem, so the 2FA step can't even be reached. The fix is a mechanical port of server.py from sync_playwright to async_playwright with awaited page/context calls; until then it blocks Phase 2 of notion-claude-two-way-sync (which degrades cleanly), and given 24 consecutive confirmations with no code change, the recommendation is to disable that leg rather than keep re-confirming a known fault twice a day.

## Why it matters

A long-standing, precisely-diagnosed blocker with a known one-line-class fix that keeps getting re-discovered instead of scheduled.

## Provenance

- Confidence **high** · durability **ephemeral** · supported by **2** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- Cowork - Notion to Claude knowledge sync
- Cowork - Browser bridge and Notion MCP integration

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
