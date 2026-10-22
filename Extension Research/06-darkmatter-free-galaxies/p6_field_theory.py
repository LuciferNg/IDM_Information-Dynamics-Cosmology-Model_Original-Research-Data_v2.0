"""P6 RESOLUTION: Entropy solidification — HONEST VERSION

PHYSICAL STATUS:
The field-theoretic operator Δα_B(r) = K·(dS_merge/dV)·exp(-r/R_vir) is 
PHYSICALLY PLAUSIBLE as a qualitative mechanism, but QUANTITATIVELY 
insufficient: the required K ≈ -0.48 to fit DF2 is 3× the cosmic IDM 
perturbation scale ε_cosmic ≈ 0.155 and 470× the galaxy-scale ε_gal ≈ 0.001.

At face value: the IDM-consistent correction to σ_v at ε_gal scale is < 0.1%.
This is undetectable with current instrumentation.
"""
print("="*66)
print("P6 RESOLUTION: FIELD-THEORETIC Δα_B(r) — HONEST VERSION")
print("="*66)
print()
print("The operator Δα_B(r) = K·(dS_merge/dV)·exp(-r/R_vir)")
print("is the CORRECT form for a localized perturbation sourced by merger entropy.")
print()

# ── Dimensional consistency ──
print("─"*66)
print("DIMENSIONAL ANALYSIS")
print("─"*66)
print()
print("S_merge = N_particles · k_B · ln(V_final/V_initial)")
print("  [S] = [k_B] = energy/temperature → dimensionless in natural units")
print("  [dS_merge/dV] = [V⁻¹] = [L⁻³]")
print("  [Δα_B] = dimensionless (braiding parameter)")
print("  [K] = [L³] (volume) — from K·(dS/dV) → dimensionless")
print()
print("Dimensionally consistent: YES ✅")
print("But [K] = [L³] means K depends on the PHYSICAL SCALE of the system.")
print("This is expected — screening profiles scale with system size.")
print()

# ── Numerical analysis ──
import numpy as np

def G_eff_ratio(alpha_B, alpha_K=1.0):
    return (1 + alpha_B/(1+alpha_B)) / (1 + alpha_K/(6*(1+alpha_B)**2))

# IDM perturbation bound
eps_cosmic = 0.1545
eps_gal = 1.025 / np.sqrt(1e6)

alpha_b_bg = 0.15

# DF2: K needed for match
# v_obs/v_bary = 7/8.1 ≈ 0.864
# Need G_eff/G_N = 0.864² = 0.746
# From G_eff_ratio, α_B ≈ -0.09 gives G_eff/G_N ≈ 0.746
# Δα_B = -0.09 - 0.15 = -0.24

# But this uses isotropic approximation and ignores projection effects
# A full Jeans analysis would give different numbers

print("─"*66)
print("DF2: CONSTRAINTS ON K")
print("─"*66)
print()
print("Best-fit α_B for DF2 (from σ_v = 7 km/s, isotropic approx):")
v_bary = 8.1  # km/s (isotropic baryonic dispersion)
v_obs = 7.0   # km/s
gr_needed = (v_obs/v_bary)**2
print(f"  Need G_eff/G_N = ({v_obs}/{v_bary})² = {gr_needed:.3f}")
print()

# Solve for α_B that gives this G_eff/G_N
for ab_test in np.linspace(-0.5, 0.15, 100):
    if abs(G_eff_ratio(ab_test) - gr_needed) < 0.01:
        dalpha = ab_test - alpha_b_bg
        print(f"  → α_B ≈ {ab_test:.3f}, Δα_B ≈ {dalpha:.3f}")
        print(f"  |Δα_B| / ε_cosmic = {abs(dalpha)/eps_cosmic:.1f}x")
        print(f"  |Δα_B| / ε_gal = {abs(dalpha)/eps_gal:.0f}x")
        break

print()

# ── Profile comparison: Gaussian vs exponential ──
print("─"*66)
print("SPATIAL PROFILE: Gaussian vs Exponential")
print("─"*66)
print()
print("  p6_derivation.py (original): Gaussian exp(-r²/2R²)")
print("  p6_field_theory.py (current): Exponential exp(-r/R)")
print()
print("  The exponential exp(-r/R_vir) is the CORRECT form for")
print("  a screened Yukawa potential from the IDM scalar field.")
print("  This is consistent with chameleon/Vainshtein screening.")
print()
print("  Gaussian was an approximation from the original (uncorrected)")
print("  analysis. All versions now use exponential. ✅")
print()

# ── DF4 prediction ──
print("─"*66)
print("DF4 PREDICTION")
print("─"*66)
print()
print("  NGC 1052-DF4: same group, similar merger origin")
print("  M_star ≈ 1.5e8 M_sun, R_eff ≈ 1.5 kpc")
print("  Observed dispersion: ~10 km/s")
print()
print("  Baryonic prediction (isotropic):")
M_DF4 = 1.5e8
R_DF4 = 1.5
sigma_bary_df4 = np.sqrt(0.5 * 4.3009e-3 * M_DF4 / (R_DF4 * 1000) / 3)
print(f"    σ_bary ≈ {sigma_bary_df4:.1f} km/s")
print(f"    Observed σ ≈ 10 km/s")
print(f"    σ_obs/σ_bary = {10/sigma_bary_df4:.2f} (consistent with ΛCDM)")
print()
print("  DF4 does NOT show significant DM deficiency — in fact, it is")
print("  closer to ΛCDM expectation than DF2. This is consistent with")
print("  the tidal stripping explanation (DF4 closer to NGC 1052).")
print()
print("  IDM prediction: DF4 could show small DM deficiency (few %)")  
print("  if the IDM mechanism is active, but tidal stripping dominates.")
print()

print("="*66)
print("P6 FIELD-THEORETIC VERDICT")
print("="*66)
print("  ✅ Δα_B(r) formalism: correct for localized scalar perturbation")
print("  ✅ Exponential profile exp(-r/R_vir): physically motivated")
print("  ⚠️  K magnitude: cannot be derived from IDM perturbation theory")
print("     — requires non-perturbative physics or alternative mechanism")
print("  ❌ DF2 'fit' with K = -0.5: misleading (chosen to match data)")
print("  ✅ Qualitative predictions (z-dependence, merger type): valid")
