---
title: "Jira/Confluence mining scoped as four independent pipelines plus a separate track"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: medium
durability: durable
evidence: 2
summary: "Rather than one model, the mining plan was split into four independent Jira pipelines (component/product classification as the build-first pipeline; similarity/duplicate detection via embeddings and a"
tags: [knowledge, decisions-rationale, conf/medium, durable, jira-mining, mlops, pipeline-scoping, historical]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Jira/Confluence mining scoped as four independent pipelines plus a separate track

## What it is

Rather than one model, the mining plan was split into four independent Jira pipelines (component/product classification as the build-first pipeline; similarity/duplicate detection via embeddings and a vector index, explicitly not a classifier; regression prediction as a rare-event classifier; fix-prediction with its target left deliberately undecided between 'will it be fixed' and 'time to fix'), with Confluence kept as a wholly separate knowledge-mining project (staleness, orphans, near-duplicates, gap analysis) rather than blended into the Jira prediction pipeline. The scope chosen was whole-org from day one with no pilot phase. On top of this, the same MLOps discipline used on an unrelated predictive-maintenance capstone was decided to wrap every stage of the mining pipeline itself: schema validation, versioned shared features with lineage, tracked training/registry, drift monitoring on both data and predictions (explicitly noted to double as an organizational signal - a cycle-time shift could mean model drift or a real process change), and SHAP explainability on every flagged item.

## Why it matters

This was the original shape of the Jira/Confluence mining ambition before it evolved into the deterministic retrieval-and-verification assistant actually built later - useful context for why early design documents describe classifiers that the shipped system doesn't use.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- MLOps capstone (predictive maintenance) -> Jira/Confluence mining discussion

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
