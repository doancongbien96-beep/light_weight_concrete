---
title: "Micromechanics of ECC: A Critical Review and New Insights (Li et al., 2023)"
type: source_note
source: "sources/__Yang micromechanics of ECC review paper.pdf"
citation: "Li, J., Qiu, J., Weng, J., Yang, E.-H. Micromechanics of engineered cementitious composites (ECC): A critical review and new insights. Construction and Building Materials 362 (2023) 129765."
date: 2026-08-22
tags: [ecc, micromechanics, fiber-bridging, steady-state-cracking, strain-hardening, multiple-cracking, stochastic-model]
---

# Micromechanics of ECC: A Critical Review and New Insights

## Summary

A review comprehensively surveying the current state of ECC micromechanics. Taking the scale-linking approach as its axis, it organizes the analytical framework running from micro-scale single-fiber pullout behavior through the meso-scale fiber bridging constitutive law and the pseudo strain-hardening (PSH) criteria to the macro-scale tensile behavior of the composite. It traces the evolution from deterministic models toward stochastic models that reflect microstructural heterogeneity, and treats the extension to dynamic loading and fatigue. Although the filename says Yang, the actual first author is J. Li (corresponding author E.-H. Yang).

## Key Contributions

1. Systematization of the three-tier scale-linking framework: micro (nm~μm, single-fiber pullout P(δ)) → meso (μm~mm, bridging stress σB(δ) and the PSH criteria) → macro (mm~cm, tensile stress–strain relation and crack characteristics).
2. Development history table (Table 1): 1992 closed-form solution for hydrophobic (PE) fibers → 1998 introduction of slip-hardening and apparent fiber strength → 1999 consideration of chemical bonding (PVA) → 2008 numerical solution (Yang et al.) → 2015 closed-form solution for hydrophilic fibers (Huang et al.). For the PSH criteria: introduced 1992 → rigorous conditions 1996 (Leung) → practical index 2006 (Kanda-Li) → dynamic 2014 → fatigue 2017 → stochastic 2018.
3. Distinction of interface types: hydrophobic PE fibers are friction-dominated with post-peak slip-softening, while hydrophilic PVA fibers exhibit dual behavior in which chemical bonding (G_d) and the slip-hardening coefficient β increase the post-peak bond resistance.
4. Sequential multiple cracking mechanism: the first crack forms at the cross-section with the minimum matrix cracking strength min[σ_c], subsequent cracks form outside the critical stress transfer distance x_d, and multiple cracking terminates when the stress reaches the minimum bridging strength min[σ_0] among the formed cracks.
5. Stochastic model (Li et al. 2019): treats all micromechanics parameters as random variables and outputs probabilistic tensile stress–strain curves including the distributions of crack initiation order, spacing, and width.
6. Extended analyses: under dynamic loading it clarified that E_f, J_tip, and G_d increase with strain rate, so fiber rupture becomes more frequent and strength rises while deformation capacity decreases. For fatigue, it presents a pullout model introducing a fatigue-induced debonding length Δa(N_d, P_max) and interfacial friction hardening coefficients γ_d, γ_s.

## Methods

This is a comprehensive literature review. The theoretical skeleton consists of the J-integral-based steady-state cracking analysis (Marshall-Cox), its extension to discontinuous randomly oriented fiber systems (Li-Leung), a shear-lag-based single-fiber pullout model, and an integral-type composite formula for the bridging stress (Eq. 8). The dynamic extension exploits the path independence of the energy release rate G(Γ) including kinetic terms, and the fatigue extension introduces interfacial parameters dependent on the number of load cycles N.

## Results

- The conditions for achieving PSH are the simultaneous satisfaction of the energy criterion J′_b ≥ J_tip and the strength criterion σ_0 ≥ σ_c. Experimental margin indices for saturated multiple cracking: PE-ECC shows J′_b/J_tip > 3 and σ_0/σ_c > 1.2, and some PVA-ECC shows σ_0/σ_c ≈ 1.45.
- Deformation capacity estimate: ε = Σδ_i/L (Eq. 15). Under the saturation assumption ε = δ/x, and the mean crack spacing x is on the order of the theoretical value of 1.337 x_d (Kimber et al.).
- Dynamic loading: tensile strength increases while tensile deformation capacity decreases (increased fiber rupture is the cause). The steady-state cracking analysis and the PSH criteria themselves retain their form under dynamic conditions as well.
- Fatigue: bridging effectiveness degrades, reducing both the degree of multiple cracking saturation and the tensile deformation capacity.
- Limitations and outlook: (i) absence of a direct linkage between micromechanics parameters and mix proportions (W/C, etc.), (ii) crack branching, banding, and interaction not considered (current models assume parallel cracks), (iii) incomplete scale-linking from material properties to structural performance (the ISMD concept proposed by Victor Li).

## Related Notes

- [[pseudo-strain-hardening-criteria]] — source literature for the energy/strength dual criteria and margin indices
- [[fiber-bridging-constitutive-law]] — derivation lineage of σ_B(δ) and the closed-form/numerical solution genealogy
- [[li-2003-ecc-review-jact]] — the same author's general review at the 10-year mark (predecessor of this review)
- [[park-2012-tensile-behavior-uhp-hfrc]] — UHP-HFRC (200 MPa matrix + coarse fiber 1 % + fine fiber) 16-series direct tension: coarse fiber type governs the curve shape, T-fiber highest (18.6 MPa, 0.64 %).
- [[aziz-2016-biomimicry-as-an-approach-for]] — literature offering a higher-level perspective on the materials innovation axis (biomimetic design methodology).
