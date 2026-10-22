#!/usr/bin/env python3
"""Extended Branch 1e oscillation constraint: BAO(D_V/r_d) + H(z) Cosmic Chronometers.
Wider grid, r_s marginalization, multi-parameter scan.
"""
import numpy as np
from scipy import integrate, stats
import json, time

# ============================================================
# Constants & Data
# ============================================================
C = 299792.458          # km/s
R_S_PLANCK = 147.09     # sound horizon (Mpc, Planck 2018)

# H(z) Cosmic Chronometers (z, H, err)
HZ = np.array([
    [0.07, 69.0, 19.5], [0.09, 69.0, 12.0], [0.12, 68.6, 26.2],
    [0.17, 83.0, 8.0], [0.179, 75.0, 4.0], [0.199, 75.0, 5.0],
    [0.20, 72.9, 29.6], [0.27, 77.0, 14.0], [0.28, 88.8, 36.6],
    [0.352, 83.0, 14.0], [0.38, 81.5, 1.9], [0.4, 82.8, 1.2],
    [0.4004, 77.0, 10.2], [0.4247, 87.1, 11.2], [0.44, 82.6, 7.8],
    [0.4448, 92.8, 12.9], [0.47, 89.0, 49.6], [0.4783, 80.9, 9.0],
    [0.48, 97.0, 62.0], [0.51, 90.4, 1.9], [0.56, 93.34, 2.3],
    [0.57, 92.4, 4.5], [0.593, 104.0, 13.0], [0.6, 87.9, 6.1],
    [0.61, 97.3, 2.1], [0.68, 92.0, 8.0], [0.73, 97.3, 7.0],
    [0.78, 97.6, 4.0], [0.781, 105.0, 12.0], [0.875, 125.0, 17.0],
    [0.88, 90.0, 40.0], [0.9, 117.0, 23.0], [1.037, 154.0, 20.0],
    [1.3, 168.0, 17.0], [1.363, 160.0, 33.6], [1.43, 177.0, 18.0],
    [1.53, 140.0, 14.0], [1.75, 202.0, 40.0], [1.965, 186.5, 50.4],
])

# BAO D_V / r_d  (z, D_V/r_d, err)
BAO = np.array([
    [0.106, 3.05, 0.14],   [0.15,  4.48, 0.17],
    [0.38,  8.47, 0.22],   [0.51, 10.74, 0.16],
    [0.61, 12.16, 0.16],   [0.70, 14.07, 0.28],
    [1.48, 26.19, 0.77],   [2.33, 37.77, 2.14],
])

# ============================================================
# Model
# ============================================================
class IDMModel:
    def __init__(self, H0=67.4, Om=0.315, eps=0.0, zc=0.6,
                 A_osc=0.0, gamma_osc=3.13, omega_osc=2.25, phi_osc=-0.836):
        self.H0 = H0
        self.Om = Om
        self.Ol = 1.0 - Om
        self.eps = eps
        self.zc = zc
        self.A = A_osc
        self.gamma = gamma_osc
        self.omega = omega_osc
        self.phi = phi_osc
        self.W0 = self._W_ana(0.0)

    def _W_ana(self, z):
        z = np.asarray(z, dtype=float)
        return self.A * np.exp(-self.gamma * (z - self.zc)) * np.cos(self.omega * (z - self.zc) + self.phi)

    def f_idm(self, z):
        z = np.asarray(z, dtype=float)
        x = z / self.zc
        f_base = 1.0 - self.eps * x * np.exp(-x)
        if self.A == 0.0:
            return f_base
        return f_base + self._W_ana(z) - self.W0

    def E(self, z):
        z = np.asarray(z, dtype=float)
        return np.sqrt(self.Om * (1+z)**3 + self.Ol * self.f_idm(z))

    def H(self, z):
        return self.H0 * self.E(z)

    def D_C(self, z):
        f = lambda x: 1.0 / self.E(x)
        I, _ = integrate.quad(f, 0, z, limit=1000, epsabs=1e-12, epsrel=1e-12)
        return C / self.H0 * I

    def D_V(self, z):
        D_M = self.D_C(z)
        H_z = self.H(z)
        return (C * z * D_M**2 / H_z)**(1/3)


# ============================================================
# Chi² with r_s marginalisation
# ============================================================
def chi2_hz(model):
    resid = model.H(HZ[:, 0]) - HZ[:, 1]
    return np.sum((resid / HZ[:, 2])**2)

def chi2_bao_marg(model, r_s_prior=R_S_PLANCK, sigma_rs=2.0):
    """BAO χ² with r_s marginalised via numerical scan.
    
    χ² = Σ ((D_V_model/r_s - data) / err)² + ((r_s - r0) / σ_rs)²
    """
    zs = BAO[:, 0]
    dv_data = BAO[:, 1]
    dv_err = BAO[:, 2]
    dv_model = np.array([model.D_V(z) for z in zs])
    
    w = 1.0 / dv_err**2
    A = np.sum(w * dv_data**2)  # constant
    B = np.sum(w * dv_data * dv_model)
    C = np.sum(w * dv_model**2)
    
    # Scan r_s ∈ [120, 170] Mpc
    rs_test = np.linspace(120.0, 170.0, 1001)
    chi2_vals = A - 2*B/rs_test + C/rs_test**2 + ((rs_test - r_s_prior) / sigma_rs)**2
    idx = np.argmin(chi2_vals)
    return chi2_vals[idx], rs_test[idx]


def chi2_total(model, marginalize_rs=True):
    c_h = chi2_hz(model)
    if marginalize_rs:
        c_b, rs = chi2_bao_marg(model)
    else:
        c_b = 0.0
        for z, dv_data, dv_err in BAO:
            dv_m = model.D_V(z) / R_S_PLANCK
            c_b += ((dv_m - dv_data) / dv_err)**2
        rs = R_S_PLANCK
    return c_h + c_b, {'H(z)': c_h, 'BAO': c_b, 'r_s': rs}


# ============================================================
# Scan: H₀ × Ωₘ grid
# ============================================================
def scan_grid(epss=[0.0], A_oscs=[0.0], zc=0.6, verbose=True):
    """Coarse 2D scan on extended H₀ (55-82) × Ωₘ (0.10-0.50)."""
    H0s = np.arange(55.0, 82.5, 1.5)       # 19 pts
    Oms = np.arange(0.10, 0.505, 0.025)     # 17 pts
    n_total = len(H0s) * len(Oms)
    
    results = {}
    for eps in epss:
        for A in A_oscs:
            label = f"eps={eps:.4f}, A={A:.4f}"
            best = None
            t0 = time.time()
            for i, H0 in enumerate(H0s):
                for Om in Oms:
                    model = IDMModel(H0=H0, Om=Om, eps=eps, zc=zc, A_osc=A)
                    c_t, det = chi2_total(model, marginalize_rs=True)
                    if best is None or c_t < best[0]:
                        best = (c_t, H0, Om, det)
            dt = time.time() - t0
            results[label] = {
                'chi2': best[0], 'H0': best[1], 'Om': best[2],
                'det': best[3], 'eps': eps, 'A': A,
            }
            if verbose:
                print(f"  {label:>25s}: χ²={best[0]:8.2f}, H₀={best[1]:6.1f}, "
                      f"Ωₘ={best[2]:.4f}, r_s={best[3]['r_s']:.2f}  [{dt:.0f}s]")
    return results


# ============================================================
# Fine scan near best-fit
# ============================================================
def scan_fine(center_H0, center_Om, eps=0.1545, A_osc=0.008, zc=0.6):
    """Fine grid near the best-fit region."""
    H0s = np.linspace(center_H0 - 5, center_H0 + 5, 21)  # 21 pts, 0.5 step
    Oms = np.linspace(max(0.10, center_Om - 0.12), min(0.50, center_Om + 0.12), 21)
    
    best = None
    for H0 in H0s:
        for Om in Oms:
            model = IDMModel(H0=H0, Om=Om, eps=eps, zc=zc, A_osc=A_osc)
            c_t, det = chi2_total(model, marginalize_rs=True)
            if best is None or c_t < best[0]:
                best = (c_t, H0, Om, det)
    
    return {
        'chi2': best[0], 'H0': best[1], 'Om': best[2],
        'det': best[3], 'eps': eps, 'A': A_osc,
    }


# ============================================================
# Gamma scan
# ============================================================
def scan_gamma(epss=[0.1545], zc=0.6, n_fixed=None):
    """Scan damping rate γ for fixed (H₀, Ωₘ) at best-fit baseline."""
    gammas = np.linspace(0.5, 6.0, 12)
    As = [0.008]  # Branch 1e spec
    
    print(f"  {'γ':>8} {'A':>10} {'χ²':>10} {'Δχ²':>10} {'χ²_H':>10} {'χ²_BAO':>8} {'r_s':>8}")
    print(f"  {'-'*60}")
    
    for eps in epss:
        for A in As:
            base_model = IDMModel(H0=n_fixed['H0'], Om=n_fixed['Om'],
                                   eps=eps, zc=zc, A_osc=0.0)
            base_chi2, _ = chi2_total(base_model, marginalize_rs=True)
            
            for gamma in gammas:
                model = IDMModel(H0=n_fixed['H0'], Om=n_fixed['Om'],
                                  eps=eps, zc=zc, A_osc=A, gamma_osc=gamma)
                c_t, det = chi2_total(model, marginalize_rs=True)
                dchi2 = c_t - base_chi2
                print(f"  {gamma:>8.2f} {A:>10.6f} {c_t:>10.2f} {dchi2:>+10.2f} "
                      f"{det['H(z)']:>10.1f} {det['BAO']:>8.1f} {det['r_s']:>8.2f}")
    
    return gammas


# ============================================================
# Amplitude scan with refit
# ============================================================
def scan_A_with_refit(eps=0.1545, zc=0.6):
    """For each A, refit H₀,Ωₘ on a coarse grid."""
    As = [0.0, 0.001, 0.003, 0.005, 0.008, 0.01, 0.015, 0.02, 0.03, 0.05, 0.08, 0.12, 0.2, 0.5, 1.0]
    
    print(f"\n  {'A':>10} {'χ²_best':>10} {'H₀':>8} {'Ωₘ':>8} {'Δχ²':>10} {'Sig':>8}")
    print(f"  {'-'*48}")
    
    base_chi2 = None
    results = []
    for A in As:
        best = scan_grid(epss=[eps], A_oscs=[A], zc=zc, verbose=False)
        label = f"eps={eps:.4f}, A={A:.4f}"
        r = best[label]
        if base_chi2 is None:
            base_chi2 = r['chi2']
        dchi2 = r['chi2'] - base_chi2
        sig = np.sqrt(max(0, dchi2))
        results.append((A, r['chi2'], r['H0'], r['Om'], dchi2, sig, r['det']))
        print(f"  {A:>10.6f} {r['chi2']:>10.2f} {r['H0']:>8.1f} {r['Om']:>8.4f} {dchi2:>+10.2f} {sig:>8.2f}")
    
    return results


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 65)
    print("  Branch 1e Extended Constraint  BAO(D_V/r_d) + H(z) + r_s marginalization")
    print("=" * 65)
    
    # ── Phase 1: Extended 2D scan for each model ──
    print("\n" + "─" * 60)
    print("  Phase 1: Extended H₀(55-82) × Ωₘ(0.10-0.50) scan")
    print("─" * 60)
    
    configs = [
        ('ΛCDM',           0.0,    0.0),
        ('IDM baseline',   0.1545, 0.0),
        ('IDM+Branch1e',   0.1545, 0.008),
    ]
    
    best_fits = []
    for label, eps, A in configs:
        print(f"\n  Scanning {label}...")
        r = scan_grid(epss=[eps], A_oscs=[A], zc=0.6, verbose=True)
        k = f"eps={eps:.4f}, A={A:.4f}"
        best_fits.append((label, r[k]))
    
    # ── Phase 2: Fine scan near best-fit for IDM+Branch1e ──
    br_b1e = best_fits[2][1]
    print("\n" + "─" * 60)
    print("  Phase 2: Fine scan near Branch1e best-fit")
    print("─" * 60)
    fine = scan_fine(br_b1e['H0'], br_b1e['Om'], eps=0.1545, A_osc=0.008)
    print(f"  Fine: χ²={fine['chi2']:.2f}, H₀={fine['H0']:.1f}, Ωₘ={fine['Om']:.4f}, "
          f"r_s={fine['det']['r_s']:.2f}")
    
    # Update best fit with fine result
    if fine['chi2'] < br_b1e['chi2']:
        best_fits[2] = ('IDM+Branch1e (fine)', fine)
    
    # ── Phase 3: Result table ──
    print("\n" + "─" * 60)
    print("  Phase 3: Results")
    print("─" * 60)
    
    lcdm_chi2 = best_fits[0][1]['chi2']
    for label, r in best_fits:
        d = r['chi2'] - lcdm_chi2
        print(f"\n  {label}")
        print(f"    χ² = {r['chi2']:.2f}  (Δχ² vs ΛCDM = {d:+.2f})")
        print(f"    H₀ = {r['H0']:.1f}, Ωₘ = {r['Om']:.4f}")
        print(f"    H(z) χ² = {r['det']['H(z)']:.1f}, BAO χ² = {r['det']['BAO']:.1f}")
        print(f"    r_s ≈ {r['det']['r_s']:.2f} Mpc")
    
    # Deltas
    d_osc_base = best_fits[2][1]['chi2'] - best_fits[1][1]['chi2']
    d_base_lcdm = best_fits[1][1]['chi2'] - best_fits[0][1]['chi2']
    d_osc_lcdm = best_fits[2][1]['chi2'] - best_fits[0][1]['chi2']
    
    print(f"\n  {'─'*48}")
    print(f"  Δχ²(osc − baseline):         {d_osc_base:>+8.2f}")
    print(f"  Δχ²(baseline − ΛCDM):        {d_base_lcdm:>+8.2f}")
    print(f"  Δχ²(osc − ΛCDM):             {d_osc_lcdm:>+8.2f}")
    print(f"  {'─'*48}")
    
    # ── Phase 4: γ scan ──
    print("\n\n" + "─" * 60)
    print("  Phase 4: Damping rate γ scan (fixed H₀, Ωₘ)")
    print("─" * 60)
    scan_gamma(epss=[0.1545], zc=0.6,
               n_fixed={'H0': best_fits[1][1]['H0'], 'Om': best_fits[1][1]['Om']})
    
    # ── Phase 5: A scan with refit ──
    print("\n\n" + "─" * 60)
    print("  Phase 5: Amplitude A scan (refitting H₀, Ωₘ each step)")
    print("─" * 60)
    amp_results = scan_A_with_refit(eps=0.1545, zc=0.6)
    
    # 95% CL
    for A, _, _, _, dchi2, _, _ in amp_results:
        if A > 0 and dchi2 > 2.71:
            print(f"\n  95% CL upper limit on A: < {A:.6f}")
            break
    
    # ── Phase 6: Contour info (2D χ² surface around best) ──
    print("\n\n" + "─" * 60)
    print("  Phase 6: χ² contour around Branch1e best-fit")
    print("─" * 60)
    
    # Simple 1D profile: for best-fit H₀, scan Ωₘ within χ² min + 1
    bb = fine if fine['chi2'] < br_b1e['chi2'] else br_b1e
    h0_best, om_best = bb['H0'], bb['Om']
    chi2_best = bb['chi2']
    
    # Ωₘ 1σ range at fixed H₀
    oms = np.linspace(om_best - 0.10, om_best + 0.10, 41)
    chi2s = []
    for om in oms:
        m = IDMModel(H0=h0_best, Om=om, eps=0.1545, zc=0.6, A_osc=0.008)
        c, _ = chi2_total(m, marginalize_rs=True)
        chi2s.append(c)
    chi2s = np.array(chi2s)
    dchi2s = chi2s - chi2_best
    # Find 1σ interval
    om_low = oms[dchi2s < 1.0].min() if np.any(dchi2s < 1.0) else oms[0]
    om_high = oms[dchi2s < 1.0].max() if np.any(dchi2s < 1.0) else oms[-1]
    print(f"  Branch1e: H₀={h0_best:.1f} (fixed)")
    print(f"  Ωₘ 1σ interval (Δχ²<1): [{om_low:.4f}, {om_high:.4f}]")
    if om_high - om_low < 0.01:
        print("  (tight constraint — BAO+H(z) pins Ωₘ well)")
    else:
        print(f"  (Ωₘ uncertainty ~ {om_high-om_low:.3f})")
    
    # ── Save ──
    out = {
        'models': [
            {'label': l, 'chi2': r['chi2'], 'H0': r['H0'], 'Om': r['Om'],
             'det': {'H_z': r['det']['H(z)'], 'BAO': r['det']['BAO'], 'r_s': r['det']['r_s']}}
            for l, r in best_fits
        ],
        'deltas': {
            'osc_vs_baseline': d_osc_base,
            'baseline_vs_lcdm': d_base_lcdm,
            'osc_vs_lcdm': d_osc_lcdm,
        },
        'amplitude_scan': [
            {'A': a, 'chi2': c, 'H0': h, 'Om': o, 'dchi2': d}
            for a, c, h, o, d, _, _ in amp_results
        ],
        'gamma_scan_params': {
            'H0_fixed': best_fits[1][1]['H0'],
            'Om_fixed': best_fits[1][1]['Om'],
            'gammas': list(np.linspace(0.5, 6.0, 12)),
        },
        'om_1sigma': [float(om_low), float(om_high)],
        'r_s_marginalized': True,
    }
    
    path = '/home/wsl/IDM-Lagrangian-Reverse-Engineering/results/branch1e_constraint_ext.json'
    with open(path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\n{'='*65}")
    print(f"  Saved: {path}")
    print(f"{'='*65}")


if __name__ == '__main__':
    main()