---
title: "Agent-driven build loops need a separate builder, auditor, and corrector"
type: knowledge-entry
domain: "Operating Preferences"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "For long autonomous build/mining projects, the user wants three distinct roles: a builder, an independent auditor (a fresh-context agent, never the builder reviewing itself), and a corrector, with cor"
tags: [knowledge, operating-preferences, conf/high, durable, agent-loop, auditor, verification, autonomy]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Operating Preferences]]"]
---

# Agent-driven build loops need a separate builder, auditor, and corrector

## What it is

For long autonomous build/mining projects, the user wants three distinct roles: a builder, an independent auditor (a fresh-context agent, never the builder reviewing itself), and a corrector, with correction capped at 3 iterations before a hard stop. The auditor must verify every claim against the database (never against a report), re-derive denominators, require every new check to have been observed failing on a planted violation before it counts, and measure recall as well as precision.

## Why it matters

Letting the builder grade its own work, or accepting an uncapped correction loop, reproduces the self-review blind spots this rule was written to close.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Vantiva Jira and Confluence mining

---

Part of [[MOC - Operating Preferences]] · [[Home]]
