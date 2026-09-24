---
title: "Artifact authority and sensitive-finding handling standing rules"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "An artifact (a run's recorded output) is never treated as authoritative over a decision the system has since made; it records what a run observed, nothing more. A test fixture must be shown able to fa"
tags: [knowledge, security-guardrails, conf/medium, durable, artifact-authority, fixtures, credential-handling]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Artifact authority and sensitive-finding handling standing rules

## What it is

An artifact (a run's recorded output) is never treated as authoritative over a decision the system has since made; it records what a run observed, nothing more. A test fixture must be shown able to fail the plausible-wrong implementation, or it is decoration, not a test. A sensitive finding (e.g. a full list of credentials discovered in a scan) is filed outside the repository with restricted permissions and only referenced, never reproduced, in tracking docs or chat.

## Why it matters

Trusting a stale artifact over current system state, trusting a fixture that cannot fail, or letting a sensitive list travel through chat/repo history are each concrete ways this user's projects have leaked or misfired before.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
