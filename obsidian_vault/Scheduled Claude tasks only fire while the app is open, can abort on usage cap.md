---
title: "Scheduled Claude tasks only fire while the app is open, can abort on usage cap"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "Scheduled tasks (e.g. the Notion sync) inherit the model and session limits of the app session, and only actually fire while the Claude app is open. A 2026-08-04 evening fire aborted on its very first"
tags: [knowledge, environment-tooling-state, conf/medium, durable, scheduled-tasks, usage-limit, silent-failure]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Scheduled Claude tasks only fire while the app is open, can abort on usage cap

## What it is

Scheduled tasks (e.g. the Notion sync) inherit the model and session limits of the app session, and only actually fire while the Claude app is open. A 2026-08-04 evening fire aborted on its very first turn after hitting a usage limit (the model's "Fable 5 limit"), producing no phases run and no report; a silent miss rather than a visible failure.

## Why it matters

Assuming a scheduled task ran because it was scheduled, without checking for a produced report, can leave a sync or digest silently stale for a full cycle.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - notion-claude-two-way-sync (2026-08-05 run)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
