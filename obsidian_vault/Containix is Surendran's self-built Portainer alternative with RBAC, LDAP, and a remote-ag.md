---
title: "Containix is Surendran's self-built Portainer alternative with RBAC, LDAP, and a remote-agent architecture"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 5
summary: "Containix is a vibe-coded Docker management UI (React frontend + Node.js backend) built as a Portainer replacement, with in-browser container terminal access (node-pty/WebSocket), three-tier RBAC (Adm"
tags: [knowledge, project-state, conf/medium, durable, containix, docker, portainer-alternative, rbac]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Containix is Surendran's self-built Portainer alternative with RBAC, LDAP, and a remote-agent architecture

## What it is

Containix is a vibe-coded Docker management UI (React frontend + Node.js backend) built as a Portainer replacement, with in-browser container terminal access (node-pty/WebSocket), three-tier RBAC (Admin/Operator or Developer/Viewer, demo creds admin/admin123), LDAP integration, and a lightweight 'Containix Agent' Node.js service on remote Docker hosts reporting containers/images/networks/volumes over WebSocket. As of these sessions it was still prototype-stage: in-memory/localStorage persistence, fake/random container data on remote-server connect, and a repeatedly-breaking 'Add Server' button and remote-container listing.

## Why it matters

Still prototype-stage — remote-server features (Add Server, real container listing) are known to be broken/faked, not production-ready yet.

## Provenance

- Confidence **medium** · durability **durable** · supported by **5** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
