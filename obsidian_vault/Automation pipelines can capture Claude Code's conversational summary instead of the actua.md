---
title: "Automation pipelines can capture Claude Code's conversational summary instead of the actual deliverable"
type: knowledge-entry
domain: "Automation & Workflow"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "An RCA generation pipeline (rca_orchestrator.py) produced severely truncated reports (3,546 words vs. 10,000+ expected) because the driving prompt didn't force direct stdout output — Claude Code respo"
tags: [knowledge, automation-workflow, conf/high, durable, automation, stdout-capture, claude-code, pipeline-bug]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Automation & Workflow]]"]
---

# Automation pipelines can capture Claude Code's conversational summary instead of the actual deliverable

## What it is

An RCA generation pipeline (rca_orchestrator.py) produced severely truncated reports (3,546 words vs. 10,000+ expected) because the driving prompt didn't force direct stdout output — Claude Code responded conversationally ('I completed the report, wrote it to file X') and that conversational text is what the orchestrator's stdout-capture logic saved as the report.

## Why it matters

Any prompt driving Claude Code programmatically must explicitly mandate printing the full deliverable to stdout, and the caller should validate the captured output starts with an expected content marker (e.g. '# ROOT CAUSE ANALYSIS REPORT') before trusting it.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Automation & Workflow]] · [[Home]]
