---
title: "VCS Estate Mining (Gerrit/Gitolite/GitHub): census and phase progress"
type: knowledge-entry
domain: "Project State"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 4
summary: "The VCS mining extension discovered a 7+ system estate (two Gerrits, two Gitolite mirrors, GitHub.com, two GitHub EMU tenants, GitLab) totalling 31,895 mirror targets, and found the real fetchable est"
tags: [knowledge, project-state, conf/high, durable, vantiva, vcs, gerrit, gitolite]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# VCS Estate Mining (Gerrit/Gitolite/GitHub): census and phase progress

## What it is

The VCS mining extension discovered a 7+ system estate (two Gerrits, two Gitolite mirrors, GitHub.com, two GitHub EMU tenants, GitLab) totalling 31,895 mirror targets, and found the real fetchable estate is only ~2,700-3,000 repos after exclusions and dedup because gitolite's 'info' reports ACL visibility, not serveability. Phases 1 and 2 gated and passed; Phase 3 (mirror engine, hygiene screens) was authorized; Phase 8's content_read pass was in flight. A restorability panel shipped: of 62 external build dependencies, 7 are unrestorable, split into two different problems, and a non-technical ESTATE-FINDINGS-BRIEF was delivered to IT/management citing six findings including two undocumented production Gerrits and a live cleartext GitHub PAT.

## Why it matters

Gives the current shape and scale of the VCS estate so future phases don't re-run discovery that already produced authoritative numbers.

## Provenance

- Confidence **high** · durability **durable** · supported by **4** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup (2026-08-16)
- Cowork - Gerrit/Gitolite/GitHub setup (2026-08-15)

---

Part of [[MOC - Project State]] · [[Home]]
