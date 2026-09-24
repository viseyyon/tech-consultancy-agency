---
title: "Platform/SoC dimension modeling: many-to-many bitemporal bridges, curated not ML"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 2
summary: "After a five-seat council review, the platform/SoC/product dimension layer for Jira/Confluence mining was redesigned around bridge tables rather than single-valued columns (a shared hardware-abstracti"
tags: [knowledge, decisions-rationale, conf/high, durable, dimensional-modeling, scd2, taxonomy, historical]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Platform/SoC dimension modeling: many-to-many bitemporal bridges, curated not ML

## What it is

After a five-seat council review, the platform/SoC/product dimension layer for Jira/Confluence mining was redesigned around bridge tables rather than single-valued columns (a shared hardware-abstraction-layer component can span multiple SoCs; middleware can span both RDK-V and Android TV), keyed on immutable Jira IDs rather than names, with bitemporal versioning (SCD Type-2 effective dates plus immutable pinned mapping releases) so that later reclassification of a codebase never retroactively regroups already-mined tickets. The dimension itself is explicitly a curated, versioned lookup table built during discovery/EDA - not a fifth machine-learning pipeline - populated by harvesting project/component/label names, seeding rules from known SoC vendor part prefixes, and routing anything ambiguous to a measured 'unclassified' bucket rather than hiding it.

## Why it matters

The bitemporal/bridge-table shape and the 'curated table, not a model' framing govern how any future taxonomy dimension should be added to this system.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Conversation 2026-07-31 - council dimension-layer review
- Jira/Confluence mining playbook session

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
