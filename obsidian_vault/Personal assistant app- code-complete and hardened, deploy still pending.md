---
title: "Personal assistant app: code-complete and hardened, deploy still pending"
type: knowledge-entry
domain: "Project State"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 2
summary: "The personal assistant app (27 files) is a Next.js PWA phone client with a Vercel backend behind a blind Upstash Redis relay and a zero-dependency Node agent for Mac/Linux, hardened so a compromised s"
tags: [knowledge, project-state, conf/high, durable, personal-assistant, deployment, security, nextjs]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Personal assistant app: code-complete and hardened, deploy still pending

## What it is

The personal assistant app (27 files) is a Next.js PWA phone client with a Vercel backend behind a blind Upstash Redis relay and a zero-dependency Node agent for Mac/Linux, hardened so a compromised server cannot read or forge commands (non-extractable phone private key, command allowlist with no sudo/shell, E2E encryption, Ed25519-signed results, 5/5 crypto test suite passing). New devices require approval from an already-trusted device. The remaining step is deployment: create Upstash and Anthropic keys, deploy to Vercel production, and enroll the first device per the README.

## Why it matters

The app is finished and secured but not live -- deployment is the one remaining action, not a design gap.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Conversation 2026-07-29 - Personal assistant app development

---

Part of [[MOC - Project State]] · [[Home]]
