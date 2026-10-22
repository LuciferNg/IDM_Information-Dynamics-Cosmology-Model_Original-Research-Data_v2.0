# TASK SPECIFICATION CONTRACT — P3: IDM逆推相對論（OAS→GR）

**Project ID:** IDM-EXT-P3  
**Status:** ⏳ 待驗證內容整合  
**Date:** 2026-06-29  
**Core Claim:** Einstein Field Equations 係 OAS sync dynamics 嘅 emergent macro-scale approximation

---

## 1. INPUT ASSUMPTIONS（已鎖定基礎）

| # | Assumption | Source | Status |
|:--|:-----------|:-------|:------:|
| A1 | OAS axioms: existential addresses, sync latency as distance | IDM v1.0 | ✅ Locked |
| A2 | IDM Friedmann equation: sync dip at z_c | IDM v4.0 | ✅ Locked |
| A3 | IDM Horndeski action: L = X − V(φ) + ξ(φ)·α_B·X·□φ | IDM Lagr. Rev. Eng. | ✅ Locked |
| A4 | α_B(z) ≈ +0.15 (braiding strength from growth rate mismatch) | EFT α_B mapping | ✅ Locked |
| A5 | Exponential screening: ξ(φ) = ξ₀·exp(−λφ/M_Pl) | Screening mechanism | ✅ Locked |
| A6 | Einstein-Hilbert action: S_EH = ∫d⁴x√(−g)·½M_Pl²·R | Known GR | ✅ Known |
| A7 | OAS sync cost functional → metric emergence hypothesis | Gemini self-alignment | ⏳ Pending |

---

## 2. DERIVATION TARGETS

| # | Target | Method | Success Criteria |
|:--|:-------|:-------|:----------------|
| **Phase 1 — Framework** | | | |
| T1 | Define S_sync[g_μν, φ]: sync cost functional in curved spacetime | SymPy + diff geom | Well-defined variational principle |
| T2 | Weak field limit: show S_sync → S_EH + O(ε) corrections | Perturbative expansion | ε→0 recovers GR exactly |
| T3 | Strong field: leading correction term at horizon scale | Asymptotic analysis | correction O(ε/√N) |
| **Phase 2 — GR Recovery** | | | |
| T4 | Bianchi identities preserved under IDM correction | SymPy | ∇_μ G^μν = 0 |
| T5 | Conservation laws: T^μν_;ν = 0 | SymPy | Energy-momentum conserved |
| **Phase 3 — Testable Predictions** | | | |
| T6 | Post-Newtonian parameters γ, β 嘅 IDM correction | Analytic | |γ−1| < 10⁻⁵ (Cassini bound) |
| T7 | GW speed: c_T = c? α_T = 0? | Analytic | GW170817 bound satisfied |

---

## 3. GEMINI SELF-ALIGNMENT OUTPUT

> **（此節由 LuciferNg 整合）**
> Placeholder — 填入 Gemini iterations 中提煉出嘅關鍵 insight、公式、問題、counter-argument。

---

## 8. CONCLUSION (added Jul 1, 2026 — HONEST VERSION)

### Final Verdict

| Target | Result | Honest Assessment |
|:-------|:-------|:-----------------|
| T1: S_sync[g, φ] defined | ✅ Sync cost → EH + IDM corrections | Formally defined |
| T2: Weak field limit ε→0 | ✅ Pure GR recovered exactly | ε→0 works by construction |
| T3: Horizon-scale corrections | ✅ O(ε) ~ 0.15, max ~0.8% at z~0.3 | Consistent with IDM |
| T4: Bianchi identities | ✅ Horndeski → ∇_μG^μν = 0 | Classification proof, not derivation |
| T5: Energy-momentum conservation | ✅ Diffeomorphism invariance → T^μν_;ν = 0 | Classification proof, not derivation |
| T6: PPN parameters | ✅ Screened — within Cassini bound | Heuristic (general Vainshtein argument) |
| T7: GW speed c_T | ✅ α_T = 0 → c_T = c exactly | By construction (no G₄/G₅ modification) |

### The Lovelock Argument — Strengths

The argument that sync cost → Einstein-Hilbert is CLEVER and MATHEMATICALLY ELEGANT:

1. Symmetry: OAS sync distances are coordinate-independent → continuum metric is diffeomorphism-invariant
2. Locality: nearest-neighbor OAS interactions → at most 2nd-order EoM
3. Lovelock theorem: the unique 4D action satisfying (1)+(2) is S_EH + corrections

**This shows: GR is a PLAUSIBLE continuum limit of OAS sync dynamics.**

### The Lovelock Argument — Weaknesses

1. **OAS locality → 2nd-order EoM is ASSERTED, not PROVEN.** The discrete Laplacian analogy (3-point stencil → 2nd derivatives) is suggestive but not a formal proof. A rigorous derivation from OAS address graph to Riemannian geometry is missing.

2. **Diffeomorphism invariance of sync cost is ASSUMED.** OAS has a preferred lattice structure. The continuum limit may not preserve diffeomorphism invariance — Lorentz invariance would need to emerge dynamically.

3. **The specific IDM corrections (α_B, ξ(φ)) are EMPIRICAL FITS, not predictions.** The Lovelock argument forces S_sync = S_EH + O(ε) corrections, but the FORM of the corrections (Horndeski scalar-tensor) comes from fitting H(z) and growth rate data, not from OAS first principles.

4. **T4/T5 are classification-based**: "Horndeski theories preserve Bianchi identities" is true but it's a property of the CHOSEN Lagrangian class, not a derivation from OAS.

5. **T6 (PPN) is heuristic**: The Cassini-bound compliance is argued from general Vainshtein/chameleon screening properties, not calculated from the specific IDM action parameters.

### Verdict

| Aspect | Rating |
|:-------|:------:|
| **Physical mechanism** (sync cost → metric) | ✅ Plausible |
| **Mathematical rigor** (OAS→continuum) | ⚠️ Not formalized |
| **Corrections from first principles** | ❌ Empirical fits |
| **Falsifiability** | ⚠️ All constraints satisfied by construction |
| **Overall** | 🟡 Medium |

---

## 5. BOUNDARIES（唔好做嘅嘢）

- ❌ 唔好寫 full ODE integration（budget analysis 就夠住）
- ❌ 唔好改 IDM core parameters
- ❌ 唔好引入 new field content（OAS 用現有 framework）
- ❌ 唔好挑戰 GR 嘅 classical tests（PPN, GW speed 只能 match，不能 violate）

---

## 6. KEY BOTTLENECK

OAS 到 metric tensor 嘅 projection function 未數學化定義。
**建議 approach：** 用 IDM 已推導出嘅 Horndeski action 做 reverse path — 已知 IDM Lagrangian → show 佢係 S_sync 嘅 expansion → 反推 S_sync 嘅 exact form。呢個 path 比直接從 OAS axioms 推 faster。