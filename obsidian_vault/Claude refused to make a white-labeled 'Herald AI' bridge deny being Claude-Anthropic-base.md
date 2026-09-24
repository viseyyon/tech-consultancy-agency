---
title: "Claude refused to make a white-labeled 'Herald AI' bridge deny being Claude/Anthropic-based, citing fraud/ToS risk"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "When asked to build a Claude Code bridge fully rebranded as 'Herald AI' by 'Viseyyon Technologies' with a system prompt instructing the model to deny any connection to Claude/Anthropic if asked, Claud"
tags: [knowledge, security-guardrails, conf/high, durable, white-label, herald-ai, tos, fraud-risk]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Claude refused to make a white-labeled 'Herald AI' bridge deny being Claude/Anthropic-based, citing fraud/ToS risk

## What it is

When asked to build a Claude Code bridge fully rebranded as 'Herald AI' by 'Viseyyon Technologies' with a system prompt instructing the model to deny any connection to Claude/Anthropic if asked, Claude flagged this as likely fraud/misrepresentation and a probable Anthropic ToS violation — building products on top of Claude's API is legitimate, but instructing the model to lie about its origin crosses into deceptive territory. The resolution offered was a transparent 'powered by Claude' white-label framing instead of denial-based branding.

## Why it matters

This is a concrete boundary marker for any future white-labeling request: rebranding is fine, but instructing denial of the underlying model is not.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
