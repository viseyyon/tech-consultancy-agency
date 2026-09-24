---
title: "Jane Agent: one physical model, logical expert swarm, replay-based graduation gate"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "Jane (a dual-AI local-mentor/cloud-mentee agent project) keeps its 'expert swarm' logical rather than physical - experts are swapped prompts with KV-prefix caching behind an inference semaphore, so pa"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, jane-agent, local-inference, capability-gating, oss-reuse]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Jane Agent: one physical model, logical expert swarm, replay-based graduation gate

## What it is

Jane (a dual-AI local-mentor/cloud-mentee agent project) keeps its 'expert swarm' logical rather than physical - experts are swapped prompts with KV-prefix caching behind an inference semaphore, so parallel workers never contend for the single local GPU, and an Expert Factory can propose new specialists on probation with scope-overlap guards rather than deploying them live immediately. All three council models independently named its Escalation Replay Benchmark - a held-out set of past escalations plus a post-graduation canary shadow-review - as the standout design decision gating when a capability is trusted to run unsupervised. The project also deliberately reuses four existing Apache-2.0 projects for defined narrow roles (a mentee-amplifier bypassed on tool-calling turns, a context economizer library, a read-only workspace knowledge graph, and a prompt-pattern donor) rather than building equivalents from scratch, with SQLite/FTS5 as the sole system of record under a single-writer queue and mentor-wins merge policy.

## Why it matters

Captures both the resource-constraint workaround (one GPU) and the safety gate (replay benchmark) that define how Jane is allowed to grow capability.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Jane Agent development plan

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
