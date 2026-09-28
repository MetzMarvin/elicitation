"""Download just the FIRST figure of each named page, into ledgers/processmaker.raw/first_figure/.

One figure per page is enough to tell the page's kind apart: a Process Modeler canvas
(white dotted grid, coloured rounded shapes, left object panel) versus a product UI
screenshot (dialogs, tables, form fields, code editors). Used to verify, across the whole
"modeling objects"/"process modeler" subtree, that the canvas-screenshot pattern holds.

`python ledgers/processmaker.raw/first_figure.py <slug> [<slug> ...]`
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ELI = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(ELI, "processmaker.raw/pages", "md")
OUT = os.path.join(ELI, "processmaker.raw/first_figure")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
FIGLINE = re.compile(r"^\s*!\[[^\]]*\]\((https?://.+)\)\s*$")


def main():
    os.makedirs(OUT, exist_ok=True)
    man = {}
    for s in sys.argv[1:]:
        s = s.strip()
        f = os.path.join(MD, s + ".md")
        if not os.path.exists(f):
            print("MISSING md:", s)
            continue
        body = open(f, encoding="utf-8").read()
        figs = [m.group(1) for m in (FIGLINE.match(ln) for ln in body.splitlines()) if m]
        if not figs:
            continue
        u = urllib.parse.quote(figs[0], safe=":/?&=#%+,")
        p = os.path.join(OUT, s + ".png")
        try:
            req = urllib.request.Request(u, headers={"User-Agent": UA,
                                                     "Referer": "https://docs.processmaker.com/"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
        except Exception as e:
            print("FAIL %s %s" % (s, e))
            continue
        open(p, "wb").write(data)
        man[s] = {"url": figs[0], "file": os.path.relpath(p, ELI).replace("\\", "/"),
                  "bytes": len(data)}
        time.sleep(0.15)
    json.dump(man, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"), indent=1)
    print("first figures:", len(man))


if __name__ == "__main__":
    main()
