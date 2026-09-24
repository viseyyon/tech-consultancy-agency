---
title: "FORGE Hub moved SYNTHFORCE-OC from embedded per-client MCP servers to a centralized hub-and-spoke topology"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "SYNTHFORCE-OC v3's FORGE Hub is a single Express.js MCP gateway (Streamable HTTP transport) hosting 47 tools across 7 servers, backed by an 11-table SQLite DB with JWT auth, scrypt password hashing, A"
tags: [knowledge, decisions-rationale, conf/high, durable, forge-hub, mcp-gateway, synthforce-oc, rbac]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# FORGE Hub moved SYNTHFORCE-OC from embedded per-client MCP servers to a centralized hub-and-spoke topology

## What it is

SYNTHFORCE-OC v3's FORGE Hub is a single Express.js MCP gateway (Streamable HTTP transport) hosting 47 tools across 7 servers, backed by an 11-table SQLite DB with JWT auth, scrypt password hashing, AES-256-GCM encrypted credential vault, and 6-tier RBAC. Distributed OpenCode clients connect via one remote MCP entry and get project-scoped credentials automatically after auth. This replaced an earlier architecture of MCP servers embedded locally per client.

## Why it matters

Centralizing to hub-and-spoke removed the need for employees to manage API keys directly and consolidated credential security in one place.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
