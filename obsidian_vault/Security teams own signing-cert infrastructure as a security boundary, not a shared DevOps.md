---
title: "Security teams own signing/cert infrastructure as a security boundary, not a shared DevOps service"
type: knowledge-entry
domain: "Operating Preferences"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "From a bootloader-signing incident (Vodafone FGV530T): when a security team (e.g. Briag on Crypto/signing) rejects a build via their validation tooling, the correct posture is to acknowledge the verdi"
tags: [knowledge, operating-preferences, conf/high, durable, security-boundary, signing, incident-response, crypto-team]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Operating Preferences]]"]
---

# Security teams own signing/cert infrastructure as a security boundary, not a shared DevOps service

## What it is

From a bootloader-signing incident (Vodafone FGV530T): when a security team (e.g. Briag on Crypto/signing) rejects a build via their validation tooling, the correct posture is to acknowledge the verdict as legitimate gatekeeping and defer, not diagnose their tooling as broken and route around it — even when a real secondary bug exists in parallel. Engineering should own documentation gaps explicitly, use observation language ('appears to,' 'if that reading is correct') rather than outside diagnosis, and never use customer timeline pressure to bypass a security gate.

## Why it matters

Security teams respond well to verifiable observations and poorly to being told their gate is wrong, so getting this posture wrong risks damaging trust with the signing/crypto team during future incidents.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Operating Preferences]] · [[Home]]
