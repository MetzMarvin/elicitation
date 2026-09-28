"""camunda-docs-blog: build the per-post evidence briefs from which the corpus records are written.

  python ledgers/_cmdb_brief.py N [N ...]        # briefs for those posts, to stdout
  python ledgers/_cmdb_brief.py --fromfile F     # briefs for the posts listed in F (one n per line)
  python ledgers/_cmdb_brief.py --include FILE   # write all briefs to one file, separated by ===

A brief holds only material taken from the page the crawler saved (its DOM text, its figure
alt texts, its links) plus the visual pass's verdict on that post's cells. Whoever writes the
record must quote from the brief, never invent: every quote in the record is checked back
against the saved page.
"""
import json, os, re, sys

import _cmdb_aijudge as A
import _cmdb_figs as F
import _cmdb_shots as S

RAW = "ledgers/camunda-docs-blog.raw"
VIZ = os.path.join(RAW, "viz")

KEEP = re.compile(r"(?i)\b(bpmn|ad-?hoc sub-?process|sub-?process|gateway|service task|user task|"
                  r"process model|process diagram|ai agent|ai task|agentic|llm|openai|gpt|claude|"
                  r"anthropic|bedrock|connector|tool|prompt|model|orchestrat\w*|autonom\w*|"
                  r"guardrail|human in the loop|human-in-the-loop|approv\w*|decision)\b")


def viznotes():
    out = {}
    import glob
    for p in sorted(glob.glob(os.path.join(VIZ, "report_*.txt"))):
        for line in open(p, encoding="utf-8", errors="replace"):
            m = re.match(r"\s*(\d+)\.(\d+)\s*\|\s*([a-z][a-z-]*)\s*\|\s*(yes|no|unclear)\s*\|(.*)",
                         line)
            if m:
                out["%s.%s" % (m.group(1), m.group(2))] = (m.group(3), m.group(4), m.group(5).strip())
    return out


def brief(r, vz):
    L = []
    L.append("=== POST %d ===" % r["n"])
    L.append("url: %s" % r["url"])
    L.append("title: %s" % r["title"])
    L.append("page text: %d characters; AI/LLM term hits: %s" % (len(r["text"]), r["n_ai"]))
    L.append("model links (.bpmn/.dmn/.cmmn) found on the page: %s" % (r["files"] or "none"))
    L.append("")
    L.append("--- FIGURES (in the order the record may capture them: figure 1 is the one the")
    L.append("    visual pass judged, and the one to capture unless it is unreadable) ---")
    for k, f in enumerate(S.selected(r), 1):
        v = vz.get("%d.%d" % (r["n"], k), ("-", "-", ""))
        L.append("  figure %d: %dx%d  alt=%r" % (k, f["w"], f["h"], f["alt"]))
        L.append("      src=%s" % f["src"])
        L.append("      visual pass: class=%s ai_visible=%s note=%s" % v)
    rest = [f for f in F.figs(r) if f["alt"] and f not in S.selected(r)]
    if rest:
        L.append("  other figures on the page (alt texts only):")
        for f in rest[:8]:
            L.append("      %dx%d %r" % (f["w"], f["h"], f["alt"]))
    L.append("")
    L.append("--- THE LINES THE AI JUDGEMENT RESTED ON (verbatim from the saved page) ---")
    ins = A.find(r, A.INSIDE)
    outs = A.find(r, A.OUTSIDE)
    for name, line in ins[:4]:
        L.append("  [AI-IN-PROCESS %s] %s" % (name, line[:300]))
    for name, line in outs[:3]:
        L.append("  [AI-AROUND-PROCESS %s] %s" % (name, line[:300]))
    L.append("")
    L.append("--- FURTHER PAGE TEXT THAT NAMES THE PROCESS ELEMENTS ---")
    seen = 0
    for line in r["text"].split("\n"):
        line = " ".join(line.split())
        if len(line) < 45 or not KEEP.search(line):
            continue
        if any(line[:60] == x[1][:60] for x in ins + outs):
            continue
        L.append("  " + line[:300])
        seen += 1
        if seen >= 18:
            break
    return "\n".join(L)


def main():
    vz = viznotes()
    nums = []
    if "--fromfile" in sys.argv:
        nums = [int(x.strip()) for x in open(sys.argv[sys.argv.index("--fromfile") + 1],
                                            encoding="utf-8") if x.strip()]
    else:
        nums = [int(a) for a in sys.argv[1:] if a.isdigit()]
    rows = {r["n"]: r for r in F.rows()}
    out = []
    for n in nums:
        if n in rows:
            out.append(brief(rows[n], vz))
    print("\n\n".join(out))


if __name__ == "__main__":
    main()
