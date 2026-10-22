# Paper Library Rules

- Do not move or rename PDFs in the Papers folder; each note links to the original filename.
- After adding or removing PDFs, rerun `tools/process_papers.py`, `tools/build.py --wiki paper-source --out . --lang en`, and `tools/layout.mjs`.
- Generated notes are stored in `wiki/papers/`; map data is stored in `data/graph.json` and `data/catalog.json`.
- Check automatically extracted abstracts against the PDF before using them in a thesis or citation.
- DOI links reflect DOI strings found in the file. Topic-based links are keyword suggestions, not verified citations.
