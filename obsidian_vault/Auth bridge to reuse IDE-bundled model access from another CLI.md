---
title: "Auth bridge to reuse IDE-bundled model access from another CLI"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: low
durability: durable
evidence: 4
summary: "NoeFabris/opencode-antigravity-auth lets the Opencode CLI authenticate against Google's Antigravity IDE via OAuth, reusing Antigravity's rate limits and model access, such as Gemini 3 Pro, instead of"
tags: [knowledge, developer-infrastructure, conf/low, durable, auth-bridge, opencode, antigravity, model-access]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Auth bridge to reuse IDE-bundled model access from another CLI

## What it is

NoeFabris/opencode-antigravity-auth lets the Opencode CLI authenticate against Google's Antigravity IDE via OAuth, reusing Antigravity's rate limits and model access, such as Gemini 3 Pro, instead of paying for separate API access.

## Why it matters

A pattern worth knowing when a CLI tool does not natively support a model already reachable through an IDE-bundled subscription.

## Provenance

- Confidence **low** · durability **durable** · supported by **4** archived item(s).
- Low confidence: the only evidence was a creator's headline. Treat as a lead, not a fact.

## Sources

- https://github.com/NoeFabris/opencode-antigravity-auth
- https://github.com/NoeFabris/opencode-antigravity-auth/blob/main/docs/CONFIGURATION.md

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
