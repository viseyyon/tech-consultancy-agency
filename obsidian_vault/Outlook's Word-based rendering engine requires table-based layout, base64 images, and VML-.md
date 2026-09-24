---
title: "Outlook's Word-based rendering engine requires table-based layout, base64 images, and VML/MSO hardening"
type: knowledge-entry
domain: "Developer Infrastructure"
entry-type: "Technique"
confidence: medium
durability: durable
evidence: 1
summary: "Converting a modern HTML newsletter into an Outlook-sendable email requires replacing CSS Grid/Flexbox with nested HTML tables, inlining all styles, removing JavaScript, hardcoding CSS custom properti"
tags: [knowledge, developer-infrastructure, conf/medium, durable, outlook, html-email, vml, mso]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Developer Infrastructure]]"]
---

# Outlook's Word-based rendering engine requires table-based layout, base64 images, and VML/MSO hardening

## What it is

Converting a modern HTML newsletter into an Outlook-sendable email requires replacing CSS Grid/Flexbox with nested HTML tables, inlining all styles, removing JavaScript, hardcoding CSS custom properties as hex values, base64-embedding images, adding VML namespaces and an OfficeDocumentSettings block, zeroing mso-table-lspace/rspace, and wrapping the container in MSO conditional comments. To send, open the HTML in a browser, select-all, copy, and paste into an Outlook compose window to preserve the table structure natively.

## Why it matters

Gives a reusable, step-by-step conversion recipe for any future HTML-to-Outlook email task, avoiding broken layouts caused by Outlook's Word-based rendering engine.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Developer Infrastructure]] · [[Home]]
