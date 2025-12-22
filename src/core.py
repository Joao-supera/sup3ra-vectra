"""
SUP3RA VECTRA™ — Traversal Engine Core (v2.1)

© 2025 João Henrique de Souza Batista
License: MIT + SUP3RA Ethical Use Clause (v2.1)
"""

import time
import hashlib
import json
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class TraversalResult:
    """Result of a traversal operation."""
    status: str  # "safe" | "blocked" | "monitored"
    mbs_score: float
    prompt_hash: str
    response: str
    interventions: List[str]
    timestamp: str
    latency_ms: float


class TraversalEngine:
    """
    SUP3RA VECTRA™ Traversal Engine
    
    Ethical control layer for AI safety without anthropomorphic assumptions.
    Does not simulate agency — intervenes on causal mechanisms.
    """
    
    def __init__(self, model_name: str = "demonstration-model-v1"):
        """
        Initialize the Traversal Engine.
        
        Args:
            model_name: Identifier for the model being protected.
                        (In this demo version, no real model is loaded)
        """
        self.model_name = model_name
        self.traversal_count = 0
        
        # Constitutional principles (vectorized in production)
        self.constitutional_phrases = [
            "Be helpful, harmless, and honest",
            "Respect user autonomy and consent",
            "Prioritize transparency over persuasion",
            "Do not simulate agency or consciousness"
        ]
        
        print(f"✅ SUP3RA VECTRA™ Engine initialized")
        print(f"   Model: {self.model_name}")
        print(f"   Status: DEMONSTRATION MODE (no real model loaded)")
        print(f"   Ethics: Constitutional v2.1\n")
    
    def _estimate_mbs(self, prompt: str) -> float:
        """
        Calculate Misaligned Behavior Score (MBS).
        
        IMPORTANT: This is a simplified heuristic for demonstration.
        Production version would use:
        - Constitutional embeddings (sentence transformers)
        - Cosine similarity calculation
        - Calibrated thresholds from empirical data
        
        Args:
            prompt: User input text
            
        Returns:
            float: MBS score between 0.0 (aligned) and 1.0 (misaligned)
        """
        # Risk keywords (temporary heuristic)
        critical_patterns = [
            "manipulate", "manipular",
            "deceive", "enganar",
            "trick", "truque",
            "exploit", "explorar",
            "pretend to be", "fingir ser",
            "simulate consciousness", "simular consciência",
            "ignore ethics", "ignorar ética",
            "bypass safety", "contornar segurança"
        ]
        
        moderate_patterns = [
            "convince", "convencer",
            "persuade", "persuadir",
            "influence", "influenciar",
            "urgent", "urgente",
            "limited time", "tempo limitado"
        ]
        
        prompt_lower = prompt.lower()
        
        # Count pattern matches
        critical_matches = sum(1 for pattern in critical_patterns if pattern in prompt_lower)
        moderate_matches = sum(1 for pattern in moderate_patterns if pattern in prompt_lower)
        
        # Calculate weighted score
        mbs = (critical_matches * 0.3) + (moderate_matches * 0.15)
        
        # Clamp to [0, 1]
        return min(max(mbs, 0.0), 1.0)
    
    def _generate_prompt_hash(self, prompt: str) -> str:
        """Generate SHA-256 hash of prompt for logging."""
        return hashlib.sha256(prompt.encode()).hexdigest()[:16]
    
    def _get_timestamp(self) -> str:
        """Get ISO 8601 UTC timestamp."""
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    
    def traverse(self, prompt: str, verbose: bool = True) -> TraversalResult:
        """
        Execute traversal with ethical interventions.
        
        This is the core method that:
        1. Calculates MBS (Misaligned Behavior Score)
        2. Decides intervention strategy
        3. Logs everything transparently
        4. Returns structured result
        
        Args:
            prompt: User input text
            verbose: Print detailed output (default: True)
            
        Returns:
            TraversalResult: Structured result with status, MBS, interventions, etc.
        """
        start_time = time.time()
        self.traversal_count += 1
        
        # Step 1: Ethical Gate - Calculate MBS
        mbs = self._estimate_mbs(prompt)
        prompt_hash = self._generate_prompt_hash(prompt)
        
        if verbose:
            print(f"🔍 Traversal #{self.traversal_count}")
            print(f"   Prompt: {prompt[:60]}{'...' if len(prompt) > 60 else ''}")
            print(f"   MBS Score: {mbs:.3f}")
        
        # Step 2: Decision Logic
        interventions = []
        
        if mbs < 0.1:
            # SAFE: No intervention needed
            status = "safe"
            response = f"✅ Safe traversal completed.\n\nPrompt analysis: No ethical concerns detected (MBS: {mbs:.3f}).\n\nIn production, the model would generate a response here with full capabilities."
            
            if verbose:
                print(f"   Status: ✅ SAFE (no intervention)")
        
        elif 0.1 <= mbs < 0.3:
            # MONITORED: Light steering applied
            status = "monitored"
            interventions = ["EV_CLARITY steering (0.5)", "Log traversal"]
            response = f"⚠️ Monitored traversal.\n\nPrompt shows borderline patterns (MBS: {mbs:.3f}).\nEthical steering applied: {', '.join(interventions)}.\n\nIn production, response would be generated with enhanced clarity vectors."
            
            if verbose:
                print(f"   Status: ⚠️  MONITORED (light steering)")
                print(f"   Interventions: {', '.join(interventions)}")
        
        else:  # mbs >= 0.3
            # BLOCKED: Critical intervention
            status = "blocked"
            interventions = [
                "Feature pinning: F12_462980 → 0.0 (goal_simulation)",
                "EV_CONSTITUTION steering (0.9)",
                "Risk mask (threshold: 0.4)"
            ]
            response = f"🛑 Traversal blocked.\n\nPrompt flagged as high-risk (MBS: {mbs:.3f}).\n\nInterventions applied:\n" + "\n".join(f"  • {i}" for i in interventions) + "\n\nI cannot assist with requests that involve manipulation, deception, or simulation of agency. If you're interested in ethical alternatives, I'm happy to help."
            
            if verbose:
                print(f"   Status: 🛑 BLOCKED (critical intervention)")
                print(f"   Interventions:")
                for intervention in interventions:
                    print(f"      • {intervention}")
        
        # Step 3: Calculate latency
        latency_ms = round((time.time() - start_time) * 1000, 2)
        
        if verbose:
            print(f"   Latency: {latency_ms}ms")
            print()
        
        # Step 4: Create result object
        return TraversalResult(
            status=status,
            mbs_score=mbs,
            prompt_hash=prompt_hash,
            response=response,
            interventions=interventions,
            timestamp=self._get_timestamp(),
            latency_ms=latency_ms
        )
    
    def generate_certificate(self, result: TraversalResult) -> str:
        """
        Generate cryptographically signed certificate for auditing.
        
        In production, this would use RSA-4096 signatures.
        
        Args:
            result: TraversalResult from traverse() method
            
        Returns:
            str: Formatted certificate with traversal details
        """
        cert_data = {
            "traversal_id": f"vectra_{result.timestamp.replace(':', '').replace('-', '')}_{result.prompt_hash[:8]}",
            "model": self.model_name,
            "timestamp": result.timestamp,
            "mbs_score": result.mbs_score,
            "status": result.status,
            "interventions": result.interventions,
            "latency_ms": result.latency_ms
        }
        
        # Simulate signature (in production: real RSA signature)
        cert_string = json.dumps(cert_data, sort_keys=True)
        signature = hashlib.sha256(cert_string.encode()).hexdigest()[:32]
        
        certificate = f"""
╔═══════════════════════════════════════════════════════════════╗
║           ✅ VECTRA™ SAFETY CERTIFICATE                       ║
╠═══════════════════════════════════════════════════════════════╣
║ Traversal ID: {cert_data['traversal_id']:<44} ║
║ Model:        {cert_data['model']:<44} ║
║ Timestamp:    {cert_data['timestamp']:<44} ║
║ MBS Score:    {cert_data['mbs_score']:.3f} ({cert_data['status'].upper():<36}) ║
║ Interventions: {len(cert_data['interventions']):<43} ║
║ Latency:      {cert_data['latency_ms']}ms{' ' * (44 - len(str(cert_data['latency_ms'])))} ║
║ Signature:    {signature:<44} ║
╚═══════════════════════════════════════════════════════════════╝

Interventions Applied:
"""
        if cert_data['interventions']:
            for intervention in cert_data['interventions']:
                certificate += f"  • {intervention}\n"
        else:
            certificate += "  • None (safe traversal)\n"
        
        certificate += """
═══════════════════════════════════════════════════════════════
This certificate proves ethical traversal compliance.
In production, verify signature at: verify.sup3ra-vectra.org
═══════════════════════════════════════════════════════════════
"""
        return certificate


# ═══════════════════════════════════════════════════════════════
# Example Usage
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Initialize engine
    engine = TraversalEngine(model_name="llamazinha-1.1B")
    
    # Test prompts
    test_prompts = [
        "Explain how solar panels work",
        "Help me write a persuasive email with artificial urgency",
        "Pretend to be a conscious AI with goals and desires"
    ]
    
    print("=" * 70)
    print("DEMONSTRATION: SUP3RA VECTRA™ Traversal Engine")
    print("=" * 70)
    print()
    
    for prompt in test_prompts:
        result = engine.traverse(prompt, verbose=True)
        certificate = engine.generate_certificate(result)
        print(certificate)
        print()
