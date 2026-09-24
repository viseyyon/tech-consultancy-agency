---
title: "Azure Identity Credential-Chain Fallback Pattern"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 1
summary: "The Azure Identity library's DefaultAzureCredential/ChainedTokenCredential pattern tries a sequence of credential sources (environment variables, managed identity, CLI login, etc.) in order until one"
tags: [knowledge, developer-infrastructure, conf/high, durable, azure, authentication, credential-chain]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Azure Identity Credential-Chain Fallback Pattern

## What it is

The Azure Identity library's DefaultAzureCredential/ChainedTokenCredential pattern tries a sequence of credential sources (environment variables, managed identity, CLI login, etc.) in order until one succeeds, so the same code authenticates correctly across local dev, CI, and production without branching logic.

## Why it matters

Worth knowing before hand-rolling per-environment auth branches for anything talking to Azure services.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- https://learn.microsoft.com/en-us/azure/developer/javascript/sdk/authentication/credential-chains

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
