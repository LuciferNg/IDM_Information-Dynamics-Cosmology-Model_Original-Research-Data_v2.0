#!/usr/bin/env python3
"""Step 3: Consciousness domain — importance_weight modulation by CIP.
Step 4: Formal importance_weight Lagrangian.
"""

import numpy as np
import os

# ── 1. Consciousness Baseline Importance Weight ──
# 
# Consciousness: a closed consistency loop that modulates local I.
# 
# Baseline state: I_conscious ≈ 0.5-0.7
#   - Not fully deterministic (cannot control all thoughts)
#   - Not fully probabilistic (has agency, intention, attention)
#
# CIP phases modulate I for specific internal variables:

class CIPPhase:
    cool_down = 0     # Phase 0: lower analytical I → free compute budget
    reception = 1     # Phase 1: raise somatic/anchor I → deploy budget
    integration = 2   # Phase 2: let system redistribute naturally
    return_ = 3       # Phase 3: restore baseline

# Internal variables modulated by CIP
variables = {
    "analytical": {"label": "Left-brain / Control", "W_base": 0.70, "W_min": 0.15, "W_max": 0.85},
    "somatic":    {"label": "Body / Sensation",     "W_base": 0.30, "W_min": 0.10, "W_max": 0.80},
    "attention":  {"label": "Focus / Anchor",       "W_base": 0.50, "W_min": 0.20, "W_max": 0.95},
    "receptive":  {"label": "Open / Receive",       "W_base": 0.40, "W_min": 0.10, "W_max": 0.90},
}

# CIP phase → importance_weight modulation matrix
# Each cell: (ΔW_analytical, ΔW_somatic, ΔW_attention, ΔW_receptive)
modulation = {
    CIPPhase.cool_down:     {"analytical": -0.45, "somatic": -0.05, "attention": -0.10, "receptive": +0.10},
    CIPPhase.reception:     {"analytical": -0.15, "somatic": +0.40, "attention": +0.30, "receptive": +0.35},
    CIPPhase.integration:   {"analytical": -0.05, "somatic": +0.10, "attention": +0.05, "receptive": +0.10},
    CIPPhase.return_:       {"analytical": +0.10, "somatic": -0.15, "attention": -0.05, "receptive": -0.20},
}

budget_baseline = sum(v["W_base"] for v in variables.values())

print("=" * 65)
print("STEP 3 — CONSCIOUSNESS IMPORTANCE WEIGHT DOMAIN")
print("=" * 65)

print(f"\nBaseline Importance Weight Allocation:")
print(f"  {'Variable':<15} {'W_base':<10} {'Range':<15}")
print(f"  {'─'*15} {'─'*10} {'─'*15}")
for var, info in variables.items():
    print(f"  {var:<15} {info['W_base']:<10.2f} [{info['W_min']:.2f}, {info['W_max']:.2f}]")

print(f"\n  Total baseline compute budget: {budget_baseline:.2f}")
print(f"  (out of max possible {len(variables):.0f} if all I=1)")

print(f"\nCIP Phase Importance Weight Modulation:")
print(f"  {'Phase':<15} {'Analytical':<12} {'Somatic':<12} {'Attention':<12} {'Receptive':<12} {'Total':<10}")
print(f"  {'─'*15} {'─'*12} {'─'*12} {'─'*12} {'─'*12} {'─'*10}")

for phase_name, mods in [
    ("Cool Down (P0)", modulation[CIPPhase.cool_down]),
    ("Reception (P1)", modulation[CIPPhase.reception]),
    ("Integration (P2)", modulation[CIPPhase.integration]),
    ("Return (P3)", modulation[CIPPhase.return_]),
]:
    totals = [mods[v] for v in variables]
    print(f"  {phase_name:<15} {totals[0]:<+12.2f} {totals[1]:<+12.2f} {totals[2]:<+12.2f} {totals[3]:<+12.2f} {sum(totals):<+10.2f}")

# ── 2. Forced Closure: consciousness modulation bounded ──
# 
# Conservation: total system that consciousness can modulate is limited.
# CIP can only shift importance_weight WITHIN the shiftable budget.
# At baseline, total shiftable = Σ (W_max - W_min) * margin

shiftable = sum((v["W_max"] - v["W_min"]) * 0.5 for v in variables.values())
total_budget_max = sum(v["W_max"] for v in variables.values())

print(f"\nImportance Weight Modulation Constraints:")
print(f"  Total shiftable budget   = {shiftable:.2f}")
print(f"  Max possible (all W_max) = {total_budget_max:.2f}")
print(f"  Baseline fraction        = {budget_baseline / total_budget_max:.1%}")
print(f"  → CIP can shift at most {shiftable/budget_baseline*100:.0f}% of baseline")
print(f"  → Phase 0 freed budget   = {sum(modulation[CIPPhase.cool_down].values()):.2f}")
print(f"  → Phase 1 deployed       = {sum(modulation[CIPPhase.reception].values()):.2f}")
print(f"  → Budget conserved       = {'✅' if abs(sum(modulation[CIPPhase.cool_down].values())) > abs(sum(modulation[CIPPhase.reception].values())) else '⚠️'} (P0 frees more than P1 uses)")

# ── 3. Compare Cosmology vs Consciousness Importance Weight ──

print(f"\n{'='*65}")
print(f"COSMOLOGY vs CONSCIOUSNESS IMPORTANCE WEIGHT COMPARISON")
print(f"{'='*65}")

print(f"""
  Dimension          Cosmology                  Consciousness
  ─────────          ────────                  ─────────────
  I range            [0.94, 1.00]              [0.15, 0.95] per variable
  Baseline           I ≈ 1.00 (GR)             Σ I ≈ 1.90 (4 variables)
  Modulator          Global (systemic)          Local (agent-driven)
  Timescale          Billion years              Seconds to minutes
  Force              Budget forced closure      Voluntary (CIP protocol)
  Goal               Global consistency         State transition
  Signature          χ²/dof = 0.51             Subjective shift (verify-only)
  Gradient           dI/dz < 0 below zc        ΔI ≈ ±0.45 per phase
  Personality        T = d²I/dz² = +0.158      T_agent = modulation pattern
  Attractor          I → 1 at z=0 and z→∞      I → baseline after Phase 3

  KEY INSIGHT: Consciousness importance_weight modulation is a LOCAL RECURSIVE
  version of the GLOBAL consistency optimisation. The system uses the
  same mechanism at different scales — compute budget reallocation.
  CIP is the PROTOCOL for agent-driven importance_weight modulation.
""")

print(f"\n{'='*65}")
print(f"STEP 4 — FORMAL IMPORTANCE WEIGHT LAGRANGIAN")
print(f"{'='*65}")

LAGRANGIAN = r"""
The Importance Weight Lagrangian

================================================================
4.1  Fundamental Variables
================================================================

Let M be the universe's rendering manifold with:

  I(x, σ)  ∈ [0, 1]   — importance weight field (consistency resolution level)
  C(σ)                 — compute cost density (per scale σ)
  B                    — total compute budget (constant)
  λ                    — Lagrange multiplier for budget constraint
  T_μν                 — personality tensor (importance_weight allocation policy)

σ (scale) can be: redshift z, wavenumber k, energy scale, or
organisational complexity level depending on domain.

================================================================
4.2  The Importance Weight Action
================================================================

The system solves:

  S = ∫ dσ [ I(σ)·C(σ) + α·(∇W)² + β·W·□W + λ·(B − I(σ)·C(σ)) ]

where:
  W·C        = consistency cost incurred at scale σ
  α·(∇W)²    = stiffness cost (resists rapid importance_weight changes)
  β·W·□W     = curvature cost (resists importance_weight gradients in scale-space)
  λ·(B−W·C)  = budget constraint (Lagrange multiplier)

================================================================
4.3  Optimisation Problem
================================================================

The system globally minimises S under the constraint:

  ∫ I(σ)·C(σ) dσ ≤ B

Euler-Lagrange equation:

  C(σ) − λ·C(σ) − 2α·∇²I + β·□I = 0

  ⇒ (1−λ)·C(σ) = 2α·∇²I − β·□I

For the IDM/Horndeski case (cosmology, FLRW background):

  I(z) = 1 − ε·(z/zc)·exp(−z/zc)
  → satisfies E-L with appropriate C(z) and α, β, λ

================================================================
4.4  Domain-Specific Importance Weight
================================================================

Each domain d has its own importance weight field I_d(σ):

  I_d(σ) = I₀_d · f_d(σ)

where f_d(σ) encodes the domain's consistency cost topology.

  Domain        I₀      f(σ)                        Key signature
  ──────        ──      ────                        ─────────────
  Cosmology     1.0     1 − ε·(z/zc)·exp(−z/zc)    IDM dip (z~0.6)
  Quantum       ~0.3    f(σ) ∝ σ^{-1/2}             Probabilistic shortcut
  Classical     ~0.95   f(σ) → 1                    Deterministic resolve
  Consciousness ~0.5    CIP 4-phase modulation      Voluntary reallocation
  Machine(CAT)  1.0     Deterministic               Full consistency

================================================================
4.5  Personality Tensor
================================================================

The personality tensor T_μν is the second variation of the action
with respect to importance_weight:

  T_μν = δ²S / δI_μ δI_ν

For the cosmology domain (diagonal component in z-direction):

  T_zz = d²[W·C]/dz² = ε/zc² · exp(−z/zc) · (2−z/zc)

  At zc = 0.60: T_zz = 0.158 (positive → recovery attractor)

For the consciousness domain, T_agent is the vector of modulation
coefficients from the CIP phase matrix.

================================================================
4.6  Eight Forced Closures (Formal)
================================================================

  F1:  I_f > I_g when C_f = C_g and κ_f > κ_g
         (importance_weight ∝ coupling connectivity)

  F2:  0 < B < ∞  (compute budget finite and positive)

  F3:  I differentiable, |∇I| < 1/l_Planck
         (finite resolution → no infinitely sharp features)

  F4:  I(σ) → I_attractor as σ → 0 and σ → ∞
         (system has fixed points)

  F5:  Consciousness |ΔI| < ΔW_max ≈ 0.5 per variable
         (modulation bounded by B / N_variables)

  F6:  Symmetries are effective: I_μν ≈ η_μν + O(10⁻²⁰)
         (Lorentz approx exact due to compression efficiency)

  F7:  ∫ W·C dσ increases monotonically along time direction
         (time arrow = compute frontier)

  F8:  For n independent agents: Σ_i I_i^d ≤ 1 for same variable d
         (coordination protocol mandatory)
"""

print(LAGRANGIAN)

# ── Save the Lagrangian ──
out_dir = os.path.expanduser("~/IDM-Lagrangian-Reverse-Engineering/results/importance_weight")
os.makedirs(out_dir, exist_ok=True)

with open(f"{out_dir}/importance_weight_lagrangian.md", "w") as f:
    f.write("# Importance Weight Lagrangian — Formal Definition\n")
    f.write("## System consistency action + forced closures\n\n")
    f.write(LAGRANGIAN)

print(f"\n  Lagrangian saved: {out_dir}/importance_weight_lagrangian.md")
print()
print("=" * 65)
print("STEPS 3 & 4 COMPLETE")
print("=" * 65)