"""Row-labelled page sheets: one row per page, its figures left to right, the slug drawn large.

`python ledgers/_pm_rowsheet.py OUT.png <pages-per-sheet> <slug> [<slug> ...]`

Why not sheet.py: on a 40-tile sheet the tiles are anonymous, and the caption bar is unreadable
after the Read tool downscales the image, so a tile cannot be attributed to a page. Here each row
is one page and the page's slug is painted across the top of the row at a size that survives the
downscale. Row width is kept under ~1850 px so the sheet comes back at ~0.85 scale.

Tiles are the page's figures in document order, at most 6 per row; a seventh figure wraps to a
second row of the same page, labelled with the figure numbers only.
"""
import os, sys

from PIL import Image, ImageDraw

ELI = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(ELI, "processmaker.raw/figures")
TILEW, PAD, LAB = 300, 8, 26
PER_ROW = 6
MAXH = 240


def load(p):
    im = Image.open(p)
    try:
        im.seek(0)
    except Exception:
        pass
    im = im.convert("RGB")
    w, h = im.size
    th = max(1, int(round(TILEW * h / w)))
    if th > MAXH:                      # keep rows shallow: crop the top of very tall figures
        im = im.crop((0, 0, w, int(w * MAXH / TILEW)))
        th = MAXH
    return im.resize((TILEW, th), Image.LANCZOS)


def rows_for(slug):
    d = os.path.join(FIGS, slug)
    if not os.path.isdir(d):
        return None
    fs = sorted(f for f in os.listdir(d) if not f.startswith("."))
    return [os.path.join(d, f) for f in fs]


def main():
    out, per = sys.argv[1], int(sys.argv[2])
    slugs = [s.strip() for s in sys.argv[3:] if s.strip()]
    rows = []
    for s in slugs:
        fs = rows_for(s)
        if fs is None:
            rows.append((s, None, 0))
            continue
        for i in range(0, len(fs), PER_ROW):
            rows.append((s, fs[i:i + PER_ROW], i))
    chunks = [rows[i:i + per] for i in range(0, len(rows), per)]
    from PIL import ImageFont
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except Exception:
        font = None
    for ci, chunk in enumerate(chunks, 1):
        H = sum(LAB + max([MAXH] + [load(p).size[1] for p in (fs or [])]) + PAD for _, fs, _ in chunk) + PAD
        W = PER_ROW * (TILEW + PAD) + PAD
        sheet = Image.new("RGB", (W, H), (228, 228, 228))
        d = ImageDraw.Draw(sheet)
        y = PAD
        for s, fs, off in chunk:
            label = "%s   (figures %d-%d)" % (s, off + 1, off + len(fs)) if fs else "%s   (NO FIGURES DOWNLOADED)" % s
            d.rectangle([0, y, W, y + LAB - 4], fill=(30, 30, 60))
            d.text((6, y + 2), label, fill=(255, 255, 255), font=font)
            y += LAB
            x = PAD
            if fs:
                for p in fs:
                    im = load(p)
                    sheet.paste(im, (x, y))
                    d.rectangle([x - 1, y - 1, x + im.size[0], y + im.size[1]], outline=(120, 120, 120))
                    d.text((x + 2, y + im.size[1] + 2), os.path.basename(p)[:44], fill=(0, 0, 0), font=font)
                    x += TILEW + PAD
                y += max(load(p).size[1] for p in fs) + PAD
            else:
                y += 10
        sheet.save(out.replace("%d", str(ci)) if "%d" in out else out + ("_%d.png" % ci))
        print(out.replace("%d", str(ci)) if "%d" in out else out + ("_%d.png" % ci), sheet.size)


if __name__ == "__main__":
    main()
