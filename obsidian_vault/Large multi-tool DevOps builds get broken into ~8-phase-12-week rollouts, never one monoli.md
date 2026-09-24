---
title: "Large multi-tool DevOps builds get broken into ~8-phase/12-week rollouts, never one monolithic prompt"
type: knowledge-entry
domain: "Automation & Workflow"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "Reviewing a 50+ requirement, 20+ file 'generate everything at once' Claude CLI prompt for an AIOps Jenkins OTA framework (Jenkins + Azure AI + Gitolite + Gerrit + Key Guardian + Artifactory) identifie"
tags: [knowledge, automation-workflow, conf/medium, durable, phased-delivery, claude-code, context-limits, jenkins]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Automation & Workflow]]"]
---

# Large multi-tool DevOps builds get broken into ~8-phase/12-week rollouts, never one monolithic prompt

## What it is

Reviewing a 50+ requirement, 20+ file 'generate everything at once' Claude CLI prompt for an AIOps Jenkins OTA framework (Jenkins + Azure AI + Gitolite + Gerrit + Key Guardian + Artifactory) identified the risk of exceeding context limits and degrading output. The recurring fix is phased delivery over roughly 8 phases / 12 weeks (also seen on a separate embedded-systems AI code-review project); secrets for the Jenkins framework are isolated per-job in jobs/{job_name}/.env files injected via --env-file, never embedded in generated files.

## Why it matters

A recurring, validated fix pattern: large multi-tool build prompts should always be phased rather than generated monolithically, to avoid context-limit degradation.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Automation & Workflow]] · [[Home]]
