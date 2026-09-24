---
title: "Vantiva Mining Console assistant: deterministic specialist-pipeline architecture"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 4
summary: "The assistant is built as a rule-based planner routing to six typed, least-privilege deterministic specialists rather than an LLM multi-agent taskforce or an LLM-as-judge grader -- a council review re"
tags: [knowledge, rag-retrieval, conf/high, durable, rag, architecture, postgres, evaluation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Vantiva Mining Console assistant: deterministic specialist-pipeline architecture

## What it is

The assistant is built as a rule-based planner routing to six typed, least-privilege deterministic specialists rather than an LLM multi-agent taskforce or an LLM-as-judge grader -- a council review rejected both as unverifiable and replaced grading with seven deterministic hard-gate checks including numeric recomputation. Storage is Postgres+pgvector rather than Neo4j/Qdrant, with documented migration thresholds. Both source Jira instances are Data Center, not Cloud, ruling out Cloud-only APIs; the semantic-evidence gate is calibrated to (>=2 chunks, similarity >=0.87) as a stated retrieval-precision limitation, not a tunable threshold, giving 0% false positives and ~55.6% false negatives on the current battery.

## Why it matters

Captures the load-bearing architectural choices and their rejected alternatives so nobody re-proposes LLM-judge grading or a graph database without re-litigating the same evidence.

## Provenance

- Confidence **high** · durability **durable** · supported by **4** archived item(s).

## Sources

- Conversation 2026-07-31 - Mining Console final prompt
- Conversation 2026-07-31 - Mining Console app prompt
- Cowork - Vantiva Jira and Confluence mining (2026-08-12 session)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
