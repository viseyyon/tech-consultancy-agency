---
title: "Distinguish 'tracked in pipeline' from 'actively processed' when reporting AI throughput to management"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "A weekly report claimed '238 incidents processed' when only 47 RCA reports were actually completed (plus 9 in-progress = 56 actively worked, 161 still in backlog); 238 was the total tracked/in-pipelin"
tags: [knowledge, evaluation-observability, conf/high, durable, reporting, metrics, throughput, executive-reporting]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# Distinguish 'tracked in pipeline' from 'actively processed' when reporting AI throughput to management

## What it is

A weekly report claimed '238 incidents processed' when only 47 RCA reports were actually completed (plus 9 in-progress = 56 actively worked, 161 still in backlog); 238 was the total tracked/in-pipeline count, not throughput.

## Why it matters

Conflating tracked-count with completed-count inflates reported numbers — always separate total-tracked from actually-completed/actively-worked counts in AI capability reporting to keep metrics defensible.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
