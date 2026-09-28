#!/usr/bin/env python3
"""Download the figures I must actually look at on the Creatio Academy and build contact sheets.

Two selections, both driven by ledgers/_creatio/articles.json (the <article> region only):

  A. every page whose article text carries an AI/LLM keyword AND publishes figures - these are
     the pages a ruling has to be written for (verdict INCLUDE / UNCERTAIN / E2), so the figure
     the ruling is about has to be seen, not guessed;
  B. every in-scope page under /bpm-tools/ that publishes figures and carries no AI keyword -
     here the only open question is the notation of the figure (BPMN -> E2, something else -> E1).

Figures are downloaded at ~1 request/second to ledgers/_creatio/figs/ and tiled into 6x5 contact
sheets (ledgers/_creatio/sheet_*.png) with an index (figs_index.json: sheet, cell, page, src).

  python ledgers/_creatio_figs.py --download   # fetch + tile
"""
import json
import pathlib
import re
import sys
import time
import urllib.request

from PIL import Image

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
FIGS = OUT / "figs"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128 Safari/537.36")
SCOPE = ("/guides/no-code-customization/", "/guides/ai-studio/", "/guides/ai-development/")
CHROME = re.compile(
    r"(/img/logo|/img/creatio|favicon|/icons?/|[-_/]icon|icon[-_.]|logo|bullet|/nav|_nav|note\."
    r"|caution|warning|arrow|expand|collapse|checkmark|sprite|spacer|blank|1x1|youtube\.com|"
    r"\.svg($|\?)|scr_ai_twin_nav|/footer)", re.I)
COLW, ROWH, THUMB = 6, 5, 250


def slug(path):
    return re.sub(r"[^A-Za-z0-9._-]", "_", path.strip("/"))[:150]


def rel(fname):
    """/guides/no-code-customization/ai-tools/... from the cached filename."""
    return "/" + fname[:-5].replace("_", "/")


def in_scope(fname):
    return any(fname.startswith(slug(p)) for p in SCOPE)


def pick(fname, v):
    figs = [i for i in v["imgs"] if not CHROME.search(i["src"])]
    if not figs:
        return []
    limit = 3 if v["kw"] else 2
    return figs[:limit]


def main():
    arts = json.loads((OUT / "articles.json").read_text(encoding="utf-8"))
    sel = {}
    for fname, v in arts.items():
        if not v["imgs"]:
            continue
        if v["kw"]:
            sel[fname] = ("ai", pick(fname, v))
        elif in_scope(fname) and "_bpm-tools_" in fname:
            sel[fname] = ("bpm", pick(fname, v))
    sel = {k: (k2, v2) for k, (k2, v2) in sel.items() if v2}

    n_ai = sum(1 for k, v in sel.values() if k == "ai")
    n_bpm = sum(1 for k, v in sel.values() if k == "bpm")
    print(f"selection: {len(sel)} pages ({n_ai} AI-keyword, {n_bpm} bpm-tools without AI)")

    if "--download" not in sys.argv:
        raise SystemExit("preview only (no --download)")

    FIGS.mkdir(parents=True, exist_ok=True)
    index, files = [], []
    seen_src = {}
    for fname, (kind, figs) in sorted(sel.items()):
        for j, im in enumerate(figs, 1):
            src = im["src"]
            if not src.startswith("http"):
                src = "https://academy.creatio.com" + ("" if src.startswith("/") else "/") + src
            local = seen_src.get(src)
            if local is None:
                local = FIGS / (slug(fname)[6:90] + f"__{j}" + (pathlib.Path(src).suffix or ".png"))
                if not local.exists():
                    try:
                        req = urllib.request.Request(src, headers={"User-Agent": UA})
                        with urllib.request.urlopen(req, timeout=60) as r:
                            local.write_bytes(r.read())
                        time.sleep(0.9)
                    except Exception as exc:                      # noqa: BLE001
                        print("ERR", src[:100], exc, flush=True)
                        continue
                seen_src[src] = local
            index.append({"file": local.name, "page": rel(fname), "slug": fname, "kind": kind,
                          "src": src, "alt": im.get("alt", ""),
                          "text_after": im.get("text_after", ""),
                          "text_before": im.get("text_before", "")})
            if local.name not in files:
                files.append(local.name)

    # tiles: 6 columns x 5 rows per sheet
    per = COLW * ROWH
    for s in range(0, len(index), per):
        chunk = index[s:s + per]
        sheet = Image.new("RGB", (COLW * THUMB, ROWH * (THUMB + 12)), "white")
        for c, it in enumerate(chunk):
            p = FIGS / it["file"]
            try:
                im = Image.open(p).convert("RGB")
            except Exception:                                     # noqa: BLE001
                continue
            w = THUMB - 6
            h = int(im.height * w / max(1, im.width))
            im = im.resize((w, min(h, THUMB - 6)))
            sheet.paste(im, ((c % COLW) * THUMB + 3, (c // COLW) * (THUMB + 12) + 3))
            it["sheet"] = s // per + 1
            it["cell"] = c + 1
        sheet.save(OUT / f"sheet_{s // per + 1}.png")
    (OUT / "figs_index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False),
                                         encoding="utf-8")
    print(f"figures downloaded: {len(index)}  sheets: {(len(index) + per - 1) // per}"
          f"  pages covered: {len(sel)}")


if __name__ == "__main__":
    main()
