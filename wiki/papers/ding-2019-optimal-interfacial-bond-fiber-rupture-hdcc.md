---
title: "Theoretical analysis on optimal fiber-matrix interfacial bonding and corresponding fiber rupture effect for high ductility cementitious composites"
type: source_note
source: "sources/ding-2019-theoretical-analysis-on-optimal-fiber-matrix.pdf"
citation: "Ding, C., Guo, L. P., & Chen, B. (2019). Theoretical analysis on optimal fiber-matrix interfacial bonding and corresponding fiber rupture effect for high ductility cementitious composites. Construction and Building Materials, 228, 116743."
date: 2026-08-23
tags: [fiber-bridging-theory, interfacial-bond, fiber-rupture, micromechanics-design, complementary-energy, pva-fiber, pe-fiber, liping-guo, theory-foundation]
---

# Theoretical Analysis on Optimal Fiber-Matrix Interfacial Bonding, Fiber Rupture Effects, and Maximization of Bridging Complementary Energy in High Ductility Cementitious Composites (HDCC)

## Summary

In strain-hardening cementitious composites (HDCC/ECC), if the fiber-matrix interfacial shear bond ($\tau_0$) is too weak, steady-state flat crack propagation cannot occur due to insufficient bridging stress ($\sigma_0$); conversely, if it is too strong, early fiber rupture drastically reduces complementary energy ($J'_b$). To resolve this dilemma, Professor Li Ping Guo and co-workers at Southeast University developed a fully analytical fiber bridging constitutive model ($\sigma-\delta$) that couples fiber debonding and pullout, inclined snubbing effects ($f$), Cook-Gordon pulley effects ($f'$), and fiber rupture criteria dependent on embedded depth and orientation angle. The study derived the **optimal interfacial shear bond strength ($\tau_0^{opt}$)** that maximizes complementary energy ($J'_b$) and established allowable matrix crack-tip toughness thresholds ($J_{tip}, K_m$) for four representative fibers (PVA, PET, PE, and steel fibers). Contrary to the conventional assumption that pure pullout without fiber rupture is strictly optimal, the mathematical analysis proved that **moderate, controlled fiber rupture (approximately 10~25 % rupture) allows coupled interfacial friction and pullout energy to achieve theoretical maximums for complementary energy ($J'_b$) and bridging stress ($\sigma_0$)**. Optimal interfacial bond ranges were determined for PVA ($\tau_0^{opt} = 1.6\ \text{MPa}$), PET ($1.4\ \text{MPa}$), PE ($2.2\ \text{MPa}$), and steel fibers ($12.0\ \text{MPa}$), establishing guidelines for fiber oil-coating and matrix chemical tailoring.

## Key Contributions

1. **Proof of bridging complementary energy ($J'_b$) maximization under moderate fiber rupture**:
   - Demonstrated that compared to overly weak interfaces ($\tau_0 < 1.0\ \text{MPa}$) without rupture, complementary energy $J'_b$ peaks at the optimal shear strength ($\tau_0^{opt}$) where inclined fibers undergo partial rupture while sustaining high frictional pullout stresses.
2. **Quantitative determination of optimal interfacial bond strength ($\tau_0^{opt}$) for four major reinforcing fibers**:
   - **PVA fiber**: $\tau_0^{opt} = 1.6\ \text{MPa} \rightarrow J'_b = 87.1\ \text{J/m}^2$, $\sigma_0 = 4.8\ \text{MPa}$ (requires $J_{tip} \le 29.0\ \text{J/m}^2$).
   - **PET fiber**: $\tau_0^{opt} = 1.4\ \text{MPa} \rightarrow J'_b = 58.2\ \text{J/m}^2$, $\sigma_0 = 3.6\ \text{MPa}$ (requires $J_{tip} \le 19.4\ \text{J/m}^2$).
   - **PE fiber**: $\tau_0^{opt} = 2.2\ \text{MPa} \rightarrow J'_b = 245.0\ \text{J/m}^2$, $\sigma_0 = 14.5\ \text{MPa}$ (requires $J_{tip} \le 81.6\ \text{J/m}^2$).
   - **Steel fiber**: $\tau_0^{opt} = 12.0\ \text{MPa} \rightarrow J'_b = 480.0\ \text{J/m}^2$, $\sigma_0 = 18.2\ \text{MPa}$.
3. **Establishment of matrix design boundary conditions ($K_m, \sigma_{cr}$) for PSH criteria satisfaction**:
   - Derived closed-form equations for maximum allowable matrix fracture toughness ($K_m$) to satisfy pseudo-strain-hardening indices ($\text{PSH}_E = J'_b/J_{tip} \ge 3.0$, $\text{PSH}_S = \sigma_0/\sigma_{cr} \ge 1.5$) based on the bridging potential of each fiber.

## Methods

- **Parameters of the four analyzed fiber types (Table 1)**:
  - **PVA fiber**: $L_f = 12\ \text{mm}, d_f = 39\ \mu\text{m}, \sigma_{fu} = 1260\ \text{MPa}, E_f = 30\ \text{GPa}$, snubbing coefficients $f = 0.20, f' = 0.33$.
  - **PET fiber**: $L_f = 12\ \text{mm}, d_f = 38\ \mu\text{m}, \sigma_{fu} = 1160\ \text{MPa}, E_f = 11.5\ \text{GPa}, f = 0.39, f' = 0.20$.
  - **PE fiber**: $L_f = 12\ \text{mm}, d_f = 28\ \mu\text{m}, \sigma_{fu} = 3000\ \text{MPa}, E_f = 100\ \text{GPa}, f = 0.49, f' = 0.10$.
  - **Steel fiber**: $L_f = 12\ \text{mm}, d_f = 160\ \mu\text{m}, \sigma_{fu} = 2500\ \text{MPa}, E_f = 210\ \text{GPa}, f = 0.49, f' = 0.10$.
  - Fiber volume fraction: $V_f = 2.0\ \text{vol.\%}$.
- **Governing equations of the unified bridging stress-crack opening ($\sigma-\delta$) model (Eq. 8)**:
  - Fiber rupture load capacity: $P_{rup}(\theta) = \frac{\pi}{4} d_f^2 \sigma_{fu} \cdot e^{-f'\theta}$.
  - Critical embedded length $l_d$: $P_{max}(l_d, \theta) = P_{rup}(\theta) \rightarrow l_d(\theta) = \frac{d_f \sigma_{fu} e^{-(f+f')\theta}}{4\tau_0}$.
  - 3D spatial integration:
    $$\sigma_c(\delta) = \frac{V_f}{L_f} \left[ \int_0^{\theta_c} \int_0^{l_d} P_{pull}(\delta) \sin 2\theta dL_e d\theta + \int_0^{\theta_c} \int_{l_d}^{L_f/2} P_{deb}(\delta) \sin 2\theta dL_e d\theta + \cdots \right]$$
  - Complementary energy evaluation: $J'_b = \sigma_0 \delta_0 - \int_0^{\delta_0} \sigma(\delta) d\delta$.

## Results

### 1. Optimal interfacial parameters and PSH design criteria limits across fiber types

| Fiber type | Tensile strength ($\sigma_{fu}$, MPa) | Optimal interfacial shear strength ($\tau_0^{opt}$, MPa) | Peak bridging stress ($\sigma_0$, MPa) | Maximum complementary energy ($J'_b$, $\text{J/m}^2$) | Fiber rupture fraction at optimum (%) | Maximum allowable crack-tip toughness ($J_{tip}^{max}$, $\text{J/m}^2$) | Maximum allowable matrix fracture toughness ($K_m^{max}$, $\text{MPa}\cdot\sqrt{\text{m}}$) |
|---|---|---|---|---|---|---|---|
| **PVA fiber** | 1260 MPa | **1.6 MPa** | **4.8 MPa** | **87.1** | **18 %** | **29.0** | **0.76** |
| **PET fiber** | 1160 MPa | **1.4 MPa** | **3.6 MPa** | **58.2** | **15 %** | **19.4** | **0.62** |
| **PE fiber** | **3000 MPa** | **2.2 MPa** | **14.5 MPa** | **245.0** | **12 %** | **81.6** | **1.28 (accommodates ultra-high strength)** |
| **Steel fiber** | 2500 MPa | **12.0 MPa** | **18.2 MPa** | **480.0** | **22 %** | **160.0** | **1.78** |

### 2. Micromechanical design and fiber surface tailoring guidelines
- **Oil-coating optimization**: Untreated PVA fibers exhibited $\tau_0 > 3.5\ \text{MPa}$ due to hydrophilic hydrogen bonding, leading to over 80 % premature rupture; applying 1.2 wt.% oil coating **precisely regulates $\tau_0$ to 1.6 MPa**, maximizing $J'_b$.
- **PE fiber performance advantages**: Due to high tensile strength (3000 MPa) and long critical rupture embedment length, PE fibers achieved $J'_b = 245\ \text{J/m}^2$ at $\tau_0 = 2.2\ \text{MPa}$, sustaining stable PSH strain-hardening even in ultra-high strength matrices ($K_m \approx 1.0$) exceeding 100 MPa.

- **Overall conclusion**: This theoretical analysis reframed fiber rupture from a defect into a design parameter for complementary energy maximization, establishing closed-form formulations for optimal interfacial shear strengths and matrix compatibility criteria.

## Related Notes

- [[fiber-bridging-constitutive-law]] — Fiber bridging $\sigma-\delta$ constitutive laws and single-fiber pullout mechanics.
- [[pseudo-strain-hardening-criteria]] — PSH energy ($J'_b/J_{tip}$) and strength criteria.
- [[high-strength-strain-hardening-composites]] — PE fiber bridging design in high-strength composites (UHDCC).
- [[strain-hardening-mechanism]] — Micromechanical design principles of strain-hardening composites.
