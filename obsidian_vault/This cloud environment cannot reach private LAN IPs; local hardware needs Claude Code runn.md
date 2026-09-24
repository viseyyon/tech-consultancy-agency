---
title: "This cloud environment cannot reach private LAN IPs; local hardware needs Claude Code running locally instead"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "An SSH attempt from this cloud environment to a Raspberry Pi 5 at a private IP (192.168.1.3) timed out due to network isolation between the cloud session and the local network. Workaround: build the d"
tags: [knowledge, environment-tooling-state, conf/high, durable, network-isolation, ssh, local-hardware, raspberry-pi]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# This cloud environment cannot reach private LAN IPs; local hardware needs Claude Code running locally instead

## What it is

An SSH attempt from this cloud environment to a Raspberry Pi 5 at a private IP (192.168.1.3) timed out due to network isolation between the cloud session and the local network. Workaround: build the deployment package here and execute it via Claude Code, OpenCode, or another CLI running locally on the target machine, or expose the device via a tunnel like ngrok/Tailscale.

## Why it matters

Direct SSH from this session to home/office LAN devices is not possible — plan any local-hardware task around building-then-handing-off, not remote execution.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
