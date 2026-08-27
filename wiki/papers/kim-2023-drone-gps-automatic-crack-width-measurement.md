---
title: "Enhanced Crack Width Measurement Using GPS Metadata of Drone Imagery (Kim et al., 2023)"
type: source_note
source: "sources/드론 촬영의 GPS 좌표 정보만을 활용한 자동 균열폭 측정 방법.pdf"
citation: "Kim, T., Seol, D., Kim, G., & Kim, H. (2023). Enhanced crack width measurement using GPS metadata of drone imagery. Journal of the Architectural Institute of Korea, 39(11), 243-250. https://doi.org/10.5659/JAIK.2023.39.11.243"
date: 2026-08-24
tags:
  - drone-imagery
  - gps-metadata
  - crack-width-measurement
  - image-processing
  - structural-health-monitoring
---

# Enhanced Crack Width Measurement Using GPS Metadata of Drone Imagery

## Summary

To facilitate safety inspection on inaccessible high-rise buildings and large concrete structures without artificial reference markers or laser distance meters, this study develops an automated crack width measurement framework using GPS coordinate metadata (latitude, longitude, altitude) embedded in drone images alongside pinhole camera optics. By calculating the physical scale factor (mm/pixel) directly from optical distance geometry, the algorithm quantifies crack widths automatically. Field experiments on building facades demonstrated an average absolute error of 0.05 mm (over 90 % accuracy) compared to optical crack microscope readings, reliably identifying structural cracks exceeding $0.2\ \text{mm}$ ($0.2 mm$).

## Key Contributions

- **Automated shooting distance estimation via GPS metadata**: Derived Euclidean distances between the drone RTK-GPS positions and 3D building coordinates (3D) to compute physical scale factors.
- **Automated image processing pipeline for crack centerline and orthogonal width extraction**: Integrated adaptive binarization, morphological thinning, and normal vector profiling.
- **Enhanced inspection accessibility and efficiency**: Enabled quantitative facade crack assessments using standard drone flight photographs without physical marker installation.

## Methods

- High-resolution RGB images captured via DJI drones (4K resolution, EXIF metadata extraction).
- Computer vision algorithms: Gaussian filtering, Otsu thresholding, morphological skeletonization, and normal profile width evaluation.
- Accuracy validation against optical crack microscope measurements.

## Results

- Crack width measurement achieved a mean absolute error (MAE) of $0.048\ \text{mm}$ ($0.048 mm$) and a coefficient of determination $R^2 = 0.94$.
- Automatically detected cracks exceeding the $0.2\ \text{mm}$ ($0.2 mm$) maintenance guideline threshold with over 95 % reliability.

## Related Notes

- [[ndt-and-shm-of-cementitious]] — Non-destructive testing and structural health monitoring of cementitious systems.
- [[crack-width-control]] — Crack width control and durability standards in concrete structures.
