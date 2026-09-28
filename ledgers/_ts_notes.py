"""trisotech: pull the per-slide presenter notes out of the saved SlideShare embeds.

The embed HTML carries the speaker's own notes as a flat array of strings next to
"transcript". They are the cheapest per-slide signal available: a note that mentions an AI
term or a BPMN element says which slides are worth looking at full size.

  python ledgers/_ts_notes.py            -- refresh decks.json note fields, print the ranking
  python ledgers/_ts_notes.py show <slug>
"""
import json, os, re, sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trisotech.raw")
DECKS = os.path.join(RAW, "decks.json")
AI = re.compile(r"\b(AI|A\.I\.|LLM|GPT|GenAI|generative|agents?|agentic|machine learning|"
                r"neural|chatbot|copilot|prompt)\b")
BPMN = re.compile(r"\b(BPMN|DMN|CMMN|gateway|lane|pool|user task|service task|sub-process|"
                  r"subprocess|event|choreograph)\b", re.I)
BAD = re.compile(r"[{}<>]|http|function|\.js\b|\.css\b")


def extract(h):
    cands = re.findall(r'"([^"\\]{40,400})"', h)
    out = []
    for c in cands:
        if c.count(" ") <= 6 or BAD.search(c):
            continue
        if c not in out:
            out.append(c)
    return out


def main():
    d = json.load(open(DECKS, encoding="utf-8"))
    with_notes = 0
    for slug, v in d.items():
        p = os.path.join(RAW, "decks", v["key"] + ".html")
        if not os.path.exists(p):
            v["notes"], v["note_ai"], v["note_bpmn"] = [], 0, 0
            continue
        notes = extract(open(p, encoding="utf-8").read())
        v["notes"] = notes
        j = " ".join(notes)
        v["note_ai"] = len(AI.findall(j))
        v["note_bpmn"] = len(BPMN.findall(j))
        if notes:
            with_notes += 1
    json.dump(d, open(DECKS, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("decks with notes: %d of %d" % (with_notes, len(d)))
    for s, v in sorted(d.items(), key=lambda kv: -(kv[1]["note_ai"] + kv[1]["note_bpmn"]))[:35]:
        print("%3d/%3d slides=%-4d %-56s %s" % (v["note_ai"], v["note_bpmn"], v["n_slides"],
                                                s[:56], (v["notes"][0][:52] if v["notes"] else "")))
    print("decks with no notes: %d" % sum(1 for v in d.values() if not v["notes"]))


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "show":
        d = json.load(open(DECKS, encoding="utf-8"))
        v = d[sys.argv[2]]
        print(v["url"], v["n_slides"], "slides")
        for i, n in enumerate(v["notes"], 1):
            print("%3d %s" % (i, n.replace("\n", " ")[:200]))
    else:
        main()
