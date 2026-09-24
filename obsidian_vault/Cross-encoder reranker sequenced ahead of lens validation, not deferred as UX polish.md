---
title: "Cross-encoder reranker sequenced ahead of lens validation, not deferred as UX polish"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "With the assistant's semantic gate refusing 55.6% of a test battery, the reranker (bge-reranker-v2-m3) was sequenced to ship before Phase 4's cross-lens entailment gate, because that gate is untestabl"
tags: [knowledge, rag-retrieval, conf/high, durable, reranker, retrieval, sequencing, bge-reranker]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Cross-encoder reranker sequenced ahead of lens validation, not deferred as UX polish

## What it is

With the assistant's semantic gate refusing 55.6% of a test battery, the reranker (bge-reranker-v2-m3) was sequenced to ship before Phase 4's cross-lens entailment gate, because that gate is untestable when most questions get refused before reaching it - the reranker is a prerequisite for validating lenses, not an optional quality improvement. The vector-similarity stage becomes a top-50 candidate generator rather than the final filter; both vector_similarity and rerank_score get recorded per chunk so the evidence gate can be recalibrated from scratch on the new score scale, with success defined as FP staying at 0/10 and FN dropping below 25-40%.

## Why it matters

Explains why the reranker exists in the build order before lens work, and gives the exact success bar so nobody re-litigates the sequencing decision.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-12 session)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
