---
title: "VCS governance: per-instance authorization matrix replaces one global sign-off boolean"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "The original brief gated all identity processing behind a single GOVERNANCE_SIGNOFF=false boolean, which can't express that an instance may be legitimately mirrorable for hygiene facts while still for"
tags: [knowledge, security-guardrails, conf/high, durable, governance, authorization-matrix, identity-mode, gdpr]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# VCS governance: per-instance authorization matrix replaces one global sign-off boolean

## What it is

The original brief gated all identity processing behind a single GOVERNANCE_SIGNOFF=false boolean, which can't express that an instance may be legitimately mirrorable for hygiene facts while still forbidden for identity facts. It was replaced with a deny-by-default matrix over {mirror_allowed, hygiene_facts, identity_facts, embedding} per VCS instance, each cell carrying its legal basis and audit reference; Phase 1 shipped all 9 instances deny-all, and grants were later issued only for gitolite_chennai, gitolite_beijing, and gerrit_ttm. A third identity_mode value, 'none,' was added and made the default - author/committer fields are never populated or even read from the object store, enforced structurally in code rather than as a flag any call site could ignore - which is what let repo-hygiene work (Goal 4) move from last to first in the plan, since hygiene has no legal-identity dependency at all.

## Why it matters

Any future grant or extension to this VCS mining system must go through the matrix and the identity_mode=none default, not a workaround boolean.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Gerrit/Gitolite/GitHub setup (2026-08-15)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
