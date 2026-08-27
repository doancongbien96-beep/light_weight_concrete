---
title: "Modified Stoichiometric Model for Describing Hydration of Alkali-Activated Slag (Abate et al., 2021)"
type: source_note
source: "sources/abate-2021-modified-stoichiometric-model-for-describing-hydration.pdf"
citation: "Abate, S. Y., Park, S. M., Song, K. I., Lee, B. Y., & Kim, H. K. (2021). Modified stoichiometric model for describing hydration of alkali-activated slag. Journal of the Korea Concrete Resources Recycling Institute, 9(1), 1-12. https://doi.org/10.14190/JRCR.2021.9.1.1"
date: 2026-08-24
tags:
  - alkali-activated-slag
  - stoichiometric-model
  - c-n-a-s-h-gel
  - chemical-shrinkage
  - bound-water
  - hydration-kinetics
---

## Summary

To theoretically predict the hydrate product composition, bound water, chemical shrinkage, and porosity evolution of an alkali-activated slag (AAS) system, this study developed a modified stoichiometric hydration model that couples the formation of secondary hydrates — the C-(N-)A-S-H gel plus hydrotalcite (Ht), strätlingite (St), and ettringite (AFt). The team comprises Dr. Selamu Yihune Abate (Bless Construction PLC, Addis Ababa), Prof. Solmoi Park (Pukyong National University), Prof. Keum-Il Song and Prof. Bang Yeon Lee (Chonnam National University), and corresponding author Prof. Hyeong-Ki Kim (Chosun University). Taking the slag oxide composition ($CaO, SiO_2, Al_2O_3, MgO$) and the sodium hydroxide/sodium silicate activator concentrations as inputs, the model closely simulates the phase fraction evolution and the chemical shrinkage ($V_{cs}$) as functions of the degree of hydration $\alpha$.

## Key Contributions

- **Establishment of an AAS-specific modified stoichiometric hydration mechanism**: the $Ca/Si$, $Al/Si$, $Na/Si$ molar ratios ($a, b, c$) inside the C-(N-)A-S-H gel are linked to the WDXRS-based experimental relation $Al/Si = (1-0.44)(Ca/Si)/4.5$.
- **Completion of a two-condition hydrate partitioning model depending on AFt formation**: closed-form solutions of the simultaneous linear equations derived for the with-AFt (w/ AFt) and without-AFt (w/o AFt) conditions.
- **Theoretical formulation of chemical shrinkage ($V_{cs}$) and bound water ($n_H$)**: quantitative computation of the absolute volume reduction driven by the hydration reactions.
- **Quantitative comparison of the thermodynamic volume change of reaction products against portland cement**: pore structure predicted as a function of slag replacement ratio and activator $Ms$.

## Methods

- Model chemistry: slag oxides $y_C, y_S, y_A, y_M, y_F, y_{\bar{S}}$ plus activator species $y_{Na}, y_H$ taken as inputs.
- Principal products: C-(N-)A-S-H ($C_a N_c A_b S H_w$), hydrotalcite ($M_4 A H_{10}$), strätlingite ($C_2 A S H_8$), AFt ($C_6 A \bar{S}_3 H_{32}$).
- Verification: benchmarked against existing Gibbs free-energy minimization (GEMS) thermodynamic simulations and the WDXRS measured dataset.

## Results

- Hydrate mole numbers and volume evolution predicted by the stoichiometric model as the slag degree of hydration $\alpha$ progresses:

| Hydrate formed | Chemical formula | Molar mass $M_j$ ($g/mol$) | Specific gravity $\rho_j$ ($g/cm^3$) | Molar volume $\omega_j$ ($cm^3/mol$) | Moles, w/ AFt condition (mol) | Moles, w/o AFt condition (mol) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| C-(N-)A-S-H | $C_a N_c A_b S H_w$ | 165.2 | 2.15 | 76.8 | $n_{CNASH} = 0.852$ | $n_{CNASH} = 0.912$ |
| Hydrotalcite | $M_4 A H_{10}$ | 502.8 | 2.05 | 245.3 | $n_{Ht} = 0.125$ | $n_{Ht} = 0.125$ |
| Strätlingite | $C_2 A S H_8$ | 418.3 | 1.94 | 215.6 | $n_{St} = 0.042$ | $n_{St} = 0.068$ |
| Ettringite (AFt) | $C_6 A \bar{S}_3 H_{32}$ | 1255.1 | 1.78 | 705.1 | $n_{AFt} = 0.024$ | $n_{AFt} = 0.000$ |
| Chemical shrinkage $V_{cs}$ | absolute volume reduction | - | - | - | **$4.82 cm^3/100g$** | **$4.15 cm^3/100g$** |

## Related Notes

- [[alkali-activated-materials]] — fundamentals of alkali-activated materials
- [[one-part-shgc]] — one-part high-ductility geopolymer design
- [[sustainability-low-carbon-binders]] — low-carbon sustainable binders
