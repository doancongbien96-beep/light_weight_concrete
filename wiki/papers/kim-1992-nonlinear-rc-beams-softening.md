---
title: "Nonlinear Analysis of Reinforced Beams with Softening Concrete (Kim & Lee, 1992)"
type: source_note
source: "sources/1-s2.0-004579499290389H-main.pdf"
citation: "Kim, J.-K., Lee, T.-G. Nonlinear analysis of reinforced beams with softening concrete. Computers & Structures 44(3) (1992) 567-573."
date: 2026-08-22
tags: [rc-beam, strain-softening, nonlinear-fem, moment-curvature, plastic-hinge, displacement-control]
---

# Nonlinear Analysis of Reinforced Beams with Softening Concrete

## Summary

This study supplements the limitations of limit analysis by incorporating the sectional strain-softening regime of concrete in the flexural collapse analysis of reinforced concrete (RC) beams. A displacement-control-based finite element analysis is established to trace the full load-deflection response of RC beams up to failure. The primary contribution is resolving the mesh-size dependency of moment-curvature relationships using the concept of concentrated inelastic rotation within plastic hinges. From the perspective of the ECC wiki, this paper serves as an early practical reference addressing mesh objectivity in strain-softening structural analysis, contrasting sharply with the distributed strain-hardening behavior of ECC.

## Key Contributions

1. **Establishment of displacement-control nonlinear FEM procedure**: Enables response tracking through snapback regimes, providing distinct numerical stability over load control in softening branches.
2. **Resolution of mesh objectivity**: Unadjusted moment-curvature relationships lead to spurious mesh sensitivity and divergent post-peak responses. Enforcing an invariant concentrated inelastic rotation over the plastic hinge length ($A_{II} = A'_{II}$, area equivalence) adjusts elemental moment-curvature curves to achieve objective results.
3. **Plastic hinge length formulation**: Adopted the average value between the Corley formula and Sawyer formula.
4. **Sectional constitutive modeling with softening**: Confined compression via recalculation of the Fafitis-Shah model, tension using the Vebo-Ghali model, and cyclic hysteresis via the Otter-Naaman model.

## Methods

- Beam elements based on the modified stiffness approach (cubic polynomial displacement field, linear interpolation of nodal stiffnesses $(EI)_i$ and $(EI)_j$).
- Concrete compression follows an ascending parabolic curve and descending exponential branch; steel is modeled as elastic-perfectly plastic.
- Load-controlled systems of equations are converted into displacement-control form and converged via residual load iterations.

## Results

- The modified model reasonably reproduces experimental load-deflection curves across under-reinforced, balanced, and over-reinforced simply supported and continuous beams.
- In continuous beam analyses, sectional softening tended to be underestimated, leading to minor underpredictions of ultimate capacity and deflection.
- Comparisons before and after moment-curvature modification demonstrated that unadjusted meshes produce divergent responses, whereas the proposed method ensures consistent objectivity.

## Related Notes

- Unlike conventional reinforced concrete exhibiting localized strain-softening, ECC displays multiple microcracking and tensile strain-hardening, alleviating structural mesh-sensitivity issues.

