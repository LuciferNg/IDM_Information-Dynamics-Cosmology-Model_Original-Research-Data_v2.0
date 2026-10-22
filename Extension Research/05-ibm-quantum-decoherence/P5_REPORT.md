# Report: P5 — IBM QC Decoherence (IDM Sync Cost Test)

> **Project ID:** IDM-EXT-P5  
> **Date:** 2026-07-01  
> **Core Design:** Two-track protocol — Simulator vs Real IBM QC — detect IDM sync cost correction

---

## 1. Theory

### 1.1 IDM Decoherence Prediction

Standard QM: $P(t) = \exp(-t/T_2)$ (exponential decay)

IDM correction: $P_{\rm IDM}(t) = \exp[-t/T_2 - \varepsilon\ln(1 + t/\tau_0)]$

where $\varepsilon = 1/\sqrt{N_{\rm eff}}$ is the IDM epsilon at quantum processor scale.

### 1.2 Circuit Design
Ramsey interferometer with ZZ-coupled control qubits:
```
q0: |0⟩ — H — [IDLE for τ] — H — Measure
q1: |0⟩ — X — [IDLE for τ] — X — Measure (control, |1⟩)
q2: |0⟩ — H — [IDLE for τ] — H — Measure (control, |0⟩)
```

Measured: $P(|1\rangle) = 0.5[1 - \cos(\phi)\exp(-\Gamma t)]$ with $\Gamma = 1/T_2 + \Gamma_{\rm gate} + \Gamma_{\rm readout}$

---

## 2. Results

### 2.1 Hardware Blocker

| Quantity | Value |
|:---------|:-----|
| IDM correction $\Delta\Gamma/\Gamma$ | $\sim 10^{-5}$ |
| Current NISQ noise (IBM) | $\sim 10^{-2}$ |
| Signal-to-noise | $10^{-3}$ — **1000× below noise floor** |

### 2.2 Detection Horizon

| Platform | Noise | S/N | Viable? |
|:---------|:-----:|:---:|:-------:|
| IBM superconducting | $10^{-2}$ | $10^{-3}$ | ❌ NO |
| Ion trap (Quantinuum) | $5\times10^{-3}$ | $2\times10^{-3}$ | ❌ NO |
| Photonic (Xanadu) | $10^{-8}$ | $10^{3}$ | ⚠️ Maybe |
| Fault-tolerant QC | $10^{-15}$ | $10^{10}$ | ✅ YES (~30yr) |

---

## 3. Conclusion

**HARDWARE BLOCKED — current NISQ devices cannot detect the IDM correction.**

The IDM decoherence correction ($10^{-5}$) is 1000× below current IBM noise ($10^{-2}$). Detection requires fault-tolerant quantum computing (10-30 year horizon).

**Best current approach:** Measure the power-law tail at $t \gg T_2$, where IDM predicts $P_{\rm IDM}(t) > P_{\rm QM}(t)$ from the $\varepsilon\ln(1+t/\tau_0)$ correction.

**Experimental verdict:** Theoretically sound, falsifiable, but experimentally inaccessible for now.

### Files
- `p5_design.py` — circuit design + prediction formulas
- `p5_resolution.py` — detection threshold analysis
- `TASK_SPEC_CONTRACT.md` — full experimental design with conclusion