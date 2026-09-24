---
title: "In Claude Code bash sessions, /mnt/user-data/uploads is read-only — copy to /home/claude before unzip/extract"
type: knowledge-entry
domain: "Claude Code Practice"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "Attempting to unzip or modify files directly in /mnt/user-data/uploads fails because it is mounted read-only; the working pattern is `cp /mnt/user-data/uploads/file.zip /home/claude/ && cd /home/claud"
tags: [knowledge, claude-code-practice, conf/high, durable, claude-code, file-system, read-only, uploads]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Claude Code Practice]]"]
---

# In Claude Code bash sessions, /mnt/user-data/uploads is read-only — copy to /home/claude before unzip/extract

## What it is

Attempting to unzip or modify files directly in /mnt/user-data/uploads fails because it is mounted read-only; the working pattern is `cp /mnt/user-data/uploads/file.zip /home/claude/ && cd /home/claude && unzip -q file.zip`.

## Why it matters

Avoids wasted attempts to write into a read-only mount during file-extraction tasks.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Claude Code Practice]] · [[Home]]
