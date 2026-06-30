# Consistency Importance Weight Framework

Parameters are not chosen — they are forced.

The universe has one mandate: consistency. With finite compute budget, parameters are the only feasible solution. This framework maps physics onto importance_weight — the system's resource allocation for maintaining consistency.

## Core Axioms

- **Consistency mandate** — the universe must maintain global consistency
- **Finite budget** — not all degrees of freedom can be resolved deterministically
- **Forced closure** — parameters are the unique feasible solution, not an optimization choice
- **Importance Weight** *I_f* ∈ [0,1] — fraction of compute budget allocated to resolving variable *f*
  - *I_f* → 1: deterministic (classical)
  - *I_f* → 0: probabilistic (quantum)

## Repo Structure

```
IDM-Consistency-Importance-Weight/
├── README.md                    # This file
├── AGENTS.md                    # Hermes agent instructions
├── LICENSE                      
├── docs/
│   ├── IDM-Consistency-Importance-Weight.md     # Core document
│   ├── importance-weight-branch-analysis.md  # Territory map of all possibilities
│   ├── importance_weight_lagrangian.md     # Formal Lagrangian + forced closures
│   └── preliminary-report.md         # Current state summary
├── src/
│   ├── importance_weight_spike.py              # I(z) mapping, α_B consistency, personality
│   └── importance_weight_consciousness_lagrangian.py  # Consciousness domain + Lagrangian
└── results/
    └── importance_weight/
        ├── importance_weight_space.png   # Full importance_weight plot
        ├── importance_weight_z.txt       # Numerical data
        └── importance_weight_lagrangian.md  # From Step 4
```

## Status

- **Framework**: v0.1 — interpretive ontology, connected to IDM data
- **Quantitative**: sync dip → *I*(*z*) mapping confirmed, α_B consistent
- **Personality tensor**: *T_{zz}* = +0.158 at the critical scale (recovery attractor)
- **Forced closures**: 8 irreducible constraints identified

## Related Projects

- [IDM Lagrangian Reverse Engineering](https://github.com/LuciferNg/IDM-Lagrangian-Reverse-Engineering)
- [Consciousness Interface Protocol (CIP)](references in docs)

---
*2026-06-30  ·  Author: LuciferNg*