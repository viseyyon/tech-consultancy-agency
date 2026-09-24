---
title: "Verification discipline: real question, balanced ledgers, trust no report"
type: knowledge-entry
domain: "Operating Preferences"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 2
summary: "The user requires: probing systems with the actual client question rather than a constructed proxy; never renaming domain vocabulary just to make an over-matching check pass (narrow the check instead)"
tags: [knowledge, operating-preferences, conf/high, durable, verification, ledger, measurement, audit]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Operating Preferences]]"]
---

# Verification discipline: real question, balanced ledgers, trust no report

## What it is

The user requires: probing systems with the actual client question rather than a constructed proxy; never renaming domain vocabulary just to make an over-matching check pass (narrow the check instead); ledgers that balance exactly with counters committed in the same transaction as the rows they count; every claim verified by re-running the query against the database, never accepted from a report; a check never observed failing on a deliberate violation does not count as a check; and cumulative state (total/resolved/outstanding) reported every time, not just the delta.

## Why it matters

Skipping any one of these has already produced real incidents for this user: silently lost rows, a check that passed vacuously, and a report that overstated results the underlying data didn't support.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Cowork - Vantiva Jira and Confluence mining
- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Operating Preferences]] · [[Home]]
