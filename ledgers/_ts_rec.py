"""trisotech: apply a batch of reviewed dispositions, and write the corpus records that go with them.

  python ledgers/_ts_rec.py trisotech.raw/batch1.json

The batch is a JSON array of disposition objects (see trisotech.raw/dispositions.jsonl). Each entry is
appended to dispositions.jsonl; the last row for a key wins, so a re-judged page is superseded by
appending a new row rather than editing the old one. `captures` is a list of {"from", "to"} pairs
(source figure on disk, PNG to place next to the record) — JPEG sources are re-encoded so the audit's
`NNN_*.png` rule can see them. Record markdown is written with the Write tool, not from here.
The batch file is renamed to `<batch>.applied` afterwards so a re-run is a no-op.
"""
import json, os, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
DISPOS = os.path.join(RAW, "dispositions.jsonl")


def apply_batch(path):
    batch = json.load(open(path, encoding="utf-8"))
    with open(DISPOS, "a", encoding="utf-8") as f:
        for r in batch.get("dispositions", []):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    for cap in batch.get("captures", []):
        from PIL import Image
        src = os.path.normpath(os.path.join(ROOT, "..", cap["from"]))
        dst = os.path.normpath(os.path.join(ROOT, "..", cap["to"]))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst):
            Image.open(src).convert("RGB").save(dst)
        w, h = Image.open(dst).size
        print("capture %s (%dx%d)" % (os.path.basename(dst), w, h))
    shutil.move(path, path + ".applied")
    n = sum(1 for _ in open(DISPOS, encoding="utf-8") if _.strip())
    print("dispositions now: %d" % n)


if __name__ == "__main__":
    apply_batch(sys.argv[1])
