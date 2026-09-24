---
title: "AST-based codebase knowledge graphs instead of embedding RAG"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 4
summary: "graphify and Understand-Anything both turn a codebase, including code, docs, schemas, configs, and PDFs, into a queryable knowledge graph using deterministic AST parsing rather than vector embeddings,"
tags: [knowledge, rag-retrieval, conf/medium, durable, knowledge-graph, ast-parsing, codebase, non-vector]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# AST-based codebase knowledge graphs instead of embedding RAG

## What it is

graphify and Understand-Anything both turn a codebase, including code, docs, schemas, configs, and PDFs, into a queryable knowledge graph using deterministic AST parsing rather than vector embeddings, giving explainable answers about the code.

## Why it matters

Reach for this when an agent's answers about a codebase need to be explainable and traceable rather than similarity-scored, which a vector store cannot guarantee.

## Provenance

- Confidence **medium** · durability **durable** · supported by **4** archived item(s).

## Sources

- https://github.com/safishamsi/graphify
- https://github.com/Graphify-Labs/graphify
- https://github.com/Lum1104/Understand-Anything

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
