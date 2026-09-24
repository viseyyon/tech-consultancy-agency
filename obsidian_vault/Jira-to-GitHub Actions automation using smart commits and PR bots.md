---
title: "Jira-to-GitHub Actions automation using smart commits and PR bots"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Pattern"
confidence: high
durability: durable
evidence: 1
summary: "His automation setup ties Jira to GitHub Actions via repository_dispatch events, using Jira smart-commit syntax (e.g. PROJ-123 #comment ... #time 1h #in-progress) and a PROJ-123-feature branch naming"
tags: [knowledge, developer-infrastructure, conf/high, durable, github-actions, jira, ci-cd, automation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Jira-to-GitHub Actions automation using smart commits and PR bots

## What it is

His automation setup ties Jira to GitHub Actions via repository_dispatch events, using Jira smart-commit syntax (e.g. PROJ-123 #comment ... #time 1h #in-progress) and a PROJ-123-feature branch naming convention. Pull requests are opened automatically via the peter-evans/create-pull-request action, and a separate copilot-setup-steps.yml workflow (which must be named exactly copilot-setup-steps and only runs on Ubuntu x64 or Windows x64) configures the GitHub Copilot coding agent.

## Why it matters

Documents his working CI/CD and issue-tracking conventions, which matter if a future session touches his repos or GitHub Actions workflows.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- AI Automation Projects — Ollama & Phi-4 Fine-Tuning Detail

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
