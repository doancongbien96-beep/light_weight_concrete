---
title: "Fiber Orientation Impacts on Flexural Behavior of Steel Fiber Reinforced Ultra High Strength Concrete (Kang et al., 2008)"
type: source_note
source: "sources/2008-fiber-orientation-impacts-on-the.pdf"
citation: "Kang, S.-T., Kim, Y.-Y., Lee, B.-Y., Kim, J.-K. 섬유의 방향성이 강섬유 보강 초고강도 콘크리트의 휨거동 특성에 미치는 영향 (Fiber orientation impacts on the flexural behavior of steel fiber reinforced high strength concrete). Journal of the Korea Concrete Institute 20(6) (2008) 731-739."
date: 2026-08-22
tags: [fiber-orientation, uhpc, steel-fiber, flexural-strength, image-analysis, casting-direction]
---

# Effects of Fiber Orientation on the Flexural Behavior of Steel-Fiber-Reinforced Ultra-High-Strength Concrete

## Summary

This study quantifies changes in fiber orientation and dispersion in steel-fiber-reinforced ultra-high-strength concrete (SFR-UHSC: RPC matrix + 2 vol.% steel fibers) across different casting methods (longitudinal along beam axis vs transverse perpendicular to axis) using image processing. The authors investigated the effects of orientation on flexural performance through four-point bending tests and analytical models. While first cracking strength showed negligible sensitivity to casting direction, peak flexural tensile strength varied by up to 61 %. An analytical strength prediction model incorporating measured fiber orientation distributions matched experimental values for longitudinal casting within an error of approximately 5 %.

## Key Contributions

1. **Confirmation of casting flow rules governing fiber alignment**: Fibers align parallel to the principal flow direction, maximizing fiber count and dispersion along that axis. For longitudinal casting (F2-L), the longitudinal cut face yielded $\alpha_f = 0.38$, $F_n = 49\ /\text{cm}^2$ (49 fibers/cm²), and $F_c = 0.70$ (mean orientation angle $\theta \approx 45^\circ$); transverse casting (F2-T) yielded $\alpha_f = 0.40$, $F_n = 36\ /\text{cm}^2$ (36 fibers/cm²), and $F_c = 0.62$ along the flow direction.
2. **Differential sensitivity of first cracking versus peak flexural strength**: First cracking strength showed little variation between F2-L (19.97 MPa) and F2-T (18.93 MPa, +5.5 %), whereas flexural tensile strength differed dramatically (35.43 MPa vs 21.99 MPa, +61 %). First cracking is matrix-dominated with minimal fiber bridging influence, while peak strength directly reflects fiber bridging efficiency.
3. **Orientation-coefficient-based strength prediction model**: Combined the rule of mixtures $\sigma_{ct} = \eta_l \eta_\theta V_f \sigma_{fu} + V_m \sigma_m$ with flexural conversion factors ($\sigma_{mft} = \beta \sigma_m, \beta = 1.5$; $\sigma_{cft} = \alpha \sigma_{ct}$, SFR-UHSC $\alpha \approx 2.0$) into $\sigma_{cft} = \alpha \eta_l \eta_\theta V_f \sigma_{fu} + (\alpha/\beta)\sigma_{mft} V_m$. Applying image-analyzed actual distributions yielded higher accuracy than theoretical PDF fitting: F2-L predicted/experimental ratio 0.954~0.974 (error ~5 %), F2-T ratio 1.179~1.181 (error ~18 %).
4. **Mechanism of model overprediction at high inclination angles**: Larger fiber inclination angles relative to the crack plane induce secondary flexural stresses in fibers and compressive stresses in the matrix during bridging, reducing composite flexural capacity (for F2-T, the model predicted 25.9 MPa vs 21.99 MPa measured).
5. **Systematic quantitative image evaluation indices**: Applied dispersion coefficient $\alpha_f$ (1 for uniform distribution), number of fibers per unit area $F_n$, and packing density $F_c = A_{ob}/A_{cc} = d/l = \cos\theta$ to UHSC cross sections, observing fiber depletion in specimen cores and accumulation along edges.

## Methods

- **Mixture proportions**: Cement 1.00 / water 0.25 / silica fume 0.25 / fine aggregate 1.10 / filler 0.30 / superplasticizer 0.018 (by cement mass), steel fibers 2 vol.% (tensile strength 2,500 MPa, diameter 0.2 mm, length 13 mm). Flow 230 mm, compressive strength 198 ± 3.44 MPa ($\phi 100 \times 200\ \text{mm}$, φ100×200 mm cylinders).
- **Specimens**: $100 \times 100 \times 400\ \text{mm}$ (100×100×400 mm) prismatic flexural specimens across 2 casting methods (longitudinal F2-L / transverse F2-T) plus plain control. Sectioned into 4 segments, capturing high-resolution photos of vertical and horizontal cut faces.
- **Flexural testing**: Four-point bending on a 250 kN UTM under displacement control with mid-span LVDT.
- **Strength analysis parameters**: $\eta_l = l/(2l_c)$ for $l < l_c$, $1 - l_c/(2l)$ for $l \ge l_c$, $l_c = \sigma_{fu} d_f / (2\tau_{fu})$; $\eta_\theta = \int g(\theta)\cos^2\theta \, d\theta$ (1 for parallel, 0 for perpendicular). Reference orientation efficiency factors: Aveston 2D $2/\pi$, 3D $1/2$; Laws $1/3$, $1/6$; Allen 2D $1/2$.

## Results

| Parameter | Plain (Non) | F2-L (Longitudinal) | F2-T (Transverse) |
|---|---|---|---|
| First crack strength (MPa) | 12.68 ± 0.80 | 19.97 ± 1.05 | 18.93 ± 0.09 |
| Flexural tensile strength (MPa) | — | 35.43 ± 1.03 | 21.99 ± 2.68 |

- Orientation efficiency $\eta_\theta$: F2-L 0.677 (PDF fit p=0.905, q=1.895) / 0.704 (measured); F2-T 0.369 (p=3.785, q=2.210) / 0.367 (measured); $\eta_l = 0.2550$ for both.
- Predicted flexural strength: F2-L 33.82~34.52 MPa (measured 35.43 MPa, 35.43), F2-T 25.92~25.96 MPa (measured 21.99 MPa, 21.99).

## Related Notes

- [[kim-2008-fiber-classification-and-detection-technique]] — Detection and classification techniques for PVA-ECC by the same research group.
- [[fiber-bridging-constitutive-law]] — Bridging stress relations including orientation angle $\phi$ and snubbing effects.
- [[pseudo-strain-hardening-criteria]] — Role of fiber orientation in satisfying the $\sigma_0 \ge \sigma_{fc}$ strength criterion.
- [[hambach-2017-properties-3d-printed-fiber-reinforced-cement-paste]] — Artificial fiber alignment control via 3D printing nozzle toolpaths.
