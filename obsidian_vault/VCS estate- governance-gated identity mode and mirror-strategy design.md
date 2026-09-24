---
title: "VCS estate: governance-gated identity mode and mirror-strategy design"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 2
summary: "The VCS extraction pipeline replaced a single global governance boolean with a per-instance x per-capability authorization matrix (mirror/hygiene/identity/embedding, deny-by-default) and added a third"
tags: [knowledge, developer-infrastructure, conf/high, durable, vcs, governance, privacy, architecture]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# VCS estate: governance-gated identity mode and mirror-strategy design

## What it is

The VCS extraction pipeline replaced a single global governance boolean with a per-instance x per-capability authorization matrix (mirror/hygiene/identity/embedding, deny-by-default) and added a third identity_mode value 'none' -- enforced structurally in code, never a config flag -- so hygiene-first extraction can ship with zero works-council dependency while identity-bearing extraction stays blocked pending sign-off. Mirror strategy prefers Chennai over Beijing (cheaper, faster) with Beijing as delta; shared accounts get a distinct identity-kind so bus factor renders 'unknown' rather than a falsely confident low number.

## Why it matters

The governance and identity-mode design is the mechanism that let the estate-hygiene product ship before legal sign-off landed, and any new capability must slot into the same matrix.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Conversation 2026-08-02 - VCS mining extension prompt + council round
- Cowork - Gerrit/Gitolite/GitHub setup (2026-08-15)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
