---
title: "pptxgenjs hex colors must be strictly 6-digit; 8-digit alpha hex silently corrupts the PPTX"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "An 8-digit alpha hex code (e.g. '0A162880') passed to pptxgenjs causes silent file corruption that PowerPoint reports as a damaged file rather than a rendering error — must use strict 6-digit hex ('0A"
tags: [knowledge, environment-tooling-state, conf/high, durable, pptxgenjs, powerpoint, hex-color, file-corruption]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# pptxgenjs hex colors must be strictly 6-digit; 8-digit alpha hex silently corrupts the PPTX

## What it is

An 8-digit alpha hex code (e.g. "0A162880") passed to pptxgenjs causes silent file corruption that PowerPoint reports as a damaged file rather than a rendering error — must use strict 6-digit hex ("0A1628"). Zero-dimension LINE shapes (w:0, h:0) can also contribute to corruption. Verify PPTX integrity post-generation via Python's zipfile module (internal file count, slide presence).

## Why it matters

Avoids shipping a corrupted PPTX that only fails when the recipient opens it in PowerPoint.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
