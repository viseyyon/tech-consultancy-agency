---
title: "Foundry Local GA is a ~20MB in-process ONNX library, not a daemon — catalog-curated, WinML-registered"
type: note
tags: [model-serving-local-inference, onnx, foundry-local, windows-ai, on-device]
created: 2026-08-24
updated: 2026-08-24
status: evergreen
confidence: high
summary: "Microsoft Foundry Local GA'd 2026-04-09 as an embedded native library (.dll/.so/.dylib, ~20MB) loaded in-process by the app — the preview-era CLI/service architecture is explicitly legacy. Inference = ONNX Runtime with plugin EPs; Windows EP acquisition/registration goes through WinML; models come from the curated Foundry Catalog as hardware-optimized quantized ONNX variants."
related: ["[[MOC - Model Serving & Local Inference]]"]
---

# Foundry Local GA architecture (validated 2026-08-24)

**Core claim.** At GA (April 9, 2026) Foundry Local ships as a single platform-native library the app loads in-process — no CLI, daemon, or background service. SDKs: C# (`Microsoft.AI.Foundry.Local`, plus `.WinML` variant on Windows), Python/JS (`foundry-local-sdk`), Rust (crates.io). Adds ~20MB to the app package. An OpenAI-compatible REST endpoint (incl. Responses API) is optional and runs inside the app process.

## Mechanics

- **ONNX Runtime** does inference: graph partitioning/optimization, runtime-loaded plugin execution providers, CPU EP as guaranteed fallback.
- **EP matrix**: NVIDIA CUDA (Win/Linux GPU) · WebGPU-via-Dawn (Win/Linux/macOS GPU) · AMD Vitis NPU (Win) · Qualcomm QNN NPU (Win) · Intel OpenVINO (Win) · CPU everywhere. On Apple Silicon the chain is ONNX → WebGPU EP → Dawn → Metal (FP16, GPU-side tensors, graph capture) — deliberately **no dedicated Metal/CoreML EP**.
- **WinML (Windows only)** acquires hardware-matched EP plugins from OS/Windows Update, registers them with ONNX Runtime, negotiates driver compat. Linux/macOS: SDK bundles EPs and registers directly.
- **Foundry Catalog**: cloud registry of curated, hardware-optimized quantized ONNX variants (Phi, Qwen, DeepSeek, Mistral, GPT-OSS, Whisper). Download-on-first-use → local cache → fully offline after. Version pinning or auto-update. BYO models via Olive (HF → ONNX), though quantization×EP compatibility is non-trivial.

## Positioning & caveats

- Single-user client inference by design — no continuous batching; Microsoft itself points to vLLM/Triton for multi-user serving.
- Vs [[Ollama has no native fine-tuning; 'training' on a codebase means a Modelfile, not updated|Ollama]]/llama.cpp: Foundry Local targets developers *shipping* bundled AI (zero end-user setup); Ollama targets end users with GGUF freedom; llama.cpp gives explicit backend/quant control. Catalog-only selection and automatic EP choice = less tuning freedom. Linux GPU story: CUDA + WebGPU only.
- In-process design means the runtime competes with the host app for RAM/VRAM — a real sizing concern for models >2-4GB.
- "Hardware-optimized variants" break the write-once illusion: cache holds per-hardware artifacts, not one universal file (contrast: single GGUF).
- Check per-model catalog licenses before commercial shipping; OpenAI-compat ≠ full parity (tool-calling/streaming vary per model/EP).

## Council validation (2026-08-24)

3/5 seats usable (Opus 4.6, GPT-OSS quota-failed). Verdict: "mostly accurate." Both Gemini seats + Sonnet objected with **stale pre-2026 knowledge** (claimed DirectML is the flagship EP, WinML is legacy, CoreML on macOS, and that Foundry Local is a CLI/service) — all superseded by the current MS Learn architecture doc: the GA redesign *replaced* the preview CLI/service with the embedded library, and new-WinML plugin EPs *replaced* the DirectML path. Council dissent here was itself the strongest confirmation that the GA pivot is recent and poorly known. Genuinely useful council additions folded in above: host-memory competition, per-hardware cache variants, licensing, OpenAI-compat gaps.

## Sources

- [Architecture overview](https://learn.microsoft.com/azure/foundry-local/concepts/foundry-local-architecture) · [What is Foundry Local](https://learn.microsoft.com/azure/foundry-local/what-is-foundry-local) · [SDK reference](https://learn.microsoft.com/azure/foundry-local/reference/reference-sdk-current) · [GA announcement](https://devblogs.microsoft.com/foundry/foundry-local-ga/) · [Compile HF models with Olive](https://learn.microsoft.com/azure/foundry-local/how-to/how-to-compile-hugging-face-models) · [Windows AI decision tree](https://learn.microsoft.com/windows/ai/overview)

Part of [[MOC - Model Serving & Local Inference]]
