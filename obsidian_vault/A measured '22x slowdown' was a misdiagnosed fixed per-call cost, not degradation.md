---
title: "A measured '22x slowdown' was a misdiagnosed fixed per-call cost, not degradation"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "When the Mining Console sync hit its stop condition (0.164 issues/s vs a 2.0 threshold) with 'root cause unknown,' investigation found there was no slowdown at all - every sync invocation paid a const"
tags: [knowledge, evaluation-observability, conf/high, durable, performance, root-cause, jira-sync, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# A measured '22x slowdown' was a misdiagnosed fixed per-call cost, not degradation

## What it is

When the Mining Console sync hit its stop condition (0.164 issues/s vs a 2.0 threshold) with 'root cause unknown,' investigation found there was no slowdown at all - every sync invocation paid a constant ~165s overhead (one project took 168s for a single issue) because the code fetched a summary of all 799 Jira projects before filtering to the one it needed. The apparent '22x degradation' was arithmetic on projects too small to amortize that fixed cost, and the operator's own 'smallest project first' instruction produced the worst possible rate estimate for exactly that reason. A related review-agent claim that a status-derivation feature was 'missing' was also false - the code existed and the reviewer hadn't grepped for it.

## Why it matters

Anyone re-diagnosing a Jira-sync performance regression on this codebase should check for the fetch-then-filter pattern before assuming the corpus or hardware changed.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- ESCALATION-005 ruling

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
