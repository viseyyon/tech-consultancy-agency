---
title: "EDGE PULSE (Vantiva's internal AI newsletter) assigns a different Claude model to each of 8 agents by task complexity"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "EDGE PULSE is Vantiva's internal AI newsletter, run as an 8-agent pipeline (MERCURY orchestrator, HERMES fetcher, ATHENA curator, CALLIOPE writer, ARGUS validator, APOLLO editor, IRIS visual, VULCAN r"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, edge-pulse, multi-agent, model-routing, azure-ai-foundry]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# EDGE PULSE (Vantiva's internal AI newsletter) assigns a different Claude model to each of 8 agents by task complexity

## What it is

EDGE PULSE is Vantiva's internal AI newsletter, run as an 8-agent pipeline (MERCURY orchestrator, HERMES fetcher, ATHENA curator, CALLIOPE writer, ARGUS validator, APOLLO editor, IRIS visual, VULCAN renderer) on Azure AI Foundry. Production model assignment: ATHENA uses claude-sonnet-4-5, CALLIOPE uses claude-opus-4-6, APOLLO uses claude-opus-4-5-5, IRIS uses claude-haiku-4-5, with a fallback chain iterating alternatives on 404 for graceful degradation.

## Why it matters

A working reference architecture for task-specific model assignment across an agent pipeline, including a concrete fallback strategy for model unavailability.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
