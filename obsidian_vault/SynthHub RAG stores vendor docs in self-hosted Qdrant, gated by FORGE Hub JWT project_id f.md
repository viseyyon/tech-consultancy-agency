---
title: "SynthHub RAG stores vendor docs in self-hosted Qdrant, gated by FORGE Hub JWT project_id filters, never managed cloud"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "SynthHub's settled RAG architecture is self-hosted Qdrant (pgvector as fallback), one collection per project, with a mandatory project_id metadata filter enforced at query time via FORGE Hub's JWT cla"
tags: [knowledge, rag-retrieval, conf/high, durable, rag, qdrant, synth-guard, forge-hub]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# SynthHub RAG stores vendor docs in self-hosted Qdrant, gated by FORGE Hub JWT project_id filters, never managed cloud

## What it is

SynthHub's settled RAG architecture is self-hosted Qdrant (pgvector as fallback), one collection per project, with a mandatory project_id metadata filter enforced at query time via FORGE Hub's JWT claims. The ingestion pipeline gates all embedding calls through SYNTH-GUARD, uses a local embedding model for Class A/B classified content, and stamps every chunk with project_id, source_vendor, classification, allowed_principals, and doc_version.

## Why it matters

Managed cloud vector stores (Pinecone, Zilliz Cloud) were ruled out because Broadcom/MaxLinear source cannot legally land in a non-air-gapped index, so this architecture is the enforced boundary for vendor-confidential material.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
