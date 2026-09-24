---
title: "PHOENIX Test Rig: 61 tests across 10 suites with an 8-category vendor/SOC/app error-attribution engine"
type: knowledge-entry
domain: "Project State"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "PHOENIX Test Rig is Vantiva's firmware binary validation system: 61 tests (IDs FV-001 to EM-002) across 10 suites covering flash/boot validation, race conditions, stress/load, negative scenarios, perf"
tags: [knowledge, project-state, conf/high, durable, phoenix, firmware-testing, rdk, test-automation]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# PHOENIX Test Rig: 61 tests across 10 suites with an 8-category vendor/SOC/app error-attribution engine

## What it is

PHOENIX Test Rig is Vantiva's firmware binary validation system: 61 tests (IDs FV-001 to EM-002) across 10 suites covering flash/boot validation, race conditions, stress/load, negative scenarios, performance, MSO validation, end-customer experience, OpenWrt, and mesh networking, extended beyond RDK to Airties, Airoha, and Purple Mesh. A FastAPI backend auto-classifies failures into 8 categories (vendor bug, SOC limitation, application bug, environment, config, flaky, infrastructure, unknown), with an 'ANTIGRAVITY' meta-prompt driving autonomous framework extension and a React UI decoupled from test execution.

## Why it matters

The 8-category attribution engine makes it possible to tell whether a firmware failure originates from vendor SDK, SOC, or application layer without manual triage.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
