---
title: "Modified-Stoichiometric Model for Describing Hydration of Alkali-Activated Slag (Abate, Park, Song, Lee & Kim, 2021)"
type: source_note
source: "sources/'abate-2021-modified-stoichiometric-model-for-describing-hydration.pdf'"
citation: "Abate, S.Y., Park, S., Song, K.-I., Lee, B.-Y., Kim, H.-K. 알칼리 활성 슬래그의 수화에 대한 개선된 화학량론적 모델(Modified-stoichiometric model for describing hydration of alkali-activated slag). 한국건설순환자원학회 논문집(J. Recycled Construction Resources) 9(1):1-12, 2021. DOI 10.14190/JRCR.2021.9.1.1. 조선대(김형기 교신저자)·부경대(박솔뫼)·전남대(송금일·이방연) 공동"
date: 2026-08-23
tags: [aas, hydration-model, stoichiometric-model, thermodynamic-modelling, non-evaporable-water, chemical-shrinkage, porosity, user-group]
---

# Modified stoichiometric model for the hydration of alkali-activated slag (AAS)

## Summary

A user-group paper (co-authored by Bang Yeon Lee of Chonnam National University;
corresponding author Hyeong-Ki Kim of Chosun University). It proposes an improved
stoichiometric model that computes the final hydration product assemblage of
sodium-silicate-activated AAS by linear algebra alone, benchmarked against GEM-Selektor
v3.5 + Cemdata18 thermodynamic equilibrium calculations and OPC results. The core is an
update of the Chen-Brouwers 2007 model with the C-(N-)A-S-H solid-solution data of Myers
et al. 2014. Phase volume compositions matched thermodynamic-model trends within about 20 %,
bound water agreed with experiments within 10 %, but chemical shrinkage deviated by more
than 30 %, so caution is advised per indicator.

## Key Contributions

- Modernization of AAS stoichiometry: portlandite and hydrogarnet are removed from the
  hydrate candidates (realistic C/S and Fe content plus computational simplicity) in favor
  of a unified C-(N-)A-S-H solid solution merging C-S-H gel and C-A-H.
- Constraint introduction: the experimental WDX relationship of Richardson et al. 1994 (a
  linear relation between S/C and A/C) links the unknowns a(C/S) and b(A/S), resolving the
  chemically underdetermined problem; computed a = 1.07–1.19 stays within the solid-
  solution limit of 1.25.
- Interpolation formulas for gel properties: end-member data of five C-(N-)A-S-H and three
  C-S-H types from Myers et al. 2014 are connected through interpolation functions to derive
  bulk bound water H_CNASH and density rho_CNASH (rho = 0.46 H + 2.24 form). M-A-H is treated
  as hydrotalcite-like layered double hydroxide (LDH) fixed at M/A molar ratio 5.
- Verification record: computed infinite-time bound water wne/b of 0.24–0.28 versus 0.24–
  0.26 measured on identical materials and mixes (TG, vacuum drying, EDTA reaction degree;
  Park et al. 2020a) — agreement within 10 %. Porosity agrees within 2 percentage points
  (2 %p) between the two models.
- Quantified limitation: chemical shrinkage is about 14 ml/100 g binder in the thermodynamic
  model (mix-independent) versus 7.5–13.0 ml/100 g stoichiometrically; experiments (Kim et
  al. 2019: 9 ml/100 g at DoH 70 %, final ~13 estimated; Thomas et al. 2012: 13.5–14.5 ml/100 g)
  side with the thermodynamic values, so stoichiometric use on volume-sensitive indicators
  carries a warning of ≥30 % error.
- Auxiliary check of the thermodynamic runs: three LDH species at M/A 4, 6, and 8 form in
  roughly an 8:4:2 ratio, averaging M/A ≈ 5 — supporting the stoichiometric assumption.
  Thermodynamics yields trace portlandite not confirmed by XRD/TG experiments (Park et al. 2020a).
- Practical standing: strength/shrinkage/durability screening indicators are obtainable from
  spreadsheet-level linear equations without iteration — an alternative to the accessibility
  barrier of thermodynamic programs.

## Methods

- Raw materials: domestic G-grade blast-furnace slag (gypsum-ground; CaO 45.7, SiO2 29.1,
  Al2O3 11.7, MgO 3.1 %; Park et al. 2020b) and OPC taken as theoretical pure CEM I 42.5R
  clinker composition rather than XRF (amorphous impurities per Rietveld analysis). Sulfur in
  the slag is split into sulfate (SO3 2.0 %) and sulfide (S 0.3 %), quantified separately by
  ASTM C114 BaCl2 and CdCl-ZnSO4 methods — essential for the thermodynamic calculation since
  sulfide is stabilized as H2S and forms no hydrates.
- Mixes: sodium metasilicate pentahydrate activator (Na2SiO3·5H2O) at 6 %, 10 %, and 14 % of
  binder weight (slag + activator) × w/b 0.4 and 0.5 = 6 mixes. Only the final hydrated state
  assuming 100 % reaction of slag and activator is computed (no hydration kinetics); w/b below
  0.4 excluded as unworkable flow could not be secured.
- Comparators: OPC stoichiometry follows Brouwers 2011 (succeeding Powers-Brownyard);
  OPC thermodynamic results borrowed from Park et al. 2020b. Gehlenite and akermanite are
  nearly unreactive but negligible in quantity, following common practice.
- Outputs: hydrate mole-number equations (1)–(8); bound water, chemical shrinkage Vcs, and
  porosity phi via equations (11)–(15). Porosity explicitly excludes entrained/entrapped air:
  it is a theoretical value in the capillary + gel pore sense.

## Results

- Phase composition (AAS, w/b 0.5 example): C-(N-)A-S-H ~33–36 %, stratlingite 9–16 %
  (prominent at SS 6 %), M-A-H 4–8 %, residual pore solution 17–30 %, void (chemical
  shrinkage share) 13–23 %. Since AFt does not actually form in sodium silicate systems,
  the w/o-AFt case is closer to reality and w/-AFt is shown for comparison only.
- w/b barely affects phase composition; sodium silicate dosage dominates. Increasing SS
  raises bound water, porosity, and chemical shrinkage together. Excess activator implies
  long-term expansion of theoretical porosity → overestimated shrinkage and possible micro-
  cracking (at 28-day DoH, the SS 6 % mix reaches the level of the SS 14 % mix at 1 day;
  Park et al. 2020b).
- Against OPC: the chemical shrinkage (void fraction) of AAS far exceeds OPC's; in OPC
  thermodynamic runs part of the residual water separates into C-S-H gel pores, absent in
  the AAS calculation.
- Error diagnosis: attributable to simplification of several hydrate mole ratios; expected
  to shrink once thermodynamically confirmed hydrates such as portlandite are incorporated.

## Related Notes

- [[abate-2018-internal-curing-effect-of-raw]] — experimental companion by the same team
  (Abate, Song K.-I., Lee B.-Y., Kim H.-K.) on slag cement mortar; where this paper is the
  theory part, the 2018 paper is a case of bound-water measurement.
- [[choi-2020-aas-shcc-micromechanics]] — micromechanics of AAS-based SHCC (user group):
  composite application direction of the AAS hydration model.
- [[song-2012-aas-carbonation-characteristics]] — AAS carbonation characteristics
  (user-group AAS axis).
- [[shi-2006-alkali-activated-cements-and-concretes]] — AAS textbook hub.
- [[nematollahi-2017-one-part-shgc-micromechanics]] — micromechanics of AAM-family SHGC,
  sharing the issue of hydrate diversity across activator types.
