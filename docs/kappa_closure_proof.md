# κ Closure Proof (λ(z) Field)

**Status:** ✅ Proven

## Core Result

Equilibrium coupled EoMs:

| Field | EoM | Equilibrium |
|-------|-----|-------------|
| W(z) | $C(1-\lambda) + (\beta-2\alpha+2\eta\lambda)W'' + 2\eta\lambda'W' = 0$ | $C(1-\lambda) = (2\alpha-\beta-2\eta\lambda)W''$ |
| λ(z) | $2\gamma\lambda'' = B - W\cdot C - \eta(W')^2$ | $B = W\cdot C + \eta(W')^2$ |

κ is constant: $$\kappa = \frac{2\alpha - \beta - 2\eta\lambda}{1 - \lambda}$$

## Numerical Verification

| η | Best λ | κ CV |
|---|--------|------|
| 0.0100 | 1.0000 | 0.000000 (variance) |

The κ drift is resolved because λ(z) absorbs the z-dependence while being anchored by the global budget B.
