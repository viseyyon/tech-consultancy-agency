---
title: "Claude Code CLI install can leave a stale ~/.local/bin vs NVM PATH conflict on macOS"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "After installing Claude Code CLI 2.0.67 via the official installer, the binary lands at ~/.local/bin/claude but the shell may still resolve `claude` from an old NVM Node path, producing 'No such file"
tags: [knowledge, environment-tooling-state, conf/high, durable, claude-code, macos, path, nvm]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# Claude Code CLI install can leave a stale ~/.local/bin vs NVM PATH conflict on macOS

## What it is

After installing Claude Code CLI 2.0.67 via the official installer, the binary lands at ~/.local/bin/claude but the shell may still resolve `claude` from an old NVM Node path, producing 'No such file or directory'. Fix: run `hash -r` to clear the shell's command hash cache, then put `export PATH="$HOME/.local/bin:$PATH"` ahead of the NVM directory in shell config.

## Why it matters

Prevents wasted troubleshooting time when `claude` appears missing right after a fresh install on macOS.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
