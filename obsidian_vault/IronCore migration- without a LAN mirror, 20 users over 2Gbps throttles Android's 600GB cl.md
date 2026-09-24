---
title: "IronCore migration: without a LAN mirror, 20 users over 2Gbps throttles Android's 600GB clone to 13.3 hours"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Claim"
confidence: medium
durability: durable
evidence: 2
summary: "Bandwidth modeling for the IronCore Source Code Migration Programme (Android 600GB, RDK Broadband 300GB, Homeware 400GB, ~6.4TB total) found that without an internal LAN mirror, 2Gbps split across 20"
tags: [knowledge, decisions-rationale, conf/medium, durable, ironcore, bandwidth, lan-mirror, risk-assessment]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# IronCore migration: without a LAN mirror, 20 users over 2Gbps throttles Android's 600GB clone to 13.3 hours

## What it is

Bandwidth modeling for the IronCore Source Code Migration Programme (Android 600GB, RDK Broadband 300GB, Homeware 400GB, ~6.4TB total) found that without an internal LAN mirror, 2Gbps split across 20 concurrent users yields only 100Mbps (12.5MB/s) per user; with a 10Gbps LAN mirror each user gets 512Mbps (64MB/s) — a 5.1x speedup, cutting Android's clone time from 13.3 to 2.6 hours. Moving to 3x-daily Gerrit-to-GitHub sync introduces two new HIGH-severity risks: IAM drift between Gerrit ACLs and GitHub RBAC, and QoS saturation when CI runners and developer clones coincide with sync pushes. Full 117-project classification (48 LOW/18 MEDIUM/12 HIGH/39 ASSESS) across 36,693 repos and 13 servers is estimated at ~635 person-days over an 18-month programme.

## Why it matters

Justifies investing in a LAN mirror for the migration and flags two specific new risks that need mitigation if sync frequency increases.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
