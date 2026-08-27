# LLM Wiki (English Edition) — Operating Rules (Schema)

This repository is a research knowledge base following the Karpathy LLM Wiki pattern (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Domain: cementitious composites (ECC/SHCC/EGC/UHDCC/UHPC), tensile strain-hardening, multiple cracking, fiber bridging, and related topics.

**Provenance**: This is the English edition of `~/Documents/Research_Knowledge/llm_wiki/` (Korean original). All 907 source PDFs are shared via the `sources/` symlink and must never be modified. Notes here are English translations of the Korean originals; the two wikis are maintained side by side.

## Three-Layer Structure

```
llm_wiki_en/
├── AGENTS.md      ← this document (schema layer, agent entry point)
├── sources/       ← raw sources (symlink to Korean wiki's sources). Immutable.
│                     Never edit, rename, or delete anything inside.
├── wiki/          ← Wiki layer. The only layer agents write to.
│   ├── index.md   ← content catalog (kept up to date)
│   ├── log.md     ← append-only operation log
│   ├── NOTE_QUALITY_STANDARD.md  ← single authoritative quality spec
│   ├── GLOSSARY.md               ← fixed KO→EN terminology table (single source of truth)
│   └── _ingest_progress.json     ← ledger copied from the Korean wiki
```

- Never edit, rename, or delete PDFs under `sources/`.
- Only `wiki/` is writable by agents. Humans read it and set direction.

## Workflow

### Ingest (new paper)

New papers are ingested into the **Korean wiki first**, then translated here during sync batches. Do not ingest directly into this English edition unless the user explicitly asks; if you do, write the note directly in English following `wiki/NOTE_QUALITY_STANDARD.md`.

1. Pick one unprocessed PDF from `sources/` (user-designated takes priority).
2. Read the actual paper and create a summary note in `wiki/`. Filename: `firstauthor-lowercase-year-slug.md`.
3. Cross-link related existing notes (`[[filename]]`); create concept pages where none exists. One source may touch 10–15 pages.
4. Update `wiki/index.md`, and append one line to the end of `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | Author Year Title`

### Query

1. Read `wiki/index.md` first, then open candidate notes; go back to the source PDF when deeper detail is needed.
2. Cite supporting notes (or source filenames) in every answer.
3. File valuable answers (comparison tables, syntheses) as new notes under `wiki/overviews/` instead of leaving them in chat. The wiki must compound.
4. Log every query with one line in `wiki/log.md`.

### Lint (periodic audit)

When the user asks for a wiki audit: find contradictory statements, stale claims superseded by newer sources, orphan pages with no inbound links, frequently cited core concepts lacking pages, and missing cross-references. Fix them and record results in the log.

## Note Quality Standard (mandatory)

Note quality for any new or edited page must follow `wiki/NOTE_QUALITY_STANDARD.md`:
three fidelity tiers ([Deep-read]/[Standard]/[Brief]), mandatory 5-section structure,
style conventions, and a 12-step checklist. Read it before any writing task and use its
self-check items to declare completion.

## Terminology (mandatory)

All translations and new writing must follow `wiki/GLOSSARY.md`. It is the single
source of truth for domain terms (e.g., 변형률능력 → strain capacity, 다중균열 →
multiple cracking). Do not invent variant renderings of established terms.

## Note Conventions

- Required frontmatter keys: `title`, `type` (`source_note|concept|overview|synthesis`),
  `source` (filename inside sources/, or external URL), `date`, `tags`.
- Paper-note sections: Summary / Key Contributions / Methods / Results / Related Notes.
- Academic style: space between numbers and units (degree sign attaches only to angles),
  no em-dashes, dry declarative prose, no first-person-human subjects, no AI filler
  ("notably", "remarkably"). Methods in past passive; Results cite figures/tables
  explicitly ("Fig. X shows ...").
- `source` and `citation` fields carry over unchanged from the Korean notes
  (bibliographic data is not translated). Korean-language paper titles inside citations
  are preserved verbatim.
- Fidelity tags: [심독]→[Deep-read], [표준]→[Standard], [간략]→[Brief].

## Special Files

- `wiki/index.md`: full catalog of notes (link + one-line summary each). Updated after
  every ingest/batch. Read first on any query.
- `wiki/log.md`: append-only. Format `## [YYYY-MM-DD] <ingest|query|lint|schema> | title`.
  Keep it parseable: `grep "^## \[" log.md | tail -5`.
- `wiki/_ingest_progress.json`: filename → status ledger shared in structure with the
  Korean wiki's own ledger.

## Prohibitions

- Never modify or delete anything under `sources/`.
- No history falsification by manual index/log edits (log appends are the exception).
- No fabricated wiki content: never write a summary note without reading the source.
  When citing quantitative values, verify them against the extracted source text.
- Never mix artifacts with the separate ECC Atlas system
  (`~/Documents/Research_Knowledge/ECC_Research_Atlas/`). The two systems stay apart.
