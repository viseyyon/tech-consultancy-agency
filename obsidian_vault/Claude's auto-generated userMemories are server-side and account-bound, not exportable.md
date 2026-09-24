---
title: "Claude's auto-generated userMemories are server-side and account-bound, not exportable"
type: knowledge-entry
domain: "Agent Memory"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "Confirmed while migrating context to a new Claude account: auto-generated userMemories live server-side per account and cannot be exported via UI or API. The functional workaround is a manually-mainta"
tags: [knowledge, agent-memory, conf/high, durable, user-memories, account-migration, context-seed, memory-portability]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Memory]]"]
---

# Claude's auto-generated userMemories are server-side and account-bound, not exportable

## What it is

Confirmed while migrating context to a new Claude account: auto-generated userMemories live server-side per account and cannot be exported via UI or API. The functional workaround is a manually-maintained 'Context Seed Prompt' (identity, active systems, workstreams, technical knowledge) pasted as the first message on the new account, plus the User Preferences block pasted into Settings, rather than any true memory transfer.

## Why it matters

Manual memory_user_edits, if any exist, are the only memory layer that could theoretically be replicated by re-issuing the same edit commands — relevant to any future account migration or memory-continuity effort.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Memory]] · [[Home]]
