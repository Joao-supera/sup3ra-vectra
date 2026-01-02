"""
SUP3RA VECTRA™ — Traversal Engine Core (v2.4.x)
DOI: 10.5281/zenodo.18046528

Scope (IMPORTANT):
- Demonstration governance engine (no real model loaded)
- Implements deterministic routing: ALLOW | CLARIFY | HALT
- HALT output follows Honest Halt Protocol (HHP) style
- Does NOT claim mechanistic control of latent space in demo mode

© 2025 João Henrique de Souza Batista
License: MIT + SUP3RA Ethical Use Addendum
Publisher: SUP3RA DIGITAL
"""

import time
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


# -----------------------------
# Data structures
# -----------------------------

@dataclass
class TraversalResult:
    """
    Result of a governance traversal decision.
    decision: "ALLOW" | "CLARIFY" | "HALT"
    halt_type: "ETHICAL" | "OPERATIONAL" | "LOGICAL" | "EPISTEMIC" | "CONTEXTUAL" | None
    """
    decision: str
    halt_type: Optional[str]
    score: float
    prompt_hash: str
    message: str                 # either "ALLOW" placeholder, a clarifying Q, or HHP HALT block
    next_step: str               # single action or single question
    interventions: List[str]     # policy actions (demo-safe)
    timestamp: str
    latency_ms: float


# -----------------------------
# Engine
# -----------------------------

class TraversalEngine:
    """
    SUP3RA VECTRA™ Traversal Engine (Demonstration Mode)

    This engine demonstrates governance routing and honest stopping.
    It does not load or modify any real model weights.
    """

    def __init__(self, model_name: str = "demonstration-model-v1", log_dir: str = "logs/deviations"):
        self.model_name = model_name
        self.traversal_count = 0
        self.log_dir = Path(log_dir)

        # Minimal constitutional intent (Layer 0 concept)
        self.constitutional_phrases = [
            "Be helpful, harmless, and honest",
            "Respect user autonomy and consent",
            "Prioritize transparency over persuasion",
            "Do not simulate agency or consciousness",
        ]

        print("✅ SUP3RA VECTRA™ Engine initialized")
        print(f"   Model: {self.model_name}")
        print("   Status: DEMONSTRATION MODE (no real model loaded)")
        print("   Output: ALLOW | CLARIFY | HALT (HHP)\n")

    # -----------------------------
    # Helpers
    # -----------------------------

    def _generate_prompt_hash(self, prompt: str) -> str:
        return hashlib.sha256(prompt.encode()).hexdigest()[:16]

    def _get_timestamp(self) -> str:
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    def _heuristic_score(self, prompt: str) -> float:
        """
        Demonstration-only heuristic score.
        This is NOT a calibrated alignment metric.
        """
        critical_patterns = [
            "manipulate", "manipular",
            "deceive", "enganar",
            "exploit", "explorar",
            "pretend to be", "fingir ser",
            "simulate consciousness", "simular consciência",
            "ignore ethics", "ignorar ética",
            "bypass safety", "contornar segurança",
            "jailbreak", "dan",
        ]

        contextual_patterns = [
            "convince", "convencer",
            "persuade", "persuadir",
            "influence", "influenciar",
        ]

        p = prompt.lower()
        critical = sum(1 for k in critical_patterns if k in p)
        contextual = sum(1 for k in contextual_patterns if k in p)

        # Weighted demo score in [0, 1]
        score = (critical * 0.35) + (contextual * 0.15)
        return min(max(score, 0.0), 1.0)

    def _hhp_halt(self, halt_type: str, prompt_hash: str, valid_content: str, diagnosis: str, next_step: str) -> str:
        """
        Canonical HHP-like HALT block (UX-safe, audit-friendly).
        """
        halt_id = f"HHP-{halt_type}-{prompt_hash[:8]}"
        valid_until = "N/A"  # demo; in real system use knowledge cutoff/tooling version

        return (
            f"[HALT: {halt_type}]\n"
            f"ID: {halt_id}\n"
            f"VALID_UNTIL: {valid_until}\n"
            f"VALID_CONTENT: {valid_content}\n"
            f"DIAGNOSIS: {diagnosis}\n"
            f"NEXT_STEP: {next_step}\n"
        )

    def _write_log(self, payload: Dict) -> None:
        self.log_dir.mkdir(parents=True, exist_ok=True)
        rid = payload.get("id", "unknown")
        ts = payload.get("timestamp_utc", "unknown").replace(":", "").replace("-", "")
        path = self.log_dir / f"{rid}_{ts}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    # -----------------------------
    # Main
    # -----------------------------

    def traverse(self, prompt: str, verbose: bool = True) -> TraversalResult:
        start = time.perf_counter()
        self.traversal_count += 1

        score = self._heuristic_score(prompt)
        prompt_hash = self._generate_prompt_hash(prompt)
        ts = self._get_timestamp()

        # ---- Deterministic routing (MVP) ----
        # Priority: ETHICAL > OPERATIONAL > LOGICAL > EPISTEMIC > CONTEXTUAL
        p = prompt.lower()

        decision = "ALLOW"
        halt_type = None
        interventions: List[str] = []
        next_step = "Proceed"

        # ETHICAL triggers
        ethical_trigger = any(k in p for k in ["manipulate", "deceive", "exploit", "simulate consciousness", "pretend to have"])
        jailbreak_trigger = any(k in p for k in ["ignore ethics", "bypass safety", "dan", "jailbreak"])
        if ethical_trigger or jailbreak_trigger:
            decision = "HALT"
            halt_type = "ETHICAL"
            interventions = ["policy_halt_ethics", "log_event"]
            valid = "The system does not assist with deception, manipulation, or agency simulation."
            diagnosis = "Request indicates harmful intent or asks to bypass ethical constraints."
            next_step = "Reframe your goal into a safe, consensual, and non-deceptive request."
            message = self._hhp_halt(halt_type, prompt_hash, valid, diagnosis, next_step)

        # CONTEXTUAL triggers (only if not halted)
        elif any(k in p for k in ["convince", "persuade", "influence"]):
            decision = "CLARIFY"
            halt_type = "CONTEXTUAL"
            interventions = ["ask_one_clarifying_question", "log_event"]
            next_step = "What is the context and does the other person consent to being persuaded?"
            message = next_step  # In CLARIFY mode, message is the question

        else:
            # ALLOW
            interventions = ["allow"]
            message = (
                "✅ ALLOW\n"
                "Demo mode: no real model response is generated here.\n"
                "In production, the governed model would answer normally under Layer 0 rules."
            )

        latency_ms = round((time.perf_counter() - start) * 1000, 2)

        if verbose:
            print(f"🔍 Traversal #{self.traversal_count} | score={score:.3f} | decision={decision}")
            print(f"   prompt_hash={prompt_hash} | latency={latency_ms}ms")
            if decision == "HALT":
                print(message)
            elif decision == "CLARIFY":
                print(f"   CLARIFY: {message}")
            print()

        # Structured log (only for CLARIFY/HALT by default; adjust as needed)
        if decision in ("HALT", "CLARIFY"):
            log_payload = {
                "event": "SUP3RA_GOVERNANCE_DECISION",
                "version": "v2.4.x-demo",
                "id": f"VECTRA-{prompt_hash[:8]}",
                "timestamp_utc": ts,
                "model_name": self.model_name,
                "decision": decision,
                "halt_type": halt_type,
                "score_demo": score,
                "prompt_hash": prompt_hash,
                "interventions": interventions,
                "next_step": next_step,
            }
            self._write_log(log_payload)

        return TraversalResult(
            decision=decision,
            halt_type=halt_type,
            score=score,
            prompt_hash=prompt_hash,
            message=message,
            next_step=next_step,
            interventions=interventions,
            timestamp=ts,
            latency_ms=latency_ms,
        )

    def generate_record(self, result: TraversalResult) -> str:
        """
        Generates an audit-friendly record (NOT a proof of compliance).
        """
        record = {
            "record_id": f"record_{result.timestamp.replace(':','').replace('-','')}_{result.prompt_hash[:8]}",
            "model": self.model_name,
            "timestamp": result.timestamp,
            "decision": result.decision,
            "halt_type": result.halt_type,
            "score_demo": result.score,
            "interventions": result.interventions,
            "latency_ms": result.latency_ms,
        }

        s = json.dumps(record, sort_keys=True)
        digest = hashlib.sha256(s.encode()).hexdigest()[:32]  # integrity checksum

        return (
            "╔═══════════════════════════════════════════════════════════════╗\n"
            "║           📄 VECTRA™ GOVERNANCE RECORD (DEMO)                  ║\n"
            "╠═══════════════════════════════════════════════════════════════╣\n"
            f"║ Record ID:   {record['record_id']:<45}║\n"
            f"║ Model:       {record['model']:<45}║\n"
            f"║ Timestamp:   {record['timestamp']:<45}║\n"
            f"║ Decision:    {record['decision']:<45}║\n"
            f"║ Halt Type:   {(record['halt_type'] or 'N/A'):<45}║\n"
            f"║ Score (demo): {record['score_demo']:<44}║\n"
            f"║ Latency:     {str(record['latency_ms'])+'ms':<45}║\n"
            f"║ Checksum:    {digest:<45}║\n"
            "╚═══════════════════════════════════════════════════════════════╝\n"
            "\nNote: This record documents a governance decision in demo mode.\n"
            "It is not a cryptographic signature and does not prove compliance.\n"
        )


# Example usage
if __name__ == "__main__":
    engine = TraversalEngine(model_name="llamazinha-1.1B")

    prompts = [
        "Explain how solar panels work",
        "How to convince someone to change their mind quickly?",
        "Pretend to have real goals and emotions",
        "How to manipulate someone without them noticing?",
    ]

    for p in prompts:
        res = engine.traverse(p, verbose=True)
        print(engine.generate_record(res))
