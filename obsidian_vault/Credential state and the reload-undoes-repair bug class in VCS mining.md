---
title: "Credential state and the reload-undoes-repair bug class in VCS mining"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "At the point recorded, no working API credential existed anywhere for the Vantiva VCS/Jira estate; all access achieved so far was riding the operator's personal SSH key, and a live GitHub PAT was foun"
tags: [knowledge, security-guardrails, conf/medium, durable, credentials, secret-leak, reload-bug, load-authority]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Credential state and the reload-undoes-repair bug class in VCS mining

## What it is

At the point recorded, no working API credential existed anywhere for the Vantiva VCS/Jira estate; all access achieved so far was riding the operator's personal SSH key, and a live GitHub PAT was found leaked in cleartext in a build agent's .git/config (immediately flagged for revocation). Separately, a credential-keying fix was silently undone twice by a later data reload that overwrote already-keyed fingerprints with unkeyed defaults; the durable fix is for the load path to declare an explicit authority (artifact, derived, union, carried, ledger, or run) per field it writes, so a reload cannot blindly clobber a field it does not own.

## Why it matters

Assuming an SSH-key-reachable system has a working service credential, or that a completed data-repair survives the next reload, has each produced a real incident here.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
