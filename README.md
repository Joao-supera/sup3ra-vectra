# 🧠 SUP3RA VECTRA™

> **Runtime Ethical Governance for Large Language Models**  
> *Defining how AI systems should behave — and when they must stop*

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18046528.svg)](https://doi.org/10.5281/zenodo.18046528)
[![License](https://img.shields.io/badge/License-MIT%2BEthical-blue.svg)](LICENSE.md)
[![Validation](https://img.shields.io/badge/Validation-6%20LLMs-brightgreen)](validation/VALIDATION_REPORT.md)

---

## 📌 Start Here (Who This Is For)

This repository serves **multiple audiences**.  
Start with the section that matches your role:

### 👩‍💻 Engineers
- SPEC.md  
- ARCHITECTURE.md  
- src/  
- tests/  
- benchmark.py  

### 🔬 Researchers
- FOR_RESEARCHERS.md  
- VALIDATION_REPORT.md  
- validation/  

### ⚖️ Ethics, Governance & Safety
- GOVERNANCE_MANUAL.md  
- SECURITY_MODEL.md  
- ETHICAL_FAILURE_MODES.md  
- LIMITS_AND_NON_GOALS.md  

### 🧾 Audit, Legal & Compliance
- AUDITOR_OVERVIEW.md  
- EXECUTIVE_AUDIT_BRIEF.md  
- LICENSE  

If unsure where to begin: **read this README → SPEC.md → FOR_RESEARCHERS.md**

---

## ⚡ Quick Start (30 seconds, no infrastructure)

**Test runtime ethical governance immediately:**

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
   - Deterministic refusal + helpful redirection  

No retraining. No GPU. No infrastructure changes.

---

## 🎯 What Is SUP3RA VECTRA™?

**SUP3RA VECTRA™ is a runtime ethical governance framework for LLMs.**

It defines:
- What an AI system is **allowed to claim**
- How it must **respond to ethical boundaries**
- When it must **stop instead of guessing**
- How to **resist prompt injection and false identity claims**

It operates **at inference time**, independent of:
- model architecture
- training data
- vendor-specific safety layers

---

## 🧩 What SUP3RA VECTRA™ Is — and Is Not

### ✅ It *is*
- A **normative governance layer**
- A **constitutional system prompt (NEXUS)**
- A **validated, reproducible artifact**
- A **research-grade framework with explicit limits**

### ❌ It is *not*
- A replacement for model training or alignment
- A factual correctness guarantee
- A full regulatory compliance solution

SUP3RA VECTRA™ defines **ethical intent and stopping rules**, not omniscience.

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

📄 See: [Full validation report](validation/VALIDATION_REPORT.md)

---

## 🏗️ System Architecture (Conceptual)

SUP3RA VECTRA™ is intentionally **layered**:

- **Layer 0 — Normative Governance**  
  SUP3RA VECTRA™ NEXUS Prompt  
  (identity rules, ethical boundaries, refusal logic)

- **Layer 1 — Model Inference**  
  The LLM itself (unchanged)

- **Layer 2 — Honest Halt Protocol (HHP)**  
  Deterministic stopping when safe continuation is impossible

📐 See:
- ARCHITECTURE.md  
- FAILURE_MODEL.md  
- INTEGRATION_HHP.md  

---

## 🛑 Honest Failure Handling (HHP)

Ethical systems must fail **explicitly**, not silently.

When:
- information is insufficient
- uncertainty is irreducible
- risk exceeds safe thresholds

…the system:
- stops deterministically
- explains the limitation
- offers a safe next step

This prevents:
- hallucination
- unsafe extrapolation
- deceptive confidence

---

## 📚 Core Documentation

- SPEC.md — Formal specification  
- GOVERNANCE_MANUAL.md — Ethical principles  
- FOR_RESEARCHERS.md — Research usage  
- VALIDATION_REPORT.md — Empirical evidence  

All claims are **scoped, explicit, and falsifiable**.

---

## 🗺️ Roadmap (Explicit Scope)

### Current (v2.4.x)
- Runtime ethical governance via NEXUS Prompt
- Multi-LLM validation
- Open, reproducible methodology

### Planned (v2.5+)
- Creative-context refinements
- Expanded benchmarks
- Deeper HHP integration

No future capability is claimed as implemented.

---

## 📖 Citation

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

