---
title: "teamccp Gerrit + its GitHub EMU tenant frozen pending contract review, not GDPR sign-off"
type: knowledge-entry
domain: "Security & Guardrails"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 2
summary: "gerrit.teamccp.com turned out to be a Comcast-operated RDK consortium Gerrit (93% of its projects are rdk/*, committers are largely Comcast/Sky/Liberty/vendor staff) rather than Vantiva's own instance"
tags: [knowledge, security-guardrails, conf/high, durable, governance, contract, gdpr, teamccp]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Security & Guardrails]]"]
---

# teamccp Gerrit + its GitHub EMU tenant frozen pending contract review, not GDPR sign-off

## What it is

gerrit.teamccp.com turned out to be a Comcast-operated RDK consortium Gerrit (93% of its projects are rdk/*, committers are largely Comcast/Sky/Liberty/vendor staff) rather than Vantiva's own instance, so a Vantiva works-council or CSE sign-off gives no GDPR Article 6 basis over other companies' employees - mirroring a customer's Gerrit onto Vantiva infrastructure was ruled a contract question that sits before and separate from the GDPR question. Both the instance and its associated _comcast GitHub Enterprise Managed Users tenant are frozen for all mirroring including hygiene facts until contract review completes, enforced in code (collect.py refuses teamccp by name) rather than left as a policy note.

## Why it matters

Prevents anyone from treating a later privacy/GDPR approval as sufficient to unfreeze this instance - the actual blocker is contractual, not a data-protection sign-off.

## Provenance

- Confidence **high** · durability **durable** · supported by **2** archived item(s).

## Sources

- Gerrit/Gitolite/GitHub setup (2026-08-15)
- VCS realignment analysis + owner ratification

---

Part of [[MOC - Security & Guardrails]] · [[Home]]
