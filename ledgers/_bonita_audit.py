#!/usr/bin/env python3
"""Calibration pass over the mechanically excluded pages (worker elicitation-6f).

The census's residual blind spot is the pages the screen excludes without anyone looking at
them. This module measures it deterministically: every `step`-th mechanically excluded page
that has figures or an AI/proc token is sampled, its figures are looked at in a contact sheet,
and its HTML is re-searched *outside* the content region for diagram-capable elements
(canvas/iframe/object/embed, bpmn markers, .bpmn links). Anything found is re-coded in RULINGS.

  python ledgers/_bonita_audit.py sample [STEP]     # choose the sample, write ledgers/_bonita/audit.json
  python ledgers/_bonita_audit.py report            # per sampled page: what the shadow screen sees
  python ledgers/_bonita_audit.py sheet OUT COLS TW TH
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _bonita_rows as S  # noqa: E402

OUT = ELI / "ledgers" / "_bonita"
AUD = OUT / "audit.json"

SHADOW = re.compile(r"<canvas\b|<iframe\b|<object\b|<embed\b|djs-element|bpmn-js|"
                    r"\bbpmn\b|\.bpmn\b|\.proc\b", re.I)


def mech_pages():
    out = []
    for url, rec in S.records():
        h = S.html_of(rec)
        sc = S.screen(url, h)
        if S.tier(url, sc) != "mech":
            continue
        if sc["figures"] or sc["ai"] or sc["proc"]:
            out.append((url, rec, sc, h))
    return out


def sample():
    step = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    pages = mech_pages()
    picked = pages[::step]
    data = {"step": step, "candidates": len(pages), "sampled": len(picked),
            "method": "every %d-th mechanically excluded page that has figures or an AI/proc "
                      "token, in population order" % step, "pages": []}
    for url, rec, sc, h in picked:
        shadow = {}
        for pat, name in ((r"<canvas\b", "canvas"), (r"<iframe\b", "iframe"),
                          (r"<object\b|<embed\b", "object/embed"), (r"djs-element|bpmn-js", "bpmnjs"),
                          (r"\bbpmn\b", "word-bpmn"), (r"\.bpmn\b", "dot-bpmn"),
                          (r"\.proc\b", "dot-proc")):
            n = len(re.findall(pat, h, re.I))
            if n:
                shadow[name] = n
        ctx = [re.sub(r"\s+", " ", m.group(0))[:120]
               for m in re.finditer(r".{70}\bbpmn\b.{70}", h, re.I)][:3]
        data["pages"].append({"url": url, "page_figures": len(sc["figures"]),
                              "figures": sc["figures"], "ai": sc["ai"], "proc": sc["proc"],
                              "shadow": shadow, "bpmn_context": ctx})
    AUD.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("mechanical candidates %d | sampled %d (step %d)" % (len(pages), len(picked), step))
    for p in data["pages"]:
        print("  %-70s figs=%-2d shadow=%s" % (p["url"].split("//")[1][:70], p["page_figures"],
                                               p["shadow"] or "-"))


def report():
    data = json.loads(AUD.read_text(encoding="utf-8"))
    print("sample: step %d, %d of %d mechanical pages" % (data["step"], data["sampled"],
                                                          data["candidates"]))
    n_shadow = 0
    for p in data["pages"]:
        if p["shadow"]:
            n_shadow += 1
            print("SHADOW %s -> %s" % (p["url"], p["shadow"]))
            for c in p["bpmn_context"]:
                print("        %s" % c)
    print("sampled pages with any diagram-capable element outside the content region: %d of %d"
          % (n_shadow, data["sampled"]))
    figs = sum(p["page_figures"] for p in data["pages"])
    print("figures on the sampled pages: %d" % figs)


def sheet():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    data = json.loads(AUD.read_text(encoding="utf-8"))
    wanted = {p["url"] for p in data["pages"]}
    man = [m for m in json.loads((OUT / "figs" / "manifest.json").read_text(encoding="utf-8"))
           if m.get("file") and m["page"] in wanted]
    rows = (len(man) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    skipped = []
    for k, m in enumerate(man):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(OUT / "figs" / m["file"])
        except Exception:  # noqa: BLE001  (SVG and AVIF have no PIL decoder here)
            skipped.append(m)
            d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(200, 160, 160))
            d.text((x + 4, y + 4), "%d %s [no decoder]" % (k + 1, m["name"][:36]), fill=(160, 0, 0))
            d.text((x + 4, y + 15), m["page"].split("//")[1][:52], fill=(90, 90, 90))
            continue
        if im.mode in ("P", "RGBA", "LA"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        im = im.convert("RGB")
        w, h = im.size
        sc = min((tw - 8) / w, (th - 30) / h, 2.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS),
                 (x + 4, y + 26))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (k + 1, m["name"][:40], w, h), fill=(0, 0, 0))
        d.text((x + 4, y + 15), m["page"].split("//")[1][:52], fill=(90, 90, 90))
        print("%-4d %-42s %s" % (k + 1, m["name"][:42], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles, %d without a PIL decoder)" % (stem, len(man), len(skipped)))
    for m in skipped:
        print("   no-decoder %-52s %s" % (m["name"][:52], m["page"].split("//")[1][:60]))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "sample"
    {"sample": sample, "report": report, "sheet": sheet}[mode]()
