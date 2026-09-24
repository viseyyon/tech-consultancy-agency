---
title: "Span-based tracing for debugging RAG and agent pipelines"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 1
summary: "A recommended debugging structure breaks each AI call into spans (intent router, retriever, retrieved chunks, LLM call, tool calls, final response), logs request metadata (session, model, prompt versi"
tags: [knowledge, evaluation-observability, conf/medium, durable, tracing, rag-debugging, spans, observability]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# Span-based tracing for debugging RAG and agent pipelines

## What it is

A recommended debugging structure breaks each AI call into spans (intent router, retriever, retrieved chunks, LLM call, tool calls, final response), logs request metadata (session, model, prompt version, temperature) and retrieval scores, and adds explicit flagging rules for suspicious answers.

## Why it matters

Without span-level structure, diagnosing why a RAG answer was wrong reduces to guesswork.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- https://instagram.com/reel/DX0u_BzuAGm

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
