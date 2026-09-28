#!/usr/bin/env python3
"""Per-listing evidence digest for the phase-2 (process-language) marketplace candidates.

For each candidate: its process-language sentence, its AI token contexts (hard vs soft), the
'Business Process Element' tag if present, and its figures - split into those the contact sheets
actually showed (non-noise, i.e. present in mp_figsel.json) and those the noise filter dropped.
The noise-dropped ones are named too, so a ruling never claims to have seen a logo it did not.

  python ledgers/_creatio_mp_digest.py > ledgers/_creatio/mp_digest.txt
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
sys.path.insert(0, str(ELI / "ledgers"))
import _creatio_mp_rows as M  # noqa: E402

items = json.loads((OUT / "mp_items.json").read_text(encoding="utf-8"))["items"]
pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
blog = json.loads((OUT / "mp_blog_index.json").read_text(encoding="utf-8"))["articles"]
bp = json.loads((OUT / "mp_blog_pages.json").read_text(encoding="utf-8"))
figctx = json.loads((OUT / "mp_figctx.json").read_text(encoding="utf-8"))
sel = json.loads((OUT / "mp_figsel.json").read_text(encoding="utf-8"))
shown = {}
for e in sel:
    shown.setdefault(e["link"], {})[e["file"]] = e.get("heading")


def sents(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s", re.sub(r"\s+", " ", t)) if len(s.split()) >= 5]


def main():
    census = [("app", i["link"]) for i in items] + [("blog", b) for b in blog]
    for kind, link in census:
        p = (pages if kind == "app" else bp).get(link) or {}
        if p.get("status") != "ok":
            continue
        hay = M.hay_of(p)
        if not M.EYES.search(hay):
            continue
        b = M.body(p)
        print("=" * 4, link)
        print("   TITLE:", p["title"].replace(" | Creatio Marketplace", ""))
        proc = [s for s in sents(b) if re.search(M.PROC, s, re.I)][:3]
        for s in proc:
            print("   PROC:", " ".join(s.split()[:26]))
        hit_a = [m.group(0) for m in re.finditer(M.AI, b, re.I)]
        hit_s = [m.group(0) for m in re.finditer(M.SOFT, b, re.I)]
        print("   AI-in-body: %s | SOFT-in-body: %s" % (sorted(set(hit_a))[:6] or "none",
                                                        sorted(set(hit_s))[:6] or "none"))
        for m in list(re.finditer(M.AI, b, re.I))[:2]:
            print("      ctx:", re.sub(r"\s+", " ", b[max(0, m.start() - 60):m.start() + 60]))
        for m in list(re.finditer(M.SOFT, b, re.I))[:2]:
            print("      soft:", re.sub(r"\s+", " ", b[max(0, m.start() - 60):m.start() + 60]))
        print("   TAG-BPE:", bool(re.search(M.TAG_BPE, b)),
              "| TAG-AIWorkflow:", bool(re.search(r"AI Workflow", b)),
              "| AI-in-figurename/alt:", bool(re.search(M.AI, " ".join(
                  [(i.get("alt") or "") + " " + i["src"].split("/")[-1] for i in M.figs(p)]), re.I)))
        sel_names = shown.get(link, {})
        names = [(i["src"].split("/")[-1].replace("%2520", " ").replace("%20", " ").replace("%2B", "+"))
                 for i in M.figs(p)]
        print("   FIGS shown(%d): %s" % (
            len(sel_names),
            "; ".join("%s@%s" % (f[:34], h or "") for f, h in list(sel_names.items())[:12])))
        rest = [n for n in names if n not in sel_names and
                n.replace(" ", "%20") not in sel_names]
        print("   FIGS noise(%d): %s" % (len(names) - len(sel_names), "; ".join(rest[:8])))
        fc = figctx.get(link) or []
        if fc:
            print("   FIGCTX-ai: %s" % "; ".join(
                (f["file"][:30] + "|" + (f["heading"] or "")) for f in fc
                if re.search(M.AI, (f["file"] + " " + (f["alt"] or "") + " " + (f["heading"] or "")), re.I))[:200])
        print()


if __name__ == "__main__":
    main()
