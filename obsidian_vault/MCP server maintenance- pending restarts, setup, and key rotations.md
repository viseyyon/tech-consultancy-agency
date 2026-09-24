---
title: "MCP server maintenance: pending restarts, setup, and key rotations"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: ephemeral
evidence: 4
summary: "Two ssh-docker MCP fixes (12-session pool size, host 'asta' use_pty plus v7 stdout/stderr hardening) are on disk but need a full Claude Desktop restart to take effect, since the running server cannot"
tags: [knowledge, developer-infrastructure, conf/high, ephemeral, mcp, ssh-docker, notion-memory, credentials]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# MCP server maintenance: pending restarts, setup, and key rotations

## What it is

Two ssh-docker MCP fixes (12-session pool size, host 'asta' use_pty plus v7 stdout/stderr hardening) are on disk but need a full Claude Desktop restart to take effect, since the running server cannot hot-reload config. Separately, notion-memory has no .env or notion_dbs.json yet -- it needs a Notion integration token, a bootstrap.py run against a parent page, and doctor.py --write before first use. Two credential-hygiene items are also outstanding: an AZURE_FOUNDRY_API_KEY sitting unencrypted in claude_desktop_config.json's browser-bridge block, and a plaintext SSH password for host 'project' in hosts.json that should move to key_path.

## Why it matters

A checklist of small but concrete local-environment fixes needed before these MCP servers are fully operational and hardened.

## Provenance

- Confidence **high** · durability **ephemeral** · supported by **4** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- Cowork - SSH MCP server for remote deployment
- Cowork - Browser bridge and Notion MCP integration
- Cowork - MCP server browser integration

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
