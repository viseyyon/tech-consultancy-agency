---
title: "Broadcom's SLA safe harbor requires genuine air-gap, not enterprise cloud controls, for source code"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 1
summary: "Vantiva's AIRLOCK campaign resolved the Broadcom SLA compliance letter (Apr 29 2026) by determining that only true on-prem, air-gapped inference (Option A) satisfies the SLA's 'non-airgapped, third-pa"
tags: [knowledge, decisions-rationale, conf/high, durable, broadcom, sla, air-gap, compliance]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Broadcom's SLA safe harbor requires genuine air-gap, not enterprise cloud controls, for source code

## What it is

Vantiva's AIRLOCK campaign resolved the Broadcom SLA compliance letter (Apr 29 2026) by determining that only true on-prem, air-gapped inference (Option A) satisfies the SLA's 'non-airgapped, third-party cloud-hosted AI platform' prohibition for Broadcom-licensed source code. Option C (Azure AI Foundry + enterprise controls, even tenant-isolated) was ruled non-compliant for Broadcom source specifically; Option B (other vendor-approved cloud) was left conditional on Legal's ruling.

## Why it matters

This makes air-gap the mandatory routing default whenever Broadcom source code is involved, distinct from the general AI tooling policy that treats Azure AI Foundry as sufficiently controlled for other work.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
