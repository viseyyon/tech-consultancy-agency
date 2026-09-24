---
title: "BuildPulse: distributed embedded-build monitoring uses per-container agents reporting to a central hub"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: medium
durability: durable
evidence: 1
summary: "For monitoring Docker containers building Android TV/RDK/OpenWrt binaries, the design converged (after two earlier iterations, BuildGuardian and BuildSentinel) on BuildPulse: a lightweight agent injec"
tags: [knowledge, decisions-rationale, conf/medium, durable, buildpulse, docker-monitoring, embedded-builds, architecture-decision]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# BuildPulse: distributed embedded-build monitoring uses per-container agents reporting to a central hub

## What it is

For monitoring Docker containers building Android TV/RDK/OpenWrt binaries, the design converged (after two earlier iterations, BuildGuardian and BuildSentinel) on BuildPulse: a lightweight agent injected into each existing container reports build phase, metrics, issues, and resource usage over WebSocket to a central FastAPI hub, which persists to Redis/PostgreSQL/InfluxDB and renders a real-time dashboard. The key decision was per-container lightweight agents plus central aggregation, rather than a single custom monitoring container, because the Docker images already existed and couldn't be rebuilt from scratch.

## Why it matters

This architecture works within the constraint of pre-existing, unmodifiable build container images rather than requiring a rebuild.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
