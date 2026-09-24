---
title: "Private-Network Access for GitHub-Hosted Runners"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "GitHub Actions' docs describe supported ways to let GitHub-hosted (not self-hosted) runners reach resources on a private network - private package registries, secret managers, on-prem services - witho"
tags: [knowledge, developer-infrastructure, conf/high, durable, github-actions, ci, networking, runners]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Private-Network Access for GitHub-Hosted Runners

## What it is

GitHub Actions' docs describe supported ways to let GitHub-hosted (not self-hosted) runners reach resources on a private network - private package registries, secret managers, on-prem services - without giving up hosted-runner convenience.

## Why it matters

Relevant when CI needs private-network access but self-hosting runners isn't wanted for other reasons.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- https://docs.github.com/en/actions/how-tos/manage-runners/github-hosted-runners/connect-to-a-private-network

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
