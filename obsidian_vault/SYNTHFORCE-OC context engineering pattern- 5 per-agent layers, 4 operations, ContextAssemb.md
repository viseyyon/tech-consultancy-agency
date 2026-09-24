---
title: "SYNTHFORCE-OC context engineering pattern: 5 per-agent layers, 4 operations, ContextAssembler + AgentHandoff schema"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "The context engineering pattern wired into SYNTHFORCE-OC's swarm (TITAN orchestrator, SYNTH-RCA, SYNTH-PATCH, FORGE Hub gateway) defines 5 context layers per agent (Identity, Knowledge, State, Memory,"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, context-engineering, synthforce-oc, agent-handoff, pydantic]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# SYNTHFORCE-OC context engineering pattern: 5 per-agent layers, 4 operations, ContextAssembler + AgentHandoff schema

## What it is

The context engineering pattern wired into SYNTHFORCE-OC's swarm (TITAN orchestrator, SYNTH-RCA, SYNTH-PATCH, FORGE Hub gateway) defines 5 context layers per agent (Identity, Knowledge, State, Memory, Constraints) and 4 core operations (Compression, Injection, Isolation, Propagation), via a ContextAssembler class run before every agent invocation and a Pydantic AgentHandoff schema to prevent context drift. Infrastructure: Qdrant/GraphRAG for semantic memory, Redis for shared task state, 60% token-budget compression trigger. TITAN gets the full meta-context; other agents get isolated, need-to-know slices.

## Why it matters

Recurring template for wiring context management into any new agent added to the SYNTHFORCE-OC swarm.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
