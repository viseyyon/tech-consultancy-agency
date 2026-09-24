---
title: "Built an MCP server that strips @vantiva.com/@technicolor.com emails from code before pushing to GitHub"
type: knowledge-entry
domain: "Automation & Workflow"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "A custom MCP server (code_sanitizer_mcp.py) scans a codebase for corporate email addresses (@vantiva.com, @technicolor.com) in code and git author/committer history, replaces them with Viseyyon-brande"
tags: [knowledge, automation-workflow, conf/medium, durable, mcp-server, git-sanitization, open-source, viseyyon]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Automation & Workflow]]"]
---

# Built an MCP server that strips @vantiva.com/@technicolor.com emails from code before pushing to GitHub

## What it is

A custom MCP server (code_sanitizer_mcp.py) scans a codebase for corporate email addresses (@vantiva.com, @technicolor.com) in code and git author/committer history, replaces them with Viseyyon-branded addresses, and automates the git add/commit/push to GitHub, with dry-run preview and backup-file safety before any destructive git-history rewrite. Built so side/personal projects touched at work can be open-sourced under the Viseyyon identity without leaking employer email references.

## Why it matters

This is the tool to reach for whenever a work-adjacent side project needs to be sanitized and open-sourced under his own identity without corporate email leakage.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Automation & Workflow]] · [[Home]]
