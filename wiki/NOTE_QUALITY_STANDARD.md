# LLM Wiki (English Edition) — Note Quality Standard

This is the single authoritative document governing the quality of every note created
or edited in this wiki. Read it before any writing task and use its self-check items
(§7) to declare completion.

- Version: 1.0 EN (2026-08-24), translated and adapted from the Korean original v1.0.
- Scope: all notes under `wiki/papers/`, `wiki/references/`, `wiki/concepts/`,
  `wiki/overviews/`.
- Precedence: `AGENTS.md` (schema) over this document (quality). On conflict,
  AGENTS.md wins.

---

## 1. Three fidelity tiers

Every paper is written at one of three tiers. **Assign the tier before writing.**

| Tier | Size target | Applies to |
|---|---|---|
| [Deep-read] | 5–11 KB | Papers from the maintainer's group (DJP/IJP, co-authored by Bang Yeon Lee), theoretical origin papers, classics that opened lineages, landmark reviews |
| [Standard] | 2.5–4 KB | Ordinary research papers (the default — when unsure, Standard or above) |
| [Brief] | 0.8–2 KB | Textbooks, theses, standards, reports: `references`-type only |

**When in doubt, tier up.** Writing thin and moving on is the worst failure mode.

### Worked examples from this wiki

| Tier | Example files |
|---|---|
| [Deep-read] | `papers/chun-2024-rc-beams-impact-resistance-hpfrcc.md`, `papers/choi-2021-fiber-hybridization-aas-healing.md` |
| [Standard] | `papers/park-2022-pe-pva-hybrid-healing-comparison.md`, `papers/lao-2022-seawater-sea-sand-egc.md` |
| [Brief] | `references/aci-544-1r-96-frc-report.md`, `references/afgc-2013-uhpfrc-recommendations.md` |

---

## 2. Mandatory structure (five sections)

Paper notes must contain all five sections:

```
---
title: "Paper title (Authors, Year)"
type: source_note
source: "sources/original-filename.pdf"
citation: "Authors. Title. Journal vol(issue) (Year) pages. doi: ..."
date: YYYY-MM-DD
tags: [keyword, ...]
---

# One-line title

## Summary
## Key Contributions
## Methods
## Results
## Related Notes
```

Missing frontmatter = batch-close violation. The close-out script catches it.
In this edition, `source` and `citation` values are carried over **unchanged** from the
Korean notes; only `title` is translated. Korean-language paper titles inside citations
stay verbatim.

---

## 3. Section requirements

### 3.1 Summary

- Compress purpose + method + key quantitative result + conclusion into one paragraph
  (3–6 sentences).
- **Must include the headline numbers**: strength (MPa), strain capacity (%), mix
  substitution ratios (%), etc.
- Bad: "This study evaluated the tensile behavior of ECC." (no numbers)
- Good: "The PE-fiber ECC (2 vol %) achieved a tensile strength of 8.5 MPa and a strain
  capacity of 7.5 %, 1.5 times the ductility of the PVA-ECC control (4.9 %)."

### 3.2 Key Contributions (3–6 items)

- Each item = **mechanism interpretation + quantitative evidence**, as a pair.
- Bad: "Ductility was improved."
- Good: "Crack width decreased from 100 µm to 59.8 µm, staying within the self-healing
  threshold of 100 µm."
- Number every item (1., 2., ...).

### 3.3 Methods

[Deep-read] notes must record all of:

- Mix proportions: binder (W/B), SCMs and substitution ratios, SP dosage
- Fiber specs: type, material, diameter (µm), length (mm), volume fraction (vol %),
  surface treatment (oil coating % etc.)
- Specimens: dimensions (mm), count, curing conditions
- Test methods: standard (ASTM/JSCE/ISO), loading rate, instrumentation (LVDT/DIC etc.)

[Standard] notes must still give a mix summary plus one or two lines on the test method.

### 3.4 Results

- Port small quantitative datasets as markdown tables (mix tables, result tables).
- Where data exist only as figures, extract the key numbers from the text.
- At least one table recommended for [Deep-read].

### 3.5 Related Notes

- Never delete existing links.
- Add links only to **notes that actually exist** (verify with glob/grep). A broken link = lint failure.
- One-line relationship per link: `- [[note-name]] — what the relationship is`
- Recommended density: 3–7 links (more becomes noise).

---

## 4. Style conventions

| Item | Rule |
|---|---|
| Language | English throughout; no residual Korean in body text (verbatim bibliographic fields excepted) |
| Tone | Dry declarative academic prose; no exclamation, no speculation presented as fact |
| Numbers + units | One space between value and unit: `8 %`, `50 µm`, `36.8 MPa`; degree sign attaches only to angles (`90°`, but `20 °C`) |
| em-dash | Prohibited; use commas or parentheses |
| Hanja / CJK characters | Prohibited in body text |
| Human subjects | Avoid ("the authors..." style prohibited); prefer passive or inanimate subjects |
| AI filler words | Prohibited ("notably", "remarkably", "interestingly", "it is worth noting") |
| Methods voice | Past passive ("Specimens were tested...") |
| Results voice | Cite exhibits explicitly ("Fig. X shows...", "Table 3 lists...") |
| Tensile parameters | first-cracking strength (σcc), post-cracking strength (σpc), strain capacity (εpc), strain-hardening ratio (σpc/σcc) |

Terminology follows `wiki/GLOSSARY.md` without deviation.

---

## 5. Translation checklist (per note, English edition)

```
[ ] 1. Identify the Korean source note (same filename).
[ ] 2. Read the full Korean note before translating.
[ ] 3. Translate body text; keep frontmatter keys type/source/citation/date/tags unchanged.
[ ] 4. Convert fidelity tag: [심독]→[Deep-read], [표준]→[Standard], [간략]→[Brief].
[ ] 5. Apply GLOSSARY.md terms exactly; no variant renderings.
[ ] 6. Preserve every number, unit, table row, and [[wikilink]] target verbatim.
[ ] 7. Section headings in English: Summary / Key Contributions / Methods / Results / Related Notes.
[ ] 8. No residual Korean/Hanja in body text (citation original titles exempt).
[ ] 9. Run scripts/check_translation.py for this pair → numeric/link/frontmatter checks pass.
[ ]10. File size within ±20 % of the Korean original (translation may vary, content may not).
[ ]11. Mark done in _translation_progress.json.
[ ]12. After each batch: en_lint.py + spot-check 2 random pairs against source PDFs if any numeric claim looks load-bearing.
```

---

## 6. Special cases

### 6.1 Duplicate copies

If two PDFs are byte-identical duplicates: one note only, both filenames recorded in its
`source` field, both ledger entries marked done. (Already resolved in the Korean wiki;
this edition inherits the surviving notes.)

### 6.2 Series papers (Part 1/2...)

One merged note if the abstracts show the same study; separate notes otherwise.

### 6.3 Korean-language papers

Citations keep the original Korean title verbatim; body text is English. Do not invent
translations of cited titles.

### 6.4 Reference-type documents

Written under `wiki/references/`, [Brief] tier. Only Summary + Related Notes are
mandatory (Methods/Results may be omitted).

### 6.5 Concept pages

Under `wiki/concepts/`, `type: concept`. Lineage tables, key-paper links, and formulas
raise their value sharply. Reference example:
`concepts/fiber-bridging-constitutive-law.md`.

### 6.6 Known contaminated numbers

Three rewritten Korean notes were found to contain fabricated values
(luong-2023, nguyen-2021, nguyen-2023). When translating these, verify every headline
number against the extracted source text before porting it; do not translate
uncritically. See `wiki/log.md` for the audit record.

---

## 7. Post-batch self-check

Before closing any batch:

1. Every new note satisfies §2 structure (frontmatter keys + five sections).
2. Size targets met (§1).
3. check_translation.py passes for all translated pairs.
4. Broken links 0 (run en_lint.py).
5. Residual Korean/Hanja in EN body text 0.
6. Ledger pending count decreased accordingly.
7. index/log updated.

If any item fails, the batch is not closed.
