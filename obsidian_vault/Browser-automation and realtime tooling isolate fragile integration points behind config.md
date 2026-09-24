---
title: "Browser-automation and realtime tooling isolate fragile integration points behind config"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 3
summary: "Components that drive another system's UI or a live socket keep the fragile parts swappable without a rewrite: the Gemini browser driver keeps its DOM selectors in an external config.json and the Link"
tags: [knowledge, mcp-tool-integration, conf/medium, durable, dom-selectors, websocket, systemd, m365-connector]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Browser-automation and realtime tooling isolate fragile integration points behind config

## What it is

Components that drive another system's UI or a live socket keep the fragile parts swappable without a rewrite: the Gemini browser driver keeps its DOM selectors in an external config.json and the LinkedIn bridge keeps an ordered-fallback SELECTORS dict, so a target site's UI change is a config edit rather than code surgery. On the Anvil project, three related realtime-transport bugs were fixed together: the socket.io server package had never actually been installed (pinned to 4.8.3 to match the client), nothing supervised the websocket server process (now a proper user systemd unit with linger), and the frontend had a hardcoded fallback to a specific production host instead of deriving it from window.location. Separately, the Microsoft 365 connector was confirmed to cover Teams and Outlook reads directly, leaving the custom teams-mcp server needed only for write operations.

## Why it matters

Small but concrete integration lessons - where to expect drift (selectors) and what 'it just needs a restart' bugs actually turn out to be (unsupervised process, hardcoded host).

## Provenance

- Confidence **medium** · durability **durable** · supported by **3** archived item(s).

## Sources

- Anvil project analysis
- Codebase documentation generator
- MCP server for Teams

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
