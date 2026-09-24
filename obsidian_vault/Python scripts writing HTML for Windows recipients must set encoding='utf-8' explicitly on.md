---
title: "Python scripts writing HTML for Windows recipients must set encoding='utf-8' explicitly on every file write"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "A generated log-analyzer script crashed on a colleague's Windows machine with UnicodeEncodeError because Windows' default cp1252 codec cannot encode emoji characters written into HTML templates withou"
tags: [knowledge, developer-infrastructure, conf/medium, durable, windows, unicode, encoding, python]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Python scripts writing HTML for Windows recipients must set encoding='utf-8' explicitly on every file write

## What it is

A generated log-analyzer script crashed on a colleague's Windows machine with UnicodeEncodeError because Windows' default cp1252 codec cannot encode emoji characters written into HTML templates without an explicit encoding argument; a follow-up run then hit a Jinja2 UnicodeDecodeError loading those same malformed template files.

## Why it matters

Always pass encoding='utf-8' on file writes (and avoid emoji in generated templates) when a script may run on a Windows machine other than the one it was authored on, to prevent this class of crash.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
