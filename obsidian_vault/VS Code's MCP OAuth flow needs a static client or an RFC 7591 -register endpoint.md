---
title: "VS Code's MCP OAuth flow needs a static client or an RFC 7591 /register endpoint"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "VS Code's MCP OAuth client attempts Dynamic Client Registration (RFC 7591) against the auth server, expecting a /register endpoint that returns a client_id on demand. FORGE Hub's auth server (10.17.58"
tags: [knowledge, mcp-tool-integration, conf/high, durable, vs-code, mcp, oauth, rfc-7591]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# VS Code's MCP OAuth flow needs a static client or an RFC 7591 /register endpoint

## What it is

VS Code's MCP OAuth client attempts Dynamic Client Registration (RFC 7591) against the auth server, expecting a /register endpoint that returns a client_id on demand. FORGE Hub's auth server (10.17.58.140:9400) doesn't expose one, so VS Code falls back to asking for a manually supplied client_id and needs two redirect URIs whitelisted (http://127.0.0.1:33418 and https://vscode.dev/redirect).

## Why it matters

The durable fix for team scale (12 engineers) is implementing a full RFC 7591 /register endpoint on the FORGE Hub auth layer for self-provisioning, rather than registering static OAuth clients one at a time.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
