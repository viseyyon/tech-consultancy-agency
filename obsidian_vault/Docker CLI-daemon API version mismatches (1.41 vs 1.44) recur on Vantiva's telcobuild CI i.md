---
title: "Docker CLI/daemon API version mismatches (1.41 vs 1.44) recur on Vantiva's telcobuild CI infra"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "OpenWrt builds running via telcobuild-22.1 containers on Jenkins agents can fail with 'client version 1.41 is too old, minimum supported API version is 1.44' when the agent's Docker CLI is outdated re"
tags: [knowledge, environment-tooling-state, conf/medium, durable, docker, jenkins, openwrt, ci-infra]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Docker CLI/daemon API version mismatches (1.41 vs 1.44) recur on Vantiva's telcobuild CI infra

## What it is

OpenWrt builds running via telcobuild-22.1 containers on Jenkins agents can fail with 'client version 1.41 is too old, minimum supported API version is 1.44' when the agent's Docker CLI is outdated relative to the daemon. Fix: upgrade the agent's Docker client, set a DOCKER_API_VERSION env override, or connect directly to the daemon socket; longer-term fix is standardizing Jenkins agent Docker templates/base images.

## Why it matters

A recurring, identifiable failure signature on Vantiva's telcobuild CI infra with a known immediate fix and a longer-term standardization remedy.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
