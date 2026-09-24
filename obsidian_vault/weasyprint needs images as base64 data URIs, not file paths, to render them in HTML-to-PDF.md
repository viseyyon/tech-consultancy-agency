---
title: "weasyprint needs images as base64 data URIs, not file paths, to render them in HTML-to-PDF output"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "When generating a LinkedIn PDF article with weasyprint, images referenced via normal file paths/URLs in the HTML silently failed to render in the output PDF. Fix: read each image as binary, base64-enc"
tags: [knowledge, developer-infrastructure, conf/high, durable, weasyprint, pdf-generation, base64, images]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# weasyprint needs images as base64 data URIs, not file paths, to render them in HTML-to-PDF output

## What it is

When generating a LinkedIn PDF article with weasyprint, images referenced via normal file paths/URLs in the HTML silently failed to render in the output PDF. Fix: read each image as binary, base64-encode it, and inline it as `data:image/png;base64,[string]` in the `img src` attribute before running the HTML through weasyprint.

## Why it matters

Reliable pattern to avoid silently missing images in any future weasyprint-based PDF generation with visuals.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
