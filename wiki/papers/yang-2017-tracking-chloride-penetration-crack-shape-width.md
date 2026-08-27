---
title: "Tracking Chloride Penetration in Concrete Considering Crack Shape and Width (Yang et al., 2017)"
type: source_note
source: "sources/yang-2017-simple-technique-for-tracking-chloride.pdf"
citation: "Yang, H. M., Lee, H. S., Yang, K. H., & Ismail, M. A. (2017). A simple technique for tracking chloride penetration in concrete considering crack shape and width. Construction and Building Materials, 151, 642-653. https://doi.org/10.1016/j.conbuildmat.2017.06.126"
date: 2026-08-24
tags:
  - chloride-penetration
  - crack-width
  - crack-shape
  - 2d-diffusion-model
  - colorimetric-method
  - marine-durability
---

## Summary
A research paper from Hanyang University and Kyonggi University that developed a two-dimensional chloride diffusion tracking technique combining the silver nitrate ($AgNO_3$) colorimetric method with digital image analysis to visualize and quantitatively interpret the two-dimensional spatial penetration paths of chloride ions through fine cracks in reinforced concrete structures exposed to marine salt environments, and clarified the two-dimensional unsteady-state chloride concentration profiles according to crack opening width ($w = 0.05 \sim 0.5 mm$) and crack shape (single linear, branched, and V-shape wedge). It was demonstrated that when the crack width is restrained to at most $0.1 mm$, the lateral chloride diffusion depth falls sharply by more than 70 %.

## Key Contributions
- **Two-dimensional crack-shape-tailored chloride diffusion interpretation model ($D_{eff}(x, y, w)$) developed**: formalization of the superposition effect of vertical penetration through crack walls and two-dimensional diffusion at the crack tip.
- **Digital image boundary extraction precision of $0.1 mm$ achieved in $AgNO_3$ colorimetric reaction**: automatic extraction of the chloride ion critical concentration ($0.15 \%$) boundary line through optical density calibration.
- **Shielding effect of fine crack widths of at most $0.05 mm$ demonstrated**: applying ductile SHCC composites extends the time to rebar corrosion onset by a factor of 3.5 over ordinary concrete.
- **Residual service life prediction accuracy for marine infrastructure members improved by 40 %**: error of the one-dimensional Fick law fully corrected.

## Methods
- Specimens: $100 \times 100 \times 400 mm$ concrete prisms with flexure-induced cracks ($w = 0.05, 0.1, 0.2, 0.3, 0.5 mm$).
- Salt exposure: immersion in 3.5 % $NaCl$ solution (30, 60, 90, and 180 days).
- Measurement: after splitting specimens, spraying $0.1 M AgNO_3$; high-resolution image processing of the white precipitate ($AgCl$) boundary; comparison against 2D FDM diffusion numerical simulation.

## Results
- Chloride penetration depth and lateral diffusion data by crack width:

| Crack width $w$ (mm) | 90-day crack-zone penetration depth (mm) | 90-day lateral diffusion width (mm) | Sound-zone penetration depth (mm) | Rebar corrosion arrival risk |
| :---: | :---: | :---: | :---: | :--- |
| Sound (uncracked) | - | - | 12.5 | safe over 50 years |
| **0.05 mm (SHCC level)** | **18.5** | **8.2** | 12.5 | **safe (delayed)** |
| 0.10 mm | 32.0 | 18.5 | 12.5 | caution |
| 0.30 mm | 58.0 | 35.0 | 12.5 | severe (early corrosion) |
| 0.50 mm | > 75.0 (reaches rebar) | 52.0 | 12.5 | immediate damage risk |

## Related Notes
- [[lee-2015-performance-marine-concrete-floating-structures]] - marine concrete durability analysis
- [[crack-width-control]] - salt attack prevention via fine crack control
- [[concrete-durability-and-service-life]] - concrete durability service life theory
