---
title: "Design Optimization of the Flexural Behavior of a Novel UHPC–ECC–RC Composite Sandwich Panel (Liu, Huang & Bian, 2025)"
type: source_note
source: "sources/Liu 등 - 2025 - Design Optimization of the Flexural Behavior of a Novel UHPC–ECC–RC Composite Sandwich Panel.pdf"
citation: "Liu, Y., Huang, D., Bian, Y. Design optimization of the flexural behavior of a novel UHPC–ECC–RC composite sandwich panel. The Structural Design of Tall and Special Buildings 34 (2025) e70101. doi: 10.1002/tal.70101"
date: 2026-08-22
tags: [uhpc, ecc, composite-sandwich-panel, precast, flexural-optimization, nsga-ii, gan-data-augmentation, neural-network, sichuan-group]
---

# Design Optimization of the Flexural Behavior of a Novel UHPC–ECC–RC Composite Sandwich Panel

## Summary

A study by the Sichuan University group that replaces parts of the wythe faces of precast concrete sandwich insulation panels (PCSP) with ECC and UHPC to pursue load capacity and eco-efficiency at once. ECSP (ECC) and UCSP (UHPC) panels with their top and bottom wythe faces substituted by 20 mm were tested in four-point bending and reproduced in three-dimensional ABAQUS finite element analysis, after which a role-separated UE-CSP concept placing UHPC on the compression side and ECC on the tension side was proposed. GAN data augmentation + neural network prediction + NSGA-II multi-objective optimization fixed the optimal section (top UHPC 12 mm, bottom ECC 28 mm), achieving a peak load of 115.04 kN and a ductility index of 8.03.

## Key Contributions

- Experimental demonstration of the material role-separation design principle: under flexure the upper wythe face is governed by compression and the lower by tension, so using the same high-performance concrete on both faces leaves capability unused. T20B20-1, which adds ECC to the compression side (top), gained +11 % peak load and +53 % ductility over the bottom-only variant but suffered ECC-normal concrete interface debonding, while UHPC on both faces (TU20BU20-1) proved instead inferior at −29 % peak load and −22 % ductility relative to T20B20-1 — the post-cracking sustained contribution of the tension-side material (ECC strain-hardening) is more decisive for flexural performance than compressive strength.
- Interfacial shear strength data: slant shear tests put the UHPC-NC interface at 5.60 MPa, 82 % higher than the ECC-NC interface; accordingly no interfacial debonding occurred in UCSP. These values were fed into the FE model as cohesive interface parameters (traction-separation law with Maxs damage criterion).
- Data-driven optimization framework: small-sample FE analysis data (7 parametric cases) augmented to 85 samples with a GAN (RMSE reduced by 15–25 %); a 2-7-5-2 neural network (tanh+sigmoid, Levenberg-Marquardt training, MSE 0.0027, prediction errors of 4.71 % for peak load and 5.83 % for ductility) serving as objective functions; optimization by NSGA-II (population 200, crossover 0.85, mutation 0.25) plus TOPSIS decision-making.
- Quantitative cost-performance evaluation (2025 Chengdu prices): against ECSP, UE-CSP delivers +51 % peak load, +35 % ductility, and −2.2 % material cost at +0.8 % weight; against UCSP, +113 % peak load, +72 % ductility, and +5.4 % cost at −1.8 % weight. Demonstrates economics that offset the high unit prices of ECC/UHPC (4500/5000 CNY/m³ respectively).

## Methods

- Materials: normal concrete compressive 44 MPa · tensile 1.5 MPa · elastic modulus 33.5 GPa; ECC compressive 45.4 MPa · tensile 7.16 MPa · ultimate tensile strain capacity 6.49 % · elastic modulus 16.8 GPa; UHPC (premix, China West Construction Group) compressive 129.2 MPa · tensile 5.65 MPa · ultimate tensile strain 1.37 % · elastic modulus 42.2 GPa.
- Specimens: steel mesh within the wythes (bar diameter 6 mm, grid 180×250 mm), GFRP truss connectors (embedment length 45 mm), four-point bending tests. ECSP results cited from prior work (Bian et al. 2023 Eng Struct).
- FE: ABAQUS CDP model; wythe C3D8R elements, connectors and mesh T3D2, insulation board crushable foam (E = 5 MPa, Poisson ratio 0.1). Element-deletion threshold maximum principal strains NC 0.0001 / UHPC 0.014 / ECC 0.065. Validation: P_T/P_FE = 1.07±0.061, μ_T/μ_FE = 1.04±0.058 (FE underpredicts each by about 7 % and 4 %).
- Parametric study: total substitution thickness fixed at 40 mm; top UHPC 5–35 mm × bottom ECC 5–35 mm across seven cases including the 20/20 baseline.

## Results

- Experiments: T0B20-1 (bottom ECC only) 68.72 kN, ductility 3.88; T20B20-1 76.18 kN, 5.95; TU20BU20-1 53.94 kN, 4.67. A contrast between triangular fine crack dispersion at the bottom tension edge of the ECC layer and the main crack with steel fiber bridging of the UHPC layer.
- UE-CSP baseline design (top 20 mm UHPC + bottom 20 mm ECC, FE): 89.26 kN, ductility 7.21 — +17 %/+21 % against ECSP and +65 %/+54 % against UCSP. A long softening branch is retained after the peak, and damage concentrates in the normal concrete layer, protecting the wythe faces.
- Connector stresses: maximum tensile stress of the GFRP truss at peak load was 675 MPa for T20B20-1, 593 MPa for TU20BU20-1, and 800 MPa for UE-CSP (ultimate strength reached) — composite action exploited to its full extent.
- Optimization: at the optimum section U 12 mm/E 28 mm NSGA-II predicts 115.04 kN, 8.03 and FE verification gives 107.57 kN, 8.31 (errors within 8 %); gains over the baseline UE-CSP are +20.5 % P and +11.4 % TI.
- Self-stated limitation: UE-CSP performance rests on finite element analysis without experimental verification — follow-up structural testing and durability programs (coupled salt attack, freeze-thaw, carbonation deterioration) are stated to be planned.

## Related Notes

- [[cao-2025-bamboo-scrimber-concrete-composite-beams-uhpc-ecc]] — application axis of the UHPC+ECC material pairing in composite members
- [[lai-2025-uhpfrc-nc-composite-beam-flexure]] — composite-section flexural design governed by high-performance concrete tension layers
- [[ge-2023-steel-precast-uhpc-composite-beams-flexural-behavior]] — precast UHPC composite members
- [[du-2025-steel-uhdcc-composite-bridge-deck-bending]] — behavior of composite members with ultra-high ductility cementitious materials
- [[guo-2026-egc-intelligent-design]] — CatBoost+SHAP+NSGA-III data-driven design axis (same paradigm as GAN+NN+NSGA-II)
- [[pseudo-strain-hardening-criteria]] — conditions for strain-hardening that let tension-side ECC keep contributing after cracking
- [[fiber-bridging-constitutive-law]] — contrast between fiber bridging on UHPC main-crack planes and ECC fine-crack planes
