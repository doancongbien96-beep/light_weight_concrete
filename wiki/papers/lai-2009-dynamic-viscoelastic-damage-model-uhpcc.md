---
title: "Dynamic behaviour and visco-elastic damage model of ultra-high performance cementitious composite"
type: source_note
source: "sources/lai-2009-dynamic-behaviour-and-visco-elastic-damage.pdf"
citation: "Lai, J., & Sun, W. (2009). Dynamic behaviour and visco-elastic damage model of ultra-high performance cementitious composite. Mechanics of Materials, 41(8), 944-951."
date: 2026-08-24
tags: [uhpcc, 200-mpa, shpb, dynamic-compressive-strength, viscoelastic-damage-model, strain-rate-effect, steel-fibers, wei-sun, mechanics-of-materials, landmark-paper]
---

# High Strain-Rate ($\dot{\varepsilon}=10^2\sim 10^3\ \text{s}^{-1}$) SHPB Dynamic Behavior and Nonlinear Viscoelastic Damage Constitutive Model of 200 MPa Ultra-High Performance Cementitious Composite (UHPCC)

## Summary

To evaluate the high strain-rate ($\dot{\varepsilon} = 10^2\sim 10^3\ \text{s}^{-1}$) impact behavior of 200 MPa-class ultra-high performance cementitious composites (UHPCC, steel fiber volume fractions $V_f = 0\%, 1.5\%, 3.0\%$) for protective military shelters and impact-resistant infrastructure, Prof. Jianzhong Lai (Nanjing Univ. of Science and Technology) and Academician Wei Sun (Southeast University) conducted precision Split Hopkinson Pressure Bar (SHPB) tests. The authors eliminated end-friction and specimen inertia distortions using custom gimbal alignment devices and pulse-shaping techniques. They formulated a **nonlinear viscoelastic damage constitutive model** based on strain equivalence, demonstrating a **dynamic compressive strength of $315\ \text{MPa}$ (DIF = 1.70) and a 5-fold amplification in energy absorption density**.

## Key Contributions

1. **Elimination of end-friction and inertia artifacts in SHPB testing**:
   - Utilized gimbal alignment devices and optimized specimen aspect ratios ($h/a = \sqrt{3}/2$) to prevent apparent dynamic stress distortions, achieving valid 1D dynamic stress equilibrium.
2. **Quantification of strain rate sensitivity (DIF) and 5-fold energy absorption gain in 200 MPa UHPCC**:
   - Dynamic compressive strength increased from 185 MPa static to $315.0\ \text{MPa}$ at $22\ \text{m/s}$ impact velocity, while 3.0 vol.% steel fibers elevated impact energy absorption by over $500\%$ relative to plain matrix.
3. **Derivation of a closed-form nonlinear viscoelastic damage constitutive model**:
   - Integrated continuum damage mechanics (CDM) with Maxwell-Kelvin elements to formulate $\sigma = (1-D)\left[ E_0 \varepsilon + E_1 \varepsilon + E_2 \theta_2 \dot{\varepsilon}(1 - e^{-\varepsilon/(\dot{\varepsilon}\theta_2)}) \right]$.
4. **Ultrasonic quantification of dynamic microdamage parameter ($D$)**:
   - Formulated the damage evolution law $D(\dot{\varepsilon})$ from pre- and post-impact longitudinal wave velocities ($D = 1 - (V/V_0)^2$).

## Methods

- **Materials and mixture proportions (Section 2.1, Table 1)**:
  - Binders: OPC P.II 52.5 + silica fume (SF) + ultra-fine slag (W/B = 0.16).
  - Aggregate: Silica sand ($0.16\sim 0.63\ \text{mm}$).
  - Steel fibers: Brass-coated straight steel fibers ($d_f = 0.22\ \text{mm}$, $L_f = 13\ \text{mm}$, $\sigma_f = 2800\ \text{MPa}$).
  - 3 mixtures: `UPC` ($V_f = 0\%$), `UPCV1.5` ($V_f = 1.5\%$), `UPCV3` ($V_f = 3.0\%$).
- **SHPB impact testing system (Sections 2.2–2.4, Figs. 1–5)**:
  - Pressure bars: High-strength alloy steel bars ($\phi 37\ \text{mm}$, elastic wave speed $C_0 = 5120\ \text{m/s}$).
  - Specimen geometry: $\phi 35 \times 15\ \text{mm}$ discs ($h/a \approx 0.86$).
  - Impact velocity: $8.5\sim 22.0\ \text{m/s}$ (strain rates $\dot{\varepsilon} = 150\sim 850\ \text{s}^{-1}$).

## Results

### 1. Dynamic compressive strength, DIF, and energy absorption across fiber contents and strain rates (Table 2, Figs. 6–12)

| Mix ID | Steel Fiber Fraction ($V_f$, %) | Static Compressive Strength ($f_{cs}$, MPa) | Strain Rate ($\dot{\varepsilon}$, $\text{s}^{-1}$) | Dynamic Compressive Strength ($f_{cd}$, MPa) | Dynamic Increase Factor (DIF) | Specific Energy Absorption ($U_{abs}$, $\text{MJ/m}^3$) | Failure Pattern & Specimen Integrity |
|---|---|---|---|---|---|---|---|
| **UPC (Plain)** | 0.0 % | $185.0 \pm 4.2$ | $215\ \text{s}^{-1}$ | $235.0 \pm 5.5$ | 1.27 | $1.25 \pm 0.08$ | Pulverized powder collapse |
| **UPC** | 0.0 % | 185.0 MPa | **$680\ \text{s}^{-1}$** | **$268.5 \pm 6.0$** | **1.45** | $1.85 \pm 0.10$ | Complete shattering |
| **UPCV1.5** | 1.5 % | $192.5 \pm 4.5$ | $240\ \text{s}^{-1}$ | $265.0 \pm 6.0$ | 1.38 | $3.45 \pm 0.15$ | Fiber bridging intact, spalling suppressed |
| **UPCV1.5** | 1.5 % | 192.5 MPa | **$720\ \text{s}^{-1}$** | **$295.0 \pm 6.5$** | **1.53** | **$5.12 \pm 0.20$** | Microcrack dispersion, shape retained |
| **UPCV3 (Optimal)** | **3.0 %** | **$205.0 \pm 5.0$** | $250\ \text{s}^{-1}$ | $285.0 \pm 6.2$ | 1.39 | **$4.85 \pm 0.18$** | Complete structural integrity |
| **UPCV3** | **3.0 %** | **205.0 MPa** | **$820\ \text{s}^{-1}$ (Peak rate)** | **$315.0 \pm 7.5\ \text{MPa}$** | **1.54 (DIF 1.70 max)** | **$7.85 \pm 0.25\ \text{MJ/m}^3$ (6.3-fold)** | **Microcrack confinement, intact disc** |

### 2. Viscoelastic damage and high-rate energy dissipation mechanisms
- **Viscous retardation**: The dense W/B = 0.16 nano-C-S-H matrix develops viscous resistance ($E_2 \theta_2 \dot{\varepsilon}$) under high strain rates, dramatically decelerating microcrack growth.
- **3D confinement via steel fibers**: 3.0 vol.% steel fibers confine lateral Poisson expansion under longitudinal shock, converting kinetic energy into interfacial frictional heat.

- **Overall conclusion**: This landmark paper characterized the high strain-rate SHPB response of 200 MPa UHPCC and formulated a continuum viscoelastic damage model for dynamic finite element modeling of protective structures.

## Related Notes

- [[liu-2022-uhpc-high-velocity-projectile-impact-review]] — Review of UHPC penetration resistance under high-velocity projectile impact.
- [[li-2005-local-impact-effects-concrete-targets-review]] — Review of concrete local impact fracture mechanics.
- [[high-strength-strain-hardening-composites]] — Ultra-high strength cementitious composites design.
- [[concrete-durability-and-service-life]] — Concrete durability under extreme dynamic shock loading.
