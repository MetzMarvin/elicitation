"""camunda-docs-blog: what the plan would say, without the "every figure looked at" guard.

  python ledgers/_cmdb_preview.py            # verdict counts + the rows that would need records
  python ledgers/_cmdb_preview.py -v         # ... and every non-EXCLUDE row

Same code path as _cmdb_final.py's plan, minus its refusal to run while some post's figure
has never been in front of anyone. So the counts here are a floor, not the census: posts whose
figures no report has judged yet fall into the UNCERTAIN branch ("never put in front of
anyone"). Use it to size the record-writing work, never to emit the ledger.
"""
import collections, sys

import _cmdb_final as M
import _cmdb_figs as F


def main():
    verbose = "-v" in sys.argv
    cls, aiv, vnt = M.visual()
    counter = collections.Counter()
    need, ruled = [], []
    for line in open(M.FRONTIER, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2:
            continue
        n = int(parts[0])
        if n > 1435:
            counter[("BLOCKED", None)] += 1
            continue
        r = next(x for x in F.rows() if x["n"] == n)
        c = M.RULED.get(n) or M.model_verdict(r, cls) or M.classify(r, cls, aiv, vnt)
        if c is None:
            continue
        v, reason = c[0], c[1]
        counter[(v, reason)] += 1
        rec = M.DONE.get(n)
        if v in ("INCLUDE", "UNCERTAIN") and not rec:
            (ruled if n in M.RULED else need).append((n, v, r["title"][:56]))
        if verbose and v != "EXCLUDE":
            print("%5d %-9s %-16s %-28s %s" % (n, v, reason or "-", rec or "", r["title"][:44]))
    print(counter)
    print("INCLUDE/UNCERTAIN already carrying a record:", len(M.DONE))
    print("would need a record - mechanical:", len(need))
    for n, v, t in sorted(need):
        print("   %5d %-9s %s" % (n, v, t))
    print("would need a record - hand-ruled:", len(ruled))
    for n, v, t in sorted(ruled):
        print("   %5d %-9s %s" % (n, v, t))


if __name__ == "__main__":
    main()
