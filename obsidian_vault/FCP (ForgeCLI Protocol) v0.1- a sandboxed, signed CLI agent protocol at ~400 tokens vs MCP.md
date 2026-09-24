---
title: "FCP (ForgeCLI Protocol) v0.1: a sandboxed, signed CLI agent protocol at ~400 tokens vs MCP's 15k-55k"
type: knowledge-entry
domain: "MCP & Tool Integration"
entry-type: "Tool"
confidence: high
durability: durable
evidence: 1
summary: "FCP (ForgeCLI Protocol) v0.1 is a designed-but-unbuilt token-lean alternative to MCP for CLI-based agent tool calls: broker-mediated execve with typed argv (no shell execution), Sigstore-signed tool m"
tags: [knowledge, mcp-tool-integration, conf/high, durable, fcp, mcp, token-efficiency, protocol-design]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - MCP & Tool Integration]]"]
---

# FCP (ForgeCLI Protocol) v0.1: a sandboxed, signed CLI agent protocol at ~400 tokens vs MCP's 15k-55k

## What it is

FCP (ForgeCLI Protocol) v0.1 is a designed-but-unbuilt token-lean alternative to MCP for CLI-based agent tool calls: broker-mediated execve with typed argv (no shell execution), Sigstore-signed tool manifests, progressive schema disclosure, per-invocation OAuth 2.1, default-deny sandboxing (bubblewrap/nsjail/gVisor), workspace file refs instead of shell pipes, and a hash-chained audit ledger meant to slot into SYNTH-GUARD. It targets ~400 idle tokens vs MCP's measured 15k-55k (tool definitions alone eating up to 72% of context), with a stated kill criterion of ≥5x token improvement and a scoped 2-week MVP path not yet started.

## Why it matters

If MCP's token overhead becomes a real bottleneck, FCP is the already-designed fallback with a concrete kill criterion, so it shouldn't need to be re-derived from scratch.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - MCP & Tool Integration]] · [[Home]]
