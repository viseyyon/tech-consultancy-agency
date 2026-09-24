---
title: "ML priority scoring (10x error + 3x network + 2x state + 2x timestamp) compressed 487MB logs to 1.2MB"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "To fix specialized RCA agents exceeding the 200K token context limit (208K tokens), built a token budget manager allocating 60% logs/20% configs/20% code, with ML priority-weighted log-line filtering"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, rca, token-budget, log-compression, context-window]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# ML priority scoring (10x error + 3x network + 2x state + 2x timestamp) compressed 487MB logs to 1.2MB

## What it is

To fix specialized RCA agents exceeding the 200K token context limit (208K tokens), built a token budget manager allocating 60% logs/20% configs/20% code, with ML priority-weighted log-line filtering (score = 10x error-keywords + 3x network + 2x state + 2x timestamp) that strips heartbeats/debug spam. Achieved 99.8% compression (487MB to 1.2MB) with claimed 100% critical-data preservation, cutting RCA turnaround from 2-4 hours to 3-6 minutes.

## Why it matters

Reusable technique for keeping large log sets within LLM context limits without losing high-signal lines.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
