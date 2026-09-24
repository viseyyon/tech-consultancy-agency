---
title: "Phase gates require ratification; enforce rules by construction, not discipline"
type: knowledge-entry
domain: "Operating Preferences"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "The user treats phase gates as hard stops: work pauses with named deliverables until the owner explicitly ratifies moving on, and no number is accepted unless it traces to a persisted artifact. Heuris"
tags: [knowledge, operating-preferences, conf/high, durable, phase-gate, ratification, enforcement, governance]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Operating Preferences]]"]
---

# Phase gates require ratification; enforce rules by construction, not discipline

## What it is

The user treats phase gates as hard stops: work pauses with named deliverables until the owner explicitly ratifies moving on, and no number is accepted unless it traces to a persisted artifact. Heuristic proposals live outside the active config until ratified. Rules (identity handling, exclusion lists, deny-by-default matrices) must be enforced structurally in code, not by convention, so they cannot silently drift. Infrastructure discovery is escalated to IT rather than probed directly, and a failure state is reported as a red or amber row rather than treated as a reason to stop reporting.

## Why it matters

Treating a proposal as ratified, or enforcing a rule only by convention, is how this user's projects have repeatedly shipped silent drift and false compliance.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Operating Preferences]] · [[Home]]
