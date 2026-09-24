---
title: "CVA603 setup-environment supports env-var overrides via `_EXT` suffixes, replacing magic-number heredocs"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "The CVA603 REL build was being automated by piping numeric menu selections (e.g. `1 14 2 2 1 2`) into `setup-environment` via heredoc. Analysis of the script showed it already checks for `_EXT`-suffix"
tags: [knowledge, environment-tooling-state, conf/high, durable, cva603, build-automation, environment-variables, setup-environment]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# CVA603 setup-environment supports env-var overrides via `_EXT` suffixes, replacing magic-number heredocs

## What it is

The CVA603 REL build was being automated by piping numeric menu selections (e.g. `1 14 2 2 1 2`) into `setup-environment` via heredoc. Analysis of the script showed it already checks for `_EXT`-suffixed environment variables (WAN_EXT, DEVICE_VARIANT_EXT, IMAGE_TYPE_EXT, REGION_EXT, MAC14_EXT, SW_REL_VER_EXT, TSFS_EXT, SW_V6V_VER_EXT) before falling back to interactive menus, so exact string values (e.g. WAN_EXT=Cable, DEVICE_VARIANT_EXT=CVA603, IMAGE_TYPE_EXT=platform, REGION_EXT=NAM) can bypass prompts entirely.

## Why it matters

This converts a fragile, unmaintainable magic-number invocation into a self-documenting, version-controllable, CI/CD-ready configuration for any future build automation of this script.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
