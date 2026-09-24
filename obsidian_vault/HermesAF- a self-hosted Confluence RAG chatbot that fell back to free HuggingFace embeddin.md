---
title: "HermesAF: a self-hosted Confluence RAG chatbot that fell back to free HuggingFace embeddings after OpenAI quota errors"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "'HermesAF' is a Confluence RAG chat assistant using ChromaDB for vector storage and a Streamlit UI, capable of scanning Confluence spaces, answering questions via chat, and creating new pages. It laun"
tags: [knowledge, rag-retrieval, conf/high, durable, hermesaf, confluence, rag, chromadb]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# HermesAF: a self-hosted Confluence RAG chatbot that fell back to free HuggingFace embeddings after OpenAI quota errors

## What it is

'HermesAF' is a Confluence RAG chat assistant using ChromaDB for vector storage and a Streamlit UI, capable of scanning Confluence spaces, answering questions via chat, and creating new pages. It launched on OpenAI embeddings + GPT-4, but hit a 429 insufficient_quota error mid-use; it was then rebuilt on free HuggingFace sentence-transformer embeddings with template-based responses so the tool would keep working at zero cost.

## Why it matters

The concrete lesson for future RAG/chatbot builds is to default to a free local-embedding fallback rather than a hard OpenAI dependency, avoiding this same quota-outage failure mode.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
