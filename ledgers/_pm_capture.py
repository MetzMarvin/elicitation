"""Build the evidence capture that sits beside a corpus record.

`python ledgers/_pm_capture.py OUT.png <stem> <i1,i2,...>`

Images are taken in DOCUMENT ORDER from the page's markdown twin, whatever form they take:
a standalone figure (its own `![...](url)` line) or an image embedded inside a paragraph.
That matters because some pages publish the whole article as prose with embedded images and
have no standalone figure at all (import-a-process-template), so a figure-indexed downloader
sees nothing on them.

The requested 1-based indices are downloaded into ledgers/processmaker.raw/figures/<stem>/cap_NNN_<name>.<ext>
(skipped when already on disk) and then laid on one sheet, 3 columns, each tile captioned with
"figure N of M" and the image's own file name. The chosen URLs are printed so the record can
cite them.
"""
import os, re, sys, time, urllib.parse, urllib.request

from PIL import Image, ImageDraw, ImageFont

ELI = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(ELI, "processmaker.raw/pages", "md")
FIGS = os.path.join(ELI, "processmaker.raw/figures")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
IMG = re.compile(r"!\[[^\]]*\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)")
TILEW, PAD, LAB, MAXH = 560, 8, 24, 420


def images(stem):
    """All image URLs in document order, inline ones included.

    Not a regex: the URLs on this site are full of characters a regex cannot walk cleanly -
    unencoded spaces ("Smart Extract Object Modeler.png") and balanced parentheses
    ("image(135).png"). A regex either misses the former or over-runs the latter into the
    following prose. So: find every `![`, take the URL between the next `](` and its matching
    `)`, counted by nesting depth.
    """
    body = open(os.path.join(MD, stem + ".md"), encoding="utf-8").read()
    out, pos = [], 0
    while True:
        a = body.find("![", pos)
        if a < 0:
            break
        b = body.find("](", a)
        if b < 0 or "\n" in body[a:b]:
            pos = a + 2
            continue
        k, depth, end = b + 2, 0, -1
        while k < len(body):
            c = body[k]
            if c == "(":
                depth += 1
            elif c == ")":
                if depth == 0:
                    end = k
                    break
                depth -= 1
            elif c == "\n":
                break
            k += 1
        if end < 0:
            pos = a + 2
            continue
        u = body[b + 2:end]
        if u.startswith("http"):
            out.append(u)
        pos = end + 1
    return out


def grab(url, dest):
    if os.path.exists(dest):
        return os.path.getsize(dest)
    req = urllib.request.Request(urllib.parse.quote(url, safe=":/?&=#%+,"),
                                 headers={"User-Agent": UA,
                                          "Referer": "https://docs.processmaker.com/"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    open(dest, "wb").write(data)
    time.sleep(0.6)
    return len(data)


def main():
    out, stem, idxs = sys.argv[1], sys.argv[2], sys.argv[3]
    want = [int(x) for x in idxs.split(",")]
    urls = images(stem)
    d = os.path.join(FIGS, stem)
    os.makedirs(d, exist_ok=True)
    picked = []
    for i in want:
        u = urls[i - 1]
        name = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(u).path))
        name = re.sub(r"[^A-Za-z0-9._-]", "_", name)[:60] or "image.png"
        p = os.path.join(d, "cap_%03d_%s" % (i, name))
        grab(u, p)
        picked.append((i, u, p))
    try:
        font = ImageFont.truetype("arial.ttf", 17)
    except Exception:
        font = None
    tiles = []
    for i, u, p in picked:
        im = Image.open(p)
        try:
            im.seek(0)
        except Exception:
            pass
        im = im.convert("RGB")
        w, h = im.size
        th = int(round(TILEW * h / w))
        if th > MAXH:
            im = im.crop((0, 0, w, int(w * MAXH / TILEW)))
            th = MAXH
        tiles.append((i, u, im.resize((TILEW, th), Image.LANCZOS)))
    cols = 3 if len(tiles) > 2 else len(tiles)
    rows = (len(tiles) + cols - 1) // cols
    rowh = max(t[2].size[1] for t in tiles) + LAB + PAD
    W = cols * (TILEW + PAD) + PAD
    sheet = Image.new("RGB", (W, rows * rowh + PAD), (228, 228, 228))
    dr = ImageDraw.Draw(sheet)
    for k, (i, u, im) in enumerate(tiles):
        cx, cy = k % cols, k // cols
        x = PAD + cx * (TILEW + PAD)
        y = PAD + cy * rowh
        dr.rectangle([x - 2, y - 2, x + TILEW + 2, y + LAB - 6], fill=(30, 30, 60))
        dr.text((x + 4, y - 1), "figure %d of %d" % (i, len(urls)), fill=(255, 255, 255), font=font)
        sheet.paste(im, (x, y + LAB - 4))
    sheet.save(out)
    print("wrote", out, sheet.size)
    for i, u, p in picked:
        print("figure %d of %d: %s" % (i, len(urls), u))


if __name__ == "__main__":
    main()
