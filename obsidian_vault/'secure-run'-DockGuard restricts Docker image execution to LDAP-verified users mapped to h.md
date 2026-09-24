---
title: "'secure-run'/DockGuard restricts Docker image execution to LDAP-verified users mapped to host UID/GID"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "A Docker security wrapper (named secure-run, then renamed DockGuard) that only starts a container when the invoking Linux user's UID/GID matches an LDAP-verified identity bound to that image -- enforc"
tags: [knowledge, security-guardrails, conf/medium, durable, dockguard, docker-security, ldap, non-root]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# 'secure-run'/DockGuard restricts Docker image execution to LDAP-verified users mapped to host UID/GID

## What it is

A Docker security wrapper (named secure-run, then renamed DockGuard) that only starts a container when the invoking Linux user's UID/GID matches an LDAP-verified identity bound to that image -- enforcing non-root execution, capability dropping, an image allowlist, and session-bound audit logging -- to prevent unauthorized use of internally built Docker images.

## Why it matters

An existing security tool for enforcing LDAP-verified, non-root Docker image execution, reusable wherever internal image access needs to be locked down.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
