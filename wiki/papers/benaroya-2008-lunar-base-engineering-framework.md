---
title: "Engineering of lunar bases"
type: source_note
source: "sources/benaroya-2008-engineering-of-lunar-bases.pdf"
citation: "Benaroya, H., & Bernold, L. (2008). Engineering of lunar bases. Acta Astronautica, 62(4-5), 277-299."
date: 2026-08-24
tags: [lunar-bases, space-structures, radiation-shielding, inflatable-habitats, structural-mechanics, whipple-shield, robotic-construction, acta-astronautica, rutgers-university, theory-foundation]
---

# Structural engineering framework of a permanent crewed lunar base: environmental loads, 2.5 m regolith radiation shielding, nonlinear pressurized-shell analysis, and robotic erection process

## Summary

To complete the engineering and structural technology framework for humanity's return to
the Moon after the Apollo program and for building Lunar Permanent Settlements, Prof.
Haym Benaroya of Rutgers University and Prof. Leonhard Bernold of North Carolina State
University led a joint research team whose Acta Astronautica landmark review consolidated
decades of accumulated space structural-mechanics research, quantitatively analyzed the
Moon's harsh surface environment — **lethal solar particle events (SPE) reaching up to
10 Sv over an 11-year solar cycle and galactic cosmic rays (GCR) at 0.3 Sv per year,
steel out-gassing under ultra-high vacuum ($10^{-12}\ \text{Torr}$), cryogenic brittle
fracture at $-180\ ^\circ\text{C}$, hypervelocity micrometeorite impacts at
$10\sim 70\ \text{km/s}$, and severe thermal fatigue over the 28-day cycle** — and
systematically established **nonlinear finite-element analysis of pressurized shells
supporting crewed habitat modules at internal pressure ($101.3\ \text{kPa}$), optimal
regolith shielding-layer design at $2.5\ \text{m}$ for complete blocking of primary and
secondary radiation, dual Whipple bumper meteorite barriers, and remote autonomous
robotic construction processes** — a top-rank landmark review paper of space structural
engineering published in Acta Astronautica. The authors demonstrated that a $2.5\ \text{m}$
regolith layer is the optimum limiting thickness that suppresses radiation dose below the
occupational annual limit of **$0.05\ \text{Sv}$ ($5\ \text{rem}$)** while minimizing
secondary neutron and Bremsstrahlung production, and completed the structural analysis and
risk-based safety-factor framework of semihard domes and inflatable membrane modules.

## Key Contributions

1. **Precise determination of the optimal $2.5\ \text{m}$ regolith shield thickness for
   controlling lunar-surface radiation exposure**: a critical design thickness of
   $2.5\ \text{m}$ established that attenuates the lethal unshielded dose of 0.3 Sv per
   year (10 Sv during solar flares) to below 0.05 Sv annually while preventing the
   secondary-radiation amplification that occurs at excessive thicknesses.
2. **Structural mechanics of semihard domes and membrane shells supporting internal
   pressure of $101.3\ \text{kPa}$**: interaction between circumferential tensile stress
   ($\sigma_\theta = P R / t$) carried by shell structures under vacuum and the self-weight
   load of overlying regolith analyzed via large-deformation geometrically nonlinear FEA.
3. **Design relations for multilayer Whipple shields against hypervelocity micrometeorites**:
   impact-absorption mechanism quantified in which the outer sacrificial bumper vaporizes
   and fragments the hypervelocity impactor while fully protecting the inner pressure wall.
4. **Standardization of robotic autonomous excavation, stockpiling, and module-interconnection
   processes for lunar-base infrastructure**: a staged construction scenario completed in
   which unmanned rovers accomplish excavation, module placement, and regolith covering
   while excluding hazardous astronaut EVA (extravehicular activity).

## Methods

- **Lunar extreme-environment load database (Section 2 & Table 1)**:
  - Pressure and thermal: $P_{in} = 101.3\ \text{kPa}$, external vacuum
    $10^{-12}\ \text{Torr}$, day $+120\ ^\circ\text{C}$ / night $-180\ ^\circ\text{C}$
    ($\Delta T = 300\ ^\circ\text{C}$).
  - Radiation flux: galactic cosmic rays (GCR protons $85\%$, helium $14\%$, heavy ions
    $1\%$); solar flares (SPE up to $10\ \text{Sv}$).
  - Micrometeorites: velocity $10\sim 70\ \text{km/s}$, mass $10^{-12}\sim 1\ \text{g}$
    (cumulative flux $F(m) = 10^{-14.5} m^{-1.2}$).
- **Structural analysis and conceptual design (Sections 3~5)**:
  - Shell structures: hemispherical domes, cylinders, inflatable tori (Al 2219 alloy,
    composite membranes).
  - Shielding mass attenuation model: $I = I_0 \exp(-\mu \rho x)$ coupled with the HZETRN
    space-radiation transport code.
  - Soil-foundation system: nonlinear foundation moduli of lunar regolith
    ($E = 10\sim 30\ \text{MPa}$, friction angle $\phi = 35^\circ\sim 45^\circ$).

## Results

### 1. Comprehensive comparison table of lunar-base load conditions, structural performance requirements, and shielding criteria (Table 1~4 & Fig. 1~8)

| Environmental/load element | Characteristic value vs terrestrial conditions | Structural design implication | Engineering response | Mandatory design criterion |
|---|---|---|---|---|
| **Internal pressurization load** | external ambient 0 kPa (1 atm differential) | pure tension dominates shell walls | high-tensile alloys and membrane ring anchors | **pressurization support at $P_{in} = 101.3\ \text{kPa}$** |
| **Galactic cosmic rays/solar flares** | no magnetosphere (0.3~10 Sv per year) | human carcinogenesis and electronics failure | **$2.5\ \text{m}$ lunar regolith cover layer** | **annual dose $\le 0.05\ \text{Sv}$** |
| **Severe temperature cycling** | $-180\sim +120\ ^\circ\text{C}$ over the 28-day cycle | thermal stress and cryogenic brittle fracture | multilayer insulation (MLI) + thermostatic regolith covering | interior held at constant $+20\pm 2\ ^\circ\text{C}$ |
| **Hypervelocity micrometeorite impact** | impactors at $10\sim 70\ \text{km/s}$ | shell perforation and explosive decompression | dual Whipple bumper (Whipple Shield) | $1.0\ \text{cm}$ aluminum bumper at $10\ \text{cm}$ standoff |
| **Lunar low gravity ($1/6 g$)** | 16.6 % of Earth gravity ($1.62\ \text{m/s}^2$) | sharp loss of bearing capacity; buoyancy dominance | deep foundation anchors and regolith ballast | settlement controlled to $\le 5.0\ \text{mm}$ |

### 2. Structural-mechanics and shielding-physics interpretation

- **Secondary-radiation defense optimization**: below 1.0 m of regolith thickness,
  high-energy protons penetrate through and remain dangerous; beyond 4.0 m, collisions
  with atomic nuclei inside the regolith over-produce secondary neutrons and gamma rays —
  **$2.5\ \text{m}$ is identified as the optimal Goldilocks thickness minimizing total
  dose**.
- **Material behavior under ultra-high vacuum**: special ceramic coatings and dry-lubricant
  standards established to prevent 'cold welding', which arises when metallic surface oxide
  films disappear under vacuum, and embrittlement from evaporation of volatile substances.

- **Overall conclusion**: this paper is a top-level landmark review of space structural
  engineering that organically integrates environmental loads, radiation-shielding physics,
  nonlinear structural-mechanics analysis, and robotic construction methods toward the safe
  design of permanent lunar bases.

## Related Notes

- [[benaroya-2002-engineering-design-construction-lunar-bases]] — Prof. Benaroya's primary
  origin paper on lunar base design and construction.
- [[dyke-2024-standards-lunar-isru-materials]] — origin paper on test standards for lunar
  ISRU structural materials and landing-pad design.
- [[he-2025-lunar-base-insitu-functional-materials]] — origin paper on lunar regolith basalt
  fiber and ISRU materials.
- [[high-strength-strain-hardening-composites]] — high-strength composite design framework
  for extreme space environments.
