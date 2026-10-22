# Your Paper Library

This website uses the interface and source code from [ekvm80/llm-wiki-en](https://github.com/ekvm80/llm-wiki-en), adapted for the PDF collection in your Papers folder.

## Open the library

Start a local web server from the Papers folder, which contains `llm-wiki-source` and the PDF files:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/llm-wiki-source/`. A local server lets the browser load the catalog and paper notes. Each paper links to its original PDF in the Papers folder.

## Publish with GitHub Pages

The repository deploys the website from its root when changes are pushed to `main`:

```text
https://doancongbien96-beep.github.io/light_weight_concrete/
```

In the repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**. The workflow publishes the website files automatically. The PDFs are not uploaded, so the online paper pages show each original filename and point out that the PDF remains in your local Papers folder.

## Update the catalog after adding PDFs

Place new PDFs in the Papers folder, then open PowerShell in the website folder and run:

```powershell
python tools/process_papers.py
python tools/build.py --wiki paper-source --out . --lang en
node tools/layout.mjs
```

Python package `pypdf` and Node.js are required. The site creates one note per PDF. `tools/process_papers.py` extracts the title, year, DOI, page count, and abstract when possible, and suggests related papers based on keywords. Verify DOI links against the original paper before citing.
