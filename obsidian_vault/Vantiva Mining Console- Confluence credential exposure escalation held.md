---
title: "Vantiva Mining Console: Confluence credential exposure escalation held"
type: knowledge-entry
domain: "Open Commitments"
entry-type: "Caveat"
confidence: high
durability: ephemeral
evidence: 2
summary: "A scan of 4,505 Confluence pages found 37 with embedded credentials (passwords, tokens, one private key), but the escalation to the Confluence administrator was deliberately held rather than sent beca"
tags: [knowledge, open-commitments, conf/high, ephemeral, vantiva, confluence, credentials, security]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Open Commitments]]"]
---

# Vantiva Mining Console: Confluence credential exposure escalation held

## What it is

A scan of 4,505 Confluence pages found 37 with embedded credentials (passwords, tokens, one private key), but the escalation to the Confluence administrator was deliberately held rather than sent because the draft report's own space attribution was self-contradictory. Five corrections are required before sending: verify space_key against the URL for all 4,505 pages, manually triage the 37 into confirmed-secret/placeholder/needs-review, rank by what each credential opens, file the finding outside the repo, and state the scan is a floor not a total (attachments, comments, and Jira's error text were not scanned).

## Why it matters

This is a live, unresolved security escalation with named next steps -- sending it uncorrected would itself be an overstated finding.

## Provenance

- Confidence **high** · durability **ephemeral** · supported by **2** archived item(s).
- This is transient operational state and may already be stale.

## Sources

- Cowork - Vantiva Jira and Confluence mining (2026-08-16)

---

Part of [[MOC - Open Commitments]] · [[Home]]
