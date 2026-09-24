---
title: "A white-background slide retheme needs a full color-token rewrite, not a single background swap"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "When converting a dark-theme deck to white background, dark card fills and light text become invisible unless every color token (backgrounds, card fills, borders, text colors) is rewritten together. A"
tags: [knowledge, environment-tooling-state, conf/medium, durable, deck-design, color-tokens, retheme, white-background]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# A white-background slide retheme needs a full color-token rewrite, not a single background swap

## What it is

When converting a dark-theme deck to white background, dark card fills and light text become invisible unless every color token (backgrounds, card fills, borders, text colors) is rewritten together. A single background-property swap leaves unreadable dark-on-dark or invisible light text.

## Why it matters

Any future dark-to-light deck retheme must rewrite the full color-token set at once, not just the background property, or the result will be unreadable.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
