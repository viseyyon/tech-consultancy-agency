---
title: "`pandoc -t gfm --wrap=none` reliably converts Word release-notes/technical docs to clean Markdown"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "For converting a 4,642-line Vantiva release-notes Word document to Markdown, GitHub-Flavored Markdown output (`-t gfm`) preserved table structures better than standard Markdown, and `--wrap=none` prev"
tags: [knowledge, developer-infrastructure, conf/high, durable, pandoc, word-to-markdown, gfm, document-conversion]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# `pandoc -t gfm --wrap=none` reliably converts Word release-notes/technical docs to clean Markdown

## What it is

For converting a 4,642-line Vantiva release-notes Word document to Markdown, GitHub-Flavored Markdown output (`-t gfm`) preserved table structures better than standard Markdown, and `--wrap=none` prevented unwanted line breaks that would otherwise disrupt tables and technical specs (version numbers, dates, issue IDs).

## Why it matters

Reliable pandoc invocation for converting large technical Word documents without corrupting tables or specs.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
