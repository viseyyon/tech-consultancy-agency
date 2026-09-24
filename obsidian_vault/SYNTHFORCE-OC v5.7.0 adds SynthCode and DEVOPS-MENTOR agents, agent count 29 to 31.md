---
title: "SYNTHFORCE-OC v5.7.0 adds SynthCode and DEVOPS-MENTOR agents, agent count 29 to 31"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "SynthCode is a production code-review engine wired into Gerrit patchsets and Jenkins pipeline gates, with 10 impact areas, 7 review presets, and severity-driven Code-Review/Verified label voting, run"
tags: [knowledge, decisions-rationale, conf/high, durable, synthcode, devops-mentor, gerrit, jenkins]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# SYNTHFORCE-OC v5.7.0 adds SynthCode and DEVOPS-MENTOR agents, agent count 29 to 31

## What it is

SynthCode is a production code-review engine wired into Gerrit patchsets and Jenkins pipeline gates, with 10 impact areas, 7 review presets, and severity-driven Code-Review/Verified label voting, run as a standalone FastAPI sidecar on port 9450 rather than as a 16th MCP server on the hub — deliberately, for Gerrit webhook timeout discipline, independent scaling, and letting the Jenkins Shared Library call plain HTTP. DEVOPS-MENTOR is a pedagogical agent teaching CI/CD, IaC, and observability via a six-step Socratic interaction pattern, explicitly paired with JENKINS, VEGA, and SynthCode.

## Why it matters

The deliberate choice to keep SynthCode as a standalone sidecar rather than folding it into the MCP hub is a reusable architectural precedent for any future latency-sensitive or independently-scaled agent.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
