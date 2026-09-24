---
title: "Mining Console's ingest pipeline repeatedly shipped false-pass verification checks"
type: knowledge-entry
domain: "Evaluation & Observability"
entry-type: "Caveat"
confidence: high
durability: durable
evidence: 4
summary: "Multiple independent incidents showed a check reporting PASS without actually evaluating the thing it claimed to guard: a gate validated one artifact (error_signature_normalizer) while the build shipp"
tags: [knowledge, evaluation-observability, conf/high, durable, false-pass, verification, data-integrity, mining-console]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Evaluation & Observability]]"]
---

# Mining Console's ingest pipeline repeatedly shipped false-pass verification checks

## What it is

Multiple independent incidents showed a check reporting PASS without actually evaluating the thing it claimed to guard: a gate validated one artifact (error_signature_normalizer) while the build shipped a different, broken one (error_signature_normalizer_v2), inflating an error count from an eventual-correct 772 to a wrong 855; a component/fixVersion persistence check (SC4) passed on the excuse 'source data is empty' when the fields were demonstrably populated in live Jira; a counter-mismatch self-check would have discarded all 3,363 committed rows on its very next run because it conflated Jira's reported issue count with the DB's row count; and a circuit breaker added to the Confluence sync path was never added to the sibling Jira ingest path, silently quarantining 42% of one project's rows. The standing rule adopted from these: a check is not a check until it has been observed failing on a deliberately planted violation, and any check protecting one path must be moved into shared code both paths call, not duplicated per path.

## Why it matters

Anyone trusting a green verification result on this pipeline needs to know green has repeatedly meant 'the check didn't actually run,' not 'the thing is correct.'

## Provenance

- Confidence **high** · durability **durable** · supported by **4** archived item(s).

## Sources

- Vantiva Jira and Confluence mining (2026-08-20)
- ESCALATION-004 ruling
- R5-fix D1/D2/D3 review

---

Part of [[MOC - Evaluation & Observability]] · [[Home]]
