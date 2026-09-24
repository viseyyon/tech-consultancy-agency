---
title: "Jane Agent: dual-AI local agent project, build-ready at v7"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 1
summary: "Jane Agent pairs a local mentee model with a cloud mentor on the Hermes framework, using a logical (not physical) expert swarm -- experts are swapped prompts with KV prefix caching and an inference se"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, jane-agent, local-llm, hermes, design]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Jane Agent: dual-AI local agent project, build-ready at v7

## What it is

Jane Agent pairs a local mentee model with a cloud mentor on the Hermes framework, using a logical (not physical) expert swarm -- experts are swapped prompts with KV prefix caching and an inference semaphore so parallel workers share one model in VRAM rather than needing multiple GPUs. It reuses four Apache-2.0 OSS projects in defined roles (optillm as mentee amplifier, headroom as context economizer, graphify as read-only knowledge graph, Raven as pattern donor only) and gates capability graduation on an Escalation Replay Benchmark with a hold-out split and post-graduation canary shadow-review. Design is complete and council-validated; it is awaiting a build session, not yet implemented.

## Why it matters

Captures Jane's full design state so a build session picks up from v7 rather than re-deriving the architecture.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Conversation 2026-07-29 - Jane Agent development plan

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
