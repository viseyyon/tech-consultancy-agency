---
title: "Surendran's AOSP rebase automation remembers per-repo-pattern conflict resolutions across runs"
type: knowledge-entry
domain: "Automation & Workflow"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "The AOSP auto-rebase script syncs latest AOSP, rebases platform then modified projects, and on merge conflicts offers per-repo choices (upstream/downstream/manual/skip). It includes 'smart memory' tha"
tags: [knowledge, automation-workflow, conf/high, durable, aosp, rebase-automation, merge-conflicts, git]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Automation & Workflow]]"]
---

# Surendran's AOSP rebase automation remembers per-repo-pattern conflict resolutions across runs

## What it is

The AOSP auto-rebase script syncs latest AOSP, rebases platform then modified projects, and on merge conflicts offers per-repo choices (upstream/downstream/manual/skip). It includes 'smart memory' that remembers a chosen resolution for a repo-name pattern (e.g. always take upstream for frameworks/*) so future conflicts in similarly named repos auto-resolve without re-prompting.

## Why it matters

Reduces repeated manual conflict-resolution effort across AOSP rebase runs over time.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Automation & Workflow]] · [[Home]]
