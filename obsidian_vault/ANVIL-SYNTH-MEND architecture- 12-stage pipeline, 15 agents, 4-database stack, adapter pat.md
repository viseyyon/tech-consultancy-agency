---
title: "ANVIL/SYNTH-MEND architecture: 12-stage pipeline, 15 agents, 4-database stack, adapter pattern"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "ANVIL (commercial name) / SYNTH-MEND (internal codename) is the autonomous defect-resolution platform for Comcast's RDK-B Condor 5G gateway codebase: a 12-stage pipeline with three feedback loops and"
tags: [knowledge, decisions-rationale, conf/high, durable, anvil, synth-mend, rdk-b, condor]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# ANVIL/SYNTH-MEND architecture: 12-stage pipeline, 15 agents, 4-database stack, adapter pattern

## What it is

ANVIL (commercial name) / SYNTH-MEND (internal codename) is the autonomous defect-resolution platform for Comcast's RDK-B Condor 5G gateway codebase: a 12-stage pipeline with three feedback loops and 15 Foundry-style agents, backed by a 4-database stack (PostgreSQL, Neo4j, Qdrant, Azure AI Search/OpenSearch) and 6 RBAC roles. Pluggability across products/frameworks comes via Product Profiles plus an 18-adapter Adapter Pattern and Policy Engine, a 5-layer configuration hierarchy, and a per-run 'run_memory' brain for context continuity; cloud (Azure-native) and on-prem (Kubernetes+Jenkins+Gerrit) deployment prompts were kept as two separate documents rather than one with conditionals.

## Why it matters

The deliberate cloud/on-prem prompt split is a reusable lesson for any future dual-deployment agent design — conditionals inside one prompt were judged worse than two clean documents.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
