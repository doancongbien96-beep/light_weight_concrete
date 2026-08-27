---
title: "Flexural/tensile-strength ratio in engineered cementitious composites"
type: source_note
source: "sources/maalej-1994-flexuraltensile‐strength-ratio-in-engineered-cementitious.pdf"
citation: "Maalej, M., & Li, V. C. (1994). Flexural/tensile-strength ratio in engineered cementitious composites. Journal of Materials in Civil Engineering (ASCE), 6(4), 490-508."
date: 2026-08-24
tags: [flexural-tensile-strength-ratio, mor, engineered-cementitious-composites, pseudo-strain-hardening, neutral-axis-shift, plastic-stress-block, victor-li, mohamed-maalej, asce, landmark-paper]
---

# Mechanism of the Flexural/Tensile Strength Ratio ($\text{MOR}/\sigma_{tc} \approx 5.0$) of Strain-Hardening ECC and Establishment of a Nonlinear Sectional Moment-Curvature Analysis Model

## Summary

This paper elucidates the difference in flexural failure mechanisms between quasi-brittle strain-softening fiber-reinforced concrete (FRC) and ECC exhibiting pseudo strain-hardening behavior, and derives **the theoretical upper bound of the ratio of the modulus of rupture to the direct-tension first-cracking strength ($\text{MOR}/\sigma_{tc}$), driven by tensile strain-hardening plastic flow and the upward neutral axis shift, together with the governing equations of the moment-curvature ($M-\kappa$) response**, then fully demonstrates through three-point bending experiments and the theoretical model that **the flexural strength of 2 vol.% Spectra PE-ECC reaches $12.49\ \text{MPa}$, 5.0 times its direct-tension first-cracking strength ($2.50\ \text{MPa}$)**: the immortal supreme landmark original paper of Mohamed Maalej (PhD) and chaired professor Victor C. Li of the University of Michigan, published in the ASCE Journal of Materials in Civil Engineering in 1994.

## Key Contributions

1. **First elucidation of the amplification mechanism of the ECC flexural/tensile strength ratio ($\text{MOR}/\sigma_{tc} \approx 5.0$)**:
   - While ordinary concrete and strain-softening FRC exhibit $\text{MOR}/\sigma_{tc}$ of only $1.5\sim 2.1$, ECC's continuous stress retention on the tension side amplifies the modulus of rupture (MOR) to as much as 5 times the tensile strength.
2. **Establishment of the theoretical model of nonlinear sectional stress redistribution and neutral-axis upward shift**:
   - Establishes the theory whereby, after crack formation, the tensile-side stress redistributes from a triangular distribution into a full plastic rectangular block (Plastic Stress Block) and the neutral axis migrates toward the extreme compression fiber, maximizing the moment arm of the section's resisting moment.
3. **One-to-one comparative verification of the flexural behavior of 1% steel-fiber FRC vs. 2% PE-ECC**:
   - The 1% steel-fiber FRC stayed at single-crack opening with MOR = 8.53 MPa ($\text{MOR}/\sigma_{tc} = 2.12$), whereas the 2% PE-ECC reached multiple-cracking saturation with MOR = 12.49 MPa ($\text{MOR}/\sigma_{tc} = 5.00$) and exhibited huge deflection ductility.
4. **Mitigation of the size effect and provision of a structural flexural design framework**:
   - Mathematically proves that the volumetric strain-hardening of ECC can completely offset the abrupt size effect characteristic of brittle materials.

## Methods

- **Governing model for sectional mechanics analysis (Sections 3–4 & Figs. 6–10)**:
  - Uniaxial tension model: bilinear elastic model ($\sigma = E \varepsilon$ for $\varepsilon \le \varepsilon_{tc}$, $\sigma = \sigma_{tu}$ for $\varepsilon_{tc} < \varepsilon \le \varepsilon_{tu}$).
  - Uniaxial compression model: parabola-straight-line nonlinear compression formulation.
  - Section compatibility condition and axial-force equilibrium: $\int_0^d \sigma(y) b dy = 0 \rightarrow$ determination of the neutral axis depth $c$ $\rightarrow$ bending moment $M = \int_0^d \sigma(y) b y dy$.
  - Modulus of rupture: $\text{MOR} = \frac{6 M_{max}}{b d^2}$.
- **Experimental verification program (Section 2 & Figs. 3–5)**:
  - Specimen dimensions: $25.4 \times 76.2 \times 304.8\ \text{mm}$ flexural beams (span 254 mm, three-point bending).
  - Composite mixes:
    1. `1% Steel FRC`: $V_f = 1.0\ \text{vol.}\%$, $d_f = 0.5\ \text{mm}$, $L_f = 30\ \text{mm}$.
    2. `2% PE-ECC`: $V_f = 2.0\ \text{vol.}\%$, Spectra 900 PE ($d_f = 38\ \mu\text{m}$, $L_f = 12.7\ \text{mm}$).

## Results

### 1. Comparison table of direct-tension and flexural strength characteristics of 1% Steel FRC vs. 2% PE-ECC (Tables 1–3 & Figs. 4–11)

| Composite material | Fiber volume fraction ($V_f$) | Uniaxial first-cracking strength ($\sigma_{tc}$, MPa) | Ultimate uniaxial tensile strength ($\sigma_{tu}$, MPa) | Ultimate uniaxial tensile strain ($\varepsilon_u$, %) | Modulus of rupture (MOR, MPa) | Flexural/tensile strength ratio ($\text{MOR}/\sigma_{tc}$) | Flexural failure behavior |
|---|---|---|---|---|---|---|---|
| **1% Steel FRC** | 1.0 vol.% Steel | **$4.02 \pm 0.2$** | $4.02\ \text{MPa}$ (softening) | $0.10 \pm 0.02\%$ | **$8.53 \pm 0.8$** | **$2.12 \pm 0.20$** | Single-crack localization and softening |
| **2% PE-ECC** | **2.0 vol.% PE** | **$2.50 \pm 0.1$** | **$4.85 \pm 0.3$ (hardening)** | **$5.40 \pm 0.4\%$ (ultra-ductile)** | **$12.49 \pm 1.1\ \text{MPa}$** | **$5.00 \pm 0.35$ (5× amplification)** | **Ultra-high-density multiple cracking and pseudo-plastic flow** |

### 2. Mechanism analysis of the 5× flexural-strength amplification and the neutral-axis upward shift
- **Formation of the plastic stress block**: in a tension-softening material the crack-face stress drops immediately upon first cracking, so the neutral axis stays near mid-depth and the resistance halts at the elastic flexural moment capacity ($M \approx \sigma_{tc} b d^2 / 6$); in ECC, by contrast, the entire tension side continuously sustains a constant plastic stress of $\sigma_{tu}$.
- **Extreme upward migration of the neutral axis**: to support the enormous plastic tensile force on the tension side, the neutral axis depth $c$ is driven up to within $10\sim 15\%$ of the height below the top compression edge, extending the section's internal lever arm to $\approx 0.9 d$ and reaching the theoretical maximum bending moment $M_{max} \approx 0.5 \sigma_{tu} b d^2$ ($\text{MOR} = 3 \sigma_{tu} \approx 5\sim 6 \sigma_{tc}$).

- **Overall conclusion**: This paper is the supreme immortal classic landmark original paper in the fields of structural engineering and mechanics of materials in which Mohamed Maalej and Victor C. Li fully demonstrated, through sectional mechanics and experiments, how the tensile strain-hardening characteristic of ECC converts under flexural loading into a modulus-of-rupture (MOR) amplification of up to 5 times.

## Related Notes

- [[li-1991-micromechanical-model-tension-softening-bridging]] — Victor Li: original paper on the micromechanics model of fiber-bridging tension softening.
- [[strain-hardening-mechanism]] — Theoretical framework of ECC strain-hardening micromechanics.
- [[lin-2022-hogging-moment-composite-beam-uhtcc-uhpc]] — Original paper on UHTCC/ECC flexural crack-control behavior.
- [[high-strength-strain-hardening-composites]] — Structural behavior framework of high-ductility composites.
