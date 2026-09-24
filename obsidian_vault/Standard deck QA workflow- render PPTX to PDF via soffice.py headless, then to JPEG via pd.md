---
title: "Standard deck QA workflow: render PPTX to PDF via soffice.py headless, then to JPEG via pdftoppm"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "Every executive deck goes through: `soffice.py --headless --convert-to pdf file.pptx` then `pdftoppm -jpeg -r 110 file.pdf prefix` to produce per-slide JPGs for inspection, catching overflow/clipping/"
tags: [knowledge, developer-infrastructure, conf/high, durable, pptx, libreoffice, visual-qa, deck-generation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Standard deck QA workflow: render PPTX to PDF via soffice.py headless, then to JPEG via pdftoppm

## What it is

Every executive deck goes through: `soffice.py --headless --convert-to pdf file.pptx` then `pdftoppm -jpeg -r 110 file.pdf prefix` to produce per-slide JPGs for inspection, catching overflow/clipping/collision defects before shipping. For LAYOUT_WIDE slides the usable canvas is 13.3x7.5in, safe content zone x=0.7-12.6/y=0.5-7.1, footer strip at y=6.55 (height 0.55), and right-aligning the final label (lx = mx - labelWidth + 0.12) prevents right-edge overflow. Icons render via react-icons SVG -> ReactDOMServer.renderToStaticMarkup -> sharp PNG buffer -> base64 into addImage.

## Why it matters

This pipeline is what catches layout defects before an executive deck ships, so skipping it is the direct cause of any overflow/clipping bug reaching a reviewer.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
