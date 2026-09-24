---
title: "claude -p headless mode can't approve Write permissions; pre-accept trust + settings.local.json for CI"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 3
summary: "Running `claude --dangerously-skip-permissions -p` for CI/Jenkins still triggers an interactive directory-trust prompt on first run, and headless `claude -p` has no way to approve a Write-permission p"
tags: [knowledge, claude-code-practice, conf/high, durable, claude-code, ci-cd, headless, permissions]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# claude -p headless mode can't approve Write permissions; pre-accept trust + settings.local.json for CI

## What it is

Running `claude --dangerously-skip-permissions -p` for CI/Jenkins still triggers an interactive directory-trust prompt on first run, and headless `claude -p` has no way to approve a Write-permission prompt at all. Fix is to pre-accept trust via `claude /init` or write `.claude/settings.local.json` with explicit `allowedPaths`/`autoApprove` patterns (e.g. `Bash(*)`, `Write(*)`) before the first headless run.

## Why it matters

Without this fix, CI/Jenkins pipelines that need Claude to save files break silently on first headless run.

## Provenance

- Confidence **high** · durability **durable** · supported by **3** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
