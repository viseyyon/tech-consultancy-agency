---
title: "Reasoning-based hierarchical indexing as an alternative to vector-chunk RAG"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 2
summary: "VectifyAI's PageIndex builds a hierarchical page index over a document and reasons over that structure to retrieve, instead of splitting text into chunks and embedding them into a vector store."
tags: [knowledge, rag-retrieval, conf/medium, durable, rag, document-indexing, vectorless, retrieval]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Reasoning-based hierarchical indexing as an alternative to vector-chunk RAG

## What it is

VectifyAI's PageIndex builds a hierarchical page index over a document and reasons over that structure to retrieve, instead of splitting text into chunks and embedding them into a vector store.

## Why it matters

Consider this over standard chunk-and-embed RAG when documents are long or structured and chunking is causing retrieval errors or losing document-level context.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- https://github.com/VectifyAI/PageIndex

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
