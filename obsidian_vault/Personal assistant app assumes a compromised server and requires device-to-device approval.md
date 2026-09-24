---
title: "Personal assistant app assumes a compromised server and requires device-to-device approval"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "The personal-assistant phone app was designed so that a fully compromised backend server still cannot read or forge commands: the phone holds a non-extractable private key (survives XSS), there are no"
tags: [knowledge, security-guardrails, conf/high, durable, security, e2e-encryption, device-enrollment, threat-model]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Personal assistant app assumes a compromised server and requires device-to-device approval

## What it is

The personal-assistant phone app was designed so that a fully compromised backend server still cannot read or forge commands: the phone holds a non-extractable private key (survives XSS), there are no inbound ports, commands are E2E encrypted and signed inside the ciphertext with the command ID bound into the GCM authenticated-associated-data, replay is deduped persistently, and results are Ed25519-signed against a pinned agent key - a 5/5 crypto test suite passes this threat model. Because the council converged on enrollment trust as one of the three weakest points in this design, new devices cannot self-enroll; they must be approved from an already-trusted device via an explicit approved flag and approval flow.

## Why it matters

Documents the actual threat model this app defends against, which matters for any future feature that touches the command channel or device enrollment.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Personal assistant app development

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
