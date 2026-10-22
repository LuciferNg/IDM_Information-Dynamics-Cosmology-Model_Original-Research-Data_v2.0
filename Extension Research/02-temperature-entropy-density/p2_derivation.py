"""P2: Temperature = entropy density — HONEST VERSION 2026-07-01

The claim "T = dS/dV is universal" is WRONG as a universal statement.
Standard thermodynamics: 1/T = (∂S/∂E)_V, while ∂S/∂V = P/T (the Gibbs relation).

For BH and Unruh horizons, T IS proportional to dS/dV, but this is a 
COINCIDENCE of specific horizon geometries (S ∝ R², V ∝ R³), not a
universal law. This file documents this honestly.
"""
import sys
sys.path.insert(0, '/home/wsl/IDM-Lagrangian-Reverse-Engineering')
from src.hubble import H0, Omega_m, Omega_r, Omega_L, E2
import numpy as np

G_N = 6.67430e-11
c = 299792458
hbar = 1.054571817e-34
kB = 1.380649e-23

m_Pl = np.sqrt(hbar * c / G_N)
l_Pl = np.sqrt(hbar * G_N / c**3)
t_Pl = np.sqrt(hbar * G_N / c**5)
T_Pl = m_Pl * c**2 / kB

print("="*66)
print("P2: TEMPERATURE = ENTROPY DENSITY — HONEST VERSION")
print("="*66)
print()

# ── T1: Dimensional analysis ──
print("─"*66)
print("T1: DIMENSIONAL ANALYSIS")
print("─"*66)
print()
print("In Planck units (hbar=c=kB=G=1):")
print("  [T] = 1, [S] = 1, [V] = 1, [dS/dV] = 1")
print("  -> [T] = [dS/dV] is DIMENSIONALLY CONSISTENT ✅")
print()
print("In SI units:")
print("  [T] = K, [S] = J/K, [V] = m^3")
print("  [dS/dV] = J/(K·m^3) ≠ K")
print("  -> NOT dimensionally consistent in SI without conversion factor")
print("  -> The conversion factor is kB (Boltzmann constant)")
print("  -> T = kB^(-1) · (T_Pl/l_Pl^3)^(-1) · dS/dV in physical units")
print()
print("KEY POINT: The claim T = dS/dV only works in natural units where")
print("kB = 1. In physical units, T = (some constant) x dS/dV where the")
print("constant has dimensions of [K·m^3]. This is NOT a prediction — it's")
print("a UNIT CONVENTION. ✅ (trivial)")
print()

# ── Standard thermodynamics ──
print("─"*66)
print("STANDARD THERMODYNAMICS: The Gibbs Relation")
print("─"*66)
print()
print("  dS = (1/T) dE + (P/T) dV - (mu/T) dN")
print()
print("From this:")
print("  1/T = (∂S/∂E)_V,N   ← FUNDAMENTAL TEMPERATURE DEFINITION")
print("  P/T = (∂S/∂V)_E,N   ← THIS IS PRESSURE, NOT TEMPERATURE")
print()
print("The claim T = dS/dV substitutes (∂S/∂V) for 1/T = (∂S/∂E).")
print("These are DIFFERENT thermodynamic derivatives.")
print()

# ── Counter-example: ideal gas ──
print("─"*66)
print("COUNTER-EXAMPLE: Ideal Gas")
print("─"*66)
print()
print("S = N[ln(V/N) + (3/2)ln(T) + const]")
print("  (∂S/∂V)_E,T = N/V  (at fixed temperature)")
print("  If T = dS/dV were universal: T = N/V")
print("  But T = PV/(N·kB) by ideal gas law")
print("  These are PROPORTIONAL but with different constants")
print("  T = P/(kB · N/V) has P factor — NOT T = dS/dV")
print()
print("CONCLUSION: T ≠ dS/dV for ordinary matter.")
print("The Gibbs relation clearly separates ∂S/∂E (temperature)")
print("from ∂S/∂V (pressure/entropy density).")
print()

# ── Black hole: why it "works" ──
print("─"*66)
print("BLACK HOLE: Why T ∝ dS/dV (special case)")
print("─"*66)
print()

M_arr = np.array([1e-7, 1e-5, 1e-3, 0.1, 1, 10, 100, 1e4])

print("For Schwarzschild BH (Planck units):")
print("  S = A/4 = pi·R^2 = 4pi·M^2")
print("  E = M")
print("  V = 4pi·R^3/3 = 32pi·M^3/3")
print()
print("  Correct thermodynamic temperature:")
print("    1/T = ∂S/∂E = 8pi·M  → T_H = 1/(8pi·M)  ✅")
print()
print("  Entropy density:")
print("    dS/dV = (dS/dM)/(dV/dM) = (8pi·M)/(32pi·M^2) = 1/(4M)")
print()
print("  Relationship:")
print("    T_H = 1/(8pi·M) = (1/(2pi)) · 1/(4M) = (1/2pi) · dS/dV")
print()
print("  This WORKS because S ∝ M^2 and V ∝ M^3:")
print("    dS/dV ∝ M^(2-1)/M^(3-1) = M/M^2 = 1/M")
print("    T_H ∝ 1/M")
print("  Both scale as 1/M → T ∝ dS/dV is a SCALING COINCIDENCE")
print()

print(f"{'M(m_Pl)':<12} {'T_H':<16} {'dS/dV':<16} {'T_H/(dS/dV)':<16} {'1/(2pi)':<12}")
print(f"{'':-<12} {'':-<16} {'':-<16} {'':-<16} {'':-<12}")
for M in M_arr:
    T_H = 1.0 / (8 * np.pi * M)
    dS_dV = 1.0 / (4 * M)
    ratio = T_H / dS_dV if dS_dV != 0 else 0
    print(f"{M:<12.1e} {T_H:<16.6e} {dS_dV:<16.6e} {ratio:<16.6f} {1/(2*np.pi):<12.6f}")

print()
print("T_H / (dS_BH/dV) = 1/(2pi) = 0.159 — UNIVERSAL for Schwarzschild BH")
print("This is a real geometric fact about BH thermodynamics.")
print("But it's NOT evidence for T = dS/dV as a universal law.")
print()

# ── Unruh effect ──
print("─"*66)
print("UNRUH EFFECT: Same coincidence, different geometry")
print("─"*66)
print()
print("  T_U = a/(2pi)")
print("  S_Rindler = pi/a^2")
print("  V_Rindler ~ 4pi/(3a^3)")
print("  dS/dV = a/2")
print("  T_U / (dS/dV) = [a/(2pi)]/[a/2] = 1/pi")
print()
print("  Same pattern: S ∝ a^(-2), V ∝ a^(-3)")
print("  → dS/dV ∝ a, T_U ∝ a → T ∝ dS/dV")
print("  Different geometry → different constant (1/pi vs 1/(2pi))")
print()

# ── CMB ──
print("─"*66)
print("CMB: Stefan-Boltzmann IDENTITY (not a test)")
print("─"*66)
print()
print("  Stefan-Boltzmann: u = a_rad·T^4, s = (4/3)·a_rad·T^3")
print("  T = (3s/(4·a_rad))^(1/3) — this is a DEFINITIONAL IDENTITY")
print("  It says T = f(s), not T = s.")
print()
print("  For T = dS/dV = s, we would need T = s which gives:")
print("  T = (4/3)·a_rad·T^3 → T^2 = 3/(4·a_rad) → T = sqrt(3/(4·a_rad))")
print("  This gives T = O(1) in Planck units — a NUMBER, not a law.")
print()
print("  The Stefan-Boltzmann law is PRESERVED identically regardless")
print("  of whether T = dS/dV or not — it's math, not physics.")
print()

print("="*66)
print("P2 OVERALL VERDICT (HONEST)")
print("="*66)
print()
print("  T1: Dimensional analysis [PASS — but trivial]")
print("       In natural units, [T] = [dS/dV] by construction")
print("")
print("  T2: BH thermodynamics [OBSERVATION — NOT universal law]")
print("       T_H = (1/2pi)·dS_BH/dV is REAL physics for Schwarzschild BH")
print("       But this is a GEOMETRIC COINCIDENCE (S∝M², V∝M³), not universal")
print("")
print("  T3: Unruh effect [SAME PATTERN, different geometry]")
print("       T_U = (1/pi)·dS/dV — real but not universal")
print("")
print("  T4: CMB temperature [IDENTITY, not test]")
print("       Stefan-Boltzmann gives T = f(s) self-consistently by definition")
print("")
print("  T5: Stefan-Boltzmann [IDENTITY, not test]")
print("       u = a_rad·T^4 is preserved — trivially")
print()
print("  CORE CLAIM: T = O(1)·dS/dV is NOT universal.")
print("  It holds for horizon systems (BH, Unruh) where S ∝ R², V ∝ R³.")
print("  For ordinary matter (ideal gas: S ∝ ln(V)), T ≠ dS/dV.")
print()
print("  HONEST VERDICT: The BH/Unruh proportionality is real and interesting,")
print("  but claiming it as a universal law is INCORRECT.")
print("  P2 should be reframed as 'Horizon Thermodynamics' — a subset of the")
print("  Jacobson program (Einstein eq from horizon thermodynamics).")