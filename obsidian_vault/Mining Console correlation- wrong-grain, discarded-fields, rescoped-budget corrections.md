---
title: "Mining Console correlation: wrong-grain, discarded-fields, rescoped-budget corrections"
type: knowledge-entry
domain: "Project State"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 6
summary: "The correlation pipeline's low match rate (0.27% of issues) was first blamed on Vantiva's Jira having empty custom fields, but investigation found platform/SoC custom fields really are almost unpopula"
tags: [knowledge, project-state, conf/high, durable, attribution, grain, product-taxonomy, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Mining Console correlation: wrong-grain, discarded-fields, rescoped-budget corrections

## What it is

The correlation pipeline's low match rate (0.27% of issues) was first blamed on Vantiva's Jira having empty custom fields, but investigation found platform/SoC custom fields really are almost unpopulated org-wide (0.19%/1.7% of 1.9M issues) - the real signal was that product identity lives in the PROJECT KEY (e.g. CGA4233VDF = family CGA4233 + operator VDF), so per-project inheritance gives ~100% attribution for the 64 alias-matched projects versus near-zero from per-issue text matching. A second defect then surfaced: the extractor was fetching components/fixVersions/platform/SoC fields over the wire and then discarding them unwritten (an unimplemented TODO), and a populated labels field (66% of issues) was never scanned by the matcher at all - fixing this before the full sync saved an estimated 72h re-sync. The sync budget itself was corrected twice: an initial 72.6h estimate was actually the cost of a different, larger 100-project non-product set; the real 64-project scope needed only ~5 hours at a measured 3.55 issues/s.

## Why it matters

Anyone extending Vantiva product-family correlation needs the project-key-first rule and must confirm the extractor actually persists (not just fetches) every field it uses before trusting coverage numbers.

## Provenance

- Confidence **high** · durability **durable** · supported by **6** archived item(s).

## Sources

- ESCALATION-003 ruling
- ESCALATION-002 ruling
- ESCALATION-001 ruling
- Vantiva Jira and Confluence mining (2026-08-16)

---

Part of [[MOC - Project State]] · [[Home]]
