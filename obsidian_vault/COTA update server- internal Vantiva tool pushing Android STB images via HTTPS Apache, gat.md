---
title: "COTA update server: internal Vantiva tool pushing Android STB images via HTTPS Apache, gated by MAC-address whitelist"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: medium
durability: durable
evidence: 1
summary: "COTA (Custom Over-The-Air) is an internal Vantiva tool pushing Android APK images to set-top-box devices over a simple HTTPS Apache server, authorizing devices by a MAC-address whitelist. He built a w"
tags: [knowledge, project-state, conf/medium, durable, cota, android-stb, ota-updates, jwt-auth]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# COTA update server: internal Vantiva tool pushing Android STB images via HTTPS Apache, gated by MAC-address whitelist

## What it is

COTA (Custom Over-The-Air) is an internal Vantiva tool pushing Android APK images to set-top-box devices over a simple HTTPS Apache server, authorizing devices by a MAC-address whitelist. He built a web front-end and Flask backend for it, later extended with JWT-based admin login, drag-and-drop APK upload with automatic version detection from the filename, and one-click 'set as active' switching that updates the download JSON config automatically.

## Why it matters

A working, extended admin interface for COTA already exists, so future STB image-push work should build on this rather than the bare Apache server.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
