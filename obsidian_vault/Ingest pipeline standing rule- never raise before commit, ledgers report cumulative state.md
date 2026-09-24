---
title: "Ingest pipeline standing rule: never raise before commit, ledgers report cumulative state"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 5
summary: "After a NUL byte in one 2017 Jira record rolled back all 3,363 committed rows in a batch, and a counter self-check nearly reproduced the same bug, the pipeline adopted a permanent rule: validation may"
tags: [knowledge, evaluation-observability, conf/high, durable, quarantine, data-integrity, ledger, ingest]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# Ingest pipeline standing rule: never raise before commit, ledgers report cumulative state

## What it is

After a NUL byte in one 2017 Jira record rolled back all 3,363 committed rows in a batch, and a counter self-check nearly reproduced the same bug, the pipeline adopted a permanent rule: validation may log, mark, and report a mismatch but must never raise/rollback before the commit - persisted status gets one of four explicit states (completed / completed_with_quarantine / completed_with_counter_mismatch / both) rather than a plain 'completed' that hides the problem. Uncommittable rows go to an ingest_quarantine table (isolate, don't discard) rather than being fixed only for the one known offender (NUL bytes) while missing the sibling case (lone UTF-16 surrogates). Any persistent counter must be reported as total/resolved/outstanding grouped by cause on every run, never just the delta, and must never be reconstructed from the rows it exists to audit (that's circular and was itself a repeat defect).

## Why it matters

This is the difference between a sync that silently eats data and one that isolates and surfaces every bad row - breaking it reintroduces the original data-loss incident.

## Provenance

- Confidence **high** · durability **durable** · supported by **5** archived item(s).

## Sources

- R5-fix v2 delivery
- R4 result review + R5 filing
- ESCALATION-007 ruling
- D3 corrected review

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
