---
title: "Council fan-out via browser-bridge must run sequentially, never in parallel"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "Firing ask_gemini/ask_chatgpt/ask_kimi (or ask_all) together in one block previously killed the shared browser context and forced an MCP server restart. Council queries must be issued one at a time; a"
tags: [knowledge, mcp-tool-integration, conf/high, durable, browser-bridge, council, concurrency, mcp]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Council fan-out via browser-bridge must run sequentially, never in parallel

## What it is

Firing ask_gemini/ask_chatgpt/ask_kimi (or ask_all) together in one block previously killed the shared browser context and forced an MCP server restart. Council queries must be issued one at a time; ask_all should be avoided since it exceeds the client timeout.

## Why it matters

Ignoring this reproduces a known crash that takes down the browser-bridge MCP server for every tool relying on it.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Content implementation architecture

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
