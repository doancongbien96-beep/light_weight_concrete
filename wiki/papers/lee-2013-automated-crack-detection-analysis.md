---
title: "Automated Image Processing Technique for Detecting and Analysing Concrete Surface Cracks (Lee et al., 2013, Structure and Infrastructure Engineering)"
type: source_note
source: "sources/Lee 등 - 2013 - Automated image processing technique for detecting and analysing concrete surface cracks.pdf"
citation: "Lee, B.Y., Kim, Y.Y., Yi, S.T., Kim, J.-K. Automated image processing technique for detecting and analysing concrete surface cracks. Structure and Infrastructure Engineering 9(6) (2013) 567-577. doi:10.1080/15732479.2011.593891"
date: 2026-08-22
tags: [crack-detection, image-processing, binarization, morphology, neural-network, crack-pattern-recognition, ndt, user-group]
---

# Automated Image Processing Technique for Detecting and Analysing Concrete Surface Cracks

## Summary

This paper consolidated and completed the user-group NDT-axis Korean-language series (2005 improved binarization and morphology analysis, 2005/2006 ANN pattern recognition, 2007 crack evaluation) as an international journal article (Bang Yeon Lee first author; corresponding author Yun Yong Kim of Chungnam National University, with Jin-Keun Kim of KAIST; submitted 2008, published online 2011, issue dated 2013). Background illumination non-uniformity was corrected by morphological operations, detection performance was enhanced through improved binarization (local binarization plus secondary extraction) and shape analysis, and the algorithms for computing crack width, length, and orientation were combined with a five-class pattern recognition artificial neural network (horizontal, vertical, diagonal −45°, diagonal +45°, random) into a single pipeline. Compared with an optical crack microscope, the mean relative width error was 3.8 %, orientation error 0.67~2.8 %, and pattern recognition accuracy 100 % (38 images).

## Key Contributions

1. **Illumination non-uniformity correction**: background brightness was normalized by subtracting the opening result (dilation followed by erosion, with a circular structuring element of radius 15 pixels) from the original image. Comparison of pixel-value profiles before and after correction confirmed a flattened background, securing the premise of binarization performance.
2. **Three elements of improved detection**: (a) noise removal that sets a pixel to 1 when five or more of its 3×3 neighbors equal 1, (b) local binarization applied five times over an 11×11 pixel region around object boundaries found by global binarization (Otsu), and (c) secondary extraction reapplying Otsu to a modified image from which first-pass objects had been removed — capturing fine cracks whose brightness resembles the background.
3. **Modified filling density index Fpd = Ao/Acc**: the ratio of object area (Ao) to the area of the circumscribed circle (Acc) of the object's bounding rectangle converges to 0 for slender cracks and to 1 for circular defects. A threshold of 0.12 was empirically optimized through numerical experiments to discriminate cracks from other defects in a second pass.
4. **Automated crack-characteristic computation algorithms**: after Zhang-Suen thinning, boundary extraction, and 8-connected labeling, (a) width is the sum of distances from each centerline pixel to the two nearest boundary pixels (two of four distance filters A~D selected by crack direction), (b) length accumulates unit pixel steps of 1.0 or √2 starting from the start pixel whose 9-pixel neighbor sum equals twice its label number, and (c) orientation follows from the arctan relation between start and end coordinates.
5. **Pattern recognition ANN**: total-projection-based features — projection lengths at each rotation angle (180 values), averaged three at a time to yield 60 features → network structure 60-4-5, hyperbolic tangent sigmoid transfer function, Bayesian regularization training against overfitting.

## Methods

- Image acquisition: digital camera with a 23.7 × 15.6 mm CCD, lens assumed parallel to the surface. The unit pixel length α0 was computed from shooting distance ℓ, focal length ℓfocus, CCD width oCCD, and total pixel count Npix; a distance- and focal-length-dependent correction coefficient γ = 0.47·ℓ^0.058·ℓfocus^0.075 was determined by regression.
- Measurement condition verification: crack widths at five points of one identical crack measured under seven combinations of camera-to-surface distance (865~1915 mm) and focal length (28~70 mm).
- Four test-image types for detection performance: cracks with many meaningless objects, branched cracks, small cracks attached along a main crack, and cracks on contaminated backgrounds with stains and small holes.
- Reference-device comparison: widths against an optical crack microscope, lengths against a ruler graduated at 1 mm, orientations against a protractor graduated at 1°. Relative deviation defined as RD = |w_new − w_con|/w_con.

## Results

- Standard deviation of crack width across measuring conditions (distance, focal length): 0.024~0.045 mm (mean 0.036 mm) — attributable to resolution differences but negligible within the tested conditions.
- Width: relative error versus microscope 0.67~5.9 % (mean 3.8 %). Length: 3.98~21.3 % versus ruler, a larger spread (a limitation of straight-ruler use, improvable by segmented measurement). Orientation: 0.67~2.8 % versus protractor.
- Pattern recognition: 100 % correct classification in all five categories versus human judgment (horizontal 4 images, vertical 19, diagonal −45° 7, diagonal +45° 5, random 3).
- Detection tests: clear separation of small holes and stains from cracks, and complete detection of branched cracks. One limitation: a single fine crack beside a main crack went undetected because its Fpd exceeded 0.12 — the trade-off that raising the threshold increases false positives is stated explicitly.

## Related Notes

- [[lee-2005-enhanced-binarization-crack]] — KCI origin of the improved binarization and morphology analysis underlying this paper's detection pipeline.
- [[lee-kim-kim-2006-crack-pattern-recognition]] — KCI origin of total-projection features plus ANN pattern recognition (succeeded by this paper's 60-4-5 network).
- [[lee-2007-surface-crack-evaluation]] — Crack evaluation technique on the same NDT axis (Journal of the Korean Society for Nondestructive Testing).
- [[kim-2008-fiber-classification-and-detection-technique]] — Sister technique from the same group's image-processing axis, retargeting detection from cracks to fibers (sharing watershed segmentation and morphological reconstruction).
- [[pseudo-strain-hardening-criteria]] — Quantitative crack-width measurement presupposes judging the expression of fine multiple cracking in ECC; this technique supplies that tooling axis.
