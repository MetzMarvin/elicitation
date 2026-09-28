"""camunda-docs-blog: append one disposition per judged post (append-only, last row per n wins).

Usage: python ledgers/_cmdb_disp.py <rows.json>
  rows.json = list of dicts with at least: n, verdict, evidence.
A row is refused if its evidence is not a contiguous (whitespace-normalised) substring of the
screened page text, so no quote can enter the ledger without being on the page.
"""
import json, os, re, sys

RAW = "ledgers/camunda-docs-blog.raw"
DIPS = os.path.join(RAW, "dips.jsonl")
SCREEN = os.path.join(RAW, "screen.jsonl")


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def main(path):
    screen = {}
    for l in open(SCREEN, encoding="utf-8"):
        try:
            r = json.loads(l)
        except Exception:
            continue
        screen[r["n"]] = r
    rows = json.load(open(path, encoding="utf-8"))
    ok = 0
    with open(DIPS, "a", encoding="utf-8") as fh:
        for r in rows:
            n = r["n"]
            s = screen.get(n)
            if s is None:
                if r.get("verdict") == "BLOCKED":
                    # a blocked item has no page to quote: its evidence is the refusal itself
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
                    ok += 1
                    continue
                print("REFUSED n=%d: no screen row" % n)
                continue
            q = norm(r.get("evidence"))
            if not q:
                print("REFUSED n=%d: empty evidence" % n)
                continue
            if q not in norm(s["text"]):
                print("REFUSED n=%d: quote not on page: %r" % (n, r["evidence"][:80]))
                continue
            if len(q.split()) > 25:
                print("REFUSED n=%d: quote longer than 25 words" % n)
                continue
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            ok += 1
    print("appended", ok, "of", len(rows))


if __name__ == "__main__":
    main(sys.argv[1])
