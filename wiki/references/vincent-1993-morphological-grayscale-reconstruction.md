---
title: "Morphological Grayscale Reconstruction in Image Analysis: Applications and Efficient Algorithms (Vincent, 1993)"
type: reference_book
source: "sources/vincent-1993-morphological-grayscale-reconstruction-in-image.pdf"
citation: "Vincent, L. (1993). Morphological grayscale reconstruction in image analysis: Applications and efficient algorithms. IEEE Transactions on Image Processing, 2(2), 176-201. https://doi.org/10.1109/83.217222"
date: 2026-08-24
tags:
  - image-processing
  - mathematical-morphology
  - grayscale-reconstruction
  - crack-detection
  - algorithm
---

## Summary
A landmark origin paper of the computer vision field that systematized the fast FIFO queue-based algorithm for grayscale morphological reconstruction (reconstruction by dilation/erosion), a core technique of mathematical morphology in digital image processing and pattern recognition, together with its fields of application. It proposed a pioneering algorithm that converges the infinitely iterated dilation operation (geodesic dilation), computed between a marker image and a mask image, within only one or two sequential scans. It is widely cited as the core image-processing principle behind digital image detection of microcracks in cementitious composites, pore segmentation, and fiber orientation-angle filtering.

## Key Contributions
- **Development of a fast queue-based morphological reconstruction algorithm**: reduces the conventional iterative operation ($O(N^2)$) to linear time complexity ($O(N)$), making real-time segmentation of large, high-resolution images feasible.
- **Establishment of regional extrema (h-maxima/h-minima) and dome extraction techniques**: enables precise extraction of microcrack and pore boundaries without distortion amid nonuniform illumination and noise on concrete surfaces.
- **Provision of an over-segmentation prevention technique for watershed segmentation**: the marker-based watershed transformation maximizes the identification of even complex cement microstructure particles.

## Related Notes
- [[lee-2010-fluorescence-discriminating-fibers-hybrid-ecc]] - quantitative evaluation of fiber dispersion using digital image processing
- [[ndt-and-shm-of-cementitious]] - image-based nondestructive diagnosis of concrete surface cracks
