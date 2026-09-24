---
title: "2025-2026 pieces converge on needing prompt/output-level observability and adversarial evals, not just standard logs"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 4
summary: "A Jan 2026 thenewstack piece argues logs, metrics, and traces miss LLM-specific failure modes; Anthropic's Bloom (Dec 2025) open-sources automated behavioral evals for frontier models; Anthropic's 'AI"
tags: [knowledge, evaluation-observability, conf/medium, durable, observability, evals, red-teaming, jailbreak]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# 2025-2026 pieces converge on needing prompt/output-level observability and adversarial evals, not just standard logs

## What it is

A Jan 2026 thenewstack piece argues logs, metrics, and traces miss LLM-specific failure modes; Anthropic's Bloom (Dec 2025) open-sources automated behavioral evals for frontier models; Anthropic's 'AI-resistant technical evaluations' post (Jan 2026) describes redesigning a take-home exam three times because Claude kept passing it; and DeepTeam (Aug 2026) is an open-source red-teaming framework testing agents and RAG pipelines for jailbreaks, prompt injection, and PII leakage.

## Why it matters

Plan for a dedicated prompt/completion-level trace layer plus adversarial or behavioral testing — conventional software observability and static evals are being treated as insufficient for LLM systems.

## Provenance

- Confidence **medium** · durability **durable** · supported by **4** archived item(s).

## Sources

- https://thenewstack.io/llms-create-a-new-blind-spot-in-observability
- https://marktechpost.com/2025/12/21/anthropic-ai-releases-bloom-an-open-source-agentic-framework-for-automated-behavioral-evaluations-of-frontier-ai-models
- https://anthropic.com/engineering/AI-resistant-technical-evaluations
- https://x.com/DanKornas/status/2085461154504036354

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
