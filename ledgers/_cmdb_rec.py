"""camunda-docs-blog: pull one figure of a post at full width, for a corpus record.

  python ledgers/_cmdb_rec.py shot N K PATH      # figure K of post N -> PATH (cdn, w=1400)
  python ledgers/_cmdb_rec.py list N            # the figures of post N, numbered as in the sheets
  python ledgers/_cmdb_rec.py all N             # every figure of post N, numbered for shotall
  python ledgers/_cmdb_rec.py shotall N K PATH  # figure K of `all N` -> PATH

`list`/`shot` use the same numbering as the contact sheets and the briefs (the selected
figures). `all`/`shotall` cover every figure on the page, for the case where the record should
show a figure the selection skipped (e.g. the post's own BPMN diagram when the sheet cell was
a screenshot).
"""
import subprocess, sys

import _cmdb_figs as F
import _cmdb_shots as S

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/140.0.0.0 Safari/537.36")


def every(r):
    fs = F.figs(r)
    fs.sort(key=lambda f: (0 if F.DIAG.search(f["alt"]) else 1, -f["w"] * f["h"]))
    return fs


def fetch(f, path):
    subprocess.run(["curl", "-s", "-m", "60", "-A", UA, "-o", path,
                    "%s?w=1400&q=90" % f["src"]], check=False)
    print("wrote", path, "<-", f["src"].split("/")[-1], "|", f["alt"][:60])


def main():
    cmd = sys.argv[1]
    n = int(sys.argv[2])
    for r in F.rows():
        if r["n"] != n:
            continue
        if cmd in ("list", "all"):
            fs = S.selected(r) if cmd == "list" else every(r)
            for k, f in enumerate(fs, 1):
                print("%d  %4dx%-4d %-60s %s" % (k, f["w"], f["h"], f["alt"][:58], f["src"]))
            return
        k, path = int(sys.argv[3]), sys.argv[4]
        fetch((S.selected(r) if cmd == "shot" else every(r))[k - 1], path)
        return


if __name__ == "__main__":
    main()
