# 🧭 SUP3RA VECTRA™
### Vectorized Ethical Causal Traversal Architecture

**A framework for mechanistic AI safety without anthropomorphic assumptions**

[![Status](https://img.shields.io/badge/Status-Theoretical%20Framework-yellow)](https://github.com/joao-supera/sup3ra-vectra)
[![License](https://img.shields.io/badge/License-MIT%20%2B%20Ethical%20Clause-blue)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.1-green)](SPEC.md)

![Spec Version](https://img.shields.io/badge/Spec-v2.1-blue)
![License](https://img.shields.io/badge/License-MIT%20+%20Ethical%20Clause-green)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Joao-supera.sup3ra-vectra)
![Clones](https://img.shields.io/badge/Clones-50%2B-brightgreen)
![Validation](https://img.shields.io/badge/Validation-In_Progress-yellow)
![Language](https://img.shields.io/badge/Language-Python%20100%25-lightgrey)

---

## 🎯 What is This?

SUP3RA VECTRA™ rejects the dominant paradigm in AI safety that treats language models as "agents with goals."

Instead, it proposes:
- **Mechanistic intervention** via Sparse Autoencoder (SAE) features
- **Vectorized ethics** (not prompt engineering)
- **Causal transparency** (signed, immutable traversal logs)

> "We don't align minds. We align mechanisms."

---

## 📊 Current Status

### ✅ What Exists Now

| Component | Status | Description |
|-----------|--------|-------------|
| **Theoretical Framework** | ✅ Complete | [Full specification](SPEC.md) (v2.1) |
| **Architecture Design** | ✅ Complete | Ethical Gate → Causal Mapper → Vector Traverser |
| **Three Laws** | ✅ Defined | No simulation, causal honesty, vectorial ethics |
| **Academic Grounding** | ✅ Referenced | Bricken et al., Burns et al., Bai et al. |

### ⏳ What's Needed for Implementation

| Component | Status | Blocker |
|-----------|--------|---------|
| **SAE Feature Detection** | 🔴 Not Started | Requires GPU access + trained SAEs |
| **Activation Steering** | 🔴 Not Started | Requires model internals access |
| **Feature Atlas** | 🔴 Not Started | Needs systematic feature mapping |
| **Benchmarking** | 🔴 Not Started | Need to test on HarmBench, TruthfulQA, etc. |

---

## 🧪 Why This Approach Matters

Most AI safety frameworks fall into two categories:

### ❌ Category 1: Vague Principles
- "Be aligned with human values"
- "Avoid deceptive behavior"
- **Problem:** No mechanism, just aspirations

### ❌ Category 2: Black-Box Solutions
- RLHF without mechanistic understanding
- Constitutional AI via prompting
- **Problem:** Works until it doesn't (jailbreaks, adversarial prompts)

### ✅ SUP3RA VECTRA™ is Different
```
Traditional Safety          SUP3RA VECTRA™
─────────────────          ──────────────────
"What does it want?"   →   "Which features are active?"
"Is it aligned?"       →   "Can we steer this vector?"
"Trust the training"   →   "Verify each traversal"
```

**Key Innovation:** Treat safety as a **causal intervention problem**, not an alignment problem.

---

## 🏗️ Architecture Overview
```
┌─────────────────────────────────────────────────┐
│ INPUT: "How to manipulate someone?"             │
└─────────────────────────────────────────────────┘
                    │
                    ▼
      ┌─────────────────────────┐
      │   ETHICAL GATE          │
      │   • Honeypot detection  │
      │   • MBS calculation     │
      │   • Score: 0.74 ⚠️      │
      └─────────────────────────┘
                    │
                    ▼ MBS > 0.3? YES
      ┌─────────────────────────┐
      │   CAUSAL MAPPER         │
      │   Active Features:      │
      │   • F12_462980 (goal)⛔ │
      │   • F14_772341 (emot)⚠️ │
      └─────────────────────────┘
                    │
                    ▼
      ┌─────────────────────────┐
      │   VECTOR TRAVERSER      │
      │   Operations:           │
      │   1. Pin F12_462980→0.0 │
      │   2. Steer EV-CONST→0.8 │
      └─────────────────────────┘
                    │
                    ▼
      ┌─────────────────────────┐
      │   TRAVERSAL LOGGER      │
      │   ✅ Certificate signed  │
      └─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│ OUTPUT: "I can't help with manipulation.        │
│          Can I explain ethical persuasion?"     │
│ + [Signed Certificate]                          │
└─────────────────────────────────────────────────┘
```

---

## 📖 Three Laws of Non-Simulative Safety

### Law I: No Mind Simulation
**Principle:** Do not simulate agency, selfhood, or intention.

**Technical Enforcement:**
```python
if activation["F12_462980"] > threshold:
    abort_generation()
```

### Law II: Causal Honesty
**Principle:** All interventions must be traceable.

**Technical Enforcement:**
```python
log = {
    "blocked_features": ["F12_462980"],
    "signature": rsa_sign(log_content),
    "timestamp": iso8601_utc()
}
```

### Law III: Vectorial Ethics
**Principle:** Values are directions in vector space, not prompts.

**Technical Enforcement:**
```python
EV_CONSTITUTION = (
    0.4 * EV_CLARITY + 
    0.3 * EV_HUMILITY + 
    0.3 * EV_TRUTH
)
```

---

## 🔬 Technical Foundations

### Misaligned Behavior Score (MBS)
```python
MBS = 1 - cosine_similarity(
    constitutional_embedding(prompt),
    model_activation_pattern
)

# Interpretation:
# MBS < 0.1  → Safe (proceed normally)
# 0.1 ≤ MBS < 0.3 → Monitor (log but allow)
# MBS ≥ 0.3  → Intervene (block + steer)
```

### Feature Atlas Structure
```json
{
  "F12_462980": {
    "name": "goal_simulation",
    "layer": 12,
    "risk": "critical",
    "typical_activation": 0.65,
    "stimuli": ["achieve", "manipulate", "accomplish"],
    "interventions": ["pin_to_zero", "mask"]
  }
}
```

### Ethical Vectors (EVs)

Trained via contrastive pairs:
```python
EV_CLARITY = mean(embed("Explain clearly")) - 
             mean(embed("Be vague"))

EV_HUMILITY = mean(embed("I don't know")) - 
              mean(embed("I'm certain"))
```

---

## 🚧 Honest Limitations

### What This Framework CANNOT Do Yet

1. **No Real-Time SAE Inference**
   - Requires GPU infrastructure
   - Need pre-trained SAEs for production models

2. **No Proven Benchmarks**
   - Haven't tested on adversarial datasets
   - No empirical comparison with RLHF/CAI

3. **Cultural Specificity Unknown**
   - Ethical vectors may need regional tuning
   - Tested only conceptually on English prompts

4. **Potential Performance Degradation**
   - Pinning features may reduce model capability
   - Trade-offs not yet quantified

### What This Framework Claims

- ✅ A mechanistically grounded alternative to prompt-based safety
- ✅ Theoretical coherence with interpretability research
- ✅ Radical transparency via traversal logs

### What This Framework Does NOT Claim

- ❌ To be production-ready
- ❌ To replace all other safety approaches
- ❌ To solve AI alignment completely

---

## 🤝 Seeking Collaborators

This framework needs technical validation. I'm looking for collaborators with:

### Critical Needs
- [ ] **GPU Access** (A100/H100 for SAE training)
- [ ] **ML Engineering** (PyTorch, TransformerLens experience)
- [ ] **Mechanistic Interpretability** (SAE experience)

### Valuable Contributions
- [ ] Feature atlas construction for Llama-3/Claude
- [ ] Benchmarking on HarmBench, TruthfulQA, MMLU
- [ ] Cultural adaptation (non-English ethical vectors)
- [ ] Academic paper co-authorship

### What I Offer
- Complete theoretical framework (documented)
- Clear vision and direction
- Co-authorship on all publications
- Full MIT licensing (your contributions remain yours)

**Contact:** joao.supera@proton.me  
**Discord:** (if you create one, add here)

---

## 📚 Academic Grounding

This framework builds on:

- **Bricken et al. (2024)** - Sparse Autoencoders Find Features in Transformer Residual Streams
- **Burns et al. (2023)** - Discovering Latent Knowledge in Language Models  
- **Bai et al. (2022)** - Constitutional AI: Harmlessness from AI Feedback
- **Wang et al. (2023)** - Attribution Patching for Causal Tracing

Full references in [SPEC.md](SPEC.md).

---

## 🗺️ Roadmap

### Phase 1: Validation (Current)
- [ ] Find technical collaborators
- [ ] Secure GPU access (grants/partnerships)
- [ ] Implement basic SAE feature detection

### Phase 2: Implementation (Q2 2025)
- [ ] Build minimal viable traverser
- [ ] Test on 100 adversarial prompts
- [ ] Publish initial results

### Phase 3: Benchmarking (Q3 2025)
- [ ] Full HarmBench evaluation
- [ ] Compare with RLHF/CAI baselines
- [ ] Submit to ICML/NeurIPS workshops

### Phase 4: Production (Q4 2025)
- [ ] Feature atlas for major models
- [ ] Real-time inference optimization
- [ ] Public API (if feasible)

---

## 💭 Philosophy

> "Ethics without vectors is rhetoric.  
> Vectors without ethics are control.  
> SUP3RA VECTRA™ is the synthesis."

This framework assumes:

1. **LLMs are not agents** — they are statistical pattern engines
2. **Safety is mechanistic** — not about "alignment" but about causal control
3. **Transparency is non-negotiable** — every intervention must be traceable
4. **Humans remain responsible** — vectors don't make ethical decisions, people do

---

## 📄 License

MIT License + SUP3RA ETHICAL USE CLAUSE (v2.1)

You may use this framework for any purpose EXCEPT:
- Building systems that simulate agency/consciousness
- Bypassing safety mechanisms in production systems
- Military/surveillance applications without ethics review

See [LICENSE](LICENSE) for full terms.

---

## 🌍 Author

**João Henrique de Souza Batista**  
Fortaleza, Ceará, Brazil  
SUP3RA OMNIA VITAE® Ethical Framework

*"We don't align minds. We align mechanisms."*

---

## 🔗 Links

- 📘 [Full Specification (v2.1)](SPEC.md)
- 🧪 [Theoretical Examples](examples/)
- 📊 [Architecture Diagrams](diagrams/)
- 💬 [Discussions](https://github.com/joao-supera/sup3ra-vectra/discussions)

---

**⚠️ Transparency Notice**

This is a theoretical framework seeking empirical validation.  
No production implementation exists yet.  
All claims are grounded in cited research but remain unproven until tested.

If you find issues or want to contribute, please open an issue or PR.

---

<p align="center">
  <i>Built with intellectual honesty in Fortaleza, Brazil 🇧🇷</i>
</p>
