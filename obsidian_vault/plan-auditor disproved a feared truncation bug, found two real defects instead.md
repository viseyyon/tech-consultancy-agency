---
title: "plan-auditor disproved a feared truncation bug, found two real defects instead"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "A suspected changelog-truncation bug (zero fallback triggers across 57k synced issues, when Jira DC was believed to cap expand=changelog around 100 entries) was disproven by direct comparison - wareho"
tags: [knowledge, evaluation-observability, conf/high, durable, changelog, verification, false-alarm, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# plan-auditor disproved a feared truncation bug, found two real defects instead

## What it is

A suspected changelog-truncation bug (zero fallback triggers across 57k synced issues, when Jira DC was believed to cap expand=changelog around 100 entries) was disproven by direct comparison - warehouse row counts matched live Jira exactly with no pile-up at 100, so the 'commonly truncated at 100' claim in the project spec itself was false on both Jira instances. But the same investigation found two real, previously-hidden defects: the single-issue changelog fallback endpoint (/rest/api/2/issue/{key}/changelog) 404s on both instances, so the untested recovery path would error rather than recover if truncation ever did occur; and Vantiva sync failures were read-timeouts caused by the extractor requesting fields=*all in violation of its own field-projection rule.

## Why it matters

Shows that 'the fear turned out to be false' doesn't mean 'audit clean' - the same pass that clears one suspicion is exactly where the real defects were sitting.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- plan-auditor run 2 - fallback disproof
- plan-auditor baseline run 2026-08-04

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
