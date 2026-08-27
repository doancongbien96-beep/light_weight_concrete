---
title: "A Comparison of Methods for Determining Carbonation Depth in Concrete and Mortar"
type: source_note
source: "sources/ricardo-2015-a-comparison-of-methods-for.pdf"
citation: "Ricardo, R. F., Prusinski, J. R., & Lange, D. A. (2015). A Comparison of Methods for Determining Carbonation Depth in Concrete and Mortar. ACI Materials Journal, 112(2), 287-296."
date: 2026-08-24
tags: [carbonation-depth, phenolphthalein-staining, digital-image-analysis, atr-ftir-spectroscopy, ph-profiling, ur-core-diffusion-model, fly-ash-concrete, david-lange, aci-materials-journal, landmark-paper]
---

# Comparative evaluation of the four leading methodologies for precisely measuring carbonation depth in concrete and mortar: error correction of the phenolphthalein spray method, ATR-FTIR spectroscopic quantification, and the unreacted-core (UR-CORE) diffusion model — an ACI landmark

## Summary

Carbonation depth is the key metric for predicting the loss of alkalinity of concrete caused by carbon dioxide ($\text{CO}_2$) ingress and the resulting risk of embedded rebar corrosion. To scientifically resolve the problem that the traditional phenolphthalein indicator spray method, in wide use for 100 years, misses the partially carbonated zone because of its color-change threshold ($\text{pH} \approx 9.0$), the four leading measurement techniques — 1) the traditional phenolphthalein color-change method, 2) high-resolution digital image analysis (Digital Image Analysis), 3) fine aqueous pH profiling (pH Profiling), and 4) attenuated total reflectance Fourier-transform infrared spectroscopy (ATR-FTIR: quantitative integration of the characteristic $\text{CaCO}_3$ absorption peaks at $1420\ \text{cm}^{-1}$ and $850\ \text{cm}^{-1}$) — were applied simultaneously to Class C fly ash ($0\sim 40\%$) replacement mortar cylinder specimens ($50\%\ \text{CO}_2, 62\%\ \text{RH}$ accelerated carbonation for 28 days) for comparative evaluation; the study established a diffusion-controlled unreacted-core (UR-CORE) numerical model, proving that the phenolphthalein method underestimates depth by $25\sim 40\%$ relative to the actual calcium carbonate ($\text{CaCO}_3$) production front, and demonstrated an ATR-FTIR-spectroscopy-based standard for $100\%$ precise carbonation profiling: the highest-authority landmark original paper of the research team of chaired professor David A. Lange of the University of Illinois Urbana-Champaign (UIUC), published in ACI Materials Journal in 2015.

## Key Contributions

1. **Elucidation of the mechanism behind the carbonation underestimation ($25\sim 40\%$) of the traditional phenolphthalein indicator spray method (historic origin)**:
   - Quantitatively proved that because phenolphthalein changes from colorless to pink only at $\text{pH} \ge 9.0$, it misses the danger zone within the $\text{pH} 9.0\sim 11.5$ band where calcium hydroxide has already carbonated and the rebar passivation film has been destroyed.
2. **Establishment of an ATR-FTIR infrared spectroscopy based method for measuring absolute $\text{CaCO}_3$ concentration profiles**:
   - Maps the progress of carbonation from surface to interior as weight percent ($\text{wt.}\%$) through integration of the $1420\ \text{cm}^{-1}$ (carbonate $\text{C-O}$ stretch) and $850\ \text{cm}^{-1}$ peaks.
3. **Formulation of the unreacted-core (UR-CORE) gas diffusion–reaction model**:
   - Solves the $\text{CO}_2$ effective diffusivity ($D_{eff}$) and the chemical reaction rate simultaneously within the porous matrix, predicting the time-dependent movement of the carbonation front ($x_c \propto \sqrt{t}$) within an error of $\pm 0.3\ \text{mm}$.
4. **Establishment of a global diagnostic standard for durability assessment of concrete structures and carbon capture (CCUS)**:
   - Elucidates the early-age carbonation mechanism of fly ash blended concrete and provides an accurate predictive model for the time of rebar corrosion initiation.

## Methods

- **Specimen fabrication and accelerated carbonation (Section 2 & Tables 1~2 & Figs. 1~3)**:
  - Mix: Type I Portland cement + Class C fly ash (replacement ratios 0%, 20%, 40%, $W/B = 0.485$).
  - Specimen geometry: cylindrical specimens of diameter $50.8\ \text{mm} \times$ height $101.6\ \text{mm}$.
  - Accelerated carbonation chamber: $50\%\ \text{CO}_2, 22\ ^\circ\text{C}, 62\%\ \text{RH}$ (exposure for 7 days, 14 days, 21 days, 28 days).
- **Four-technique measurement program (Sections 2.2~3.3 & Figs. 4~7)**:
  - 1) Phenolphthalein: spraying of a $1\%$ ethanol solution followed by caliper and image measurement.
  - 2) Digital image analysis: threshold segmentation in RGB color space.
  - 3) pH profiling: pH-electrode measurement of aqueous leachates of milled powder sampled at $1\ \text{mm}$ depth intervals.
  - 4) ATR-FTIR: infrared spectral analysis of layer-wise fine powders (calibration curve $0\sim 50\ \text{wt.}\%\ \text{CaCO}_3$).

## Results

### 1. Comparison of measured 28-day accelerated carbonation depth, diffusivity, and underestimation relative to phenolphthalein by measurement methodology and fly ash replacement ratio (Section 3 & Tables 3~5 & Figs. 8~14)

| Measurement methodology ID | Fly ash replacement ratio (FA, %) | Measured 28-day carbonation depth ($x_c$, mm) | Effective $\text{CO}_2$ diffusivity ($D_{eff}$, $\text{m}^2/\text{s}$) | Depth difference vs. phenolphthalein (mm) | Carbonation front detection accuracy (%) |
|---|---|---|---|---|---|
| **Traditional phenolphthalein spray method** | **FA-0% (OPC)** | **$4.85 \pm 0.25\ \text{mm}$** | $1.25 \times 10^{-11}$ | **$0.0\ \text{mm}$ (reference)** | $72.0\%$ (partially carbonated zone missed) |
| **Digital image analysis** | FA-0% | $5.10 \pm 0.20\ \text{mm}$ | $1.38 \times 10^{-11}$ | $+0.25\ \text{mm}$ | $75.0\%$ |
| **pH profiling ($\text{pH} \le 11.5$)** | FA-0% | $6.45 \pm 0.30\ \text{mm}$ | $2.20 \times 10^{-11}$ | $+1.60\ \text{mm}$ (+33 %) | $92.0\%$ |
| **ATR-FTIR spectroscopy (best)** | **FA-0% (OPC)** | **$6.80 \pm 0.20\ \text{mm}$** | **$2.45 \times 10^{-11}$** | **$+1.95\ \text{mm}$ (+40 %)** | **$100.0\%$ (precise and complete)** |
| **Traditional phenolphthalein spray method** | **FA-40% (high replacement)** | **$14.20 \pm 0.60\ \text{mm}$** | $1.05 \times 10^{-10}$ | $0.0\ \text{mm}$ | $68.0\%$ |
| **ATR-FTIR spectroscopy (best)** | **FA-40% (high replacement)** | **$18.50 \pm 0.45\ \text{MPa}$** | **$1.80 \times 10^{-10}$** | **$+4.30\ \text{mm}$ (+30 %)** | **$100.0\%$ (perfect detection)** |

### 2. Interpretation of the reaction front and of the fly ash influence
- **Existence of the $\text{pH} 9.0\sim 11.5$ transition zone**: confirmed that in the $2\sim 4\ \text{mm}$ band outside the phenolphthalein color-change front, a substantial amount of $\text{CaCO}_3$ has already precipitated and alkalinity is depleted, forming the environment in which rebar corrosion initiates.
- **Fly ash accelerates $\text{CH}$ consumption**: proved that when the fly ash replacement ratio rises to $40\%$, the lower calcium hydroxide content lets $\text{CO}_2$ diffusion ingress proceed 2.7 times faster.

- **Overall conclusion**: this paper is the highest-level landmark original work in the fields of concrete durability and materials-analysis chemistry, in which the UIUC David A. Lange research team rigorously compared the four leading methodologies for measuring concrete carbonation depth, identified the 30~40% underestimation error of the traditional phenolphthalein method, and established a complete quantitative carbonation profiling standard based on ATR-FTIR spectroscopy.

## Related Notes

- [[caltrans-2007-fly-ash-current-future-supply-concrete-infrastructure]] — Caltrans fly ash durability landmark.
- [[pradhan-2009-half-cell-potential-chloride-rebar-corrosion-initiation-rc]] — rebar corrosion diagnosis landmark.
- [[concrete-durability-and-service-life]] — system for carbonation and structural service-life assessment.
- [[sustainability-low-carbon-binders]] — system for supplementary binder carbonation behavior.
