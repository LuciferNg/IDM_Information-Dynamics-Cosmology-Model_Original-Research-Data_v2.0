# Report: P6 — DM-Free Galaxies (Entropy Solidification)

> **Project ID:** IDM-EXT-P6  
> **Date:** 2026-07-01 (honest version)  
> **Core Claim:** DM-deficient galaxies form via entropy solidification during sync dip recovery — but magnitude is INCOMPATIBLE with IDM perturbation scale

---

## 1. Qualitative Mechanism (Physically Plausible)

During sync dip recovery (z < 0.6), the cosmic W is recovering from its dip minimum at z_c ≈ 0.6. A galaxy merger at z < 0.6 adds extra sync bandwidth demand, SUPPRESSING the local W value. This reduces the local braiding parameter α_B(x) < α_B(z), producing G_eff/G_N < 1 (reduced gravitational coupling).

The sign is now CORRECTED: merger during dip recovery → **reduced** G_eff (not enhanced).

**Three falsifiable qualitative predictions:**
1. DM-deficient galaxies form at z < 0.6 (post-dip recovery regime)
2. Mergers at z > 0.6 (pre-dip) should show **enhanced** G_eff → DM-overabundant
3. Dry (gas-poor) mergers produce larger effect than wet mergers

---

## 2. Quantitative Barrier (Critical)

The IDM perturbation framework places a strict bound on the correction magnitude:

| Scale | ε = α/√N | Max Δα_B | Max ΔG_eff/G_N |
|:------|:--------:|:--------:|:--------------:|
| Cosmic (N_horizon = 44) | 0.1545 | ±0.155 | ±15% |
| Galaxy (N_eddies = 10⁶) | 0.001 | ±0.001 | ±0.1% |

**To match DF2 (σ = 7 km/s vs σ_bary ≈ 8.1 km/s):**

| Quantity | Value |
|:---------|:-----|
| Needed σ_obs / σ_bary | 0.864 → G_eff/G_N ≈ 0.746 |
| Required Δα_B | ≈ −0.24 |
| Ratio to ε_cosmic | **1.6×** (exceeds IDM bound) |
| Ratio to ε_gal | **230×** (far exceeds galaxy bound) |

**Conclusion: P6 cannot quantitatively explain DF2 within the IDM perturbation framework.** The correction scale is too small at galaxy level (ε_gal ≈ 0.001) and even at cosmic level (ε_cosmic ≈ 0.155) it falls short by a factor of 1.6–3×.

---

## 3. Sign Correction Note

The original analysis (uncorrected) predicted **enhanced** G_eff (merger → more braiding → extra attraction). This was the WRONG sign. The corrected mechanism gives **reduced** G_eff (dip recovery + merger → suppressed braiding → weaker gravity). The sign correction stands, but the magnitude problem is independent of the sign.

---

## 4. NGC 1052-DF4 Prediction

| Property | DF4 | DF2 |
|:---------|:---:|:---:|
| M_star | 1.5×10⁸ M☉ | 2×10⁸ M☉ |
| R_eff | 1.5 kpc | 2.2 kpc |
| σ_obs | ~10 km/s | ~7 km/s |
| σ_bary (isotropic) | 9.6 km/s | 8.1 km/s |
| σ_obs/σ_bary | 1.04 (ΛCDM-consistent) | 0.86 (DM-deficient) |

DF4 does NOT show significant DM deficiency, consistent with tidal stripping rather than modified gravity. If the IDM mechanism were dominant, DF4 should also show DM deficiency (given its similar merger origin). **This observation favors the standard tidal stripping explanation.**

---

## 5. Results Summary

| Target | Result | Status |
|:-------|:-------|:------|
| T1: Entropy solidification operator | Δα_B(r) formalism defined | ✅ Formal |
| T2: Merger entropy budget | Qualitatively dS_merge > dS_bg | ✅ Plausible |
| T3: Gravitational potential | Mechanism gives G_eff < G_N (corrected sign) | ✅ Direction |
| T4: DF2 rotation curve | σ_pred ≈ 8.09 km/s (IDM-consistent, ε_gal scale) | ❌ Cannot explain 7 km/s |
| T5: Predict DM-deficient types | 3 qualitative conditions | ✅ Valid |
| T6: Failure conditions | 3 failure modes + z-condition | ✅ Valid |

---

## 6. Conclusion

**P6 provides a qualitatively plausible mechanism linking DM deficiency to IDM sync dip recovery, but QUANTITATIVELY INSUFFICIENT within the IDM perturbation framework.**

The sign-corrected mechanism (reduced G_eff during z < 0.6 dry mergers) is physically sound as a direction. The falsifiable predictions (z-dependent DM distribution, merger-type dependence) remain valid tests of the framework.

However, the magnitude of G_eff reduction needed to explain DF2 (≈ 25% reduction in σ) is 1.6–3× larger than the IDM perturbation scale allows. At galaxy scale (ε_gal ≈ 0.001), the IDM-consistent correction to σ is < 0.1% — undetectable.

**The way forward:**
1. Identify non-perturbative enhancement mechanisms within IDM for galaxy scales
2. Or accept P6 as a qualitative framework with quantitative predictions pending a non-linear treatment
3. The z-dependent predictions (z < 0.6 → DM-deficient, z > 0.6 → DM-overabundant) are the strongest tests and should be pursued observationally with DESI and JWST

### Files
- `p6_derivation.py` — honest physical analysis with perturbation bounds
- `p6_field_theory.py` — field-theoretic Δα_B(r) operator, dimensional analysis
- `TASK_SPEC_CONTRACT.md` — task specification with honest conclusion