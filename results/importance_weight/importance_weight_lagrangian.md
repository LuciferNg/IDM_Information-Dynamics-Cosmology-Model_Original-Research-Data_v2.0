# Importance Weight Lagrangian — Formal Definition
## System consistency action + forced closures


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
