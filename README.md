# IDM-Consistency-Importance-Weight

**Parameters are not chosen — they are forced.**

The universe has one mandate: **consistency** — with finite compute budget, parameters are the unique feasible solution. This framework reverse-engineers that constraint set.

---

## The Core Idea

- **Importance Weight W ∈ [0,1]** — fraction of compute budget allocated to resolving a variable's consistency
  - W → 1: deterministic (classical physics)
  - W → 0: probabilistic (quantum mechanics)
- **Parameters are forced closure** — they are the only feasible stable state, not an optimization choice
- **Personality T_μν** — the shape of the consistency cost function itself, one level deeper than parameters

---

## What's Been Proven

| Proof | Method | Result |
|-------|--------|--------|
| Sync dip → W(z) mapping | IDM CLASS data | ε = 0.1545, zc = 0.60, χ²/dof = 0.51 |
| Forced closure | Numerical fixed-point stability | True (ε, zc) is unique stable attractor |
| α_B consistency | IDM growth mismatch | α_B = −0.58·dW/dz, α_B(0) = 0.1444 |
| Euler-Lagrange | SymPy derivation + δC/δW coupling | CV improved 0.76 → 0.17 |
| Consciousness | CIP phase → W modulation | Local recursive version of global optimisation |

---

## Repo Structure

```
docs/
├── report_1.0.md                     # Full programme narrative
├── consistency-importance-weight.md   # Core framework definitions
├── importance-weight-branch-analysis.md / Territory map
├── importance-weight-lagrangian.md    # Formal action + EL
├── forced_closure_derivation.md       # Fixed-point proof
├── euler_lagrange_proof.md           # SymPy derivation
├── preliminary-report.md              # Phase 1 summary
└── theory-assessment.md               # Honest evaluation
src/
├── importance_weight_spike.py              # W(z) from sync dip
├── local_w_modulation.py
├── forced_closure_derivation.py
└── euler_lagrange_proof.py
results/importance_weight/                # Figures + data
```

---

## Key Numbers

| Quantity | Value |
|----------|-------|
| Sync dip ε | 0.1545 |
| Critical scale zc | 0.60 |
| W(0) | 0.9975 |
| W(zc) — minimum | 0.9432 |
| Personality T_zz(zc) | +0.158 |
| Braiding α_B(0) | 0.1444 |
| CLASS χ²/dof | 0.51 |
| Dip budget fraction | 0.22% |

---

## Status

| Phase | What | Status |
|-------|------|--------|
| Ontology + Interpretation | Axioms, mapping, forced closure proof | ✅ Complete |
| Derivation + Formalisation | δC/δW coupling, Horndeski-level EL | ⏳ In progress |
| Verification | Publishable prediction for DESI/Euclid | ❌ Not started |

---

## Related

- [IDM Lagrangian Reverse Engineering](https://github.com/LuciferNg/IDM-Lagrangian-Reverse-Engineering) — the sync dip that started this

---

*2026-06-30  ·  Author: LuciferNg*