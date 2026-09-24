---
title: "HERMES distills Claude into fine-tuned GPT-4.1-mini, cutting cost from $750/yr to $425/yr at 92-95% quality"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "HERMES v2.0 (RDK/OpenWrt RCA report generator) implements a teacher-student pattern: Claude Sonnet generates high-quality training data used to fine-tune GPT-4.1-mini on Azure as the primary low-cost"
tags: [knowledge, model-serving-local-inference, conf/medium, durable, hermes, fine-tuning, gpt-4-1-mini, distillation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# HERMES distills Claude into fine-tuned GPT-4.1-mini, cutting cost from $750/yr to $425/yr at 92-95% quality

## What it is

HERMES v2.0 (RDK/OpenWrt RCA report generator) implements a teacher-student pattern: Claude Sonnet generates high-quality training data used to fine-tune GPT-4.1-mini on Azure as the primary low-cost model, escalating complex tickets back to Claude via a multi-tier router. This dropped projected annual cost from ~$750 (Claude-only) to ~$425 (hybrid) while retaining 92-95% of Claude's quality, versus 70-80% for an earlier Phi-4-mini approach; direct Claude fine-tuning via Amazon Bedrock was ruled out as too expensive (~$15K+/month).

## Why it matters

A validated cost-reduction pattern (teacher-student distillation to a cheap fine-tuned model) that cut projected annual cost by roughly 43% while keeping quality above 90%, reusable for other high-volume, low-complexity Claude workloads.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
