---
title: "python-pptx template fidelity needs direct master indexing plus inspecting the unpacked template XML"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "For pixel-perfect alignment to Vantiva's multi-master PowerPoint template, accessing a specific master via `prs.slide_masters[3]` then its layout via `master3.slide_layouts[1]`/`[11]` was more reliabl"
tags: [knowledge, developer-infrastructure, conf/high, durable, python-pptx, slide-masters, ooxml, template-fidelity]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# python-pptx template fidelity needs direct master indexing plus inspecting the unpacked template XML

## What it is

For pixel-perfect alignment to Vantiva's multi-master PowerPoint template, accessing a specific master via `prs.slide_masters[3]` then its layout via `master3.slide_layouts[1]`/`[11]` was more reliable than the global `prs.slide_layouts` index, which can resolve to the wrong master. Unpacking the .pptx as a ZIP and reading `ppt/slideLayouts/` and `ppt/slideMasters/` XML was necessary for exact positioning/colors/placeholder relationships; `set_ph()` helpers populated placeholders by `placeholder_format.idx` while preserving font styling; removing template placeholder slides was done by manipulating `prs.slides._sldIdLst` directly.

## Why it matters

This is the reliable technique for any future python-pptx build against a multi-master template, avoiding the wrong-master resolution bug the global index can cause.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
