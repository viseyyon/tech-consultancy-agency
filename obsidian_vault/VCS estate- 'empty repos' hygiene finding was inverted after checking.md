---
title: "VCS estate: 'empty repos' hygiene finding was inverted after checking"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "An owner instruction to publish '850 repositories advertise no refs at all' was checked against the A16 tier's own ref counts before publishing and found wrong by more than 4x: only 200 repos are genu"
tags: [knowledge, evaluation-observability, conf/high, durable, vcs, data-quality, git, measurement]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# VCS estate: 'empty repos' hygiene finding was inverted after checking

## What it is

An owner instruction to publish '850 repositories advertise no refs at all' was checked against the A16 tier's own ref counts before publishing and found wrong by more than 4x: only 200 repos are genuinely empty, while 828 have a dangling HEAD (a branch name that doesn't exist) despite holding real content -- confirmed live against git's own behavior, not a warehouse artifact. The fix distinguishes a new head_unborn state from true emptiness, upgrading the finding from a hygiene footnote to an actionable defect (828 repos would clone to an empty working tree).

## Why it matters

A concrete, once-published-wrong number to remember before trusting any future 'empty repo' style hygiene metric from this estate.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup (2026-08-16)

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
