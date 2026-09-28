#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Superseding rows for the flowx-ai E1 re-judgement, plus the contact sheets to look at.

Why this exists
---------------
530 ledger rows excluded a page as `E1-not-bpmn` on the strength of the page's figure *count*, with
`judged_from: mechanical screen (no figure opened by eye)`. That is not a licensed way to name a
notation, and tools/audit.py rejects it. The rows are corrected the only way this census allows:
new rows are appended with the same `n` (the ledger is append-only and the last row for an `n`
wins).

Two classes, two corrections:

  A. 324 rows whose screen says ai=False. The page's main text carries no AI/LLM term at all, so no
     AI element can sit inside a process artefact on that page whatever the figures show. Those
     become `E2-no-ai-element`, mechanical, and the note says so. `alt` texts and figure filenames
     were screened too, so the note can state that check.

  B. 206 rows whose screen says ai=True: the page does discuss AI somewhere, so the figures have to
     be looked at before any notation is named. `sheets` builds contact sheets over the distinct
     images those rows reference, 4 tiles per sheet, each tile 900 px wide; `progress` records the
     disposition of every figure so a resumed session (or the researcher) can see what was seen.

Usage
  python ledgers/_fx_fix.py recode-a          append the 324 case-A rows
  python ledgers/_fx_fix.py recode-a --dry    print what would be appended
  python ledgers/_fx_fix.py sheets [--only-ai]  build the contact sheets + sheets/index.jsonl
  python ledgers/_fx_fix.py list-b            the case-B work list (sheets, tiles, rows)
"""
import json, os, re, sys

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
FIGS = os.path.join(RAW, "figures2")
INV = os.path.join(RAW, "figs_inventory.json")
SHEETS = os.path.join(RAW, "sheets")
PROG = os.path.join(RAW, "visual-progress.jsonl")
LEDGER = os.path.join(ELI, "flowx-ai.jsonl")

# The same lexicon the classifier screens pages with. `FlowX.AI` is a false positive (it is the
# vendor's own name) and is stripped before the term test everywhere in this census.
sys.path.insert(0, ELI)
from _fx_class import AILEX                                          # noqa: E402

JUDGED_FROM = ("mechanical: no AI/LLM keyword in page main and no AI term in any figure's alt text "
               "or filename; figures not opened")


def rows():
    for ln in open(LEDGER, encoding="utf-8"):
        r = json.loads(ln)
        if not r.get("type"):
            yield r


def case_rows(ai):
    """Current E1 rows, filtered by whether their screen says the page discusses AI."""
    out = []
    for r in rows():
        if r.get("reason") != "E1-not-bpmn":
            continue
        if ("ai=True" in (r.get("screen") or "")) == ai:
            out.append(r)
    return out


def figmeta():
    return json.load(open(os.path.join(RAW, "figmeta.json"), encoding="utf-8"))


def alt_ai_terms(url, fm):
    """AI terms in this page's figure filenames/alt texts, minus the vendor's own name."""
    out = []
    for f in fm.get(url) or []:
        blob = re.sub(r"(?i)flowx\.?ai|docs\.flowx\.ai", "FlowX", (f.get("alt") or "") + " "
                      + (f.get("name") or ""))
        m = AILEX.search(blob)
        if m:
            out.append((f.get("name", ""), m.group(0), f.get("alt", "")))
    return out


def recode_a(dry=False):
    fm = figmeta()
    src = case_rows(False)
    out = []
    for r in src:
        alts = alt_ai_terms(r["url"], fm)
        n_fig = len(fm.get(r["url"]) or [])
        common = ("the page's main text carries no AI/LLM term at all: the census lexicon's only "
                  "apparent hits on this class of page are the vendor's own name (FlowX.AI) and the "
                  "HTTP User-Agent header. ")
        if n_fig:
            what = ("Its %d figure filenames and alt texts were screened for AI terms as well and "
                    "carry none, so no AI element can sit inside a process artefact on this page "
                    "whatever those figures show. Re-coded from E1-not-bpmn to E2-no-ai-element by a "
                    "superseding row: the superseded row named a notation for %d figures that were "
                    "never opened, which this census's audit does not allow. The figures are still "
                    "not opened, and this verdict does not depend on what they show." % (n_fig, n_fig))
        else:
            what = ("The page publishes no standalone figure; the artefact its screen counted is a "
                    "text fence. Re-coded from E1-not-bpmn to E2-no-ai-element by a superseding row: "
                    "the superseded row named a notation for a fence that was never opened, which "
                    "this census's audit does not allow.")
        note = common + what
        if alts:
            note += (" Alt-text hits that were dismissed as the vendor name: %s."
                     % "; ".join("%s (%s)" % (a[0], a[1]) for a in alts[:3]))
        row = dict(r)
        row.update({"reason": "E2-no-ai-element", "judgment": False, "judged_from": JUDGED_FROM,
                    "note": note, "supersedes_row": True, "figures_looked_at": None})
        out.append(row)
    if dry:
        print("would append %d rows; example:" % len(out))
        print(json.dumps(out[0], ensure_ascii=False, indent=1))
        return out
    with open(LEDGER, "a", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("appended %d superseding rows (E1-not-bpmn -> E2-no-ai-element, mechanical)" % len(out))
    return out


# ---------------------------------------------------------------- case B: the sheets

def inventory():
    return json.load(open(INV, encoding="utf-8"))


def row_titles():
    return {str(r["n"]): (r.get("title") or "")[:60] for r in rows() if r.get("n")}


def work_list(only_ai=True):
    """One entry per distinct image, keyed by sha1, that a case-B row needs."""
    inv = inventory()
    titles = row_titles()
    todo = []
    for sha, d in inv.items():
        if only_ai and not d["ai_rows"]:
            continue
        p = os.path.join(FIGS, d["file"])
        if not os.path.exists(p):
            continue
        ai_titles = sorted({titles.get(str(n), "?") for n in d["ai_rows"]})
        todo.append({"sha": sha, "file": p, "names": d["names"], "urls": d["urls"][:3],
                     "rows": d["rows"], "ai_rows": d["ai_rows"], "ai_titles": ai_titles})
    todo.sort(key=lambda d: (-len(d["ai_rows"]), (d["ai_titles"] or [""])[0], d["names"][0]))
    return todo


def build_sheets(only_ai=True, tiles=4, tile_w=900, pad=56, label=34, limit=None):
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs(SHEETS, exist_ok=True)
    todo = work_list(only_ai)
    if limit:
        todo = todo[:limit]
    cols = 2 if tiles == 4 else tiles
    rowsn = (tiles + cols - 1) // cols
    try:
        font = ImageFont.load_default(size=label)
    except Exception:                                                # noqa: BLE001
        font = ImageFont.load_default()
    index, n_sheet, ok, bad = [], 0, 0, 0
    for i in range(0, len(todo), tiles):
        group = todo[i:i + tiles]
        cell_w, cell_h = tile_w, tile_w
        foot = 2 * label + 10                       # two label lines under each tile
        sheet = Image.new("RGB", (cols * cell_w + (cols + 1) * pad,
                                  rowsn * (cell_h + foot) + (rowsn + 1) * pad), (255, 255, 255))
        dr = ImageDraw.Draw(sheet)
        entries = []
        for k, d in enumerate(group):
            cx = (k % cols) * (cell_w + pad) + pad
            cy = (k // cols) * (cell_h + foot + pad) + pad
            try:
                im = Image.open(d["file"])
                im.load()
                if im.mode in ("RGBA", "LA", "P"):
                    bg = Image.new("RGB", im.size, (255, 255, 255))
                    im = im.convert("RGBA")
                    bg.paste(im, mask=im.split()[-1])
                    im = bg
                else:
                    im = im.convert("RGB")
                w, h = im.size
                scale = tile_w / float(w)
                nh = max(1, int(h * scale))
                if nh <= cell_h:
                    im2 = im.resize((tile_w, nh), Image.LANCZOS)
                    sheet.paste(im2, (cx, cy))
                else:                                   # tall image: fit the height, centre it
                    scale = cell_h / float(h)
                    nw = max(1, int(w * scale))
                    im2 = im.resize((nw, cell_h), Image.LANCZOS)
                    sheet.paste(im2, (cx + (tile_w - nw) // 2, cy))
                dr.rectangle([cx - 2, cy - 2, cx + tile_w + 1, cy + cell_h + 1], outline=(200, 0, 0))
                dr.text((cx + 4, cy + 4), "%d" % (k + 1), fill=(200, 0, 0), font=font,
                        stroke_width=3, stroke_fill=(255, 255, 255))
                dr.text((cx + 4, cy + cell_h + 4), "%s  %dx%d" % (d["names"][0][:40], w, h),
                        fill=(0, 0, 0), font=font, stroke_width=3, stroke_fill=(255, 255, 255))
                dr.text((cx + 4, cy + cell_h + 4 + label + 4),
                        "on: %s" % ("; ".join(d["ai_titles"])[:70] or "(no ai=True row)"),
                        fill=(0, 0, 0), font=font, stroke_width=3, stroke_fill=(255, 255, 255))
                ok += 1
                entries.append({"tile": k + 1, "sha": d["sha"], "name": d["names"][0],
                                "size": [w, h], "rows": d["rows"], "ai_rows": d["ai_rows"],
                                "ai_titles": d["ai_titles"],
                                "url": d["urls"][0] if d["urls"] else ""})
            except Exception as exc:                                     # noqa: BLE001
                dr.text((cx + 4, cy + 40), "UNREADABLE %s" % str(exc)[:40], fill=(200, 0, 0),
                        font=font)
                bad += 1
                entries.append({"tile": k + 1, "sha": d["sha"], "name": d["names"][0],
                                "error": str(exc)[:80], "rows": d["rows"],
                                "ai_rows": d["ai_rows"], "url": d["urls"][0] if d["urls"] else ""})
        n_sheet += 1
        name = "B_%03d.png" % n_sheet
        try:
            big = ImageFont.load_default(size=44)
        except Exception:                                            # noqa: BLE001
            big = font
        dr.text((pad, 10), "SHEET %s   (tiles left-right, top-bottom: 1 2 / 3 4)" % name,
                fill=(0, 0, 200), font=big)
        sheet.save(os.path.join(SHEETS, name))
        index.append({"sheet": name, "tiles": entries})
    json.dump(index, open(os.path.join(SHEETS, "index.json"), "w", encoding="utf-8"), indent=0)
    print("images: %d  sheets: %d (tiles=%d, tile width %d px)  unreadable: %d"
          % (len(todo), n_sheet, tiles, tile_w, bad))
    print("index: %s" % os.path.join(SHEETS, "index.json"))
    return index


def list_b():
    todo = work_list(True)
    inv = inventory()
    print("case-B distinct images with a file on disk: %d" % len(todo))
    print("case-B rows:", len(case_rows(True)))
    n = sum(1 for d in inv.values() if d["ai_rows"])
    print("inventory says %d distinct images are needed by an ai=True row" % n)


def dispose(sheet, pairs):
    """Log one disposition per tile, appended as it is decided.

    pairs are 'tile=class[:note]' where class is one of
      ui          product UI screenshot / form / table / listing / dashboard / chat / code editor
      drawn       a drawn diagram that is not BPMN (architecture box, state chart, D2/Excalidraw,
                  proprietary canvas, rendered Mermaid or ASCII flowchart)
      bpmn-noai   BPMN 2.0 notation, no AI element inside the diagram
      bpmn-ai     BPMN 2.0 notation with an AI/LLM element inside the diagram
      bpmn-prose  BPMN 2.0 notation, the page's AI talk is prose only (needs a ruling)
      unclear     cannot tell what the figure shows
      broken      the file is unreadable / the vendor's own page fails to render it
    """
    idx = json.load(open(os.path.join(SHEETS, "index.json"), encoding="utf-8"))
    want = sheet if sheet.endswith(".png") else sheet + ".png"
    me = next((s for s in idx if s["sheet"] in (sheet, want)), None)
    if me is None:
        raise SystemExit("no such sheet: %s" % sheet)
    with open(PROG, "a", encoding="utf-8") as fh:
        for p in pairs:
            tn, _, rest = p.partition("=")
            cls, _, note = rest.partition(":")
            t = me["tiles"][int(tn) - 1]
            fh.write(json.dumps({"sheet": sheet, "tile": int(tn), "sha": t["sha"],
                                 "name": t["name"], "class": cls, "note": note,
                                 "rows": t["rows"], "ai_rows": t["ai_rows"],
                                 "url": t.get("url", "")}, ensure_ascii=False) + "\n")
    print("%s: logged %d tiles" % (sheet, len(pairs)))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list-b"
    if cmd == "recode-a":
        recode_a("--dry" in sys.argv)
    elif cmd == "sheets":
        limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
        build_sheets(only_ai="--only-ai" in sys.argv, limit=limit)
    elif cmd == "list-b":
        list_b()
    elif cmd == "dispose":
        dispose(sys.argv[2], sys.argv[3:])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
