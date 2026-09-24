---
title: "Git-commit-derived training data generator (GitPython-based)"
type: knowledge-entry
domain: "Model Serving & Local Inference"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "He built a script pipeline using GitPython that walks a parent directory of git repos, extracts up to 1,000 non-merge commits per repo, decodes each patch diff, and formats them into instruction/outpu"
tags: [knowledge, model-serving-local-inference, conf/high, durable, git, fine-tuning-data, gitpython, automation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Git-commit-derived training data generator (GitPython-based)

## What it is

He built a script pipeline using GitPython that walks a parent directory of git repos, extracts up to 1,000 non-merge commits per repo, decodes each patch diff, and formats them into instruction/output JSONL training samples for fine-tuning. Key functions include generate_git_sample_data, find_git_repos, extract_commit_samples, and generate_finetune_data_from_repos, with reusable scripts named prepare_finetune_data.py and generate_ollama_finetune_data.py; a GitHub API variant uses a personal access token for the same extraction.

## Why it matters

This is a reusable data-generation tool he has already built for turning any codebase's git history into LLM fine-tuning data.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- AI Automation Projects — Ollama & Phi-4 Fine-Tuning Detail

---

Part of [[MOC - Model Serving & Local Inference]] · [[Home]]
