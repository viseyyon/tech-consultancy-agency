---
title: "Claude Code needs Node 18+ (ReadableStream); GLIBC<2.28 systems need unofficial Node builds"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "Claude Code CLI's bundled fetch implementation requires the Web Streams API `ReadableStream` global, reliably present only in Node.js 18+; Node 16 fails outright. On systems with GLIBC < 2.28 (e.g. Ub"
tags: [knowledge, environment-tooling-state, conf/high, durable, claude-code, node-js, glibc, readablestream]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Claude Code needs Node 18+ (ReadableStream); GLIBC<2.28 systems need unofficial Node builds

## What it is

Claude Code CLI's bundled fetch implementation requires the Web Streams API `ReadableStream` global, reliably present only in Node.js 18+; Node 16 fails outright. On systems with GLIBC < 2.28 (e.g. Ubuntu 18.04 dev/CI Docker containers, GLIBC 2.27, hit on at least two separate occasions), standard Node 18 binaries fail with 'GLIBC_2.28 not found.'

## Why it matters

Workaround: install Node via unofficial-builds.nodejs.org (compiled against GLIBC 2.17) integrated into NVM using NVM_NODEJS_ORG_MIRROR, or containerize with a newer base image — the first thing to check whenever Claude Code fails to start on an older Linux CI image.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
