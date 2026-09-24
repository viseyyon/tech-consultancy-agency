---
title: "Claude Code supports local SLMs via Ollama's Anthropic-compatible API (v0.14.0+)"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Claim"
confidence: medium
durability: durable
evidence: 1
summary: "Claude Code can be pointed at locally-hosted small language models through Ollama's Anthropic-compatible endpoint (v0.14.0+), configured via environment variables or ~/.claude/settings.json. Minimum v"
tags: [knowledge, model-serving-local-inference, conf/medium, durable, claude-code, ollama, local-inference, slm]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Claude Code supports local SLMs via Ollama's Anthropic-compatible API (v0.14.0+)

## What it is

Claude Code can be pointed at locally-hosted small language models through Ollama's Anthropic-compatible endpoint (v0.14.0+), configured via environment variables or ~/.claude/settings.json. Minimum viable models need 32K+ context (64K+ preferred for agentic workflows) and tool-calling support, with Q4_K_M quantization as the default and Q5_K_M for better fidelity; recommended models include Qwen3-Coder, NVIDIA Nemotron-3-Nano, and DeepSeek-Coder-V2, with LM Studio and MLX as alternative stacks.

## Why it matters

Confirms a concrete local-inference path for RDK-B/embedded work when cloud API cost or availability is a constraint, with specific model and quantization recommendations already vetted.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
