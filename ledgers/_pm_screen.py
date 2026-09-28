"""Screen every fetched processmaker page offline.

Reads ledgers/processmaker.raw/pages/md/*.md and writes ledgers/processmaker.raw/screen/screen.json:
one record per page with the figure list (standalone images vs inline icons), the AI
sentences, the process/BPMN sentences, and the word count. Nothing here decides a
verdict - it only says which pages a human eye has to look at.
"""
import json, os, re

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "processmaker.raw/pages")
MD = os.path.join(RAW, "md")
HTML = os.path.join(RAW, "html")
OUT = os.path.join(ELI, "processmaker.raw/screen/screen.json")

AI = re.compile(r"\b(ai|a\.i\.|llm|gen ai|generative|gpt|openai|anthropic|claude|gemini|"
                r"watsonx|langflow|mcp|agent|agentic|genie|prompt|embedding|vector|rag|"
                r"machine learning|ml model|copilot|chatbot|natural language|vision model|"
                r"smart assist|predict)\b", re.I)
PROC = re.compile(r"\b(bpmn|process model|process diagram|workflow diagram|pool|lane|gateway|"
                  r"service task|user task|sub-?process|sequence flow|modell?er|object panel|"
                  r"object bar|boundary event|start event|end event|intermediate event|"
                  r"flowgenie object|task)\b", re.I)
FIGLINE = re.compile(r"^\s*!\[[^\]]*\]\((https?://.+)\)\s*$")

AI_DROP = re.compile(r"documentation index|llms\.txt", re.I)


def strip_front(t):
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = {}
    if m:
        for ln in m.group(1).splitlines():
            if ":" in ln:
                k, v = ln.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        t = t[m.end():]
    return fm, t


def sentences(t):
    t = re.sub(r"!\[[^\]]*\]\([^\)]*\)", " ", t)          # drop image markup
    t = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", t)        # links -> their text
    t = re.sub(r"[`*>#|]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]


def slice_html(body):
    """The apidocs pages have no markdown twin: take the rendered article out of the HTML.

    The nav tree, the header and the site chrome live outside `<article
    class="editor360-preview-content">`, so slicing there removes the thousands of
    navigation labels that would otherwise fire the AI screen on every page.
    """
    m = re.search(r"<article[^>]*>(.*?)</article>", body, re.S)
    t = m.group(1) if m else body
    t = re.sub(r"<script.*?</script>", " ", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S)
    imgs = re.findall(r"<img[^>]+src=\"([^\"]+)\"", t)
    t = re.sub(r"<(h[1-6]|p|div|li|tr|br|table)[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
         .replace("&gt;", ">").replace("&#39;", "'").replace("&quot;", '"'))
    return t, imgs


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    pop = json.load(open(os.path.join(RAW, "population.json")))
    titles = json.load(open(os.path.join(RAW, "llms_titles.json")))
    recs = []
    missing = []
    for u in pop:
        slug = re.sub(r"^https://docs\.processmaker\.com", "", u).strip("/").replace("/", "__") or "root"
        f = os.path.join(MD, slug + ".md")
        h = os.path.join(HTML, slug + ".html")
        figs, inline = [], 0
        if os.path.exists(f):
            body = open(f, encoding="utf-8").read()
            fm, t = strip_front(body)
            for ln in t.splitlines():
                m = FIGLINE.match(ln)
                if m:
                    figs.append(m.group(1))
            inline = len(re.findall(r"!\[[^\]]*\]\(", t)) - len(figs)
            src = "md"
        elif os.path.exists(h):
            body = open(h, encoding="utf-8").read()
            fm = {}
            m = re.search(r"<title>(.*?)</title>", body, re.S)
            if m:
                fm["title"] = re.sub(r"\s+", " ", m.group(1)).split("|")[0].strip()
            t, figs = slice_html(body)
            src = "html"
        else:
            missing.append(u)
            continue
        ss = sentences(t)
        ai_s, proc_s = [], []
        for s in ss:
            if AI_DROP.search(s):
                continue
            if AI.search(s) and 8 <= len(s) <= 300:
                ai_s.append(s)
            if PROC.search(s) and 8 <= len(s) <= 300:
                proc_s.append(s)
        recs.append({
            "url": u, "slug": fm.get("slug", slug), "title": fm.get("title", titles.get(u, "")),
            "updated": fm.get("updated", ""), "section": "apidocs" if "/apidocs/" in u else "docs",
            "figures": figs, "n_figures": len(figs), "n_inline_images": inline,
            "words": len(re.findall(r"\w+", t)),
            "ai": bool(ai_s), "proc": bool(proc_s),
            "ai_sentences": ai_s, "proc_sentences": proc_s[:6],
            "bytes": len(body), "file": slug + ("." + src), "src": src,
        })
    json.dump(recs, open(OUT, "w", encoding="utf-8"), indent=0)
    print("screened", len(recs), "missing", len(missing))
    if missing:
        print("MISSING:", missing[:10])
    import collections
    print("with figures:", sum(1 for r in recs if r["n_figures"]))
    print("ai pages:", sum(1 for r in recs if r["ai"]))
    print("ai AND figures:", sum(1 for r in recs if r["ai"] and r["n_figures"]))
    print("proc AND figures:", sum(1 for r in recs if r["proc"] and r["n_figures"]))
    print(collections.Counter(r["section"] for r in recs))


if __name__ == "__main__":
    main()
