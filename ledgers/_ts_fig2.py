"""trisotech: the figure pass -- compact inventory + legible per-page sheets.

  python ledgers/_ts_fig2.py todo            -- list the pages still to judge in the figure pass
  python ledgers/_ts_fig2.py dump [slug...]  -- text inventory: figures per page, ranked diagram-likely first
  python ledgers/_ts_fig2.py sheet  slug...  -- legible 2-per-row sheet of a page's own images
"""
import json, os, re, sys
from PIL import Image, ImageDraw

import _ts_figs as F
import _ts_rows as R

RAW = F.RAW
FIGS = F.FIGS
OUT = os.path.join(RAW, "fig2")
C = json.load(open(os.path.join(RAW, "content.json"), encoding="utf-8"))

DIAG = re.compile(r"(process|model|diagram|dmn|bpmn|cmmn|decision|drd|bkm|flow|workflow|gateway|"
                  r"lane|pool|chart|fig|figure|agent|graph|architect|journey|map|blueprint|"
                  r"scenario|example|steps|screen|dash)", re.I)
PHOTO = re.compile(r"(photo|portrait|headshot|people|team|event|conference|speaker|booth|audience|"
                   r"stock|person|award|winner|group)", re.I)


def todo():
    last = {}
    for ln in open(os.path.join(RAW, "dispositions.jsonl"), encoding="utf-8"):
        r = json.loads(ln)
        last[r["key"]] = r
    sc = json.load(open(os.path.join(RAW, "screen.json"), encoding="utf-8"))
    out = []
    for r in sc:
        if r["family"] != "content" or r["slug"] in last:
            continue
        if R.INDEXY.search("https://www.trisotech.com/" + r["slug"].replace("__", "/") + "/"):
            continue
        t = (C.get(r["slug"]) or {}).get("text") or ""
        if R.AI.findall(t):
            out.append((r["bucket"], r["slug"]))
    return out


def imgs(page):
    seq = [x for x in F.own_urls() if x["page"] == page]
    keep = [x for x in seq if not F.FURN.search(x["url"])]
    def rank(x):
        s = 0
        if DIAG.search(x["url"]) or DIAG.search(x["alt"]):
            s -= 3
        if PHOTO.search(x["url"]) or PHOTO.search(x["alt"]):
            s += 3
        if x["url"].lower().endswith(".png"):
            s -= 1
        s -= min((x["w"] * x["h"]) / 400000.0, 3)
        return s
    return sorted(keep, key=rank), [x for x in seq if F.FURN.search(x["url"])]


def dump(pages):
    for page in pages:
        v = C.get(page) or {}
        keep, drop = imgs(page)
        t = v.get("text") or ""
        sents = [" ".join(s.split()) for s in re.split(r"(?<=[.!?])\s+", t)
                 if R.AI.search(s) and 30 <= len(s) <= 320][:3]
        print("\n=== %s  (imgs %d keep / %d furniture, text %d ch)" % (page, len(keep), len(drop), len(t)))
        print("    title: %s" % (v.get("title") or "")[:110])
        for s in sents:
            print("    ai: %s" % s[:190])
        for i, x in enumerate(keep, 1):
            flag = "MODEL?" if (DIAG.search(x["url"]) or DIAG.search(x["alt"])) else "       "
            print("    %s k%-2d %5dx%-5d %s |alt: %s" % (flag, i, x["w"], x["h"],
                  x["url"].rsplit("/", 1)[-1][:46], x["alt"][:60]))
        for i, x in enumerate(drop, 1):
            print("     furn f%-2d %5dx%-5d %s |alt: %s" % (i, x["w"], x["h"],
                  x["url"].rsplit("/", 1)[-1][:46], x["alt"][:60]))


def sheet(pages, width=740, maxh=520, cols=2, per=6, furn=False, skip=0):
    """Legible contact sheet(s) per page. Chunks of `per` images; k-index labels continue across sheets."""
    os.makedirs(OUT, exist_ok=True)
    for page in pages:
        keep, drop = imgs(page)
        group = keep + drop if furn else keep
        group = group[skip:skip + per]
        tiles = []
        for x in group:
            p = os.path.join(FIGS, F.local(x["url"]))
            if not os.path.exists(p) or os.path.getsize(p) < 300:
                continue
            try:
                tiles.append((x, Image.open(p).convert("RGB")))
            except Exception:
                pass
        if not tiles:
            print("  %s: no image on disk" % page)
            continue
        rows = (len(tiles) + cols - 1) // cols
        sh = Image.new("RGB", (cols * width, rows * (maxh + 34)), "white")
        dr = ImageDraw.Draw(sh)
        for k, (x, im) in enumerate(tiles):
            sc = min((width - 8) / max(im.width, 1), (maxh - 8) / max(im.height, 1), 2.0)
            im2 = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))))
            px = (k % cols) * width + 4
            py = (k // cols) * (maxh + 34) + 26
            sh.paste(im2, (px, py))
            dr.text((px, py - 24), "k%d  %dx%d" % (k + 1, im.width, im.height), fill="black")
            dr.text((px, py - 13), x["url"].rsplit("/", 1)[-1][:52], fill="black")
        name = "%s%s.png" % (page[:62], "__f" if furn else "")
        sh.save(os.path.join(OUT, name))
        print("  %-64s %d tiles  %dx%d" % (name, len(tiles), sh.width, sh.height))


PLAN = [
    ("decision-orchestration-with-agentic-ai", dict(width=740, cols=2, per=6)),
    ("dmn-meet-machine-learning", dict(width=740, cols=2, per=6)),
    ("modeling-virus-transmission-on-an-airplane", dict(width=740, cols=2, per=6)),
    ("covid-19", dict(width=420, cols=4, maxh=330, per=12)),
    ("governed-agentic-orchestration", dict(width=740, cols=2, per=6, furn=True)),
    ("discovering-processes-in-unusual-places", dict(width=740, cols=2, per=6, furn=True)),
    ("better-process-analysis-using-analytical-techniques", dict(width=740, cols=2, per=6)),
    ("digital-automation-suite", dict(width=740, cols=2, per=6)),
    ("the-case-for-a-business-automation-center-of-excellence", dict(width=740, cols=2, per=6)),
    ("healthcare-feature-set", dict(width=740, cols=2, per=6, furn=True)),
    ("the-changing-nature-of-work", dict(width=420, cols=4, maxh=330, per=12)),
    ("index", dict(width=740, cols=2, per=6)),
]


def sweep(pages, width=340, maxh=280, cols=4, per_page=2, batch=16):
    """One sheet per `batch` tiles: up to `per_page` images per page (furniture included), so a
    diagram cannot hide behind the filename heuristic. Page label on every tile."""
    os.makedirs(OUT, exist_ok=True)
    tiles = []
    for page in pages:
        keep, drop = imgs(page)
        for x in (keep + drop)[:per_page]:
            p = os.path.join(FIGS, F.local(x["url"]))
            if not os.path.exists(p) or os.path.getsize(p) < 250:
                continue
            try:
                tiles.append((page, x, Image.open(p).convert("RGB")))
            except Exception:
                pass
    for b, off in enumerate(range(0, len(tiles), batch), 1):
        chunk = tiles[off:off + batch]
        rows = (len(chunk) + cols - 1) // cols
        sh = Image.new("RGB", (cols * width, rows * (maxh + 34)), "white")
        dr = ImageDraw.Draw(sh)
        for k, (page, x, im) in enumerate(chunk):
            sc = min((width - 8) / max(im.width, 1), (maxh - 8) / max(im.height, 1), 2.0)
            im2 = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))))
            px = (k % cols) * width + 4
            py = (k // cols) * (maxh + 34) + 26
            sh.paste(im2, (px, py))
            dr.text((px, py - 24), "%s" % page[:44], fill="black")
            dr.text((px, py - 13), "%dx%d %s" % (im.width, im.height,
                                                 x["url"].rsplit("/", 1)[-1][:34]), fill="black")
        name = "sweep%02d.png" % b
        sh.save(os.path.join(OUT, name))
        print("  %-16s %d tiles  %dx%d" % (name, len(chunk), sh.width, sh.height))


def plan():
    return [p for p, _ in PLAN]


def plan_sheets():
    for p, kw in PLAN:
        sheet([p], **kw)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if cmd == "todo":
        for b, s in todo():
            print("%-8s %s" % (b, s))
    elif cmd == "dump":
        dump(sys.argv[2:] or [s for _, s in todo()])
    elif cmd == "sheet":
        sheet(sys.argv[2:])
    elif cmd == "plan":
        plan_sheets()
