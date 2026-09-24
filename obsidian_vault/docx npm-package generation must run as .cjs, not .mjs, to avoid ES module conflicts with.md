---
title: "docx npm-package generation must run as .cjs, not .mjs, to avoid ES module conflicts with require()"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "Using the `docx` npm package, ES modules break `require()` calls; the reliable pattern is a `.cjs` main script plus a separate ES5-only helpers module (explicit `var`, `function` keyword callbacks, no"
tags: [knowledge, claude-code-practice, conf/high, durable, docx, nodejs, esm-vs-cjs, word-generation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# docx npm-package generation must run as .cjs, not .mjs, to avoid ES module conflicts with require()

## What it is

Using the `docx` npm package, ES modules break `require()` calls; the reliable pattern is a `.cjs` main script plus a separate ES5-only helpers module (explicit `var`, `function` keyword callbacks, no arrow functions). Syntax-check with `node --check` before running; `PageNumber` imports from `docx` can throw at runtime — replace with a static footer text string.

## Why it matters

Avoids module-system and runtime errors that silently break DOCX generation for future docx npm-package work.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
