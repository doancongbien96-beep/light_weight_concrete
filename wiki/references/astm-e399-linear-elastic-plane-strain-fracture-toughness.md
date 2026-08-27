---
title: "ASTM E399-17 Standard Test Method for Linear-Elastic Plane-Strain Fracture Toughness (KIc) of Metallic Materials"
type: reference_book
source: "sources/e08-test-method-for-linear-elastic-plane-strain.pdf"
citation: "ASTM International. (2017). ASTM E399-17: Standard Test Method for Linear-Elastic Plane-Strain Fracture Toughness (KIc) of Metallic Materials. West Conshohocken, PA: ASTM International."
date: 2026-08-24
tags:
  - fracture-toughness
  - standard-test-method
  - linear-elastic-fracture-mechanics
  - k1c
---

## Summary
ASTM E399 is the representative standard test method for measuring the linear-elastic plane-strain fracture toughness ($K_{Ic}$) of metals and homogeneous brittle materials. A quasi-static tensile or bending load is applied to a notched specimen into which a fatigue precrack has been introduced; $P_Q$ and the conditional fracture toughness ($K_Q$) are evaluated from the load-displacement curve, and a valid $K_{Ic}$ is determined by verifying that the specimen thickness, crack length, and ligament width satisfy plane-strain conditions sufficient relative to the plastic zone size ($B, a \ge 2.5 (K_Q / \sigma_{ys})^2$). It is widely referenced as the foundational standard principle for fracture-mechanics measurement of the matrix fracture toughness ($K_m$) of cement-based composites and high-performance cement composites (ECC/HPFRCC), and for micromechanical energy-balance design ($J_{tip} \le J_b'$).

## Key Contributions
- **Establishment of the criterion for linear-elastic plane-strain fracture toughness**: establishes the evaluation procedure for a purely elastic fracture property through the size validity condition ($B \ge 2.5 (K_Q / \sigma_{ys})^2$) that strictly limits the influence of the crack-tip plastic zone.
- **Provisions for various standard specimen geometries**: provides stress intensity factor ($K$) geometry functions for a variety of specimen geometries, including compact tension (Compact Tension, C(T)), single-edge notch bend (Single-Edge Bend, SE(B)), arc-shaped (Arc-shaped, A(T)), and disk-shaped compact (Disk-shaped, DC(T)).
- **Determination of $P_Q$ based on the 5 % secant method**: verifies the small-scale yielding condition through the intersection ($P_5$) with a line of slope 95 % of the initial linear slope of the load-displacement curve and the ratio of this value to the maximum load ($P_{max}/P_Q \le 1.10$).

## Methods
- **Specimen types**: SE(B) three-point bend specimen, C(T) compact tension specimen.
- **Fatigue precracking**: a sharp natural crack is introduced at the tip of the machined notch by controlling the load amplitude ($a/W = 0.45 \sim 0.55$).
- **Instrumentation system**: crack opening displacement (COD, Crack Opening Displacement) gauge mounted; displacement-controlled quasi-static loading.
- **Validity equations**:
  $$K_Q = \frac{P_Q S}{B W^{3/2}} f(a/W)$$
  $$B, a, (W-a) \ge 2.5 \left( \frac{K_Q}{\sigma_{ys}} \right)^2$$

## Results
- When the plane-strain condition is strictly satisfied, the material's intrinsic minimum-resistance fracture toughness $K_{Ic}$ is secured.
- For fiber-reinforced cement composites with large plastic deformation or fiber bridging zones, direct application of a single $K_{Ic}$ value has limitations; the standard provides the theoretical foundation for extended application via $J$-integral or R-curve techniques.

## Related Notes
- [[pseudo-strain-hardening-criteria]] - matrix fracture toughness and the steady-state crack initiation energy condition
- [[strain-hardening-mechanism]] - analysis of the strength/energy criteria linking matrix fracture toughness and fiber bridging fracture energy
