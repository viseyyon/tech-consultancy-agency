---
title: "Standardized engineer productivity formula: tickets_touched*3 + comments*1 + status_changes*2 + tickets_completed*5"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "Standard adopted for Vantiva Jira analytics tooling (weekly performance summaries, dashboards): productivity score = tickets_touched*3 + comments*1 + status_changes*2 + tickets_completed*5, weighting"
tags: [knowledge, decisions-rationale, conf/high, durable, productivity-scoring, jira-analytics, formula, vantiva]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Standardized engineer productivity formula: tickets_touched*3 + comments*1 + status_changes*2 + tickets_completed*5

## What it is

Standard adopted for Vantiva Jira analytics tooling (weekly performance summaries, dashboards): productivity score = tickets_touched*3 + comments*1 + status_changes*2 + tickets_completed*5, weighting completed tickets highest and merely-touched tickets lowest.

## Why it matters

This is the fixed scoring formula to reuse or reference when extending or auditing his team-performance scripts.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
