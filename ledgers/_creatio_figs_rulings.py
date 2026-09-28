#!/usr/bin/env python3
"""Classify the notation of every figure I downloaded, from its caption/alt/context text.

The Academy writes a caption under most figures ("Fig. N <what it shows>") and the paragraph
after it says what the figure is for; both are textual evidence for "is this BPMN 2.0?" and are
cheaper and stronger than the picture. This pass classifies every figure mechanically and prints
the ones it cannot decide, so the visual pass can be spent on those (and on the AI pages).

Classes:
  bpmn      - a business-process diagram in the Creatio process designer (BPMN 2.0 notation:
              start/end events, tasks, gateways, sequence flows)
  not-bpmn  - a UI screenshot, panel, wizard, list, log, settings dialog, architecture diagram,
              sequence/columnar flow, table illustration, chat UI, brand icon, ...
  unsure    - nothing in the caption or the surrounding text decides it: needs a look

  python ledgers/_creatio_figs_rulings.py            # classify + print the unsure list
  python ledgers/_creatio_figs_rulings.py --write    # write _creatio_figs_rulings.json
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"

# --- evidence that the figure is a process diagram in the process designer -------------
BPMN_HINT = re.compile(
    r"(process designer|start event|end event|intermediate event|boundary event|signal event|"
    r"timer event|message event|gateway|exclusive|parallel|inclusive|sequence flow|conditional "
    r"flow|default flow|business process|sub-process|subprocess|call activity|process element|"
    r"element palette|process canvas|process diagram|process library|case designer|"
    r"\bprocess\b.*\b(step|flow|branch)\b|element setup area.*process|new process)", re.I)
# --- evidence that the figure is not a diagram at all -----------------------------------
UI_HINT = re.compile(
    r"(setup area|setup panel|settings|parameters|parameter|mini page|wizard|dialog|field|"
    r"drop-down|dropdown|checkbox|tab|list of|library|log|progress|report|dashboard|chart|"
    r"architecture|environments|deployments|credits|budget|chat|prompt|portal|registrations|"
    r"table|grid|record page|form|section|profile|account|contact|calendar|email|notification|"
    r"indicator|menu|button|panel|page|screen|workspace|console|designer|editor)"
    , re.I)


def classify(alt, before, after):
    """The caption (alt) is the decisive evidence; the paragraph around the figure is only a
    fallback, because a page that says "you can use this element in a business process" next to
    a screenshot of the element's parameter panel is not publishing a process diagram."""
    cap = (alt or "").strip()
    if BPMN_HINT.search(cap):
        return "bpmn", "caption names process-model notation"
    if cap and UI_HINT.search(cap):
        return "not-bpmn", "caption names a UI surface, not a diagram"
    hay = " ".join([after or "", before or ""])
    b, u = bool(BPMN_HINT.search(hay)), bool(UI_HINT.search(hay))
    if b and not u:
        return "bpmn", "paragraph around the figure names process-model notation"
    if u and not b:
        return "not-bpmn", "paragraph around the figure names a UI surface, not a diagram"
    if not cap:
        return "unsure", "figure has no caption to decide on"
    return "unsure", "caption is generic"


def main():
    idx = json.loads((OUT / "figs_index.json").read_text(encoding="utf-8"))
    arts = json.loads((OUT / "articles.json").read_text(encoding="utf-8"))

    by_page = {}
    for it in idx:
        by_page.setdefault(it["slug"], []).append(it)

    rulings, unsure = {}, []
    for slug, figs in sorted(by_page.items()):
        page = figs[0]["page"]
        kinds, named = [], []
        for it in figs:
            k, why = classify(it.get("alt", ""), it.get("text_before", ""), it.get("text_after", ""))
            kinds.append(k)
            named.append(f'{it["file"]}: {why}')
        if "bpmn" in kinds:
            kind = "bpmn"
        elif "unsure" in kinds:
            kind = "unsure"
        else:
            kind = "not-bpmn"
        a = arts.get(slug, {})
        text = a.get("text", "") or ""
        rulings[slug] = {
            "page": page, "kind": kind, "figs": [it["file"] for it in figs],
            "alt": [it.get("alt", "") for it in figs],
            "named": named,
            "fig_caption_evidence": " | ".join(filter(None, [it.get("alt", "") for it in figs]))[:300],
            "method": ("caption / alt text / surrounding paragraph of each downloaded figure "
                       "(ledgers/_creatio/articles.json); visual confirmation recorded separately "
                       "for the pages whose caption did not decide it"),
        }
        if kind == "unsure":
            unsure.append((slug, page, len(figs),
                           "; ".join(filter(None, [it.get("alt", "") for it in figs]))[:80],
                           re.sub(r"\s+", " ", text[:110])))

    n = {"bpmn": 0, "not-bpmn": 0, "unsure": 0}
    for r in rulings.values():
        n[r["kind"]] += 1
    print(f"pages: {len(rulings)}  bpmn: {n['bpmn']}  not-bpmn: {n['not-bpmn']}  unsure: {n['unsure']}")
    print("\nUNSURE (need a look):")
    for slug, page, nf, alt, txt in unsure:
        print(f"  [{nf}f] {slug[:70]}\n        alt: {alt}\n        text: {txt}")

    if "--write" in sys.argv:
        (OUT / "_creatio_figs_rulings.json").write_text(
            json.dumps(rulings, indent=1, ensure_ascii=False), encoding="utf-8")
        print("\nwrote", OUT / "_creatio_figs_rulings.json")


if __name__ == "__main__":
    main()
