---
title: "Detectability of Subsurface Defects in Concrete Structures Using Pulsed Thermography (Tran et al., 2018)"
type: source_note
source: "sources/Tran-2018-Detectability of Subsurface Defects.pdf"
citation: "Tran, Q. H., Nguyen, V. T., & Huh, J. (2018). Detectability of subsurface defects in concrete structures using pulsed thermography. Applied Sciences, 8(8), 1319. https://doi.org/10.3390/app8081319"
date: 2026-08-24
tags:
  - pulsed-thermography
  - non-destructive-testing
  - subsurface-defects
  - infrared-camera
  - snr-analysis
  - concrete-delamination
---

## Summary
This paper, by a Chonnam National University research team, employed pulsed thermography (PT) non-destructive testing using a high-power halogen flash heat source and a high-resolution infrared thermal camera (FLIR SC655) to determine the defect detectability limit and signal-to-noise ratio (SNR) for the rapid, non-contact / wide-area-scanning diagnosis of cover-concrete delamination, internal voids, and crack defects in concrete infrastructure structures, through 3D transient heat-conduction numerical simulation and physical model experiments. It was demonstrated that artificial delamination defects located at depths of up to $50 mm$ could be precisely detected under the defect size-to-depth ratio condition of $D/d \ge 2.0$.

## Key Contributions
- **Quantitative formulation of the internal-defect detectability ratio in concrete ($D/d \ge 2.0$)**: statistical significance (SNR $> 3.0$) is secured when the defect diameter $D$ is at least twice the depth $d$.
- **Verification of the post-pulse-heating optimal observation time model ($t_{max} = 1.8 d^2 / \alpha$)**: established a technique for back-calculating the peak time of thermal-wave reflection as a function of defect depth.
- **Introduction of pulsed phase thermography (PPT) processing**: removed non-uniform surface emissivity and illumination noise 100 %, improving defect-boundary sharpness 3-fold.
- **Proposal of a rapid automated inspection system for bridge decks and tunnel linings**: laid the groundwork for vehicle-mounted real-time scanning technology.

## Methods
- Specimens: concrete slabs of $500 \times 500 \times 150 mm$ ($f_c = 35 MPa$), with artificial defects embedded (polystyrene and air pockets, diameter $20 \sim 100 mm$, embedment depth $10 \sim 60 mm$).
- Thermography system: 2000 W high-power pulsed halogen lamps and a high-resolution uncooled microbolometer IR camera ($640 \times 480$ pixels, thermal sensitivity $0.05 °C$).
- Data processing: MATLAB-based absolute temperature contrast and Fourier phase transform algorithms.

## Results
- Thermographic detection performance data by defect size and depth:

| Defect diameter $D$ (mm) | Embedment depth $d$ (mm) | Size/depth ratio ($D/d$) | Max surface temperature difference $\Delta T_{max}$ ($°C$) | Peak arrival time $t_{max}$ (s) | Detection success |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 100 mm | 20 mm | 5.0 | $2.45 °C$ | 24 s | Perfectly detected (sharp) |
| 60 mm | 30 mm | 2.0 | $0.85 °C$ | 52 s | Detected successfully (good) |
| 40 mm | 30 mm | 1.33 | $0.28 °C$ | 55 s | Partially detected (blurred boundary) |
| 20 mm | 40 mm | 0.5 | $0.04 °C$ | 95 s | Not detectable ($D/d < 1.0$) |

## Related Notes
- [[lee-2007-surface-crack-evaluation]] - Image-processing-based concrete crack diagnosis
- [[segura-2010-measurement-degraded-depth-concrete-ultrasonic]] - Ultrasonic surface-wave measurement of degraded depth in concrete
- [[ndt-and-shm-of-cementitious]] - Review of non-destructive testing technologies
