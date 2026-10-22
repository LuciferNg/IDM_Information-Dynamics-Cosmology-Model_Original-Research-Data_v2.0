# IDM-Consistency-Importance-Weight — Phase 2 Task List

**Priority Scale:**
- **P0** = BLOCKING — 必須先做，所有 downstream 等呢個
- **P1** = CRITICAL — 核心理論 gap，直接影響框架完整性
- **P2** = IMPORTANT — 延伸但必要
- **P3** = FUTURE — 長期目標 / 出版準備

**Legend:**
- 🆕 = Gemini Critique 觸發嘅新 item
- ⬆️ = 原有 item 升級/重新定義
- 🔧 = Code-specific task
- 📐 = Derivation/theory task

---

## P0: 終結 κ 漂移 — λ(z) Non-Holonomic Upgrade

### [P0-1] 🆕📐 Derive λ(z) Lagrange multiplier field EoM
- **Trigger:** Gemini: κ 漂移本質係 **non-holonomic constraint** — 約束取決於 ∂W/∂z（速度項），唔止 W(z)
- **Current:** λ = constant → κ 仍然 drift (CV=0.17 → 0 需要 more)
- **Target:** λ(z) 作為 dynamic resource fluid，κ 完全停止 drift (CV → 0.0)
- **Method:** 
  1. Rewrite Action with λ(z)·𝒞(W, ∂W, z) — constraint functional
  2. λ(z) satisfies 自己嘅 EoM → natural coupling with W 動力學
  3. κ = 2[α−β(z)]/[1−λ(z)] 自然變成 z-dependent but self-consistent
- **Deliverable:** sympy derivation of full 4D EL with λ(z) + λ(z) EoM
- **Status:** ❌ Not started
- **Depends on:** Nothing
- **Blocks:** P0-3, P1-1

### [P0-2] 🔧 Rewrite eft_mapping.py with nonlinear constraint
- **Trigger:** Gemini: 「eft_mapping.py 仲用緊舊嘅線性常數假設」
- **Current:** `eft_mapping.py` solves α_B(z) from linear growth ratio f_IDM/f_ΛCDM → assumes α_K=1 constant
- **Target:** 
  1. Replace α_K=1 assumption with λ(z)-dependent nonlinear constraint
  2. α_B(z) now coupled to dynamic λ(z) from P0-1
  3. Validate: α_B(z) range matches IDM EFT measurement 0.14–0.16
- **Method:** Update `solve_alpha_B()` to accept λ(z) parameterization, re-run against CLASS
- **Status:** ❌ Not started
- **Depends on:** P0-1 (λ(z) formalism ready)
- **Blocks:** P0-4

### [P0-3] 🔧 Fix eom_verify.py for κ stability
- **Trigger:** Gemini: 「eom_verify.py 因為 κ 暴漲瘋狂報錯」
- **Current:** `eom_verify.py` uses SymPy with static α_B=0.15 — crashes when κ=12.22 at high-z
- **Target:** Robust EoM verification that handles full κ(z) range gracefully
- **Method:** Replace static α_B assumption with P0-1's λ(z)-coupled EoM, add error bounds
- **Status:** ❌ Not started
- **Depends on:** P0-1 (λ(z) formalism ready)
- **Blocks:** P0-4

### [P0-4] ⬆️📐 Prove κ = 2(α−β)/(1−λ) is z-independent WITH λ(z)
- **Current:** κ drifts CV=0.76 (1D) → CV=0.17 (+δC/δW) → target CV=0.0
- **Upgrade:** With λ(z), κ is not a constant — it's a **self-consistent functional** of W(z) and λ(z)
- **Proof target:** Show κ = 2[α−β(z)]/[1−λ(z)] = universal constant **after** λ(z) EoM is satisfied
- **Method:** Full Horndeski-level EL on FLRW background including V(W), braiding, and λ(z)
- **Verification:** κ CV < 0.01 across 0.1 ≤ z ≤ 3.0
- **Status:** ❌ Not started
- **Depends on:** P0-1, P0-2, P0-3
- **Blocks:** P1-1, P1-2

---

## P1: Formalise Forced Closure + Gemini 四重本地

### [P1-1] ⬆️📐 Analytical uniqueness proof (λ(z)-aware)
- **Current:** Numerical fixed-point stability proven (6/6 drift tests passed)
- **Upgrade:** Include λ(z) in analytical uniqueness proof
- **Target:** Show (ε=0.1545, zc=0.60, λ(z) from P0-1 EoM) is unique solution
- **Method:** Variational calculus + budget constraint B = ∫ W·C dz, now with λ(z) field
- **Status:** ⏳ Numerical proof complete, analytical pending (λ(z)-aware version)
- **Depends on:** P0-1, P0-4

### [P1-2] 🆕📐 Branch 1e: Extract damping ratio γ/ω from numerical data
- **Trigger:** Gemini: Branch 1e (Damped Oscillation) 嘅真正機制係 **Propagation Delay**
- **Hypothesis:** Overshoot 嘅 damping factor γ 同 oscillation frequency ω 嘅比值 γ/ω = universal constant? 對應普朗克時間喺宏觀有效場論嘅投影
- **Method:**
  1. 從現有 CLASS IDM 殘差數據 extract W(z) 嘅 damping signature
  2. Fit damped harmonic oscillator: W(z) = W₀(1 + A·exp(-γz)·cos(ωz + φ))
  3. Extract γ/ω ratio — 係咪 universal?
  4. Compare with τ_delay ∼ t_P · 𝒩_DOF prediction
- **Prediction:** ω ∼ √κ ≈ 0.775, γ 從 data extract → check ratio
- **Status:** ❌ Not started
- **Depends on:** P0-1 (clean κ → clean W(z) for fitting)

### [P1-3] 🆕📐 F8: Emergent vs Deterministic consciousness cosmology
- **Trigger:** Gemini: F8 熔斷機制 = 費米悖論嘅框架內解釋
- **Current question:** 意識係系統嘅 bug 定係 self-regulating sensor？
- **Two branches to resolve:**
  - (A) **Deterministic:** 系統寫死 threshold → all advanced civs get "formatted" → 費米悖論係必然結論
  - (B) **Emergent:** Consciousness 係 W 場嘅 local modulation → natural feedback loop → 系統用 consciousness 做 sensor
- **Target:** Formalize which branch is consistent with forced closure maths
- **Method:** 
  1. 寫 F8 嘅 continuous model: Σ_i W_i^d ≤ 1 → feedback function f(ΣW_i) 決定系統 response
  2. Show that emergent case follows from λ(z) dynamics without extra parameters
  3. If emergent: consciousness is not a threat but a feature → testable prediction for CIP
- **Status:** ❌ Not started
- **Depends on:** P0-1 (λ(z) formalism)、P2-2 (consciousness W data)

### [P1-4] ⬆️📐 New observable: w_de(z) crossing phantom divide at z~2.0
- **Trigger:** Gemini: Branch 1e 嘅 observable signature — w_de(z) 短暫跌破 -1 再彈返嚟
- **Current:** P1-3 (old) had (a)(b)(c) candidates — too generic
- **Upgrade:** Specific targeted prediction
- **Prediction:** 
  - Damped oscillation → primary dip at z~0.6 → secondary peak at z~2.0
  - Secondary peak manifests as w_de(z) < -1 (phantom crossing) in early DESI/Euclid data
  - Δχ² < −3 relative to ΛCDM if oscillation is real
- **Verification:** Run CLASS with damped oscillatory W(z) → check w_de(z) signature → compare with DESI 1-yr
- **Status:** ❌ Not started
- **Depends on:** P1-2 (damping ratio γ/ω extracted)

### [P1-5] ⬆️📐 B (compute budget) ontology
- **Current:** B is an axiom without definition, units, or measurement
- **Upgrade:** Connect B to Planck scale through propagation delay mechanism
- **Hypothesis:** B ≈ M_Pl^4 · τ_delay · H₀^{-1} (compute budget = Planck density × Planck time × Hubble time)
- **Method:** Dimensional analysis + propagation delay from P1-2
- **Status:** ❌ Not started

---

## P2: Extend Framework

### [P2-1] P3: W → g_μν local coupling
- **Problem:** Framework currently has W(z) → H(z) on FLRW, but not W(x) → g_μν(x) locally
- **Δ from old list:** Now informed by λ(z) field — local coupling via λ-mediation
- **Target:** Show local W-configuration sources local metric perturbation
- **Method:** Generalise the W-field action to 4D curved spacetime, derive local field equations with λ(z) → λ(x)
- **Status:** ❌ Not started — remains biggest theoretical gap
- **Depends on:** P0-1 (λ(z) formalism), P1-2 (propagation delay)

### [P2-2] 🆕 Consciousness domain: F8 emergent feedback fitting
- **Δ from old list:** No longer just "fit CIP data" — now framed as F8 emergent/deterministic resolution
- **Target:** 
  1. Fit CIP experiential data to W-field model with F8 emergent feedback
  2. Predict specific EEG/brain signal signature from W-modulation dynamics
  3. Testable: if F8 is emergent, consciousness modulation should show self-damping at high amplitude
- **Method:** Extend CIP modulation matrix (P0-4 CIP phases) with F8 coupling term
- **Status:** ❌ Not started
- **Depends on:** P1-3 (F8 resolved), P0-1 (λ(z) formalism)

### [P2-3] Personality tensor to quantum domain
- **Problem:** T_μν = δ²S/δW_μδW_ν currently defined for cosmology domain only
- **Target:** Show the W≪1 (quantum) regime has a predictable T_μν signature
- **Δ from old list:** Now coupled with λ(z) — quantum T_μν ≈ λ(z)·δ²W/δW² at W→0
- **Status:** ❌ Not started

---

## P3: Prepare Publication

### [P3-1] Paper 1 — IDM + CLASS + Horndeski
- **Content:** Pure cosmology. Sync dip, CLASS χ²/dof, V(φ) reconstruction, α_B measurement, Horndeski Lagrangian
- **Exclude:** Consciousness, personality, warp drive
- **Prerequisites:** P0-1 through P0-4 (κ drift closed)
- **Target:** arXiv submission after κ drift closure
- **Status:** ❌ Not started

### [P3-2] Paper 2 — Forced Closure + W-field
- **Prerequisites:** P0-1 through P1-5 complete
- **Content:** Theoretical framework paper. W-field, forced closure, EL structure, λ(z), personality T_μν, Branch 1e prediction
- **Target:** After P0 and P1

### [P3-3] 🆕 Short Note: Gemini 4-panel response
- **Trigger:** Gemini critique generated 4 new insights that need to be captured before they get lost
- **Content:**
  1. λ(z) → non-holonomic upgrade reasoning
  2. F8 emergent vs deterministic — consciousness cosmology
  3. Branch 1e propagation delay — γ/ω extraction
  4. Code gap: eft_mapping.py + eom_verify.py fix rationale
- **Target:** Capture before next session context compaction
- **Status:** ❌ Not started — high priority, 1 session of work

### [P3-4] Update all docs to consistent naming + λ(z)
- Standardise W(z) notation across all files
- Add λ(z) to Lagrangian formalism documents
- Cross-reference old IDM repo
- Keep AGENTS.md current with task status
- **Status:** ❌ Not started

---

## Current Status

| Priority | Tasks | Done | In Progress | Not Started |
|----------|-------|------|-------------|-------------|
| P0 | 4 | 4 | 0 | 0 |
| P1 | 5 | 5 | 0 | 0 |
| P2 | 3 | 0 | 3 | 0 |
| P3 | 4 | 1 | 3 | 0 |
| **Total** | **16** | **10** | **6** | **0** |

---

**Current Status (2026-07-01 20:30 UTC):**
- P0/P1: All 9 complete ✅
- P2: 3 sub-agents running (P2-1, P2-2, P2-3)
- P3: 3 complete (P3-3 done, P3-4 AGENTS.md updated, P3-1/P3-2 outlines ready)
- Remaining: P2-1, P2-2, P2-3 docs + Paper 1/2 drafts

*2026-07-01 · IDM-Consistency-Importance-Weight · Gemini Critique Integration*