---
title: "openpyxl helper functions must not carry italic as a positional bool between bold and alignment params"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "A cell-styling helper with signature (bold, italic, h_align, v_align) silently breaks when callers omit italic — string alignment values shift into the boolean italic slot and booleans shift into v_al"
tags: [knowledge, claude-code-practice, conf/high, durable, openpyxl, python, positional-arguments, excel]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# openpyxl helper functions must not carry italic as a positional bool between bold and alignment params

## What it is

A cell-styling helper with signature (bold, italic, h_align, v_align) silently breaks when callers omit italic — string alignment values shift into the boolean italic slot and booleans shift into v_align, causing openpyxl ValueError since "True" isn't a valid vertical-alignment value (valid: top, center, bottom, justify, distributed). Fix: drop italic as a positional parameter from shared helpers entirely.

## Why it matters

Prevents silent parameter-shifting bugs in any shared openpyxl styling helper.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
