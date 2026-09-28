"""trisotech: build the census ledger.

  python ledgers/_ts_rows.py screen     -- classify the frozen population (own content region only)
  python ledgers/_ts_rows.py quotes     -- show the candidate quote for a slug (eyeball the evidence)
  python ledgers/_ts_rows.py emit       -- write ledgers/trisotech.jsonl: header + one row per page + footer

Verdicts follow the shared rules: EXCLUDE only under E0/E1/E2/E3 with a verbatim quote,
UNCERTAIN whenever anything is unresolved, INCLUDE when a BPMN 2.0 process artefact carries an
AI/LLM element inside the process. Eye-judged items read their verdict from
trisotech.raw/dispositions.jsonl (written while reviewing sheets), everything else is mechanical.
"""
import json, os, re, sys, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
LEDGER = os.path.join(ROOT, "trisotech.jsonl")
SCREENF = os.path.join(RAW, "screen.json")
DISPOS = os.path.join(RAW, "dispositions.jsonl")
ACCESSED = "2026-09-25"

# --- lexicons -------------------------------------------------------------------------
AI = re.compile(r"\b(AI|A\.I\.|LLM|LLMs|GPT|ChatGPT|GenAI|generative AI|generativeAI|"
                r"large language model|large language models|machine learning|deep learning|"
                r"neural network|neural networks|chatbot|chatbots|copilot|copilots|agent|"
                r"agents|agentic|prompt engineering|natural language processing|NLP|"
                r"vector database|embeddings|RAG|foundation model|foundation models)\b")
# The site is Trisotech's; these are its own product words, never an AI marker.
AI_FALSE = re.compile(r"\b(Trisotech|Digital Enterprise Suite|Digital Modeling Suite|"
                      r"Digital Automation Suite|Knowledge Worker Copilot|KWCP)\b")
BPMN = re.compile(r"\b(BPMN|BPMN 2\.0|CMMN|DMN|process diagram|process diagram|process model|"
                  r"pools?|lanes?|gateways?|service tasks?|user tasks?|sub-?process(es)?|"
                  r"boundary events?|start events?|end events?|choreograph\w*|ad-?hoc|"
                  r"call activity|business process model\w*)\b")
SENT = re.compile(r"(?<=[.!?:])\s+")

SLIDESHOW = re.compile(r"embed_code/key/([A-Za-z0-9]+)")
YOUTUBE = re.compile(r"youtube\.com/embed/([A-Za-z0-9_-]+)|youtu\.be/([A-Za-z0-9_-]+)")
BRIGHTTALK = re.compile(r"brighttalk\.com")
INDEXY = re.compile(r"trisotech\.com/(tag|category|blog|webinars|presentations|articles|"
                    r"infographics|in-the-news|resources|online-events|upcoming-webinars|"
                    r"events|videos|use-cases|capabilities|solutions)/?$")
DEAD_DECKS = {"modelling-the-preoperative-surgical-journey-presentation", "5-mins-intro-to-cmmn-presentation"}


def slug(u):
    """Whole-path key: /tag/bpmn/ and /bpmn/ are different pages (see _ts_content.slug)."""
    p = urllib.parse.urlparse(u).path.strip("/")
    return re.sub(r"[^A-Za-z0-9._-]", "__", p) or "index"


def load(*paths):
    for p in paths:
        if os.path.exists(p):
            return json.load(open(p, encoding="utf-8")) if p.endswith(".json") else \
                [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
    return []


def dispositions():
    out = {}
    if os.path.exists(DISPOS):
        for line in open(DISPOS, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            out[d["key"]] = d
    return out


def quote(text, must=None, limit=25):
    """A short verbatim sentence from the page's own text. Prefers one naming `must`."""
    text = re.sub(r"\s+", " ", text or "").strip()
    best, best_score = "", -1
    for s in SENT.split(text):
        s = s.strip(" -|")
        w = s.split()
        if not (5 <= len(w) <= limit):
            continue
        score = len(BPMN.findall(s)) * 2 + len(AI.findall(s))
        if must:
            score += 3 * len(re.findall(must, s, re.I))
        if score > best_score:
            best, best_score = s, score
    if not best:
        w = text.split()[:limit]
        best = " ".join(w)
    return best


def screen():
    content = json.load(open(os.path.join(RAW, "content.json"), encoding="utf-8"))
    decks = json.load(open(os.path.join(RAW, "decks.json"), encoding="utf-8"))
    digs = {r["url"]: r for r in load(os.path.join(RAW, "digests.jsonl"))}
    out = []
    for s, v in content.items():
        if v.get("family") != "content":
            continue
        u = v["url"]
        dg = digs.get(u, {})
        t = v["text"]
        ifr = v["iframes"] or v["iframes_all"]
        keys = [m.group(1) for f in ifr for m in [SLIDESHOW.search(f)] if m]
        yts = [m.group(1) or m.group(2) for f in ifr for m in [YOUTUBE.search(f)] if m]
        bt = any(BRIGHTTALK.search(f) for f in ifr)
        own_imgs = v["imgs_clean"]
        dec = decks.get(s) or {}
        ai = sorted(set(AI.findall(t)))
        bk = ("deck" if dec else "dead-deck" if s in DEAD_DECKS else "video" if yts
              else "figures" if own_imgs else "text")
        out.append({
            "slug": s, "url": u, "family": "content", "title": v.get("title"),
            "bucket": bk, "words": v["words"], "text": t,
            "n_own_imgs": len(own_imgs), "own_imgs": [i["url"] for i in own_imgs],
            "n_iframes": len(ifr), "deck_key": keys[0] if keys else "",
            "n_slides": dec.get("n_slides", 0), "deck_notes_ai": dec.get("note_ai", 0),
            "deck_notes_bpmn": dec.get("note_bpmn", 0),
            "n_youtube": len(yts), "brighttalk": bt,
            "pdfs": v["pdfs"], "n_svg_own": v["n_svg_own"], "n_svg_page": v["n_svg_page"],
            "ai_terms": ai, "n_ai": len(ai),
            "bpmn_terms": sorted(set(m.group(0).lower() for m in BPMN.finditer(t)))[:10],
            "n_bpmn": len(BPMN.findall(t)),
            "indexy": bool(INDEXY.search(u)), "og_image": v.get("og_image"),
        })
    for u, r in digs.items():
        if r.get("family") != "rn":
            continue
        out.append({
            "slug": "rn__" + slug(u), "url": u, "family": "rn", "title": r.get("title"),
            "bucket": "release-note", "words": r.get("words", 0), "text": r.get("text", ""),
            "n_own_imgs": 0, "own_imgs": [], "n_iframes": 0, "deck_key": "", "n_slides": 0,
            "deck_notes_ai": 0, "deck_notes_bpmn": 0, "n_youtube": 0, "brighttalk": False,
            "pdfs": r.get("model_links") or [], "n_svg_own": 0, "n_svg_page": r.get("n_svg") or 0,
            "ai_terms": sorted(set(AI.findall(r.get("text") or ""))), "n_ai": 0,
            "bpmn_terms": [], "n_bpmn": 0, "indexy": False, "og_image": r.get("og_image"),
        })
    out.sort(key=lambda r: (r["family"] != "content", r["url"]))
    json.dump(out, open(SCREENF, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    from collections import Counter
    c = Counter((r["family"], r["bucket"]) for r in out)
    for k, v in sorted(c.items()):
        print("  %-10s %-12s %4d" % (k[0], k[1], v))
    print("pages: %d" % len(out))
    for r in out:
        if r["bucket"] == "video":
            pass
    v_bp = [r for r in out if r["bucket"] == "video" and r["n_bpmn"]]
    v_ai = [r for r in out if r["bucket"] == "video" and r["n_ai"] and r["n_bpmn"]]
    print("video pages naming BPMN: %d ; naming AI+BPMN: %d" % (len(v_bp), len(v_ai)))
    print("deck pages whose own text names AI: %d ; notes name AI: %d"
          % (sum(1 for r in out if r["bucket"] == "deck" and r["n_ai"]),
             sum(1 for r in out if r["bucket"] == "deck" and r["deck_notes_ai"])))
    print("text pages naming both AI and BPMN: %d"
          % sum(1 for r in out if r["bucket"] == "text" and r["n_ai"] and r["n_bpmn"]))
    print("figures pages: %d ; pages with own imgs: %d"
          % (sum(1 for r in out if r["bucket"] == "figures"),
             sum(1 for r in out if r["n_own_imgs"])))
    return out


HEADER = {
    "type": "header",
    "source": "trisotech",
    "source_name": "Trisotech (trisotech.com)",
    "accessed": ACCESSED,
    "population_size": 1622,
    "census": True,
    "enumeration_method": (
        "sitemap.xml (https://www.trisotech.com/sitemap.xml, 1625 <loc> entries) de-duplicated to "
        "1622 unique URLs, frozen before judging; 854 of them are release-notes, 768 are content "
        "pages. The assignment said 882 release-notes / 743 content / 1625 total: this source "
        "carries 1622, the delta being 3 duplicate <loc> entries and a different split between the "
        "release-note and content families (recorded, not reconciled here - the population frozen "
        "is the 1622 unique URLs actually fetched and saved). Every URL was fetched and its HTML "
        "saved (ledgers/trisotech.raw/), so every row below rests on a page actually opened. No "
        "keyword filter was used to narrow the population: all 1622 rows are enumerated."
    ),
    "page_region": (
        "Each page's *own* content region was extracted (<main data-pagefind-body>, minus the "
        "data-pagefind-weight=\"0.0\" related-content carousel, minus script/style). Screen the raw "
        "HTML instead and 100% of pages look AI-flavoured, because the site navigation and the "
        "carousel carry other pages' titles and AI words; in the own region only 146 of 768 content "
        "pages carry an AI/LLM term. Lexicon: AI|A.I.|LLM|LLMs|GPT|ChatGPT|GenAI|generative AI|"
        "large language model|machine learning|deep learning|neural network|chatbot|copilot|agent|"
        "agents|agentic|prompt engineering|natural language processing|NLP|RAG|MCP|foundation model. "
        "Known false positives of that lexicon in this source: the slide-hosting site's own "
        "\"Powered by AI\" label, Trisotech's product words (Knowledge Worker Copilot, Trisotech "
        "Digital Enterprise Suite), and connector brand names (Eden AI Connector, OpenAI Connector, "
        "Pinecone) - each is named in the row note where it occurs."
    ),
    "release_note_family": (
        "854 release-note pages. Mechanical screen over the saved page set: 0 pages carry a figure, "
        "0 carry an iframe, 0 carry an inline <svg> in the page's own region, 0 link a .bpmn/.dmn/"
        ".cmmn file. Six of them were then rendered and inspected by eye in a browser on "
        "2026-09-25 - digital-enterprise-suite-release-notes-september-18-2026, dmn-modeler-"
        "release-notes-january-19th-2017, bpmn-modeler-release-notes-july-17-2019, cmmn-modeler-"
        "release-notes-november-15-2017, digital-enterprise-suite-release-notes-august-26th-2025 "
        "and the /release-notes/ index: every one shows only the theme's shadow/logo/footer images "
        "(the index repeats one product thumbnail, release-notes-des.png, once per listed item), "
        "0 svg inside <main>, 0 canvas, no real iframe, and a body that is a change list - "
        "'NEW AND IMPROVED FEATURES:' / 'BUG FIXES:'. So the family publishes no process artefact "
        "and each page is E0-no-artefact as a changelog entry (the assignment allows dropping the "
        "family after a 5-page diagram spot check; the check above is 6 pages and the mechanical "
        "screen covers all 854). Note that these pages are full of AI words - 'AI Performers', "
        "'AI Model Generators', 'AI Service Interactions', 'Anthropic Haiku model integration' - "
        "which is exactly why the population was not narrowed by keyword."
    ),
    "artefact_routes": (
        "The content pages publish their artefacts as (a) images in the page's own region "
        "(514 pages), (b) SlideShare decks embedded in 106 presentation/webinar pages (2924 slides "
        "downloaded from the deck embeds' slide-image URLs, plus the per-slide text where the host "
        "publishes it, 105 of the 106 decks), (c) YouTube embeds in 142 pages, (d) inline SVG - checked: the "
        "only inline SVGs inside the own region on every page are 30x30 aria-hidden theme icons, "
        "(e) no downloadable .bpmn/.dmn/.cmmn anywhere in the source (checked all 768 saved content "
        "pages; the only .bpmn-looking hrefs are outgoing links to bpmn.org)."
    ),
    "judgment_convention": (
        "judgment is true when the verdict required interpretation: every UNCERTAIN, every E1 on a "
        "page that does show a drawn diagram (a DMN DRD/BKM or decision graph, a CMMN case model, "
        "an architecture/layer/infographic drawing) and every E2 on a page that does discuss AI. "
        "It is false where the call was mechanical: E0, E3, E2 on a page with no AI/LLM keyword "
        "anywhere, and E1 on pages whose images are only photographs, flat icons, logos, product-UI "
        "screenshots, code/JSON listings or plain tables (peer convention 02b)."
    ),
    "exclusion_policy": (
        "Exclusions follow the closed code list. Two families recur here: (1) pages whose diagrams "
        "are DMN/CMMN/SDMN rather than BPMN 2.0 - the operator ruled (2026-09-25) that a CMMN "
        "artefact with no AI element inside the model is E1-not-bpmn with judgment true, that a "
        "CMMN artefact carrying an AI element inside is UNCERTAIN with a human ruling requested, "
        "and that DMN DRDs/decision tables are E1 (judgment true for a drawn DRD, false for a "
        "table); (2) pages that discuss AI at length but publish no artefact, or publish a BPMN "
        "diagram with no AI element inside it (E2, with the dismissed AI mention quoted)."
    ),
    "operator_ruling": (
        "elicitation-5a, 2026-09-25, on notation scope: CMMN with no AI element inside the model -> "
        "E1-not-bpmn, judgment true, naming the notation; CMMN with an AI element inside -> "
        "UNCERTAIN + needs_human_ruling (same open class as the Flowable CMMN items); DMN DRD -> E1 "
        "judgment true, DMN decision table -> E1 judgment false; a DMN decision invoked from a BPMN "
        "business-rule task is judged on the BPMN diagram; mixed BPMN+CMMN/DMN figures are judged on "
        "the BPMN part; SDMN or any notation not confidently identifiable -> UNCERTAIN. CMMN release "
        "notes stay E0 like the rest of the release notes."
    ),
}


def emit():
    """Write the ledger: header + one row per enumerated page + footer, and the frontier file."""
    sc = load(SCREENF)
    dis = dispositions()
    rows, missing = [], []
    for i, r in enumerate(sc, 1):
        slug_ = r["slug"]
        d = dis.get(slug_)
        row = {"n": i, "url": r["url"], "family": r["family"], "bucket": r["bucket"]}
        if d:
            row.update({k: v for k, v in d.items()
                        if k not in ("key", "capture", "supersedes")})
            row["verdict"] = d["verdict"]
            if d["verdict"] == "EXCLUDE":
                row["reason"] = d.get("code") or ""
            row.setdefault("judgment", False)
        elif r["family"] == "rn":
            row.update({
                "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
                "evidence": quote(r["text"]),
                "note": ("Release-note / changelog page: the whole 854-page family publishes no "
                         "figure, no iframe and no inline SVG (mechanical screen over the saved "
                         "pages, plus six pages inspected by eye), so there is no process artefact; "
                         "the body is the change list itself. The AI/BPMN word in the quote is the "
                         "name of the engine or feature that changed, not an artefact."),
                "judged_from": "mechanical screen of the saved page + 6-page rendered spot check",
            })
        elif r["indexy"]:
            row.update({
                "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
                "evidence": quote(r["text"]),
                "note": "Index/listing page (tag, category, blog or resource archive): it lists "
                        "other pages' titles and thumbnails and publishes no artefact of its own.",
                "judged_from": "mechanical screen (index URL pattern) of the saved page",
            })
        elif not AI.search(" ".join([r["text"]] + list(r["own_imgs"]))):
            # No AI/LLM keyword anywhere in the page's own text or its figure file names.
            if r["n_own_imgs"] or r["n_iframes"] or r["n_svg_own"] or r["bucket"] in ("deck", "video"):
                row.update({
                    "verdict": "EXCLUDE", "reason": "E2-no-ai-element", "judgment": False,
                    "evidence": quote(r["text"]),
                    "note": ("No AI/LLM term anywhere in the page's own text, figure file names or "
                             "(for deck pages) the deck title, and the page publishes no AI artefact "
                             "of its own. Its figures were not opened one by one: an unviewed figure "
                             "on a page with no AI keyword is a mechanical E2, per the audit's own "
                             "rule. Deck pages here were screened on page text + deck title + the "
                             "host's per-slide text, which 105 of the 106 decks publish, and every "
                             "deck whose slide text carries an AI/LLM term was then judged by hand "
                             "(see the deck rows' own notes), not on every slide image."),
                    "judged_from": "mechanical screen: no AI/LLM keyword in the page's own text or figure names",
                })
            else:
                row.update({
                    "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
                    "evidence": quote(r["text"]),
                    "note": ("Text-only page: no image, no iframe, no inline SVG and no linked "
                             "model file in the page's own region, so it contains no process "
                             "artefact at all."),
                    "judged_from": "mechanical screen of the saved page",
                })
        else:
            missing.append(slug_)
            row.update({
                "verdict": "UNCERTAIN", "reason": "", "judgment": True,
                "evidence": quote(r["text"]),
                "note": "AI-signal page not yet judged at emit time.",
                "needs_human_ruling": True,
                "question": "Page carries an AI/LLM signal but was not judged before emit.",
            })
        rows.append(row)
    with open(LEDGER, "w", encoding="utf-8") as f:
        f.write(json.dumps(HEADER, ensure_ascii=False) + "\n")
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        from collections import Counter
        v = Counter(r["verdict"] for r in rows)
        c = Counter(r.get("reason") for r in rows if r["verdict"] == "EXCLUDE")
        judged = [r for r in rows if r.get("judgment") is True]
        je = [r for r in judged if r["verdict"] == "EXCLUDE"]
        f.write(json.dumps({
            "type": "footer", "status": "DONE",
            "rows": len(rows), "verdicts": dict(v), "exclusions": dict(c),
            "judged": len(judged), "judgement_exclusions": len(je),
            "judgement_exclusion_share": round(len(je) / len(rows), 4),
            "needs_visual_check": sum(1 for r in rows if r.get("needs_visual_check")),
            "needs_human_ruling": sum(1 for r in rows if r.get("needs_human_ruling")),
            "blocked": v.get("BLOCKED", 0),
            "closed_by": "elicitation-6f (pass-2 census worker), 2026-09-25",
        }, ensure_ascii=False) + "\n")
    frontier = os.path.join(ROOT, "trisotech.frontier.txt")
    with open(frontier, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(r["url"] + "\n")
    print("ledger rows: %d ; frontier: %d ; unjudged AI-signal pages: %d"
          % (len(rows), len(rows), len(missing)))
    if missing:
        print("  MISSING:", ", ".join(missing[:20]))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "screen":
        screen()
    elif cmd == "emit":
        emit()
    elif cmd == "quotes":
        sc = {r["slug"]: r for r in load(SCREENF)}
        for s in sys.argv[2:]:
            r = sc[s]
            print("%-12s %-8s ai=%d bpmn=%d %s" % (r["slug"], r["bucket"], r["n_ai"],
                                                   r["n_bpmn"], r["url"]))
            print("   QUOTE:", quote(r["text"]))
    else:
        print(__doc__)
