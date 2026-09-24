---
title: "MS Teams webhooks reject Adaptive Card Table elements (need v1.5); use ColumnSet layouts (v1.2) instead"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "A JIRA-to-Teams dashboard's Adaptive Card posts silently failed in production (test connection worked, actual posts didn't) because Table elements require Adaptive Card schema v1.5, but Microsoft Team"
tags: [knowledge, developer-infrastructure, conf/high, durable, microsoft-teams, adaptive-cards, webhooks, jira-integration]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# MS Teams webhooks reject Adaptive Card Table elements (need v1.5); use ColumnSet layouts (v1.2) instead

## What it is

A JIRA-to-Teams dashboard's Adaptive Card posts silently failed in production (test connection worked, actual posts didn't) because Table elements require Adaptive Card schema v1.5, but Microsoft Teams incoming webhooks typically only support up to v1.2. Fix: rebuild card layouts using ColumnSet instead of Table.

## Why it matters

Avoids silent production failures in any future Teams-webhook Adaptive Card integration.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
