---
title: "VCS credential tier permits personal-key enumeration but hard-forbids bulk mirroring"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 3
summary: "Read-only enumeration (ls-remote, ssh info) is allowed to run on the operator's personal SSH key as long as every artifact's lineage is stamped credential_tier:personal, but bulk mirroring stays hard-"
tags: [knowledge, security-guardrails, conf/high, durable, credentials, estate-discovery, gdpr, vcs-mining]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# VCS credential tier permits personal-key enumeration but hard-forbids bulk mirroring

## What it is

Read-only enumeration (ls-remote, ssh info) is allowed to run on the operator's personal SSH key as long as every artifact's lineage is stamped credential_tier:personal, but bulk mirroring stays hard-forbidden until real service keys land. A narrow, time-boxed exception (A15b) was carved out purely to measure bytes-per-ref and WAN throughput: clone --mirror of at most 20 repos from the already-ratified scope, deleted immediately after measurement with the deletion logged, no data extraction of any kind. This sits on top of a corrected estate picture: the original brief's premises (a GitHub Enterprise Server, 4 systems, 31,895 mirror targets) were all wrong - there is no GHES (two GitHub Enterprise Cloud EMU tenants instead), and the real fetchable estate after dedup and exclusions is roughly 2,700-3,000 repos, with evidence of a third, unseen gitolite master node holding ~6,000 more repos that was escalated to IT rather than probed.

## Why it matters

Sets the exact boundary of what's allowed on a personal credential versus what needs service keys, and warns that estate-size numbers from the original brief are wrong by an order of magnitude.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Gerrit/Gitolite/GitHub setup (2026-08-15)
- VCS Phase 2 gate
- VCS realignment round 2 approval

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
