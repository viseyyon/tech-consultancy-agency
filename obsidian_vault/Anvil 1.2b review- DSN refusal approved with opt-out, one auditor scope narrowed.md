---
title: "Anvil 1.2b review: DSN refusal approved with opt-out, one auditor scope narrowed"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "In the Anvil project's phase-review loop, a hard refusal on undetermined database DSNs was approved but only with a required, logged opt-out path (no execution can proceed silently without either a de"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, anvil, phase-review, reflexivity, refusal]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Anvil 1.2b review: DSN refusal approved with opt-out, one auditor scope narrowed

## What it is

In the Anvil project's phase-review loop, a hard refusal on undetermined database DSNs was approved but only with a required, logged opt-out path (no execution can proceed silently without either a declared DSN or a recorded manual override). One meta-check (M4) was explicitly NOT granted access to review its own gating script, because that would have made the check evaluate its own gate (reflexivity) - the mis-read that prompted the request became a separately owned fifth item instead, preserving the intended four-item meta-check scope. A companion safety claim (that a config-loading path 'fails open' safely) was challenged as unsupported by evidence and required either a demonstrated fail-open consumer or formal withdrawal.

## Why it matters

A concrete example of the project's 'auditor must not certify its own gate' and 'no claim without evidence' rules being applied to real review requests, useful if similar requests recur.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Anvil project analysis (session local_bd1187ab)

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
