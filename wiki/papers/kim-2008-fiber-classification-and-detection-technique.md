---
title: "Fiber Classification and Detection Technique for PVA-ECC Sectional Images (Kim et al., 2008)"
type: source_note
source: "sources/2008-fiber-classification-and-detection-technique.pdf"
citation: "Kim, Y.Y., Lee, B.Y., Kim, J.-K. PVA-ECC 단면 이미지의 섬유 분류 및 검출 기법 (Fiber classification and detection technique proposed for applying on the PVA-ECC sectional image). Journal of the Korea Concrete Institute 20(4) (2008) 513-522."
date: 2026-08-22
tags: [pva-fiber, image-analysis, fluorescence, ann, watershed-algorithm, fiber-dispersion, ecc]
---

# Fiber Classification and Detection Technique Proposed for Applying on the PVA-ECC Sectional Image

## Summary

This study proposes an automated fiber detection algorithm for fluorescence microscopy images to quantitatively evaluate the dispersion of non-conductive PVA fibers with low optical contrast in cementitious matrices. To correct primary binarization errors caused by the accidental merging of adjacent fibers, the authors introduced an ANN classifier dividing fiber blobs into 5 categories, paired with category-specific re-detection utilizing watershed segmentation and morphological reconstruction. The average error in detected fiber diameter was 6.84 %, which is well within the acceptable tolerance (< 10 %) for spatial dispersion evaluation.

## Key Contributions

1. **Five-category classification system**: Separated fiber blobs by watershed peak counts into Type S1 (single isolated fibers) and Type N, further sub-classifying Type N into N1 (fibers parallel to observation—circular, over-segmentation prone), N2 (perpendicular/inclined fibers—elongated ellipse, over-segmentation prone), N3 (merged S1 clusters), and N4 (merged N1/N2 clusters). Focused re-detection selectively on N3 and N4 to eliminate redundant processing.
2. **Five transformation-invariant geometric features**: Defined features invariant to rotation, translation, scaling, and contrast: $F_s$ (solidity = $A_{ob}/A_{ch}$), $F_c$ (packing density = $A_{ob}/A_{cc} = d/l = \cos\theta$, quantifying inclination angle $\theta$), $F_p$ (perimeter-to-area ratio), $F_l$ (major axis to area), and $F_{rl}$ (major axis to average major axis). Trained the ANN using a database of 1,350 fiber images.
3. **ANN classifier architecture**: Single hidden layer (5-4-4 structure optimized via 10-fold cross-validation), tan-sigmoid hidden layer, linear output layer, trained using Levenberg-Marquardt with weight decay. Jackknife verification accuracy: N1 97.7 %, N2 89.7 %, N3 97.0 %, N4 67.5 %, overall 95.3 %.
4. **Category-specific re-detection pipeline**: Applied standard watershed segmentation to N3, while applying morphological reconstruction (marker = mask − $h$, $h = 20$) prior to watershed segmentation on N4 to prevent over-segmentation.
5. **Experimental verification**: Detected average fiber diameter of 42.2 μm vs actual 39.5 μm (+6.84 % error due to slight threshold underestimation). Since spatial location is more critical than exact diameter for dispersion indices, this error is well within acceptable limits.

## Methods

- Specimens: Micromechanically designed PVA-ECC, cured in water for 28 d, cut with diamond saws ($13\ \text{mm} \times 36\ \text{mm} \times 20\ \text{mm}$, 13 mm × 36 mm × 20 mm), and polished.
- Imaging: Olympus BX51 fluorescence microscope with CCD camera (40$\times$ magnification). Workflow: RGB $\rightarrow$ grayscale $\rightarrow$ Otsu binary thresholding.
- Classifier: ANN with 5 input features scaled to [−1, 1] and 4 one-hot outputs, trained on 1,350 labeled images.
- Quantitative connection: Linked detection outputs with the statistical dispersion index method of Kim et al. (2007, JKNDT 27(2) 148-156).

## Results

- ANN classification confusion matrix achieved an overall accuracy of 95.3 % (N4 lowest at 67.5 % due to geometric diversity of long merged blobs).
- Feature value ranges (min/max): $F_s$ 0.3913/1, $F_c$ 0.028/0.962, $F_p$ 0.2461/1.0365, $F_l$ 0.0512/0.4538, $F_{rl}$ 0.3996/10.532.
- Successfully corrected clustering errors in N3/N4 categories and eliminated over-segmentation via morphological reconstruction (Fig. 13).

## Related Notes

- [[kang-2008-fiber-orientation-impacts-on-the]] — Image-processing evaluation of steel fiber distribution in UHSC, sharing the $F_c = \cos\theta$ orientation concept.
- [[li-2023-ecc-micromechanics-critical-review]] — Experimental verification of uniform fiber dispersion assumed in ECC micromechanical design.
- [[fiber-bridging-constitutive-law]] — Fiber dispersion as the prerequisite for bridging performance ($\sigma_B(\delta)$).
- [[lee-2009-extruded-ecc-panel-fiber-distribution]] — Application of this detection technique to extruded ECC panels.
