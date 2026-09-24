---
title: "CodeLlama code-review vs Copilot resolves to a hybrid: Copilot for completion, in-house model for critical review"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 5
summary: "A recurring internal initiative (explored across at least five separate planning sessions) is a fine-tuned CodeLlama-based automated code-review system positioned against GitHub Copilot. The consisten"
tags: [knowledge, decisions-rationale, conf/high, durable, codellama, github-copilot, hybrid-strategy, code-review]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# CodeLlama code-review vs Copilot resolves to a hybrid: Copilot for completion, in-house model for critical review

## What it is

A recurring internal initiative (explored across at least five separate planning sessions) is a fine-tuned CodeLlama-based automated code-review system positioned against GitHub Copilot. The consistent conclusion is a hybrid strategy: Copilot remains for everyday code completion, while a fine-tuned, internally-hosted model handles security/architecture-critical review.

## Why it matters

The deciding factors are that fine-tuning keeps proprietary code fully on-prem with no per-request cost after training, versus Copilot's per-seat licensing and inability to do deep security/architecture analysis — this is the settled default answer whenever this comparison comes up again.

## Provenance

- Confidence **high** · durability **durable** · supported by **5** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
