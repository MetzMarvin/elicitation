#!/usr/bin/env python3
"""Screens for the bonitasoft/ofelia census (worker elicitation-6f).

Two page shapes in one source:
  * documentation.ofelia.com - Antora HTML; the content is one `<article class="doc">`, figures
    are `<figure class="imageblock">` blocks with `<figcaption class="title">`.
  * www.ofelia.com - Webflow marketing pages; content is one `<main>`, figures are decorative
    `<img>`/`<svg>` from cdn.prod.website-files.com, with no captions.

Everything is read from the crawl cache (ledgers/_bonita/pages/), never re-fetched.

  python ledgers/_bonita_rows.py survey        # what is in the population: figures, tokens
"""
import html as htmlmod
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_bonita"
INDEX = OUT / "index.json"
PAGES = OUT / "pages"

# --- vocabulary -----------------------------------------------------------------------------
# Process-side tokens: words that only appear where a process artefact is being discussed.
PROC = re.compile(
    r"\bBPMN\b|process diagram|process model|\bpool\b|\blane\b|\bgateway\b|sequence flow|"
    r"sub-?process|user task|service task|call activity|\bdiagram\b|\bworkflow\b|"
    r"Bonita Studio|process definition|business process", re.I)

AI = re.compile(
    r"\bAI\b|\bA\.I\.|artificial intelligence|\bLLM\b|large language model|\bagents?\b|"
    r"\bagentic\b|OpenAI|Anthropic|ChatGPT|\bGPT-|Gemini|Mistral|Azure AI|Ollama|DeepSeek|"
    r"\bGroq\b|Cohere|Copilot|machine learning|natural language|prompt", re.I)

# Figure attachments whose *name* announces a diagram/process artefact.
DIAGRAM_NAME = re.compile(
    r"bpmn|diagram|process|workflow|flow|model|pool|lane|gateway|orchestrat|archi|"
    r"sequence|example|tutorial|case|canvas|schema|scheme|graph|chart", re.I)

# BPMN viewer / file evidence, decisive when present.
BPMN_XML = re.compile(r"<bpmn:process|<bpmn:serviceTask|<bpmn:exclusiveGateway|<bpmn:userTask")
BPMN_JS = re.compile(r"djs-element|djs-shape|djs-connection|data-element-id|bpmn-js|"
                     r"bpmn\.io|modeler\.js")
BPMN_FILE = re.compile(r'href="[^"]+\.bpmn"|src="[^"]+\.bpmn"')

# Strict pattern: a figure name/caption that can only belong to a process-diagram artefact.
# Deliberately narrower than DIAGRAM_NAME (which is a survey aid): this one decides who gets
# looked at by eye, so it must not fire on generic product screenshots.
BPMN_FIG = re.compile(
    r"bpmn|process.?diagram|diagram|process.?model|pools?[-_]|lanes?[-_]|gateway|"
    r"workflow|process.?flow|orchestrat|canvas|sequence.?flow|sub-?process|tasklist|"
    r"process[-_]|[-_]process|demo[-_]|[-_]demo", re.I)


def tier(url, sc):
    """'judged' = looked at by eye; 'mech' = decided by the screen alone.

    The two properties need different rules. On the docs portal an AI token is rare and means
    the page is about something AI-related, so any figure there is worth looking at. On the
    marketing site "AI" is in almost every page's copy (the company is "AI-native"), so a figure
    alone proves nothing; what makes a site page worth looking at is a figure *plus* process
    vocabulary, or a figure whose own name/alt/caption announces a diagram.
    """
    if sc["bpmn_js"] or sc["bpmn_xml"] or sc["bpmn_file"] or sc["big_svg"]:
        return "judged"
    if sc["figures"] and sc["ai"] and ("documentation." in url or sc["proc"]):
        return "judged"
    for f in sc["figure_meta"]:
        blob = "%s %s %s" % (f["name"], f["alt"], f["caption"])
        if BPMN_FIG.search(blob):
            return "judged"
    if sc["ai"] and sc["proc"]:
        return "judged"
    return "mech"


def records():
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    out = []
    for url, rec in sorted(idx.items()):
        if rec.get("status") == 200 and rec.get("file") and (PAGES / rec["file"]).exists():
            out.append((url, rec))
    return out


def html_of(rec):
    return (PAGES / rec["file"]).read_text(encoding="utf-8", errors="replace")


def strip_scripts(t):
    t = re.sub(r"<script\b.*?</script>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<style\b.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    return t


# Site chrome (Webflow): the shared navbar / mega-menu / banner / footer are not page content.
# Without removing them the site's own marketing copy ("Build and scale workflows with AI") leaks
# into every page and makes the AI screen fire on all 254 of them.
CHROME = re.compile(r'class="[^"]*(nav_component|nav_fixed|nav_container|nav_menu|menu_offers|'
                    r'\bbanner\b|\bfooter\b|w-nav|dropdown)[^"]*"', re.I)


def drop_blocks(h, tag, cls_rx=CHROME):
    """Remove every balanced <tag ...class matches cls_rx...> ... </tag> block."""
    out, i, n = [], 0, len(h)
    pat = re.compile(r"<%s\b[^>]*>" % tag, re.I)
    while True:
        m = pat.search(h, i)
        if not m:
            out.append(h[i:])
            break
        if not cls_rx.search(m.group(0)):
            out.append(h[i:m.end()])
            i = m.end()
            continue
        out.append(h[i:m.start()])
        depth, j = 1, m.end()
        step = re.compile(r"<%s\b[^>]*?(/?)>|</%s\s*>" % (tag, tag), re.I)
        while depth and j < n:
            s = step.search(h, j)
            if not s:
                j = n
                break
            if s.group(0).startswith("</"):
                depth -= 1
            elif not s.group(1):
                depth += 1
            j = s.end()
        i = j
    return "".join(out)


def region(url, h):
    """The page's own content region: <article> on the docs portal, <main> on the site."""
    if "ofelia.com" in url and "documentation." not in url:
        h = drop_blocks(drop_blocks(h, "div"), "footer")
        m = re.search(r"<main\b[^>]*>(.*?)</main\s*>", h, re.S | re.I)
        if m and len(m.group(1)) > 400:
            return m.group(1)
        m = re.search(r"<body\b[^>]*>(.*?)</body>", h, re.S | re.I)
        return m.group(1) if m else h
    m = re.search(r"<article\b[^>]*>(.*?)</article\s*>", h, re.S | re.I)
    if m and len(m.group(1)) > 400:
        return m.group(1)
    m = re.search(r"<main\b[^>]*>(.*?)</main\s*>", h, re.S | re.I)
    if m and len(m.group(1)) > 400:
        return m.group(1)
    m = re.search(r"<body\b[^>]*>(.*?)</body>", h, re.S | re.I)
    return m.group(1) if m else h


def text(h):
    t = strip_scripts(h)
    t = re.sub(r"<[^>]+>", " ", t)
    t = htmlmod.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def figs(h):
    """[{name, alt, caption, src}] for the figures of a content region (figcaption aware)."""
    out = []
    for m in re.finditer(r"<figure\b[^>]*>(.*?)</figure>", h, re.S | re.I):
        blk = m.group(1)
        img = re.search(r"<img\b[^>]*>", blk, re.I)
        cap = re.search(r"<figcaption\b[^>]*>(.*?)</figcaption>", blk, re.S | re.I)
        src = alt = None
        if img:
            src = (re.search(r'src="([^"]+)"', img.group(0)) or [None, None])[1]
            alt = (re.search(r'alt="([^"]*)"', img.group(0)) or [None, None])[1]
        out.append({"src": src, "alt": htmlmod.unescape(alt or ""),
                    "caption": text(cap.group(1)) if cap else "",
                    "name": (src or "").split("/")[-1].split("?")[0]})
    for m in re.finditer(r"<img\b[^>]*>", h, re.I):
        tag = m.group(0)
        src = (re.search(r'src="([^"]+)"', tag) or [None, None])[1]
        if not src or src.startswith("data:"):
            continue
        if any(f["src"] == src for f in out):
            continue
        alt = (re.search(r'alt="([^"]*)"', tag) or [None, None])[1]
        out.append({"src": src, "alt": htmlmod.unescape(alt or ""), "caption": "",
                    "name": src.split("/")[-1].split("?")[0]})
    return out


def quote(t, rx, maxw=25):
    """First sentence (>=5 words) of `t` matching `rx`, truncated to `maxw` words."""
    for s in re.split(r"(?<=[.!?])\s|\n", t):
        s = s.strip()
        if len(s.split()) >= 5 and rx.search(s):
            w = s.split()
            return " ".join(w[:maxw]) + (" ..." if len(w) > maxw else "")
    return None


def screen(url, h):
    reg = region(url, h)
    t = text(reg)
    fs = figs(reg)
    svgs = re.findall(r"<svg\b.*?</svg>", reg, re.S | re.I)
    big_svg = [s for s in svgs if len(re.findall(r"<", s)) > 40]
    return {
        "url": url,
        "figures": [f["name"] for f in fs],
        "figure_meta": fs,
        "captions": [f["caption"] for f in fs if f["caption"]],
        "diagram_named_figures": [f["name"] for f in fs if DIAGRAM_NAME.search(f["name"] or "")
                                  or DIAGRAM_NAME.search(f["caption"] or "")
                                  or DIAGRAM_NAME.search(f["alt"] or "")],
        "svg": len(svgs),
        "big_svg": len(big_svg),
        "ai": bool(AI.search(t)),
        "proc": bool(PROC.search(t)),
        "ai_quote": quote(t, AI),
        "proc_quote": quote(t, PROC),
        "bpmn_xml": bool(BPMN_XML.search(h)),
        "bpmn_js": bool(BPMN_JS.search(h)),
        "bpmn_file": bool(BPMN_FILE.search(h)),
        "text": t,
    }


def survey():
    recs = records()
    print("cached pages: %d" % len(recs))
    n_fig = n_ai = n_proc = n_both = n_dn = n_bjs = n_bxml = n_bfile = 0
    names = {}
    for url, rec in recs:
        sc = screen(url, html_of(rec))
        n_fig += bool(sc["figures"])
        n_ai += sc["ai"]
        n_proc += sc["proc"]
        n_both += sc["ai"] and sc["proc"]
        n_dn += bool(sc["diagram_named_figures"])
        n_bjs += sc["bpmn_js"]
        n_bxml += sc["bpmn_xml"]
        n_bfile += sc["bpmn_file"]
        for f in sc["figures"]:
            names[f] = names.get(f, 0) + 1
    print("pages with figures      : %d" % n_fig)
    print("pages with AI token     : %d" % n_ai)
    print("pages with process token: %d" % n_proc)
    print("pages with AI + process : %d" % n_both)
    print("pages with diagram-named figure: %d" % n_dn)
    print("pages with bpmn-js markers     : %d" % n_bjs)
    print("pages with bpmn XML            : %d" % n_bxml)
    print("pages with .bpmn link          : %d" % n_bfile)
    print("unique figure names: %d" % len(names))
    print("--- most common figure names ---")
    for k, v in sorted(names.items(), key=lambda kv: -kv[1])[:60]:
        print("  %4d  %s" % (v, k))
    print("--- names matching the diagram-name screen ---")
    hit = sorted(k for k in names if DIAGRAM_NAME.search(k or ""))
    for k in hit[:120]:
        print("  %4d  %s" % (names[k], k))
    print("  (%d of %d unique names)" % (len(hit), len(names)))


def flag():
    """The worklist: every page the screen sends to judgement, with what fired."""
    recs = records()
    judged = []
    for url, rec in recs:
        sc = screen(url, html_of(rec))
        if tier(url, sc) == "judged":
            judged.append((url, sc))
    print("cached %d | judged %d | mechanical %d" % (len(recs), len(judged), len(recs) - len(judged)))
    for url, sc in sorted(judged):
        why = []
        if sc["bpmn_js"]:
            why.append("bpmn-js")
        if sc["bpmn_xml"]:
            why.append("bpmn-xml")
        if sc["bpmn_file"]:
            why.append(".bpmn-link")
        if sc["big_svg"]:
            why.append("big-svg")
        if sc["figures"] and sc["ai"]:
            why.append("fig+ai")
        for f in sc["figure_meta"]:
            blob = "%s %s %s" % (f["name"], f["alt"], f["caption"])
            if BPMN_FIG.search(blob):
                why.append("fig-name")
                break
        if sc["ai"] and sc["proc"]:
            why.append("ai+proc")
        print("-" * 100)
        print("%s   [%s]" % (url, ",".join(why)))
        print("   figs: %s" % (", ".join(sc["figures"])[:150] or "-"))
        print("   ai  : %s" % (sc["ai_quote"] or "-"))
        print("   proc: %s" % (sc["proc_quote"] or "-"))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "survey"
    if mode == "survey":
        survey()
    elif mode == "flag":
        flag()
