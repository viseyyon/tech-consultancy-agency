---
title: "Built a self-healing 'AI DevOps Engineer' that creates Jenkins Gerrit jobs from JIRA tickets without the DSL plugin"
type: knowledge-entry
domain: "Automation & Workflow"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "Built from an existing Vantiva Jenkins Gerrit-review build job (CGA6444VF v23.2), an autonomous system that avoids the Jenkins DSL plugin and instead: parses JIRA tickets with NLP to extract build req"
tags: [knowledge, automation-workflow, conf/medium, durable, jenkins, gerrit, jira, ci-automation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Automation & Workflow]]"]
---

# Built a self-healing 'AI DevOps Engineer' that creates Jenkins Gerrit jobs from JIRA tickets without the DSL plugin

## What it is

Built from an existing Vantiva Jenkins Gerrit-review build job (CGA6444VF v23.2), an autonomous system that avoids the Jenkins DSL plugin and instead: parses JIRA tickets with NLP to extract build requirements, creates Jenkins jobs via REST API, self-diagnoses and auto-fixes common build failures (disk space, timeouts, permissions, Docker issues), and uses a learned model over historical build data to predict success and recommend optimizations. Deployed as a 24/7 systemd service with a JIRA webhook handler and monitoring dashboard.

## Why it matters

A working example of end-to-end JIRA-to-Jenkins automation without the DSL plugin, useful as a reference implementation for future CI automation work.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Automation & Workflow]] · [[Home]]
