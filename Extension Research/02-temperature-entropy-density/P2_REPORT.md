# Report: P2 — Temperature and Entropy Density (HONEST VERSION)

> **Project ID:** IDM-EXT-P2  
> **Date:** 2026-07-01  
> **Core Claim (downgraded):** For horizon systems (BH, Unruh), temperature is proportional to entropy density. This is NOT a universal law.

---

## 1. The Thermodynamic Truth

The fundamental definition of temperature in thermodynamics is:

$$\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V,N}$$

This is the Gibbs relation: $dS = (1/T)dE + (P/T)dV - (\mu/T)dN$.

The claim $T = dS/dV$ confuses $\partial S/\partial E$ (temperature) with $\partial S/\partial V$ (which is pressure/temperature). These are DIFFERENT derivatives.

---

## 2. Where It Works: Horizon Systems

### Black Hole (Schwarzschild)
- $S = A/4 = \pi R^2 = 4\pi M^2$ (Planck units)
- $V = 4\pi R^3/3 = 32\pi M^3/3$
- $dS/dV = (dS/dM)/(dV/dM) = (8\pi M)/(32\pi M^2) = 1/(4M)$
- $T_H = 1/(8\pi M) = (1/2\pi) \cdot dS/dV$

**Why it works:** $S \propto M^2$, $V \propto M^3$ → $dS/dV \propto 1/M$, $T_H \propto 1/M$. The shared $1/M$ scaling is a geometric coincidence, not a universal law.

### Unruh Effect (Rindler)
- $S_{\rm Rindler} = \pi/a^2$
- $V_{\rm Rindler} \propto 1/a^3$
- $dS/dV = a/2$
- $T_U = a/(2\pi) = (1/\pi) \cdot dS/dV$

Same pattern: $S \propto a^{-2}$, $V \propto a^{-3}$ → $dS/dV \propto a$, $T_U \propto a$.

---

## 3. Where It Fails: Ordinary Matter

For an ideal gas: $S = N[\ln(V/N) + (3/2)\ln T + \text{const}]$
- $(\partial S/\partial V)_T = N/V$
- $T \neq N/V$ (unless $P = 1$ in very specific units)
- The Gibbs relation gives $P/T = \partial S/\partial V$, not $1/T$

---

## 4. Results

| Target | Result | Honest Assessment |
|:-------|:-------|:-----------------|
| T1: Dimensional analysis | $[T] = [dS/dV]$ in Planck units | ✅ Trivial (unit convention) |
| T2: BH thermodynamics | $T_H = (1/2\pi) \cdot dS_{\rm BH}/dV$ | ✅ Real, not universal |
| T3: Unruh effect | $T_U = (1/\pi) \cdot dS/dV$ | ✅ Real, geometry-dependent |
| T4: CMB temperature | Stefan-Boltzmann preserved | ✅ Identity, not test |
| T5: Stefan-Boltzmann | $u = a_{\rm rad} T^4$ | ✅ Identity, not test |

---

## 5. Conclusion

**$T \propto dS/dV$ holds for horizon systems (BH, Unruh) as a geometric coincidence — it is NOT a universal law of thermodynamics.**

The relationship is real physics (part of the Jacobson 1995 program showing Einstein equations from horizon thermodynamics), but it's LIMITED to systems with horizon geometries where $S \propto R^2$ and $V \propto R^3$.

**Proposed reframing:** Rename P2 to "Horizon Temperature from Entropy Density" and position it within the established thermodynamics-of-spacetime literature, not as a new universal law.

### Files
- `p2_derivation.py` — honest derivation with Gibbs relation
- `TASK_SPEC_CONTRACT.md` — task specification with corrected conclusion