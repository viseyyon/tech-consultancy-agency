---
title: "Self-compiling wiki-from-dropped-documents memory pattern"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 4
summary: "Both llm-wiki-agent and llm-knowledge-base implement the pattern popularized by Andrej Karpathy: drop source documents in, and an LLM agent extracts and files the knowledge into a persistent, interlin"
tags: [knowledge, agent-memory, conf/medium, durable, wiki, knowledge-base, persistence]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# Self-compiling wiki-from-dropped-documents memory pattern

## What it is

Both llm-wiki-agent and llm-knowledge-base implement the pattern popularized by Andrej Karpathy: drop source documents in, and an LLM agent extracts and files the knowledge into a persistent, interlinked wiki that keeps building on itself.

## Why it matters

Use this pattern to give a coding-agent CLI durable, organized knowledge of ingested material across sessions instead of re-reading source docs every time.

## Provenance

- Confidence **medium** · durability **durable** · supported by **4** archived item(s).

## Sources

- https://github.com/SamurAIGPT/llm-wiki-agent
- https://github.com/apoorav21/llm-knowledge-base

---

Part of [[MOC - Agent Memory]] · [[Home]]
