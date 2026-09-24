---
title: "Mining Console host facts: Ollama dependency, stale uvicorn, CORS"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "The Mining Console runs on 10.17.58.119:8002 against Postgres (db mining_console, user mining). Its WHY-synthesis and embeddings depend on a host-level systemd Ollama listening on port 11434, not the"
tags: [knowledge, developer-infrastructure, conf/high, durable, ollama, stale-process, cors, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Mining Console host facts: Ollama dependency, stale uvicorn, CORS

## What it is

The Mining Console runs on 10.17.58.119:8002 against Postgres (db mining_console, user mining). Its WHY-synthesis and embeddings depend on a host-level systemd Ollama listening on port 11434, not the mining_ollama Docker container (created but never started, a dead-weight port conflict that still let synthesis return text, masking the real dependency). Separately, a stale uvicorn process served old committed code from an earlier restart, causing three separate rounds of confused debugging until a healthz endpoint exposing the running code's git commit hash was added; CORS was also tightened from a wildcard to an explicit allowlist.

## Why it matters

Debugging "wrong behavior" on this app without checking the code-version endpoint or which Ollama is actually serving requests wastes time chasing a phantom bug.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Cowork - Vantiva Jira and Confluence mining

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
