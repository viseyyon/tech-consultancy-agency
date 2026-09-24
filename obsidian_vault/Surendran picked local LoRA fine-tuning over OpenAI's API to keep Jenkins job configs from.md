---
title: "Surendran picked local LoRA fine-tuning over OpenAI's API to keep Jenkins job configs from leaving the machine"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "For a project fine-tuning an LLM on Jenkins job configs to auto-generate new jobs from CSV template tables, switched from OpenAI-API fine-tuning to local Hugging Face + PEFT/LoRA training so Jenkins d"
tags: [knowledge, decisions-rationale, conf/high, durable, lora, fine-tuning, local-training, jenkins]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# Surendran picked local LoRA fine-tuning over OpenAI's API to keep Jenkins job configs from leaving the machine

## What it is

For a project fine-tuning an LLM on Jenkins job configs to auto-generate new jobs from CSV template tables, switched from OpenAI-API fine-tuning to local Hugging Face + PEFT/LoRA training so Jenkins data (potentially containing credentials/config) never leaves his machine, and to avoid ongoing API cost — accepting slower training (2-4h CPU, 30-60min GPU) as the tradeoff.

## Why it matters

Data-confidentiality and cost were prioritized over training speed for this project.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
