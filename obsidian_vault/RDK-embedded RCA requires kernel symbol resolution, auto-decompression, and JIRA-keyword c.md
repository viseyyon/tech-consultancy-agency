---
title: "RDK/embedded RCA requires kernel symbol resolution, auto-decompression, and JIRA-keyword context before analysis"
type: knowledge-entry
domain: "Project State"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "Hard requirements for Vantiva's RCA orchestrator: kernel addresses must be resolved to function+source-line via addr2line/System.map/kallsyms fallback before analysis; compressed logs (.gz/.bz2/.xz/.z"
tags: [knowledge, project-state, conf/high, durable, rca, rdk, kernel-debugging, zero-hallucination]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# RDK/embedded RCA requires kernel symbol resolution, auto-decompression, and JIRA-keyword context before analysis

## What it is

Hard requirements for Vantiva's RCA orchestrator: kernel addresses must be resolved to function+source-line via addr2line/System.map/kallsyms fallback before analysis; compressed logs (.gz/.bz2/.xz/.zip/.tar.*) must be auto-extracted first; JIRA ticket text must be scanned against a 200+-keyword database across 8 categories to seed context; every RCA claim must cite an exact source location plus a 5-line snippet, under a zero-hallucination policy.

## Why it matters

These are binding preconditions for any embedded/RDK RCA tooling — skipping them would produce unverifiable or hallucinated root-cause claims.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
