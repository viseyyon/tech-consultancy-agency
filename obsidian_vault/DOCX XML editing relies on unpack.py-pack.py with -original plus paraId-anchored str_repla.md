---
title: "DOCX XML editing relies on unpack.py/pack.py with --original plus paraId-anchored str_replace"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 1
summary: "Structured Word-document edits use the docx skill's unpack.py and pack.py (pack.py requires --original to preserve relationships). w14:paraId attributes are stable anchors for str_replace targeting sp"
tags: [knowledge, claude-code-practice, conf/medium, durable, docx, xml-editing, unpack-pack, paraid]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# DOCX XML editing relies on unpack.py/pack.py with --original plus paraId-anchored str_replace

## What it is

Structured Word-document edits use the docx skill's unpack.py and pack.py (pack.py requires --original to preserve relationships). w14:paraId attributes are stable anchors for str_replace targeting specific table cells; when replacing an empty paragraph with several new ones, the full pPr formatting (border, shading, spacing, font) must be replicated on every new paragraph or styling is lost. Verify rendered content with pandoc file.docx -t plain.

## Why it matters

This is the exact reliable procedure for direct DOCX XML edits -- skipping the --original flag or the pPr replication step causes broken relationships or lost formatting.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
