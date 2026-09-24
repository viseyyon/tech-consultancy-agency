---
title: "Enterprise low-code agents that inherit the querying user's own permissions"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "A Copilot Studio agent connected to a 10,000-row SharePoint list, augmented with a Work IQ connector for full CRUD, is shown respecting each user's existing SharePoint permissions rather than acting u"
tags: [knowledge, mcp-tool-integration, conf/medium, durable, permissions, sharepoint, enterprise-agents, copilot-studio]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Enterprise low-code agents that inherit the querying user's own permissions

## What it is

A Copilot Studio agent connected to a 10,000-row SharePoint list, augmented with a Work IQ connector for full CRUD, is shown respecting each user's existing SharePoint permissions rather than acting under one shared service identity.

## Why it matters

Concrete example of the access-control pattern enterprise agents need before they can safely write, not just read, data.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- https://youtu.be/OdCZCvFaPtg

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
