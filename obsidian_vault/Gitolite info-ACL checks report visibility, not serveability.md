---
title: "Gitolite info/ACL checks report visibility, not serveability"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "Running ssh info against a gitolite mirror node can report full read/write/execute access while git ls-remote against the same path fails with a mirrored-but-not-here error; gitolite mirror mode repor"
tags: [knowledge, developer-infrastructure, conf/medium, durable, gitolite, git, mirroring, serveability]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Gitolite info/ACL checks report visibility, not serveability

## What it is

Running ssh info against a gitolite mirror node can report full read/write/execute access while git ls-remote against the same path fails with a mirrored-but-not-here error; gitolite mirror mode reports ACL visibility, not whether the repo is actually served locally. In this estate roughly 42% of a sampled set of shared repo names were served by neither of two known mirror nodes, revealing an unseen third master holding thousands of repos.

## Why it matters

Treating ACL-visible as fetchable overstates a mirrored estate's real size and reachable population by a wide margin.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
