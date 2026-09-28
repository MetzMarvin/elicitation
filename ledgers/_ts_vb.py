"""trisotech video class: turn the running per-video dispositions into an applicable batch.

  python ledgers/_ts_vb.py build            -> writes trisotech.raw/batch9.json (.applied if it exists)
  python ledgers/_ts_vb.py orphans          -> prints the corpus records/captures that the new verdicts
                                               leave unreferenced (records for rows that are no longer
                                               INCLUDE/UNCERTAIN)

The dispositions live in trisotech.raw/video_disp.jsonl, one JSON object per line, appended as each
video is judged, so the file is the state a fresh agent can resume from. Records and captures named
in `keep` are (re)written by hand; everything else follows from the dispositions.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
RUN = os.path.join(RAW, "video_disp.jsonl")
OUT = os.path.join(RAW, "batch9.json")
CORPUS = os.path.normpath(os.path.join(ROOT, "..", "corpus", "trisotech"))


def rows():
    return [json.loads(l) for l in open(RUN, encoding="utf-8") if l.strip()]


def build():
    rs = rows()
    batch = {"dispositions": rs,
             "captures": [{"from": c[0], "to": c[1]} for c in CAPTURES]}
    out = OUT if not os.path.exists(OUT + ".applied") else OUT
    json.dump(batch, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("%s: %d dispositions, %d captures" % (out, len(rs), len(CAPTURES)))


# (source frame -> record capture) for the verdicts that keep a record
CAPTURES = []


def orphans():
    live = {r["key"] for r in rows() if r.get("verdict") in ("INCLUDE", "UNCERTAIN")}
    keep = {os.path.basename(r["record"]) for r in rows() if r.get("record")}
    print("verdicts: " + ", ".join("%s=%s" % (r["key"], r["verdict"] + ("/" + r["code"] if r.get("code") else ""))
                                   for r in rows()))
    print("\nrecords that must be DELETED (row no longer INCLUDE/UNCERTAIN):")
    for f in sorted(os.listdir(CORPUS)):
        nnn = f.split("_")[0]
        if f.endswith(".md"):
            if f not in keep and any(r["key"] in f for r in rows if r.get("verdict") == "EXCLUDE"):
                print("  ", f)
    print("\n(delete the matching NNN_*.png captures too; the audit fails on an NNN with no record)")


if __name__ == "__main__":
    (build if (len(sys.argv) > 1 and sys.argv[1] == "build") else orphans)()
