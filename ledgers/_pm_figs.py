"""Download the standalone figures of chosen processmaker pages.

`python ledgers/processmaker.raw/figures.py <slug> [<slug> ...]`

A "standalone figure" is a markdown line that is nothing but an image: those are the article's
illustrations. Images embedded mid-sentence (the palette icons, the "Add" button, the plan badges)
are not figures and are not downloaded. Files land in ledgers/processmaker.raw/figures/<slug>/NNN_name.ext and a
manifest is printed as JSON.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "processmaker.raw/pages")
MD = os.path.join(RAW, "md")
OUT = os.path.join(ELI, "processmaker.raw/figures")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
FIGLINE = re.compile(r"^\s*!\[[^\]]*\]\((https?://.+)\)\s*$")


def get(url, path):
    url = urllib.parse.quote(url, safe=":/?&=#%+,")
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                              "Referer": "https://docs.processmaker.com/"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    open(path, "wb").write(data)
    return len(data)


def main():
    slugs = sys.argv[1:]
    man = {}
    for s in slugs:
        f = os.path.join(MD, s + ".md")
        if not os.path.exists(f):
            print("MISSING md:", s)
            continue
        body = open(f, encoding="utf-8").read()
        figs = [m.group(1) for m in (FIGLINE.match(ln) for ln in body.splitlines()) if m]
        d = os.path.join(OUT, s)
        os.makedirs(d, exist_ok=True)
        recs = []
        for i, u in enumerate(figs, 1):
            name = re.sub(r"[^A-Za-z0-9._-]", "_", u.rsplit("/", 1)[-1])
            ext = os.path.splitext(name)[1].lower() or ".png"
            if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg"):
                ext = ".png"
            p = os.path.join(d, "%03d_%s" % (i, name if name.lower().endswith(ext) else name + ext))
            try:
                n = get(u, p)
            except Exception as e:
                print("FAIL %s %s" % (u, e))
                continue
            recs.append({"i": i, "url": u, "file": os.path.relpath(p, ELI).replace("\\", "/"),
                         "bytes": n})
            time.sleep(0.2)
        man[s] = recs
        print("%-46s %d figures" % (s, len(recs)))
    json.dump(man, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
