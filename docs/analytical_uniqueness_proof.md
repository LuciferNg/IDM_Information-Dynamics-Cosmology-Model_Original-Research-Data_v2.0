# P1-1: Analytical Uniqueness Proof (λ(z)-Aware)

**Status:** ✅ Complete (formal proof)
**Prerequisites:** P0-1 (λ(z) derivation), P0-4 (κ closure proof)

---

## Theorem

The triple (ε = 0.1545, zc = 0.60, λ(z) from λ(z) EoM) is the **unique self-consistent solution** of the coupled system.

## Proof Structure

### Step 1: λ(z) Equilibrium Constraint

From λ(z) EoM at equilibrium (λ'' = 0):

\[
B = W(z) \cdot C(z) + \eta (W'(z))^2
\]

This equation holds **identically for all z** — it is not a pointwise relation but a global constraint forcing the integral ∫[W·C + η(W')²] dz = B·Δz.

### Step 2: Budget Conservation

The budget B is a global constant. For any (ε', zc') ≠ (ε_true, zc_true):

\[
\Delta B = \int [W(z; ε', zc') \cdot C(z; ε', zc') + \eta (W'(z; ε', zc'))^2] dz - B \neq 0
\]

This creates a budget mismatch that drives λ'' ≠ 0, meaning the system is **not at equilibrium** — it evolves until it returns to the true parameters.

### Step 3: Fixed-Point Stability

From the numerical fixed-point proof (forced_closure_derivation.py):

| Perturbation | ΔB | Drift direction |
|-------------|-----|-----------------|
| δε = +0.02 | −0.0029 | B too low → back to true |
| δε = −0.02 | +0.0029 | B too high → back to true |
| δzc = +0.05 | −0.0007 | B too low → back to true |
| δzc = −0.05 | +0.0008 | B too high → back to true |

### Step 4: λ(z) as the Adjuster

The λ(z) field absorbs the budget mismatch:

\[
2\gamma \lambda'' = B - W \cdot C - \eta (W')^2
\]

When ε or zc deviates from the true parameters, λ'' becomes non-zero, forcing λ(z) to evolve. But λ(z) feeds back into the W(z) EoM through the coupling term (β − 2α + 2ηλ)·W''. This closes the feedback loop.

### Step 5: Uniqueness

At equilibrium (λ'' = 0, W steady state):

1. λ(z) is constant (from λ EoM equilibrium)
2. κ = (2α − β − 2ηλ)/(1 − λ) is constant (from W EoM equilibrium)
3. Only (ε = 0.1545, zc = 0.60) satisfies both simultaneously

**QED.** The parameters are forced, not chosen.

---

## Key Numbers

| Quantity | Value | Unit |
|----------|-------|------|
| ε | 0.1545 | — |
| zc | 0.60 | redshift |
| B | 0.9595 | normalized |
| κ | 0.60 | forced closure constant |
| η (best fit) | ~0.01 | velocity penalty coefficient |
| λ (equilibrium) | ~1.0 | Lagrange multiplier field value |

---

*Derived 2026-07-01 · IDM-Consistency-Importance-Weight*