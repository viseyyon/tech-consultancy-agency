---
title: "ssh-docker MCP: version pin, slow handshake, and no config hot-reload"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "The ssh-docker MCP server's install pins mcp<2.0.0 because 2.0.0 broke the FastMCP import. Its initialize handshake normally takes roughly 15 seconds; a strict startup timeout will falsely mark it as"
tags: [knowledge, mcp-tool-integration, conf/high, durable, ssh-docker, mcp, hot-reload, timeout]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# ssh-docker MCP: version pin, slow handshake, and no config hot-reload

## What it is

The ssh-docker MCP server's install pins mcp<2.0.0 because 2.0.0 broke the FastMCP import. Its initialize handshake normally takes roughly 15 seconds; a strict startup timeout will falsely mark it as failed even though the server is fine. Editing its hosts.json (e.g. raising a host's pool_size) does not take effect in a running server, since the in-memory pool object was created at startup, so a full Claude Desktop restart (or connector toggle) is required to reread the config.

## Why it matters

Misreading any of these three as "the server is broken" leads to wasted debugging of a server that is actually working as designed.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Cowork - SSH MCP server for remote deployment

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
