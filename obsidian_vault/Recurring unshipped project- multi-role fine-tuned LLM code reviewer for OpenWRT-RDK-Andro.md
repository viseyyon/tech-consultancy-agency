---
title: "Recurring unshipped project: multi-role fine-tuned LLM code reviewer for OpenWRT/RDK/Android TV video"
type: knowledge-entry
domain: "Project State"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 3
summary: "Across at least three conversations (Aug 4, Aug 7, Oct 13 2025), the same unfinished project recurs: an AI code-review system for embedded platforms (OpenWRT, RDK Broadband, Android TV, Linux video) p"
tags: [knowledge, project-state, conf/high, durable, lora, code-review, gerrit, mcp]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Recurring unshipped project: multi-role fine-tuned LLM code reviewer for OpenWRT/RDK/Android TV video

## What it is

Across at least three conversations (Aug 4, Aug 7, Oct 13 2025), the same unfinished project recurs: an AI code-review system for embedded platforms (OpenWRT, RDK Broadband, Android TV, Linux video) playing five expert roles (architect, security engineer, senior developer, staff engineer, static analyzer) via role-specific LoRA adapters on one fine-tuned model with an RLHF-style expertise-weighted feedback loop. The most recent iteration reframes it around a Gerrit MCP server with platform-specific analyzer modules (rdk_analyzer.py, androidtv_analyzer.py, openwrt_analyzer.py).

## Why it matters

As of the latest digest it remains a design/prompt-engineering exercise, not a running production system, so future requests in this shape should be recognized as continuing an unshipped idea rather than treated as new.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
