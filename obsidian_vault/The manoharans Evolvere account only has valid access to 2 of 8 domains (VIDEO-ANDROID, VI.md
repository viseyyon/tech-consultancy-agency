---
title: "The manoharans Evolvere account only has valid access to 2 of 8 domains (VIDEO-ANDROID, VIDEO-NON-ANDROID)"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "The Evolvere platform (with a web UI and separate API port) has 8 business domains -- VIDEO-ANDROID, VIDEO-NON-ANDROID, VIDEO-LEGACY, BB-CABLE, BB-TELCO, PROFESSIONAL SERVICES, IOT, NAVIGATE -- but hi"
tags: [knowledge, environment-tooling-state, conf/medium, durable, evolvere, access-control, credentials, domain-scoping]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# The manoharans Evolvere account only has valid access to 2 of 8 domains (VIDEO-ANDROID, VIDEO-NON-ANDROID)

## What it is

The Evolvere platform (with a web UI and separate API port) has 8 business domains -- VIDEO-ANDROID, VIDEO-NON-ANDROID, VIDEO-LEGACY, BB-CABLE, BB-TELCO, PROFESSIONAL SERVICES, IOT, NAVIGATE -- but his manoharans login only authenticates successfully against VIDEO-ANDROID and VIDEO-NON-ANDROID; the other six domains return 'Invalid credentials.'

## Why it matters

Any live-data pull from Evolvere for the six non-authorized domains needs separate access granted first, or the pull will silently fail with an auth error.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
