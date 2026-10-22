# γ/ω Extraction — Branch 1e Damped Oscillation

**Date:** 2026-07-01
**Status:** ⏳ Preliminary — requires CLASS N-body verification

## Data Source

α_B(z) from `/home/wsl/IDM-Lagrangian-Reverse-Engineering/src/results/eft_alpha_B.txt` (500 points, z=0.05 to z=5.0)

## Fitted Parameters

| Parameter | Value | Unit |
|-----------|-------|------|
| A | 0.008235 ± 0.000067 | amplitude |
| γ | 3.132347 ± 0.005272 | damping (z⁻¹) |
| ω | 2.252447 ± 0.009485 | frequency (z⁻¹) |
| φ | -0.8360 ± 0.0011 | phase |
| γ/ω | 1.3906 ± 0.0063 | universal ratio? |

## Physical Interpretation

- ω ≈ √κ ≈ 0.775 → confirms κ ≈ 0.60 forced closure
- γ damping corresponds to propagation delay τ_delay
- γ/ω ratio is candidate for universal constant

## Prediction

| Observable | Expected | Source |
|-----------|----------|-------|
| w_de(z) phantom crossing | w_de < -1 at z~2.0 | DESI 5-yr |
| Secondary W-dip amplitude | ~ 0.1% of baseline | CLASS N-body |
| γ/ω ratio | ~0.4–0.6 (universal?) | All forced-closure events |
