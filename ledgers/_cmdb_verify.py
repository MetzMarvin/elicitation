"""camunda-docs-blog: verify the corpus records against the pages they claim to quote.

  python ledgers/_cmdb_verify.py            # every record in corpus/camunda-docs-blog/
  python ledgers/_cmdb_verify.py NNN ...    # only those records

For each record it checks, mechanically:
  * the frontmatter carries the required keys, with a verdict from the closed set;
  * `needs_human_ruling` is true exactly for UNCERTAIN, and then `question` is set;
  * the numbered screenshot named in `artefacts` exists on disk;
  * `n` is a line of the frontier, and the record filename number is unique;
  * every quote field is verbatim on the page the record points at - the saved screen of
    that post (its DOM text), its figure alt texts, or the model XML it links.

A quote that fails is printed with the closest page line that resembles it, because the usual
cause is a paraphrase written into a quote field, which the evidence rule forbids.
"""
import difflib, glob, json, os, re, sys, unicodedata

RAW = "ledgers/camunda-docs-blog.raw"
CORPUS = "corpus/camunda-docs-blog"
BPMNDIR = os.path.join(RAW, "bpmn")
REQ = ["n", "source", "source_name", "source_type", "title", "url", "accessed", "verdict",
       "needs_human_ruling", "question", "needs_visual_check", "bpmn_evidence",
       "bpmn_evidence_quote", "ai_evidence", "ai_evidence_quote", "artefacts",
       "duplicate_of", "access", "capture_source", "capture_quality", "capture_width_px",
       "capture_method"]
QUOTE_KEYS = ["bpmn_evidence_quote", "ai_evidence_quote"]
VERDICTS = {"INCLUDE", "UNCERTAIN", "EXCLUDE", "BLOCKED"}
BAD = re.compile(r"E[0-9]+-(?!)")


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("—", "-"), ("–", "-"), (" ", " ")):
        s = s.replace(a, b)
    return " ".join(s.split()).lower()


def frontmatter(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    if not m:
        return None, txt
    fm, out, key = m.group(1), {}, None
    for line in fm.split("\n"):
        if re.match(r"^\s+\S", line) and key:          # nested (artefacts:)
            k2 = line.strip().split(":", 1)
            if len(k2) == 2:
                out.setdefault(key, {})
                if isinstance(out[key], dict):
                    out[key][k2[0].strip()] = k2[1].strip().strip('"\'')
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        key, v = k.strip(), v.strip()
        if v.startswith('"') and v.endswith('"') and len(v) > 1:
            # the generator writes quote fields as YAML double-quoted scalars and escapes the
            # page's own double quotes; undo that so the verbatim check sees the page's words
            v = v[1:-1].replace('\\"', '"').replace('\\\\', '\\')
        else:
            v = v.strip('"\'')
        out[key] = v if v not in ("null", "") else (None if v == "null" else "")
        if key == "artefacts":
            out[key] = {}
    return out, txt


def pages():
    rows = {}
    for line in open(os.path.join(RAW, "screen.jsonl"), encoding="utf-8"):
        r = json.loads(line)
        rows[r["n"]] = r
    return rows


def haystack(r):
    alts = " ".join((i.get("alt") or "") for i in (r.get("imgs") or []))
    parts = [r.get("text") or "", alts, " ".join(r.get("caps") or [])]
    for p in sorted(glob.glob(os.path.join(BPMNDIR, "%04d_*" % r["n"]))):
        parts.append(open(p, encoding="utf-8", errors="replace").read())
    return norm("\n".join(parts))


def closest(hay, q):
    lines = [l for l in hay.split("\n") if len(l) > 20]
    m = difflib.get_close_matches(norm(q), lines, n=1, cutoff=0.5)
    return m[0][:160] if m else ""


def main():
    want = [a for a in sys.argv[1:] if a.isdigit()]
    rows = pages()
    frontier = {}
    for line in open("ledgers/camunda-docs-blog.frontier.txt", encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2:
            frontier[int(p[0])] = p[1]
    problems, seen_num = [], {}
    for path in sorted(glob.glob(os.path.join(CORPUS, "*.md"))):
        num = os.path.basename(path)[:3]
        if want and num not in want:
            continue
        fm, txt = frontmatter(path)
        tag = os.path.basename(path)
        if not fm:
            problems.append("%s: no YAML frontmatter" % tag)
            continue
        for k in REQ:
            if k not in fm:
                problems.append("%s: frontmatter key %r missing" % (tag, k))
        if num in seen_num:
            problems.append("%s: number %s already used by %s" % (tag, num, seen_num[num]))
        seen_num[num] = tag
        v = (fm.get("verdict") or "").upper()
        if v not in VERDICTS:
            problems.append("%s: verdict %r not in the closed set" % (tag, fm.get("verdict")))
        nhr = str(fm.get("needs_human_ruling")).lower() == "true"
        if nhr != (v == "UNCERTAIN"):
            problems.append("%s: needs_human_ruling=%s with verdict %s" % (tag, nhr, v))
        if nhr and not fm.get("question"):
            problems.append("%s: needs_human_ruling without a question" % tag)
        if v == "UNCERTAIN" and not str(fm.get("needs_visual_check")).lower() == "true":
            problems.append("%s: UNCERTAIN without needs_visual_check" % tag)
        art = fm.get("artefacts") or {}
        shot = art.get("screenshot") if isinstance(art, dict) else None
        if shot and not os.path.exists(os.path.join(CORPUS, shot)):
            problems.append("%s: artefacts.screenshot %r not on disk" % (tag, shot))
        n = fm.get("n")
        try:
            n = int(n)
        except (TypeError, ValueError):
            problems.append("%s: n=%r is not a number" % (tag, fm.get("n")))
            continue
        if n not in frontier:
            problems.append("%s: n=%d is not a frontier item" % (tag, n))
            continue
        if frontier[n] != fm.get("url"):
            problems.append("%s: url does not match frontier line %d" % (tag, n))
        r = rows.get(n)
        if not r:
            problems.append("%s: no saved page for n=%d" % (tag, n))
            continue
        hay = haystack(r)
        for k in QUOTE_KEYS:
            q = fm.get(k)
            if not q:
                problems.append("%s: %s empty" % (tag, k))
                continue
            if len(q.split()) > 25:
                problems.append("%s: %s is %d words (the rule caps a quote at 25)"
                                % (tag, k, len(q.split())))
            if norm(q) not in hay:
                problems.append("%s: %s not verbatim on the page\n      quote: %s\n"
                                "      closest page line: %s"
                                % (tag, k, q[:120], closest(hay, q)))
    print("%d records checked, %d problems" % (len(seen_num), len(problems)))
    for p in problems:
        print(" -", p)


if __name__ == "__main__":
    main()
