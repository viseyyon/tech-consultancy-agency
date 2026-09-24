---
title: "Krno (formerly OpsCentral Alert Hub) is Surendran's maintenance-notification app with team-based routing rules"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 2
summary: "Krno (formerly OpsCentral Alert Hub) is an enterprise maintenance/outage notification system spanning geographies (Americas, EMEA, APAC) and services (GitLab, Bitbucket, Gerrit, Gitolite, Artifactory,"
tags: [knowledge, project-state, conf/high, durable, krno, notification-system, outage-alerting, postgresql]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Krno (formerly OpsCentral Alert Hub) is Surendran's maintenance-notification app with team-based routing rules

## What it is

Krno (formerly OpsCentral Alert Hub) is an enterprise maintenance/outage notification system spanning geographies (Americas, EMEA, APAC) and services (GitLab, Bitbucket, Gerrit, Gitolite, Artifactory, build servers, LDAP/AD, VPN). Routing logic: IT/Network teams auto-select affected applications for a geography and trigger a generic broadcast; Tools and Security teams manually select applications and notify only that specific application's team; DevOps routes to a completely separate mailing list. Stack is PostgreSQL, Redis, Node/Express, Nginx, Docker Compose, with JWT auth and Admin/Lead/Operator roles.

## Why it matters

This is a distinct named product (not part of the SYNTHFORCE-OC family) built for operational notification routing, worth distinguishing from his other Vantiva AI systems.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
