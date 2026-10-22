#!/usr/bin/env python3
"""
Python-only CLASS (classy) 3-model comparison: ΛCDM vs IDM baseline vs IDM+Branch1e.

Uses Omega_fld + fluid_equation_of_state (CPL) interface with effective w(z)
derived from each model's W(z) modulation of the dark energy density.

Method:
  H(z)²/H₀² = Ω_m(1+z)³ + Ω_r(1+z)⁴ + Ω_DE·W(z)
  
  Effective w(z) for fluid DE:
    ρ_DE(z) = ρ_DE(0)·exp(3∫₀ᶻ(1+w(z'))/(1+z') dz') = Ω_DE·W(z)·ρ_crit(0)
    
  ⇒ 1 + w(z) = (1+z)/3 · W'(z)/W(z)
  
  We fit CPL: w(z) = w0 + wa·z/(1+z) to the effective w(z)
  for each model (baseline and oscillatory), then run CLASS with
  Omega_fld + w0_fld + wa_fld.

Outputs:
  - results/classy_3model/cl_ratio.png   — Cℓ ratio vs ℓ
  - results/classy_3model/chi2_table.txt  — χ² comparison
"""

import numpy as np
import os, sys, json

# ── IDM parameters ──
H0 = 69.0                     # km/s/Mpc
Omega_m = 0.297
Omega_r = 4.15e-5 / (H0 / 100) ** 2
Omega_L = 1.0 - Omega_m - Omega_r   # ≈ 0.703
eps = 0.1545
zc = 0.60

# Branch 1e oscillation parameters
A, gamma, omega, phi = 0.008, 3.13, 2.25, -0.836

# ── W(z) model definitions ──

def W_lcdm(z):
    return np.ones_like(z, dtype=float)

def W_baseline(z):
    x = np.asarray(z, dtype=float) / zc
    return 1.0 - eps * x * np.exp(-x)

def W_osc_raw(z):
    x = np.asarray(z, dtype=float) / zc
    base = 1.0 - eps * x * np.exp(-x)
    osc = A * np.exp(-gamma * (np.asarray(z, dtype=float) - zc)) * \
          np.cos(omega * (np.asarray(z, dtype=float) - zc) + phi)
    return base + osc

# Normalize osc so W_osc(0) = 1
z0 = 1e-6
osc_offset = 1.0 - float(W_osc_raw(z0))
def W_osc(z):
    return W_osc_raw(z) + osc_offset

# ── Effective w(z) from W(z) ──
def w_eff_from_W(W_func, z):
    """Compute effective w(z) for a given dark energy density modulation W(z).
    
    ρ_DE(z) ∝ W(z), and for fluid DE:
        ρ_DE(z) = ρ_DE(0)·exp(3∫ (1+w(z'))/(1+z') dz')
    
    ⇒ 1 + w(z) = (1+z)/3 · d/dz[ln W(z)]
    
    Returns w_eff(z) array with same shape as z.
    """
    z_arr = np.asarray(z, dtype=float)
    eps_z = 1e-6
    W_vals = W_func(z_arr)
    # Numerical derivative of ln W
    W_shift = W_func(z_arr + eps_z)
    dlnW_dz = (np.log(W_shift) - np.log(W_vals)) / eps_z
    w = -1.0 + (1.0 + z_arr) / 3.0 * dlnW_dz
    # Handle z=0 edge case: use forward difference from small z
    mask_z0 = (z_arr < 1e-5)
    if np.any(mask_z0):
        z_small = 1e-4
        W_small = float(W_func(z_small))
        W_0 = float(W_func(0.0))
        dlnW_dz0 = (np.log(W_small) - np.log(W_0)) / z_small
        w[mask_z0] = -1.0 + (1.0 + z_arr[mask_z0]) / 3.0 * dlnW_dz0
    return w


def fit_cpl(w_func, z_max=3.0, n_pts=2000):
    """Fit CPL parameters w0, wa to effective w(z) over z∈[0, z_max].
    
    w(z) = w0 + wa * z/(1+z)
    
    Returns (w0, wa, rms_residual).
    """
    z_arr = np.linspace(0.01, z_max, n_pts)  # avoid z=0 singularity
    w_vals = w_func(z_arr)
    x = z_arr / (1.0 + z_arr)  # CPL variable
    
    # Linear least squares: w = w0 + wa * x
    A_mat = np.column_stack([np.ones_like(x), x])
    params, residuals, rank, s = np.linalg.lstsq(A_mat, w_vals, rcond=None)
    w0, wa = params
    
    w_pred = w0 + wa * x
    rms = np.sqrt(np.mean((w_vals - w_pred)**2))
    
    return w0, wa, rms


# ── Compute CPL fits ──
z_max_fit = 3.0

print("=" * 65)
print("CLASSY 3-MODEL COMPARISON")
print("=" * 65)

# For LCDM: w(z) = -1 exactly
w0_lcdm, wa_lcdm = -1.0, 0.0
print(f"\nΛCDM: w0={w0_lcdm}, wa={wa_lcdm}")

# For IDM baseline
w0_base, wa_base, rms_base = fit_cpl(
    lambda z: w_eff_from_W(W_baseline, z), z_max_fit)
print(f"IDM baseline: w0={w0_base:.6f}, wa={wa_base:.6f}, RMS={rms_base:.6e}")

# For IDM + Branch 1e
w0_osc, wa_osc, rms_osc = fit_cpl(
    lambda z: w_eff_from_W(W_osc, z), z_max_fit)
print(f"IDM+Branch1e: w0={w0_osc:.6f}, wa={wa_osc:.6f}, RMS={rms_osc:.6e}")

# Show effective w(z) at key redshifts
print("\nEffective w(z) at key redshifts:")
print(f"{'z':<8} {'ΛCDM':<12} {'baseline':<12} {'Branch1e':<12}")
for zv in [0.0, 0.2, 0.5, 1.0, 2.0, 3.0]:
    wl = -1.0
    wb = w_eff_from_W(W_baseline, np.array([zv]))[0]
    wo = w_eff_from_W(W_osc, np.array([zv]))[0]
    print(f"  {zv:<6.1f} {wl:<12.6f} {wb:<12.6f} {wo:<12.6f}")

# Verify H(z) matches
print("\nVerifying H(z)/H0 from CPL approximation vs exact W(z):")
z_test = np.array([0.0, 0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0])
for model_name, Wf, w0, wa in [
    ("ΛCDM", W_lcdm, w0_lcdm, wa_lcdm),
    ("baseline", W_baseline, w0_base, wa_base),
    ("Branch1e", W_osc, w0_osc, wa_osc),
]:
    # Exact H(z) from W(z)
    H2_exact = Omega_m * (1 + z_test)**3 + Omega_r * (1 + z_test)**4 + Omega_L * Wf(z_test)
    H_exact = np.sqrt(H2_exact)
    
    # CPL approximated H(z): ρ_DE(z) = Ω_L·exp(3∫(1+w(z'))/(1+z') dz')
    # For CPL: exp(3∫(1+w(z'))/(1+z') dz') = (1+z)^{3(1+w0+wa)}·exp(-3wa·z/(1+z))
    rho_de_cpl = Omega_L * (1 + z_test)**(3*(1+w0+wa)) * np.exp(-3*wa*z_test/(1+z_test))
    H2_cpl = Omega_m * (1 + z_test)**3 + Omega_r * (1 + z_test)**4 + rho_de_cpl
    H_cpl = np.sqrt(H2_cpl)
    
    rel_err = np.max(np.abs(H_cpl/H_exact - 1)) * 100
    print(f"  {model_name:<12}: max H(z) error = {rel_err:.4f}%")


# ── 2. CLASS runs ──
print("\n─── Running CLASS models ───")

from classy import Class

LMAX = 2000
BASE_PARAMS = {
    'output': 'tCl pCl lCl',
    'l_max_scalars': LMAX,
    'lensing': 'yes',
    'N_ur': 3.046,
    'h': H0 / 100.0,
    'omega_b': 0.02237,
    'omega_cdm': 0.1200,
    'tau_reio': 0.0544,
    'A_s': 2.1e-9,
    'n_s': 0.9649,
}

def run_model(label, Omega_fld_val, w0, wa, params_extra=None):
    """Run CLASS with fluid DE and return lensed Cℓ dict."""
    M = Class()
    pars = dict(BASE_PARAMS)
    pars.update({
        'Omega_fld': Omega_fld_val,
        'w0_fld': w0,
        'wa_fld': wa,
        'cs2_fld': 1.0,
    })
    if params_extra:
        pars.update(params_extra)
    M.set(pars)
    
    print(f"  Running {label}...", end=" ", flush=True)
    try:
        M.compute()
        cls = M.lensed_cl(LMAX)
        print(f"✅  ({len(cls['tt'])} ell values)")
        return cls, M
    except Exception as e:
        print(f"❌  {str(e)[:150]}")
        return None, M

models = [
    ("ΛCDM", Omega_L, w0_lcdm, wa_lcdm),
    ("IDM-baseline", Omega_L, w0_base, wa_base),
    ("IDM+Branch1e", Omega_L, w0_osc, wa_osc),
]

results = {}
for label, Omega_fld_val, w0, wa in models:
    cls, M = run_model(label, Omega_fld_val, w0, wa)
    results[label] = {"cls": cls, "M": M, "params": (Omega_fld_val, w0, wa)}


# ── 3. Output directory ──
out_dir = os.path.expanduser(
    "~/IDM-Consistency-Importance-Weight/results/classy_3model")
os.makedirs(out_dir, exist_ok=True)

# ── 4. χ² computation ──
print("\n" + "=" * 65)
print("χ² ANALYSIS (pseudo-χ² relative to ΛCDM)")
print("=" * 65)

# Reference: ΛCDM
ref_cls = results["ΛCDM"]["cls"]
if ref_cls is None:
    print("❌ ΛCDM failed — cannot compute χ². Exiting.")
    sys.exit(1)

ell = np.array(ref_cls["ell"], dtype=int) if hasattr(ref_cls['ell'], '__iter__') else np.arange(len(ref_cls['tt']))

# For each model, compute χ² vs ΛCDM
chi2_results = {}
f_sky = 0.65  # Planck sky fraction

for label, data in results.items():
    if data["cls"] is None:
        chi2_results[label] = None
        continue
    if label == "ΛCDM":
        chi2_results[label] = {"chi2": 0.0, "ndof": 0}
        continue
    
    cls = data["cls"]
    
    total_chi2 = 0.0
    total_ndof = 0
    
    print(f"\n  {label} vs ΛCDM:")
    
    for spec, spec_label, noise_level in [
        ("tt", "TT", 1e-14),
        ("ee", "EE", 5e-15),
        ("te", "TE", 2e-15),
    ]:
        lcdm_vals = np.array(ref_cls[spec])
        model_vals = np.array(cls[spec])
        
        # Ensure same length
        n_min = min(len(lcdm_vals), len(model_vals))
        lcdm_v = lcdm_vals[:n_min]
        model_v = model_vals[:n_min]
        ell_v = np.arange(n_min, dtype=int)
        
        # Skip low ell where cosmic variance is very large (ℓ<30 for TE/EE, ℓ<2 for TT)
        if spec == "tt":
            l_min_spec = 2
        else:
            l_min_spec = 30
        
        mask = ell_v >= l_min_spec
        l_m = ell_v[mask]
        lcdm_m = lcdm_v[mask]
        model_m = model_v[mask]
        
        # Variance: cosmic variance + noise
        # σ²_Cℓ = 2/(2ℓ+1) * Cℓ² / f_sky²
        cv_term = 2.0 / (2.0 * l_m + 1.0) * lcdm_m**2 / f_sky**2
        noise_term = (noise_level * (l_m / 1000.0)**2)**2
        var = cv_term + noise_term
        
        # ℓ-binned χ² (bin width ~ 30 to reduce noise)
        bin_width = 30
        chi2_spec = 0.0
        n_bins = 0
        for i in range(0, len(l_m), bin_width):
            i_end = min(i + bin_width, len(l_m))
            if i_end - i < 5:
                continue
            delta = model_m[i:i_end] - lcdm_m[i:i_end]
            var_b = var[i:i_end] / (i_end - i)  # effective variance of binned mean
            chi2_spec += np.sum(delta**2 / var[i:i_end])
            n_bins += (i_end - i)
        
        chi2_spec_clean = np.sum((model_m - lcdm_m)**2 / var)
        total_chi2 += chi2_spec_clean
        total_ndof += len(l_m)
        
        # Per-spec stats
        rel_diff = (model_m - lcdm_m) / np.maximum(lcdm_m, 1e-30)
        rms_rel = np.sqrt(np.mean(rel_diff**2)) * 100
        print(f"    {spec_label:4s} (ℓ≥{l_min_spec:3d}): χ²={chi2_spec_clean:.1f}, ndof={len(l_m)}, RMS={rms_rel:.3f}%")
    
    chi2_results[label] = {"chi2": total_chi2, "ndof": total_ndof}
    print(f"    → Total χ²={total_chi2:.1f} / {total_ndof} dof = {total_chi2/total_ndof:.3f}")

# Δχ²
if chi2_results.get("IDM+Branch1e") and chi2_results.get("ΛCDM"):
    chi2_lcdm = chi2_results["ΛCDM"]["chi2"]
    chi2_osc = chi2_results["IDM+Branch1e"]["chi2"]
    delta_chi2 = chi2_lcdm - chi2_osc  # positive = Branch1e fits better
    print(f"\n  Δχ² = χ²_ΛCDM − χ²_Branch1e = {delta_chi2:.2f}")
    print(f"  {'✅ Δχ² > 0 (Branch1e preferred)' if delta_chi2 > 0 else '❌ ΛCDM preferred'}")


# ── 5. Cℓ ratio plot ──
print("\n─── Generating Cℓ ratio plot ───")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("CLASSY 3-Model Comparison: Cℓ Ratio vs ΛCDM", fontsize=14, y=0.98)

# Get baseline and Branch1e Cℓ
ref_cl = ref_cls
base_cl = results["IDM-baseline"]["cls"]
osc_cl = results["IDM+Branch1e"]["cls"]

if base_cl is not None and osc_cl is not None:
    specs = [("tt", "TT"), ("ee", "EE"), ("te", "TE"), ("pp", "PP")]
    
    for idx, (spec, label) in enumerate(specs):
        ax = axes[idx // 2, idx % 2]
        
        ell_arr = np.arange(len(ref_cl[spec]), dtype=int)
        ref_v = np.array(ref_cl[spec])
        base_v = np.array(base_cl[spec])
        osc_v = np.array(osc_cl[spec])
        
        n_min = min(len(ref_v), len(base_v), len(osc_v))
        ell_v = ell_arr[:n_min]
        ref_v = ref_v[:n_min]
        base_v = base_v[:n_min]
        osc_v = osc_v[:n_min]
        
        # Ratios (with small offset to avoid division by zero)
        eps_ratio = 1e-30
        ratio_base = base_v / np.maximum(ref_v, eps_ratio)
        ratio_osc = osc_v / np.maximum(ref_v, eps_ratio)
        
        ax.plot(ell_v[2:], ratio_base[2:], 'b-', lw=1.5, alpha=0.8, label="IDM baseline / ΛCDM")
        ax.plot(ell_v[2:], ratio_osc[2:], 'r-', lw=1.5, alpha=0.8, label="IDM+Branch1e / ΛCDM")
        ax.axhline(1.0, color='k', ls='--', lw=0.8, alpha=0.4)
        ax.set_xlabel("ℓ")
        ax.set_ylabel(f"Cℓ({label}) / Cℓ(ΛCDM)")
        ax.set_title(f"{label} Power Spectrum Ratio")
        ax.set_xlim(2, LMAX)
        ax.grid(alpha=0.3)
        ax.legend(fontsize=9)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plot_path = f"{out_dir}/cl_ratio.png"
    fig.savefig(plot_path, dpi=150, bbox_inches="tight")
    print(f"  Plot saved: {plot_path}")
else:
    print("  Skipping plot — some models failed")

plt.close()

# ── 6. Save results ──
print("\n─── Saving results ───")

# Save χ² table
chi2_lines = [
    "CLASSY 3-Model χ² Comparison",
    "=" * 65,
    f"{'Model':<20} {'χ²':<12} {'ndof':<8} {'χ²/dof':<10}",
    "-" * 50,
]
for label in ["ΛCDM", "IDM-baseline", "IDM+Branch1e"]:
    if chi2_results.get(label):
        c = chi2_results[label]
        chi2_lines.append(f"{label:<20} {c['chi2']:<12.1f} {c['ndof']:<8d} {c['chi2']/max(c['ndof'],1):<10.3f}")
    else:
        chi2_lines.append(f"{label:<20} {'FAILED':<12}")

if delta_chi2 is not None:
    chi2_lines.extend([
        "",
        f"Δχ² = χ²_ΛCDM - χ²_Branch1e = {delta_chi2:.2f}",
    ])

chi2_path = f"{out_dir}/chi2_table.txt"
with open(chi2_path, "w") as f:
    f.write("\n".join(chi2_lines))
print(f"  χ² table: {chi2_path}")

# Save model params
params_path = f"{out_dir}/model_params.txt"
with open(params_path, "w") as f:
    f.write("CLASSY 3-Model Comparison — Model Parameters\n")
    f.write("=" * 65 + "\n\n")
    f.write(f"Omega_m = {Omega_m:.6f}\n")
    f.write(f"Omega_r = {Omega_r:.6e}\n")
    f.write(f"Omega_L = {Omega_L:.6f}\n")
    f.write(f"H0 = {H0:.1f} km/s/Mpc\n")
    f.write(f"eps = {eps:.6f}, zc = {zc:.6f}\n")
    f.write(f"Branch1e: A={A}, gamma={gamma}, omega={omega}, phi={phi}\n\n")
    f.write(f"{'Model':<20} {'Omega_fld':<12} {'w0':<12} {'wa':<12} {'RMS_w':<12}\n")
    f.write("-" * 68 + "\n")
    for label, od, w0, wa in models:
        f.write(f"{label:<20} {od:<12.6f} {w0:<12.6f} {wa:<12.6f} -\n")

print(f"  Model params: {params_path}")

# Save Cℓ data
for label, data in results.items():
    if data["cls"] is None:
        continue
    cls = data["cls"]
    ell_arr = np.arange(len(cls['tt']), dtype=int)
    cl_save = np.column_stack([ell_arr, cls['tt'], cls['ee'], cls['te'], cls['bb'], cls['pp']])
    np.savetxt(
        f"{out_dir}/cl_{label.lower().replace('+','_').replace('-','_')}.txt",
        cl_save,
        header="ell TT EE TE BB PP",
        fmt="%d  %.10e  %.10e  %.10e  %.10e  %.10e"
    )
print(f"  Cℓ data: {out_dir}/cl_*.txt")

# ── Summary ──
print("\n" + "=" * 65)
print("SUMMARY")
print("=" * 65)
print(f"""
Models compared:
  1. ΛCDM (w0=-1, wa=0)
  2. IDM baseline (w0={w0_base:.4f}, wa={wa_base:.4f})
  3. IDM+Branch1e (w0={w0_osc:.4f}, wa={wa_osc:.4f})

Δχ² = χ²_ΛCDM − χ²_Branch1e = {delta_chi2:.2f} ({'Branch1e preferred' if delta_chi2 > 0 else 'ΛCDM preferred'})

Output:
  Cℓ ratio plot: {plot_path}
  χ² table:      {chi2_path}
  Parameters:    {params_path}
""")