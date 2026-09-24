---
title: "Vantiva's RDK Broadband repos migrated from GitLab to an internal Gerrit at padcsictonic01.va.vantiva.org"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 1
summary: "Vantiva's TCH-RDKM (RDK broadband) project repos moved off GitLab onto an internal Gerrit instance at padcsictonic01.va.vantiva.org:29418 (repo tch-rdkm-core/tch-rdkm-manifests.git, e.g. manifest rele"
tags: [knowledge, environment-tooling-state, conf/high, durable, gerrit, gitlab-migration, rdk-b, vantiva]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Vantiva's RDK Broadband repos migrated from GitLab to an internal Gerrit at padcsictonic01.va.vantiva.org

## What it is

Vantiva's TCH-RDKM (RDK broadband) project repos moved off GitLab onto an internal Gerrit instance at padcsictonic01.va.vantiva.org:29418 (repo tch-rdkm-core/tch-rdkm-manifests.git, e.g. manifest release-OBFC_24.2_CVA438.xml on branch vbv-rdk-next). Surendran built a Python/Flask validator that fetches the manifest over SSH and flags remaining GitLab/GitHub URLs or malformed Gerrit remotes.

## Why it matters

Confirms the current source of truth for RDK broadband repos, and gives a tool to verify a project is fully migrated.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
