---
title: "Anthropic's own posts push context curation and code-execution-via-MCP as the main agent efficiency levers"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Claim"
confidence: medium
durability: durable
evidence: 2
summary: "Anthropic's Nov 2025 'Effective context engineering for AI agents' and 'Code execution with MCP' posts argue that curating what enters context, and letting agents write code that calls MCP tools rathe"
tags: [knowledge, mcp-tool-integration, conf/medium, durable, mcp, context-engineering, token-efficiency, anthropic]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# Anthropic's own posts push context curation and code-execution-via-MCP as the main agent efficiency levers

## What it is

Anthropic's Nov 2025 'Effective context engineering for AI agents' and 'Code execution with MCP' posts argue that curating what enters context, and letting agents write code that calls MCP tools rather than issuing direct tool-call JSON, are the primary ways to cut token overhead; the MCP post reports up to 98.7% context reduction internally.

## Why it matters

For tool-heavy MCP agents, consider a code-execution pattern instead of turn-by-turn tool calls, but treat the 98.7% figure as Anthropic's own best-case internal result, not a generic benchmark.

## Provenance

- Confidence **medium** · durability **durable** · supported by **2** archived item(s).

## Sources

- https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://anthropic.com/engineering/code-execution-with-mcp

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
