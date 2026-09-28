"""trisotech deck pass: the deck's own per-slide transcript.

The Slideshare pages saved in trisotech.raw/decks/<key>.html carry a "transcript" array: the text
of every slide of the deck (105 of 106 decks have one; one deck has none). That is textual
evidence for every slide, which is both cheaper and stronger than reading the slide images, and it
lets the deck family be screened unfiltered -- every slide of every deck, not a keyword subset.

  python ledgers/_ts_deck3.py ai                 -- decks with any AI/LLM term in their slide text
  python ledgers/_ts_deck3.py scan <slug> [...]  -- per-slide AI/notation hits for the given decks
  python ledgers/_ts_deck3.py sents <slug> <n>   -- full slide text of slide n (0-based in hits list)
  python ledgers/_ts_deck3.py find <slug> <word>  -- slides whose text contains word
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
DECKS = os.path.join(RAW, "decks")

AI = re.compile(r"(?i)\b(AI|A\.I\.|artificial intelligence|LLM|LLMs|GPT|ChatGPT|OpenAI|Copilot|"
                r"machine learning|neural|agentic|AI agent|agents?|generative AI|GenAI|RAG|"
                r"predictive|autonomous)\b")
NOT = re.compile(r"(?i)\b(BPMN|CMMN|DMN|BPM\+|DRD|service task|user task|business rule task|"
                 r"gateway|pool|lane|sub-?process|case model|decision table|decision model|"
                 r"flowchart|process diagram|model)\b")


def arr(html, name):
    i = html.find('"%s":[' % name)
    if i < 0:
        return None
    j = html.index("[", i)
    depth, k = 0, j
    while k < len(html):
        if html[k] == "[":
            depth += 1
        elif html[k] == "]":
            depth -= 1
            if depth == 0:
                break
        k += 1
    try:
        return json.loads(html[j:k + 1])
    except Exception:
        return None


def key(slug):
    return json.load(open(os.path.join(RAW, "decks.json"), encoding="utf-8"))[slug]["key"]


def trans(slug):
    p = os.path.join(DECKS, key(slug) + ".html")
    if not os.path.exists(p):
        return []
    return arr(open(p, encoding="utf-8", errors="replace").read(), "transcript") or []


def deckinfo():
    return json.load(open(os.path.join(RAW, "decks.json"), encoding="utf-8"))


def clean(s):
    return " ".join((s or "").split())


def hits(slug):
    t = trans(slug)
    out = []
    for i, s in enumerate(t):
        c = clean(s)
        if AI.search(c):
            out.append((i + 1, c))
    return out


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "ai"
    d = deckinfo()
    if cmd == "ai":
        n = 0
        for s in d:
            h = hits(s)
            if h:
                n += 1
                print("== %-62s %2d/%2d slides with an AI term" % (s[:62], len(h), len(trans(s))))
                for i, c in h[:6]:
                    print("     s%-3d %s" % (i, c[:210]))
        print("\ndecks with an AI term in slide text: %d / %d" % (n, len(d)))
    elif cmd == "scan":
        for s in sys.argv[2:]:
            t = trans(s)
            print("== %s  (%d slides)" % (s, len(t)))
            for i, x in enumerate(t, 1):
                c = clean(x)
                f = []
                if AI.search(c):
                    f.append("AI")
                if NOT.search(c):
                    f.append("NOT")
                print("   s%-3d [%s] %s" % (i, ",".join(f) or "  ", c[:230]))
    elif cmd == "sents":
        for i, x in enumerate(trans(sys.argv[2]), 1):
            print("s%-3d %s\n" % (i, clean(x)))
    elif cmd == "find":
        w = re.compile(sys.argv[3], re.I)
        for i, x in enumerate(trans(sys.argv[2]), 1):
            c = clean(x)
            if w.search(c):
                print("s%-3d %s" % (i, c[:300]))
