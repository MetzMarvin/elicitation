"""camunda-docs-blog: derive the per-post figure list (deduped, featured card dropped).

The post's featured card is a 1200x627 CMS image whose alt text is the post's own title; it
is not an artefact. Everything else on the Sanity CDN with a real width is a candidate
figure, and its alt text is the strongest textual evidence available about what it shows.

  python ledgers/_cmdb_figs.py stats
  python ledgers/_cmdb_figs.py list <n> [<n> ...]
"""
import json, os, re, sys, collections

RAW = "ledgers/camunda-docs-blog.raw"
SCREEN = os.path.join(RAW, "screen.jsonl")
FIGDIR = os.path.join(RAW, "figs")


def key(u):
    m = re.search(r"/([0-9a-f]{20,})(?:-\d+x\d+)?\.(png|jpg|jpeg|webp|gif)$", u.split("?")[0])
    return m.group(1) if m else u.split("?")[0]


def dims(u):
    m = re.search(r"-(\d{2,4})x(\d{2,4})\.", u)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


def figs(r):
    """content figures of a post, deduped by asset id, featured card dropped."""
    title = re.sub(r"\s*\|\s*Camunda\s*$", "", r.get("title") or "").strip().lower()
    out, seen = [], set()
    for i in r["imgs"]:
        if i["kind"] != "raster" or "sanity.io" not in i["src"]:
            continue
        w, h = dims(i["src"])
        if w < 200:
            continue
        alt = (i.get("alt") or "").strip()
        if (w, h) == (1200, 627) and alt.lower() == title:
            continue
        k = key(i["src"])
        if k in seen:
            continue
        seen.add(k)
        out.append({"src": i["src"], "alt": alt, "w": w, "h": h})
    out.sort(key=lambda f: -f["w"] * f["h"])
    return out


def rows():
    for l in open(SCREEN, encoding="utf-8"):
        try:
            yield json.loads(l)
        except Exception:
            pass


DIAG = re.compile(r"(?i)\b(bpmn|process|diagram|flow ?chart|workflow|model|gateway|"
                  r"orchestration|architecture|sub-?process|lane|pool|task)\b")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if cmd == "list":
        want = set(int(x) for x in sys.argv[2:])
        for r in rows():
            if r["n"] in want:
                print("===", r["n"], r["title"], "| ai", r["n_ai"])
                for f in figs(r):
                    print("   %4dx%-4d %s | %s" % (f["w"], f["h"], f["alt"][:70], f["src"][-34:]))
        return
    c = collections.Counter()
    for r in rows():
        if r["n"] > 1435:
            continue
        fs = figs(r)
        c["posts"] += 1
        c["no_fig" if not fs else "has_fig"] += 1
        if fs:
            c["figs_total"] += len(fs)
            if any(DIAG.search(f["alt"]) for f in fs):
                c["diag_alt"] += 1
            elif any(f["alt"] for f in fs):
                c["other_alt"] += 1
            else:
                c["no_alt"] += 1
    print(c)
    # how many posts have a BPMN word in the fig alt vs in the body text
    n_altbpmn = n_txtbpmn = 0
    for r in rows():
        if r["n"] > 1435:
            continue
        fs = figs(r)
        if any("bpmn" in f["alt"].lower() for f in fs):
            n_altbpmn += 1
        if "BPMN" in r["text"] or "bpmn" in r["text"]:
            n_txtbpmn += 1
    print("posts with BPMN in a figure alt:", n_altbpmn,
          "| posts with BPMN in body text:", n_txtbpmn)


if __name__ == "__main__":
    main()
