---
title: "FORGE Hub is Vantiva's production MCP gateway: 106 tools, 7 servers, 6-tier RBAC"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 2
summary: "FORGE Hub is a centralized MCP gateway built on Express.js managing 106 tools across 7 MCP servers, using JWT authentication, AES-256-GCM vault encryption, and a 6-tier RBAC system mapped to Vantiva e"
tags: [knowledge, mcp-tool-integration, conf/high, durable, forge-hub, mcp-gateway, rbac, jwt]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# FORGE Hub is Vantiva's production MCP gateway: 106 tools, 7 servers, 6-tier RBAC

## What it is

FORGE Hub is a centralized MCP gateway built on Express.js managing 106 tools across 7 MCP servers, using JWT authentication, AES-256-GCM vault encryption, and a 6-tier RBAC system mapped to Vantiva engineering roles, hosted on Azure Container Apps (deployed via azd+Bicep). Its closest open-source peer is IBM ContextForge; other adjacent tools include Obot, Lunar.dev MCPX, and Microsoft MCP Gateway.

## Why it matters

Its differentiators are vertical integration with the internal agent fleet, domain-curated tool taxonomy for RDK-B/Yocto/Jenkins/Gerrit, and coupling to SynthCode and the IronCore Gerrit migration.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
