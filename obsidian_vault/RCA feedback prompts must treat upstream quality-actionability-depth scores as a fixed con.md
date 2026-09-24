---
title: "RCA feedback prompts must treat upstream quality/actionability/depth scores as a fixed contract, not re-derive them"
type: knowledge-entry
domain: "Decisions & Rationale"
entry-type: "Decision"
confidence: high
durability: durable
evidence: 1
summary: "When an RCA system already has Claude compute quality/actionability/technical-depth scores, the feedback-processing prompt (rdkb rca validate-feedback) must declare those as a formal SCORE INPUT CONTR"
tags: [knowledge, decisions-rationale, conf/high, durable, rca, scoring, feedback-loop, prompt-design]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Decisions & Rationale]]"]
---

# RCA feedback prompts must treat upstream quality/actionability/depth scores as a fixed contract, not re-derive them

## What it is

When an RCA system already has Claude compute quality/actionability/technical-depth scores, the feedback-processing prompt (rdkb rca validate-feedback) must declare those as a formal SCORE INPUT CONTRACT and only do threshold gating plus feedback-modulated adjustment, not re-derive scores with a separate manual rubric. A score-audit-trail phase persists predicted vs. actual outcome (score_predicted_intent -> SCORE_MISS flag) for longitudinal calibration.

## Why it matters

Prevents double-scoring drift and enables tracking how well predicted scores match real developer corrections over time.

## Provenance

- Confidence **high** · durability **durable** · supported by **1** archived item(s).

## Sources

- Claude conversation archive (claude.ai export, 2025-05 to 2026-08)

---

Part of [[MOC - Decisions & Rationale]] · [[Home]]
