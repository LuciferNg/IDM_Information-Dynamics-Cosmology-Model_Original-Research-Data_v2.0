# TASK SPECIFICATION CONTRACT — P6: 無暗物質星系 — IDM熵固化額外引力

**Project ID:** IDM-EXT-P6  
**Status:** ⏳ 待驗證內容整合  
**Date:** 2026-06-29  
**Core Claim:** 觀測到嘅 dark matter-deficient 星系（NGC 1052-DF2, DF4 等）唔係 anomaly —— IDM 嘅 entropy 固化機制喺星系合併過程中產生額外引力勢，令呢啲星系無需傳統 DM halo 都能維持觀測動力學

---

## 1. INPUT ASSUMPTIONS（已鎖定基礎）

| # | Assumption | Source | Status |
|:--|:-----------|:-------|:------:|
| A1 | IDM Friedmann equation: H²(z) = H₀²[Ω_m(1+z)³ + Ω_Λ·f_ID(z)] | IDM v4.0 | ✅ Locked |
| A2 | f_ID(z) = 1 − ε·(z/z_c)·exp(−z/z_c), ε = α/√N_horizon | IDM v4.0 | ✅ Locked |
| A3 | IDM Horndeski action: S = ∫d⁴x√(−g)[½M_Pl²R + X − V(φ) + ξ₀e^{−λφ}·α_B·X·□φ] | IDM Lagr. Rev. Eng. | ✅ Locked |
| A4 | α_B(z) ≈ +0.15, braiding provides extra gravity-like effect | EFT α_B mapping | ✅ Locked |
| A5 | DM-deficient galaxies exist: NGC 1052-DF2 (DM fraction < 10%), DF4, others | Observational literature | ✅ Known |
| A6 | Galaxy mergers are entropy-increasing events in IDM framework | Hypothesis | ⏳ Pending |
| A7 | 星系合併中 entropy 固化（screening 機制局部 freezing）產生額外引力勢 | Hypothesis | ⏳ Pending |

---

## 2. DERIVATION TARGETS

| # | Target | Method | Success Criteria |
|:--|:-------|:-------|:----------------|
| **Phase 1 — Mechanism Definition** | | | |
| T1 | 定義 galaxy-scale entropy solidification：merger 事件點樣局部提升 α_B(x) 或 ξ(φ) 嘅 screening 強度 | IDM Lagrangian + field analysis | Well-defined operator Δα_B(x,t) |
| T2 | 合併過程 entropy budget：dS_merger = ?，衡量固化程度 | IDM entropy gradient action | dS_merger > dS_background |
| **Phase 2 — Gravitational Prediction** | | | |
| T3 | 固化後嘅額外引力勢 Φ_entropy(r)：由 localised braiding term 產生嘅 effective mass | Weak-field expansion of IDM action | Φ_entropy ~ GM_eff/r, M_eff versus merger mass |
| T4 | IDM rotation curve prediction for DM-deficient galaxies: v²(r) = v_baryon² + v_IDM² | Numeric (IDM core) | v_IDM sufficient to explain DF2/DF4 data without DM |
| **Phase 3 — Falsifiability** | | | |
| T5 | 預測：邊類星系應該 DM-deficient（merger history, mass range, environment） | Merger history catalog + IDM prediction | Catalog prediction vs observation |
| T6 | 反預測：乜 conditions 下 entropy 固化失效（violent mergers, gas-rich vs gas-poor） | Parameter space scan | Testable with upcoming JWST/VLT data |

---

## 3. GEMINI SELF-ALIGNMENT OUTPUT

> **（此節由 LuciferNg 整合）**
> Placeholder — 填入 Gemini iterations 中提煉出嘅關鍵 insight、公式、問題、counter-argument。

---

## 4. VERIFICATION MATRIX

| Verification | Type | Tool | Expected |
|:-------------|:----:|:----:|:--------|
| [ ] Entropy solidification operator defined | Analytic | SymPy | Well-posed Δα_B(x,t) |
| [ ] Merger entropy budget: dS_merger > 0 | Numeric | IDM core | Monotonic increase |
| [ ] Φ_entropy(r) from IDM action weak-field | Analytic | SymPy | Inverse-square at large r |
| [ ] DF2 rotation curve fit without DM | Numeric | Galpy / IDM | χ² < 2 (per data point) |
| [ ] Catalog prediction matched to observed DM-deficient galaxies | Statistical | Survey data | p-value > 0.05 |
| [ ] Falsifiable: merger-poor ellipticals should NOT be DM-deficient | Observational | — | Checkable |

| **Risk** | Galaxy-scale N_horizon → ε_correction tiny — 需確認效應可觀測

## 8. CONCLUSION (added Jul 1, 2026 — HONEST VERSION)

### Final Verdict

| Target | Result | Status |
|:-------|:-------|:------|
| T1: Entropy solidification operator | ✅ Δα_B(r) = K·(dS/dV)·exp(-r/R_vir) defined | ✅ Formal |
| T2: Merger entropy budget | ✅ dS_merger >> dS_bg qualitatively | ✅ Plausible |
| T3: Extra gravitational potential | ✅ Mechanism direction: G_eff < G_N (sign-corrected) | ✅ Direction |
| T4: DF2 rotation curve | ❌ IDM-consistent ε_gal gives σ ≈ 8.09 km/s (needs 7 km/s) | ❌ Insufficient |
| T5: Predict DM-deficient types | ✅ 3 conditions: z<0.6, dry merger, low mass | ✅ Qualitative |
| T6: Failure conditions | ✅ 3 failure modes + z-condition | ✅ Qualitative |

### Critical Physical Finding

**The P6 mechanism is QUANTITATIVELY INSUFFICIENT within IDM perturbation theory:**

- IDM perturbation scale: ε_cosmic ≈ 0.15, ε_gal ≈ 0.001
- Required Δα_B ≈ −0.24 to match DF2 (G_eff/G_N ≈ 0.75)
- |Δα_B_needed| / ε_cosmic ≈ 1.6× (exceeds bound)
- |Δα_B_needed| / ε_gal ≈ 230× (far exceeds bound)

Within the IDM-consistent perturbation framework (|Δα_B| ≤ ε_gal ≈ 0.001), 
the maximum predicted G_eff correction at galaxy scales is < 0.1% — 
undetectable with current instruments.

### What Still Works (Qualitative Predictions)

1. DM-deficient galaxies should preferentially form at z < 0.6 (dip recovery regime)
2. Mergers at z > 0.6 should produce ENHANCED G_eff → DM-overabundant galaxies
3. Dry, low-mass-ratio mergers produce the largest effect

These predictions are testable with DESI and JWST kinematic surveys.

### Files
- `p6_derivation.py` — honest physical analysis with perturbation bounds
- `p6_field_theory.py` — field-theoretic Δα_B(r) operator
- `P6_REPORT.md` — full report with quantitative barrier documentation

### Falsifiable Predictions
1. DM-deficient galaxies (like DF2) should show merger signatures in deep imaging
2. Low HI gas fraction (< 10⁸ M☉) and shallow inner profile
3. Merger-poor ellipticals should NOT be DM-deficient
4. High-z (z > 0.6) mergers should show ENHANCED DM (opposite effect)

- ❌ 唔好修改 IDM core（ε, z_c, α_B, ξ₀ 已鎖定）
- ❌ 唔好引入 new free parameter（只用現有 IDM 參數）
- ❌ 唔好 claim「IDM eliminates DM entirely」— IDM modifies DM distribution, doesn't remove it
- ❌ 唔好做 full N-body simulation（budget/code constraint）
- ❌ 唔好挑戰已確認嘅 DM观测（bullet cluster, weak lensing maps）

---

## 6. KEY BOTTLENECK

Galaxy-scale entropy solidification 未有 field-theoretic definition。
**IDM Lagrangian 嘅 local braiding term**（α_B(x) 而非 α_B(z)）需要推導，而家得 background-level α_B(z)。
**建議 approach：** 用 IDM Horndeski action 嘅 screening mechanism（ξ(φ)）做 spatial perturbation analysis，睇 merger 點樣局部 enhance screening。

---

## 7. WAVE PLACEMENT PROPOSAL

| Dimension | Assessment |
|:----------|:-----------|
| **Wave** | **1.5**（與 P1+P2 並行，但 domain 不同） |
| **Feasibility** | 🟡 Medium |
| **Dependency** | 獨立於 P1/P2（用 IDM core Lagrangian 直接出發） |
| **Risk** | Galaxy-scale N_horizon → ε_correction tiny — 需確認效應可觀測 |