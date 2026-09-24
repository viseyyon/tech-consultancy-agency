---
title: "PROMETHEUS CODEX requires exact file/line evidence tracing every JIRA story into RDK-B source"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "Built for the FGV530T_UK Vodafone-UK broadband gateway project, PROMETHEUS CODEX is a ~3,500-line multi-agent orchestration spec that ingests source code, environment variables, build steps, and JIRA"
tags: [knowledge, project-state, conf/medium, durable, prometheus-codex, traceability, rdk-b, jira]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# PROMETHEUS CODEX requires exact file/line evidence tracing every JIRA story into RDK-B source

## What it is

Built for the FGV530T_UK Vodafone-UK broadband gateway project, PROMETHEUS CODEX is a ~3,500-line multi-agent orchestration spec that ingests source code, environment variables, build steps, and JIRA user-story/bug folders, then produces a requirement-by-requirement traceability report backed by exact file, folder, and line-number evidence cross-checked against the source tree. It evolved to require pasting the actual code lines (not just line numbers) after pushback that references alone weren't audit-sufficient.

## Why it matters

Sets the bar for traceability tooling going forward: exact code-line evidence, not just references, is required for an audit to be considered adequate.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
