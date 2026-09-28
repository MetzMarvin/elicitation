"""camunda-docs-blog: judge the AI-bearing posts (the ones the mechanical screen cannot settle).

Usage
  python ledgers/_cmdb_aijudge.py list [FROM] [TO]   # one block per AI post: evidence found, verdict
  python ledgers/_cmdb_aijudge.py stats

The distinction that matters is whether the page shows an AI/LLM element *inside* a process
(the artefact the thesis is after) or only talks about AI *around* the process - Camunda
Copilot suggesting model elements, AI writing docs, AI on the roadmap, an AI feature of the
platform. The first is INCLUDE, the second is E2-no-ai-element, and anything I cannot settle
from the page is UNCERTAIN.
"""
import re, sys

import _cmdb_figs as F

# an AI/LLM element sitting inside a process, named as a process element
INSIDE = [
    (r"(?i)ai agent task", "AI Agent Task"),
    (r"(?i)ai task agent", "AI Task Agent"),
    (r"(?i)ai agent sub-?process", "AI Agent sub-process"),
    (r"(?i)ai agent connector", "AI Agent connector"),
    (r"(?i)agentic ai connector", "agentic AI connector"),
    (r"(?i)ad-?hoc sub-?process", "ad-hoc sub-process"),
    (r"(?i)openai connector", "OpenAI connector"),
    (r"(?i)hugging ?face connector", "Hugging Face connector"),
    (r"(?i)amazon (comprehend|bedrock|textract)", "Amazon AI service"),
    (r"(?i)google (vertex|gemini|ai)", "Google AI service"),
    (r"(?i)anthropic|claude", "Anthropic/Claude"),
    (r"(?i)(ai|llm|gpt|openai|agent)[^.]{0,30}(service task|user task|business rule task|"
     r"script task|send task|task connector|connector element)", "AI-bound task"),
    (r"(?i)(service task|task|connector)[^.]{0,40}(openai|gpt|llm|ai model|ai agent|ai service)",
     "AI-bound task"),
    (r"(?i)ai[- ]powered (task|step|activity|decision)", "AI-powered task"),
    (r"(?i)intelligent document analysis", "intelligent document analysis"),
    (r"(?i)(invoke|call|ask|query)[^.]{0,30}(llm|gpt|openai|ai model|ai agent)", "call to an LLM"),
    (r"(?i)mcp (client )?connector|a2a (client )?connector", "MCP/A2A connector"),
    (r"(?i)ai (gateway|decision|routing|classif\w+)", "AI gateway/decision"),
]
# AI talk that is about the platform/tooling rather than an element inside the process
OUTSIDE = [
    (r"(?i)copilot", "Camunda Copilot"),
    (r"(?i)modeler suggestions|suggestions? (for|to) (refin|improv|build)", "Modeler suggestions"),
    (r"(?i)docs ai|documentation ai|ai (assistant|chatbot) for (our )?docs", "AI for documentation"),
    (r"(?i)ai skills?\b", "AI Skills (coding assistance)"),
    (r"(?i)vibe cod", "vibe coding"),
    (r"(?i)ai[- ]generated (forms?|text|documentation)", "AI-generated content"),
    (r"(?i)ai-powered suggestions", "Modeler suggestions"),
    (r"(?i)roadmap|coming soon|we (will|plan to) (launch|release)", "roadmap"),
]


def lines(r):
    for line in r["text"].split("\n"):
        l = " ".join(line.split())
        if len(l) >= 30:
            yield l


def find(r, pats):
    out = []
    for line in lines(r):
        for pat, name in pats:
            if re.search(pat, line):
                out.append((name, line))
                break
    return out


def verdict(r):
    """(verdict, reason, judgment, evidence, why) for an AI-bearing post."""
    ins = find(r, INSIDE)
    outs = find(r, OUTSIDE)
    figs = F.figs(r)
    if r["files"]:
        return ("MODEL", "", True, "", "downloadable model: judged from the XML")
    if not figs:
        ev = (ins[0][1] if ins else (outs[0][1] if outs else "")) or \
             next(l for l in lines(r))
        return ("EXCLUDE", "E0-no-artefact", False, " ".join(ev.split()[:25]),
                "the page shows no figure and links no .bpmn/.dmn/.cmmn: no process artefact "
                "at all, whatever AI it discusses in prose")
    if ins:
        name, line = ins[0]
        return ("UNCERTAIN", "", True, " ".join(line.split()[:25]),
                "the page names %r - an AI element bound to a process element" % name)
    if outs:
        name, line = outs[0]
        return ("EXCLUDE", "E2-no-ai-element", True, " ".join(line.split()[:25]),
                "the only AI the page points at is %r, which is tooling around the diagrams, "
                "not an element inside the process" % name)
    return ("UNCERTAIN", "", True, " ".join(next(lines(r)).split()[:25]),
            "the page carries AI/LLM terms but names no AI element bound to a process element")


def main():
    lo = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 0
    hi = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 1436
    import collections
    c = collections.Counter()
    for r in F.rows():
        n = r["n"]
        if n > 1435 or n < lo or n > hi or not r["n_ai"]:
            continue
        v = verdict(r)
        c[v[0]] += 1
        if sys.argv[1] == "list":
            print("== %d %s :: %s" % (n, r["title"][:66], r["url"]))
            print("   figs=%d BPMNtxt=%s BPMNalt=%s" % (
                len(F.figs(r)), "BPMN" in r["text"] or "bpmn" in r["text"],
                any("bpmn" in f["alt"].lower() for f in F.figs(r))))
            print("   %s | %s | %s" % (v[0], v[1] or "-", v[4]))
            print("   EV: %s" % v[3])
    print(c) if sys.argv[1] != "list" else None


if __name__ == "__main__":
    main()
