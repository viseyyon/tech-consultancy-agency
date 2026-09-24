---
title: "Conversation search works best combining an internal codename with a deployment-state qualifier"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 1
summary: "When searching Claude's own conversation history to check whether similar work already exists, a broad technical query ('log analyzer RCA failure analysis deployed') was less productive than a query c"
tags: [knowledge, agent-memory, conf/medium, durable, conversation-search, search-technique, claude]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# Conversation search works best combining an internal codename with a deployment-state qualifier

## What it is

When searching Claude's own conversation history to check whether similar work already exists, a broad technical query ('log analyzer RCA failure analysis deployed') was less productive than a query combining the specific internal framework name with a deployment-state qualifier ('Automatics deployed production'). The second query surfaced the exact prior conversation about a previously built Build Failure Analyzer.

## Why it matters

Materially changed the strategic response to a colleague's request by surfacing prior work -- future conversation searches should default to codename plus deployment-state qualifier queries rather than broad technical descriptions.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Memory]] · [[Home]]
