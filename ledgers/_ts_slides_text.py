"""trisotech: read the per-slide text out of the saved SlideShare embeds.

The embed page carries the deck's slide-by-slide text (and speaker notes) as a JSON array of
{"index": n, "text": "..."}. That is the cheapest per-slide signal there is: it says which slides
carry AI/LLM words and which carry BPMN words, so only those slides need to be looked at full size.
(The page also carries *other* decks' descriptions from its "related" carousel and a large i18n
message blob - including the site's own "Powered by AI" label, which is a feature name, not content.
Neither is in this array.)

  python ledgers/_ts_slides_text.py            -- refresh decks.json, print the screening table
  python ledgers/_ts_slides_text.py show <slug> -- print one deck's per-slide text
"""
import json, os, re, sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trisotech.raw")
DECKS = os.path.join(RAW, "decks.json")
AI = re.compile(r"\b(AI|A\.I\.|LLM|LLMs|GPT|ChatGPT|GenAI|generative AI|large language model|"
                r"machine learning|deep learning|neural network|chatbot|copilot|agents?|agentic|"
                r"prompt engineering|natural language processing|NLP|RAG|MCP|foundation model)\b")
BPMN = re.compile(r"\b(BPMN|BPMN 2\.0|CMMN|DMN|process diagram|pools?|lanes?|gateways?|service tasks?|"
                  r"user tasks?|sub-?process(es)?|boundary events?|start events?|end events?|"
                  r"ad-?hoc|call activity|choreograph\w*)\b", re.I)
ITEM = re.compile(r'\{"index":(\d+),"text":"((?:[^"\\]|\\.)*)"\}')


def slides_of(html):
    out = {}
    for m in ITEM.finditer(html):
        try:
            t = json.loads('"' + m.group(2) + '"')
        except Exception:
            continue
        out[int(m.group(1))] = t
    return out


def main():
    d = json.load(open(DECKS, encoding="utf-8"))
    table = []
    for slug, v in d.items():
        p = os.path.join(RAW, "decks", v["key"] + ".html")
        st = slides_of(open(p, encoding="utf-8").read()) if os.path.exists(p) else {}
        v["slide_texts"] = {str(k): val for k, val in sorted(st.items())}
        ai_slides, bp_slides = [], []
        for k, t in sorted(st.items()):
            if AI.search(t):
                ai_slides.append(k)
            if BPMN.search(t):
                bp_slides.append(k)
        v["slide_ai_idx"] = ai_slides
        v["slide_bpmn_idx"] = bp_slides
        n = v["n_slides"] or 1
        table.append((len(ai_slides) / n, len(ai_slides), len(bp_slides), n, slug))
    json.dump(d, open(DECKS, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("decks: %d ; decks with per-slide text: %d"
          % (len(d), sum(1 for v in d.values() if v["slide_texts"])))
    print("decks whose slides mention AI: %d ; mention BPMN: %d ; both: %d"
          % (sum(1 for v in d.values() if v["slide_ai_idx"]),
             sum(1 for v in d.values() if v["slide_bpmn_idx"]),
             sum(1 for v in d.values() if v["slide_ai_idx"] and v["slide_bpmn_idx"])))
    print()
    for frac, na, nb, n, slug in sorted(table, reverse=True)[:60]:
        print("  %5.0f%% ai=%-3d bpmn=%-3d slides=%-4d %s" % (frac * 100, na, nb, n, slug[:60]))


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "show":
        d = json.load(open(DECKS, encoding="utf-8"))
        v = d[sys.argv[2]]
        print(v["url"], v["n_slides"], "slides | ai idx", v["slide_ai_idx"], "| bpmn idx", v["slide_bpmn_idx"])
        for k, t in v["slide_texts"].items():
            print("%3s | %s" % (k, t.replace("\n", " ")[:230]))
    else:
        main()
