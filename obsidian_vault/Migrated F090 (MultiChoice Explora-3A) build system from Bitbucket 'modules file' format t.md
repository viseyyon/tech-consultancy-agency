---
title: "Migrated F090 (MultiChoice Explora-3A) build system from Bitbucket 'modules file' format to Gerrit repo manifest.xml"
type: knowledge-entry
domain: "Project State"
entry-type: "Claim"
confidence: medium
durability: durable
evidence: 1
summary: "F090 is a 14-component embedded product line (MultiChoice Explora-3A) previously tracked via a custom Perl 'modules file' format read by a getstable.pl script. He had this reverse-engineered and conve"
tags: [knowledge, project-state, conf/medium, durable, f090, gerrit-migration, repo-manifest, bitbucket]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Project State]]"]
---

# Migrated F090 (MultiChoice Explora-3A) build system from Bitbucket 'modules file' format to Gerrit repo manifest.xml

## What it is

F090 is a 14-component embedded product line (MultiChoice Explora-3A) previously tracked via a custom Perl 'modules file' format read by a getstable.pl script. He had this reverse-engineered and converted via a custom Python tool (modules2manifest_advanced.py) into a valid Google repo manifest.xml, as part of a broader Bitbucket-to-Gerrit migration planned as a 6-phase, 8-12 week rollout.

## Why it matters

A working conversion tool and reference approach already exists for any future migration of legacy Perl-modules-file build tracking to a standard repo manifest format.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Project State]] · [[Home]]
