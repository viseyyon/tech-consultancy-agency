---
title: "Xray QA metrics split pass-rate from execution-rate and zombies into two buckets"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "A single 'pass rate' was conflating firmware quality with how much of the test suite actually ran, so the QA marts now report pass_rate = passing/executed and execution_rate = executed/all separately;"
tags: [knowledge, evaluation-observability, conf/high, durable, qa-metrics, xray, pass-rate, zombie-tests]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# Xray QA metrics split pass-rate from execution-rate and zombies into two buckets

## What it is

A single 'pass rate' was conflating firmware quality with how much of the test suite actually ran, so the QA marts now report pass_rate = passing/executed and execution_rate = executed/all separately; PASS_WITH_MINOR_BUGS counts as a terminal pass (72.5% including it vs 66.5% excluding, a 6-point swing) but renders as its own series in charts so the caveat stays visible, and OUT_OF_SCOPE runs are excluded from the executed denominator via a new is_executed column. The 'zombie' inventory (tests with no recent runs) was likewise split into never_scheduled (a coverage gap) versus scheduled_not_run (all runs in-window are still TODO, an execution gap) - the second turned out to be the larger, sharper story at 11.7-12.4% of all runs, which a single zombie count would have hidden entirely.

## Why it matters

Anyone reading a single Xray pass-rate or zombie number from this system is reading a number that has already hidden a real distinction - the split view is the only trustworthy one.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-14 session)

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
