"""Pass 2 statistics for report.md: per-source outcomes, processing-mode classification, disk inventory."""
import json, glob, os, re, collections
from pathlib import Path
ELI = Path(__file__).resolve().parents[2]
L = ELI / "ledgers"

NATIVE = re.compile(r"native(-resolution)? read|full[- ]?size|full[- ]resolution|at native|one image per call|eye ruling|"
                    r"eye examination|eye census|read by eye|by eye(?!\))|opened the asset and read|viewed every|"
                    r"figure viewed(?!: no figure)|opened the export|looked at|read the (png|figure|image|diagram)", re.I)
STRONG = re.compile(r"native(-resolution)? read|full[- ]?size|full[- ]resolution|at native|one image per call|native resolution", re.I)
SHEET = re.compile(r"contact[- ]?sheet|sheet-900|sheets?|tiles?|tiled|montage", re.I)
NEG = re.compile(r"no figure opened|figures not opened|not opened|cell class None|^none|^no figure|no figures on the page|"
                 r"the page has no figure|zero figures", re.I)
# visual-progress logs: which kind of look they record
VP_KIND = {"flowable": "native", "camunda-docs-blog": "native", "flowx-ai": "sheet"}

def load(slug):
    rows, header = {}, None
    for l in open(L / f"{slug}.jsonl", encoding="utf-8"):
        l = l.strip()
        if not l: continue
        r = json.loads(l)
        if r.get("type") == "header": header = r
        if "n" in r: rows[r["n"]] = r
    return header, rows

def vp_sets(slug):
    s = set()
    pats = [str(L / f"{slug}.raw" / "**" / "visual-progress*.jsonl"), str(L / f"{slug}.raw" / "shards" / "*.progress.jsonl*")]
    for pat in pats:
        for f in glob.glob(pat, recursive=True):
            for l in open(f, encoding="utf-8", errors="replace"):
                try: d = json.loads(l)
                except Exception: continue
                n = d.get("n")
                if isinstance(n, int): s.add(n)
    return s

def look(field):
    s = str(field or "").strip()
    if not s or s == "None" or NEG.search(s): return None
    if STRONG.search(s): return "strong"
    if SHEET.search(s): return "sheet"
    if NATIVE.search(s): return "weak"
    return None

def mode(r, vp, slug):
    kinds = []
    if r["n"] in vp: kinds.append(VP_KIND.get(slug, "native"))
    for k in ("judged_from", "figures_looked_at", "seen", "figure_note", "note", "figure_evidence"):
        kinds.append(look(r.get(k)))
    if r.get("visual_evidence"): kinds.append("strong")
    if "strong" in kinds or "native" in kinds: return "agent-visual-native"
    if "sheet" in kinds: return "agent-visual-sheet"
    if "weak" in kinds: return "agent-visual-native"
    if r.get("verdict") == "BLOCKED": return "blocked"
    if r.get("verdict") == "EXCLUDE" and r.get("judgment") is False: return "script"
    return "agent-text"

out = {}
for f in sorted(L.glob("*.jsonl")):
    slug = f.stem
    header, rows = load(slug)
    vp = vp_sets(slug)
    v = collections.Counter(r.get("verdict") for r in rows.values())
    codes = collections.Counter(r.get("reason") for r in rows.values() if r.get("verdict") == "EXCLUDE")
    m = collections.Counter(mode(r, vp, slug) for r in rows.values())
    je = sum(1 for r in rows.values() if r.get("verdict") == "EXCLUDE" and r.get("judgment") is True)
    recs = len(list((ELI / "corpus" / slug).glob("[0-9][0-9][0-9]_*.md"))) if (ELI / "corpus" / slug).exists() else 0
    # disk inventory
    inv = collections.Counter(); size = 0
    for root in [L / f"{slug}.raw", ELI / "corpus" / slug]:
        if not root.exists(): continue
        for p in root.rglob("*"):
            if not p.is_file() or "__pycache__" in p.parts: continue
            ext = p.suffix.lower(); size += p.stat().st_size
            name = p.name.lower()
            if "sheet" in name or "sheet" in str(p.parent).lower() or name.startswith("batch_") or "montage" in name: k = "contact-sheet"
            elif ext in (".html", ".htm", ".md") and root.name != slug: k = "page"
            elif ext in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif", ".image", ".bmp"): k = "image"
            elif ext in (".bpmn", ".dmn", ".cmmn", ".xml", ".bpmn2"): k = "model-xml"
            elif ext in (".pdf", ".pptx"): k = "document"
            elif ext == ".md": k = "record"
            elif ext == ".py": k = "script"
            else: k = "other"
            inv[k] += 1
    out[slug] = dict(population=(header or {}).get("population_size"), rows=len(rows), verdicts=dict(v), codes=dict(codes),
                     modes=dict(m), judgement_exclusions=je, records=recs,
                     rulings=sum(1 for r in rows.values() if r.get("needs_human_ruling")),
                     visual_checks=sum(1 for r in rows.values() if r.get("needs_visual_check")),
                     vp_entries=len(vp), disk=dict(inv), bytes=size)
json.dump(out, open(L / "_report" / "pass2_stats.json", "w", encoding="utf-8"), indent=1)
T = collections.Counter(); M = collections.Counter(); D = collections.Counter(); B = 0
for s, d in out.items():
    T.update(d["verdicts"]); M.update(d["modes"]); D.update(d["disk"]); B += d["bytes"]
    print(f"{s:24} rows={d['rows']:5} pop={d['population']} {d['verdicts']} modes={d['modes']} rec={d['records']} disk={d['disk']}")
print("TOTAL", sum(d["rows"] for d in out.values()), dict(T), dict(M), dict(D), round(B/1e9,2), "GB")
