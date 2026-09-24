---
title: "pptxgenjs/LibreOffice rendering has specific shape-name and mutation gotchas"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "pptxgenjs/LibreOffice needs OOXML preset shape names — 'roundRect' and 'rect', not 'roundedRectangle'/'rectangle' — the wrong name silently renders nothing rather than erroring. 'pres.shapes.RIGHT_TRI"
tags: [knowledge, developer-infrastructure, conf/high, durable, pptxgenjs, libreoffice, shape-names, rendering-bugs]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# pptxgenjs/LibreOffice rendering has specific shape-name and mutation gotchas

## What it is

pptxgenjs/LibreOffice needs OOXML preset shape names — 'roundRect' and 'rect', not 'roundedRectangle'/'rectangle' — the wrong name silently renders nothing rather than erroring. 'pres.shapes.RIGHT_TRIANGLE' with rotation renders incorrectly through the LibreOffice pipeline; use 'pres.shapes.CHEVRON' for directional arrows instead. Any shadow() helper must return a fresh object each call since pptxgenjs mutates option objects in place. LAYOUT_WIDE (13.33x7.5in) is the standard widescreen preset.

## Why it matters

These are silent-failure traps (invisible shapes, misrendered rotation, shared-object mutation bugs) that won't throw an error, so they need to be checked proactively in any pptxgenjs build rather than debugged after the fact.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
