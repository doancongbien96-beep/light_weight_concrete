# LLM Wiki — Cementitious Composites Knowledge Graph

A research knowledge base of papers and textbooks on high-ductility and ultra-high-performance
cementitious composites (ECC · SHCC · EGC · UHPC · geopolymers), and a static dashboard for
reading it.

**→ https://ekvm80.github.io/llm-wiki-en/**

| | |
|---|---|
| Notes | **973** (concepts 23 · papers 859 · references 90 · overview 1) |
| Links between notes | **3,437** |
| Publication years | 1964 – 2026 |
| Tags | 3,272 |

Follows the [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
every note is joined to the others by `[[wikilinks]]`, forming a single network.

This is the English edition. The Korean original lives at
[ekvm80/llm-wiki](https://github.com/ekvm80/llm-wiki) — the two share note slugs, so
`viewer.html?note=<slug>` resolves to the same paper in either site.

## Pages

| Page | What it does |
|---|---|
| `index.html` | Citation network across all 973 notes (canvas force graph) |
| `catalog.html` | Full list — search titles, tags, journals and summaries; sort by year or link count |
| `concepts.html` | The 23 core concepts plus a recommended reading order |
| `about.html` | What this wiki is (renders MANUAL.md / AGENTS.md) |
| `viewer.html?note=<slug>` | Note reader — markdown rendered client-side |

## Layout

```
wiki/          the 973 source markdown notes (single source of truth)
data/          graph.json (nodes, edges, coordinates) - catalog.json (search text)
assets/        per-page JS plus shared CSS and the i18n string table
vendor/        d3 7.9 - marked 12 - KaTeX 0.16 (woff2 only)
docs/          MANUAL.md - AGENTS.md - NOTE_QUALITY_STANDARD.md - GLOSSARY.md
tools/         build.py - layout.mjs
```

Notes ship as plain markdown and the viewer renders them at read time. There are no
pre-rendered HTML copies, so editing a note updates the site directly.

## Rebuilding

```bash
sh tools/build.sh --wiki ~/Documents/Research_Knowledge/llm_wiki_en/wiki --lang en
python3 -m http.server 8000     # then open http://localhost:8000
```

`--strict` makes broken wikilinks, duplicate slugs or unbalanced `$` exit non-zero.

Always check locally over HTTP. Opening `file://` fails: the viewer's `fetch()` is blocked by CORS.

## Notes

- **Original PDFs are not included** — they are 4.1 GB of publisher material. Each note carries
  its full citation and a DOI link instead.
- `.nojekyll` is required. Without it Jekyll consumes the front-mattered `.md` files and the
  viewer's `fetch()` returns 404 for every note.
- The UI is driven by `assets/i18n.js` and `meta.lang` in `graph.json`, so this repo and the
  Korean one run the same code with different data.
