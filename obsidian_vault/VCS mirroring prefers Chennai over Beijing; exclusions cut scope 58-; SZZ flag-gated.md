---
title: "VCS mirroring prefers Chennai over Beijing; exclusions cut scope 58%; SZZ flag-gated"
type: knowledge-entry
domain: "Project State"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "Chennai and Beijing gitolite nodes serve overlapping repos, but Chennai is preferred (44% of shared names served there vs 25% for Beijing, and ~3x cheaper per-connection since Beijing is WAN-bound) wi"
tags: [knowledge, project-state, conf/high, durable, mirroring, namespace-exclusion, szz, vcs-mining]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# VCS mirroring prefers Chennai over Beijing; exclusions cut scope 58%; SZZ flag-gated

## What it is

Chennai and Beijing gitolite nodes serve overlapping repos, but Chennai is preferred (44% of shared names served there vs 25% for Beijing, and ~3x cheaper per-connection since Beijing is WAN-bound) with Beijing used only as a fallback delta and unreached names recorded as 'third_master' rather than treated as failures. Twelve proposed upstream-mirror namespace exclusions (AOSP mirrors under five different roots, external, various vendor Android forks) were ratified for 11 of 12, cutting distinct repo names by 58.5%; the twelfth (bootloader/u-boot forks) was deliberately held in scope because those forks often carry real Vantiva integration work. SZZ-style bug-inducing-commit blame tracing was split behind a feature flag after one council model called it a pure noise generator: v1 ships only deterministic bug-fix-touch density at module grain, with SZZ-lite aggregate-only and never person-attributed if it ships at all.

## Why it matters

Sets the concrete mirroring priority order and scope boundary for anyone resuming VCS ingestion, and the guardrail on ever shipping blame-style analysis.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Gerrit/Gitolite/GitHub setup (2026-08-15)

---

Part of [[MOC - Project State]] · [[Home]]
