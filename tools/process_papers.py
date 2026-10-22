#!/usr/bin/env python3
"""Create one source note per PDF in the parent Papers folder.

Run: python tools/process_papers.py
Then: python tools/build.py --wiki paper-source --out . --lang en
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse, hashlib, html, json, re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PDF_DIR = ROOT.parent
SOURCE = ROOT / "paper-source"
PAPERS = SOURCE / "papers"
TODAY = "2026-10-22"
TAXONOMY = {
    "lightweight-aggregate": r"lightweight aggregate|expanded clay|expanded shale|leca|pumice|perlite|vermiculite|cenosphere",
    "foamed-concrete": r"foam concrete|foamed concrete|foaming agent|foam glass",
    "self-compacting": r"self.?compacting|self.?consolidating|lwscc|scc concrete",
    "recycled-materials": r"recycl|waste|plastic|oil palm|palm kernel|rubber|tailings|red mud|sludge|biochar",
    "thermal-performance": r"thermal|temperature|heat transfer|insulation|thermomechanical|energy storage|phase change",
    "mechanical-properties": r"mechanical|compressive|tensile|strength|stress.?strain|modulus|fracture|impact",
    "durability": r"durab|marine|chloride|carbonation|sulphate|sulfate|acid resistance|permeability|shrinkage|creep",
    "low-carbon": r"low.?carbon|sustainab|co2|carbon|environmental|circular",
    "digital-and-ai": r"digital twin|machine learning|deep learning|neural network|artificial intelligence|optimization|prediction model",
    "fiber-reinforcement": r"fiber|fibre|reinforced|micro.?fiber",
    "supplementary-binders": r"fly ash|slag|ggbs|silica fume|geopolymer|alkali.?activated|rice husk|cement replacement",
    "oil-palm-shell": r"oil palm shell|palm kernel shell|palm oil clinker",
    "polystyrene-eps": r"polystyrene|eps bead|expanded polystyrene",
    "3d-printing": r"3d.print|additive manufact",
}
STOP = set("a an and are as at based by concrete concretes construction for from in into of on or properties study the their this using with lightweight development production investigation experimental review analysis effect effects performance research behavior behaviour material materials paper sustainable structural mechanical strength fresh hardened high influence characterization characterisation application novel numerical evaluation toward through mix design".split())
FIXES = {
    "1-s2.0-S1876610218311299-main.pdf": ("Employment the plastic waste to produce the light weight concrete", "2019"),
    "10.EvaluationofMechanical.pdf": ("Evaluation of Mechanical Properties of Lightweight Concrete with Pumice Aggregate", "2021"),
    "A8.pdf": ("Use of pumice fine aggregate as an alternative to standard sand in production of lightweight cement mortar", "2011"),
    "Journal-6_Oyejobi_USEP.pdf": ("Effects of Palm Kernel Shells Sizes and Mix Ratios on Lightweight Concrete", "2012"),
    "Paper-2.pdf": ("Effects of Palm Kernel Shells Sizes and Mix Ratios on Lightweight Concrete", "2012"),
    "MaterialspropertiesandapplicationreviewofLightweightconcrete.pdf": ("Materials, properties and application review of lightweight concrete", "2014"),
    "1-s2.0-S0950061818331179-main.pdf": ("Recent development and perspective of lightweight aggregates based self-compacting concrete", "2019"),
    "1-s2.0-S0958946598000353-main.pdf": ("Determination of the dividing strength and its relation to the concrete strength in lightweight aggregate concrete", "1999"),
    "1-s2.0-S0360132305001824-main.pdf": ("Quality improvement of oil palm shell (OPS) as coarse aggregate in lightweight concrete", "2006"),
    "1-s2.0-S2214785319339239-main.pdf": ("An experimental investigation on lightweight concrete blocks using vermiculite", "2020"),
    "ssrn-4043366.pdf": ("Experimental investigation on low density foamed concrete blended with nano-RHA and nano-GGBS as cement replacement", "2022"),
    "1-s2.0-S1877705815010930-main.pdf": ("Assessing the feasibility of using the heat demand-outdoor temperature function for a long-term district heat demand forecast", "2019"),
}
CACHED = {}
for entry_path in (ROOT.parent / "paper-wiki" / "extracted").glob("*.json"):
    try:
        entry = json.loads(entry_path.read_text(encoding="utf-8"))
        CACHED[entry.get("file")] = entry
    except (OSError, ValueError):
        pass

def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()

def slugify(s):
    return (re.sub(r"[^a-z0-9]+", "-", s.lower().replace("&", " and ")).strip("-")[:88].rstrip("-") or "paper")

def q(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ') + '"'

def doi_from(text):
    ms = re.findall(r"10\.\d{4,9}/[^\s<>\"\u0000]+", text, re.I)
    return list(dict.fromkeys(x.rstrip(".,;:) ]}").lower() for x in ms))

def read_pdf(path):
    cached = CACHED.get(path.name)
    if cached and cached.get("size") == path.stat().st_size:
        fix = FIXES.get(path.name)
        title, year = (fix if fix else (cached.get("title", path.stem), cached.get("year", "")))
        return {"file":path.name,"title":title,"year":year,"abstract":cached.get("abstract", ""),
                "doi":cached.get("doi", ""),"all_dois":cached.get("allDois", []),
                "pages":cached.get("pages", 0),"id":cached.get("id", hashlib.sha1(path.name.encode()).hexdigest()[:12]),
                "text":cached.get("searchText", "")}
    reader = PdfReader(path)
    pages = [(page.extract_text() or "") for page in reader.pages]
    first = "\n".join(pages[:2])
    title = norm(str((reader.metadata or {}).get("/Title", "")))
    if not title or len(title) < 20 or re.search(r"^doi:|^10\.|untitled|elsevier|microsoft", title, re.I):
        lines = [norm(x) for x in first.splitlines() if norm(x)]
        position = next((i + 1 for i, line in enumerate(lines[:35]) if re.search(r"journal homepage|contents lists available|available online at|www\..*journal|science direct", line, re.I)), 0)
        candidates = lines[position:]
        start = next((i for i, line in enumerate(candidates[:14]) if len(line) > 14 and not re.search(r"^(available online|science ?direct|www\.|received|accepted|article history|keywords|abstract|issn|vol\.?\s|journal homepage)", line, re.I)), 0)
        picked = []
        for line in candidates[start:start + 7]:
            if picked and (re.search(r"@|\b(19|20)\d{2}\b|received|accepted|abstract|department|university|article info", line, re.I) or len(line) < 6): break
            if re.search(r"journal homepage|www\.|science ?direct|energy procedia 00|contents lists available|\bISSN\b", line, re.I): continue
            picked.append(line)
        title = norm(" ".join(picked))
        if len(title) < 20: title = path.stem.replace("_", " ")
    am = re.search(r"abstract\s*[:：—-]?\s*(.*?)(?=keywords?\s*[:：]|\b1\s*[.]\s*introduction\b|©|\(C\)\s*\d{4})", first, re.I | re.S)
    abstract = norm(am.group(1)) if am else ""
    if len(abstract) < 80: abstract = ""
    ds = doi_from(first); doi = ds[0] if ds else ""
    ym = re.search(r"\b(?:19\d{2}|20[0-2]\d)\b", first[:9000]); year = ym.group(0) if ym else ""
    if path.name in FIXES: title, year = FIXES[path.name]
    if path.name == "1-s2.0-S1876610218311299-main.pdf":
        actual = re.search(r"doi\.org/(10\.\d{4,9}/[^\s]+)", "\n".join(pages[:4]), re.I)
        if actual: doi = actual.group(1).rstrip(".,;)").lower()
    return {"file":path.name,"title":title,"year":year,"abstract":abstract,"doi":doi,"all_dois":doi_from("\n".join(pages)),"pages":len(pages),"id":hashlib.sha1(path.name.encode()).hexdigest()[:12]}

def tags_for(p):
    text=p["title"]+" "+p["abstract"]
    return [k for k,v in TAXONOMY.items() if re.search(v,text,re.I)] or ["lightweight-concrete"]

def build(pdf_dir):
    pdfs=sorted(pdf_dir.glob("*.pdf"),key=lambda p:p.name.casefold())
    with ThreadPoolExecutor(max_workers=4) as pool: papers=list(pool.map(read_pdf,pdfs))
    used=set()
    for p in papers:
        p["slug"]=slugify(Path(p["file"]).stem)
        if p["slug"] in used: p["slug"] += "-"+p["id"][:5]
        used.add(p["slug"]); p["tags"]=tags_for(p)
    links=set()
    for i,a in enumerate(papers):
        for b in papers[i+1:]:
            direct=bool(b["doi"] and b["doi"] in a.get("all_dois",[])) or bool(a["doi"] and a["doi"] in b.get("all_dois",[]))
            if direct:
                links.add(tuple(sorted((a["slug"],b["slug"])))); continue
            shared=set(a["tags"])&set(b["tags"])
            wa={w for w in re.findall(r"[a-z]{4,}",(a["title"]+" "+a["abstract"]).lower()) if w not in STOP}
            wb={w for w in re.findall(r"[a-z]{4,}",(b["title"]+" "+b["abstract"]).lower()) if w not in STOP}
            overlap=wa&wb
            similarity=len(overlap)/max(1,len(wa|wb))
            if shared and len(overlap)>=3 and similarity>=0.08: links.add(tuple(sorted((a["slug"],b["slug"]))))
    neighbors={p["slug"]:[] for p in papers}
    for a,b in links: neighbors[a].append(b); neighbors[b].append(a)
    PAPERS.mkdir(parents=True,exist_ok=True)
    for old in PAPERS.glob("*.md"): old.unlink()
    for p in papers:
        cite=(f"{p['title']} ({p['year']})" if p["year"] else p["title"])+(f". DOI: https://doi.org/{p['doi']}" if p["doi"] else "")
        abstract=html.escape(p["abstract"] or "No abstract could be extracted from the first pages. Open the PDF to read the full text.")
        safe_title=html.escape(p["title"])
        related="\n".join(f"- [[{slug}]]" for slug in neighbors[p["slug"]]) or "- No related papers were identified in this collection."
        md=("---\n"+f"title: {q(p['title'])}\ntype: source_note\nsource: {q('../'+p['file'])}\n"+f"citation: {q(cite)}\ndate: {TODAY}\ntags: ["+", ".join(p["tags"])+"]\n---\n\n"+f"# {safe_title}\n\n## Abstract from PDF\n\n{abstract}\n\n## File information\n\n- File name: "+p["file"]+f"\n- Pages: {p['pages']}\n- Topics were identified automatically from the title and abstract.\n- DOI links found in the PDF and topic-based links are suggestions; check the original paper to verify citations.\n\n## Related papers in this folder\n\n{related}\n")
        (PAPERS/(p["slug"]+".md")).write_text(md,encoding="utf-8")
    SOURCE.mkdir(parents=True,exist_ok=True)
    (SOURCE/"index.md").write_text("# Paper catalog\n\n"+"\n".join(f"- [[{p['slug']}]] — {p['title']} ({p['year'] or 'year unknown'})" for p in papers)+"\n",encoding="utf-8")
    (ROOT/"data"/"papers-source.json").write_text(json.dumps([{k:p[k] for k in ("file","title","year","doi","pages","tags","slug")} for p in papers],ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"pdfs":len(papers),"notes":len(list(PAPERS.glob('*.md'))),"links":len(links),"with_abstract":sum(bool(p['abstract']) for p in papers),"with_doi":sum(bool(p['doi']) for p in papers),"pdf_folder":str(pdf_dir)},ensure_ascii=False))

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--pdf-dir",type=Path,default=DEFAULT_PDF_DIR);build(parser.parse_args().pdf_dir.resolve())
