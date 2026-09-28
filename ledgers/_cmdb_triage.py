"""camunda-docs-blog: one compact line per post that carries an AI/LLM term, for judgement.

  python ledgers/_cmdb_triage.py [FROM] [TO]      # posts with an AI term (or a model link)
  python ledgers/_cmdb_triage.py -d [FROM] [TO]   # only posts whose figure alt names a diagram

Line: n | figs | flags | title :: selected figure alts :: best AI-and-structure line
"""
import re, sys

import _cmdb_figs as F

STRUCT = re.compile(r"(?i)\b(bpmn|diagram|process model|ad-?hoc sub-?process|sub-?process|"
                    r"gateway|service task|user task|business rule task|script task|pool|lane|"
                    r"modeler|process instance|sequence flow|task|connector)\b")
AIX = re.compile(r"(?i)\b(ai|artificial intelligence|llm|large language model|agent|agentic|"
                 r"copilot|gpt|openai|anthropic|claude|gemini|generative|genai|machine learning|"
                 r"prompt|embedding|rag|intelligent|neural|mcp)\b")


def best_line(r):
    out = ""
    for line in r["text"].split("\n"):
        l = " ".join(line.split())
        if len(l) < 45:
            continue
        if STRUCT.search(l) and AIX.search(l):
            if not out or len(set(STRUCT.findall(l.lower()))) > len(set(STRUCT.findall(out.lower()))):
                out = l
    if not out:
        for line in r["text"].split("\n"):
            l = " ".join(line.split())
            if len(l) >= 45 and AIX.search(l):
                return l[:220]
    return out[:260]


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("-")]
    lo = int(a[0]) if a else 0
    hi = int(a[1]) if len(a) > 1 else 1436
    diagrams = "-d" in sys.argv
    for r in F.rows():
        n = r["n"]
        if n > 1435 or n < lo or n > hi:
            continue
        if not (r["n_ai"] or r["files"]):
            continue
        fs = F.figs(r)
        if diagrams and not any(F.DIAG.search(f["alt"]) for f in fs):
            continue
        sel = sorted(fs, key=lambda f: (0 if F.DIAG.search(f["alt"]) else 1, -f["w"] * f["h"]))
        alts = " | ".join(f["alt"][:38] for f in sel[:2])
        flags = ("BPMNtxt " if ("BPMN" in r["text"] or "bpmn" in r["text"]) else "") + \
                ("BPMNalt " if any("bpmn" in f["alt"].lower() for f in fs) else "") + \
                ("FILE " if r["files"] else "")
        print("%5d f=%-3d ai=%-4d %s%s\n      :: %s\n      :: %s" % (
            n, len(fs), r["n_ai"], flags, r["title"][:70], (alts or "(no alt)")[:120], best_line(r)))


if __name__ == "__main__":
    main()
