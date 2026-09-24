---
title: "LinkedIn's individual-developer API tier has no real refresh tokens and no messaging access"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Caveat"
confidence: medium
durability: durable
evidence: 1
summary: "For personal LinkedIn post automation via the official API, individual developers get self-service app creation but access tokens expire every 60 days, and programmatic long-lived refresh tokens are g"
tags: [knowledge, mcp-tool-integration, conf/medium, durable, linkedin-api, oauth, token-expiry, automation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# LinkedIn's individual-developer API tier has no real refresh tokens and no messaging access

## What it is

For personal LinkedIn post automation via the official API, individual developers get self-service app creation but access tokens expire every 60 days, and programmatic long-lived refresh tokens are gated behind Marketing Developer Platform (MDP) partner approval — unavailable to individuals. Workaround: a browser-based re-auth script on a ~50-day cron, since the member stays logged in and LinkedIn silently reissues a token. The Messaging API is restricted to approved partners entirely; reading one's own posts is possible via the ugcPosts API.

## Why it matters

Any LinkedIn automation built on the individual-developer tier must plan around 60-day token expiry and cannot access messaging at all.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
