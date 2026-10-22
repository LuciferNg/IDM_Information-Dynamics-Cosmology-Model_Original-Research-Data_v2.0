"""P6: DM-free galaxies — entropy solidification (HONEST VERSION 2026-07-01)

PHYSICAL VERDICT:
The qualitative mechanism (sync dip recovery + merger entropy → local gravity 
modification) is physically plausible within the IDM Horndeski framework. However,
QUANTITATIVELY, the required G_eff suppression (≈ 64% of G_N) exceeds the IDM
perturbation scale ε_cosmic ≈ 0.155 by a factor of 3×.

At galaxy scale: ε_gal = α/√N_gal ≈ 0.001 (from turbulent eddies, P7)
This gives a maximum IDM correction of ≈ 0.1% at galaxy scales.

CONCLUSION: P6 provides a qualitative mechanism for DM-deficient galaxies but 
CANNOT quantitatively explain the ≈40% G_eff reduction needed for NGC 1052-DF2
within the IDM perturbation framework. The mechanism may require non-perturbative 
enhancement or an alternative channel not captured by the current linear analysis.
"""
import numpy as np

print("="*66)
print("P6: DM-FREE GALAXIES — ENTROPY SOLIDIFICATION (HONEST VERSION)")
print("="*66)
print()

# ── IDM perturbation scale ──
eps_cosmic = 0.1545  # from MCMC: ε = α/√N_horizon
alpha = 1.025
N_horizon = 44

# Galaxy-scale epsilon from turbulent eddies
N_gal_eddies = int(1e6)  # from P7
eps_gal = alpha / np.sqrt(N_gal_eddies)

print("─"*66)
print("SCALE ANALYSIS: IDM perturbation bounds")
print("─"*66)
print(f"  Cosmic ε = α/√N_horizon = {eps_cosmic:.4f} (from N_horizon={N_horizon})")
print(f"  Galaxy ε_gal = α/√N_eddy = {eps_gal:.6f} (from N_eddies=10⁶)")
print(f"  Ratio ε_cosmic / ε_gal = {eps_cosmic/eps_gal:.0f}x")
print()

# ── DF2: what would IDM-consistent correction give? ──
# With ε_gal ≈ 0.001, the maximum Δα_B from galaxy-scale IDM corrections is:
max_dalpha_gal = eps_gal  # O(ε) correction to α_B
alpha_b_bg = 0.15

def G_eff_ratio(alpha_B, alpha_K=1.0):
    return (1 + alpha_B/(1+alpha_B)) / (1 + alpha_K/(6*(1+alpha_B)**2))

# Baryonic-only prediction for DF2
# Using Plummer model: M(<R_1/2) ≈ 0.5 × M_total (half-mass within half-light)
M_star_DF2 = 2.0e8  # M_sun
R_eff_DF2 = 2.2  # kpc
sigma_bary = np.sqrt(0.5 * 4.3009e-3 * M_star_DF2 / (R_eff_DF2 * 1000) / 3)  # isotropic
print(f"─"*66)
print(f"DF2: BARYONIC BASELINE")
print(f"─"*66)
print(f"  M_star = {M_star_DF2:.1e} M_sun")
print(f"  R_eff = {R_eff_DF2:.1f} kpc")
print(f"  Keplerian v_circ(R_eff) = {np.sqrt(4.3009e-3*M_star_DF2/(R_eff_DF2*1000)):.1f} km/s")
print(f"  Baryonic dispersion (isotropic) = {sigma_bary:.1f} km/s")
print(f"  Observed dispersion = 7 km/s")
print(f"  DM-deficient ratio = {7/sigma_bary:.2f} (σ_obs/σ_bary)")
print()

# IDM correction at galaxy scale (ε_gal scale)
dalpha_idm = eps_gal  # maximum IDM-consistent correction
print(f"─"*66)
print("IDM-CONSISTENT PREDICTION (within perturbation theory)")
print("─"*66)
print(f"  Maximum galaxy-scale Δα_B = ±{dalpha_idm:.6f}")
for sign in [+1, -1]:
    ab_mod = alpha_b_bg + sign * dalpha_idm
    gr = G_eff_ratio(ab_mod)
    sigma_idm = sigma_bary * np.sqrt(gr)
    print(f"  Δα_B = {sign*dalpha_idm:+.6f} → α_B = {ab_mod:.4f}")
    print(f"    G_eff/G_N = {gr:.6f}")
    print(f"    σ_pred = {sigma_idm:.2f} km/s")
    print(f"    vs observed 7 km/s → {(sigma_idm/7 - 1)*100:+.1f}% off")
    print()

print(f"─"*66)
print("QUANTITATIVE BARRIER")
print("─"*66)
print(f"  Required Δα_B ≈ -0.48 to match DF2 from first principles")
print(f"  IDM-consistent maximum |Δα_B| = ε_gal = {eps_gal:.6f}")
print(f"  Gap: |Δα_B_needed| / ε_gal = {0.48/eps_gal:.0f}x")
print()
print(f"  Even using cosmic ε_cosmic = {eps_cosmic:.4f}:")
print(f"    |Δα_B_needed| / ε_cosmic = {0.48/eps_cosmic:.1f}x")
print(f"  → P6 requires a correction 3× the cosmic IDM perturbation scale.")
print()

# ── Qualitative mechanism ──
print("="*66)
print("QUALITATIVE MECHANISM (physically sound)")
print("="*66)
print()
print("The sign-corrected mechanism is PHYSICALLY PLAUSIBLE:")
print("  1. Sync dip recovery (z < 0.6): W is recovering from dip minimum")
print("  2. Galaxy merger adds sync cost demand → local W suppressed")
print("  3. This modifies the local braiding: α_B(x) < α_B(z)")  
print("  4. Reduced braiding → G_eff < G_N → DM-deficient appearance")
print()
print("This mechanism makes THREE falsifiable qualitative predictions:")
print("  a) DM-deficient galaxies should form at z < 0.6 (post-dip recovery)")
print("  b) At z > 0.6, mergers should produce ENHANCED G_eff")
print("     → DM-overabundant galaxies (G_eff > G_N)")
print("  c) Dry (gas-poor) mergers produce larger effect than wet mergers")
print()

# ── DF4 prediction ──
print("─"*66)
print("PREDICTION: NGC 1052-DF4")
print("─"*66)
print("  Same host group (NGC 1052) → similar formation environment")
print("  Tidal features detected → consistent with recent merger origin")
print()
print("  IDM prediction (qualitative):")
print("    σ_DF4 < σ_bary (DM-deficient) but less extreme than DF2")
print("    Reason: DF4 is closer to NGC 1052 → more tidal stripping")
print("    → standard tidal explanation may dominate over IDM effect")
print()
print("  If IDM contribution is ε_gal ≈ 0.001 scale:")
print("    Δσ/σ_bary < 0.1% → undetectable with current instrumentation")
print("  If non-perturbative enhancement exists:")
print("    Δσ/σ_bary ∼ few% → potentially detectable but model-dependent")
print()

print("="*66)
print("P6 VERDICT")
print("="*66)
print("  ✅ Qualitative mechanism: plausible and internally consistent")
print("  ⚠️  Quantitative magnitude: INCOMPATIBLE with IDM perturbation scale")
print("  ❌ Cannot claim DF2 'fit' — parameters were chosen, not predicted")
print("  ✅ Qualitative predictions (z-dependent DM, merger conditions): valid")
print("  ❌ DF4 prediction: signal below detectability unless non-perturbative")
print()
print("The way forward: identify non-perturbative enhancement mechanisms")
print("within IDM that could amplify ε_gal at galaxy scales, or accept")
print("that P6 explains the DIRECTION but not the MAGNITUDE of DM deficiency.")
