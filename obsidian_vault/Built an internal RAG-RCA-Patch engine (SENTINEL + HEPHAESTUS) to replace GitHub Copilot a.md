---
title: "Built an internal RAG-RCA-Patch engine (SENTINEL + HEPHAESTUS) to replace GitHub Copilot as interim tooling"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "The Vantiva RAG-RCA-Patch Engine was built to replace Copilot's workspace-scoped, transient RAG. SENTINEL is the RCA orchestrator (retrieves via ChromaDB+SentenceTransformer RAG, calls Claude Sonnet v"
tags: [knowledge, rag-retrieval, conf/high, durable, sentinel, hephaestus, rag, rca]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Built an internal RAG-RCA-Patch engine (SENTINEL + HEPHAESTUS) to replace GitHub Copilot as interim tooling

## What it is

The Vantiva RAG-RCA-Patch Engine was built to replace Copilot's workspace-scoped, transient RAG. SENTINEL is the RCA orchestrator (retrieves via ChromaDB+SentenceTransformer RAG, calls Claude Sonnet via the Anthropic API for structured JSON RCA reports); HEPHAESTUS is the patch generator (produces git unified-diff patches from RCA output plus similar historical patches). Completed RCAs and accepted patches feed back into the RAG index as a flywheel; a REST API wrapper into Jenkins for auto-triggered RCA on failed builds was the next planned step.

## Why it matters

This exists specifically because Copilot's RAG has no institutional memory, no JIRA awareness, and a Microsoft-controlled index — the gap this engine was built to close.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
