---
title: "linkedin-bridge is a read-only Playwright automation with a dedicated Chrome profile"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Resource"
confidence: medium
durability: durable
evidence: 1
summary: "linkedin-bridge (~/mcp-servers/linkedin-bridge/server.py) automates LinkedIn via a dedicated, persistent Chromium profile at ~/.linkedin-bridge-profile, kept separate from the user's normal Chrome pro"
tags: [knowledge, developer-infrastructure, conf/medium, durable, linkedin-bridge, playwright, read-only, chrome-profile]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# linkedin-bridge is a read-only Playwright automation with a dedicated Chrome profile

## What it is

linkedin-bridge (~/mcp-servers/linkedin-bridge/server.py) automates LinkedIn via a dedicated, persistent Chromium profile at ~/.linkedin-bridge-profile, kept separate from the user's normal Chrome profile to avoid profile-lock conflicts. It only lists and reads conversations; it never sends messages. Login is via server.py --login, health via --check, configured through LINKEDIN_BROWSER_PROFILE / LINKEDIN_HEADLESS.

## Why it matters

Assuming this tool can send on the user's behalf, or running it against the user's main Chrome profile, would either take an unintended action or hit a profile lock.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Browser bridge and Notion MCP integration

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
