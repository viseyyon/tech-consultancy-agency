---
title: "Built a custom, non-invasive MCP server for an existing self-hosted JFrog Artifactory + LDAP deployment"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "Rather than a from-scratch JFrog setup, built an MCP server that auto-discovers and connects to an already-running, LDAP-linked, data-populated JFrog Artifactory Docker container without disrupting it"
tags: [knowledge, mcp-tool-integration, conf/high, durable, mcp, jfrog-artifactory, ldap, non-invasive]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Built a custom, non-invasive MCP server for an existing self-hosted JFrog Artifactory + LDAP deployment

## What it is

Rather than a from-scratch JFrog setup, built an MCP server that auto-discovers and connects to an already-running, LDAP-linked, data-populated JFrog Artifactory Docker container without disrupting it. Delivered design has 15+ tools covering discovery/health, repository and user management, LDAP sync, and full config/data export-backup.

## Why it matters

Establishes a pattern of preferring non-invasive integration over reconfiguring existing infrastructure.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
