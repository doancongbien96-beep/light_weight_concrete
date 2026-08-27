---
title: "New Technique for Reinforcement of Concrete Columns Confined by Embedded Composite Grid (Bentayeb, Ait Tahar & Chateauneuf, 2008)"
type: source_note
source: "sources/bentayeb-2008-new-technique-for-reinforcement-of.pdf"
citation: "Bentayeb, F., Ait Tahar, K., Chateauneuf, A. New technique for reinforcement of concrete columns confined by embedded composite grid. Construction and Building Materials 22 (2008) 1624-1633. DOI 10.1016/j.conbuildmat.2007.06.015."
date: 2026-08-23
tags: [frp-grid, confinement, embedded-composite-grid, e-glass, rc-column, strain-hardening-concrete, finite-element]
---

# New technique for reinforcing concrete columns confined by embedded composite grid

## Summary

A joint effort of LaMoMS (University of Tizi Ouzou, Algeria) and LGC (Blaise Pascal
University, France) validating — experimentally, theoretically, and by finite elements — a
novel confinement technique that embeds an E-glass composite grid inside the concrete section
rather than bonding an FRP jacket externally. Embedding eliminates surface preparation and
adhesive-interface premature failure outright, preserves concrete continuity, and leaves the
appearance untouched. Compression tests on cylinders showed a mean strength gain of about
20 % (30.03 to 36.48 MPa) and a shift to non-brittle failure; the authors propose their own
confinement model introducing grid shape factors u1 and u2 into Wu's external-confinement model.

## Key Contributions

- Quantified proof of the embedded-confinement concept: with confinement ratio
  (fl/f'co)= 0.19 the mix sits in the strain-hardening domain above the softening/hardening
  threshold of 0.10. Confined strengths of 37.86/34.80/36.79 MPa against unconfined
  32.38/31.69/26.04 MPa per batch; mean 30.03 to 36.48 MPa (+21.5 %).
- Interface problems eliminated: concrete penetrates the grid apertures creating mechanical
  interlock without prestress, and the physical interface survives failure. The cover spalls
  during compression but the confined core keeps resisting — presented as a safety concept in
  which cover loss acts as pre-collapse warning.
- Grid-specific confinement model proposed: confinement density ρf derived in closed form from
  grid geometry (bf= 3 mm, sf= 20 mm, tf= 1 mm, opening ratio Av/Ab); generalized as ultimate
  strength f'cu= f'co(0.75 + 2.5 u1u2ff/f'co) in ultimate-strength and ultimate-strain forms.
  Wu-model predictions f'cp= 37.11, f'cu= 37.39 MPa versus experimental 36.48 MPa — error within
  2.5 %.
- Calibration link with over 400 literature cylinders (F'co 23–70 MPa, FRP tensile strength
  300–4000 MPa): provides a k-coefficient comparison framework against Richart-type
  f'cc= f'co+ kfl models (Fardis, Saafi, Miyauchi, Lam-Teng, Toutanji, Karabinis-Rousakis).
- Economics: for a 300 mm × 4 m column, grid + minimal rebar (6 mm @ 300 mm) costs 6.9 EUR
  versus 7.5 EUR for conventional stirrups (8 mm @ 200 mm) — superior on material cost alone,
  before constructability and schedule gains.
- ANSYS axisymmetric analysis, 8-node, 4800 elements: confinement cuts lateral displacement
  by 17 % (7.9 to 6.6 ×10^-3 mm) and homogenizes stress flow within the confined core.

## Methods

- Specimens: eighteen 160 mm × 320 mm cylinders (3 batches × 3 confined + 3 unconfined).
  Eurocode 2 mix (Portland cement, gravel, natural sand, superplasticizer), NFP18-406
  compression testing, 3000 kN universal machine at 0.5 kN/s, sulfur capping to remove
  eccentricity, 28-day lime-saturated-water curing.
- Grid: resin-impregnated E-glass fiber, alternating meshes 20 × 30 mm and 20 × 25 mm, yield
  strength 560 MPa, modulus 4.1 GPa (manufacturer values). Embedded before casting around
  rebars and stirrups.
- Model: Wu's (2002) confinement index k1= ρf Ef sqrt(f'co)/f'co = 0.26 indicating the
  hardening regime; peak-strength and -strain equations (5a)(5b) alongside the proposed
  equations (14a)(14b). FE compared radial displacement and vertical stress distributions at
  0.1 mm top-platen displacement.

## Results

- Failure mode: unconfined specimens failed brittle; grid-confined cylinders deformed axially
  and laterally with the grid trapping crack fragments inside the section — ductile behavior.
  Stress concentration appeared at the bottom of specimens without grid cover.
- Table 1 ultimate loads: mean 604.08 kN unconfined vs 729.94 kN confined. Batches with lower
  unconfined strength gained more (26.04 to 36.79 MPa in batch 3).
- Table 3 model values: fl= 5.95 MPa, ρf= 28.12 ×10^-4, confinement ratio 0.19, e'cp= 0.062,
  e'cu= 0.096.
- Parametrics: peak strength is insensitive to confinement density; ultimate strength rises up
  to 25 % with increasing density in high-strength concrete.
- Limits: dynamic loading, crack-width assessment, and reliability-based design factors left
  as follow-up tasks.

## Related Notes

- [[bencardino-2006-frp-strengthened-rc-beams-holistic]] — holistic design of externally bonded
  FRP strengthening (external versus embedded contrast axis)
- [[su-2024-flexural-behavior-beams-gfrp-hpfrcc-strengthening]] — GFRP+HPFRCC strengthened members
- [[kim-2014-shcc-hsrs-strengthened-rc-beam]] — RC member improvement through SHCC strengthening layers
- [[ahmad-2003-reinforcement-corrosion-in-concrete-structures]] — corrosion deterioration review
  (durability context of embedded metallic reinforcement)
