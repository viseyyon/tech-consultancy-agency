---
title: "RDK-B autonomous patch pipelines carry hard, non-negotiable safety invariants around bitbake and quilt"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "For AI-driven patch application on RDK-B (Vodafone FGV530T UK, AN7581/eagle/mt-wifi7): never run the full `bitbake rdk-generic-broadband-image`; always `quilt refresh -p1` and never modify the working"
tags: [knowledge, decisions-rationale, conf/high, durable, rdk-b, bitbake, quilt, safety-invariants]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# RDK-B autonomous patch pipelines carry hard, non-negotiable safety invariants around bitbake and quilt

## What it is

For AI-driven patch application on RDK-B (Vodafone FGV530T UK, AN7581/eagle/mt-wifi7): never run the full `bitbake rdk-generic-broadband-image`; always `quilt refresh -p1` and never modify the working quilt patch directly; any component-rename sed operation (e.g. mt7990->eagle) requires explicit human confirmation. Baked into the CLAUDE.md constitution as unconditional constraints.

## Why it matters

Violating any of these invariants risks breaking the RDK-B build or silently corrupting patches — they are non-negotiable, not suggestions.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
