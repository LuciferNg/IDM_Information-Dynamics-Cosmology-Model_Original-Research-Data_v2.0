# Paper 1: IDM + CLASS + Horndeski — Cosmological Evidence for Forced Consistency

**Status:** ⏳ Draft outline (P0 closure complete, P2 pending)
**Target:** arXiv submission after P0 closure verification

---

## Outline

### Abstract (150 words)

We present evidence for a sync dip at z ≈ 0.6 in the cosmological expansion history, detected through a modified dark energy density f(z) = 1 − ε·(z/zc)·exp(−z/zc) with ε = 0.1545 ± 0.0032, zc = 0.60 ± 0.03. The dip improves the fit to combined cosmological data (Planck + Pantheon + BAO) by Δχ² = −50.8 relative to ΛCDM, producing χ²/dof = 0.51. We show this dip is not an anomaly but a signal of forced consistency: the system's finite compute budget forces a temporary importance weight deficit. The dip maps onto a Horndeski braiding parameter α_B ≈ +0.15 through the W-gradient relation α_B = −η·dW/dz. The V(φ) reconstruction reveals phantom crossing below z = 0.59, confirming modified gravity. We present the forced closure proof and identify a testable prediction: damped oscillation with secondary phantom crossing at z ∼ 2.0.

### 1. Introduction
- The ΛCDM success and its cracks
- Sync dip anomaly: CLASS χ²/dof = 0.51
- Why "too good a fit" is the signal
- Structure of this paper

### 2. Data & Methodology
- Datasets: Planck 2018 TT+TE+EE+lowE, Pantheon, BAO (BOSS+eBOSS)
- CLASS modifications: IDM implementation
- Sync dip: f(z) = 1 − ε·(z/zc)·exp(−z/zc)
- MCMC: ε, zc free; Ω_m, H₀ fitted simultaneously

### 3. Results
- Best-fit parameters: Table
- Δχ² = −50.8 vs ΛCDM
- χ²/dof = 0.51 — anomalously good
- W-mapping: W(z) = 1 − ε·(z/zc)·exp(−z/zc)
  - W(0) = 0.9975, W(zc) = 0.9432
  - Deficit = 5.68%
  - T_zz(zc) = +0.158 (recovery attractor)

### 4. V(φ) Reconstruction
- Method: H(z) → V(φ) via background reconstruction
- Phantom crossing at z < 0.59
- φ'² < 0 → GR+canonical scalar ruled out
- Modified gravity is forced by the data

### 5. EFT Mapping: α_B(z)
- α_B(z) from growth ratio f_IDM / f_ΛCDM
- α_B ≈ +0.14–0.16 at z=0
- α_B = −η·dW/dz, η = 0.58
- α_K(z) = 1 + η·λ(z) (nonlinear constraint)
- Consistency with GW170817 (α_T = 0)

### 6. Forced Closure
- Numerical fixed-point proof
- Budget conservation: B = ∫ W·C dz
- Perturbation stability (6/6 tests passed)
- κ = (2α − β − 2η·λ)/(1 − λ) stability with λ(z)

### 7. Prediction: Damped Oscillation
- Propagation delay: τ_delay ∼ t_Pl · 𝒩_DOF
- Secondary phantom crossing at z ∼ 2.0
- w_de(z) signature: brief w < −1
- Testable with DESI 5-yr / Euclid

### 8. Discussion
- Interpretation: universe as consistency-constrained system
- Not fine-tuning — forced closure
- Relation to other modified gravity approaches
- Limits and open questions

### 9. Conclusion

---

**Excluded:** Consciousness, personality, CIP, warp drive — reserved for Paper 2.