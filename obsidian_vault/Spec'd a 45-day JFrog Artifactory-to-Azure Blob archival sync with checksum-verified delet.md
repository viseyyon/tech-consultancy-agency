---
title: "Spec'd a 45-day JFrog Artifactory-to-Azure Blob archival sync with checksum-verified delete for release/build repos"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 2
summary: "Sync system mirroring a scoped set of JFrog Artifactory content -- full repos BUILD_SCRIPTS and BUILD_SCRIPTS_AUTOMATION, plus specific folders (RELEASES, RELEASE_XMLS, EVOLVERE_RELEASE, RELEASE_MANIF"
tags: [knowledge, environment-tooling-state, conf/medium, durable, jfrog-artifactory, azure-blob, archival, checksum-verification]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Spec'd a 45-day JFrog Artifactory-to-Azure Blob archival sync with checksum-verified delete for release/build repos

## What it is

Sync system mirroring a scoped set of JFrog Artifactory content -- full repos BUILD_SCRIPTS and BUILD_SCRIPTS_AUTOMATION, plus specific folders (RELEASES, RELEASE_XMLS, EVOLVERE_RELEASE, RELEASE_MANIFEST) -- to Azure Blob Storage on a 45-day cycle. Files are only deleted from Artifactory after their SHA1/MD5 checksum matches the Azure copy; a mismatch triggers re-upload and re-verification. Runs with a login-protected dashboard, SQLite-backed history, and audit logging.

## Why it matters

A safe, checksum-verified archival pattern that prevents data loss during Artifactory cleanup, reusable for any future storage-tiering or archival design.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
