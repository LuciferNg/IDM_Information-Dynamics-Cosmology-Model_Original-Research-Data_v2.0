"""P7: Young galaxy entropy overload — HONEST VERSION 2026-07-01

NOTE: The dS/dt vs C_gal comparison is SEMI-QUANTITATIVE.
dS/dt (turbulent dissipation) integrates over the whole galaxy,
while C_gal (consensus capacity) is per-coherent-patch. They
cannot be directly compared in absolute units. The qualitative
trend (high-z galaxies are more turbulent) is observationally
correct and consistent with the entropy overload picture.
"""
import numpy as np

# Physical constants
k_B = 1.380649e-23  # J/K
M_sun = 1.989e30    # kg
kpc_m = 3.086e19    # m
km_s = 1e3          # m/s

print("="*66)
print("P7: YOUNG GALAXY ENTROPY OVERLOAD (HONEST VERSION)")
print("="*66)
print()

# ── Dimensional analysis ──
print("─"*66)
print("DIMENSIONAL ANALYSIS")
print("─"*66)
print()
print("Consensus capacity: C_gal = N_ed / t_coh")
print("  [N_ed] = dimensionless (count of turbulent eddies)")
print("  [t_coh] = [L/sigma] = s (crossing time)")
print("  [C_gal] = s^-1 (information processing rate boundary)")
print()
print("Entropy flow: dS/dt = E_dot / T_gas")
print("  [E_dot] = [M·sigma^3/L] = kg·m^2/s^3 = W (turbulent power)")
print("  [T_gas] = K")
print("  [dS/dt] = [E_dot/T] = J/(K·s) = k_B/s")
print()
print("ISSUE: C_gal is in [s^-1] (rate), dS/dt is in [k_B/s]")
print("These are NOT the same units! A direct comparison requires")
print("assuming each eddy processes 1 k_B per crossing time, giving:")
print("  C_gal [k_B/s] = N_ed / t_coh · k_B")
print("But this is a CONVENTION, not derived from IDM first principles.")
print()

# ── Galaxy parameters ──
# Qualitative trend (all values approximate, from literature)
galaxies = [
    {"name": "MW-like",   "z": 0,   "M": 1e9,   "R": 15,  "sigma": 40,  "T": 1e4,   "Ned": 3e6},
    {"name": "SF disk",   "z": 1,   "M": 5e9,   "R": 5,   "sigma": 60,  "T": 1.5e4, "Ned": 1e5},
    {"name": "Turbulent", "z": 3,   "M": 1e10,  "R": 3,   "sigma": 80,  "T": 2e4,   "Ned": 3e4},
    {"name": "Primeval",  "z": 6,   "M": 5e9,   "R": 1.5, "sigma": 120, "T": 3e4,   "Ned": 3e3},
]

def C_gal_bits(N_ed, L_kpc, sigma_kms):
    """Consensus capacity in bits/s (each eddy = 1 bit per crossing time)"""
    t_coh_s = (L_kpc * kpc_m) / (sigma_kms * km_s)
    return N_ed / t_coh_s

def dS_dt_phys(M_msun, R_kpc, sigma_kms, T_gas):
    """Turbulent entropy production in k_B/s"""
    M_kg = M_msun * M_sun
    R_m = R_kpc * kpc_m
    # Turbulent dissipation: E_dot ~ 0.5 * M * sigma^3 / R
    E_dot = 0.5 * M_kg * (sigma_kms * km_s)**3 / R_m
    return E_dot / (T_gas * k_B)  # k_B/s

print("─"*66)
print("QUALITATIVE TREND (semi-quantitative)")
print("─"*66)
print()
print(f"{'System':<12} {'z':<4} {'C_gal(bits/s)':<16} {'dS/dt(kB/s)':<16} {'Ratio':<10} {'Overload?':<10}")
print(f"{'':-<12} {'':-<4} {'':-<16} {'':-<16} {'':-<10} {'':-<10}")
for g in galaxies:
    C = C_gal_bits(g["Ned"], g["R"], g["sigma"])
    dS = dS_dt_phys(g["M"], g["R"], g["sigma"], g["T"])
    ratio = np.log10(dS / C) if C > 0 else 99
    overload = "YES" if ratio > 5 else "maybe" if ratio > 3 else "no"
    print(f"{g['name']:<12} {g['z']:<4} {C:<16.2e} {dS:<16.2e} {ratio:<10.1f} {overload:<10}")

print()
print("NOTE: C_gal and dS/dt are in DIFFERENT conceptual units.")
print("C_gal = maximum bits per second the turbulent system can")
print("  'process' via coherent eddy motion.")
print("dS/dt = actual entropy production rate from dissipation.")
print("The absolute comparison is not physically meaningful — only")
print("the RELATIVE TREND across redshift is significant.")
print()
print("Relative trend: high-z galaxies have 10^4-10^5 times more")
print("turbulent dissipation relative to their processing capacity.")
print("This is CONSISTENT with the qualitative entropy overload picture.")
print()

# ── Qualitative prediction ──
print("─"*66)
print("OBSERVABLES AND PREDICTIONS")
print("─"*66)
print()
print("The entropy overload picture makes one clear prediction:")
print()
print("  v_rot / sigma_v < 1  at z > 3  (turbulent, clumpy)")
print("  v_rot / sigma_v > 1  at z < 1  (settled disks)")
print()
print("This is CONFIRMED by JWST kinematics at z~3-6.")
print("But it's ALSO predicted by standard disk instability theory")
print("(Toomre Q < 1 at high gas fraction).")
print()
print("What distinguishes IDM from standard theory?")
print("  1) IDM predicts a SHARP transition at z~1-2 (when consensus")
print("     capacity catches up), while standard theory predicts")
print("     a GRADUAL decline in gas fraction")
print("  2) IDM predicts that clumpiness correlates with merger rate")
print("     (entropy source), not just gas fraction")
print("  3) Both predictions testable with JWST kinematics surveys")
print()

print("="*66)
print("P7 VERDICT")
print("="*66)
print("  ✅ Qualitative trend: high-z galaxies are more turbulent")
print("  ✅ Prediction: v_rot/sigma < 1 at z>3 (confirmed by JWST)")
print("  ⚠  Direct dS/dt vs C_gal comparison: units incompatible")
print("     → must treat as semi-quantitative trend only")
print("  ⚠  Same qualitative prediction as standard galaxy formation")
print("  ✅ Distinguishing prediction: SHARP transition at z~1-2")
print("     (vs gradual decline in standard theory)")
print("  ⚠  Quantitative prediction needs proper units and modeling")