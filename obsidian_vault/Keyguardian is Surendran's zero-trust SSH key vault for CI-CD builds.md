---
title: "Keyguardian is Surendran's zero-trust SSH key vault for CI/CD builds"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 2
summary: "Keyguardian is a Python/FastAPI + React zero-trust SSH key vault letting Docker/Jenkins builds pull SSH keys without exposing them outside the org. It uses AES-256 encryption at rest, Azure Blob/Key V"
tags: [knowledge, project-state, conf/high, durable, keyguardian, ssh, zero-trust, jenkins]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Keyguardian is Surendran's zero-trust SSH key vault for CI/CD builds

## What it is

Keyguardian is a Python/FastAPI + React zero-trust SSH key vault letting Docker/Jenkins builds pull SSH keys without exposing them outside the org. It uses AES-256 encryption at rest, Azure Blob/Key Vault backup, JWT auth with role-based access (admins add users/keys, regular users only view), and Jenkins pipeline + freestyle-job integration for scoped key download plus post-build cleanup. Later hardened with LDAP verification requiring matching UID/GID.

## Why it matters

Provides a reusable, audited alternative to storing raw SSH keys in CI/CD systems.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
