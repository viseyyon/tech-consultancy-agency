---
title: "python-docx edits must replace text at the run level, not paragraph level, to preserve formatting"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 2
summary: "Paragraph-level text replacement in python-docx strips existing character formatting (bold, color, font); run-level replacement is required to preserve it. The broader working pattern: write the full"
tags: [knowledge, developer-infrastructure, conf/medium, durable, python-docx, document-generation, resume-editing, formatting]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# python-docx edits must replace text at the run level, not paragraph level, to preserve formatting

## What it is

Paragraph-level text replacement in python-docx strips existing character formatting (bold, color, font); run-level replacement is required to preserve it. The broader working pattern: write the full document via a Node.js build script using the docx library, run it, validate with the docx skill's validate.py, then copy to outputs -- targeted edits are more reliable via str_replace on the build script followed by a rebuild than in-place document editing.

## Why it matters

Following this pattern avoids silently losing formatting when editing resumes or other .docx files programmatically, and rebuild-from-script is more reliable than direct in-place edits.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
