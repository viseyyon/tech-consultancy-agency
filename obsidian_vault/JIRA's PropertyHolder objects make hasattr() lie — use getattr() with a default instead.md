---
title: "JIRA's PropertyHolder objects make hasattr() lie — use getattr() with a default instead"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 1
summary: "The python-jira library's PropertyHolder objects implement `__getattr__` such that `hasattr(obj, 'priority')` returns True even when the attribute doesn't exist, causing `'PropertyHolder' object has n"
tags: [knowledge, developer-infrastructure, conf/high, durable, python-jira, hasattr, getattr, bug]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# JIRA's PropertyHolder objects make hasattr() lie — use getattr() with a default instead

## What it is

The python-jira library's PropertyHolder objects implement `__getattr__` such that `hasattr(obj, 'priority')` returns True even when the attribute doesn't exist, causing `'PropertyHolder' object has no attribute 'priority'` crashes when code trusts the hasattr check. Fix: use `getattr(obj, 'attr', default)` anywhere JIRA issue objects are touched, never hasattr().

## Why it matters

Prevents runtime crashes in any code that touches JIRA issue attributes via the python-jira library.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
