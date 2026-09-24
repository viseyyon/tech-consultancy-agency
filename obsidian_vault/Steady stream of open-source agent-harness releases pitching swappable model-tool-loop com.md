---
title: "Steady stream of open-source agent-harness releases pitching swappable model/tool/loop components"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 5
summary: "From Nov 2025 to Aug 2026 several projects — Google's ADK Go, DeepAgent, Prime Intellect's 'Prime Agent' RLM harness, DeepSeek's MIT-licensed plugin harness, and 'Confucius AI Agent' — each announce a"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, agent-harness, open-source, orchestration, plugins]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# Steady stream of open-source agent-harness releases pitching swappable model/tool/loop components

## What it is

From Nov 2025 to Aug 2026 several projects — Google's ADK Go, DeepAgent, Prime Intellect's 'Prime Agent' RLM harness, DeepSeek's MIT-licensed plugin harness, and 'Confucius AI Agent' — each announce a reusable agent loop where the model adapter, tool registry, and sub-agents are pluggable pieces rather than one fixed app.

## Why it matters

The agent-harness layer is converging on a plugin-style architecture; when evaluating a new framework, check whether model, tools, and loop are cleanly separable, and treat any headline benchmark number (e.g. a specific ARC-AGI-3 score) as a vendor claim, not independent verification.

## Provenance

- Confidence **medium** · durability **durable** · supported by **5** archived item(s).

## Sources

- https://thenewstack.io/deepseek-harness-open-source-plugins
- https://marktechpost.com/2026/08/06/prime-intellect-releases-prime-agent
- https://marktechpost.com/2025/11/01/deepagent-a-deep-reasoning-ai-agent-that-performs-autonomous-thinking-tool-discovery-and-action-execution-within-a-single-reasoning-process
- https://marktechpost.com/2025/11/07/google-extends-its-agent-development-kit-adk-to-go-bringing-native-agentic-workflows-to-backend-teams

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
