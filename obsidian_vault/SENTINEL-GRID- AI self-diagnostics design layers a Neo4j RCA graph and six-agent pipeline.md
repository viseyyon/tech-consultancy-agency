---
title: "SENTINEL-GRID: AI self-diagnostics design layers a Neo4j RCA graph and six-agent pipeline onto stock Zabbix"
type: knowledge-entry
domain: "Agent Architecture & Orchestration"
entry-type: "Pattern"
confidence: medium
durability: durable
evidence: 1
summary: "SENTINEL-GRID adds AI self-diagnostics to open-source Zabbix without forking it: a Neo4j knowledge graph modeling Host→Interface→Item→Trigger→Event plus service-dependency edges (turning 200 alerts in"
tags: [knowledge, agent-architecture-orchestration, conf/medium, durable, sentinel-grid, zabbix, neo4j, rca]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Agent Architecture & Orchestration]]"]
---

# SENTINEL-GRID: AI self-diagnostics design layers a Neo4j RCA graph and six-agent pipeline onto stock Zabbix

## What it is

SENTINEL-GRID adds AI self-diagnostics to open-source Zabbix without forking it: a Neo4j knowledge graph modeling Host→Interface→Item→Trigger→Event plus service-dependency edges (turning 200 alerts into one root node), a multi-agent RCA pipeline triggered via Zabbix webhooks, AI-driven self-discovery/auto-enrollment of new agents (LLM classifies workload type and applies templates), per-hop network path monitoring (MTR/traceroute, SNMP interface LLD, optical DOM), and a full SLA/incident/metrics framework — produced as a complete master design in one session on 2026-07-17.

## Why it matters

A non-invasive design pattern for bolting AI RCA/self-diagnostics onto an existing monitoring tool rather than replacing it.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Agent Architecture & Orchestration]] · [[Home]]
