---
title: "This Mac's default Python 3.13 breaks older pinned TensorFlow/NumPy versions"
type: knowledge-entry
domain: "Environment & Tooling State"
entry-type: "Resource"
confidence: medium
durability: durable
evidence: 1
summary: "The user's Mac runs Python 3.13, which is incompatible with tensorflow==2.18.0 and numpy 1.26.x as pinned in some assignment starter instructions. The working correction for ML notebook work on this m"
tags: [knowledge, environment-tooling-state, conf/medium, durable, python, tensorflow, numpy, mac]
created: 2026-08-23
updated: 2026-08-23
generated-by: obsidian_sync
related: ["[[MOC - Environment & Tooling State]]"]
---

# This Mac's default Python 3.13 breaks older pinned TensorFlow/NumPy versions

## What it is

The user's Mac runs Python 3.13, which is incompatible with tensorflow==2.18.0 and numpy 1.26.x as pinned in some assignment starter instructions. The working correction for ML notebook work on this machine is tensorflow==2.20.0, numpy>=2.0, scikit-learn>=1.5; no notebook code changes were needed since keras is already accessed via tensorflow.keras.

## Why it matters

Following an older pinned requirements list verbatim on this machine causes an install/import failure before any code even runs.

## Provenance

- Confidence **medium** · durability **durable** · supported by **1** archived item(s).

## Sources

- CNN Waste Segregation assignment

---

Part of [[MOC - Environment & Tooling State]] · [[Home]]
