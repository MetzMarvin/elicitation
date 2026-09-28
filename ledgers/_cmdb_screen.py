"""camunda-docs-blog: screen the saved blog HTML -> screen.jsonl.

One JSON object per post so that every later evidence quote can be tested as a contiguous
substring of `text`, and so the mechanical screen (no process artefact / no AI term) can be
re-run and audited.

Row: n, url, title, text, imgs[{src,alt,caption,w,h}], files[.bpmn...], n_ai, hits, n_bpmn,
bpmn_terms[...], yt (embedded youtube ids), has_fig

Usage: python ledgers/_cmdb_screen.py [start_n]
Resumable: a post already present in screen.jsonl is skipped.
"""
import html, json, os, re, sys, urllib.parse

RAW = "ledgers/camunda-docs-blog.raw"
BLOG = os.path.join(RAW, "blog")
FRONTIER = "ledgers/camunda-docs-blog.frontier.txt"

AI_TERMS = ["artificial intelligence", "Artificial Intelligence", "AI agent", "AI Agent",
            "AI-powered", "AI powered", "GenAI", "generative AI", "Generative AI", "LLM",
            "large language model", "machine learning", "machine-learning", "neural",
            "chatbot", "copilot", "Copilot", "GPT", "OpenAI", "Anthropic", "Claude", "Gemini",
            "prompt", "embedding", "RAG", "retrieval-augmented", "agentic", "Agentic",
            "AI ", "AI,", "AI.", "AI-", "AI/", "agent", "Agent", "agents", "intelligent"]
BPMN_TERMS = ["BPMN", "bpmn", "ad-hoc sub-process", "ad hoc sub-process", "adHocSubProcess",
              "bpmn-js", "Modeler", "modeler", "gateway", "sub-process", "subprocess",
              "process diagram", "pool", "lane", "user task", "service task", "process model",
              ".bpmn", "Camunda Modeler"]


def strip_html(h):
    h = re.sub(r"(?is)<script.*?</script>", " ", h)
    h = re.sub(r"(?is)<style.*?</style>", " ", h)
    h = re.sub(r"(?is)<noscript.*?</noscript>", " ", h)
    m = re.search(r"(?is)<main[^>]*>(.*?)</main>", h)
    body = m.group(1) if m else h
    body = re.sub(r"(?is)<(br|/p|/div|/li|/h[1-6]|/tr|/figcaption)>", "\n", body)
    body = re.sub(r"(?s)<[^>]+>", " ", body)
    body = html.unescape(body)
    body = re.sub(r"[ \t\r\f\v]+", " ", body)
    body = re.sub(r"\n\s*\n+", "\n", body)
    return body.strip()


def main(start=1):
    rows = [l.rstrip("\n").split("\t", 1) for l in open(FRONTIER, encoding="utf-8")]
    path = os.path.join(RAW, "screen.jsonl")
    done = set()
    if os.path.exists(path):
        for l in open(path, encoding="utf-8"):
            try:
                done.add(json.loads(l)["n"])
            except Exception:
                pass
    out = open(path, "a", encoding="utf-8")
    for n, url in rows:
        n = int(n)
        if n < start or n in done:
            continue
        p = os.path.join(BLOG, "%04d.html" % n)
        if not os.path.exists(p) or os.path.getsize(p) < 2000:
            continue
        h = open(p, encoding="utf-8", errors="replace").read()
        text = strip_html(h)
        # drop the cookie/consent boilerplate that appears on every page
        text = re.sub(r"(?is)We use cookies.*?privacy policy\.", " ", text)
        mt = re.search(r"(?is)<title[^>]*>(.*?)</title>", h)
        title = html.unescape(re.sub(r"\s+", " ", mt.group(1)).strip()) if mt else ""
        caps = [html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c))).strip()
                for c in re.findall(r"(?is)<figcaption[^>]*>(.*?)</figcaption>", h)]
        imgs, seen = [], set()
        region = re.search(r"(?is)<main[^>]*>(.*)</main>", h)
        body = region.group(1) if region else h
        for m in re.finditer(r"(?is)<(img|source)([^>]*)>", body):
            attrs = m.group(2)
            cands = []
            for a in re.finditer(r'(?i)\b(?:src|srcset)=["\']([^"\']+)["\']', attrs):
                for part in a.group(1).split(","):
                    cands.append(part.strip().split(" ")[0])
            for src in cands:
                if not src:
                    continue
                src = html.unescape(src)
                if "images.weserv.nl" in src or src.startswith("data:"):
                    continue
                if "/_next/image" in src or "url=" in src and src.startswith("/_next/"):
                    q = re.search(r"[?&]url=([^&]+)", src)
                    if q:
                        src = urllib.parse.unquote(q.group(1))
                if src.startswith("//"):
                    src = "https:" + src
                elif src.startswith("/"):
                    src = "https://camunda.com" + src
                if src in seen:
                    continue
                seen.add(src)
                alt = re.search(r'(?i)\balt=["\']([^"\']*)["\']', attrs)
                w = re.search(r'(?i)\bwidth=["\']?(\d+)', attrs)
                hh = re.search(r'(?i)\bheight=["\']?(\d+)', attrs)
                kind = "svg" if src.lower().split("?")[0].endswith(".svg") else "raster"
                imgs.append({"src": src,
                             "alt": html.unescape(alt.group(1)) if alt else "",
                             "w": int(w.group(1)) if w else 0,
                             "h": int(hh.group(1)) if hh else 0,
                             "kind": kind})
        files, seenf = [], set()
        for m in re.finditer(r'(?i)(https?://[^\s"\'<>()]+\.(?:bpmn|dmn|cmmn))(?![\w.])', h):
            s = m.group(1)
            if s not in seenf:
                seenf.add(s)
                files.append(s)
        yt = []
        for m in re.finditer(r'(?i)(?:youtube\.com/embed/|youtu\.be/|youtube\.com/watch\?v=)([A-Za-z0-9_-]{8,})', h):
            if m.group(1) not in yt:
                yt.append(m.group(1))
        og = ""
        mo = re.search(r'(?i)<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', h) or \
             re.search(r'(?i)<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', h)
        if mo:
            og = urllib.parse.unquote(html.unescape(mo.group(1)))
        hits = {t: text.count(t) for t in AI_TERMS if t in text}
        bt = [t for t in BPMN_TERMS if t in text]
        row = {"n": n, "url": url, "title": title, "text": text, "imgs": imgs,
               "caps": caps, "files": files, "yt": yt, "og": og, "n_ai": sum(hits.values()),
               "hits": hits, "bpmn_terms": bt,
               "n_bpmn": sum(text.count(t) for t in bt),
               "has_fig": bool(re.search(r"(?is)<figure|<figcaption|<picture", h))}
        out.write(json.dumps(row, ensure_ascii=False) + "\n")
        out.flush()
        if n % 100 == 0:
            print("screened", n, flush=True)
    out.close()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    print("screen done")
