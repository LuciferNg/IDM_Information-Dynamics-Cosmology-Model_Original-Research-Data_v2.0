# TASK SPECIFICATION CONTRACT — P2: 溫度是熵流密度的驗證

**Project ID:** IDM-EXT-P2  
**Status:** ⏳ 待驗證內容整合  
**Date:** 2026-06-29  
**Core Claim:** 溫度係 entropy flow 嘅空間密度 — T = dS/dV

---

## 1. INPUT ASSUMPTIONS（已鎖定基礎）

| # | Assumption | Source | Status |
|:--|:-----------|:-------|:------:|
| A1 | Standard thermodynamics: dS = dQ/T, Gibbs-Duhem | Literature | ✅ Known |
| A2 | Black hole thermodynamics: T_H = κ/2π, S_BH = A/4 | Literature | ✅ Known |
| A3 | Unruh effect: T_U = a/2π | Literature | ✅ Known |
| A4 | IDM entropy gradient action | IDM Lagr. Rev. Eng. | ✅ Locked |
| A5 | CMB temperature T₀ = 2.725K | Planck 2018 | ✅ Known |
| A6 | 溫度 = 熵流密度 hypothesis | Gemini self-alignment | ⏳ Pending |

---

## 2. DERIVATION TARGETS

| # | Target | Method | Success Criteria |
|:--|:-------|:-------|:----------------|
| T1 | 量綱驗證： [T] = [S]/[V] | SymPy dimensional analysis | 無矛盾 |
| T2 | Black hole: T_H 可否寫為 dS_BH/dV | Analytic | T_H = f(dA/dV) |
| T3 | Unruh effect: T_U = a/2π ↔ dS/dV | Analytic + numeric | consistency |
| T4 | CMB T₀ = 2.725K 對應宇宙熵密度 | IDM + known cosmology | ρ_s(0) = f(T₀) |
| T5 | Stefan-Boltzmann law 一致性 | Analytic | σ·T⁴ ↔ dS/dt·T |

---

## 3. GEMINI SELF-ALIGNMENT OUTPUT

> **（此節由 LuciferNg 整合）**
> Placeholder — 填入 Gemini iterations 中提煉出嘅關鍵 insight、公式、問題、counter-argument。

---

## 6. CONCLUSION (added Jul 1, 2026 — HONEST VERSION)

### Final Verdict

| Target | Result | Honest Assessment |
|:-------|:-------|:-----------------|
| T1: Dimensional analysis | ✅ Planck units consistent — [T] = [dS/dV] | Trivial (unit convention) |
| T2: BH thermodynamics | ✅ T_H = (1/2π)·dS_BH/dV | Real horizon physics, NOT universal |
| T3: Unruh effect | ✅ T_U = (1/π)·dS/dV | Same geometric pattern, diff constant |
| T4: CMB temperature | ✅ Stefan-Boltzmann preserved | Identity, not a test |
| T5: Stefan-Boltzmann law | ✅ u = a_rad·T⁴ = a_rad·(dS/dV)⁴ | Identity, not a test |

### Critical Correction

The original claim "T = O(1)·dS/dV is universal" is **incorrect as a universal statement**.

**Why:** Standard thermodynamics defines temperature through the Gibbs relation:
$$dS = (1/T)dE + (P/T)dV - (\mu/T)dN$$
so $1/T = (\partial S/\partial E)_V$, NOT $T = dS/dV = (\partial S/\partial V)_E$.

**Where it works:** For BH and Unruh horizons, T IS proportional to dS/dV because of specific geometric scalings:
- BH: $S \propto M^2$, $V \propto M^3$ → $dS/dV \propto 1/M \propto T_H$
- Unruh: $S \propto a^{-2}$, $V \propto a^{-3}$ → $dS/dV \propto a \propto T_U$

These are real physical results from the Jacobson-type thermodynamics-of-spacetime program, but they are NOT evidence for a universal law.

**Where it fails:** For an ideal gas, $(\partial S/\partial V)_T = N/V \neq T$.

### Proposed Reframing
P2 should be positioned as "Horizon Temperature from Entropy Density" — a known result from the thermodynamics of spacetime (Jacobson 1995, Padmanabhan 2010), not a new universal law. The BH and Unruh proportionalities are real and interesting, but do not constitute a general theory of temperature.

---

## 5. BOUNDARIES（唔好做嘅嘢）

- ❌ 唔好修改 IDM core
- ❌ 唔好引入新 free parameter
- ❌ 唔好做 statistical fitting（呢個係 definitional validation）
- ❌ 唔好挑戰 well-established thermodynamics laws