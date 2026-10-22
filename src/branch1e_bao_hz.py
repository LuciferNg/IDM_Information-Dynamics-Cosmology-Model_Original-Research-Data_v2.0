#!/usr/bin/env python3
"""Branch 1e oscillation constraint: BAO(D_V/r_d) + H(z) Cosmic Chronometers.

Model comparison between ΛCDM, IDM baseline, and IDM+Branch1e oscillation.
The Branch 1e adds A·exp(-γ(z-zc))·cos(ω(z-zc)+φ) to the IDM sync dip f(z).
Normalized so f(0)=1.

Branch 1e spec: A=0.008, γ=3.13, ω=2.25, φ=-0.836
"""
import numpy as np
from scipy import integrate
import sys, json

# ============================================================
# Constants
# ============================================================
C = 299792.458          # km/s
R_S = 147.09            # sound horizon (Mpc, Planck 2018)

# ============================================================
# Models
# ============================================================

class IDMModel:
    """IDM with optional Branch 1e damped oscillation in f(z)."""
    def __init__(self, H0=67.4, Om=0.315, eps=0.0, zc=0.6,
                 A_osc=0.0, gamma_osc=3.13, omega_osc=2.25, phi_osc=-0.836):
        self.H0 = H0
        self.Om = Om
        self.Ol = 1.0 - Om
        self.eps = eps
        self.zc = zc
        # Branch 1e oscillation
        self.A = A_osc
        self.gamma = gamma_osc
        self.omega = omega_osc
        self.phi = phi_osc
        self.W0 = self._W_ana(0.0)  # normalization offset

    def _W_ana(self, z):
        """Un-normalized oscillation term."""
        return self.A * np.exp(-self.gamma * (z - self.zc)) * np.cos(self.omega * (z - self.zc) + self.phi)

    def f_idm(self, z):
        """Total f(z) = baseline + oscillation (normalized: f(0)=1)."""
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
        """Comoving distance (Mpc)."""
        f = lambda x: 1.0 / self.E(x)
        I, _ = integrate.quad(f, 0, z, limit=1000, epsabs=1e-12, epsrel=1e-12)
        return C / self.H0 * I

    def D_V_over_rs(self, z):
        """D_V(z) / r_s — the BAO observable."""
        D_M = self.D_C(z)  # flat universe
        H_z = self.H(z)
        D_V = (C * z * D_M**2 / H_z)**(1/3)
        return D_V / R_S


# ============================================================
# Data
# ============================================================

# H(z) Cosmic Chronometers
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

# BAO D_V / r_d
BAO = [
    (0.106, 3.05, 0.14),   # 6dFGS
    (0.15,  4.48, 0.17),   # SDSS MGS
    (0.38,  8.47, 0.22),   # SDSS DR12
    (0.51, 10.74, 0.16),   # SDSS DR12
    (0.61, 12.16, 0.16),   # SDSS DR12
    (0.70, 14.07, 0.28),   # eBOSS LRG
    (1.48, 26.19, 0.77),   # eBOSS QSO
    (2.33, 37.77, 2.14),   # eBOSS Lyα
]


# ============================================================
# χ² functions
# ============================================================

def chi2_hz(model):
    resid = model.H(HZ[:, 0]) - HZ[:, 1]
    return np.sum((resid / HZ[:, 2])**2)

def chi2_bao(model):
    chi2 = 0.0
    pulls = []
    for z, dv_data, dv_err in BAO:
        dv_model = model.D_V_over_rs(z)
        pull = (dv_model - dv_data) / dv_err
        chi2 += pull**2
        pulls.append(pull)
    return chi2, np.array(pulls)

def chi2_total(model):
    c_h = chi2_hz(model)
    c_b, _ = chi2_bao(model)
    return c_h + c_b, {'H(z)': c_h, 'BAO': c_b}


# ============================================================
# Scan
# ============================================================

def scan_H0_Om(eps_list=[0.0], A_list=[0.0], zc=0.6, verbose=True):
    """Scan H₀ and Ω_m for each (ε, A_osc) pair, find best-fit χ²."""
    H0s = np.linspace(60, 78, 37)
    Oms = np.linspace(0.18, 0.45, 28)
    
    results = {}
    
    for eps in eps_list:
        for A in A_list:
            label = f"ε={eps:.4f}, A={A:.4f}"
            best = None
            for H0 in H0s:
                for Om in Oms:
                    model = IDMModel(H0=H0, Om=Om, eps=eps, zc=zc, A_osc=A)
                    c_t, det = chi2_total(model)
                    if best is None or c_t < best[0]:
                        best = (c_t, H0, Om, det)
            
            results[label] = {
                'chi2': best[0],
                'H0': best[1],
                'Om': best[2],
                'det': best[3],
                'eps': eps,
                'A': A,
            }
            if verbose:
                print(f"  {label:>25s}: χ²={best[0]:8.2f}, "
                      f"H₀={best[1]:6.1f}, Ω_m={best[2]:.4f}")
    
    return results


def scan_A_amplitude(eps=0.1545, zc=0.6, H0_fixed=None, Om_fixed=None):
    """Scan oscillation amplitude A and see χ² impact."""
    As = np.logspace(-4, 0, 20)  # A = 0.0001 to 1.0
    
    # First find best-fit H0, Om for A=0 (baseline)
    if H0_fixed is None or Om_fixed is None:
        print("Finding best-fit H₀, Ω_m for IDM baseline (ε=0.1545, A=0)...")
        base = scan_H0_Om(eps_list=[eps], A_list=[0.0], zc=zc, verbose=False)
        H0_best = base[f"ε={eps:.4f}, A={0.0000}"]['H0']
        Om_best = base[f"ε={eps:.4f}, A={0.0000}"]['Om']
        chi2_base = base[f"ε={eps:.4f}, A={0.0000}"]['chi2']
    else:
        H0_best = H0_fixed
        Om_best = Om_fixed
        model = IDMModel(H0=H0_best, Om=Om_best, eps=eps, zc=zc, A_osc=0.0)
        chi2_base, _ = chi2_total(model)
    
    print(f"\n  Baseline (A=0): H₀={H0_best:.1f}, Ω_m={Om_best:.4f}, χ²={chi2_base:.1f}")
    print(f"\n  {'A':>10} {'χ²':>10} {'Δχ²':>10} {'χ²_H(z)':>10} {'χ²_BAO':>10} {'Sig(σ)':>10}")
    print(f"  {'-'*50}")
    
    results = []
    for A in As:
        model = IDMModel(H0=H0_best, Om=Om_best, eps=eps, zc=zc, A_osc=A)
        c_t, det = chi2_total(model)
        dchi2 = c_t - chi2_base
        sigma = np.sqrt(max(0, dchi2))
        results.append((A, c_t, dchi2, det))
        print(f"  {A:>10.6f} {c_t:>10.2f} {dchi2:>+10.2f} {det['H(z)']:>10.1f} {det['BAO']:>10.1f} {sigma:>10.2f}")
    
    return H0_best, Om_best, chi2_base, results


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 65)
    print("  Branch 1e Oscillation Constraint  BAO + H(z)")
    print("=" * 65)
    
    # Step 1: Compare fixed-H₀,Ω_m models at the SAME baseline params
    print("\n" + "─" * 60)
    print("  Phase 1: 3-model comparison at fixed H₀=67.4, Ω_m=0.315")
    print("─" * 60)
    
    H0_fixed = 67.4
    Om_fixed = 0.315
    
    models = [
        ("ΛCDM",           IDMModel(H0=H0_fixed, Om=Om_fixed, eps=0.0,    A_osc=0.0)),
        ("IDM baseline",   IDMModel(H0=H0_fixed, Om=Om_fixed, eps=0.1545, A_osc=0.0)),
        ("IDM+Branch1e",   IDMModel(H0=H0_fixed, Om=Om_fixed, eps=0.1545, A_osc=0.008, gamma_osc=3.13, omega_osc=2.25, phi_osc=-0.836)),
    ]
    
    print(f"\n{'Model':<20} {'χ²_H(z)':>10} {'χ²_BAO':>10} {'χ²_total':>10} {'Δχ²':>10}")
    print(f"  {'-'*60}")
    
    base_chi2 = None
    for name, model in models:
        c_t, det = chi2_total(model)
        if base_chi2 is None:
            base_chi2 = c_t
            dchi2 = 0.0
        else:
            dchi2 = c_t - base_chi2
        print(f"  {name:<20s} {det['H(z)']:>10.1f} {det['BAO']:>10.1f} {c_t:>10.1f} {dchi2:>+10.2f}")
    
    # Step 2: Full H₀, Ω_m marginalization for each model
    print("\n" + "─" * 60)
    print("  Phase 2: 3-model scan (best-fit H₀, Ω_m each)")
    print("─" * 60)
    
    eps_list = [0.0, 0.1545, 0.1545]
    A_list   = [0.0, 0.0,    0.008]
    labels   = ['ΛCDM', 'IDM baseline', 'IDM+Branch1e']
    
    results = []
    for eps, A, label in zip(eps_list, A_list, labels):
        print(f"\n  Scanning {label}...")
        r = scan_H0_Om(eps_list=[eps], A_list=[A], zc=0.6, verbose=True)
        r_full = r[f"ε={eps:.4f}, A={A:.4f}"]
        results.append((label, r_full))
    
    print("\n" + "─" * 60)
    print("  Phase 3: Results Comparison")
    print("─" * 60)
    
    best_results = []
    for label, r in results:
        best_results.append(r)
        print(f"\n  {label}")
        print(f"    χ² = {r['chi2']:.2f}")
        print(f"    H₀ = {r['H0']:.1f}, Ω_m = {r['Om']:.4f}")
        print(f"    per-dataset: H(z) χ² = {r['det']['H(z)']:.1f}, BAO χ² = {r['det']['BAO']:.1f}")
    
    # Δχ² between oscillation and baseline
    br = best_results
    d_osc_base = br[2]['chi2'] - br[1]['chi2']
    d_base_lcdm = br[1]['chi2'] - br[0]['chi2']
    d_osc_lcdm = br[2]['chi2'] - br[0]['chi2']
    
    print(f"\n  {'─'*48}")
    print(f"  {'Δχ²(osc − baseline)':<30s} {d_osc_base:>+8.2f}")
    print(f"  {'Δχ²(baseline − ΛCDM)':<30s} {d_base_lcdm:>+8.2f}")
    print(f"  {'Δχ²(osc − ΛCDM)':<30s} {d_osc_lcdm:>+8.2f}")
    print(f"  {'─'*48}")
    
    if d_osc_base > 2:
        print(f"\n  ❌ Branch 1e oscillation IS detectable!")
        print(f"     Δχ² = {d_osc_base:.2f} > 2 → ruled out at ~√{d_osc_base:.1f}σ")
    elif d_osc_base > 0:
        print(f"\n  ⚠️  Branch 1e oscillation weakly constrained: Δχ² = {d_osc_base:.2f}")
    else:
        print(f"\n  ✅ Branch 1e oscillation is undetectable (Δχ² = {d_osc_base:.2f})")
        print(f"     IDM baseline preferred OVER oscillation within current data")
    
    # Step 4: Scan oscillation amplitude
    print("\n\n" + "─" * 60)
    print("  Phase 4: Amplitude scan A ∈ [10⁻⁴, 1]")
    print("─" * 60)
    
    H0_best, Om_best, chi2_base, amp_scan = scan_A_amplitude(
        eps=0.1545, zc=0.6, H0_fixed=br[1]['H0'], Om_fixed=br[1]['Om'])
    
    # Find 95% CL upper limit on A
    print(f"\n  {'─'*48}")
    for A, c_t, dchi2, det in amp_scan:
        if dchi2 > 2.71:  # 1-parameter 95% CL (Δχ²=2.71)
            print(f"  95% CL upper limit on oscillation amplitude A: < {A:.6f}")
            break
    else:
        print(f"  No 95% CL bound — oscillation fully degenerate within data")
    
    print(f"\n{'='*65}")
    
    # Save results
    out = {
        'fixed_params': {
            'H0_fixed': H0_fixed, 'Om_fixed': Om_fixed,
            'models': [
                {'name': 'LCDM', 'chi2_total': None},
                {'name': 'IDM_baseline', 'chi2_total': None},
                {'name': 'IDM_Branch1e', 'chi2_total': None},
            ]
        },
        'best_fit': [
            {'label': label, 'chi2': r['chi2'], 'H0': r['H0'], 'Om': r['Om'],
             'det': r['det']}
            for label, r in zip(labels, best_results)
        ],
        'amplitude_scan': [
            {'A': A, 'chi2': c_t, 'dchi2': dchi2}
            for A, c_t, dchi2, _ in amp_scan
        ],
        'deltas': {
            'osc_minus_baseline': d_osc_base,
            'baseline_minus_lcdm': d_base_lcdm,
            'osc_minus_lcdm': d_osc_lcdm,
        }
    }
    
    with open('/home/wsl/IDM-Lagrangian-Reverse-Engineering/results/branch1e_constraint.json', 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\n  Results saved to results/branch1e_constraint.json")


if __name__ == '__main__':
    main()
