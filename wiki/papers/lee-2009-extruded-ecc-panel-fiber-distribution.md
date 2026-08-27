---
title: "Fiber Distribution Characteristics and Flexural Performance of Extruded ECC Panel (Lee, Han, Cho, Kwon & Kim, 2009)"
type: source_note
source: "sources/Lee 등 - 2009 - Fiber Distribution Characteristics and Flexural Performance of Extruded ECC Panel.pdf"
citation: "이방연, 한병찬, 조창근, 권영진, 김윤용. 압출성형 ECC 패널의 섬유분포 특성과 휨 성능. 한국콘크리트학회논문집 21(5) (2009) 573-580. doi: 10.4334/JKCI.2009.21.5.573"
date: 2026-08-22
tags: [extruded-ecc, fiber-distribution, image-processing, fiber-orientation, psh-criteria, flexural-performance, user-group, kaist-era]
---

# Fiber Distribution Characteristics and Flexural Performance of Extruded ECC Panels

## Summary

Authored by Prof. Bang Yeon Lee as first author during his KAIST doctoral work (Prof. Yun Yong Kim as corresponding author), this paper establishes the mix proportioning, manufacturing process, and curing regime for extruded engineered cementitious composite (ECC) panels exhibiting pseudo-strain-hardening and multiple cracking. Using fluorescence microscopy and digital image processing, the authors quantified PVA fiber dispersion and orientation, interpreting the resulting flexural performance through micromechanics. Mix variations simultaneously altered fiber distribution and matrix fracture toughness, governing flexural behavior. The mean fiber orientation angle of approximately 44° confirmed that extrusion aligns fibers primarily in 2D rather than 3D random space, though the measured orientation probability density function differed distinctly from an idealized uniform 2D distribution.

## Key Contributions

- **Establishment of extruded ECC manufacturing process**: Enabled 2 vol % PVA fiber incorporation via dry pre-dispersion and secondary mixing; utilized 0.6 wt % hydroxypropyl methylcellulose (HPMC) thickener; omitted autoclaving due to PVA melting (180~200 °C) in favor of 4~5 h precuring followed by 60 °C steam curing, completing production within 3 days.
- **Optimization of mix proportion**: At a water-to-binder mass ratio W/M 9.8 %, a cement : ECC powder : silica sand ratio of 33 : 29 : 37.2 (mix NO3) achieved superior strain-hardening and toughness. Flexural strength reached 35~38 MPa, 2~4 times higher than cast ECC panels (10~15 MPa).
- **Correlation between fiber dispersion coefficient $\alpha_f$ and flexural toughness**: Higher $\alpha_f$ correlated with increased toughness (NO3 0.31 > NO2 0.30 > NO4 0.28 > NO1 0.27). Mix proportioning simultaneously influenced $\alpha_f$, $J'_b$, and $\sigma_0$: mix NO1 exhibited a 94.3 % higher $J_{tip}$ and 14 % lower $\alpha_f$ than NO3, losing multiple cracking capacity.
- **Satisfaction of saturated PSH criteria**: Toughness ratios $J'_b/J_{tip}$ ranged from 7.06~11.9 across all mixes, satisfying Kanda and Li's saturated PSH criterion ($> 3$). Sectional orientation PDFs were fitted using Xia's distribution function, providing the methodological foundation for subsequent fiber orientation research.

## Methods

- Materials: Ordinary Portland cement (density 3.15 g/cm³), silica flour (specific surface area 3,793 cm²/g), silica sand (mean particle size 0.2 mm), high-tenacity PVA fibers (diameter 39 µm, length 6~8 mm, oil-coated). ECC powder: composite blend of BFS, sepiolite, $\text{Mg(OH)}_2$, $\text{CaCO}_3$, CSA, and $\text{Al(OH)}_3$.
- 4 mix proportions (NO1~NO4): OPC 33~38 wt %, ECC powder 26~29 wt %, silica flour 27.8~37.2 wt %, silica sand 0~9.4 wt % (NO4 only), SP 0.2 wt %, HPMC 0.6 wt %, PVA 2 vol %. Mixing: omni-mixer dry mix 4 min + wet mix 6 min + extrusion 5 min (total 15 min).
- Flexural testing: 3-point bending per KS F 2408 on 100×10×400 mm panels with LVDT midspan deflection tracking.
- Fiber distribution analysis: 8×8 mm² cross-sections examined under fluorescence microscopy + CCD camera; fiber detection via neural network classification + watershed segmentation + morphological reconstruction (Kim et al. 2008 technique). Dispersion coefficient $\alpha_f = -\exp\left[\frac{\sum(x_i-1)^2}{n}\right]$, orientation angle $\theta = \arccos(l_s/l_l)$.
- Micromechanics: Frictional bond strength 2.9 MPa (Kim et al. 2007 GGBS-ECC experimental data), chemical debonding energy 1.85 J/m², and matrix fracture toughness $J_{tip} = 10\ \text{J/m}^2$ assumed to calculate $\sigma(\delta)$ bridging curves and complementary energy $J'_b$.

## Results

- Flexural peak strength: NO1 reached 49.78 MPa (highest strength but brittle post-crack drop with deflection ductility $\delta_b/\delta_{bi} = 1.45$), NO2 reached 37.07 MPa, NO3 reached 37.01 MPa, and NO4 reached 36.22 MPa. Ductility index $\delta_b/\delta_{bi}$ peaked at 8.72~9.39 for NO3, accompanied by 11~12 multiple microcracks.
- Flexural stiffness: 42.04~53.58 kN/mm, consistent with the flexural strength order.
- Micromechanical parameters: Peak bridging stress σ0 = 5.11~5.67 MPa and complementary energy J′b = 70.6~119 J/m² (highest in NO3). Low ductility in NO1 resulted from high Jtip combined with lower αf, 40.9 % lower J′b, and 9.98 % lower σ0.
- Fiber orientation: mean orientation angle 44° ± 1.3~2.2° (compared with 57.3° for 3D random and 45° for 2D random orientation), indicating an alignment effect of approximately 23 % along the extrusion axis. The orientation PDF differed from the uniform 2D theoretical value ($2/\pi$), confirming orientation non-uniformity.

## Related Notes

- [[kim-2008-fiber-classification-and-detection-technique]] — Foundational image processing algorithms for fiber detection.
- [[kim-2007-fiber-dispersion-fluorescence]] — Quantitative fluorescence image analysis for fiber dispersion.
- [[kanda-2006-saturated-psh-design-criteria-ecc]] — Saturated PSH design criteria ($J'_b/J_{tip} > 3$).
- [[fiber-bridging-constitutive-law]] — Constitutive modeling of fiber bridging curves $\sigma(\delta)$.
- [[pseudo-strain-hardening-criteria]] — Steady-state flat crack propagation criterion ($J'_b > J_{tip}$).
- [[cho-2012-extruded-dfrcc-panel-composite-slab-flexure]] — Application of extruded DFRCC panels in composite slabs.
- [[li-2023-ecc-micromechanics-critical-review]] — Critical review of ECC micromechanical design principles.
- [[kim-2007-slag-ecc-tensile-fiber-dispersion]] — Source for interfacial frictional bond value (2.9 MPa).
