---
title: "Mining assistant's evidence gate recalibrated to at least 2 chunks at similarity 0.87"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "The semantic evidence-sufficiency gate was first tuned on a single test case (>=2 chunks, similarity 0.84, FP 0/1) and looked safe, but an extended battery of 10 genuine absent-answer cases (competito"
tags: [knowledge, rag-retrieval, conf/high, durable, retrieval, evidence-gate, calibration, threshold]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Mining assistant's evidence gate recalibrated to at least 2 chunks at similarity 0.87

## What it is

The semantic evidence-sufficiency gate was first tuned on a single test case (>=2 chunks, similarity 0.84, FP 0/1) and looked safe, but an extended battery of 10 genuine absent-answer cases (competitor tech, fake family codes, real out-of-scope families) exposed FP 5/10 at that threshold - family-adjacent vocabulary was fooling the similarity check. The corrected default (>=2 chunks, 0.87) holds FP at 0/10 with FN 5/9 (55.6%), and that residual false-negative rate is recorded verbatim as 'a retrieval-precision limitation, not a tuning choice' specifically to stop anyone lowering the threshold back to 0.84 to make refusals disappear.

## Why it matters

Any future threshold change on this gate needs to be checked against the full absent-case battery, not a single example, or the false-positive hole reopens.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-12 session)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
