"""trisotech: deck pass -- cheap 5-column overview sheets, then full-size views of the slides
that look like diagrams.

  python ledgers/_ts_deck2.py mini <slug> [per]     -- overview sheet(s) for a deck
  python ledgers/_ts_deck2.py full <slug> <n> [...] -- copy the given slide numbers (1-based) to
                                                       trisotech.raw/deckfull/ for full-size viewing
"""
import json, os, re, sys
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
SLIDES = os.path.join(RAW, "slides")
OUT = os.path.join(RAW, "deckmini")
FULL = os.path.join(RAW, "deckfull")
DECK_JSON = os.path.join(RAW, "decks.json")


def files(slug):
    d = os.path.join(SLIDES, slug[:90])
    return sorted(f for f in os.listdir(d) if f.endswith(".jpg"))


def mini(slug, per=20, width=300, cols=5):
    fs = files(slug)
    os.makedirs(OUT, exist_ok=True)
    made = []
    for i in range(0, len(fs), per):
        chunk = fs[i:i + per]
        ch = int(width * 9 / 16)
        rows = (len(chunk) + cols - 1) // cols
        im = Image.new("RGB", (cols * width, rows * (ch + 16)), "white")
        dr = ImageDraw.Draw(im)
        for k, f in enumerate(chunk):
            s = Image.open(os.path.join(SLIDES, slug[:90], f)).convert("RGB").resize((width - 2, ch - 2))
            x, y = (k % cols) * width + 1, (k // cols) * (ch + 16) + 14
            im.paste(s, (x, y))
            dr.text((x + 1, y - 12), "s%s" % re.sub(r"\D", "", f)[:3], fill="black")
        name = "%s__%02d.png" % (slug[:66], i // per + 1)
        im.save(os.path.join(OUT, name))
        made.append((os.path.join(OUT, name), im.size, len(chunk)))
    for p, size, n in made:
        print("%s  %d slides  %dx%d" % (p, n, size[0], size[1]))


def full(slug, nums):
    fs = files(slug)
    os.makedirs(FULL, exist_ok=True)
    for n in nums:
        f = fs[n - 1]
        im = Image.open(os.path.join(SLIDES, slug[:90], f)).convert("RGB")
        p = os.path.join(FULL, "%s__s%02d.png" % (slug[:40], n))
        im.save(p)
        print("%s  %dx%d" % (p, im.width, im.height))


def mid(slug, nums, width=1000):
    fs = files(slug)
    os.makedirs(FULL, exist_ok=True)
    for n in nums:
        im = Image.open(os.path.join(SLIDES, slug[:90], fs[n - 1])).convert("RGB")
        im = im.resize((width, int(im.height * width / im.width)))
        p = os.path.join(FULL, "%s__s%02d_mid.png" % (slug[:40], n))
        im.save(p)
        print("%s  %dx%d" % (p, im.width, im.height))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "mini":
        mini(sys.argv[2], *(int(x) for x in sys.argv[3:]))
    elif cmd == "mid":
        mid(sys.argv[2], [int(x) for x in sys.argv[3:]])
    elif cmd == "full":
        full(sys.argv[2], [int(x) for x in sys.argv[3:]])
