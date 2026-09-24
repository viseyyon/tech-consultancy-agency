---
title: "Sir's standard production-build prompt pattern: 4-role team with remote-deployment-confirmed gates per task"
type: knowledge-entry
domain: "Automation & Workflow"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "Standard production-build prompt structure: an Architect/Expert Programmer/UI-UX Engineer/QA Engineer team, where the Architect must produce a structured TODO plan before any code is written, no mock/"
tags: [knowledge, automation-workflow, conf/medium, durable, prompt-pattern, production-build, qa-gate, claude-code]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Automation & Workflow]]"]
---

# Sir's standard production-build prompt pattern: 4-role team with remote-deployment-confirmed gates per task

## What it is

Standard production-build prompt structure: an Architect/Expert Programmer/UI-UX Engineer/QA Engineer team, where the Architect must produce a structured TODO plan before any code is written, no mock/demo/stub code is allowed, and no TODO item is checked off until validated locally AND confirmed working in the live remote deployed system (including UI). Every backend change must have a corresponding UI update within the same gate.

## Why it matters

This is the reusable template for hardened engineering prompts going forward -- applying it prevents premature task completion and ensures backend/UI parity on every change.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Automation & Workflow]] · [[Home]]
