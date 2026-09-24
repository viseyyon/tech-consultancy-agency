---
title: "Sandboxed runtime layer underneath agent frameworks"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 6
summary: "NVIDIA's OpenShell provides an isolated execution environment for autonomous agents, with NemoClaw as a hardened wrapper for running third-party agent frameworks (Hermes, LangChain Deep Agents, OpenCl"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, sandbox, agent-runtime, security, nvidia]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Sandboxed runtime layer underneath agent frameworks

## What it is

NVIDIA's OpenShell provides an isolated execution environment for autonomous agents, with NemoClaw as a hardened wrapper for running third-party agent frameworks (Hermes, LangChain Deep Agents, OpenClaw) on top with managed inference; OpenHarness is a similar general-purpose harness bundled with a reference personal-assistant agent.

## Why it matters

Useful when you want to run someone else's agent framework without granting it unrestricted access to the host machine.

## Provenance

- Confidence **medium** · durability **durable** · supported by **6** archived item(s).

## Sources

- https://github.com/NVIDIA/OpenShell
- https://github.com/NVIDIA/NemoClaw
- https://github.com/HKUDS/OpenHarness

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
