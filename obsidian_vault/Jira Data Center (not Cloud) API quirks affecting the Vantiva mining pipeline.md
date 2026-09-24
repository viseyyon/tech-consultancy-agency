---
title: "Jira Data Center (not Cloud) API quirks affecting the Vantiva mining pipeline"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 2
summary: "Both mined Jira instances are Data Center, not Atlassian Cloud: only /rest/api/2 is available (no /rest/api/3, no nextPageToken, no Cloud enhanced search). expand=changelog truncates at roughly 100 en"
tags: [knowledge, developer-infrastructure, conf/high, durable, jira, data-center, xray, api-quirks]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Jira Data Center (not Cloud) API quirks affecting the Vantiva mining pipeline

## What it is

Both mined Jira instances are Data Center, not Atlassian Cloud: only /rest/api/2 is available (no /rest/api/3, no nextPageToken, no Cloud enhanced search). expand=changelog truncates at roughly 100 entries on deep pages, and the documented per-issue fallback endpoint (/rest/api/2/issue/{key}/changelog) itself returns HTTP 404 on both instances, so that fallback path is untested and would error rather than recover if truncation ever occurred. The Xray/raven testplan-to-execution endpoint also 404s on this DC instance; that relationship must come from issue links instead. Custom field IDs (platform, SoC vendor, etc.) are per-instance, not portable across Jira instances.

## Why it matters

Assuming Cloud-API behavior or a working changelog/testplan fallback against a Data Center instance produces silent data loss or an unhandled error at scale.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Cowork - Vantiva Jira and Confluence mining

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
