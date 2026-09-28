#!/usr/bin/env python3
"""Screens and text helpers for the scheer-pas ledger rows.

The docs site is Confluence/Scroll Sites: every page has one `<article id="content">` whose
`<section class="article-body ...">` holds the prose and the figures. The site chrome (the docs
navigation, the cookie notice, the "Ask the PAS Chatbot!" banner) sits OUTSIDE the article, which
matters here because the chrome carries AI words on every page - the screen must not read them.
"""
import html as _html
import re

# --- process-model language ---------------------------------------------------------------------
# Strong tokens: naming a process MODEL/notation. A page carrying one of these is judged by eye.
PROC = (r"\bBPMN\b|business process(es)?\b|process model|process diagram|process design|"
        r"\bgateway\b|\bpool\b|\blane\b|sub-?process|execution model|activity diagram|"
        r"xUML service|process element|start event|end event|user task|service task|"
        r"process step|modeling process|process editor")
# Weaker: talking about a process at all (used for the "no process language" claim in the E0 note).
PROC_WEAK = r"\bprocess(es)?\b|\bworkflow\b|\bmodel(l)?ing\b"

# --- AI -----------------------------------------------------------------------------------------
AI = (r"\bAI\b|\bAI[- ][A-Za-z]+|artificial intelligence|\bLLM(s)?\b|\bGPT\b|OpenAI|Mistral|"
      r"Microsoft Foundry|machine learning|\bML\b|deep learning|neural|large language model|"
      r"prompt engineering|\bRAG\b|embedding|Sub-?agent|AI agent|AI service provider")
SOFT = r"agent|assistant|copilot|chatbot|intelligen|automat"

# figure file names that name a diagram, used for the site-wide name-level backstop sweep
DIAGRAM_NAME = (r"bpmn|diagram|process|workflow|model|gateway|pool|lane|canvas|flow|editor|"
                r"chart|graph|sequence|activity")

VERSION_RE = re.compile(r'version:\s*"([^"]+)"')
ART_RE = re.compile(r'<article id="content".*?</article>', re.S)
CHROME_CUT = ("Ask the PAS Chatbot", "Was this article helpful", "Related Content",
              "Powered by", "Privacy Preference")


def article(t):
    """The page's own region (prose + figures), with the docs chrome removed."""
    m = ART_RE.search(t)
    return m.group(0) if m else t


def text(t, cut_chrome=True):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)<br\s*/?>|</(p|li|h[1-6]|div|tr)>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = _html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    if cut_chrome:
        for c in CHROME_CUT:
            i = t.find(c)
            if i > 400:
                t = t[:i]
    return t.strip()


def body(t):
    """The page's prose region only."""
    return text(article(t))


def figs(t):
    """The page's figures as [{src, alt}] - only those inside the article region."""
    a = article(t)
    out = []
    for m in re.finditer(r"<img\b[^>]*>", a, re.I):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        if not src:
            continue
        s = _html.unescape(src.group(1))
        if s.startswith("/__site/") or s.startswith("/__theme/"):
            continue  # chrome assets (logo, icons)
        out.append({"src": s, "alt": _html.unescape(alt.group(1)) if alt else ""})
    return out


def version(t):
    m = VERSION_RE.search(t)
    return m.group(1) if m else None


def quote(t, rx, maxw=25):
    """The first sentence of the page (<= maxw words) that matches rx - the verbatim evidence."""
    for s in re.split(r"(?<=[.!?])\s|\n", text(t)):
        s = " ".join(s.split())
        if len(s.split()) >= 5 and re.search(rx, s, re.I):
            w = s.split()
            return " ".join(w[:maxw]) + (" ..." if len(w) > maxw else "")
    return None
