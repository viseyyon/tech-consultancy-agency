---
title: "Vantiva's 3GPP Combo Analysis Tool proposal is ~40% complete; ComboID must be content-addressed, not per-upload minted"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Caveat"
confidence: medium
durability: ephemeral
evidence: 1
summary: "A reviewed internal proposal for a 3GPP carrier-aggregation band-combination compliance tool was assessed as sound UI scoping but only ~40% of a working system. The key design fix identified: ComboID"
tags: [knowledge, decisions-rationale, conf/medium, ephemeral, 3gpp, combo-analysis, data-model, deduplication]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Vantiva's 3GPP Combo Analysis Tool proposal is ~40% complete; ComboID must be content-addressed, not per-upload minted

## What it is

A reviewed internal proposal for a 3GPP carrier-aggregation band-combination compliance tool was assessed as sound UI scoping but only ~40% of a working system. The key design fix identified: ComboID was modeled backwards — the proposal mints a new ComboID on every document upload instead of using a content-addressed/canonical string, so the same combo across different source documents fails to deduplicate. Recommended stack: PostgreSQL with a Combo Registry (UNIQUE canonical string, JSONB attributes, provenance/audit tables), Camelot/pdfplumber for spec table extraction, an 8-stage document lifecycle, with LLM-assisted extraction kept rules-first and human-in-the-loop, never autonomous.

## Why it matters

Without fixing the ComboID design, the tool cannot correctly deduplicate combos sourced from different documents — a core correctness flaw before further build-out.

## Provenance

- Confidence **medium** · durability **ephemeral** · supported by **1** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
