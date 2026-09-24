---
title: "CodeAct Pattern Cuts Agent Model Turns"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 1
summary: "Microsoft's Agent Framework demonstrates a 'CodeAct' pattern (paired with the Hyperlight micro-VM sandbox) where the agent emits executable code that chains multiple tool calls in one shot instead of"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, codeact, tool-calling, latency, agent-framework]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# CodeAct Pattern Cuts Agent Model Turns

## What it is

Microsoft's Agent Framework demonstrates a 'CodeAct' pattern (paired with the Hyperlight micro-VM sandbox) where the agent emits executable code that chains multiple tool calls in one shot instead of one model turn per tool call.

## Why it matters

Worth adopting when an agent's tool-calling loop is the main latency or cost bottleneck.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
