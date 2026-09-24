---
title: "CLAUDE.md as a project's authority-order document, paired with a RUNBOOK"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "For the Mining Console project, the repo's CLAUDE.md is auto-loaded by Claude Code and declares a document authority order (which prompt/spec supersedes which), marks superseded docs as historical-do-"
tags: [knowledge, claude-code-practice, conf/medium, durable, claude-md, runbook, authority-order, project-setup]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# CLAUDE.md as a project's authority-order document, paired with a RUNBOOK

## What it is

For the Mining Console project, the repo's CLAUDE.md is auto-loaded by Claude Code and declares a document authority order (which prompt/spec supersedes which), marks superseded docs as historical-do-not-follow, lists non-negotiable rules, and records environment facts and cautions (host, port, stale-pid trap, deprecated services). A companion RUNBOOK.md gives the operator sequence: preconditions, phase-by-phase paste order, run/operate commands, and disaster-recovery notes.

## Why it matters

Without a single authority document, an agent working across many superseding prompts/specs can act on a stale or overridden instruction.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Vantiva Jira and Confluence mining

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
