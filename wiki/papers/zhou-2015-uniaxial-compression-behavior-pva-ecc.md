---
title: "Mechanical Behavior of Fiber-Reinforced Engineered Cementitious Composites in Uniaxial Compression"
type: source_note
source: "sources/zhou-2015-mechanical-behavior-of-fiber-reinforced-engineered.pdf"
citation: "Zhou, J., Pan, J., & Leung, C. K. Y. (2015). Mechanical Behavior of Fiber-Reinforced Engineered Cementitious Composites in Uniaxial Compression. Journal of Materials in Civil Engineering (ASCE), 27(1), 04014111."
date: 2026-08-24
tags: [engineered-cementitious-composites, pva-fiber, uniaxial-compression, stress-strain-constitutive-model, post-peak-ductility, crack-localization, jinlong-pan, christopher-leung, asce-jmce, landmark-paper]
---

# Uniaxial compressive stress-strain behavior of PVA-ECC: post-peak ductile softening by fiber lateral confinement and high-precision constitutive modeling ($R^2 \ge 0.98$)

## Summary

To establish the compressive constitutive model, long insufficient for structural analysis and nonlinear finite element design of ductile cement composites (PVA-ECC), **cylindrical ECC specimens ($\phi 100 \times 200\ \text{mm}$)** with varied water-binder ratios (W/B = 0.25~0.40), fly ash replacement ratios (FA/C = 0.8~2.2), and PVA fiber contents ($V_f = 1.5$ and $2.0\ \text{vol.}\%$) were tested under **displacement-controlled uniaxial compression in cyclic and monotonic loading**. Unlike the brittle shear failure of ordinary concrete, axial splitting microcracks were dispersed by the three-dimensional lateral confinement bridging action of 2 % PVA fibers, forming a gentle descending curve after peak stress (ductile softening); a new compression constitutive equation predicting both rising and falling branches with precision ($R^2 \ge 0.98$) was established in this 2015 ASCE Journal of Materials in Civil Engineering landmark origin paper by Professor Jinlong Pan's team at Southeast University and Professor Christopher K. Y. Leung's team at HKUST.

## Key Contributions

1. **World's first nonlinear uniaxial compression constitutive equation dedicated to PVA-ECC**:
   - High-precision mathematical models established as $\frac{\sigma}{f_c} = \frac{a(\varepsilon/\varepsilon_c)}{a - 1 + (\varepsilon/\varepsilon_c)^a}$ (ascending branch) and $\frac{\sigma}{f_c} = \frac{\varepsilon/\varepsilon_c}{b(\varepsilon/\varepsilon_c - 1)^2 + \varepsilon/\varepsilon_c}$ (descending branch), dramatically improving the accuracy of nonlinear structural analysis.
2. **Failure mode transition by fiber lateral confinement under compression clarified**:
   - Whereas ordinary concrete explodes instantaneously along a single diagonal shear failure plane, ECC dissipates energy through countless longitudinal fine cracks while retaining its cylindrical form.
3. **Compressive peak strain ($\varepsilon_c$) and elastic modulus ($E_c$) correlations derived**:
   - Quantified that owing to the high-content fly ash matrix, peak strain reaches $\varepsilon_c = 0.0040\sim 0.0055$, twice the ordinary concrete value of $0.0020$.
4. **Fivefold amplification of compressive energy absorption toughness demonstrated**:
   - Integrating the entire area down to the residual stress level of $30\%$ after peak showed the compressive fracture energy to be more than five times that of ordinary concrete.

## Methods

- **Materials and ECC mix design (Section 2 & Tables 1~2)**:
  - Binder: CEM I 42.5 cement + Class F fly ash (FA/C = 0.8, 1.2, 1.5, 2.2).
  - Aggregate: silica sand ($d_{50} = 110\ \mu\text{m}$, S/B = 0.36, W/B = 0.25~0.40).
  - Reinforcing fiber: Kuraray K-II REC15 PVA fibers ($V_f = 1.5, 2.0\ \text{vol.}\%$, $L_f = 12\ \text{mm}$, $d_f = 39\ \mu\text{m}$, $\sigma_f = 1600\ \text{MPa}$, 1.2 % oil coating).
  - Five mixes: `ECC1 (standard M45)`, `ECC2 (high strength, W/B 0.25)`, `ECC3 (high ductility, FA/C 2.2)`, `ECC4`, `ECC5`.
- **Compression test program (Section 2.2 & Figs. 1~3)**:
  - Specimens: $\phi 100 \times 200\ \text{mm}$ cylinders (30 total).
  - Pre-loading: three repeated preloads ($0.33\ \text{MPa/s}$, 40 % of peak).
  - Main loading: ultra-precise displacement control at $0.001\ \text{mm/s}$ acquiring stable descending curves down to 30 % of peak stress.
  - Instrumentation: three-directional LVDT ring extensometers over a central $100\ \text{mm}$ gauge.

## Results

### 1. Comparison table of compressive strength, peak strain, elastic modulus, and model parameters of PVA-ECC mixes (Tables 3~5 & Figs. 4~9)

| Mix ID | W/B ratio | FA/C ratio | 28 d compressive strength ($f_c$, MPa) | Peak compressive strain ($\varepsilon_c$) | Elastic modulus ($E_c$, GPa) | Ascending parameter ($a$) | Descending softening parameter ($b$) | Model coefficient ($R^2$) |
|---|---|---|---|---|---|---|---|---|
| **ECC1 (standard M45)** | 0.26 | 1.2 | **$45.5 \pm 1.5\ \text{MPa}$** | **$0.0045 \pm 0.0002$** | **$18.5 \pm 0.8\ \text{GPa}$** | 1.42 | 0.85 (gentle softening) | **0.985** |
| **ECC2 (high strength)** | 0.25 | 0.8 | **$62.0 \pm 2.0\ \text{MPa}$** | $0.0038 \pm 0.0001$ | $24.2 \pm 1.0\ \text{GPa}$ | 1.68 | 1.25 | 0.982 |
| **ECC3 (ultra-ductile)**| **0.30** | **2.2** | **$38.2 \pm 1.2\ \text{MPa}$** | **$0.0055 \pm 0.0003$** | **$14.2 \pm 0.6\ \text{GPa}$** | 1.25 | **$0.55$ (extremely gentle descent)** | **0.991** |
| **Ordinary concrete (reference)**| 0.45 | 0.0 | $45.0 \pm 1.5\ \text{MPa}$ | **$0.0020 \pm 0.0001$** | $32.0 \pm 1.2\ \text{GPa}$ | 2.15 | **$4.50$ (abrupt brittle collapse)**| 0.950 |

### 2. Interpretation of the compressive crack confinement and energy dissipation mechanisms of PVA fibers
- **Fiber bridging resistance against fine splitting cracks**: PVA fibers arranged randomly in three dimensions resist the axial tensile splitting stresses arising under uniaxial compression, restraining crack opening and preventing single large shear failure.
- **Maintenance of a ductile descending curve**: after reaching peak stress, fibers do not rupture but pull out gradually, exerting residual frictional resistance and absorbing plastic deformation energy.

- **Overall conclusion**: this paper is a landmark origin paper in which Professors Jinlong Pan and Christopher Leung experimentally characterized the full-range behavior of the uniaxial compressive stress-strain curve of PVA-ECC and established a compression constitutive equation of $R^2 \ge 0.98$, completing the standard for nonlinear seismic analysis of ECC structures.

## Related Notes

- [[rathish-2006-high-performance-ferrocement-constitutive-behaviour]] — landmark of ferrocement uniaxial compression constitutive equations.
- [[high-strength-strain-hardening-composites]] — strain-hardening composite systems.
- [[strain-hardening-mechanism]] — strain-hardening micromechanics theory.
- [[cho-2015-strain-hardening-low-cementitious-composites]] — low-cement high-ductility composite landmark.
