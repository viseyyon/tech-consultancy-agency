---
title: "EVO.AI's 'untriaged enhancement' module overwrites good Jira ticket analysis with generic templates"
type: knowledge-entry
domain: "Project State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "In EVO.AI, a downstream 'untriaged enhancement' module overrides the main analysis engine's real, data-grounded JSON output with generic placeholder templates (literal unfilled '%' and '- hours' value"
tags: [knowledge, project-state, conf/high, durable, evo-ai, jira, bug, placeholder-data]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# EVO.AI's 'untriaged enhancement' module overwrites good Jira ticket analysis with generic templates

## What it is

In EVO.AI, a downstream 'untriaged enhancement' module overrides the main analysis engine's real, data-grounded JSON output with generic placeholder templates (literal unfilled '%' and '- hours' values, risk assessments copy-pasted across unrelated ticket types). Fix direction: a rewritten Claude CLI prompt enforcing extraction of actual Jira JSON fields with validation against placeholder/malformed-JSON patterns.

## Why it matters

Explains why EVO.AI ticket comments look generic despite good underlying analysis — a downstream module is silently discarding it.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
