---
title: "Experimental study and code predictions of fibre reinforced polymer reinforced concrete (FRP RC) tensile members (Baena, Turon, Torres & Miàs, 2011)"
type: source_note
source: "sources/baena-2011-experimental-study-and-code-predictions.pdf"
citation: "Baena, M., Turon, A., Torres, Ll., Miàs, C. Experimental study and code predictions of fibre reinforced polymer reinforced concrete (FRP RC) tensile members. Composite Structures 93 (2011) 2511-2520. doi: 10.1016/j.compstruct.2011.04.012"
date: 2026-08-23
tags: [gfrp-bar, rc-tensile-member, tension-stiffening, crack-spacing, crack-width, code-comparison, eurocode2, aci-440]
---

# Experimental study and code-prediction comparison for GFRP-reinforced RC tensile members

## Summary

Experimental study of GFRP-reinforced concrete tensile members (ties) by the AMADE group at the University of Girona (Composite Structures 93, 2511-2520). Six specimens with reinforcement ratios of 0.51~1.69 %, combining three GFRP bar diameters (12.7/15.9/19.1 mm) with two square cross-sections (170/110 mm), were tested in direct tension, and load–mean strain response, crack spacing, and crack width were compared against the predictions of Eurocode 2 (EC2-92/-04), ACI 224/ACI 440, and Model Code 90 (MC90). Because of the low elastic modulus of FRP, serviceability (deflection and crack width) governs design; the study quantitatively confirms that simple extension of steel-based design equations is unsuitable for GFRP RC tensile members, and proposes a new regression equation for crack spacing.

## Key Contributions

- **Deformation prediction**: ACI 224/440 (effective section Ae based on the Branson equation) overestimates member stiffness and therefore clearly underpredicts strains; introducing the reduction factor βd = 0.5(E_FRP/E_steel)+1 of ACI 440.1R-03 does not resolve this. By contrast, the EC2-92 mean-strain equation brackets the experimental curves across the two limiting bond coefficients β1 = 0.5 (smooth surface) and 1 (ribbed), with β1 = 0.5 conservative.
- **Crack stabilization**: the ratio of crack-stabilization load to first-cracking load, Psta/Pcrack, shows dependence on the reinforcement ratio, contrary to MC90's constant 1.3 assumption (measured 1.14~1.75, growing with reinforcement ratio).
- **Crack spacing**: the EC2-92 mean crack-spacing equation (srm = 50 + 0.25 k1k2 db/ρeff, k1 = 0.8) overpredicts the measured values by factors of 1.96~3.83, and the EC2-04 maximum crack-spacing equation by 2.09~5.17. A new regression **srm = 20.8 + 0.0835 db/ρeff** (mm) is proposed, suggesting that in tensile members, whose small sections come with large cover thicknesses, the role of concrete cover differs from that in flexural members.
- **Crack width**: ACI 224 underpredicts for lack of an FRP bond-characteristic coefficient. ACI 440.1R-03 (a Gergely-Lutz variant, design value kb = 1.2) and ACI 440.1R-06 (physical model, default kb = 1.4), although developed for flexure, in fact predict the maximum crack width of GFRP ties accurately (the two editions are nearly identical). The EC2 crack-width equation depends on the crack-spacing prediction, so direct application overpredicts; substituting the paper's srm equation yields a substantial improvement.
- **Shrinkage effect quantified**: using MC90 shrinkage strain predictions, the initial shortening εm,i = εsh/(1+nρ) and an additional initial tensile load Padd = εsh·E_FRP·A_FRP were computed; thanks to early testing at 28 days and the low FRP elastic modulus, the influence on the overall response was minor.

## Methods

- Hughes Brothers Aslan 100 helically wrapped, sand-coated GFRP bars. Member length 1300 mm with 50 mm debonded at each end, giving an effective bonded length of 1200 mm. One bar placed at the center of the cross-section.
- Concrete: ready-mix, maximum aggregate 20 mm, target strength 50 MPa. Mixes C1/C2/C3 showed compressive strengths of 48.1/56.2/46.6 MPa and elastic moduli of 27,315/33,275/34,514 MPa. GFRP bar tensile strength 535~1030 MPa (varies with nominal diameter).
- Loading: tension applied at both ends without damaging the bar via a drilled-through threaded-bar plus epoxy grip system, under displacement control. Whenever a new crack appeared, loading was paused to record cracks and strains. Deformation was doubly instrumented with LVDTs and a Demec mechanical strain gauge of 150 mm gauge length; crack width was read with an optical magnifier (precision 0.05 mm).
- Two notched (N) specimens (19-170-N, 16-170-3N) used internal bar strain gauges and notches to guide crack locations for numerical analysis; they were used only for the deformation-response analysis and excluded from crack statistics.

## Results

- Three regimes of tensile response: linear before cracking → crack propagation (reduced slope, zigzag under displacement control) → after crack stabilization, only opening and closing of existing cracks. In the ρ = 1.00 % specimen, transverse cracks occurred mixed with splitting cracks.
- First-cracking load Pcrack = 28.4~74.6 kN, with 4~9 transverse cracks at stabilization. Measured mean crack-spacing ratios sr,max/srm = 1.53 (within the literature range 1.33~1.54) and sr,min/srm = 0.58 (slightly below the literature range 0.67~0.77).
- Crack width: during the crack-formation stage the mean crack width wm,exp = 0.40~1.95 mm, reaching a maximum of 3.00 mm (ρ = 1.69 %, at 87.69 kN). Maximum and minimum crack widths follow linear trends with the mean crack width.

## Related Notes

- [[bakis-2002-frp-composites-construction-state-of-the-art]] — FRP construction review (quantitative tie-test confirmation of its 'serviceability governs' argument for internal reinforcement)
- [[gangarao-2007-frp-rc-design-textbook]] — FRP RC design textbook (the system of design equations compared in this paper)
- [[su-2024-flexural-behavior-beams-gfrp-hpfrcc-strengthening]] — GFRP bar + HPFRCC strengthened beams (application volume of the GFRP bond/serviceability axis)
- [[esfahani-2020-hpfrcc-substitution-gfrp-rc-beams]] — HPFRCC substitution in GFRP-reinforced beams (route to improved crack width and ductility)
- [[fischer-2003-frp-reinforced-ecc-cyclic-flexure]] — FRP-reinforced ECC flexure (matrix tensile ductility compensating low reinforcement stiffness)
- [[ecc-hybrid-frp-steel-beams]] — FRP + steel hybrid beams (ductility compensation for FRP's linear-elastic rupture)
- [[pseudo-strain-hardening-criteria]] — theoretical counterpart between RC-tie crack stabilization and SHCC multiple-cracking stabilization
