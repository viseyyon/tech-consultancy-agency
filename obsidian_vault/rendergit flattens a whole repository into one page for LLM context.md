---
title: "rendergit flattens a whole repository into one page for LLM context"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 2
summary: "Renders any git repository into a single static HTML page, explicitly intended for humans or LLMs. reader3 does the analogous thing for books, framing reading as something done alongside a model."
tags: [knowledge, mcp-tool-integration, conf/high, durable, context-packing, repo-to-text, tooling]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# rendergit flattens a whole repository into one page for LLM context

## What it is

Renders any git repository into a single static HTML page, explicitly intended for humans or LLMs. reader3 does the analogous thing for books, framing reading as something done alongside a model.

## Why it matters

Directly useful for context packing: one fetch gives an agent a whole repo instead of dozens of file reads, which is exactly the bottleneck in agentic code review.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- https://github.com/karpathy/rendergit
- https://github.com/karpathy/reader3

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
