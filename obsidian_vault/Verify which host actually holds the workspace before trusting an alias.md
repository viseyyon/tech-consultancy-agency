---
title: "Verify which host actually holds the workspace before trusting an alias"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "An ssh-docker host alias can point somewhere other than where the real work lives: moonknight (10.17.58.133) was registered and initially assumed to be the workspace/mirror host, but its home director"
tags: [knowledge, developer-infrastructure, conf/medium, durable, host-alias, ssh, workspace, caution]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Verify which host actually holds the workspace before trusting an alias

## What it is

An ssh-docker host alias can point somewhere other than where the real work lives: moonknight (10.17.58.133) was registered and initially assumed to be the workspace/mirror host, but its home directory was empty with no /data volume; the actual Claude Code workspace and census data lived on a different, much larger box. The working host alias for the Anvil project is 'project' = manoharans@10.17.58.113, distinct from Anvil's production box at 10.17.58.112.

## Why it matters

Applying capacity figures, credentials, or file paths to the wrong host produces confidently wrong conclusions about disk space, workspace state, or what was actually run.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
