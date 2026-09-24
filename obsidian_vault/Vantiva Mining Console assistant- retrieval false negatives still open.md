---
title: "Vantiva Mining Console assistant: retrieval false negatives still open"
type: knowledge-entry
domain: "Open Commitments"
entry-type: "Caveat"
confidence: medium
durability: ephemeral
evidence: 2
summary: "The assistant's Holdout battery (H1-H10) was invalidated as a measurement because it drove three of its own fixes; a genuinely cold Holdout 2 of 10 questions (multi-hop, permitted comparisons, Conflue"
tags: [knowledge, open-commitments, conf/medium, ephemeral, vantiva, assistant, rag, evaluation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Open Commitments]]"]
---

# Vantiva Mining Console assistant: retrieval false negatives still open

## What it is

The assistant's Holdout battery (H1-H10) was invalidated as a measurement because it drove three of its own fixes; a genuinely cold Holdout 2 of 10 questions (multi-hop, permitted comparisons, Confluence-only, one per unexercised refusal class) still needs to be built and run once without fixing against it. Three known false negatives (SoC-composite, component filter, release filter) need new routing patterns to TaxonomyQuery/SQLAggregate so composite questions don't fall back to unrouted semantic search.

## Why it matters

Marks exactly which retrieval gaps are measured-but-unfixed versus genuinely untested, so evaluation work isn't duplicated.

## Provenance

- Confidence **medium** · durability **ephemeral** · supported by **2** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- Cowork - Vantiva Jira and Confluence mining (2026-08-14)

---

Part of [[MOC - Open Commitments]] · [[Home]]
