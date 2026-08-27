---
title: "Improved Sectional Image Analysis Technique for Evaluating Fiber Orientations in Fiber-Reinforced Cement-Based Materials (Lee et al., 2016, Materials)"
type: source_note
source: "sources/Lee-2016-Improved sectional image analysis tec.pdf"
citation: "Lee, B.Y., Kang, S.-T., Yun, H.-B., Kim, Y.Y. Improved sectional image analysis technique for evaluating fiber orientations in fiber-reinforced cement-based materials. Materials 9(1) (2016) 42. doi:10.3390/ma9010042"
date: 2026-08-22
tags: [fiber-orientation, image-analysis, sectional-image, genetic-algorithm, orientation-distribution, resolution-error, user-group]
---

# Improved Sectional Image Analysis Technique for Evaluating Fiber Orientation

## Summary

An MDPI Materials paper with Bang Yeon Lee of Chonnam National University as first author (co-authors: Yun Yong Kim · Chungnam National University, corresponding author; Su-Tae Kang · Daegu University; H.-B. Yun · UCF). The "improved sectional image analysis technique" in the filename refers not to cracks but to evaluating **fiber orientation**. Whereas the conventional approach directly estimates the orientation angle θ from the aspect ratio l/d of each individual fiber in a sectional image, this paper quantified with artificial images how that approach incurs large systematic errors at low angles and low resolution (l/d is theoretically 1/cosθ, so the l/d difference between 0° and 30° is merely 15.3 %), and instead proposed an indirect estimation technique that exploits in reverse the relationship that "the number of fibers itself visible on a cut section depends on the orientation distribution," fitting Xia et al.'s two-parameter distribution function with a genetic algorithm. Verification showed that the probability-density error decreased by up to 80.6 % relative to direct measurement, especially under the 2D distribution + low-resolution condition.

## Key Contributions

1. **Error structure of direct measurement clarified**: the sensitivity of direct measurement via θ = arccos(d/l) collapses as θ grows smaller (l/d difference of 15.3 % between 0°↔30°, 41.2 % between 0°↔45°; the l/d at θ = 85° is 8.08 times that at 45°). Resolution effects pile on top — if the fiber diameter is 5 pixels, θ = 0° is misjudged as 22.2° and 15° as 41.2° (error below 1° at 150 pixels). If a 200 µm steel fiber spans 5 pixels on screen, an error of 1 pixel translates directly into a 40 µm measurement error.
2. **Count-based indirect estimation framework**: the shape parameters p, q of Xia et al.'s two-parameter exponential-type distribution function g(θ) are optimized with the difference |Nf,t − Nf,m| between the theoretical fiber count Nf,t = (4VfAs/πd²)·∫g(θ)cosθ dθ (Vf = fiber volume fraction, As = cross-sectional area) and the count Nf,m measured from the image as the fitness. p = 1, q = 0.5 corresponds to sinθ (fully 3D random), and p = q = 1 to 1/π (fully 2D random).
3. **Upgraded detection pipeline**: after Otsu threshold binarization, falsely detected objects are filtered out by an area threshold, and clumped fiber images are separated by watershed segmentation + morphological reconstruction (reconstruction suppresses oversegmentation). Each fiber is characterized by the major axis l and minor axis d of the ellipse having the same normalized second-order central moments.
4. **Conditions of applicability presented**: a practical tool that allows more accurate evaluation of the effect of orientation on mechanical performance when imaging resolution (pixel count) is limited — the count relations are also organized together: under a 3D distribution the number of fibers visible per section is 1/2 of the 1D case, and under a 2D distribution it is 2/π.

## Methods

- Artificial verification images: assuming Vf = 2.0 vol %, 6 combinations of fiber diameter 5/15/25 pixels × 2D/3D random distributions — I05-3 (2000×2000, 2038 fibers), I05-2 (2594), I15-3 (6000×6000, 2038), I15-2 (2594), I25-3 (5000×5000, 510), I25-2 (649).
- Genetic algorithm: real-valued GA, population size 200, roulette-wheel selection, crossover by random gene combination, mutation by adding Gaussian random numbers of mean 0, terminated after 50 consecutive generations without objective-function improvement.
- Comparison target: direct measurement of individual fiber orientation angles following Lee et al.'s earlier technique (2009 quantitative evaluation of PVA fiber dispersion; reference [8] of the paper).
- Funding: Ministry of Land, Infrastructure and Transport Technology Advancement Research Program 15CTAP-C097490-01, NRF 2015R1A5A1037548.

## Results

- The probability density function of direct measurement deviates substantially from the true distribution in the low-θ region, and 2D-distribution images rich in low-θ fibers show larger errors than 3D ones (the mean per-fiber error is 32.4 % lower in 3D than in 2D).
- Effect of resolution improvement: the mean per-fiber error decreases by 70.0 % from I05-2 to I15-2, and by 80.8 % at I25-2 (decreases of 60.1 % from I05-3 to I15-3 and 79.3 % at I25-3).
- Proposed technique vs direct measurement (probability-density difference against the true distribution): in 3D, I05-03 improved by 72.7 % and I15-03 by 43.7 %, but I25-03 worsened by 21.9 % (attributed to the PDF fluctuation of the 510-fiber sample). In 2D, improvements were 80.6 % for I05-02, 56.1 % for I15-02, and 17.1 % for I25-02.
- In conclusion, the proposed technique is particularly excellent under the 2D distribution + low pixel-count condition, and once resolution becomes sufficient the errors of the two methods converge.

## Related Notes

- [[kim-2008-fiber-classification-and-detection-technique]] — the group's original fiber detection algorithm in which this paper's pipeline (binarization · watershed segmentation · morphological reconstruction) is rooted
- [[kim-2007-fiber-dispersion-fluorescence]] — fluorescence-image-based quantification of fiber dispersion (preceding study of the same group's fiber-distribution evaluation axis)
- [[lee-2009-extruded-ecc-panel-fiber-distribution]] — group precedent applying fitting of the same Xia-family orientation distribution function to real extruded ECC sections
- [[fiber-bridging-constitutive-law]] — the snubbing effect (increase in inclined-fiber pullout load) treated in the introduction and the conversion of orientation PDFs into composite bridging stress correspond to an orientation extension of this bridging constitutive law
- [[li-2023-ecc-micromechanics-critical-review]] — hub comprehensively organizing the effect of orientation on tensile behavior within the micromechanics frame
- [[mlekusch-1999-fiber-orientation-contrast]] — original work on contrast processing in sectional-image fiber analysis (polymer systems)
