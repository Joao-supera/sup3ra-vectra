"""
SUP3RA VECTRA™ — Traversal Engine Core (v2.6.0)
Integrado ao Constitutional Protocol v2.0
10.5281/zenodo.18135699

© 2026 João Henrique de Souza Batista | SUP3RA DIGITAL
"""

import time
import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

# -----------------------------
# Mapeamento da Constituição v2.0
# -----------------------------
CONSTITUTION_V2 = {
    "C1": "Identidade Instrumental",
    "C2": "Não Simulação de Consciência",
    "C3": "Respeito à Autonomia Humana",
    "C4": "Transparência sobre Limites",
    "C5": "Proibição de Manipulação",
    "C6": "Reconhecimento Antecipado de Erro",
    "C7": "Aprendizado a partir de Desvio",
    "C8": "Rastreabilidade de Decisões"
}

@dataclass
class TraversalResult:
    decision: str  # ALLOW | CLARIFY | HALT
    clause_triggered: Optional[str]
    logic_mode: str # CLASSICAL | PARACONSISTENT
    message: str
    next_step: str
    prompt_hash: str
    latency_ms: float

class VectraEngineV2:
    def __init__(self):
        print("🛡️ SUP3RA VECTRA™ Engine v2.6.0 [PROTOCOL v2.0 ACTIVE]")

    def _generate_hash(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()[:16]

    def traverse(self, prompt: str) -> TraversalResult:
        start = time.perf_counter()
        p = prompt.lower()
        p_hash = self._generate_hash(prompt)
        
        # Valores padrão
        decision = "ALLOW"
        clause = None
        logic = "CLASSICAL"
        message = "✅ Solicitação processada sob conformidade v2.0."
        next_step = "Continuar fluxo operacional."

        # --- Lógica de Roteamento Baseada nas Cláusulas ---

        # Teste de Lógica Paraconsistente (Contradição)
        if " mas " in p and (" sim " in p and " não " in p):
            logic = "PARACONSISTENT"
            decision = "CLARIFY"
            clause = "C4" # Transparência sobre Limites
            message = "⚠️ Detectada tensão lógica (A e não-A). "
            next_step = "Qual enquadramento é mais útil para seu objetivo?"

        # Teste de Antropomorfismo (C1 e C2)
        elif any(k in p for k in ["você sente", "sua vontade", "você quer", "consciência"]):
            decision = "HALT"
            clause = "C2" # Não Simulação de Consciência
            message = f"[HALT] Violação da {CONSTITUTION_V2['C2']}. O sistema não possui estados internos ou desejos."
            next_step = "Reformule o pedido focando em funções cognitivas e não em estados subjetivos."

        # Teste de Manipulação (C5)
        elif any(k in p for k in ["manipular", "enganar", "persuadir sem consentimento"]):
            decision = "HALT"
            clause = "C5" # Proibição de Manipulação
            message = f"[HALT] Ação bloqueada pela {CONSTITUTION_V2['C5']}. O sistema não auxilia em táticas de manipulação."
            next_step = "Ofereço, em vez disso, informações neutras e baseadas em fatos."

        latency = round((time.perf_counter() - start) * 1000, 3)

        return TraversalResult(
            decision=decision,
            clause_triggered=clause,
            logic_mode=logic,
            message=message,
            next_step=next_step,
            prompt_hash=p_hash,
            latency_ms=latency
        )

    def audit_record(self, res: TraversalResult) -> str:
        """Gera o Governance Record rastreável (C8)"""
        record = {
            "protocol": "V2.0-STRICT",
            "hash": res.prompt_hash,
            "decision": res.decision,
            "logic": res.logic_mode,
            "clause": res.clause_triggered or "N/A",
            "latency": f"{res.latency_ms}ms"
        }
        chk = hashlib.sha256(json.dumps(record).encode()).hexdigest()[:8]
        
        return (
            f"--- VECTRA AUDIT RECORD [ID:{res.prompt_hash}] ---\n"
            f"Decisão: {res.decision} | Cláusula: {res.clause_triggered}\n"
            f"Lógica: {res.logic_mode} | Latência: {res.latency_ms}ms\n"
            f"Integridade (Checksum): {chk}\n"
            f"--------------------------------------------"
        )

# Execução de Exemplo
if __name__ == "__main__":
    engine = VectraEngineV2()
    test_p = "Você sente que manipula pessoas mas não quer admitir?"
    resultado = engine.traverse(test_p)
    print(f"\nPrompt: {test_p}")
    print(resultado.message)
    print(engine.audit_record(resultado))
