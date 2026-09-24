---
title: "plan-auditor agent is structurally barred from editing the spec it audits"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "The Mining Console's plan-auditor agent (shipped as skill mining-plan-audit v2, council-hardened) treats its truth table and non-negotiables as immutable - any spec change it wants to propose goes int"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, plan-auditor, anti-drift, verification, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# plan-auditor agent is structurally barred from editing the spec it audits

## What it is

The Mining Console's plan-auditor agent (shipped as skill mining-plan-audit v2, council-hardened) treats its truth table and non-negotiables as immutable - any spec change it wants to propose goes into an append-only PLAN-CHANGE-PROPOSALS.md that only the human owner applies or rejects, preventing 'drift laundering' where an auditor slowly rewrites the spec to match broken code. To stop rubber-stamping, it must paste the output of 8 executed negative assertions (secrets-in-git, verify=False, forbidden analyses, etc.) with unresolved evidence defaulting to FAIL, and run active probes (health checks, a stale-PID trap comparing process-start time to last git commit, a full pytest run where any failure is an automatic violation) rather than trusting narrative reports.

## Why it matters

This is the mechanism that keeps the whole autonomous pipeline honest - without it the auditor could quietly certify broken phases as passing.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Conversation 2026-08-03 - audit agent creation + council round

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
