---
title: "Codebase documentation generator: 5-stage pipeline, citation validator pending"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 2
summary: "The codebase documentation generator is a Node CLI for RDK/Android/Linux-TV codebases, orchestrated by pipeline.js with state.json checkpoints: scanner.js detects modules from build markers, chunker.j"
tags: [knowledge, developer-infrastructure, conf/high, durable, doc-generator, rdk, citations, validator]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Codebase documentation generator: 5-stage pipeline, citation validator pending

## What it is

The codebase documentation generator is a Node CLI for RDK/Android/Linux-TV codebases, orchestrated by pipeline.js with state.json checkpoints: scanner.js detects modules from build markers, chunker.js packs ~28k-character context windows, and render.js emits HTML, print-ready PDF, and DOCX with Mermaid diagrams converted to PNG. Gemini, ChatGPT, and Kimi independently converged on the same missing piece: nothing currently verifies the file:line evidence the prompts demand, so a deterministic citation validator still needs to be built.

## Why it matters

Names the one gap three independent reviewers agreed matters most, so it isn't lost among smaller polish items.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Conversation 2026-07-29 - Codebase documentation generator

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
