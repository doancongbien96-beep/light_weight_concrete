---
title: "Modeling Engineered Cementitious Composites (ECC) — ACBM/NIST workshop presentation (Ranade, 2008)"
type: source_note
source: "sources/P7 Ranade & Li (2008).pdf"
citation: "Ranade, R. Modeling Engineered Cementitious Composites (ECC). 19th ACBM/NIST Computer Modeling Workshop 발표 슬라이드 12매(2008년 6월 16~18일, Gaithersburg, Maryland, University of Michigan ACE-MRL). 파일명과 달리 단독 발표자는 Ranade."
date: 2026-08-22
tags: [ecc-modeling, multiscale, workshop-slides, micromechanics, nist, fiber-bridging, poster-series]
---

# ECC Modeling — ACBM/NIST Workshop Presentation

## Summary

A 12-slide deck presented by Ravi Ranade at the 2008 ACBM/NIST Computer Modeling Workshop. The material connects ECC's micromechanics design frame (single fiber pullout → bridging stress–crack opening → multiple cracking → structure) to NIST's concrete microstructure modeling capability, proposing a computational toolchain spanning nano-to-infrastructure scales and publicly soliciting collaboration.

## Key Contributions

- Map of ECC scale linkages: compresses onto a single slide the experiment-model correspondence at each stage — 10⁻⁶~10⁻⁵ m (single fiber pullout) → multi-fiber bridging → multiple-cracking structural elements → full ECC member structures.
- Interface parameter system: introduces the σB-δ bridging curve model including Gd (chemical bond), τ0 (frictional stress), β (slip hardening coefficient), and the snubbing coefficient f — directly citing Yang & Li 2008 JACT (the origin of the fiber-bridging constitutive law) in its references.
- Crack-width upper-bound logic: unlike ordinary concrete, whose random cracks make service-life prediction impossible, the crack width of ECC is a material property independent of reinforcement detailing and structural size, bounded at about 60 µm — grounds for coupling with durability and transport models (ECC service-life prediction).
- NIST model confirmed-task list: submicroscale control such as C-S-H growth, fiber dispersion and rheology simulation, hydrate growth around fibers, competition between autogenous shrinkage and tensile strength development, transport-property-based service-life and life-cycle cost prediction, hydration modeling of slag/silica fume/fly ash substitution, and time-dependent property changes under degradation and re-healing.
- Summary message: "ECC is moving from laboratory to full-scale field applications," and a set of computational tools linking nano-to-structural scales contributes to strong, durable, economical, sustainable infrastructure — the modeling axis of a roadmap continuing into the follow-up HSHDC report (P5) and posters (P3/P4).

## Related Notes

- [[fiber-bridging-constitutive-law]] — concept page on the bridging constitutive law cited directly in the deck's references.
- [[pseudo-strain-hardening-criteria]] — frame of conditions under which multiple cracking develops.
- [[ranade-2012-hshdc-poster]] — same author's follow-up HSHDC poster.
- [[li-2003-ecc-review-jact]] — Performance Driven Design overview (Li 1993 JSCE lineage).
