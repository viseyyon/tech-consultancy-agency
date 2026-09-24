---
title: "Token/context cost-control techniques for long agent sessions"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Technique"
confidence: high
durability: durable
evidence: 4
summary: "Recurring advice: cache repeated context, lazy-load tools or docs only when needed, route cheap subtasks to smaller models, and periodically compact or summarize conversation history instead of lettin"
tags: [knowledge, claude-code-practice, conf/high, durable, token-cost, context-management, compaction, caching]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# Token/context cost-control techniques for long agent sessions

## What it is

Recurring advice: cache repeated context, lazy-load tools or docs only when needed, route cheap subtasks to smaller models, and periodically compact or summarize conversation history instead of letting it accumulate.

## Why it matters

Directly cuts spend and avoids rate-limit cooldowns in long-running Claude Code or agent sessions.

## Provenance

- Confidence **high** · durability **durable** · supported by **4** archived item(s).

## Sources

- https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens
- https://arunninghacker.substack.com/p/stop-wasting-claude-code-tokens
- https://youtu.be/jJMbz-xziZI
- https://cnx-software.com/2026/05/14/clawdmeter-a-diy-esp32-s3-desk-dashboard-for-claude-code-token-usage-monitoring

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
