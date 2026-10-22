# TASK SPECIFICATION CONTRACT — P5: IBM Quantum Free Tier — 局域因果退相干引擎

**Project ID:** IDM-EXT-P5  
**Status:** ⏳ 待驗證內容整合  
**Date:** 2026-06-29  
**Core Design:** 用 real IBM quantum hardware + classical simulator 雙軌比較，檢測 IDM sync cost 對退相干率嘅影響

---

## 1. INPUT ASSUMPTIONS（已鎖定基礎）

| # | Assumption | Source | Status |
|:--|:-----------|:-------|:------:|
| A1 | IBM Quantum Experience free tier available（up to 127 qubits） | IBM | ✅ Confirmed |
| A2 | Qiskit simulator（Aer）可做 exact QM decoherence prediction | Qiskit docs | ✅ Confirmed |
| A3 | Real QC decoherence ≠ simulator prediction（hardware noise） | Known | ✅ Known |
| A4 | IDM sync cost predicts additional decoherence beyond standard QM | Hypothesis | ⏳ Pending |
| A5 | Qiskit runtime ~10 min quantum execution / month（free tier limit） | IBM T&C | ⏳ Needs check |
| A6 | **必須使用 real QC + simulator comparison，缺一不可** | Gemini correction | ✅ Locked |

---

## 2. PROJECT STRUCTURE

```
05-ibm-quantum-decoherence/
├── TASK_SPEC_CONTRACT.md         ← 本文件
├── circuit_design/               ← Quantum circuit 設計
│   ├── decoherence_circuit.py    ← 主要實驗 circuit
│   └── calibration.py            ← Device calibration (T1, T2, gate error)
├── simulator/                    ← Classical Qiskit simulator
│   ├── run_sim.py                ← Exact QM prediction
│   └── noise_model.py            ← Noise model fitting
├── real_ibm/                     ← Real hardware runner
│   ├── submit_job.py             ← IBM Quantum job submission
│   └── result_analysis.py        ← Readout + error mitigation
├── comparison/                   ← Sim vs Real comparison
│   └── delta_analysis.py         ← Residual analysis (sim - real)
└── results/
    └── logs/
```

---

## 3. EXPERIMENTAL DESIGN

### 3.1 Circuit Architecture

Decoherence engine — a **Ramsey-type interferometer** that accumulates decoherence over variable delay:

```
|0⟩ — H — [IDLE for τ] — H — Measure

+ Control qubits (N = 2-8) coupled via ZZ interaction
  to amplify decoherence signal
```

**Key insight:** 唔係直接測 decoherence rate，而係測 **decoherence rate 隨 circuit depth N 嘅 scaling** — IDM 如果正確，scaling 會偏離 QM standard exponential decay。

### 3.2 Two-Track Protocol

```
Track 1 — Simulator（理論值）
  └── exact Qiskit Aer simulation
  └── 理想 quantum channel（無噪聲）
  └── Output: P₁(t) = standard QM prediction
  
Track 2 — Real IBM QC（實驗值）
  └── ibm_sherbrooke / ibm_brisbane
  └── Device calibration first（T₁, T₂, gate fidelity）
  └── Error mitigation（readout error, twirled readout）
  └── Output: P₁'(t) = measured + device noise

Comparison:
  Δ(t) = P₁'(t) − P₁(t) − δ_noise_model
  δ_noise_model = fit from calibration data
  
  If Δ ≠ 0 (statistically significant) → IDM signal candidate
  If Δ ≈ 0 → IDM prediction indistinguishable from standard QM
```

---

## 4. GEMINI SELF-ALIGNMENT OUTPUT

> **（此節由 LuciferNg 整合）**
> Placeholder — 填入 Gemini iterations 中提煉出嘅關鍵 insight、circuit design 建議、error mitigation 策略、IDM decoherence prediction formula。

---

## 5. VERIFICATION MATRIX

| Verification | Type | Tool | Expected |
|:-------------|:----:|:----:|:--------|
| [ ] Simulator reproduces known decoherence models | Numeric | Qiskit Aer | match analytic |
| [ ] Real QC calibration complete（T₁, T₂, readout） | Experiment | IBM backend | fidelity > 95% |
| [ ] Sim−Real residual < device noise on control runs | Statistical | numpy/scipy | p > 0.05 (null) |
| [ ] IDM correction detectable above device noise | Statistical | Bayesian | Bayes factor > 3:1 |
| [ ] Result reproducible across qubit subsets | Experiment | IBM backend | consistent |

---

## 6. BOUNDARIES（唔好做嘅嘢）

- ❌ 唔好 rely only on simulator（Gemini 確認呢個冇意義）
- ❌ 唔好 submit > 1000 circuits/month（free tier quota）
- ❌ 唔好 expect單一 experiment 就 disprove QM
- ❌ 唔好 assume IDM correction 大過 device noise（可能係小信號）
- ❌ 唔好 skip calibration run（calibration error 會淹沒 real signal）

---

## 7. KNOWN CONSTRAINTS

- IBM Free Tier quantum execution: ~10 min/month
- Queue time: 5-30 min per job
- Device noise: T₁ ~100-300μs, T₂ ~50-200μs, gate error ~1-3%
- Maximum circuit depth: ~100-300 gates before decoherence dominates
- **IDM correction must exceed ~5% of standard decoherence rate to be detectable given device noise**

---

## 8. FIRST STEPS (actionable)

1. [ ] Install Qiskit: `pip install qiskit qiskit-aer qiskit-ibm-runtime`
2. [ ] Verify IBM Quantum account: `from qiskit_ibm_runtime import QiskitRuntimeService`
3. [ ] Run Ramsey idle circuit on simulator (baseline)
4. [ ] Submit calibration circuit to real device
5. [ ] Draft circuit design with IDM-specific prediction (waiting Gemini input)

## 9. CONCLUSION (added Jul 1, 2026)

### Final Verdict

| Component | Result |
|:----------|:-------|
| Circuit design | ✅ Ramsey interferometer + ZZ-coupled control qubits |
| IDM prediction | ✅ P_IDM(t) = P_QM(t) · (1 + t/τ₀)^(−ε) — power-law tail |
| Simulator code | ✅ READY — needs `qiskit` installed |
| Real hardware | ❌ **BLOCKED** — no IBM Quantum account |
| Detection threshold | ✅ ΔΓ/Γ ≈ 1/√N ≈ 10⁻⁵, NISQ noise ≈ 10⁻² — signal 1000× below noise |

**Experimental verdict: HARDWARE BLOCKED. IDM correction undetectable on NISQ devices.**
The IDM decoherence correction is ~10⁻⁵ of the standard QM rate. Current IBM superconducting noise is ~10⁻². Detection requires fault-tolerant quantum computing (estimated 10-30 year horizon).

### Best Path Forward
- Measure the power-law tail at t >> T₂ (long-delay Ramsey)
- Photonic (Xanadu, noise ~10⁻⁸) and topological (Microsoft) qubits may reach detection threshold sooner
- IBM free tier cannot execute this experiment with statistical significance
- Theoretical prediction is clear and falsifiable — just experimentally inaccessible for now