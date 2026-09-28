"""camunda-docs-blog: write the corpus records for the accepted items.

  python ledgers/_cmdb_gen.py plan  N [N ...]     # what each record would say; writes nothing
  python ledgers/_cmdb_gen.py write N [N ...]     # corpus/camunda-docs-blog/NNN_<slug>.md + capture
  python ledgers/_cmdb_gen.py manifest            # rebuild raw/records.json from the corpus dir

Why a generator rather than free-hand writing. The census has ~350 accepted items, each of
which needs a record whose quotes are verbatim from the page. Every quote this script puts in
a record is *taken from the saved page itself* - its DOM text, its figure alt texts, its model
XML - so the evidence rule holds by construction rather than by care. `_cmdb_verify.py`
re-checks the result against the same material afterwards.

The numbered capture is the figure the record is about, downloaded at w=1400 from the asset
URL the page names (cdn.sanity.io) and stored as PNG beside the record.

Figure choice: `pick()` scores every figure of the post on its alt text and on the
contact-sheet reading of the same asset, and takes the best - the artefact, not the title
card. `raw/gen_overrides.json` can force one: {"<n>": {"fig": <index in `_cmdb_rec.py all N`>,
"why": "..."}}.
"""
import json, os, re, sys

from PIL import Image

import _cmdb_aijudge as A
import _cmdb_figs as F
import _cmdb_final as G
import _cmdb_shots as S

RAW = "ledgers/camunda-docs-blog.raw"
IMGS = os.path.join(RAW, "imgs")
CORPUS = "corpus/camunda-docs-blog"
OVERRIDES = os.path.join(RAW, "gen_overrides.json")
MANIFEST = os.path.join(RAW, "records.json")
ACCESSED = "2026-09-26"

PROC = re.compile(r"(?i)\b(bpmn|process|diagram|workflow|model|gateway|lane|sub-?process|"
                  r"flow ?chart|orchestration)\b")
TASKW = re.compile(r"(?i)\b(task|activity|service task|user task|connector|agent|gateway|"
                   r"event|sub-?process)\b")
CARDW = re.compile(r"(?i)cover|featured|banner|title card|header image|social")
UNREADW = re.compile(r"(?i)unreadable|illegible|not legible|cannot read|too small|too tiny|"
                     r"blurry|blurred|faint|cut off")
HUMANW = re.compile(r"(?i)\b(human|approv\w*|review|threshold|guardrail|confidence|validat\w*|"
                    r"check|escalat\w*|oversight|manual)\b")
DOWNW = re.compile(r"(?i)\b(routes?|routing|sends?|creates?|generates?|triggers?|assigns?|"
                   r"forwards?|decides?|decision|approves?|escalates?|updates?|tickets?|emails?|"
                   r"downstream|next step|hands? off|hand-off|writes? (back|to)|invokes?|"
                   r"response|reply|notification)\b")
DATAW = re.compile(r"(?i)\b(variables?|data|inputs?|documents?|fields?|json|payload|extract\w*|"
                   r"parse\w*|information|customer record|results?|outputs?)\b")
CTRLW = re.compile(r"(?i)\b(gateways?|guards?|guardrails?|thresholds?|conditions?|rules?|retry|"
                   r"errors?|escalat\w*|timeouts?|decision table|decision tables|dmn|exclusive|"
                   r"branch(es|ing)?)\b")
INW = re.compile(r"(?i)\b(from the|incoming|requests?|customers?|forms?|documents?|emails?|"
                 r"messages?|trigger\w*|start events?|submitted|received|submissions?|"
                 r"applications?)\b")
MODELW = re.compile(r"(?i)\b(gpt-?[0-9o]|openai|claude|anthropic|bedrock|vertex|gemini|llama|"
                    r"mistral|ollama|hugging ?face|comprehend|textract|model id|model name|"
                    r"system prompt|user prompt|prompt template|temperature|embeddings?|"
                    r"large language model)\b")


# ---------------------------------------------------------------- page material

def lines(r):
    out = []
    for line in (r.get("text") or "").split("\n"):
        line = " ".join(line.split())
        if len(line) >= 30 and not line.startswith("Read more"):
            out.append(line)
    return out


# lines that are calls to action or shell instructions rather than statements about the
# process: they match a keyword but say nothing about the artefact
NOISE = re.compile(r"(?i)(check out (this|our)|read more|sign ?up|subscribe|follow us|"
                   r"click here|register (now|here|for)|join us|learn more about our|"
                   r"run the following command|npm |docker |pip install|curl -|git clone|"
                   r"share (this|your)|let us know|stay tuned|book a demo|download the|"
                   r"watch the (video|recording)|this blog post|[\\{}<>]|--data|=\s*@)")


def find(r, pat, avoid=(), minimum=30):
    rx = pat if hasattr(pat, "search") else re.compile(pat)
    for line in lines(r):
        if len(line) < minimum or not rx.search(line):
            continue
        if NOISE.search(line):
            continue
        if any(a and a in line for a in avoid):
            continue
        return line
    return ""


def best(r, pat, avoid=(), bonus=(), minimum=30, floor=1.6):
    """the page line that best states what the bullet asks for: the pattern must match, and the
    line is scored on how many of its terms it carries, so a passing mention of one word does
    not win over a sentence that is about the thing. Under `floor` the bullet reports nothing
    rather than a loose association."""
    rx = pat if hasattr(pat, "search") else re.compile(pat)
    bx = [b if hasattr(b, "search") else re.compile(b) for b in bonus]
    top, score = "", 0.0
    for line in lines(r):
        if len(line) < minimum or NOISE.search(line):
            continue
        if any(a and a in line for a in avoid):
            continue
        hits = len(rx.findall(line))
        if not hits:
            continue
        s = hits + sum(1 for b in bx if b.search(line))
        s += 0.5 * min(len(line), 300) / 300.0        # a fuller sentence beats a fragment
        if s > score:
            top, score = line, s
    return top if score >= floor else ""


def q(s, words=25):
    """a verbatim prefix of a page line, at or under the 25-word quote cap, cut at a sentence
    end inside the window when there is one (so the quote reads as a complete thought)."""
    if not s:
        return ""
    w = s.split()
    if len(w) <= words:
        return " ".join(w)
    head = w[:words]
    for i in range(len(head) - 1, 5, -1):
        if head[i].endswith((".", "?", "!", ":")):
            return " ".join(head[:i + 1])
    return " ".join(head)


def span(line, rx, words=25):
    """a verbatim quote that actually shows the term the bullet matched. The quote is the
    sentence of the line carrying most hits of the pattern, or - if that sentence is longer
    than the cap - a 25-word window of it centred on the first hit. Always a contiguous run of
    the page's own words, so the verbatim check still holds."""
    if not line:
        return ""
    sents = re.split(r"(?<=[.!?])\s+", line)
    target = sents[0]
    if len(sents) > 1:
        hits = [(len(rx.findall(s)), s) for s in sents]
        target = max(hits, key=lambda t: t[0])[1]
    w = target.split()
    if len(w) <= words:
        return " ".join(w)
    m = rx.search(target)
    if m:
        before = len(target[:m.start()].split())
        start = max(0, min(before - 4, len(w) - words))
        return " ".join(w[start:start + words])
    return q(target, words)


def ai_lines(r):
    return A.find(r, A.INSIDE)


def ai_outside(r):
    return A.find(r, A.OUTSIDE)


# ---------------------------------------------------------------- figures

def sheet_cells(r, vnt):
    """src -> (class, ai_visible, note) for the cells the contact sheets cover."""
    out = {}
    for k, f in enumerate(S.selected(r), 1):
        c = vnt.get("%d.%d" % (r["n"], k))
        if c:
            out[f["src"]] = c
    return out


def every(r):
    """every figure of the post, numbered as `_cmdb_rec.py all N` numbers them (diagram-like
    alt texts first), so a capture hint or a gen_overrides entry can name a figure the way the
    subagent that read it at full width saw it."""
    fs = F.figs(r)
    fs.sort(key=lambda f: (0 if F.DIAG.search(f["alt"]) else 1, -f["w"] * f["h"]))
    return fs


def pick(r, vnt, hint=None):
    """(index in `_cmdb_rec.py all N` order, why) - the figure the record is about."""
    fs = every(r)
    if not fs:
        return 0, "no figure on the page"
    cells = sheet_cells(r, vnt)
    over = (json.load(open(OVERRIDES, encoding="utf-8")).get(str(r["n"]))
            if os.path.exists(OVERRIDES) else None)
    if over:
        return int(over["fig"]), "forced by gen_overrides.json: %s" % over.get("why", "")
    if hint:
        m = re.search(r"(?i)figure\s*(\d+)", hint)
        if m:
            k = int(m.group(1))
            sel = S.selected(r)
            if 1 <= k <= len(sel):
                src = sel[k - 1]["src"]
                for i, f in enumerate(fs, 1):
                    if f["src"] == src:
                        return i, "the ruling named figure %d (sheet numbering)" % k
    best, why = 1, "the page's largest figure (no better signal)"
    score = None
    for i, f in enumerate(fs, 1):
        c = cells.get(f["src"])
        note = c[2] if c else ""
        s = 0.0
        if PROC.search(f["alt"]):
            s += 3
        if TASKW.search(f["alt"]):
            s += 1
        if f["alt"] and CARDW.search(f["alt"]):
            s -= 4
        if note and PROC.search(note):
            s += 2
        if note and TASKW.search(note):
            s += 1
        if note and UNREADW.search(note):
            s -= 3
        if c and c[0] in ("bpmn", "other-diagram"):
            s += 2
        s += min(f["w"], 2400) / 8000.0            # mild preference for resolution
        if score is None or s > score:
            best, score = i, s
            why = ("alt %r + sheet note %r" % (f["alt"][:50] or "(none)", (note or "")[:60])
                   if (f["alt"] or note) else "largest figure")
    return best, why


def capture(r, i, path):
    """download figure i (1-based, `all N` order) at w=1400 and store it at `path` (PNG)."""
    f = every(r)[i - 1]
    tmp = path + ".jpg"
    S.get(f["src"], tmp, 1400)
    if not (os.path.exists(tmp) and os.path.getsize(tmp) > 5000):
        return None
    im = Image.open(tmp).convert("RGB")
    im.save(path, "PNG")
    os.remove(tmp)
    return im.size


def quality(r, i, vnt):
    f = every(r)[i - 1]
    c = sheet_cells(r, vnt).get(f["src"])
    note = c[2] if c else ""
    if note and UNREADW.search(note) and f["w"] < 1200:
        return "poor"
    if f["w"] < 900 or (note and UNREADW.search(note)):
        return "marginal"
    return "legible"


# ---------------------------------------------------------------- naming

def slug(url):
    s = url.rstrip("/").split("/")[-1].split("?")[0]
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:70] or "post"


def manifest():
    """{n: record path} for the records already on disk, from their own frontmatter."""
    out = {}
    for p in sorted(os.listdir(CORPUS)):
        if not p.endswith(".md"):
            continue
        head = open(os.path.join(CORPUS, p), encoding="utf-8").read(1200)
        m = re.search(r"^n:\s*(\d+)\s*$", head, re.M)
        if m:
            out[int(m.group(1))] = "%s/%s" % (CORPUS, p)
    return out


def numbers():
    return sorted(int(p[:3]) for p in os.listdir(CORPUS) if re.match(r"^\d{3}_", p)
                  and p.endswith(".md"))


# ---------------------------------------------------------------- the record

def yq(v):
    """a YAML double-quoted scalar. Double quotes inside are escaped, never rewritten: a quote
    field has to stay verbatim, and the verifier unescapes them again."""
    if not v:
        return "null"
    return '"%s"' % str(v).replace("\\", "\\\\").replace('"', '\\"')


def bullets(r, vnt, cls, aiv, i, fig):
    """the eight fixed observation bullets, each from page material or 'not visible'."""
    ins = ai_lines(r)
    out = ai_outside(r)
    c = sheet_cells(r, vnt).get(fig["src"]) if fig else None
    seen = [x[1] for x in ins] + [x[1] for x in out]
    alt = fig["alt"] if fig else ""
    note = c[2] if c else ""
    B = []

    # 1 function
    if ins:
        name, line = ins[0]
        rest = [x for x in ins[1:3]]
        s = ('the page\'s own words bind the AI to the process: "%s" - the AI-bearing element it '
             'names is %s' % (q(line), name))
        if rest:
            s += '; elsewhere: "%s" (%s)' % (q(rest[0][1]), rest[0][0])
    elif out:
        s = ('the page mentions AI only around the process - "%s" refers to %s, not to an '
             'element inside it; no AI function is described inside the process itself'
             % (q(out[0][1]), out[0][0]))
    else:
        s = "not visible on the page - the post names no AI/LLM activity"
    B.append(("AI activity - function", s))

    # 2 element type
    if c:
        s = ('the captured figure is what the contact-sheet pass read as class "%s" '
             '(ai_visible=%s), in its words: %s' % (c[0], c[1], note[:200] or "(no note)"))
    elif alt:
        s = 'the page gives the figure the alt text "%s"; no element-template binding is visible' % alt[:80]
    else:
        s = "not visible on the page"
    B.append(("AI activity - element type", s))

    # 3-7: one distinct page line each, never the same line twice
    used = list(seen)
    AIW = re.compile(r"(?i)\b(ai|llm|model|agent|gpt|openai|claude|prompt)\b")

    def pick_line(pat, miss, bonus=(AIW,), floor=2.0):
        l = best(r, pat, avoid=used, bonus=bonus, floor=floor)
        if l:
            used.append(l)
            rx = pat if hasattr(pat, "search") else re.compile(pat)
            return 'the page: "%s"' % span(l, rx)
        return miss

    B.append(("Authority - downstream", pick_line(
        DOWNW, "not visible on the page - the page does not say what the AI's output acts on")))
    B.append(("Authority - data", pick_line(
        DATAW, "not visible on the page - no variable, payload or document is named")))
    B.append(("Authority - control", pick_line(
        CTRLW, "not visible on the page - no gateway, threshold or routing rule is named")))
    B.append(("Input provenance", pick_line(
        INW, "not visible on the page - the page does not name where the AI's input comes from",
        bonus=(), floor=1.2)))
    B.append(("Guards present", pick_line(
        HUMANW, "not visible on the page - no human review, threshold or validation step is named",
        bonus=(), floor=1.2)))
    B.append(("Prompt / model detail visible", pick_line(
        MODELW, "not visible on the page - no model name, prompt text or parameter is printed",
        bonus=(), floor=1.2)))
    return B


def title(r):
    return re.sub(r"\s*\|\s*Camunda\s*$", "", r.get("title") or "").strip()


def body(r, vnt, cls, aiv, ruling, i, fig, quality_note, bpmn_xml=None):
    v, reason, judg, ev, note, nvc, question = ruling[:7]
    ins = ai_lines(r)
    out = ai_outside(r)
    L = []
    L.append("## What the page shows")
    L.append("")
    what = find(r, re.compile(r"(?i)\b(this (post|article|blog)|we (will|are going to) (show|walk)|"
                              r"in this (post|tutorial|guide))\b"))
    first = ins[0][1] if ins else (out[0][1] if out else (lines(r)[0] if lines(r) else ""))
    L.append('The post is Camunda\'s own write-up of "%s".' % title(r))
    if what and what != first:
        L.append('It opens on its subject directly: "%s"' % q(what, 30))
    if first:
        L.append('The line the record quotes on the AI element is: "%s"' % q(first, 30))
    L.append("")
    if fig:
        c = sheet_cells(r, vnt).get(fig["src"])
        L.append('The captured figure is the page\'s %dx%d asset%s. The contact-sheet pass over '
                 'the same asset read it as class "%s" with ai_visible=%s, in its own words: %s'
                 % (fig["w"], fig["h"],
                    ' with alt text "%s"' % fig["alt"][:90] if fig["alt"] else " with no alt text",
                    c[0] if c else "-", c[1] if c else "-", (c[2] if c else "(not in the sheets)")))
    elif bpmn_xml:
        L.append("The page links a BPMN model; the record captures that XML, which is the "
                 "artefact itself rather than a picture of one.")
    L.append("")
    L.append("## Observations (description only, no interpretation)")
    L.append("")
    for name, s in bullets(r, vnt, cls, aiv, i, fig):
        L.append("- **%s:** %s" % (name, s))
    L.append("")
    L.append("## Notes for the researcher")
    L.append("")
    if v == "UNCERTAIN":
        L.append("**This item is UNCERTAIN and needs a human ruling.** Open question: %s" % question)
        L.append("")
    L.append("The AI call here rests on %s. %s"
             % ("the page's own words, not on a reading of the figure" if ins else
                "the material above",
                ("The page does mention AI, but only around the process - %s."
                 % ", ".join(sorted({x[0] for x in out}))) if (out and not ins) else ""))
    L.append("")
    L.append("Capture: %s" % quality_note)
    return "\n".join(L).rstrip() + "\n"


def over(n):
    if not os.path.exists(OVERRIDES):
        return {}
    return json.load(open(OVERRIDES, encoding="utf-8")).get(str(n)) or {}


def record(n, cls, aiv, vnt, num, force=None):
    r = next(x for x in F.rows() if x["n"] == n)
    ruling = G.RULED.get(n) or G.model_verdict(r, cls) or G.classify(r, cls, aiv, vnt)
    if ruling is None:
        return None, "no ruling (the page links a model: judged from the XML)"
    v, reason, judg, ev, note, nvc, question = ruling[:7]
    if v not in ("INCLUDE", "UNCERTAIN"):
        return None, "verdict %s (%s): the ledger row needs no record" % (v, reason)
    ov = over(n)
    hint = ruling[7] if len(ruling) > 7 else None
    fs = every(r)
    i, why = pick(r, vnt, hint)
    fig = fs[i - 1] if fs else None
    sl = slug(r["url"])
    name = force or "%03d_%s" % (num, sl)
    xmldir = os.path.join(RAW, "bpmn")
    xmls = sorted(x for x in os.listdir(xmldir) if x.startswith("%04d_" % n)) \
        if os.path.isdir(xmldir) else []
    bpmn_xml = "%s.bpmn" % name if xmls else None
    shot = "%s.png" % name if fig else None

    fm = []
    fm.append("---")
    fm.append("n: %d" % n)
    fm.append("source: camunda-blog")
    fm.append("source_name: Camunda (vendor blog)")
    fm.append("source_type: vendor blog")
    fm.append("title: %s" % yq(title(r)))
    fm.append("url: %s" % r["url"])
    fm.append("accessed: %s" % ACCESSED)
    fm.append("verdict: %s" % v)
    fm.append("needs_human_ruling: %s" % ("true" if v == "UNCERTAIN" else "false"))
    fm.append("question: %s" % (yq(question) if v == "UNCERTAIN" and question else "null"))
    fm.append("needs_visual_check: %s" % ("true" if nvc else "false"))
    fm.append("bpmn_evidence: %s" % yq(bpmn_ev(r, vnt, cls, i, fig)))
    fm.append("bpmn_evidence_quote: %s" % yq(bpmn_quote(r, cls, i, fig)))
    fm.append("ai_evidence: %s" % yq(ov.get("ai_evidence") or ai_ev(r, i, fig, vnt)))
    fm.append("ai_evidence_quote: %s" % yq(ov.get("ai_quote") or ai_quote(r)))
    fm.append("artefacts:")
    fm.append("  screenshot: %s" % (shot or "null"))
    fm.append("  archive: null")
    fm.append("  bpmn_xml: %s" % (bpmn_xml or "null"))
    fm.append("duplicate_of: null")
    fm.append("access: public")
    fm.append("capture_source: original-asset")
    fm.append("capture_quality: %s" % (quality(r, i, vnt) if fig else "null"))
    fm.append("capture_width_px: %s" % (fig["w"] if fig else "null"))
    fm.append("capture_method: figure downloaded at w=1400 from the asset URL the saved page "
              "names (cdn.sanity.io), fetched %s" % ACCESSED)
    fm.append("---")
    qnote = ("the page's %dx%d asset, downloaded at w=1400 and stored as %s; the contact-sheet "
             "reading of the same asset is class %s / ai_visible %s. Figure choice: %s."
             % (fig["w"], fig["h"], shot,
                (sheet_cells(r, vnt).get(fig["src"]) or ("-", "-", ""))[0],
                (sheet_cells(r, vnt).get(fig["src"]) or ("-", "-", ""))[1], why)
             if fig else
             "the page links a BPMN model; the record captures that XML as %s." % bpmn_xml)
    text = "\n".join(fm) + "\n\n" + body(r, vnt, cls, aiv, ruling, i, fig, qnote, bpmn_xml)
    return (name, text, fig, i), ruling


def bpmn_ev(r, vnt, cls, i, fig):
    c = sheet_cells(r, vnt).get(fig["src"]) if fig else None
    prose = find(r, re.compile(r"(?i)\bbpmn\b"))
    s = "the artefact is the figure the record captures"
    if c:
        s = ("the visual pass reads the captured figure as class %r: %s"
             % (c[0], c[2][:180] or "no note"))
    if prose:
        s += '; the page names BPMN itself: "%s"' % q(prose, 20)
    return s


def bpmn_quote(r, cls, i, fig):
    prose = find(r, re.compile(r"(?i)\bbpmn\b"))
    if prose:
        return q(prose)
    if fig and fig["alt"]:
        return q(fig["alt"])
    for line in lines(r):
        if PROC.search(line):
            return q(line)
    return q(lines(r)[0]) if lines(r) else ""


def ai_ev(r, i, fig, vnt):
    ins = ai_lines(r)
    out = ai_outside(r)
    if ins:
        names = ", ".join(sorted({x[0] for x in ins}))
        return ('the page binds AI to a process element (%s): "%s"%s'
                % (names, q(ins[0][1]),
                   '; the contact-sheet pass reads the captured figure as ai_visible=%s'
                   % (sheet_cells(r, vnt).get(fig["src"]) or ("-", "-", ""))[1] if fig else ""))
    if out:
        return ('AI appears only around the process (%s): "%s"'
                % (", ".join(sorted({x[0] for x in out})), q(out[0][1])))
    return ('no AI/LLM element is bound to a process element on this page; the judgement rests '
            'on the figure and the page text: "%s"'
            % (q(find(r, re.compile(r"(?i)\b(process|bpmn|diagram)\b"), minimum=20) or
                 (lines(r)[0] if lines(r) else ""))))


def ai_quote(r):
    ins = ai_lines(r)
    if ins:
        return q(ins[0][1])
    out = ai_outside(r)
    if out:
        return q(out[0][1])
    l = find(r, re.compile(r"(?i)\b(process|bpmn|diagram|task|automation)\b"), minimum=20)
    return q(l or (lines(r)[0] if lines(r) else r["title"]))


# ---------------------------------------------------------------- entry points

def write_one(n, cls, aiv, vnt, num, force=None):
    made, ruling = record(n, cls, aiv, vnt, num, force)
    if made is None:
        return ruling
    name, text, fig, i = made
    r = next(x for x in F.rows() if x["n"] == n)
    if fig:
        png = os.path.join(CORPUS, name + ".png")
        size = capture(r, i, png)
        if size is None:
            return "capture failed for %d (CDN refused figure %d)" % (n, i)
    xmldir = os.path.join(RAW, "bpmn")
    xmls = sorted(x for x in os.listdir(xmldir) if x.startswith("%04d_" % n)) \
        if os.path.isdir(xmldir) else []
    if xmls:
        import shutil
        shutil.copyfile(os.path.join(xmldir, xmls[0]), os.path.join(CORPUS, name + ".bpmn"))
    with open(os.path.join(CORPUS, name + ".md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return name


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    nums = [int(a) for a in sys.argv[2:] if a.isdigit()]
    cls, aiv, vnt = G.visual()
    if cmd == "manifest":
        m = manifest()
        with open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({str(k): v for k, v in sorted(m.items())}, fh, indent=1)
        print("records.json: %d records" % len(m))
        return
    have = manifest()
    nxt = (max(numbers()) if numbers() else 0) + 1
    for n in nums:
        if cmd == "fix":
            rec = have.get(n)
            if not rec:
                print("%5d has no record to fix" % n)
                continue
            out = write_one(n, cls, aiv, vnt, nxt, force=os.path.basename(rec)[:-3])
            print("%5d fixed -> %s" % (n, out))
            continue
        if n in have:
            print("%5d already has a record: %s" % (n, have[n]))
            continue
        if cmd == "plan":
            made, ruling = record(n, cls, aiv, vnt, nxt)
            if made is None:
                print("%5d %s" % (n, ruling))
                continue
            name, text, fig, i = made
            print("=== %s (figure %d, n=%d, verdict %s)" % (name, i, n, ruling[0]))
            print(text)
        else:
            out = write_one(n, cls, aiv, vnt, nxt)
            print("%5d -> %s" % (n, out))
            nxt += 1


if __name__ == "__main__":
    main()
