---
title: "Viseyyon's three domains (.com/.tech/.in) route SMS through one shared FastAPI + Jasmin SMPP bind pool"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: medium
durability: durable
evidence: 1
summary: "Since browsers can't speak SMPP (a stateful TCP protocol requiring a persistent bind), the architecture is website (HTTP/REST) -> backend SMPP client -> SMSC/aggregator -> handset. For viseyyon.com/.t"
tags: [knowledge, decisions-rationale, conf/medium, durable, sms, smpp, dlt-compliance, viseyyon]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Viseyyon's three domains (.com/.tech/.in) route SMS through one shared FastAPI + Jasmin SMPP bind pool

## What it is

Since browsers can't speak SMPP (a stateful TCP protocol requiring a persistent bind), the architecture is website (HTTP/REST) -> backend SMPP client -> SMSC/aggregator -> handset. For viseyyon.com/.tech/.in, the decision was one centralized backend, one SMPP bind pool, and one DLT registration under a single Viseyyon Technologies Principal Entity, with the three domains as origination-context tags rather than separate Sender IDs. India DLT compliance requires PE registration (~Rs 5,900 one-time), a 6-char alphanumeric Sender ID (e.g. VSEYON), and pre-registered templates with {#var#} placeholders. MSG91 was recommended as the starting aggregator.

## Why it matters

Consolidating under one Sender ID builds recall faster than fragmenting across three per-domain identities, at the cost of losing per-domain branding in SMS.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
