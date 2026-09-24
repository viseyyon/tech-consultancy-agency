---
title: "SYNTHFORCE-OC agent design principle: convert standalone Python/API scripts into native Opencode-session agents"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "When converting standalone tools (e.g. patch_analyzer_agent.py, patch_modifier.py calling Azure Anthropic directly with hardcoded keys) into SYNTHFORCE-OC agents, the transformation replaces direct AP"
tags: [knowledge, decisions-rationale, conf/medium, durable, synthforce-oc, agent-conversion, opencode, mcp]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# SYNTHFORCE-OC agent design principle: convert standalone Python/API scripts into native Opencode-session agents

## What it is

When converting standalone tools (e.g. patch_analyzer_agent.py, patch_modifier.py calling Azure Anthropic directly with hardcoded keys) into SYNTHFORCE-OC agents, the transformation replaces direct API calls and Python subprocess logic with native Claude reasoning inside Opencode sessions, using MCP shell tools and KB integrations instead of a separate Python runtime. Every agent auto-indexes its findings back to the project knowledge base via kb_activity_index.

## Why it matters

This is the standard conversion pattern for new SYNTHFORCE-OC agents (SYNTH-RCA, SYNTH-PATCH-ANALYZE, SYNTH-PATCH-MOD), letting later work benefit from earlier findings automatically.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
