# LLM Wiki (English Edition) — User Manual

This guide is for first-time users of the English edition at
`~/Documents/Research_Knowledge/llm_wiki_en/`. It is written for native English
speakers; no Korean knowledge is assumed.

---

## 1. What is this wiki?

A knowledge base built by reading and summarizing 907 research papers on cementitious
composites (ECC, SHCC, UHPC, geopolymers, and related materials). It contains **985+
notes** in English.

| Folder | Contents | Notes |
|---|---|---|
| `wiki/concepts/` | Core concept pages (strain-hardening, multiple cracking, ...) | 23 |
| `wiki/papers/` | Individual paper summaries | 876 |
| `wiki/references/` | Textbook / report / thesis summaries | 86 |
| `wiki/index.md` | Full catalog (what notes exist, one line each) | — |
| `wiki/log.md` | Operation history (what was done, when) | — |

This edition is a translation of the Korean original at
`~/Documents/Research_Knowledge/llm_wiki/`. Both wikis share the same 907 source PDFs
(through the `sources/` symlink) and are maintained side by side.

---

## 2. Getting started

### 2.1 Finding what you need

**Option 1: Open `wiki/index.md`.** Every note is listed under topical headings.
Search with Ctrl+F / Cmd+F. Example: searching "self-healing" lists every healing-related note.

**Option 2: Start from the concept pages.** Recommended reading order for newcomers:

1. `pseudo-strain-hardening-criteria.md` — why ECC can deform like a ductile metal
2. `strain-hardening-mechanism.md` — the tensile strain-hardening mechanism
3. `multiple-cracking-behavior.md` — why many fine cracks form instead of one large crack
4. `fiber-bridging-constitutive-law.md` — how fibers bridge cracks (the σ–δ law)
5. `crack-width-control.md` — why tight crack widths matter

Then follow your interest:
- Self-healing → `self-healing-ecc.md`
- Impact & blast resistance → `impact-and-blast-resistance-frcc.md`
- Lunar construction → `lunar-isru-materials.md`
- 3D printing → `3d-printable-ecc.md`

**Option 3: Ask an AI agent** (Hermes or any assistant whose working directory is this
folder). "Find papers on impact resistance" will search the notes and summarize with citations.

### 2.2 Reading a note

Every note (.md file) follows this structure:

```
---
title: "Paper title (Authors, Year)"   ← translated title
type: source_note                      ← note type
source: "sources/original-PDF-filename.pdf"  ← location of the source PDF
citation: "Authors. Title. Journal, vol(issue), pages. doi"   ← verbatim from the original
date: YYYY-MM-DD
tags: [keyword1, keyword2, ...]
---

# One-line title

## Summary             ← what the study is, in one paragraph
## Key Contributions   ← 3–6 key findings, each with quantitative evidence
## Methods             ← how the experiments were done
## Results             ← numbers and tables
## Related Notes       ← links to other notes ([[...]])
```

**Quick skim**: read Summary only.
**Deep understanding**: Key Contributions → Methods → Results.

Fidelity tags tell you how deeply the note was read: **[Deep-read]** (5–11 KB,
full experimental detail), **[Standard]** (2.5–4 KB), **[Brief]** (≤2 KB,
reference-type documents only).

### 2.3 Following [[links]]

Notes contain `[[other-note-name]]` wikilinks. In Obsidian (open `wiki/` as a vault)
they are clickable backlinks, and the graph view visualizes relationships between notes.

---

## 3. Topic guides

- **ECC/SHCC fundamentals**: concepts `pseudo-strain-hardening-criteria`,
  `multiple-cracking-behavior`, `fiber-bridging-constitutive-law`;
  papers `li-2003-ecc-review-jact` (general review), `li-wu-1992-psh-conditions`
  (theoretical origin).
- **High-strength high-ductility lineage**: `ranade-2013-hshdc-micromechanics` →
  `yu-2014-uhpecc-pe-fibers` → `nguyen-2021-ud-egc-13-7-percent`.
- **Self-healing**: `self-healing-ecc`, `crack-width-control`;
  papers `yang-2011-autogenous-healing-early-age`, `park-2022-pe-pva-hybrid-healing-comparison`.
- **Geopolymer / alkali-activated (AAS/AAF)**: `alkali-activated-materials`,
  `one-part-shgc`, `fly-ash-ggbs-binary-system`; papers
  `nematollahi-2017-one-part-pe-shgc-micromechanics`, `choi-2020-aas-shcc-micromechanics`.
- **Impact & blast**: `impact-and-blast-resistance-frcc`; papers
  `chun-2024-rc-beams-impact-resistance-hpfrcc`, `yankelevsky-1997-slab-missile-impact`.
- **Lunar / space construction**: `lunar-isru-materials`; references
  `heiken-1991-lunar-sourcebook`, `benaroya-lunar-base-engineering-series`;
  paper `cesaretti-2014-lunar-soil-3d-printing`.
- **Sustainability / low-carbon**: `sustainability-low-carbon-binders`;
  papers `scrivener-2016-unep-eco-efficient-cements`, `lee-2019-cfbc-ash-slag-cement`.
- **NDT / structural health monitoring**: `ndt-and-shm-of-cementitious`; papers
  `kim-2007-fbg-smart-tendon`, `tran-2018-pulsed-thermography-defects`.
- **3D printing**: `3d-printable-ecc`; papers
  `zhu-2019-3dp-ecc-ultra-high-ductility`, `cesaretti-2014-lunar-soil-3d-printing`.

---

## 4. Locating the source PDF

Each note's frontmatter carries a `source:` field pointing into the shared pool:

```
source: "sources/Li - 2003 - On Engineered Cementitious Composites.pdf"
```

Open it under `~/Documents/Research_Knowledge/llm_wiki/sources/` (or equivalently
through this edition's `sources/` symlink).

---

## 5. FAQ

**Q: How is note quality maintained?**
A: `wiki/NOTE_QUALITY_STANDARD.md` defines three fidelity tiers ([Deep-read] /
[Standard] / [Brief]), the mandatory five sections, style conventions, and a checklist.
Every new note is written and verified against it.

**Q: Why does this edition exist alongside a Korean wiki?**
A: The original wiki was written in Korean for its maintainer's group. This English
edition makes the same knowledge base usable by international collaborators. The two
share sources and structure; content diverges only during translation lag.

**Q: May I edit the PDFs in `sources/`?**
A: No. Never modify or delete originals, even to fix typos.

**Q: How do I add a new paper?**
A: Drop the PDF into the Korean wiki's `sources/` folder and ask an AI agent there to
ingest it. After ingestion it appears in the translation queue for this edition.

**Q: Links seem broken — how do I check?**
A: Ask an agent to run the lint script (`scripts/en_lint.py`). It checks broken links,
orphans, catalog omissions, and residual non-English text across all notes.

**Q: Can I open this in Obsidian?**
A: Yes. Open `wiki/` as a vault. `[[links]]` work as clickable backlinks and the graph
view renders the network.

---

## 6. Glossary for newcomers

| Term | Meaning |
|---|---|
| ECC | Engineered Cementitious Composites — micromechanically designed, strain-hardening cement composite |
| SHCC | Strain-Hardening Cementitious Composites — synonymous with ECC |
| UHPC / UHPFRC | Ultra-High Performance (fiber-Reinforced) Concrete, compressive strength ≥120 MPa |
| PSH | Pseudo Strain-Hardening — ECC's defining property |
| AAS / AAF | Alkali-Activated Slag / Fly ash — binder systems without Portland cement |
| EGC | Engineered Geopolymer Composites — geopolymer-based ECC |
| HSHDC | High-Strength High-Ductility Concrete |
| J′_b / J_tip | Complementary crack-bridging energy / crack-tip toughness — the two axes of the PSH performance index |
| ISRU | In-Situ Resource Utilization (lunar/Mars construction) |
| MSI | Material Sustainability Indicator |
| PCM | Phase Change Material (thermal storage) |
| FBG | Fiber Bragg Grating (optical strain sensor) |

---

*Created 2026-08-24 · English edition of the llm_wiki user manual.*
