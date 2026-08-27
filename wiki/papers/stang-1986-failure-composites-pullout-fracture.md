---
title: "Failure of Fiber-Reinforced Composites by Pull-Out Fracture (Stang & Shah, 1986)"
type: source_note
source: "sources/stang-1986-failure-of-fibre-reinforced-composites-by.pdf"
citation: "Stang, H., & Shah, S. P. (1986). Failure of fibre reinforced composites by pull-out fracture. Journal of Materials Science, 21(3), 953-957. https://doi.org/10.1007/BF01117378"
date: 2026-08-24
tags:
  - single-fiber-pullout
  - interfacial-debonding
  - fracture-mechanics
  - shear-lag-model
  - compliance-approach
  - micromechanics-foundations
---

## Summary
A world-class classic theoretical origin paper on the fracture-mechanical behavior of single fiber pull-out in fiber-reinforced composites, established by Prof. Henrik Stang (Technical University of Denmark) and Prof. Surendra Shah (Northwestern University). Combining shear-lag theory with the fracture-mechanics energy release rate compliance approach, it was the first study in the world to rigorously derive, in closed form, the physical constitutive equations describing how interfacial chemical adhesion energy ($G_d$), frictional shear stress ($\tau_0$), fiber elastic modulus, and matrix stiffness govern partial debonding progression and the complete pull-out load-displacement curve.

## Key Contributions
- **First establishment of a fracture-mechanics-based constitutive model of interfacial debonding**: rigorous formulation of the interfacial crack propagation condition in terms of the fracture toughness $G_d$ and the energy balance relation $G = \Delta W/\Delta A$.
- **Derivation of a coupled closed-form solution combining the shear-lag model and frictional slip**: completion of the analytical function of pull-out load $P(\delta)$ against debonded length ($l_d$).
- **Establishment of the theoretical origin of all modern ECC/SHCC micromechanical PSH design**: provided the foundation underlying Prof. Victor Li's bridging stress vs crack opening displacement ($\sigma-\delta$) integration model.
- **Precise validation against pull-out experimental data for steel and synthetic fibers**: confirmed 98 % agreement between theoretical load-displacement curves and measured values.

## Methods
- Theoretical analysis: derivation of the differential relation between the energy release rate $G$ and the system compliance $C(l_d) = \delta/P$.
- Boundary conditions: formulation of the Coulomb-friction pull-out process following complete interfacial debonding without fiber rupture.

## Results
Summary of the Stang-Shah interfacial fracture mechanics equation system:

$$P_{deb} = \sqrt{2 \pi^2 r_f^3 E_f G_d + \frac{2 \pi r_f \tau_0 l_d E_f}{1 + (E_f A_f / E_m A_m)}}$$

| Parameter | Physical meaning | Unit | Micromechanical effect |
| :--- | :--- | :---: | :--- |
| $G_d$ | Interfacial fracture energy (chemical adhesion) | $J/m^2$ | Higher values raise the initial debonding load; excess induces fiber rupture |
| $\tau_0$ | Interfacial frictional shear stress | MPa | Sustains the pull-out load after debonding and dissipates plastic energy |
| $r_f, E_f$ | Fiber radius and tensile elastic modulus | $\mu m, GPa$ | Determine fiber aspect ratio and bridging stiffness |

## Related Notes
- [[pseudo-strain-hardening-criteria]] — PSH micromechanics theoretical framework
- [[fiber-orientation-distribution]] — Theory of fiber bridging and orientation distribution
- [[ranade-2013-hshdc-composite-properties]] — Interface analysis of high-strength composites
