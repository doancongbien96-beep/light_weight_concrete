---
title: "Effect of fiber diameter variation on properties of cement-based matrix fiber reinforced composites"
type: source_note
source: "sources/li-1996-effect-of-fiber-diameter-variation.pdf"
citation: "Li, V. C., & Obla, K. (1996). Effect of fiber diameter variation on properties of cement-based matrix fiber reinforced composites. Composites Part B: Engineering, 27(3-4), 275-284."
date: 2026-08-24
tags: [fiber-diameter-variation, normal-distribution, fiber-bridging-constitutive-model, fracture-energy, first-crack-strength, fiber-rupture, micromechanics, victor-li, composites-part-b, landmark-paper]
---

# Micromechanical Quantitative Analysis of the Effect of Commercial Fiber Diameter Variation (Normal Distribution) on the Bridging Stress-Crack Opening Displacement ($\sigma_B-\delta$), First-Crack Strength, and Fracture Energy ($G_c$) of Cement Composites

## Summary

A landmark 1996 original paper in Composites Part B: Engineering by University of Michigan endowed chair professor Victor C. Li and Karthikeyan Obla, which derived an **extended micromechanics model that incorporates the fiber diameter probability density function $p(d_f)$ into the three-dimensional (3D) single-fiber debonding-pullout integral equation** in order to elucidate the effect of the inevitable statistical **fiber diameter variation (normally distributed $N(d_f^*, \sigma_d^2)$)** arising in commercial synthetic and natural fiber manufacturing processes on the bridging stress curve ($\sigma_B-\delta$), first-crack strength ($\sigma_{fc}$), fracture energy ($G_c$), fiber rupture transition, and pseudo strain hardening (PSH) behavior of cement composites, and which quantitatively analyzed the rates of change in bridging properties and fracture toughness relative to a uniform-diameter model. The study mathematically demonstrated that an appropriate degree of diameter variation has a positive effect—the high aspect ratio ($L_f/d_f$)-driven initial stiffening contribution of thin fibers and the rupture-preventing pullout of thick fibers complement each other, **enhancing the fracture energy ($G_c$) by $5\sim 15\%$ and increasing the first-crack strength**—whereas excessive diameter variation can promote localized rupture.

## Key Contributions

1. **First derivation of a generalized fiber bridging micromechanics model reflecting the normally distributed fiber diameter variation $p(d_f)$**:
   - Rigorously derived the bridging stress integral $\sigma_B(\delta) = \int_{d_1}^{d_2} \left[ \int \int P(\delta, z, \phi, d_f) p(z) p(\phi) dz d\phi \right] p(d_f) d(d_f)$ to analyze the effect of diameter variance.
2. **Quantification of the enhancement of composite fracture energy ($G_c$) and first-crack strength due to diameter variation**:
   - Relative to the uniform-diameter model, the composite with diameter variation yields $G_c = \frac{1}{12} g \tau V_f d_f^* (L_f/d_f^*)^2 k(z_1, z_2)$ with a correction factor $k > 1.0$, proving that toughness increases by approximately $10\%$.
3. **Probabilistic partitioned analysis of the critical conditions for fiber rupture onset**:
   - As the critical embedded length $L_c(d_f) = \frac{d_f \sigma_{fu}}{2\tau_0}$ varies with diameter, the combined failure modes of the thin-fiber population ($d_f < d_f'$) and the thick-fiber population ($d_f > d_f'$) were completely formalized by sector (Sector I, II, III).
4. **Proposal of quality-management criteria and allowable diameter tolerances for commercial fibers**:
   - Micromechanically proposed an upper bound on the allowable standard deviation of fiber diameter ($\sigma_d / d_f^* \le 0.15$) that does not impair PSH strain-hardening saturation.

## Methods

- **Diameter probability distribution and single-fiber model (Section 2 & Fig. 1)**:
  - Normal distribution of diameter: $p(d_f) = \frac{1}{\sqrt{2\pi}\sigma_d} \exp\left( -\frac{(d_f - d_f^*)^2}{2\sigma_d^2} \right)$ (valid range $d_1 \le d_f \le d_2$).
  - Single-fiber pullout load: $P(\delta, z, \phi, d_f) = \pi d_f \tau_0 (L_e - \delta) e^{f\phi}$.
- **Derivation of the bridging stress-crack opening displacement relation (Section 2.1~2.2 & Figs. 2~4)**:
  - Pre-peak regime ($\delta < \delta^*$): bridging stress $\sigma_B(\delta)$ during ongoing debonding.
  - Post-peak regime ($\delta > \delta^*$): full pullout-slip bridging stress $\sigma_B(\delta) = \sigma_0 (1 - 2\delta/L_f)^2 k_2$.
- **Fracture-mechanics equilibrium equation for the first-crack strength ($\sigma_{fc}$) (Section 3 & Appendix 3)**:
  - Crack-tip stress intensity factor equilibrium: $K_L + K_B = K_{tip}$.
  - Closed-form solution of $\sigma_{fc}$ obtained via the cohesive traction integral.

## Results

### 1. Comparison table of composite mechanical parameters under uniform vs. non-uniform fiber diameter distributions (Sections 2~4 & Figs. 5~9)

| Evaluation item | Uniform diameter model ($\sigma_d = 0$) | Diameter variation model ($\sigma_d / d_f^* = 0.05$) | Diameter variation model ($\sigma_d / d_f^* = 0.10$) | Influence mechanism |
|---|---|---|---|---|
| **Composite fracture energy ($G_c$)** | $1.00\ G_{c,0}$ (baseline) | **$1.05\ G_{c,0}$ (+5 %)** | **$1.12\ G_{c,0}$ (+12 %)** | High-aspect-ratio bridging toughness contribution of thin fibers |
| **First-crack strength ($\sigma_{fc}$)** | $\sigma_{fc,0}$ (baseline) | **$1.03\ \sigma_{fc,0}$** | **$1.07\ \sigma_{fc,0}$** | Increase in cohesive bridging force at the incipient crack tip |
| **Peak bridging stress ($\sigma_0$)** | $\sigma_0$ (baseline) | $\approx 1.01\ \sigma_0$ | $\approx 1.02\ \sigma_0$ | Peak stress retained |
| **Fiber rupture risk** | Single critical length $L_c$ | Some low-diameter fibers may rupture | Increased rupture of low-diameter fibers | $\sigma_d / d_f^* > 0.15$ induces PSH degradation |

### 2. Interpretation of fracture and bridging mechanisms under diameter variation

- **Initial bridging reinforcement by small-diameter fibers**: fibers with diameters smaller than the mean ($d_f < d_f^*$) offer larger surface area per unit volume and therefore provide higher cohesive stress at early crack opening, increasing the first-crack strength.
- **Rupture prevention by large-diameter fibers**: fibers with diameters larger than the mean ($d_f > d_f^*$) have a larger margin against their rupture strength and are fully pulled out (Pullout), continuously supplying the terminal fracture energy.

- **Overall conclusion**: this paper is a landmark original work that rigorously formalized, in micromechanical terms, the effect of the statistical non-uniformity of fiber diameter on the bridging stress curve and fracture toughness of composites, dramatically improving the reliability of manufacturing-tolerance management for commercial fibers and of composite design.

## Related Notes

- [[li-1991-micromechanical-model-tension-softening-bridging]] — Victor Li: original paper on the fiber-bridging tension-softening micromechanics model.
- [[li-1995-matrix-design-for-pseudo-strain-hardening]] — Victor Li: original paper on matrix design guidelines for PSH composites.
- [[lee-2010-micromechanics-fiber-bridging-distribution-model]] — Prof. Bang Yeon Lee: original paper on a bridging constitutive model coupled with the fiber orientation distribution.
- [[strain-hardening-mechanism]] — ECC strain-hardening micromechanics theory.
