---
title: "Standard doc-gen QA pipeline: Node build script to LibreOffice PDF to pdftoppm JPEG to visual QA to outputs"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 6
summary: "The consistent working pattern for polished docx/pptx deliverables: write a Node.js build script using docx-js or pptxgenjs, execute it, convert to PDF via LibreOffice headless (/mnt/skills/public/{do"
tags: [knowledge, claude-code-practice, conf/high, durable, docx, pptx, libreoffice, visual-qa]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# Standard doc-gen QA pipeline: Node build script to LibreOffice PDF to pdftoppm JPEG to visual QA to outputs

## What it is

The consistent working pattern for polished docx/pptx deliverables: write a Node.js build script using docx-js or pptxgenjs, execute it, convert to PDF via LibreOffice headless (/mnt/skills/public/{docx,pptx}/scripts/office/soffice.py --headless --convert-to pdf), render per-page/per-slide JPEGs with pdftoppm -jpeg -r 100-150 for visual QA, then copy final files to /mnt/user-data/outputs/. This reliably catches layout bugs (e.g. navy-icon-on-navy-circle invisibility, text overflow on narrow cards) before delivery.

## Why it matters

This is his default path for any executive slide deck (BRM decks, charters, pitch decks) and general docx/pptx deliverable, so it should be the default assumption for how such artifacts get produced.

## Provenance

- Confidence **high** · durability **durable** · supported by **6** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
