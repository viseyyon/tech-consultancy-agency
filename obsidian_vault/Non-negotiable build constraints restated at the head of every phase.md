---
title: "Non-negotiable build constraints restated at the head of every phase"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "Across this user's build projects, certain constraints are treated as absolute and repeated verbatim at the start of every phase rather than assumed to still hold: secrets come from .env only (never i"
tags: [knowledge, security-guardrails, conf/high, durable, secrets, ssl, no-mock-data, governance]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Non-negotiable build constraints restated at the head of every phase

## What it is

Across this user's build projects, certain constraints are treated as absolute and repeated verbatim at the start of every phase rather than assumed to still hold: secrets come from .env only (never inline, never committed, never pasted in chat); SSL verification uses a CA bundle, never a hardcoded True or False; no mock/demo data anywhere; no microphone/getUserMedia access; governance/signoff flags default to false/deny; and progress is reported from rows actually committed, never from pages or requests issued.

## Why it matters

Any one of these being silently relaxed, a hardcoded verify=True, a stray secret, a request count standing in for a commit count, has already been the root cause of a real incident in this user's work.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Vantiva Jira and Confluence mining

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
