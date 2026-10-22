# Report: P7 — Young Galaxy Entropy Overload (HONEST VERSION)

> **Project ID:** IDM-EXT-P7  
> **Date:** 2026-07-01  
> **Core Claim:** High-z (z>2) galaxies have more turbulent dissipation → entropy overload → clumpy morphology

---

## 1. What Works (Qualitative)

The trend is OBSERVATIONALLY CONFIRMED:
- z > 3 galaxies: v_rot/σ < 1 (turbulent, clumpy) ✅ JWST/ALMA
- z < 1 galaxies: v_rot/σ > 1 (settled disks) ✅
- Transition at z ~ 1-2 ✅

---

## 2. Units Incompatibility (Critical Issue)

| Quantity | Formula | Units | Physical Meaning |
|:---------|:--------|:-----|:-----------------|
| Consensus capacity | $C_{\rm gal} = N_{\rm ed} \cdot \sigma/L$ | $\text{s}^{-1}$ | Max coherence events per second |
| Entropy flow | $dS/dt = 0.5 \cdot M\sigma^3/(L T)$ | $k_B \cdot \text{s}^{-1}$ | Turbulent entropy production |

**The problem:** $C_{\rm gal}$ and $dS/dt$ have incompatible units. Converting either to match the other requires an arbitrary scale factor (how many k_B per coherence event?) that has no IDM-first-principles derivation.

The absolute comparison $dS/dt > C_{\rm gal}$ always yields "overload" by ~$10^{60}$ regardless of redshift — because turbulent dissipation is MACROSCOPIC while eddy coherence is KINEMATIC.

---

## 3. What IDM Actually Predicts

The relative trend (high-z vs low-z) is physically meaningful and consistent:

| Redshift | Relative dS/dt | Relative C_gal | dS/dt : C_gal ratio scaling |
|:--------:|:--------------:|:--------------:|:---------------------------:|
| 0 | 1× | 1× | baseline |
| 1 | 50× | 0.15× | ~330× increase |
| 3 | 400× | 0.1× | ~4000× increase |
| 6 | 1350× | 0.03× | ~45000× increase |

The ratio dS/dt : C_gal increases by **4-5 orders of magnitude** from z=0 to z>3. This is the meaningful quantity — the **relative** entropy overload.

---

## 4. Distinguishing IDM from Standard Theory

Both IDM and standard galaxy formation predict clumpy high-z galaxies (Toomre instability at high gas fraction). IDM's unique predictions:

| Test | IDM | Standard Theory |
|:-----|:---|:---------------|
| z-transition sharpness | **Sharp** (capacity catches up) | Gradual (gas fraction declines) |
| Clumpiness driver | Merger rate + gas turbulence | Gas fraction + Toomre Q |
| Signature | Correlation with merger history | Correlation with gas fraction |

These are TESTABLE with JWST kinematics surveys (e.g., PHANGS-JWST, ALMA large programs).

---

## 5. Results Summary

| Target | Result | Honest Assessment |
|:-------|:-------|:-----------------|
| T0: Consensus capacity $C_{\rm gal}$ | $C = N_{\rm ed}/t_{\rm coh}$ | ✅ Formally defined |
| T1: $N_{\rm gal}$ scaling | $N_{\rm eff} \sim 10^6$ (eddies) | ✅ Physically motivated |
| T2: Gas entropy flow | $dS/dt = f(\sigma_v, \rho, T)$ | ✅ Standard turbulence |
| T3: High-z/low-z ratio | $10^4-10^5\times$ more at z>3 | ✅ Robust |
| T4: Overload threshold | $dS/dt : C_{\rm gal}$ ratio ↑ | ⚠️ Units incompatible for absolute threshold |
| T5: Observable signatures | $v_{\rm rot}/\sigma < 1$ | ✅ Confirmed by JWST |
| T6: z-transition | z~1-2 consensus builds | ✅ Consistent with data |
| T7: Self-regulation | Feedback cycles | ✅ Standard astrophysics |

## 6. Conclusion

The qualitative picture (high-z galaxies are turbulence-dominated → clumpy) is OBSERVATIONALLY CORRECT and consistent with IDM's entropy-overload language. However:

1. **The absolute dS/dt > C_gal comparison is not physically well-defined** due to unit incompatibility
2. **The qualitative trend is the same as standard disk instability theory** (Toomre Q < 1)
3. **IDM's distinguishing predictions** (sharp transition, merger-rate correlation) are POTENTIALLY testable but have not been validated
4. **The eddy localization argument** (N_eff ~ 10⁶ instead of 10⁶⁸) is physically motivated but not derived from IDM first principles

**Proposed next step:** Conduct a survey of JWST kinematics that tests the sharpness of the v_rot/σ transition at z~1-2 — IDM predicts a sharper transition than standard gas-fraction evolution.

### Files
- `p7_derivation.py` — honest version with unit analysis
- `TASK_SPEC_CONTRACT.md` — task specification with honest conclusion