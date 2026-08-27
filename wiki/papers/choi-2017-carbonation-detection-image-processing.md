---
title: "Image-processing technique to detect carbonation regions of concrete sprayed with a phenolphthalein solution"
type: source_note
source: "sources/choi-2017-image-processing-technique-to-detect-carbonation.pdf"
citation: "Choi, J.-I., Lee, Y., Kim, Y. Y., & Lee, B. Y. (2017). Image-processing technique to detect carbonation regions of concrete sprayed with a phenolphthalein solution. Construction and Building Materials, 154, 451-461."
date: 2026-08-23
tags: [carbonation-depth, image-processing, phenolphthalein, otsu-binarization, convex-hull, green-intensity, ndt, user-group]
---

# Two-Stage Image-Processing Technique for Automatic Detection of Carbonation Regions in Phenolphthalein-Sprayed Concrete Cross Sections

## Summary

In measuring the carbonation depth of concrete, which directly determines the assessment of the residual service life of reinforced concrete structures, this study developed a two-stage automatic image-processing algorithm that combines green-intensity extraction (the complement of the magenta coloration), Otsu-based binarization and morphological operations (primary detection), and convex-hull geometric filtering (secondary detection), in order to overcome the operator subjectivity, low reproducibility, and aggregate-paste boundary reading errors inherent to manual visual measurement after spraying a phenolphthalein solution, and validated it rigorously on a variety of real concrete cross-sectional images (corresponding author Prof. Bang Yeon Lee, Chonnam National University; co-authors Yoon Lee of Daejeon University and Yun Yong Kim of Chungnam National University). The proposed algorithm completely excluded the ambiguous boundary between carbonated and non-carbonated regions and the interference of aggregate colors, removed 100 % of the false detections of micro voids and aggregates inside the non-carbonated core, and demonstrated fully automatic extraction of a high-precision carbonation boundary contour profile together with the mean carbonation depth.

## Key Contributions

1. **Color contrast maximization via Green Intensity channel extraction**:
   - Separating the **Green channel**, which is the complement of the magenta (R+B within RGB) that develops when the phenolphthalein solution reacts with the non-carbonated alkaline region ($\text{pH} > 9.2$), drastically increases the brightness contrast between carbonated and non-carbonated regions compared with grayscale conversion.
2. **Two-stage (Primary + Secondary) hybrid detection pipeline**:
   - **Primary detection**: Otsu optimal-threshold binarization $\rightarrow$ complementary-image inversion $\rightarrow$ hole filling within the non-carbonated region $\rightarrow$ removal of residual noise at the outer boundary.
   - **Secondary detection**: exploiting the physical characteristic that concrete carbonation propagates from the outer surface toward the core (the non-carbonated core forms a convex polygon), the **Convex Hull** of the non-carbonated region is computed with the QuickHull algorithm to eliminate interior false-positive objects entirely.
3. **Complete exclusion of aggregate color interference and subjective reading errors**:
   - Even when gray-toned aggregates resembling the cement paste are embedded inside the non-carbonated region, they are automatically adjudicated as interior to the convex hull, blocking at the source the error of misclassifying them as carbonated regions.
   - A precise carbonation-depth profile at 0.1 mm resolution can be acquired rapidly without any inter-operator deviation.

## Methods

- **Image acquisition and preprocessing**:
  - Digital color photographs (RGB images) of fracture or cut concrete surfaces sprayed with a 1 % ethanol phenolphthalein solution.
  - Scale calibration of the unit pixel length (mm/pixel).
  - Extraction of the Green Intensity plane from the RGB channels: $I_G(x,y)$.
- **Primary detection algorithm (binarization & morphology)**:
  1. Automatic determination of the optimal threshold $T_{opt}$ by Otsu's variance-maximization algorithm, followed by binarization.
  2. Conversion to the complementary image, then morphological erosion/dilation and hole filling (flood-fill based).
  3. Removal of white-noise pixels outside the boundary.
- **Secondary detection algorithm (convex hull geometry)**:
  1. Extraction of the boundary coordinates of the primary-detected non-carbonated region.
  2. Generation of the minimum circumscribed convex polygon (Convex Hull Polygon) $H(P)$ by applying the QuickHull algorithm.
  3. Forced conversion of black pixels (regions falsely detected as carbonated) lying inside the polygon ($\text{Point-in-Polygon}$) into non-carbonated pixels.
  4. Final composite overlay of the carbonation boundary line and depth evaluation.
- **Validation database**:
  - Comparative verification against visual reading on four sets of concrete cross-sectional images taken from the literature and field-extracted cores (various aggregate sizes, rough fracture surfaces, corner carbonation, etc.).

## Results

### 1. Stage-by-stage detection accuracy and noise-removal effect

| Processing stage | Image state | Key processing function | Residual false positives |
|---|---|---|---|
| **Input** | Original RGB color | Phenolphthalein magenta sprayed surface | Background and uneven illumination |
| **Preprocessing** | Green channel separation | Contrast maximization via magenta complement | Improved discrimination over grayscale |
| **Primary detection (Otsu)** | Binary black-and-white | Intensity-based first segmentation | 12 false detections of aggregates/voids inside the non-carbonated region |
| **Primary detection (hole fill)** | Morphological correction | Merging isolated regions inside the non-carbonated core | Residual noise remains near the boundary |
| **Secondary detection (convex hull)** | **Geometric convex hull** | **100 % removal of falsely detected aggregates inside the core** | **False positives completely eliminated (clean boundary)** |
| **Final output** | Composite overlay synthesis | Continuous carbonation-depth profile extraction | **Perfect agreement with the manual inspection line** |

- **Aggregate influence**: aggregates inside the non-carbonated region were perfectly corrected to non-carbonated, but paste-colored aggregates straddling the carbonation boundary can produce minor errors, suggesting room to supplement an aggregate-boundary detection filter.
- **Practicality**: even on complex fracture surfaces, precise carbonation depth and area are quantified within seconds, dramatically improving the reliability of structural diagnosis.

## Related Notes

- [[da-2009-concrete-carbonation-test-variation-sources]] — Error factors in concrete carbonation testing and standardization strategies.
- [[djp1612-aas-carbonation]] — Carbonation resistance and depth measurement of alkali-activated slag mortar.
- [[song-2012-aas-carbonation-characteristics]] — Carbonation mechanism of AAS materials.
- [[ndt-and-shm-of-cementitious]] — Nondestructive testing and digital-image-based structural diagnosis concepts.
