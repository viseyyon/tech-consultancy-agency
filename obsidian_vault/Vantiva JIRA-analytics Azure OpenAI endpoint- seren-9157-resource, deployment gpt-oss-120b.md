---
title: "Vantiva JIRA-analytics Azure OpenAI endpoint: seren-9157-resource, deployment gpt-oss-120b, with keyword fallback"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Resource"
confidence: high
durability: durable
evidence: 1
summary: "The weekly-performance and critical-ticket-detection Python tooling built for Vantiva uses Azure OpenAI at endpoint https://seren-9157-resource.services.ai.azure.com/openai/v1/ with deployment name 'g"
tags: [knowledge, environment-tooling-state, conf/high, durable, azure-openai, endpoint, jira-analytics, fallback]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Vantiva JIRA-analytics Azure OpenAI endpoint: seren-9157-resource, deployment gpt-oss-120b, with keyword fallback

## What it is

The weekly-performance and critical-ticket-detection Python tooling built for Vantiva uses Azure OpenAI at endpoint https://seren-9157-resource.services.ai.azure.com/openai/v1/ with deployment name 'gpt-oss-120b'. When the API key is unavailable, the system falls back to keyword-based analysis while staying fully functional.

## Why it matters

Reference endpoint/deployment config for this tooling, plus a reusable resilience pattern (keyword fallback) reused across his Jira-analysis tools.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
