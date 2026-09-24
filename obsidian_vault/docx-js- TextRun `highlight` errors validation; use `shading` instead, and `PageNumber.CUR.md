---
title: "docx-js: TextRun `highlight` errors validation; use `shading` instead, and `PageNumber.CURRENT` for page numbers"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "In the `docx` JS library, setting `highlight` on a TextRun causes validation failures; the working substitute is `shading: { fill: 'FFF3CD', type: ShadingType.CLEAR }`. Separately, page numbering only"
tags: [knowledge, developer-infrastructure, conf/high, durable, docx-js, word-generation, textrun, page-numbering]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# docx-js: TextRun `highlight` errors validation; use `shading` instead, and `PageNumber.CURRENT` for page numbers

## What it is

In the `docx` JS library, setting `highlight` on a TextRun causes validation failures; the working substitute is `shading: { fill: 'FFF3CD', type: ShadingType.CLEAR }`. Separately, page numbering only works reliably via `PageNumber.CURRENT` in header/footer tab-stop constructs, not by instantiating a PageNumber object directly.

## Why it matters

Reusable fix to avoid re-discovering the same validation failure mid-generation on future docx-js documents.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
