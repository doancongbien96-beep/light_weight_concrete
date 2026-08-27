---
title: "Crack Pattern Recognition in Concrete Surface Using Artificial Neural Networks (Lee et al., 2006)"
type: source_note
source: "sources/DJP0205N_콘크리트 표면.pdf"
citation: "Lee, B. Y., Kim, Y. Y., & Kim, J. K. (2006). Development of crack pattern recognition system on concrete surface using artificial neural network. Journal of the Korea Concrete Institute, 18(2), 245-252. https://doi.org/10.4334/JKCI.2006.18.2.245"
date: 2026-08-24
tags:
  - artificial-neural-networks
  - pattern-recognition
  - crack-type-classification
  - image-processing
  - structural-health-monitoring
  - non-destructive-testing
---

## Summary
This pioneering artificial-intelligence civil engineering paper by Professors Bang Yeon Lee, Yun Yong Kim, and Jin Keun Kim developed and validated an intelligent pattern recognition system that analyzes the morphological geometric patterns of cracks from surface digital images of reinforced concrete structures and automatically classifies and diagnoses the cause of cracking (flexural crack, shear crack, drying shrinkage crack, torsional crack, settlement crack) using a multilayer perceptron (MLP) artificial neural network (ANN) algorithm. With crack shape feature vectors extracted by morphological image processing (invariant moments Hu-moments, fractal dimension, principal direction angle, aspect ratio) as input, it demonstrated automatic diagnosis of the five major structural crack types with high accuracy of **94.8 %**.

## Key Contributions
- **Establishment of an ANN architecture for automatic determination of concrete crack causes**: construction of a two-hidden-layer multilayer perceptron based on backpropagation learning.
- **Design of a scale- and rotation-invariant crack feature extractor**: introduction of Hu's seven invariant moments and the crack fractal dimension ($D_f$), enabling classification regardless of shooting angle/distance.
- **Achievement of 94.8 % classification accuracy for the five major crack causes**: precise separation of flexure (single vertical direction), shear (inclined $45°$), drying shrinkage (map-like polygons), and settlement (following the reinforcing mesh).
- **Establishment of the foundation for automated intelligent structural health assessment and defect diagnosis**: elimination of subjective misjudgment by maintenance engineers.

## Methods
- Image processing: surface image binarization $\rightarrow$ noise filtering $\rightarrow$ crack centerline extraction and contour vectorization.
- Feature vector: 10-dimensional input vector (principal angle $\theta$, fractal dimension $D_f$, Hu moments $\phi_1 \sim \phi_7$, density index).
- Network structure: input layer (10) - hidden layer 1 (20) - hidden layer 2 (15) - output layer (5), learning rate 0.05, momentum 0.9.
- Training and test: a dataset of 500 real structure and laboratory crack pattern images.

## Results
Summary of the neural network crack-type classification results and confusion matrix:

| Crack type | Principal geometric features | Number of training data | Test accuracy (%) | Misclassification tendency |
| :--- | :--- | :---: | :---: | :--- |
| Flexural crack (Flexure) | Linear lines parallel perpendicular to the member axis | 100 | **96.5 %** | Slightly confused with shear under minor inclination |
| Shear crack (Shear) | Diagonal orientation of $30° \sim 60°$ | 100 | **95.0 %** | Combined flexure-shear zone |
| Drying shrinkage crack (Shrinkage) | Two-dimensional isotropic map cracking | 100 | **98.0 %** | Perfectly classified |
| Settlement crack (Settlement) | Longitudinal lines along the main reinforcement layout | 100 | **92.5 %** | Partially confused with flexural cracks |
| Torsional crack (Torsion) | Spiral helical pattern | 100 | **92.0 %** | Partially confused with shear cracks |

## Related Notes
- [[lee-2007-surface-crack-evaluation]] - Evaluation of concrete cracks through image processing
- [[kim-2008-fiber-classification-djp0608]] - Image-based classification of fiber dispersion
- [[ndt-and-shm-of-cementitious]] - Smart non-destructive structural health diagnostics
