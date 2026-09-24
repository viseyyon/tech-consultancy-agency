---
title: "GitHub Copilot's agent harness caps Claude Opus at 128K tokens and can't KB-index non-Markdown firmware files"
type: knowledge-entry
domain: "Industry Signal"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "Confirmed via GitHub Community Discussion #186340: Copilot's agent harness caps Claude Opus 4.6 at 128K tokens despite the model supporting 1M. Per VS Code docs, repos exceeding 2,500 indexable files"
tags: [knowledge, industry-signal, conf/high, durable, github-copilot, context-window, indexing-limits, firmware-repos]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Industry Signal]]"]
---

# GitHub Copilot's agent harness caps Claude Opus at 128K tokens and can't KB-index non-Markdown firmware files

## What it is

Confirmed via GitHub Community Discussion #186340: Copilot's agent harness caps Claude Opus 4.6 at 128K tokens despite the model supporting 1M. Per VS Code docs, repos exceeding 2,500 indexable files fall back to a basic index ('not scanning the whole repo is a feature' per GitHub). Copilot Knowledge Bases accept only Markdown, excluding .c/.h/.bbappend/Makefile.

## Why it matters

Together these make Copilot structurally weak for RDK-B/AOSP-scale firmware repos (AOSP alone: 170GB, 7M+ lines) — the core differentiator cited for SYNTHFORCE-OC in leadership pitches against Copilot.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Industry Signal]] · [[Home]]
