---
title: "Gerrit-to-GitHub migration needs a --mirror clone, and refs/changes/* usually should be excluded"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "A standard git clone misses Gerrit-specific refs (refs/changes/* patchset history, refs/meta/config project config), so full-fidelity migration requires 'git clone --mirror'. Branches and tags always"
tags: [knowledge, developer-infrastructure, conf/high, durable, gerrit, github-migration, git-mirror, refs]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Gerrit-to-GitHub migration needs a --mirror clone, and refs/changes/* usually should be excluded

## What it is

A standard git clone misses Gerrit-specific refs (refs/changes/* patchset history, refs/meta/config project config), so full-fidelity migration requires 'git clone --mirror'. Branches and tags always migrate; refs/changes/* should only be pushed to GitHub if there's a specific compliance/audit reason to preserve every patchset — otherwise leave Gerrit read-only as the archive and keep GitHub clean, since these refs often make up the majority of repo objects. Verify fidelity with 'git ls-remote' and SHA comparison; watch for Git LFS objects, open reviews, and CI config living outside Git objects.

## Why it matters

Following this reduces migration risk and repo bloat for any future Gerrit-to-GitHub move, since naively copying all refs would carry over most of the repo's non-essential object weight.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
