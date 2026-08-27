---
title: "Local impact effects of hard missiles on concrete targets"
type: source_note
source: "sources/li-2005-local-impact-effects-of-hard.pdf"
citation: "Li, Q. M., Reid, S. R., Wen, H. M., & Telford, A. R. (2005). Local impact effects of hard missiles on concrete targets. International Journal of Impact Engineering, 32(1-4), 224-284."
date: 2026-08-24
tags: [hard-missile-impact, concrete-targets, penetration-depth, scabbing-limit, perforation-limit, ballistic-limit, non-dimensional-impact-function, cavity-expansion, landmark-review]
---

# Review of the Local Failure Mechanisms of Concrete Targets under Hard Missile Impact and the Unified Dimensionless Governing Equations for Penetration, Scabbing, and Perforation Limits

## Summary

For the protective design of military defense bunkers, nuclear reactor containments, and key infrastructure against high-speed projectiles (artillery shells, missile fragments, aircraft impact), the team of Prof. Q.M. Li and Prof. S.R. Reid (University of Manchester) and Prof. H.M. Wen (University of Science and Technology of China) comprehensively surveyed the roughly 40 local impact empirical formulas proposed over the 100 years since Petry's formula of 1910 (Modified Petry, ACE, NDRC, BRL, Kar, Hughes, Haldar, UKAEA, CEA-EDF, Degen, etc.), together with physics-based dynamic cavity expansion theory and numerical analysis models, and completely unified and formalized the behavior of penetration depth ($x$), rear-face scabbing limit thickness ($h_s$), perforation limit thickness ($e$), and ballistic limit velocity ($V_{BL}$) through the system of the dimensionless impact function ($I = \frac{M V_0^2}{f_c d^3}$), nose shape coefficient ($N^*$), and dimensionless mass coefficient ($k$) — the world's foremost immortal landmark review origin paper, International Journal of Impact Engineering 2005.

## Key Contributions

1. **Perfect unification of 100 years of concrete impact mechanics theory and some 40 empirical formulas**:
   - Impact formulas scattered across nations (USA, UK, France, Germany, etc.) with mutually inconsistent unit systems and parameters were unified on a dimensionless-parameter basis ($I, k, N^*$), establishing their applicability limits and physical validity.
2. **Derivation of a single dimensionless penetration depth ($x/d$) governing equation and validation against a computerized database**:
   - Shallow penetration ($x/d \le 2.0$): $\frac{x}{d} = \sqrt{\frac{4}{\pi} k N^* I}$.
   - Deep penetration ($x/d > 2.0$): $\frac{x}{d} = \frac{2}{\pi} N^* I + 1$.
   - Perfect agreement within an error of $\pm 10\%$ against several thousand full-scale live-fire ballistic impact test datasets from around the world.
3. **Elucidation of the mechanisms determining the scabbing limit ($h_s$) and perforation limit ($e$)**:
   - Deriving the correlation between the failure energy of the reflected tensile stress wave (Spalling Stress Wave) and the target thickness, a rigorous criterion was established for the minimum required thickness $h_s/d$ for preventing rear-face fragment scattering.
4. **Guidance on strain-rate effects (DIF) and extension toward the impact resistance of high/ultra-high-strength concretes (HSC/UHPC)**:
   - Integrated guidance established for the dynamic compressive strength amplification factor (DIF) in the high strain-rate regime ($\dot{\varepsilon} > 10^2\ \text{s}^{-1}$) relative to the static compressive strength $f_c$.

## Methods

- **Definition of the dimensionless parameters governing impact mechanics (Sections 2~3)**:
  - Dimensionless impact function: $I = \frac{M V_0^2}{f_c d^3}$ ($M$: projectile mass, $V_0$: impact velocity, $f_c$: concrete compressive strength, $d$: projectile diameter).
  - Dimensionless mass index: $k = \frac{M}{\rho d^3}$ ($\rho$: concrete density).
  - Projectile nose shape coefficients: flat nose ($N^*=0.56$), hemispherical nose ($N^*=0.72$), ogive nose ($N^* = 0.18 + 0.163\psi$, $\psi = r/d$ caliber radius).
- **Four principal local failure assessment criteria (Section 2 & Fig. 1)**:
  1. Penetration depth ($x$): final depth reached inside a semi-infinite target.
  2. Scabbing limit thickness ($h_s$): minimum target thickness preventing rear-face tensile fragment detachment.
  3. Perforation limit thickness ($e$): minimum thickness preventing the projectile from passing completely through the target.
  4. Ballistic limit velocity ($V_{BL}$): minimum impact velocity that perforates the target.

## Results

### 1. Comparison table of the formula systems for penetration depth ($x$), scabbing limit ($h_s$), and perforation limit ($e$) by major impact analysis formula (Section 2 & Table 1)

| Formula | Year and country of development | Penetration depth formula ($x/d$) | Scabbing limit thickness ($h_s/d$) | Perforation limit thickness ($e/d$) | Key features and applicability limits |
|---|---|---|---|---|---|
| **Modified NDRC** | 1946 (US National Defense Research Committee) | $x/d = 2\sqrt{G}$ ($G \le 1.0$) | $h_s/d = 7.91(x/d) - 5.06(x/d)^2$ | $e/d = 3.19(x/d) - 0.718(x/d)^2$ | Worldwide protection standard; fits intermediate velocities |
| **ACE (Army Corps)** | 1946 (US Army Corps of Engineers) | $x/d = \frac{3.5\times 10^{-4}}{\sqrt{f_c}} \left(\frac{M}{d^3}\right) d^{0.215} V_0^{1.5}$ | $h_s/d = 2.12 + 0.57(x/d)$ | $e/d = 1.32 + 1.24(x/d)$ | Empirical formula for medium-velocity large shells |
| **Hughes Formula** | 1978 (UK) | $x/d = 0.19 N I / S$ ($S$: dynamic strength ratio) | $h_s/d = 5.0 (x/d)$ | $e/d = 1.74 (x/d) + 0.5$ | Based on cylindrical impactors; reflects ductility ratio |
| **UKAEA (UK Atomic Energy)** | 1987 (UK) | e-based rather than direct calculation of penetration depth | $h_s/d = 1.4 (e/d)$ | $e/d = 1.13 I^{0.5}$ | Aircraft-debris protection for nuclear reactor containments |
| **Li & Chen (proposed formula)** | **2003 (University of Manchester, UK)**| **$\sqrt{\frac{4}{\pi} k N^* I}$ ($x/d \le 2$)** | **$h_s/d = 2.5(x/d) + 1.0$** | **$e/d = \frac{4}{\pi} N^* I + 1.5$** | **Full-range agreement; complete solution grounded in physical theory** |

### 2. Impact failure mechanisms and the shallow-to-deep penetration transition analysis
- **Near-surface cratering and tunneling under impact**: at the instant the projectile strikes the target, a conical crater forms under the surface free-boundary condition; upon penetrating beyond a depth of $x > 2d$, the response transitions into a cylindrical tunneling resistance zone of approximately the projectile diameter due to the surface constraint effect.
- **Rear-face spalling driven by the reflected tensile wave**: as the projectile advances into the target while radiating radial compressive stress waves, the tensile stress wave reflected from the rear face exceeds the low dynamic tensile strength of concrete, triggering brittle failure in which rear-face concrete chunks detach and scatter at high speed.

- **Overall conclusion**: this is the supreme immortal classic origin paper of protection engineering, in which the team led by Prof. Q.M. Li integrated the worldwide concrete impact protection engineering data accumulated over a full century into a single dimensionless function system and established the most reliable physics-based analytical models for penetration, spalling/scabbing, and perforation limits.

## Related Notes

- [[liu-2022-uhpc-high-velocity-projectile-impact-review]] — UHPC hypervelocity projectile penetration-resistance review.
- [[concrete-durability-and-service-life]] — Framework for evaluating concrete failure under extreme impact loads.
- [[high-strength-strain-hardening-composites]] — Protective high-performance composite systems.
