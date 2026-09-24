---
title: "KNOWLEDGE-FORGE: code knowledge graph plus institutional-memory design"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "KNOWLEDGE-FORGE is a designed (not yet built) Neo4j-based system combining a code knowledge graph (from tree-sitter static parsing and CI/CD system metadata) with an institutional-memory / attrition-m"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, knowledge-forge, neo4j, code-graph, viseyyon]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# KNOWLEDGE-FORGE: code knowledge graph plus institutional-memory design

## What it is

KNOWLEDGE-FORGE is a designed (not yet built) Neo4j-based system combining a code knowledge graph (from tree-sitter static parsing and CI/CD system metadata) with an institutional-memory / attrition-mitigation layer (Person/Team/Commit/Review/Ticket/Decision nodes), serving AI agents via MCP, engineers via a dashboard, and leadership via knowledge-risk reporting. Its headline derived metric is orphan-module detection -- modules whose top experts have all departed -- fed by a 6-stage ingestion pipeline (static parse, git history mining, system connectors, LLM enrichment, derivation, MCP/dashboard serving).

## Why it matters

This is the design blueprint for Viseyyon's flagship KNOWLEDGE-FORGE product, referenced repeatedly in later competitive-strategy and prioritization decisions.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Conversation 2026-07-31 - Jarvis technical design session

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
