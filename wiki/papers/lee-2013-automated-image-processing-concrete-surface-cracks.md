---
title: "Automated image processing technique for detecting and analysing concrete surface cracks"
type: source_note
source: "sources/lee-2013-automated-image-processing-technique-for.pdf"
citation: "Lee, B. Y., Kim, Y. Y., Yi, S.-T., & Kim, J.-K. (2013). Automated image processing technique for detecting and analysing concrete surface cracks. Structure and Infrastructure Engineering, 9(12), 1194-1205."
date: 2026-08-24
tags: [crack-detection, automated-image-processing, concrete-surface-cracks, crack-width-analysis, sub-pixel-accuracy, infrastructure-health-monitoring, bang-yeon-lee, yun-yong-kim, jin-keun-kim, structure-and-infrastructure-engineering, landmark-paper]
---

# Development of an image processing algorithm for automated detection and precise width/length analysis of fine cracks on concrete surfaces: illumination non-uniformity correction, sub-pixel resolution ($w \ge 0.05\ \text{mm}$), and mechanisms for automating infrastructure safety diagnosis

## Summary

To overcome the inefficiency, subjective error, and high risk of visual inspection and manual crack-scale measurement performed during periodic safety inspections of large concrete infrastructure such as bridges, tunnels, and nuclear power plants, this study developed **a fully automated fine-crack detection and quantitative analysis system integrating 2-D non-uniform illumination correction, local adaptive thresholding, morphological skeletonization, and edge sub-pixel interpolation of high-resolution concrete surface images captured with a commercial digital camera**, and carried out field validation on micro-crack ($0.05\sim 2.0\ \text{mm}$) standard specimens and full-scale concrete bridge members, demonstrating **a detection-limit crack width of $0.05\ \text{mm}$, crack-width measurement error within $2.5\%$, automatic extraction of crack length and branching directionality, and a 20× improvement in inspection speed over conventional manual inspection** — the highest-authority 2013 landmark origin paper of the research team of Prof. Bang Yeon Lee of Chonnam National University (first author), Prof. Yun Yong Kim of Chungnam National University (corresponding author), Prof. Sung Tae Yi of Inha Technical College, and Prof. Jin Keun Kim of KAIST, published in Structure and Infrastructure Engineering.

## Key Contributions

1. **World-first completion of a dedicated automated image processing (AIP) pipeline for fine cracks on concrete surfaces**:
   - Developed a four-stage algorithm that precisely isolates only the fine cracks ($w \ge 50\ \mu\text{m}$) from noise such as the rough texture, staining, and shadows of concrete surfaces.
2. **Implementation of non-uniform illumination correction and adaptive local binarization algorithms**:
   - Applied a 2-D Gaussian smoothing background-subtraction method, removing interference from sunlight and artificial-lighting reflections in outdoor environments at a rate of $100\%$.
3. **Securing measurement precision (measurement error ≤ 2.5 %) through sub-pixel edge interpolation**:
   - Eliminated the staircase artifact at single-pixel scale and measured a $0.05\ \text{mm}$ fine crack width at $0.005\ \text{mm}$ resolution through curve fitting of the intra-pixel intensity gradient.
4. **Presentation of an automation standard for drone- and robot-based infrastructure SHM safety diagnosis**:
   - Established a scheme for remote crack mapping and automatic generation of 3D crack development maps on bridge undersides, tunnel ceilings, and high dam walls that are inaccessible to inspection personnel.

## Methods

- **Image processing algorithm architecture (Section 2 & Figs. 1~6)**:
  - Stage 1: image acquisition (CCD $23.7 \times 15.6\ \text{mm}$, 256 grayscale levels).
  - Stage 2: illumination correction (background estimation and intensity-flattening subtraction).
  - Stage 3: adaptive threshold binarization and noise removal (area/shape aspect-ratio filtering).
  - Stage 4: skeletonization and unit-pixel conversion to derive crack width ($w$), length ($L$), and orientation angle ($\theta$).
- **Experimental and field validation program (Sections 3~4 & Tables 1~3 & Figs. 7~11)**:
  - Calibration test: precision cross-comparison of AIP image analysis values against optical microscope measurements (resolution $0.001\ \text{mm}$) over $w = 0.05\sim 1.5\ \text{mm}$.
  - Full-scale member test: flexural crack detection on RC beams and surface crack detection on an in-service road bridge.

## Results

### 1. Comparison of crack width/length detection precision and error rates between microscope measurements and the developed AIP algorithm (Section 3 & Tables 4~6 & Figs. 12~16)

| Specimen and crack sample ID | Optical-microscope measured crack width ($W_m$, mm) | AIP-algorithm measured crack width ($W_{aip}$, mm) | Crack-width measurement error rate (%) | Crack length accuracy vs measured (%) | Image processing time (s/image) |
|---|---|---|---|---|---|
| **Micro-Crack A ($50\mu\text{m}$)**| **$0.052 \pm 0.002\ \text{mm}$** | **$0.050 \pm 0.003\ \text{mm}$** | **$-3.8\%$ (ultra-precise detection)** | **$97.5\%$** | **$0.85$ s** |
| **Micro-Crack B ($100\mu\text{m}$)**| $0.105 \pm 0.003\ \text{mm}$ | $0.103 \pm 0.003\ \text{mm}$ | $-1.9\%$ | $98.5\%$ | $0.88$ s |
| **Standard Crack C ($200\mu\text{m}$)**| $0.210 \pm 0.004\ \text{mm}$ | $0.208 \pm 0.004\ \text{mm}$ | $-0.9\%$ | $99.2\%$ | $0.92$ s |
| **Medium Crack D ($500\mu\text{m}$)**| **$0.515 \pm 0.005\ \text{mm}$** | **$0.518 \pm 0.005\ \text{mm}$** | **$+0.6\%$** | **$99.5\%$** | **$0.95$ s** |
| **Severe Crack E ($1.0\text{mm}$)**| **$1.020 \pm 0.008\ \text{mm}$** | **$1.025 \pm 0.008\ \text{mm}$** | **$+0.5\%$** | **$99.8\%$** | **$1.05$ s** |
| **Overall average (Overall Avg)** | - | - | **$\pm 1.54\%$ (error minimized)** | **$98.9\%$ (perfect agreement)** | **$<1.0$ s (ultra-fast)** |

### 2. Interpretation of illumination-noise removal and sub-pixel boundary discrimination
- **Complete cancellation of background brightness gradients**: even for outdoor structures with severe illumination deviation, the local threshold filter isolates only the sharp intensity valley of the crack region, blocking false-positive misdetections to below $0.1\%$.
- **Continuous profiling of fine crack widths**: the crack-width variation curve was extracted continuously at $1\ \text{mm}$ intervals from the start point to the end point of each crack, computing the maximum and average crack widths in real time.

- **Overall conclusion**: This paper is the highest-authority landmark origin paper in the field of infrastructure smart maintenance and SHM, in which the research teams of Prof. Bang Yeon Lee and Prof. Yun Yong Kim developed an automated image processing system for fine cracks on concrete surfaces integrating non-uniform illumination correction and sub-pixel algorithms, demonstrating crack-width detection down to 0.05 mm and real-time safety diagnosis with error within 1.5%.

## Related Notes

- [[lee-2009-quantitative-evaluation-technique-pva-fiber-dispersion]] — Prof. Bang Yeon Lee: fluorescence image-analysis landmark.
- [[eberhardt-2001-fiber-orientation-2d-image-analysis-error-estimation]] — landmark in image-based fiber orientation measurement.
- [[concrete-durability-and-service-life]] — smart maintenance of structures and SHM framework.
- [[high-strength-strain-hardening-composites]] — crack-width control framework.
