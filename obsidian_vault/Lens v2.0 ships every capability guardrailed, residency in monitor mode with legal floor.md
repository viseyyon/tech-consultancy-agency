---
title: "Lens v2.0 ships every capability guardrailed, residency in monitor mode with legal floor"
type: knowledge-entry
domain: "Business & GTM"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "Lens v2.0 'Edge Mode' (supersedes v1.1) turns on all planned capabilities at launch (multi-agent northstar, visual retrieval, impact simulator, hybrid CAG router, DSPy sandbox, agent-memory pilot) beh"
tags: [knowledge, business-gtm, conf/high, durable, lens, feature-flags, data-residency, embeddings]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Business & GTM]]"]
---

# Lens v2.0 ships every capability guardrailed, residency in monitor mode with legal floor

## What it is

Lens v2.0 "Edge Mode" (supersedes v1.1) turns on all planned capabilities at launch (multi-agent northstar, visual retrieval, impact simulator, hybrid CAG router, DSPy sandbox, agent-memory pilot) behind feature flags and runtime guardrails rather than a staged rollout; release phases become hardening waves (experimental to beta to GA on gold-set evidence) instead of feature gates. Data residency defaults to non-blocking monitor mode (log+alert+weekly report) for the general corpus, but keeps a hard floor on export-controlled and carrier-NDA data classes that only Legal+CISO can relax via the EU AI Act file - deliberately not an engineering toggle. The irreversible infrastructure pick is an open-weight embedder (BGE-M3 vs Qwen3-Embedding), explicitly never text-embedding-3, running through LiteLLM over Azure Foundry EU Data Zone.

## Why it matters

Anyone touching Lens's rollout, residency policy, or embedding choice needs to know flags are the release mechanism now, and that the export-controlled data floor cannot be relaxed by changing code.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude session 21 Aug 2026 - v2.0 revision pass

---

Part of [[MOC - Business & GTM]] · [[Home]]
