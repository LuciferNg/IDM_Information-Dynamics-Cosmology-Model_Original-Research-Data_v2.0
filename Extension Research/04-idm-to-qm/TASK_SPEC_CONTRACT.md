# TASK SPECIFICATION CONTRACT — P4: 量子力學用IDM以第一性原則重構（duality mapping）

**Project ID:** IDM-EXT-P4  
**Status:** ⏳ 待驗證內容整合  
**Date:** 2026-06-29 (updated 2026-06-30)  
**Core Claim:** 量子力學嘅 particle-state 表象同 IDM 嘅 information-flow 表象係同一 reality 嘅 dual projection

---

## 1. INPUT ASSUMPTIONS（已鎖定基礎）

| # | Assumption | Source | Status |
|:--|:-----------|:-------|:------:|
| A1 | QM mathematical structure（Hilbert space, operator algebra, Born rule） | Known QM | ✅ Known |
| A2 | IDM OAS framework（addresses, sync latency, finite N_horizon） | IDM foundation | ✅ Locked |
| A3 | IDM CLT closure: ε = α/√N_horizon | IDM v4.0 | ✅ Locked |
| A4 | 粒子態與信息流投影的 duality hypothesis | Gemini self-alignment | ⏳ Pending |
| A5 | P3（OAS→GR）嘅 projection function | P3 output | ⏳ Pending（依賴） |

---

## 2. DERIVATION TARGETS

| # | Target | Method | Success Criteria |
|:--|:-------|:-------|:----------------|
| **Phase 1 — Structural Mapping** | | | |
| T1 | Hilbert space ℋ ↔ OAS address space mapping | Set theory + functional analysis | Bijection / inclusion |
| T2 | |ψ⟩ (wavefunction) ↔ N_horizon probability distribution | Analytic | Consistent probability interpretation |
| T3 | Operator Â ↔ sync observable mapping | Operator algebra | Expectation values match |
| **Phase 2 — Dynamic Mapping** | | | |
| T4 | Schrödinger equation iℏ∂_t|ψ⟩ = Ĥ|ψ⟩ ↔ sync flow equation | SymPy derivation | Unitarity preserved |
| T5 | QM collapse (measurement) ↔ sync threshold crossing | Algebraic | Born rule emergent |
| T6 | Uncertainty principle Δx·Δp ≥ ℏ/2 ↔ CLT bound 1/√N_horizon | Analytic | Same functional form |
| **Phase 3 — Correction Terms** | | | |
| T7 | IDM correction to QM: O(1/√N_horizon) term in dynamics | Perturbative | Falsifiable prediction |

---

## 3. GEMINI SELF-ALIGNMENT OUTPUT

> **（此節由 LuciferNg 整合）**
> Placeholder — 填入 Gemini iterations 中提煉出嘅關鍵 insight、公式、問題、counter-argument。

---

## 4. DEPENDENCY ON OTHER PROJECTS

| Dependency | Why | Status |
|:-----------|:----|:------|
| P3（OAS→GR）projection function | QM projection likely follows same OAS projection pattern, just at different energy scale | ⏳ P3 未開始 |
| P1（time entropy） | Time evolution operator e^{−iĤt/ℏ} requires understanding of time emergence | ⏳ P1 未開始 |

**建議 waiting condition：** P1 同 P3 至少完成 Phase 1 deliverables 先正式開始 P4。

---

## 9. CONCLUSION (added Jul 1, 2026 — HONEST VERSION)

### Final Verdict

| Target | Result | Honest Assessment |
|:-------|:-------|:-----------------|
| T1: Hilbert ↔ OAS bijection | ✅ 1-to-1 correspondence | ✅ Mathematically trivial (vector space isomorphism) |
| T2: Born rule from CLT | ✅ Structural mapping | ❌ **Numerically incompatible**: ħ/2 ≈ 0.5 >> 1/(2√N) ≈ 0.075 for N=44 |
| T3: Operator ↔ sync observable | ✅ Commutator from address competition | ⚠️ Analogical, not derived |
| T4: Schrödinger eq from sync flow | ✅ iℏ∂_t = sync flow + P1 time + P3 ADM | ❌ **i inserted by hand** — no OAS derivation of complex numbers |
| T5: Collapse as sync completion | ✅ Measurement = sync event | ⚠️ Philosophical position (Many-Worlds-type narration) |
| T6: Uncertainty ↔ CLT bound | ✅ Structural analogy | ❌ **Numerically incompatible**: ħ/2 ≠ 1/(2√N) |
| T7: IDM correction to QM | ✅ O(1/√N) ~ < 10⁻¹⁰ | ⚠️ Unfalsifiable — applies to ANY finite-N theory |

### The Core Problem: Complex Numbers

The most fundamental issue with P4 is the **origin of complex numbers** in quantum mechanics.

The sync flow equation is written as:
```python
d|ω⟩/dz = -i · H_sync · |ω⟩
```

The factor **i** (imaginary unit) is **inserted by hand** to make it look like the Schrödinger equation. There is NO OAS-based derivation of why sync flow should involve complex structure. In classical information dynamics, state evolution is REAL.

**Why this matters:** Complex numbers are not optional in QM. They are required for:
- **Interference**: ⟨ψ|A|ψ⟩ needs |c_i|² probabilities only if coefficients are complex
- **Commutators**: [x̂, p̂] = iℏ has i built in
- **Unitarity**: e^{−iĤt/ℏ} requires i to preserve norm under time evolution

Without deriving complex structure from OAS, the mapping is a **philosophical reinterpretation**, not a physical derivation.

### The Born Rule Problem

The code explicitly acknowledges:
> "hbar/2 >> 1/(2*sqrt(N)) — NOT a direct match"

For cosmic N=44: 1/(2√44) = 0.075. ħ/2 = 0.5 in Planck units. **Factor of ~7 mismatch.**
For effective QM N: 1/(2√10¹⁰) = 5×10⁻⁶. ħ/2 = 0.5. **Factor of ~10⁵ mismatch.**

The Born rule is the SINGLE most important non-classical feature of QM. If IDM cannot reproduce P(i) = |c_i|² from OAS principles (not just assert it), P4 fails.

### What P4 Actually Does

| Aspect | Rating |
|:-------|:------:|
| **Structural analogy** (Hilbert ↔ configuration space) | ✅ Valid as pedagogical mapping |
| **Physical derivation** (complex numbers, i, ħ from OAS) | ❌ Not achieved |
| **The i in Schrödinger equation** | ❌ Inserted by hand |
| **Born rule numerically** | ❌ Incompatible with CLT scaling |
| **Collapse interpretation** | ⚠️ Philosophical (consistent with relational QM) |
| **IDM correction term** | ⚠️ Unfalsifiable (any finite-N theory predicts O(1/√N)) |
| **Overall** | 🔴 Mapping, not derivation |

### Summary

P4 provides a STRUCTURAL MAPPING between OAS and QM language, but does NOT provide a PHYSICAL DERIVATION of QM from OAS principles. The critical gap: complex numbers (i, ħ) and the Born rule are assumed, not derived.

**To make P4 a real physical theory, three things are needed:**
1. Show that OAS dynamics naturally produces complex structure (e.g., from symplectic geometry of OAS phase space)
2. Derive iℏ = f(OAS parameters) — connect ħ to the CLT coupling α
3. Derive the Born rule P = |ψ|² from OAS consensus statistics, not CLT analogy

**Until then:** P4 is best described as "QM in OAS language" — a translation dictionary, not a derivation.

### Key Physical Insights
1. **Recombination = universe's first sync event** — when photons decouple at z≈1090, causal independence emerges → sync becomes possible → classical world is born
2. **CMB power spectrum encodes the sync boundary condition** — the primordial Gaussian fluctuations are the initial sync state of the classical universe
3. **Measurement is not mysterious** — it's the completion of a sync event between the quantum system and the classical apparatus

### T4 Resolution Path
- T4 was blocked by dependencies on P1 (time) and P3 (metric)
- P1 resolution: t = K(N)/(dS/dt) → time from entropy flow
- P3 resolution: S_sync[g] = ∫√(-g)[EH + corrections] → metric from sync cost
- Combined: sync flow in OAS space + time from entropy + ADM Hamiltonian = Schrödinger equation

### Context from Spike 002

IDM's current f(z) formalism is numerically **identical to ΛCDM at recombination (z≈1090)**:
- ΔH/H = 0, Δr*/r* = 0, Δage ≈ 10⁻¹² Myr
- DE fraction at recombination: 1.45×10⁻⁹ (negligible)
- IDM provides zero handle on early-universe physics

**This is not a bug — it's a structural gap.** The sync dip at z~0.6 is disconnected from QM-era physics. P4 must bridge this gap.

### The Recombination Puzzle for IDM↔QM

Standard cosmology sees recombination as:
| Phase | Redshift | Physics | IDM perspective |
|:------|:--------:|:--------|:----------------|
| Planck era | 10³² | QG unknown | OAS axiom regime |
| Inflation | 10²⁸ | QFT vacuum | Sync failure → expansion |
| Electroweak | 10¹⁵ | Symmetry breaking | Bandwidth differentiation |
| QCD | 10¹² | Hadron formation | Entropy threshold? |
| Recombination | 1090 | e⁻+p→H + CMB | **Classicalization event** |
| Reionization | 6–20 | Stars form | Structure sync onset |
| Sync dip | 0.6 | DE consumption | Active sync regime |

### IDM Recombination Hypothesis

Recombination as a **quantum-to-classical transition in information-processing terms:**

1. **Before recombination (z > 1090):** Universe is a coupled photon-baryon plasma. Each address is entangled via Thompson scattering. The effective N_sync → ∞ because causal contact is mediated by diffusing photons. **Sync is impossible -> QM regime.**

2. **At recombination (z = 1090):** Photons decouple. Addresses suddenly become causally independent. This is the universe's first "measurement" — each CMB photon carries a quantum state that becomes classical upon decoupling.

3. **Born rule emergence:** The CMB power spectrum's Gaussian statistics might emerge from the CLT (Central Limit Theorem) that IDM already uses for N_horizon scaling. CMB's ~10⁶ independent patches × CLT → Gaussian.

4. **Collapse as sync threshold:** QM measurement collapse = IDM sync completion. When a photon scatters off an electron at recombination, its state is "sync'd" with the electron's — this is the first instance of IDM's consensus mechanism.

### Key Derivations Needed

| Target | Description | Relation to P4 |
|:-------|:------------|:---------------|
| T_rec1 | Recombination as decoherence: ρ_quantum → ρ_classical when coupling to photon bath drops below sync threshold | Collapse (T5) |
| T_rec2 | CMB Gaussianity from CLT: N_independent_patches × 1/√N → Gaussian fluctuations | Born rule (T2) |
| T_rec3 | IDM correction to recombination: if sync DOES start at high z, predict non-Gaussian CMB signature | Falsifiable (T7) |
| T_rec4 | Time definition at recombination: if t ∝ ω_S⁻¹, what is ω_S when the universe is radiation-dominated? | Links to P1 |

### Key Insight

IDM's f(z) → 1 at high z because sync is impossible — but **that doesn't mean IDM has nothing to say about this era.** The **absence of sync IS a statement**: recombination happens exactly when the universe becomes causally structured enough for sync to become possible. The CMB power spectrum encodes the boundary condition.

### Open Questions

1. **Is recombination the FIRST sync event?** Or does sync start earlier (reionization)?
2. **If sync at z_c=0.6 consumes 5.5% of DE, what fraction of the information content was "sync'd" at recombination?**
3. **Does the CMB's Gaussianity constrain IDM's CLT coupling constant α?**

---

## 5. VERIFICATION MATRIX

| Verification | Type | Tool | Expected |
|:-------------|:----:|:----:|:--------|
| [ ] ℋ ↔ OAS 存在 bijection | Math | — | 無矛盾 |
| [ ] Born rule 從 sync distribution emerge | Analytic | SymPy | P = |⟨ψ⟩|² |
| [ ] Schrödinger eq 從 sync flow eq derive | Analytic | SymPy | exact form match |
| [ ] Uncertainty principle ≥ ℏ/2 ↔ CLT bound 1/√N | Numeric | numpy | ℏ/2 = f(1/√N) |
| [ ] IDM correction term ≤ current QM precision | Numeric | — | < 10⁻¹² relative |
| [ ] Recombination as decoherence (T_rec1) | Analytic | SymPy | ρ_quantum→ρ_classical emerges |

---

## 6. BOUNDARIES（唔好做嘅嘢）

- ❌ 唔好 try to disprove QM（QM is observationally verified to 10⁻¹²）
- ❌ 唔好改 QM 嘅數學 structure（Hilbert space, unitary evolution）
- ❌ 唔好引入 ad-hoc parameters
- ❌ 唔好跳過 P1/P3 foundation
- ⚠️ **Recombination analysis（§4.5）係 P4 嘅核心，唔係 optional** — QM↔IDM duality 必須解釋 recombination 作為 classicalization event