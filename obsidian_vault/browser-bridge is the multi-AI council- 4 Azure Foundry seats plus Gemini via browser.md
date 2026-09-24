---
title: "browser-bridge is the multi-AI council: 4 Azure Foundry seats plus Gemini via browser"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Resource"
confidence: medium
durability: durable
evidence: 3
summary: "The browser-bridge MCP server (~/Documents/AI_cluster/mcp-browser-bridge/index.js) exposes ask_gemini/ask_chatgpt/ask_kimi/ask_deepseek/ask_grok plus council_status. ChatGPT, Kimi, DeepSeek and Grok r"
tags: [knowledge, developer-infrastructure, conf/medium, durable, browser-bridge, ai-council, azure-foundry, grok]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# browser-bridge is the multi-AI council: 4 Azure Foundry seats plus Gemini via browser

## What it is

The browser-bridge MCP server (~/Documents/AI_cluster/mcp-browser-bridge/index.js) exposes ask_gemini/ask_chatgpt/ask_kimi/ask_deepseek/ask_grok plus council_status. ChatGPT, Kimi, DeepSeek and Grok route through an Azure Foundry resource (deployments gpt-5.6-sol, Kimi-K2.6, DeepSeek-V4-Pro, grok-4.3); Gemini alone routes through an actual Chrome browser session. Grok's Azure seat has intermittently returned HTTP 500, dropping council votes to 4/5 or 3/4.

## Why it matters

Not knowing Grok's seat is flaky means a partial council result can be mistaken for a full quorum, or a real outage mistaken for a code bug.

## Provenance

- Confidence **medium** · durability **durable** · supported by **3** archived item(s).

## Sources

- MCP server browser integration
- Cowork - Gerrit/Gitolite/GitHub setup

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
