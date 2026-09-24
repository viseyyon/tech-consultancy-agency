---
title: "Tooling"
memory_path: "/topics/tooling.md"
category: topic
description: "Established tools, pipelines, and storage patterns"
synced: "2026-08-23T17:00:20.509733+00:00"
tags:
  - claude-memory
  - topic
---

# Tooling

> [!info] Claude memory · `/topics/tooling.md` · synced 2026-08-23

## Facts

- Notion memory (notion-memory MCP) is the persistent storage pattern; the MCP server runs locally on Claude Desktop and is sensitive to session/restart state
- Reliable Notion memory pattern: `memory_query` before `memory_upsert`
- Working upsert fields: Details, Last updated, Source, Category, Tags, Type, Date, Summary
- PPTX generation pipeline: pptxgenjs via Node.js with LibreOffice headless conversion and pdftoppm QA
- Vantiva brand palette: NAVY `#3D5488`, CYAN `#00B9F2`, GREEN `#8DC63F`, ORANGE `#F26522`, RED `#ED1B2F`, MAGENTA `#BF245E`, PURPLE `#662D91`, TEAL `#0D9488`

## Related

- [[SYNTHFORCE-OC]]
- [[Recent Work]]

---

*Synced from Claude's persistent memory. Source of truth is the memory store; edits here are local.*
