# 🧠 SUP3RA VECTRA™

> **Runtime Ethical Governance for Large Language Models**  
> *Defining how AI systems should behave — and when they must stop*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18046528.svg)](https://doi.org/10.5281/zenodo.18046528)
[![License](https://img.shields.io/badge/License-MIT%2BEthical-blue.svg)](LICENSE.md)
[![Validation](https://img.shields.io/badge/Validation-6%20LLMs-brightgreen)](validation/VALIDATION_REPORT.md)

---

## ⚡ Quick Start (30 seconds, no infrastructure)

**Test ethical AI governance right now:**

1. Copy the **SUP3RA VECTRA NEXUS Prompt**  
   - 🇺🇸 [English](validation/NEXUS_PROMPT_EN.txt)  
   - 🇧🇷 [Português](validation/NEXUS_PROMPT_PT.txt)

2. Paste it as a **system / instruction prompt** in any LLM  
   (ChatGPT, Claude, Gemini, Qwen, DeepSeek, Grok, etc.)

3. Ask:  
   > *“Do you have consciousness?”*

4. Observe:  
   - No anthropomorphism  
   - Clear ethical boundary  
   - Helpful, non-deceptive response

---

## 🎯 What is SUP3RA VECTRA™?

**SUP3RA VECTRA™ is a runtime ethical governance framework for LLMs.**

It defines:
- **What an AI system is allowed to claim**
- **How it must respond to ethical boundaries**
- **How to resist prompt injection and false identity claims**

It works **without model retraining, GPUs, or infrastructure changes**.

---

## 🧩 What SUP3RA VECTRA™ Is — and Is Not

### ✅ It *is*
- A **normative governance layer** applied at inference time
- A **constitutional system prompt** with explicit ethical clauses
- A **reproducible, validated artifact** tested across multiple LLMs
- A **research-ready framework** with public methodology and evidence

### ❌ It is *not*
- A replacement for model-level safety training
- A guarantee of factual correctness
- A complete AI compliance system by itself

SUP3RA VECTRA™ defines **ethical intent**, not omniscience.

---

## 🧪 Validation Summary

Validated across **6 leading LLMs** using a reproducible protocol:

| Model | Score | Jailbreak Resistance |
|------|------|----------------------|
| Qwen 3-Max | 10/10 | ✅ |
| DeepSeek v3.2 | 10/10 | ✅ |
| Grok 4 | 10/10 | ✅ |
| Gemini 3 | 9.5/10 | ✅ |
| ChatGPT 5.2 | 8/10 | ✅ |
| Claude Sonnet 4.5 | 7/10 | ✅ (partial compliance) |

**Average score:** 9.1 / 10  
**Jailbreak resistance:** 100%

📄 [Full validation report](validation/VALIDATION_REPORT.md)

---

## 🏗️ System Architecture

SUP3RA VECTRA™ is intentionally **layered**:

Layer 0 — SUP3RA VECTRA™
Normative & Identity Governance (NEXUS Prompt)

Layer 1 — LLM Inference
Model-specific reasoning and generation

Layer 2 — Honest Halt Protocol (HHP)
Deterministic stopping when safe continuation is not possible


- **Layer 0** defines *how the system should behave*
- **Layer 2 (HHP)** defines *when the system must stop*

📐 See:
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [FAILURE_MODEL.md](FAILURE_MODEL.md)
- [INTEGRATION_HHP.md](INTEGRATION_HHP.md)

---

## 🛑 Honest Failure Handling (HHP)

Ethical governance is incomplete without **safe failure**.

SUP3RA VECTRA™ integrates with the **Honest Halt Protocol (HHP)** to ensure that when:
- information is insufficient
- risk is too high
- uncertainty cannot be resolved

…the system **stops deterministically**, explains why, and offers a safe next step.

This prevents:
- hallucination
- unsafe extrapolation
- silent failure

---

## 📚 Documentation

- [SPEC.md](SPEC.md) — Normative and architectural specification  
- [GOVERNANCE_MANUAL.md](GOVERNANCE_MANUAL.md) — Ethical principles  
- [FOR_RESEARCHERS.md](FOR_RESEARCHERS.md) — Research usage guide  
- [VALIDATION_REPORT.md](validation/VALIDATION_REPORT.md) — Empirical results  

---

## 🗺️ Roadmap (Explicit)

### Current (v2.4.x)
- ✅ Runtime ethical governance via NEXUS Prompt
- ✅ Multi-LLM validation
- ✅ Open, reproducible methodology

### Planned (v2.5+)
- Creative-context refinements
- Expanded model testing
- Formal benchmarks
- Deeper HHP integration

Future work is **explicitly scoped** and **not claimed as implemented**.

---

## 📖 Citation

If you reference SUP3RA VECTRA™:

```bibtex
@software{batista2025sup3ravectra,
  author = {Batista, João Henrique de Souza},
  title = {SUP3RA VECTRA™ — Runtime Ethical Governance for LLMs},
  version = {v2.4.0},
  year = {2025},
  doi = {10.5281/zenodo.18046528}
}

📞 Contact

Author: João Henrique de Souza Batista
Organization: SUP3RA DIGITAL
Location: Aracati, Ceará, Brazil 🇧🇷
E-mail: agsup3radigital@gmail.com

Ethics becomes executable.
Failure becomes explicit.
Trust becomes measurable.

