---
title: "Microsoft Graph rate-limits the Teams sweep per search, not per run"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "The Teams-priority-digest sweep hits Microsoft Graph rate limits per individual search rather than per overall run; one sweep can return 43/50 chats for one keyword and 29/50 for another. The at-menti"
tags: [knowledge, environment-tooling-state, conf/high, durable, microsoft-graph, rate-limit, teams, coverage-gap]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Microsoft Graph rate-limits the Teams sweep per search, not per run

## What it is

The Teams-priority-digest sweep hits Microsoft Graph rate limits per individual search rather than per overall run; one sweep can return 43/50 chats for one keyword and 29/50 for another. The at-mentions-of-Surendran search fails hardest, hitting 429 on both the initial call and its single retry, so on a throttled run direct mentions are simply not covered and that gap must be stated explicitly rather than left implied by silence. Teams items also come back with webUrl null (links fall back to the Outlook mirror, or have no link at all), and chat-list last-updated timestamps reflect renames or membership changes rather than the last message, understating real activity.

## Why it matters

Treating a quiet digest section as "nothing happened" rather than "coverage was throttled" reports false confidence about what was actually checked.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Teams priority digest

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
