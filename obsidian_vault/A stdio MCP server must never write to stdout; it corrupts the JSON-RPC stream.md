---
title: "A stdio MCP server must never write to stdout; it corrupts the JSON-RPC stream"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "The ssh-docker MCP server once printed a permissions warning straight to stdout; for a stdio-transport MCP server any stray stdout byte corrupts the JSON-RPC framing, and Claude silently drops the ser"
tags: [knowledge, mcp-tool-integration, conf/high, durable, mcp, stdio, stdout, json-rpc]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# A stdio MCP server must never write to stdout; it corrupts the JSON-RPC stream

## What it is

The ssh-docker MCP server once printed a permissions warning straight to stdout; for a stdio-transport MCP server any stray stdout byte corrupts the JSON-RPC framing, and Claude silently drops the server rather than showing the warning, so the symptom looks like a broken connector, not a log line. Fixed by moving all diagnostics to stderr and having the server auto-relock its config file to mode 600 (editing that file through file tools had been resetting it to 644, which triggered the warning in the first place).

## Why it matters

This is a general rule for any stdio MCP server, not just this one: diagnostic output on stdout produces a silent, hard-to-diagnose connector failure.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - SSH MCP server for remote deployment

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
