---
title: "Gmail:create_draft hits an unclearing connector-level approval gate; its API also can't attach files"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "Gmail:create_draft with a replyToMessageId was blocked at the connector level with a 'no approval received' error that did not clear even after explicit chat confirmation, suggesting the gate needs a"
tags: [knowledge, mcp-tool-integration, conf/medium, durable, gmail, mcp, connector-bug, approval-gate]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Gmail:create_draft hits an unclearing connector-level approval gate; its API also can't attach files

## What it is

Gmail:create_draft with a replyToMessageId was blocked at the connector level with a 'no approval received' error that did not clear even after explicit chat confirmation, suggesting the gate needs a separate client-UI approval action rather than a chat-level yes, or reflects a scope/permission limitation specific to reply-draft creation. Gmail's draft API also does not support attachments regardless.

## Why it matters

A chat-level confirmation is not sufficient to clear this connector gate; expect to need a client-UI approval action, and always plan for manual attachment after draft creation.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
