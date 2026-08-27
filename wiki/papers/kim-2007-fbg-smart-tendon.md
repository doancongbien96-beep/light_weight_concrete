---
title: "FBG 센서 내장 스마트 강연선 개발 (김재민 외, 2007)"
type: source_note
source: "sources/JSGJAE_2007_y2007m04a_33.pdf"
citation: "김재민·김영상·김현우·서동남·윤충방. FBG 센서를 내장한 스마트 강연선 개발. 한국지진공학회 2007년 학술대회 논문집, Session 1(스마트 사회기반시설 연구센터 특별세션) (2007.4) pp. 33-38. / Kim, J.-M., Kim, Y.-S., Kim, H.-W., Seo, D.-N., Yun, C.-B. Development of Smart Tendon Instrumented with Optical FBG Sensors."
date: 2026-08-22
tags: [fbg-sensor, smart-tendon, structural-health-monitoring, prestressing, fiber-optic-sensor]
---

# Development of Smart Tendon Instrumented with Optical FBG Sensors

> Note: This note is based on OCR reading of a scanned conference paper; parts of Section 3 and some numerical equations contain OCR noise. Contextual reconstruction is applied where appropriate.

## Summary

This conference paper by Prof. Jae-Min Kim (Chonnam National University) and Prof. Chung-Bang Yun (KAIST) proposes a smart prestressing strand embedded with fiber Bragg grating (FBG) optical sensors. By replacing the central core wire (king wire) of a 7-wire strand with a hollow steel tube and bonding an optical FBG sensor inside the core using polyester resin, the authors validated the operational principle of real-time tendon strain monitoring through tensile loading tests. The work contributes to the structural health monitoring (SHM) domain.

## Key Contributions

1. **Hollow king wire replacement concept**: Replaced only the center king wire (diameter ~5.24 mm) with a pultruded hollow steel tube (outer diameter 5 mm, inner diameter 1 mm); since the king wire accounts for only 1/7 of the total cross-sectional area, degradation in overall strand stiffness and tensile behavior was negligible.
2. **Quantification of resin-hardener mix ratio on sensor bonding**: In specimens with low hardener ratios (~1/2 %), debonding at the FBG-adhesive interface occurred around 0.04 % strain (400 με); the effective maximum measurement range of the FBG sensor was determined to be approximately 6,500 με (0.65 %).
3. **Linear sensor response under cyclic loading**: Confirmed high linearity and agreement between embedded FBG readings and external electrical resistance strain gauges during loading-unloading-reloading cycles.
4. **Systematic synthesis of optical fiber tendon sensing literature**: Reviewed GFRP rockbolts (Nellen 1999, diameters 3/8/22 mm, lengths 3~5 m, strains up to 1.6 %), CFRP cables (Nellen 1999, diameter 5 mm, length 5 m, 0.8 %), FRP-OFBG stay cables (Zhou 2005), PWS cables (Zhou 2004), and PS tendons (Li 2005).

## Methods

- FBG operating principle: UV laser inscribes 1~10 mm periodic Bragg gratings onto optical fibers to reflect specific wavelengths; strain and temperature shifts are detected via Bragg wavelength shifts (Eq. (1) incorporating thermal expansion $\alpha$, thermo-optic coefficient $\xi$, and photoelastic constant $P_e$).
- Specimens: 1 m long smart strands in 3 configurations (varying polyester resin-to-hardener ratios) plus standalone hollow king wires (outer diameter 5 mm, inner diameter 1.8 mm, length 500 mm). Sensor cured for ~1 h after bonding.
- Tensile loading tests comparing embedded FBG readings against external strain gauges under ultimate and cyclic loading.
- Support: Smart Infra-Structure Technology Center (SISTeC), 2006.

## Results

- Load-strain curves showed minimal difference between standard 7-wire strands and hollow king wire replacement specimens (king wire carries only 1/7 of the total load).
- FBG sensor strain readings agreed closely with surface-mounted electrical resistance strain gauges for both smart king wires and 7-wire smart strands.
- Identified three practical development requirements: (1) improving the linear elastic range of hollow king wire materials up to operational prestress strains (~0.5 %), (2) optimizing the resin-hardener ratio for both workability and interfacial bond strength, and (3) developing protective termination connectors against field installation damage.

## Related Notes

- [[iten-2012-strain-sensing-cables]] — Subsequent technical developments in fiber-optic strain sensing cables.
- [[lim-2017-cnt-crack-monitoring]] — Comparison between external FBG sensing and internal CNT self-sensing composites.
- [[lee-2005-enhanced-binarization-crack]] — NDT and image-based crack detection methodologies.
- [[kim-2008-fiber-classification-and-detection-technique]] — Image-based detection and classification algorithms.
- [[kim-2017-enhanced-strain-measurement-range]] — Extension of smart tendon measurement range from 0.92 % to 1.73 % via polyimide tubing.
- [[watkins-2003-smart-bridges]] — Fiber-optic SHM sensor networks on bridges.
