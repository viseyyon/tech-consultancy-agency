---
title: "MCP servers live under ~/mcp-servers, each in its own venv; Python 3.10+ required"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Resource"
confidence: medium
durability: durable
evidence: 1
summary: "This user's local MCP servers (notion-memory, browser-bridge dependencies, etc.) live under ~/mcp-servers with a shared Python virtual environment holding mcp, httpx, playwright plus Chromium; verify."
tags: [knowledge, developer-infrastructure, conf/medium, durable, mcp-servers, python, venv, macos]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# MCP servers live under ~/mcp-servers, each in its own venv; Python 3.10+ required

## What it is

This user's local MCP servers (notion-memory, browser-bridge dependencies, etc.) live under ~/mcp-servers with a shared Python virtual environment holding mcp, httpx, playwright plus Chromium; verify.py handshakes servers over stdio. Python 3.10+ is a hard requirement for this stack; the macOS system python3 broke an earlier install attempt.

## Why it matters

Trying to run or install one of these servers against the wrong Python interpreter reproduces a known-broken setup.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Browser bridge and Notion MCP integration

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
