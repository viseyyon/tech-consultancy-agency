---
title: "Holdout battery H1-H10 retired to a development set; BGE-M3 upgrade stays deferred"
type: knowledge-entry
domain: "RAG & Retrieval"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "Because working through holdout questions H1-H10 drove three of the assistant's own fixes (cross-lens entailment, lenient entity recognition, suppression-gate wiring), the battery can no longer measur"
tags: [knowledge, rag-retrieval, conf/high, durable, holdout, evaluation, embeddings, bge-m3]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - RAG & Retrieval]]"]
---

# Holdout battery H1-H10 retired to a development set; BGE-M3 upgrade stays deferred

## What it is

Because working through holdout questions H1-H10 drove three of the assistant's own fixes (cross-lens entailment, lenient entity recognition, suppression-gate wiring), the battery can no longer measure generalization and was reclassified as 'development_set_2' rather than kept as a clean holdout - a new cold Holdout 2 (10 questions targeting uncovered question shapes) is required instead, and if that one also fails on missing routing patterns the ruling is to record it as a known planner-coverage limitation, not chase it as a defect. Separately, upgrading the embedding model to BGE-M3 (for multilingual support) stays deferred after three separate measurement rounds found no answer failure attributable to embedding quality; a third calibration round was explicitly rejected as unnecessary churn.

## Why it matters

Stops anyone from citing the original H1-H10 numbers as current assistant accuracy, and stops re-opening the embedding-upgrade debate without new evidence.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-14 session)

---

Part of [[MOC - RAG & Retrieval]] · [[Home]]
