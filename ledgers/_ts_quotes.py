"""trisotech: evidence audit -- every row's `evidence` string tested against the page it judges.

Writes ledgers/trisotech.quotes.txt: one line per row that fails, plus a summary.

Comparison convention (same as the census's own quotes): whitespace collapsed, curly/straight quotes
and dashes unified, leading/trailing " -|" stripped (the ledger's quote() helper strips them). A row
passes when its evidence is a contiguous substring of the *page's own text* (screen.json `text`) or,
for deck pages, of that deck's published per-slide text (the SlideShare transcript array).
"""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
_spec = importlib.util.spec_from_file_location("deck3", os.path.join(ROOT, "_ts_deck3.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)

SCREEN = {r["slug"]: r for r in json.load(open(os.path.join(RAW, "screen.json"), encoding="utf-8"))}
BY_URL = {r["url"]: r for r in json.load(open(os.path.join(RAW, "screen.json"), encoding="utf-8"))}
DECKKEYS = json.load(open(os.path.join(RAW, "decks.json"), encoding="utf-8"))


def norm(s):
    s = (s or "").replace(" ", " ")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def hay(row):
    sc = BY_URL.get(row.get("url"))
    slug = sc.get("slug") if sc else None
    parts = []
    if sc:
        parts.append(norm(sc.get("text")))
    if slug in DECKKEYS:
        parts.append(norm(" ".join(D.trans(slug))))
    return " || ".join(p for p in parts if p).strip(" |")


rows = [json.loads(l) for l in open(os.path.join(ROOT, "trisotech.jsonl"), encoding="utf-8") if l.strip()]
rows = [r for r in rows if isinstance(r, dict) and "url" in r]

out, fails, checked, nocand = [], 0, 0, 0
for r in rows:
    ev = norm(r.get("evidence"))
    if not ev:
        continue
    checked += 1
    h = hay(r)
    if not h:
        nocand += 1
        out.append("NO-PAGE-TEXT  %s" % r.get("url"))
        continue
    cands = [ev, ev.strip(" -|"), " ".join(ev.split()[1:]), " ".join(ev.split()[:-1])]
    if any(c and c in h for c in cands):
        continue
    # longest verified prefix, for the report
    w = ev.split()
    ok = 0
    for k in range(len(w), 0, -1):
        if " ".join(w[:k]) in h:
            ok = k
            break
    fails += 1
    out.append("FAIL (%d/%d words verbatim) %s :: %s" % (ok, len(w), r.get("url"), ev[:160]))

with open(os.path.join(ROOT, "trisotech.quotes.txt"), "w", encoding="utf-8") as fh:
    fh.write("trisotech evidence audit -- %d rows with evidence, %d failures, %d rows with no page text\n"
             % (checked, fails, nocand))
    fh.write("=" * 100 + "\n")
    fh.write("\n".join(out) + ("\n" if out else ""))
print("checked %d rows with evidence: %d failures, %d rows with no page text to test against"
      % (checked, fails, nocand))
for line in out[:20]:
    print("  " + line[:160])
