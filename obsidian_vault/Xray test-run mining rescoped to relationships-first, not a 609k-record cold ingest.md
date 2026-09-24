---
title: "Xray test-run mining rescoped to relationships-first, not a 609k-record cold ingest"
type: knowledge-entry
domain: "Project State"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "The original C7 Xray-mining scope assumed 609,349 records had to be ingested from scratch, but reconciliation showed 257,030 were already on disk inside issues already synced for other reasons. The ch"
tags: [knowledge, project-state, conf/high, durable, xray, scoping, ingest-order, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Xray test-run mining rescoped to relationships-first, not a 609k-record cold ingest

## What it is

The original C7 Xray-mining scope assumed 609,349 records had to be ingested from scratch, but reconciliation showed 257,030 were already on disk inside issues already synced for other reasons. The chosen path (Option A) mines test-run relationships for the shells that already exist and ships QA analytics on them immediately, backfilling the remaining ~352,319 shells afterward - rejecting the alternative of completing the full sync first - because the analytic value (execution x test case with status) attaches to existing shells without a re-fetch. This cut the rescoped estimate to 18-27 staged, resumable hours.

## Why it matters

Explains why QA analytics shipped well before the full Xray corpus was synced, and why re-scoping the ingest order is safe to reuse on future large syncs.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-14 session)

---

Part of [[MOC - Project State]] · [[Home]]
