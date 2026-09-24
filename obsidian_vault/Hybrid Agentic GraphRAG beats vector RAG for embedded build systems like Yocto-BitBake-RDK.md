---
title: "Hybrid Agentic GraphRAG beats vector RAG for embedded build systems like Yocto/BitBake/RDK-B"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Decision"
confidence: medium
durability: durable
evidence: 1
summary: "For the PHOENIX multi-agent build system, a distributed GraphRAG server (Neo4j for the knowledge graph, Qdrant for vector embeddings, Redis for caching, decoupled from the orchestrator) was recommende"
tags: [knowledge, rag-retrieval, conf/medium, durable, graphrag, rag, phoenix, neo4j]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Hybrid Agentic GraphRAG beats vector RAG for embedded build systems like Yocto/BitBake/RDK-B

## What it is

For the PHOENIX multi-agent build system, a distributed GraphRAG server (Neo4j for the knowledge graph, Qdrant for vector embeddings, Redis for caching, decoupled from the orchestrator) was recommended over plain vector-chunk RAG because build systems like Yocto/BitBake, RDK-B, Android TV, and OpenWrt have inherently graph-structured relationships (recipe dependencies, inheritance chains, component interconnections). Endpoints scoped for PHOENIX's BUILD-ENG agent: /build/analyze, /graph/traverse, /query, feeding confidence-scored fixes into the existing 5-retry loop.

## Why it matters

Graph representation captures build-system dependency structure that plain vector RAG would miss, improving fix-recommendation quality.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
