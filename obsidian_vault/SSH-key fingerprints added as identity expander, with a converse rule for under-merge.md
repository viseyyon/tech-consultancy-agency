---
title: "SSH-key fingerprints added as identity expander, with a converse rule for under-merge"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "Gitolite/Gerrit/GitHub key listings are authoritative and deterministic enough to auto-merge identities on a fingerprint match, but only when that fingerprint maps to exactly one account per system an"
tags: [knowledge, security-guardrails, conf/high, durable, identity-resolution, ssh-keys, bus-factor, k-anonymity]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# SSH-key fingerprints added as identity expander, with a converse rule for under-merge

## What it is

Gitolite/Gerrit/GitHub key listings are authoritative and deterministic enough to auto-merge identities on a fingerprint match, but only when that fingerprint maps to exactly one account per system and isn't in the bot registry - a multi-account fingerprint downgrades to a flagged 'shared key' proposal instead of an automatic merge. The guard was found to be directional: it blocks over-merging distinct people into one identity but is blind to under-merging (e.g. a legacy account and an EMU account for the same real human staying as two separate identity rows) - so a converse rule was added: two fingerprints resolving to distinct accounts in the same system that share another authoritative attribute become a fragmentation proposal, not an automatic merge. Separately, shared/bot accounts (identified partly by a 'bp-' business-partner prefix) are a first-class identity state that never merges into a person and never feeds expertise or bus-factor metrics; a repo dominated by shared-account commits reports bus factor as 'unknown' rather than a false low number, and K-anonymity suppression counts resolved persons, not raw accounts.

## Why it matters

Anyone extending identity resolution on this VCS estate needs both merge guards - the over-merge guard alone silently misses split identities.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Gerrit/Gitolite/GitHub setup (2026-08-15)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
