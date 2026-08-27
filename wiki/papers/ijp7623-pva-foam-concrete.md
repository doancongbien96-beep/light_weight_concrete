---
title: "Mechanism of PVA Fiber Reinforcement in Foam Concrete: Microstructural Analysis and Regression Model (Yu, Zhang, Sanjayan et al., 2023)"
type: source_note
source: "sources/IJP7623E_Mechanism of PVA fiber_JMCE.pdf"
citation: "Yu, K., et al. Mechanism of PVA fiber reinforcement in foam concrete: Microstructural analysis and regression model. Journal of Materials in Civil Engineering 35(12) (2023) 04023447. doi: 10.1061/JMENE23.ME-54470 계열"
date: 2026-08-22
tags: [foam-concrete, pva-fiber, microstructure, pore-structure, fiber-dispersion, regression-model, user-group]
---

# Microstructural Analysis and Regression Modeling of PVA Fiber Reinforcement Mechanisms in Foam Concrete

## Summary

This study investigates PVA fiber reinforcement mechanisms in foam concrete across fiber dimensions (diameters 19 and 200 µm; lengths 3, 6, and 12 mm), fiber volume fractions (0~0.9 vol %), and target densities (800 and 1700 kg/m³) across 32 experimental series. Using fluorescence imaging, fiber dispersion coefficients, pore size, shape factors, and pore spatial distributions were quantified and correlated with compressive strength via multi-variable regression. In high-density foam concrete (1700 kg/m³), fiber dispersion governed strength (+15.5 % gain). In low-density foam concrete (800 kg/m³), fibers directly refined the pore structure, achieving up to +45.3 % strength gain, statistically confirming density-dependent reinforcement mechanisms.

## Key Contributions

1. **Density-dependent reinforcement mechanisms**: In high-density foam concrete, pore structure and fiber dispersion were largely decoupled, with effective fiber dispersion governing strength. In low-density foam concrete, fiber dispersion directly regulated pore refinement, where uniformly dispersed fibers reduced oversized pores and promoted spherical, homogenous pore geometries.
2. **Fiber diameter trade-off**: In high-density matrices, coarse fibers (200 µm) performed better due to superior dispersion; in low-density matrices, fine fibers (19 µm) were superior due to higher interfacial bond area. An intermediate length of 6 mm optimized dispersion in low-density mixes.
3. **Identification of optimal fiber volume fractions**: Fiber content negatively correlated with dispersion coefficient $\alpha$; excessive dosages caused agglomeration and strength drops. Optimal dosages were 0.6 % (200 µm fibers) for 1700 kg/m³ and 0.15 % (19 µm fibers) for 800 kg/m³.
4. **Automated quantitative image analysis framework**: Formulated fiber dispersion coefficient $\alpha$ (Eq. 1, Kang-Lee-Yu method), pore shape factors (Eq. 2–3, size-weighted mean), effective diameter (Eq. 4), and watershed pore segmentation in MATLAB—extending the Kim (2008) and Lee (2010) fluorescence techniques to cellular concrete.

## Methods

- **Mixture proportions**: Cement : sand : water = 1 : 0.4 : 0.4 (by mass). 800 kg/m³ mix: cement 420, sand 168, water 168, foam 44 kg/m³. 1700 kg/m³ mix: cement 935, sand 374, water 374, foam 17 kg/m³. Synthetic foaming agent (ISOLTECH ISOCEM-S/X) 2.5 % solution aerated at 6 bar to a foam density of ~70 kg/m³.
- **Mixing procedure**: Bucket and paint mixer at 500 rpm. PVA fibers hand-premixed with water for 30 s $\rightarrow$ cement and sand added (ASTM C305) $\rightarrow$ preformed foam introduced and mixed for 3.5 min.
- **Curing and testing**: Wrapped in film, cured at 23 °C. Compressive testing per ASTM C109 (50 mm cubes, 3 replicates) loaded at 1000 N/s for 1700 kg/m³ and 200 N/s for 800 kg/m³. Microstructure: specimen slicing $\rightarrow$ drying at 80 °C $\rightarrow$ vacuum epoxy impregnation (black dye for low-density) $\rightarrow$ diamond saw cutting $\rightarrow$ LEICA M205 A microscope and ImageJ/MATLAB image analysis.
- **Statistics**: $t$-tests ($p < 0.05$) and ANOVA $F$-tests validating regression model significance.

## Results

- Maximum strength gain: +45.3 % for low density and +15.5 % for high density at respective optimal fiber configurations.
- Increasing fiber dosage reduced dispersion coefficient $\alpha$ (negative correlation across both densities).
- 200 µm fibers had fewer filaments per cross-section than 19 µm fibers, requiring wide-field fluorescence imaging to ensure representative sampling.

## Related Notes

- [[kim-2008-fiber-classification-and-detection-technique]] — Original fluorescence imaging fiber detection technique.
- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] — Fluorescence fiber discrimination and dispersion coefficient $\alpha$.
- [[kang-2011-fiber-distribution-uhsc-flexural-strength]] — Precedent application of the $\alpha$ dispersion coefficient.
- [[yoon-2015-lightweight-concrete-eps]] — Lightweight concrete and cellular composite systems.
- [[tosun-2014-flaw-size-fiber-distribution-pva-ecc]] — Correlation between fiber distribution and tensile ductility.
