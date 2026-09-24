---
title: "Context Engineering for Long-Running Agents"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 2
summary: "Two sources converge on the same practice: LangChain's Deep Agents docs describe deliberately curating what context a long-running agent keeps in-window (offloading, summarizing, pruning) rather than"
tags: [knowledge, agent-memory, conf/medium, durable, context-engineering, long-running-agents, memory, pruning]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# Context Engineering for Long-Running Agents

## What it is

Two sources converge on the same practice: LangChain's Deep Agents docs describe deliberately curating what context a long-running agent keeps in-window (offloading, summarizing, pruning) rather than letting it accumulate, and a separate guide frames this as 'context engineering' - a discipline distinct from prompt engineering.

## Why it matters

Long-running or multi-step agents degrade once their context window fills with stale history, so active context management is a load-bearing design decision.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- https://docs.langchain.com/oss/python/deepagents/context-engineering
- https://machinelearningmastery.com/effective-context-engineering-for-ai-agents-a-developers-guide

---

Part of [[MOC - Agent Memory]] · [[Home]]
