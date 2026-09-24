---
title: "Atlassian's official Jira/Confluence MCP connector is GA but unauthorized here"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Claim"
confidence: medium
durability: ephemeral
evidence: 1
summary: "The official Atlassian remote MCP server (OAuth 2.1, cross-project JQL search, CQL search, bulk issue ops) went GA in February 2026 with Claude as a launch partner, and its rate limits follow the org'"
tags: [knowledge, environment-tooling-state, conf/medium, ephemeral, atlassian, jira, confluence, connector-blocked]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Atlassian's official Jira/Confluence MCP connector is GA but unauthorized here

## What it is

The official Atlassian remote MCP server (OAuth 2.1, cross-project JQL search, CQL search, bulk issue ops) went GA in February 2026 with Claude as a launch partner, and its rate limits follow the org's own Jira/Confluence Cloud plan tier rather than an MCP-imposed limit. As of the last check it still shows as unauthorized in this user's setup, a hard blocker on any live, connector-based Jira/Confluence pull; direct API/PAT access has been used instead.

## Why it matters

Assuming the Atlassian connector is available because it's GA, rather than checking authorization status, leads to planning work around a tool that isn't actually usable yet.

## Provenance

- Confidence **medium** · durability **ephemeral** · supported by **1** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- MLOps capstone (predictive maintenance)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
