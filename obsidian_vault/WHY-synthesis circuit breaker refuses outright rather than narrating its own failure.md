---
title: "WHY-synthesis circuit breaker refuses outright rather than narrating its own failure"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "The constrained WHY-synthesis stage of the mining assistant (an LLM that only sees a structured ExecutionTrace, never free retrieval) got a circuit breaker (C6) fixed to hard-refuse when all evidence"
tags: [knowledge, rag-retrieval, conf/high, durable, circuit-breaker, refusal, lens-ranking, synthesis]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# WHY-synthesis circuit breaker refuses outright rather than narrating its own failure

## What it is

The constrained WHY-synthesis stage of the mining assistant (an LLM that only sees a structured ExecutionTrace, never free retrieval) got a circuit breaker (C6) fixed to hard-refuse when all evidence specialists fail, replacing earlier behavior where it would narrate its own failure as if it were an answer. Lens ranking was reworked from a rejected multiplicative-boost-with-cap scheme (which destroyed ordering) to a two-tier sort (boost_matched first, then similarity), and the Architecture lens was changed to rank by structural cross-family breadth rather than lexical keyword match.

## Why it matters

Prevents the assistant from ever presenting a synthesized failure narrative as a grounded answer, which would be worse than a visible refusal.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-13 session)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
