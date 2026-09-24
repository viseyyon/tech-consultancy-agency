---
title: "HERMES NEXUS splits into a <100KB dependency-free client agent and a heavy RAG/DB Docker Compose server"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Decision"
confidence: medium
durability: durable
evidence: 2
summary: "To support multi-project RCA analysis across Docker/VM environments without installing ML dependencies client-side, HERMES NEXUS splits into a lightweight (~50KB, zero-ML-dependency) Python agent coll"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, hermes-nexus, rca, architecture, client-server-split]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# HERMES NEXUS splits into a <100KB dependency-free client agent and a heavy RAG/DB Docker Compose server

## What it is

To support multi-project RCA analysis across Docker/VM environments without installing ML dependencies client-side, HERMES NEXUS splits into a lightweight (~50KB, zero-ML-dependency) Python agent collecting git metadata, build logs, environment info, and JIRA context shipped via compressed HTTPS to a server stack (Qdrant, Neo4j, MongoDB, Redis, PostgreSQL, MinIO, embedding service, 7 LangGraph-orchestrated AI workers). Projected speed: 60-80 min analysis down to 12-15 min first-run / 3-8 min cached, with incremental re-indexing (2-30 sec) using freshness-decay weighting (FRESH <7d = 1.0x, RECENT 7-30d = 0.8x, AGING 30-90d = 0.5x).

## Why it matters

This split lets RCA run in environments where installing heavy ML dependencies isn't viable, while projecting a large turnaround-time reduction.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
