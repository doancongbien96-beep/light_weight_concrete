---
title: "Experimental Evaluation of Fiber Reinforced Concrete Fracture Properties (Bencardino, Rizzuti, Spadea & Swamy, 2010)"
type: source_note
source: "sources/bencardino-2010-experimental-evaluation-of-fiber-reinforced.pdf"
citation: "Bencardino, F., Rizzuti, L., Spadea, G., Swamy, R.N. Experimental evaluation of fiber reinforced concrete fracture properties. Composites: Part B 41 (2010) 17-24. doi: 10.1016/j.compositesb.2009.09.002"
date: 2026-08-22
tags: [frc, fracture-properties, fracture-energy, steel-fiber, polypropylene-fiber, rilem-tc162]
---

# Experimental evaluation of FRC fracture properties (steel fiber versus polypropylene fiber)

## Summary

A joint study by the University of Calabria and the University of Sheffield (Swamy)
quantitatively comparing compressive, flexural, and fracture-energy behavior of FRC with
high-modulus steel fibers (SFRC) and low-modulus polypropylene microfibers (PFRC) at volume
fractions of 1 % and 2 %. On an 80 MPa-design-strength matrix (w/c 0.35, silica fume 5 %),
150 mm cube compression tests and notched-prism three-point flexure (RILEM TC 162-TDF) were
performed; fracture energy was computed under two bases — full-area (RILEM TC 50-FMC,
criterion I) and integration of the stress-displacement curve to a 3 mm limit (criterion II) —
and compared. First, steel fiber barely changes compressive strength while raising peak
flexural load roughly 2x at 1 % and 3x at 2 % over plain concrete, retaining 73–93 % of peak
load even at 3 mm deflection. Second, PP fibers cut compressive strength by 25–35 % yet achieve
extensibility on the load-displacement curve equivalent to steel. Third, the fracture-energy
number itself cannot serve as a measure of crack-control effectiveness, and a steel+PP hybrid
combination is proposed as reasonable from a service-life perspective.

## Key Contributions

- **Fiber modulus quantified as the governing factor of fracture characteristics**: for steel
  fiber (E 210 GPa), equivalent flexural strengths feq,2 and feq,3 exceed the proportional-
  limit strength ffct,L by 1.7–2.2x; with PP (E 3.5 GPa) this inverts, feq falling below half
  of ffct,L. The paper maps the equivalent-strength equations (Eqs. 2, 3) to ultimate-limit-state
  checks and the proportional-limit equation (Eq. 1) to serviceability verification.
- **SFRC residual-load mechanism**: residual load at 3 mm deflection was 73 % (Vf 1 %) and
  93 % (Vf 2 %) of peak, interpreted through the long embedment length of hooked fibers
  providing high pullout resistance across large crack openings.
- **Applicability verdict on fracture-energy bases for FRC**: criterion I (GF 5.2–6.8 N/mm,
  SFRC) yields only 1/5–1/6 of criterion II (31.2–41.1 N/mm); criterion I suits PC while
  criterion II is more reasonable for FRC.
- **Interpretive limit of GF numbers flagged**: since GF combines load with displacement, high-
  modulus fibers always score larger GF numerically — not a difference in crack-control effect.
  Low-modulus fibers resist internal restraint stresses from temperature and drying shrinkage,
  motivating combining both fiber types.

## Methods

- Mix (per m³): cement 500 kg, quartz sand 406 kg (0/2 mm) + 294 kg (3/6 mm), coarse aggregate
  max 15 mm, silica fume sf/c 5 %, superplasticizer sp/c 1.5 %, w/c 0.35 (water 175 l). In
  fiber mixes, 0/5 mm aggregate was removed by the weight of fibers to keep fines ratio.
- Fibers: Dramix hooked steel (tensile strength 1050 MPa, E 210 GPa, length 50 mm, aspect
  ratio 80); PP microfiber (length 19 mm, E 3500 MPa).
- Specimens: 150 mm cubes (compression) and 150×150×600 mm prisms (central diamond-blade notch
  depth 25 mm, span 500 mm). Per group: 3 compression + 3 flexure (DS2%, MP1%, MP2% with 2).
- Testing at 28 days: compression UNI EN 12390-3 (Zwick/Roell 3000 kN); flexure RILEM TC
  162-TDF (INSTRON 1195, 0.05 mm/min, 100 kN load cell). Instrumentation: two WA20 LVDTs under
  the loading point, two WI10 LVDTs for CTOD at the notch tip, a TML full-bridge transducer for
  CMOD, HBM Spider 8 acquisition.

## Results

| Mix | Vf (%) | Compressive strength (MPa) | Peak flexural load (kN) | ffct,L (MPa) | feq,2 (MPa) | fR,4 (MPa) | GF, criterion I (N/mm) | GF, criterion II (N/mm) |
|---|---|---|---|---|---|---|---|---|
| PC | 0 | 80.1 | 17.8 | - | - | - | - | - |
| DS1% (steel) | 1 | 80.5 | 39.0 | 6.6 | 11.5 | 8.7 | 5.2 | 31.2 |
| DS2% (steel) | 2 | 78.2 | 47.8 | 6.5 | 14.0 | 12.9 | 6.8 | 41.1 |
| MP1% (PP) | 1 | 59.2 | 16.5 | 5.0 | 2.2 | 1.8 | 1.1 | 6.7 |
| MP2% (PP) | 2 | 51.2 | 11.3 | 3.2 | 2.8 | 2.2 | 1.2 | 7.4 |

- PFRC compressive strength loss stems from low fiber modulus and poor dispersion at high
  volume: down to 75 % of PC at 1 % and 65 % at 2 %.
- PP-fiber beams dropped load sharply just after peak (loss of 67 % at 1 %, 40 % at 2 %) then
  held a constant residual; at 2 % the peak flexural load itself ran ~40 % below PC.
- Fracture-energy gain from 1→2 % fiber was ~30 % for SFRC versus ~10 % for PFRC. Post-fracture,
  PC split into two pieces while all FRC kept a pseudo-cracked state bridged by fibers; aggregate
  counting on fracture faces showed no fiber segregation.

## Related Notes

- [[banthia-2007-toughness-enhancement-in-steel-fiber]] : experimental predecessor in the
  fiber-driven toughness lineage
- [[aveston-1973-theory-of-multiple-fracture]] : classic multiple-cracking energy theory,
  contrasted with this paper's multiple-crack observations
- [[pseudo-strain-hardening-criteria]] : concept page defining the design boundary between
  softening FRC and hardening SHCC
- [[fiber-bridging-constitutive-law]] : constitutive axis linking crack bridging to fracture
  energy and residual strength
- [[wu-2022-matrix-fracture-energy-interfacial-ecc]] : matrix fracture energy versus interface
  properties, the materials background of GF determination
- [[lawler-2003-hybrid-fiber-fracture-processes-sscv]] : fracture-process experiments directly
  supporting the steel+microfiber hybrid proposal
