"""Run CLASS properly for Branch 1e — using existing classy + IDM Hubble tables."""
import numpy as np
import sys, os, subprocess
from scipy.interpolate import interp1d

sys.path.insert(0, os.path.expanduser("~/IDM-Lagrangian-Reverse-Engineering"))
from src.hubble import H0, Omega_m, Omega_r, Omega_L, eps, zc

# ── W(z) models ──
def W_lcdm(z): return 1.0

def W_baseline(z):
    x = z / zc
    return 1 - eps * x * np.exp(-x)

A, gamma, omega, phi = 0.008, 3.13, 2.25, -0.836
def W_osc_raw(z):
    x = z / zc
    base = 1 - eps * x * np.exp(-x)
    osc = A * np.exp(-gamma * (z - zc)) * np.cos(omega * (z - zc) + phi)
    return base + osc

z0 = 1e-6
osc_offset = 1.0 - W_osc_raw(z0)
def W_osc(z): return W_osc_raw(z) + osc_offset

# ── Generate H(z) tables for each model ──
# H(z)²/H₀² = Ω_m(1+z)³ + Ω_r(1+z)⁴ + Ω_L·W(z)
def H2_norm(z, W_func):
    return Omega_m*(1+z)**3 + Omega_r*(1+z)**4 + Omega_L*W_func(z)

z_arr = np.logspace(-3, 2, 5000)

print("="*60)
print("BRANCH 1e — CLASS N-body with IDM Hubble tables")
print("="*60)

# Generate tables
for name, Wf in [("lcdm", W_lcdm), ("baseline", W_baseline), ("osc", W_osc)]:
    h2 = np.sqrt(H2_norm(z_arr, Wf))
    # Convert to CLASS background format: z, H(z)/H0
    tbl = np.column_stack([z_arr, h2])
    out = os.path.expanduser(f"~/IDM-Consistency-Importance-Weight/results/branch1e/H_{name}.txt")
    np.savetxt(out, tbl, header="z\tH/H0")
    print(f"  {name}: H(z) table saved ({len(tbl)} points)")

# ── Prepare CLASS parameter file ──
# CLASS can read background via its 'background' module with custom H(z) file
# Use: H(z) tables via the custom background parameterization
# In classy: 'custom1' with 'custom1_filename'

from classy import Class

def run_class_custom(W_name, label, W_func, lmax=2000):
    """Run CLASS with custom H(z) background."""
    M = Class()
    
    h2_tbl = os.path.expanduser(f"~/IDM-Consistency-Importance-Weight/results/branch1e/H_{W_name}.txt")
    data = np.loadtxt(h2_tbl)
    z_tab, h_tab = data[:, 0], data[:, 1]
    
    # CLASS needs the background as custom: z, H(z)/H0, d(H/H0)/dz
    # Compute derivative
    dh_dz = np.gradient(h_tab, z_tab)
    custom_tbl = np.column_stack([z_tab, h_tab, dh_dz])
    
    custom_path = f"/tmp/class_custom_{W_name}.txt"
    np.savetxt(custom_path, custom_tbl)
    
    M.set({
        'output': 'tCl pCl lCl',
        'l_max_scalars': lmax,
        'lensing': 'yes',
        'N_ur': 3.046,
        
        # Use custom background
        'custom1_filename': custom_path,
        'custom1_format': '0.1',  # z, H/H0, d(H/H0)/dz
        
        # Set Omega values to match IDM (custom background handles the rest)
        'h': H0/100.0,
        'omega_b': 0.02237,
        'omega_cdm': 0.1200,
        
        # Reionization
        'tau_reio': 0.0544,
        
        # Primordial
        'A_s': 2.1e-9,
        'n_s': 0.9649,
        
        # Matter power
        'P_k_max_h/Mpc': 10.0,
        'z_max_pk': 4.0,
    })
    
    try:
        M.compute()
        cls = M.lensed_cl(lmax)
        print(f"  {label}: ✅ compute() succeeded, {len(cls)} Cℓ values")
        return cls, M
    except Exception as e:
        err_msg = str(e)[:300]
        print(f"  {label}: ❌ compute() failed — {err_msg}")
        return None, M

print(f"\n─── Running CLASS (this takes ~30s per model) ───")

results = {}
for key, name, wf in [("lcdm", "lcdm", W_lcdm), 
                        ("baseline", "baseline", W_baseline),
                        ("osc", "osc", W_osc)]:
    print(f"\n  🔄 {name}...")
    cls, M = run_class_custom(key, name, wf)
    results[key] = {"cls": cls, "M": M}

# ── Compute χ² estimates ──
print(f"\n{'='*60}")
print("χ² ANALYSIS")
print("="*60)

if results["lcdm"]["cls"] is not None and results["osc"]["cls"] is not None:
    cls_lcdm = results["lcdm"]["cls"]
    cls_osc = results["osc"]["cls"]
    
    # Match ell values
    ell_common = np.intersect1d(list(cls_lcdm.keys()), list(cls_osc.keys()))
    ell_vals = np.array([int(k.split('_')[1]) if '_' in k else int(k) for k in cls_lcdm.keys() if k.startswith('tt')][:100])
    
    # Compare Cℓ ratios
    print("\nCℓ ratio: Cℓ(osc) / Cℓ(ΛCDM) at selected ℓ:")
    tt_lcdm = [(int(k.split('_')[1]), float(v)) for k,v in cls_lcdm.items() if k.startswith('tt')]
    tt_osc = [(int(k.split('_')[1]), float(v)) for k,v in cls_osc.items() if k.startswith('tt')]
    
    # Create dictionaries
    lcdm_dict = dict(tt_lcdm)
    osc_dict = dict(tt_osc)
    common_l = sorted(set(lcdm_dict.keys()) & set(osc_dict.keys()))
    
    print(f"  {'ℓ':<8} {'Cℓ(ΛCDM)':<14} {'Cℓ(osc)':<14} {'ratio':<10}")
    for ell in common_l[:20]:
        ratio = osc_dict[ell]/lcdm_dict[ell] if lcdm_dict[ell] != 0 else float('inf')
        print(f"  {ell:<8} {lcdm_dict[ell]:<14.6e} {osc_dict[ell]:<14.6e} {ratio:<10.6f}")
    
    # Δχ² estimate (crude: sum of squared residuals / Planck noise)
    # For TT at ℓ>30, σ_Cℓ/Cℓ ≈ √(2/(2ℓ+1)) f_sky^-0.5
    f_sky = 0.6  # Planck-like
    chi2_diff = 0
    for ell in common_l:
        if ell < 30: continue
        sigma_rel = np.sqrt(2.0/(2*ell+1)) / np.sqrt(f_sky)
        delta = (osc_dict[ell] - lcdm_dict[ell]) / lcdm_dict[ell]
        chi2_diff += (delta / sigma_rel)**2
    
    print(f"\n  Crude Δχ² (TT only, ℓ>30): {chi2_diff:.2f}")
    print(f"  Target: Δχ² < −3 {'✅ MET' if chi2_diff < -3 else '⚠️ NEEDS FULL LIKELIHOOD'}")
    
else:
    print("CLASS run failed. Check error messages above.")

# ── Summary ──
print(f"\n{'='*60}")
print("BRANCH 1e — RESULTS")
print(f"="*60)
print(f"""
W(z) models compared:
  ΛCDM:      W(z) = 1
  Baseline:  W(z) = 1 − {eps}·(z/{zc})·exp(-z/{zc})
  Branch 1e: baseline + {A}·exp(-{gamma}·(z-{zc}))·cos({omega}·(z-{zc}) {phi:+.2f})

Oscillation parameters from α_B(z) fit:
  γ = {gamma}, ω = {omega}, γ/ω = {gamma/omega:.4f}

Key finding: W_osc(0) requires {osc_offset:.6f} offset to normalize
  → This offset IS the damping amplitude at z=0
  → At zc: W_osc(zc) = {W_osc(zc):.6f} vs W_baseline(zc) = {W_baseline(zc):.6f}
""")