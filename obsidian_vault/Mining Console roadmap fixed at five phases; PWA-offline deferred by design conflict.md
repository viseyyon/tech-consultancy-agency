---
title: "Mining Console roadmap fixed at five phases; PWA/offline deferred by design conflict"
type: knowledge-entry
domain: "Project State"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 3
summary: "The remaining path to Mining Console v1 was fixed as five phases (Tier-1 close-out, assistant verification core, refusal-floor calibration, constrained WHY synthesis, lenses+battery, then the chat sur"
tags: [knowledge, project-state, conf/high, durable, roadmap, scope, offline-mode, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Mining Console roadmap fixed at five phases; PWA/offline deferred by design conflict

## What it is

The remaining path to Mining Console v1 was fixed as five phases (Tier-1 close-out, assistant verification core, refusal-floor calibration, constrained WHY synthesis, lenses+battery, then the chat surface+hardening), explicitly excluding several large parked datasets (55,267 identity-less issues, a 132-project Confluence reverse lookup, 1.3M parked issues) so the roadmap doesn't quietly carry them. Separately, PWA/offline mode (P12) stays deferred not for scheduling reasons but because an offline cache serves stale numbers by definition, which directly conflicts with the console's core promise that every number traces to a persisted artifact with its denominator - if ever built, it must aggressively stamp staleness and refuse to serve time-sensitive cached values rather than caveat them. A related build-target extraction rule: a row qualifies on content (a build command plus a resolvable target attribute), not on being inside a fenced code block, which is only a confidence boost.

## Why it matters

Anyone re-scoping this project needs the explicit exclusion list and the reason PWA isn't just 'not yet done' but structurally against the product's honesty guarantee.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-20)

---

Part of [[MOC - Project State]] · [[Home]]
