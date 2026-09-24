---
title: "KNOWLEDGE-FORGE design: a three-layer Neo4j graph (code/system/knowledge) with bus-factor and decay scoring"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "KNOWLEDGE-FORGE is a designed three-layer Neo4j graph (code layer from tree-sitter, system layer from CI/CD metadata, knowledge layer with Person/Commit/Decision/Document nodes), built via a six-stage"
tags: [knowledge, agent-memory, conf/high, durable, knowledge-forge, neo4j, bus-factor, knowledge-graph]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# KNOWLEDGE-FORGE design: a three-layer Neo4j graph (code/system/knowledge) with bus-factor and decay scoring

## What it is

KNOWLEDGE-FORGE is a designed three-layer Neo4j graph (code layer from tree-sitter, system layer from CI/CD metadata, knowledge layer with Person/Commit/Decision/Document nodes), built via a six-stage ingestion pipeline (static parse, git history mining, system connectors, LLM decision-mining enrichment, bus-factor/decay derivation, MCP+dashboard serving). It includes a knowledge-attrition playbook: an orphan-module query for critical modules whose experts departed, an LLM pass mining implicit ADRs from PRs/Gerrit/Jira, and a pre-departure protocol gating exit checklists on a walkthrough or successor sign-off for bus-factor-1 modules.

## Why it matters

It is SYNTHFORCE's answer to CEI's eTWIN and Viseyyon's top strengthening priority, so it anchors both the internal knowledge-retention strategy and the YC pitch positioning.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Memory]] · [[Home]]
