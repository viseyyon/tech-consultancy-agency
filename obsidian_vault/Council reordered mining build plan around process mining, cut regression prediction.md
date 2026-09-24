---
title: "Council reordered mining build plan around process mining, cut regression prediction"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "A five-seat AI council reviewed the viability of six planned mining initiatives and unanimously rated deterministic changelog process-mining (C2) as high-value and build-first (no ML needed, builds th"
tags: [knowledge, decisions-rationale, conf/high, durable, council-review, prioritization, process-mining, historical]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Council reordered mining build plan around process mining, cut regression prediction

## What it is

A five-seat AI council reviewed the viability of six planned mining initiatives and unanimously rated deterministic changelog process-mining (C2) as high-value and build-first (no ML needed, builds the extraction backbone, estimated 10-15% cycle-time compression potential), while cutting regression-hotspot prediction (P3) entirely - sub-1% positive rate and no version-control signal available meant any model would learn team habits rather than code risk, with revival conditional on Gerrit/commit data eventually landing. Duplicate detection was approved for deployment only as suggestions, never as an auto-blocking gate, because every council seat agreed false-positive trust collapse was the dominant failure mode. Fix-time prediction was approved only conditionally, gated on first naming both a concrete prediction target and a real operational consumer of the forecast - one seat noted a forecast with no consumer is shelfware and predictions can become self-fulfilling.

## Why it matters

Explains why process mining shipped first in practice and why regression prediction never appears later in the build history.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Conversation 2026-07-31 - council viability review

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
