---
title: "Personal-namespace repo identifiers flagged and countable, never a derivation source"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "Ruled that repos/refs in personal namespaces (131 of 44,925 classified repo names) are recorded with a boolean flag but never used to extract a person-level fact - no handle-to-person join, no per-han"
tags: [knowledge, security-guardrails, conf/high, durable, privacy, redaction, content-read, identity]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# Personal-namespace repo identifiers flagged and countable, never a derivation source

## What it is

Ruled that repos/refs in personal namespaces (131 of 44,925 classified repo names) are recorded with a boolean flag but never used to extract a person-level fact - no handle-to-person join, no per-handle ranking, test-enforced that no query aggregates by an extracted handle. Redaction of the 131 flagged repos was explicitly refused (a redactor that removed them 'would destroy the census to protect it') - they stay flagged, counted, and aggregate-only, matching a DPIA statement that names in repo paths are retained only as object identifiers. Separately, object-level content reading was granted as a new content_read matrix column (not an overload of the existing mirror-allowed flag) with tight bounds - shallow, blobless, sparse-checkout against a committed allowlist, ephemeral clones deleted same-operation - initially for only three ratified VCS instances, later cautiously extended to one more (gerrit_tonic) while a fourth (videogit01) stayed denied because its measurement interval was too wide to trust any aggregate over it.

## Why it matters

Defines exactly what 'aggregate-only, never a derivation source' is allowed to mean in practice, and shows the content-read grant is incremental and evidence-gated, not a blanket unlock.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Gerrit/Gitolite/GitHub setup (2026-08-16)

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
