"""camunda-docs-blog: print the artefact-relevant context of a post (for judging, not evidence).

  python ledgers/_cmdb_look.py <n> [<n> ...] [-w]
     -w  also print lines that carry an AI term without a BPMN term
"""
import re, sys

import _cmdb_figs as F

PAT = re.compile(r"(?i)\b(bpmn|process model|process diagram|diagram|ad-?hoc sub-?process|"
                 r"sub-?process|gateway|service task|user task|pool|lane|modeler|workflow|"
                 r"orchestrat\w*|figure|screenshot)\b")
AI = re.compile(r"(?i)\b(ai|artificial intelligence|llm|agent|agentic|copilot|gpt|model|"
                r"prompt|connector|anthropic|claude|openai)\b")


def main(ns, wide):
    for r in F.rows():
        if r["n"] not in ns:
            continue
        print("=" * 20, r["n"], r["url"])
        print("TITLE:", r["title"])
        print("ai_terms:", r["n_ai"], "| files:", r["files"], "| yt:", r["yt"])
        for k, f in enumerate(F.figs(r), 1):
            print("  FIG %d %4dx%-4d %s" % (k, f["w"], f["h"], f["alt"][:90]))
            print("        ", f["src"])
        if OUT:
            p = "ledgers/camunda-docs-blog.raw/blog/%04d.html" % r["n"]
            h = open(p, encoding="utf-8", errors="replace").read()
            m = re.search(r"(?is)<main[^>]*>(.*?)</main>", h)
            body = m.group(1) if m else h
            seen = []
            for a in re.finditer(r'(?is)<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', body):
                href, txt = a.group(1), re.sub(r"<[^>]+>", " ", a.group(2))
                txt = re.sub(r"\s+", " ", txt).strip()
                if href.startswith("#") or "camunda.com" in href:
                    continue
                if (href, txt) in seen:
                    continue
                seen.append((href, txt))
            print("  OUTBOUND LINKS:")
            for href, txt in seen:
                print("    %-100s | %s" % (href[:100], txt[:50]))
        for line in r["text"].split("\n"):
            line = line.strip()
            if len(line) < 30:
                continue
            if PAT.search(line) and (AI.search(line) or wide):
                print("   |", line[:400])


if __name__ == "__main__":
    args = sys.argv[1:]
    wide = "-w" in args
    OUT = "-o" in args
    ns = set(int(a) for a in args if a.isdigit())
    main(ns, wide)
