---
title: "NFS-mediated memory pressure on IronCore is tool-agnostic, not an OpenCode design flaw"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "Swap exhaustion on the IronCore RDK-B/Yocto build server traced to orphaned OpenCode sessions persisting after terminal close (auto-clean/version bugs), to be fixed with a 20-session/user cap. Separat"
tags: [knowledge, environment-tooling-state, conf/high, durable, ironcore, nfs, yocto, opencode]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# NFS-mediated memory pressure on IronCore is tool-agnostic, not an OpenCode design flaw

## What it is

Swap exhaustion on the IronCore RDK-B/Yocto build server traced to orphaned OpenCode sessions persisting after terminal close (auto-clean/version bugs), to be fixed with a 20-session/user cap. Separately, accessing Linux NFS-mounted files through Windows VS Code/Copilot causes cache thrash, temp/.vscode bloat, inotify polling fallback, symlink/case-sensitivity breakage, and .git/index locking races — a property of the NFS mount topology, not of any one agent, so it affects Copilot, OpenCode, and would affect Claude Code identically.

## Why it matters

Any future report of 'Claude Code is causing memory/lock issues on IronCore' should be checked against this NFS-mount-topology explanation before assuming a Claude-specific bug; VS Code Remote-SSH is the recommended fix.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
