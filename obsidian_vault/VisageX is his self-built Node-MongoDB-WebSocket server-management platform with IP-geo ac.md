---
title: "VisageX is his self-built Node/MongoDB/WebSocket server-management platform with IP/geo activity tracking"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 4
summary: "VisageX began as an 'Enterprise Server Management Dashboard' (heartbeat via nslookup, CPU/memory/storage per server, Docker container/image management with browser terminal, role-based auth) and was r"
tags: [knowledge, project-state, conf/medium, durable, visagex, server-management, mongodb, security-monitoring]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# VisageX is his self-built Node/MongoDB/WebSocket server-management platform with IP/geo activity tracking

## What it is

VisageX began as an 'Enterprise Server Management Dashboard' (heartbeat via nslookup, CPU/memory/storage per server, Docker container/image management with browser terminal, role-based auth) and was renamed VisageX after adding per-user IP tracking via nslookup, geographic location mapping, and 'impossible travel' login detection. Backend: Node.js/Express on port 4000, MongoDB (Mongoose), WebSocket for real-time updates; agents register via POST /api/agents/register. Production instance is on Vantiva-internal IP ranges (10.x.x.x) and has hit MongoDB connectivity/DNS issues (hostname 'mongodb' unresolvable, ECONNREFUSED to 10.17.58.118:27017).

## Why it matters

Known production issue: MongoDB connectivity/DNS resolution has failed on the live instance, which would need fixing before relying on it.

## Provenance

- Confidence **medium** · durability **durable** · supported by **4** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
