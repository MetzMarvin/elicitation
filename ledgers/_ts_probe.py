"""trisotech: one-off probe -- full AI-term hits for a few decks (slides + page text)."""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
_spec = importlib.util.spec_from_file_location("deck3", os.path.join(ROOT, "_ts_deck3.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)
SCREEN = {r["slug"]: r for r in json.load(open(os.path.join(RAW, "screen.json"), encoding="utf-8"))}


def norm(s):
    return " ".join((s or "").replace(" ", " ").split())


for slug in sys.argv[1:]:
    print("=" * 100)
    print("SLUG", slug)
    t = D.trans(slug)
    print("-- slides with AI term (%d slides total):" % len(t))
    for i, s in enumerate(t, 1):
        c = norm(s)
        m = D.AI.search(c)
        if m:
            print("  s%-3d %s" % (i, c[:400]))
    p = norm(SCREEN[slug]["text"]) if slug in SCREEN else ""
    print("-- page text AI windows:")
    for m in re.finditer(D.AI, p):
        a = max(0, m.start() - 120)
        print("   ...%s..." % p[a:m.end() + 160])
