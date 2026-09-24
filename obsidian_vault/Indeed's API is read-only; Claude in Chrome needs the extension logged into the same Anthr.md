---
title: "Indeed's API is read-only; Claude in Chrome needs the extension logged into the same Anthropic account"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "The Indeed MCP tool (`get_resume`) could retrieve full profile data but could not write changes — profile edits must be made manually at profile.indeed.com. Claude in Chrome (browser MCP) connectivity"
tags: [knowledge, mcp-tool-integration, conf/high, durable, indeed, claude-in-chrome, mcp-limitations, browser-automation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Indeed's API is read-only; Claude in Chrome needs the extension logged into the same Anthropic account

## What it is

The Indeed MCP tool (`get_resume`) could retrieve full profile data but could not write changes — profile edits must be made manually at profile.indeed.com. Claude in Chrome (browser MCP) connectivity requires the Chrome extension to be active and signed into the same Anthropic account as the current session; when disconnected, both `tabs_context_mcp` and `switch_browser` return connection errors.

## Why it matters

The workaround used when Chrome MCP was disconnected was generating a detailed prompt for the Comet browser agent instead of direct browser automation — a fallback worth reusing when this connectivity issue recurs.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
