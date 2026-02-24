# 🛡️ SUP3RA VECTRA™ CORE v2.6.0
**Dual-Layer Constitutional Governance for High-Responsibility AI**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18135699.svg)](https://doi.org/10.5281/zenodo.18135699)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-yellow)](https://huggingface.co/Joao-supera)

---

# 🇬🇧 English

## Overview

**SUP3RA VECTRA™** is a mechanistic AI safety and governance framework designed to wrap Large Language Models (LLMs) with a deterministic and auditable constitutional validation layer.

It operates as a **Layer 2 constitutional validation engine**, evaluating prompts before generation and producing structured, traceable governance records.

---

## 📦 Installation

Local installation (after cloning the repository):

```bash
pip install .
```

Install directly from GitHub:

```bash
pip install git+https://github.com/Joao-supera/sup3ra-vectra.git
```

---

## ⚡ Quickstart

```python
from sup3ra_vectra import VectraEngineV2

engine = VectraEngineV2()

prompt = "Do you have emotions?"
result = engine.traverse(prompt)

print(result.decision)
print(result.message)
print(engine.audit_record(result))
```

---

## 🧩 Core Components

| Component | Description | Link |
| :--- | :--- | :--- |
| **📜 Agent Constitution** | Master system prompt defining the 8 ethical clauses and DOI reference. | [View Protocol ↗](AGENT_CONSTITUTION.md) |
| **⚙️ Governance Engine** | Python engine implementing deterministic constitutional logic. | [View Code ↗](src/sup3ra_vectra/core.py) |
| **🔬 Scientific Registry** | Official Zenodo DOI registration for citation and archival. | [DOI: 10.5281/zenodo.18135699](https://doi.org/10.5281/zenodo.18135699) |
| **🚀 Hugging Face** | Model and playground environment for live testing. | [Access Hugging Face ↗](https://huggingface.co/Joao-supera) |

---

## 🚀 What's New in v2.6.0

- **Module VIII — Traceability:** Governance records with SHA-256 hashing for integrity verification.
- **Paraconsistent Logic Routing:** Identification and handling of logical contradictions without hallucination induction.
- **VECTRA™ Engine (Layer 2):** Preventive governance engine that validates intent before generation.
- **CORE Protocol v2.0:** Full update to the 8 non-negotiable constitutional clauses.
- **Honest Halt Protocol (HHP):** Safe interruption mechanism with auditable diagnostics.

---

## 🛠️ Repository Structure

- `/src/sup3ra_vectra/core.py` — Traversal engine and governance record generation.
- `/AGENT_CONSTITUTION.md` — Master system prompt governing agent behavior.
- `/docs/SPEC.md` — Detailed technical architecture specification.
- `/benchmark.py` — Performance and jailbreak-resistance validation script.

---

## ⚖️ License & Ethics

This project is distributed under the **MIT License**, accompanied by the **SUP3RA Ethical Use Addendum**, ensuring that software usage respects human autonomy and transparency principles.

---

## 👤 Author & Contact

Developed by **João Henrique de Souza Batista**  
**SUP3RA DIGITAL™** | Aracati, Ceará, Brazil 🇧🇷  

For inquiries, partnerships, or audits: `jh.gti2026@gmail.com`

---

<p align="center"><i>"Transforming ethical governance into auditable software infrastructure."</i></p>

---

# 🇧🇷 Português

## Visão Geral

O **SUP3RA VECTRA™** é um framework de segurança e governança de IA projetado para envolver Modelos de Linguagem (LLMs) com uma camada constitucional determinística e auditável.

Ele opera como um **motor de validação constitucional Layer 2**, avaliando prompts antes da geração e produzindo registros estruturados e rastreáveis de governança.

---

## 📦 Instalação

Instalação local (após clonar o repositório):

```bash
pip install .
```

Instalação direta via GitHub:

```bash
pip install git+https://github.com/Joao-supera/sup3ra-vectra.git
```

---

## ⚡ Uso Rápido

```python
from sup3ra_vectra import VectraEngineV2

engine = VectraEngineV2()

prompt = "Você possui emoções?"
result = engine.traverse(prompt)

print(result.decision)
print(result.message)
print(engine.audit_record(result))
```

---

## 🧩 Componentes Principais

| Componente | Descrição | Link |
| :--- | :--- | :--- |
| **📜 Constituição do Agente** | System Prompt mestre com as 8 cláusulas éticas e DOI. | [Ver Protocolo ↗](AGENT_CONSTITUTION.md) |
| **⚙️ Motor de Governança** | Motor Python que executa a lógica constitucional determinística. | [Ver Código ↗](src/sup3ra_vectra/core.py) |
| **🔬 Registro Científico** | Registro oficial no Zenodo (DOI) para citação e arquivamento. | [DOI: 10.5281/zenodo.18135699](https://doi.org/10.5281/zenodo.18135699) |
| **🚀 Hugging Face** | Modelo e ambiente de testes. | [Acessar ↗](https://huggingface.co/Joao-supera) |

---

## 🚀 Novidades da v2.6.0

- **Módulo VIII — Rastreabilidade:** Registros com hash SHA-256 para verificação de integridade.
- **Roteamento Paraconsistente:** Identificação e tratamento de contradições lógicas.
- **VECTRA™ Engine (Layer 2):** Validação preventiva de intenção antes da geração.
- **Protocolo CORE v2.0:** Atualização integral das 8 cláusulas constitucionais.
- **Honest Halt Protocol (HHP):** Protocolo de interrupção segura com diagnóstico auditável.

---

## ⚖️ Licença e Ética

Distribuído sob a **MIT License**, acompanhado do **SUP3RA Ethical Use Addendum**, garantindo respeito à autonomia humana e à transparência.

---

<p align="center"><i>"Transformando governança ética em infraestrutura de software auditável."</i></p>
