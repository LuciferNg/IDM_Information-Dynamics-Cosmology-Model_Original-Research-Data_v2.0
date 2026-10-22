# λ(z) Lagrange Multiplier Field — Derivation

**Date:** 2026-07-01
**Status:** ✅ Derived — coupled W(z), λ(z) EoMs

## 1. Upgraded Action

$$S = \int \left[W \cdot C + \alpha (W')^2 + \beta W W'' + \lambda(B - W\cdot C - \eta (W')^2) + \gamma (\lambda')^2 \right] dz$$

| Term | Meaning | Upgrade from v0.1 |
|------|---------|-------------------|
| $W \cdot C$ | Consistency cost | Unchanged |
| $\alpha (W')^2$ | Stiffness cost | Unchanged |
| $\beta W W''$ | Curvature cost | Unchanged |
| $\lambda(B - W\cdot C - \eta (W')^2)$ | Budget constraint with velocity penalty | **λ is field, η·(W')² is new** |
| $\gamma (\lambda')^2$ | λ kinetic term | **New — makes λ dynamical** |

## 2. Euler-Lagrange Equation for W(z)

$$\frac{\partial L}{\partial W} - \frac{d}{dz}\frac{\partial L}{\partial W'} + \frac{d^2}{dz^2}\frac{\partial L}{\partial W''} = 0$$

$$\Rightarrow C(z)(1 - \lambda) + (\beta - 2\alpha + 2\eta\lambda) W''(z) + 2\eta \lambda' W'(z) = 0$$

## 3. Euler-Lagrange Equation for λ(z)

$$\frac{\partial L}{\partial \lambda} - \frac{d}{dz}\frac{\partial L}{\partial \lambda'} = 0$$

$$\Rightarrow 2\gamma \lambda'' = B - W \cdot C - \eta (W')^2$$

## 4. Equilibrium (No Drift)

When $\lambda' = 0$ and $\lambda'' = 0$ (equilibrium):

**λ EoM:** $B = W \cdot C + \eta (W')^2$ — budget perfectly balanced

**W EoM:** $C(1 - \lambda) = (2\alpha - \beta - 2\eta\lambda) W''$

$$\Rightarrow \kappa_\text{eff} = \frac{2\alpha - \beta - 2\eta\lambda}{1 - \lambda}$$

κ is now **parametrized by λ**, not a bare constant. The self-consistent λ solves both equations simultaneously.

## 5. Physical Interpretation

- $\lambda(z)$ = **information flow price** — marginal cost of compute reallocation
- $\eta (W')^2$ = **velocity penalty** — cost of changing W too fast (non-holonomic)
- $\gamma (\lambda')^2$ = **λ kinetics** — ensures λ is dynamical, not ad-hoc
- Budget mismatch $B - W\cdot C$ drives $\lambda''$ — λ adjusts to restore balance

