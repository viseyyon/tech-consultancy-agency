---
title: "Mining Console moved to an autonomous phase-loop with mandatory dual/six-agent review"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 2
summary: "After 8 phases of human-gated execution, the Vantiva Mining Console build switched to a self-driving 7-step loop (analyse, contract, generate, self-validate, dual-agent review, record, auto-proceed) r"
tags: [knowledge, agent-architecture-orchestration, conf/high, durable, autonomous-agents, dual-review, auditor-agents, phase-gates]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Mining Console moved to an autonomous phase-loop with mandatory dual/six-agent review

## What it is

After 8 phases of human-gated execution, the Vantiva Mining Console build switched to a self-driving 7-step loop (analyse, contract, generate, self-validate, dual-agent review, record, auto-proceed) run by a builder plus two independent reviewers (phase-reviewer verifies every criterion against the system not the report; scope-observer diffs actual vs declared scope) with a mechanical verdict matrix (PASS+CLEAN auto-proceeds, FAIL gets one repair then escalates, DRIFT reverts or amends the contract). This was later hardened into six adversarial auditor agents, each modeled on an actual defect class the project had produced (numbers, semantics, tests, authority, privacy, coverage), with an OPEN-ITEMS ledger and a fixed list of hard stops (credential findings, identity-bearing data, reversing an owner ruling, destructive ops) that force a pause for the human regardless of loop state.

## Why it matters

Anyone extending or trusting the Mining Console pipeline needs to know the auditors are load-bearing - the loop only advances autonomously because review is structurally separated from the builder, not because the work is unsupervised.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- R5 completion + autonomous loop delivery
- autonomous mode handover

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
