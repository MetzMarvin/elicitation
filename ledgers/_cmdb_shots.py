"""camunda-docs-blog: fetch post figures and build contact sheets for the visual pass.

  python ledgers/_cmdb_shots.py fetch        # download the selected figures (resumable)
  python ledgers/_cmdb_shots.py sheets       # sheets of 48 figures, in post order
  python ledgers/_cmdb_shots.py show N [N..] # list the selected figures of those posts
  python ledgers/_cmdb_shots.py one N K      # download one figure full width (for a record)

Selection: for a post with an AI/LLM term in its text, the three most informative figures
(diagram-like alt text first, then largest); otherwise the single most informative figure.
Images come from the Sanity CDN at reduced width, so the sheets stay small.
"""
import html, json, os, re, subprocess, sys

from PIL import Image, ImageDraw

import _cmdb_figs as F

RAW = "ledgers/camunda-docs-blog.raw"
IMGS = os.path.join(RAW, "imgs")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/140.0.0.0 Safari/537.36")


def selected(r):
    """Figures to look at. Every post that shows a figure gets one cell in the sheets, so the
    BPMN / not-BPMN call on each post is a visual one; a post with an AI/LLM term in its text
    gets a second, and a post with a downloadable model is handled from the XML itself."""
    fs = F.figs(r)
    if not fs:
        return []
    fs.sort(key=lambda f: (0 if F.DIAG.search(f["alt"]) else 1, -f["w"] * f["h"]))
    return fs[:2] if (r.get("n_ai") or r["files"]) else fs[:1]


def priority(r):
    return bool(F.figs(r)) or bool(r["files"])


def path_for(n, k):
    return os.path.join(IMGS, "%04d_%d.jpg" % (n, k))


def get(url, path, width):
    sep = "&" if "?" in url else "?"
    subprocess.run(["curl", "-s", "-m", "30", "-A", UA, "-o", path,
                    "%s%sw=%d&q=75" % (url, sep, width)], capture_output=True)


def fetch(width=340, workers=3):
    os.makedirs(IMGS, exist_ok=True)
    todo = []
    for r in F.rows():
        if r["n"] > 1435:
            continue
        for k, f in enumerate(selected(r), 1):
            p = path_for(r["n"], k)
            if not (os.path.exists(p) and os.path.getsize(p) > 800):
                todo.append((f["src"], p))
    print("to fetch", len(todo), flush=True)
    from concurrent.futures import ThreadPoolExecutor
    def one(job):
        get(job[0], job[1], width)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for i, _ in enumerate(ex.map(one, todo), 1):
            if i % 100 == 0:
                print("fetched", i, flush=True)
    print("fetched", len(todo), "images")


def cell(path, w, h):
    if not os.path.exists(path) or os.path.getsize(path) < 400:
        return None
    try:
        im = Image.open(path).convert("RGB")
    except Exception:
        return None
    im.thumbnail((w, h))
    return im


def needs_look(r):
    """Posts whose figure (or lack of a usable alt text) leaves the BPMN call open, so the
    call has to be a visual one: a diagram-like alt text anywhere, or an AI/LLM term in the
    text / a downloadable model, or no alt text at all."""
    fs = F.figs(r)
    if not fs:
        return False
    if any(F.DIAG.search(f["alt"]) for f in fs):
        return True
    if r.get("n_ai") or r["files"]:
        return True
    return not any(f["alt"] for f in fs)


def looked():
    """Post numbers that already have a line in a visual report (viz/report_*.txt)."""
    import glob
    seen = set()
    for p in glob.glob(os.path.join(RAW, "viz", "report_*.txt")):
        for line in open(p, encoding="utf-8", errors="replace"):
            m = re.match(r"\s*(\d+)\.\d+\s*\|", line)
            if m:
                seen.add(int(m.group(1)))
    return seen


def sheets(cols=8, rows_n=6, cw=250, ch=150, only=False, unlooked=False, prefix="figs"):
    """Contact sheets over the selected figures. `only` = the needs_look set; `unlooked` =
    the complement of what a report already covers, so no post's figure is left unjudged."""
    done = looked() if unlooked else set()
    items = []
    for r in F.rows():
        if r["n"] > 1435:
            continue
        if only and not needs_look(r):
            continue
        if unlooked and r["n"] in done:
            continue
        for k, f in enumerate(selected(r), 1):
            if os.path.exists(path_for(r["n"], k)):
                items.append((r["n"], k))
    items.sort()
    per = cols * rows_n
    for i in range(0, len(items), per):
        chunk = items[i:i + per]
        W, H = cols * cw, rows_n * (ch + 16)
        out = Image.new("RGB", (W, H), (255, 255, 255))
        d = ImageDraw.Draw(out)
        for idx, (n, k) in enumerate(chunk):
            cx, cy = (idx % cols) * cw, (idx // cols) * (ch + 16)
            ic = cell(path_for(n, k), cw - 8, ch - 8)
            if ic is not None:
                out.paste(ic, (cx + 4 + (cw - 8 - ic.width) // 2, cy + 4))
            d.rectangle([cx, cy, cx + cw - 1, cy + ch + 14], outline=(190, 190, 190))
            d.text((cx + 4, cy + ch + 1), "%d.%d" % (n, k), fill=(0, 0, 0))
        p = os.path.join(IMGS, "%s_%04d_%04d.png" % (prefix, chunk[0][0], chunk[-1][0]))
        out.save(p)
        print("wrote", os.path.basename(p), "cells", len(chunk))
    if unlooked:
        rows_by = {r["n"]: r for r in F.rows()}
        with open(os.path.join(IMGS, "sheetmap2.txt" if prefix == "figs2" else "sheetmap3.txt"),
                  "w", newline="\n", encoding="utf-8") as fh:
            for i in range(0, len(items), per):
                chunk = items[i:i + per]
                fh.write("### %s_%04d_%04d.png\n" % (prefix, chunk[0][0], chunk[-1][0]))
                for n, k in chunk:
                    r = rows_by[n]
                    f = selected(r)[k - 1]
                    fh.write("  %d.%d  aiflag=%d  alts=%s\n"
                             % (n, k, 1 if (r["n_ai"] or r["files"]) else 0,
                                f["alt"][:90] or "(none)"))
        print("wrote sheetmap2.txt")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "fetch":
        fetch(int(sys.argv[2]) if len(sys.argv) > 2 else 340)
    elif cmd == "sheets":
        sheets(only="-t" in sys.argv)
    elif cmd == "sheets2":
        sheets(unlooked=True, prefix="figs2")
    elif cmd == "show":
        for n in [int(x) for x in sys.argv[2:]]:
            for r in F.rows():
                if r["n"] == n:
                    print("===", n, r["title"], "| ai", r["n_ai"])
                    for k, f in enumerate(selected(r), 1):
                        print("   %d  %4dx%-4d %s | %s" % (k, f["w"], f["h"], f["alt"][:70], f["src"][-34:]))
    elif cmd == "one":
        n, k = int(sys.argv[2]), int(sys.argv[3])
        for r in F.rows():
            if r["n"] == n:
                f = selected(r)[k - 1]
                p = os.path.join(IMGS, "full_%04d_%d.jpg" % (n, k))
                get(f["src"], p, 1400)
                print("wrote", p, f["alt"][:70])
