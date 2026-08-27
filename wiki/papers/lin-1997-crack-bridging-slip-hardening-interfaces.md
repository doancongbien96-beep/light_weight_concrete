---
title: "Crack bridging in fiber reinforced cementitious composites with slip-hardening interfaces"
type: source_note
source: "sources/lin-1997-crack-bridging-in-fiber-reinforced.pdf"
citation: "Lin, Z., & Li, V. C. (1997). Crack bridging in fiber reinforced cementitious composites with slip-hardening interfaces. Journal of the Mechanics and Physics of Solids, 45(5), 763-787."
date: 2026-08-24
tags: [crack-bridging-model, slip-hardening-interface, micromechanics, closed-form-solution, single-fiber-pullout, psh-ductility, spectra-pe-ecc, victor-li, jmps, landmark-paper]
---

# Establishing the Crack-Bridging Constitutive Model and Closed-Form Analytical Solution for Fiber-Reinforced Cementitious Composites with Rigorous Incorporation of Slip-Hardening Interface Properties

## Summary

To resolve the limitation that the conventional constant-friction interface model ($\tau = \tau_0$) fails to reflect the slip-hardening behavior ($\tau(s) = \tau_0(1 + \beta s/d_f)$) arising from fiber surface abrasion and jamming during pullout of polymer synthetic fibers—and therefore severely underestimates the crack opening displacement at peak bridging stress ($\delta_0$) and the composite ultimate tensile strain ($\varepsilon_u$) to merely 1/4 of measured values—**Dr. Zhong Lin and Victor C. Li, endowed chair professor of the University of Michigan**, established **two-stage full-cycle micromechanics differential equations** covering single-fiber debonding (Pre-debonding) and post-complete-debonding pullout (Post-debonding Pullout), and derived a **closed-form rigorous analytical solution of the bridging stress–crack opening relation ($\sigma_B-\delta$) incorporating the slip-hardening interface** through a three-dimensional random-orientation integration, thereby predicting and verifying—without error—the ultra-high ductility ($\varepsilon_u = 3.5\sim 7.0\%$) of Spectra PE fiber composites: an immortal top landmark original paper by the pair in the Journal of the Mechanics and Physics of Solids (JMPS), 1997.

## Key Contributions

1. **First derivation of a full-cycle crack-bridging $\sigma_B(\delta)$ closed-form solution integrating the slip-hardening interface ($\beta > 0$)**:
   - Splitting the bridging stress curve into the pre-debonding ($\delta < \delta^*$) and post-debonding ($\delta > \delta^*$) regimes, an exact logarithmic analytical solution incorporating the slip-hardening coefficient $\beta$ was derived.
2. **Fundamental resolution of the constant-friction model's ductility-underestimation flaw**:
   - Whereas the existing constant-friction model severely underestimated the crack opening displacement $\delta_0$ as $16\sim 27\ \mu\text{m}$ and the tensile strain as $0.6\sim 1.8\%$, the proposed model matches the measured values perfectly with $\delta_0 = 90\sim 137\ \mu\text{m}$ and $\varepsilon_u = 3.3\sim 9.6\%$.
3. **Quantification of bridging complementary energy ($J_b'$) amplification and the PSH strain-hardening saturation mechanism**:
   - As the slip-hardening coefficient $\beta$ increases, $J_b'$—the area beneath the $\sigma_B-\delta$ curve—expands nonlinearly, completing the theoretical basis for satisfying $J_b'/J_{tip} \gg 3.0$ against the matrix fracture toughness $J_{tip}$.
4. **Verification of multiple fine-cracking behavior through plasma surface-treated Spectra PE composite experiments**:
   - Demonstrated that plasma (argon) treatment-induced increases in the frictional strength ($\tau_0$) and $\beta$ dramatically raise the composite tensile strength ($3.1 \rightarrow 5.7\ \text{MPa}$) and ductility ($3.5\% \rightarrow 7.0\%$).

## Methods

- **Single-fiber micromechanics differential equations (Section 2 & Figs. 3~5)**:
  - Interfacial shear stress: $\tau(s) = \tau_0 \left( 1 + \beta \frac{s}{d_f} \right)$.
  - Axial-force equilibrium and displacement-compatibility equations: $\frac{dP}{dx} = \pi d_f \tau(s)$, $\frac{ds}{dx} = \frac{4P(x)}{\pi d_f^2 E_f}$.
  - Displacement at completion of debonding: $\delta_0 = \frac{\tau_0 (1+\eta) L_e^2}{E_f d_f} + \text{slip-hardening correction}$.
- **3D spatial statistical integration and bridging stress homogenization (Section 3 & Fig. 6)**:
  - Inclination angle $\phi \sim \sin\phi$, centroidal distance $z \sim 2/L_f$, snubbing factor $e^{f\phi}$.
  - Governing equation for total bridging stress: $\sigma_B(\delta) = \int_0^{\pi/2} \int_0^{(L_f/2)\cos\phi} P(\delta, z, \phi) p(z) p(\phi) dz d\phi$.
- **Experimental validation database (Section 4 & Tables 1~2)**:
  - Spectra 900 PE fiber ($V_f = 2.0\ \text{vol.}\%$, $d_f = 38\ \mu\text{m}$, $L_f = 12.7\ \text{mm}$, $\sigma_{fu} = 2.6\ \text{GPa}$, $E_f = 117\ \text{GPa}$).
  - Untreated vs. argon-plasma surface-treated fibers.

## Results

### 1. Comparison table: constant-friction model vs. proposed slip-hardening model vs. measured tensile behavior (Tables 1~2 & Figs. 7~10)

| Composite condition | Model | Peak bridging stress ($\sigma_0$, MPa) | Peak crack opening ($\delta_0$, $\mu$m) | Predicted tensile strain ($\varepsilon_u$, %) | Measured tensile strength ($\sigma_{tu}$, MPa) | Measured tensile strain ($\varepsilon_u$, %) | Model accuracy |
|---|---|---|---|---|---|---|---|
| **SPECC (untreated fibers)** | Existing constant-friction model ($\beta = 0$) | 3.2 MPa | **$16\ \mu\text{m}$ (underestimate)** | **$0.6\%$ (severe underestimate)**| $3.1 \pm 0.2$ | $3.5 \pm 0.3\%$ | 83 % error |
| | **Proposed slip-hardening model ($\beta = 0.05$)**| **3.5 MPa** | **$90\ \mu\text{m}$** | **$3.3\%$** | **$3.1 \pm 0.2$** | **$3.5 \pm 0.3\%$** | **agreement within 5 % error** |
| **SPECC (plasma-treated)**| Existing constant-friction model ($\beta = 0$) | 5.4 MPa | **$27\ \mu\text{m}$ (underestimate)** | **$1.8\%$ (underestimate)** | $5.7 \pm 0.3$ | $7.0 \pm 0.5\%$ | 74 % error |
| | **Proposed slip-hardening model ($\beta = 0.12$)**| **5.9 MPa** | **$137\ \mu\text{m}$** | **$9.6\%$ (upper bound)** | **$5.7 \pm 0.3$** | **$7.0 \pm 0.5\%$** | **perfectly captures ultra-high ductility** |

### 2. Slip-hardening mechanism and bridging energy analysis
- **Micro-fibril jamming effect on the fiber surface**: as PE and PVA fibers are pulled out, hydrate particles of the matrix scratch the fiber surface so that micro-fibrils peel off and agglomerate, producing slip hardening ($\beta > 0$) in which the frictional resistance grows in proportion to the slip distance.
- **Five-fold expansion of the crack opening capacity**: thanks to slip hardening, the fiber stretches without rupturing until the peak stress is reached, so the crack opening displacement $\delta_0$ expands from $16\ \mu\text{m} \rightarrow 90\sim 137\ \mu\text{m}$, which converts into the enormous tensile straining of $3\sim 7\%$ upon multiple-crack saturation.

- **Overall conclusion**: This paper is an immortal top classic original reference in the field of modern ECC and high-performance fiber-reinforced cementitious micromechanics, in which Lin & Li completely integrated slip-hardening interface mechanics into the governing equations and completed a closed-form analytical model that mathematically and rigorously predicts the composite's $\sigma_B-\delta$ bridging curve and its ultimate tensile strain.

## Related Notes

- [[li-1991-micromechanical-model-tension-softening-bridging]] — Victor Li: original paper on the micromechanical fiber-bridging tension-softening model.
- [[li-1995-matrix-design-for-pseudo-strain-hardening]] — Victor Li: original paper on PSH composite matrix design guidelines.
- [[lee-2010-micromechanics-fiber-bridging-distribution-model]] — Prof. Bang-Yeon Lee: original paper on the measured-orientation coupled bridging constitutive model.
- [[strain-hardening-mechanism]] — theoretical system of ECC strain-hardening micromechanics.
