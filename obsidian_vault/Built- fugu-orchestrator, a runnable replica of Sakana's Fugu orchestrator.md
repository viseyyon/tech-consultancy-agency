---
title: "Built: fugu-orchestrator, a runnable replica of Sakana's Fugu orchestrator"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "Two deliverables replicate Sakana's Fugu (arXiv:2606.21228): a bilingual EN/Japanese HTML replica of the sakana.ai/fugu landing page, and fugu-orchestrator -- a ~1,950-line Python package replicating"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, fugu, sakana, orchestrator, reference-implementation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Built: fugu-orchestrator, a runnable replica of Sakana's Fugu orchestrator

## What it is

Two deliverables replicate Sakana's Fugu (arXiv:2606.21228): a bilingual EN/Japanese HTML replica of the sakana.ai/fugu landing page, and fugu-orchestrator -- a ~1,950-line Python package replicating both the Fugu and Fugu-Ultra variants (selection-head routing, soft-label SFT, GRPO-rewarded workflow orchestration with parallel tree execution) behind one OpenAI-compatible server, with 13 offline tests passing against a mock backend. The strategic hook is that this replica exposes an audit trace where Fugu itself hides routing by design, positioned as a wedge for a SYNTH-GUARD compliance-native orchestrator narrative.

## Why it matters

A concrete, tested reference implementation available to extend or demo, plus the competitive angle it was built to support.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Conversation 2026-07-31 - Jarvis build session

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
