---
title: "Homeware is Vantiva's OEM firmware product spanning multiple SoC vendors (Broadcom, Qualcomm, Airoha)"
type: knowledge-entry
domain: "Project State"
entry-type: "Claim"
confidence: high
durability: durable
evidence: 2
summary: "The Homeware codebase (homeware_23.2.a) is OEM firmware for multiple SoC platforms (Broadcom, Qualcomm, Airoha) with a layered architecture (bootloader/U-Boot, kernel, drivers, middleware, application"
tags: [knowledge, project-state, conf/high, durable, homeware, oem-firmware, u-boot, streamlit]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Homeware is Vantiva's OEM firmware product spanning multiple SoC vendors (Broadcom, Qualcomm, Airoha)

## What it is

The Homeware codebase (homeware_23.2.a) is OEM firmware for multiple SoC platforms (Broadcom, Qualcomm, Airoha) with a layered architecture (bootloader/U-Boot, kernel, drivers, middleware, applications), including vendor-specific bootloader trees like u-boot-airoha and u-boot-2014.04-rc1 under tclinux_phoenix. An interactive Streamlit 'architecture explorer' (run inside a Docker container named epic_curran, bound to 0.0.0.0) was built to onboard new developers and do OEM-aware code review (config-placement checks, MODULE_LICENSE, GFP_KERNEL vs GFP_ATOMIC) across these layers.

## Why it matters

This establishes both what Homeware is and that a dedicated onboarding/review tool already exists for it, relevant to any future Homeware-related engineering or tooling question.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
