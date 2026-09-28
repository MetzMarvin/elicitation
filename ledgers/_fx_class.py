"""Dry-run classifier for the flowx-ai census: bucket every population page before any row is written.

Reads flowx-ai.raw/{population.json,screen.json,figmeta.json} and prints, per page, the mechanical
facts the ledger rows will rest on: how many figures, which of them name a BPMN artefact in the
figure's own filename or alt text, how many diagram fences (mermaid) and downloadable model files the
page publishes, and whether the page's own prose carries a real AI term (after removing the
`FlowX.AI` / `docs.flowx.ai` false positives that made every page look AI-bearing).

Nothing here decides a verdict; it exists so the classifier can be inspected and hand-corrected
before 945 rows are emitted.
"""
import json, os, re, sys

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
PAGES = os.path.join(RAW, "pages")
FALLBACK = os.path.join(RAW, "pages_llmsfull")

# A real AI/LLM term as this vendor uses them. `FlowX.AI` is stripped first: it made every one of the
# 934 pages look AI-bearing, which is a false positive of exactly the kind the processmaker census
# had to correct (the word "model" in "Process model").
AILEX = re.compile(r"\b(llm|llms|gpt|openai|anthropic|claude|gemini|langchain|langflow|mcp|"
                   r"agent|agents|agentic|prompt|prompts|embedding|embeddings|vector|rag|retrieval|"
                   r"machine learning|copilot|chatbot|chat interface|natural language|"
                   r"artificial intelligence|ai model|ai models|ai node|ai nodes|ai platform|"
                   r"ai agent|ai agents|ai assistant|ai analyst|ai architect|ai designer|"
                   r"ai developer|ai-powered|ai powered|ai gateway|ai action|ai actions|"
                   r"ai core|ai-core|gen ai|generative ai|generative|intelligent|intelligence|"
                   r"semantic|classifier|classification|speech.to.text|ocr|summari[sz]|"
                   r"recommendation|knowledge base|vision model|document understanding|"
                   r"text understanding|text generation|document extraction|ai operations|"
                   r"ai trigger|ai triggers|agent builder|guardrail)", re.I)
# `model` alone is deliberately absent: FlowX says "data model", "process model" and "Project Data
# Model" on hundreds of pages, none of them LLM models.

# A figure whose own filename or alt text names a BPMN artefact. Deliberately narrow: `workflow` and
# `designer` alone are NOT here, because FlowX's Integration Designer and Agent Builder canvases are
# workflows, not BPMN, and a rule matching them would file those canvases as BPMN artefacts.
BPMNFIG = re.compile(r"(process_designer|prs_def|process_desig|process\.png|dsgnr|bpmn|gateway|lane|"
                     r"swimlane|pool|subprocess|call_activity|boundary|message_catch|message_throw|"
                     r"message_send|message_intermediate|intermediate_event|start_end|task_node|"
                     r"user_task|exclusive|parallel|xor_|embed_node|process_instance|active_process|"
                     r"proc_def|process_definition|start_event|end_event|timer_event|error_event)", re.I)
BPMNALT = re.compile(r"(process designer|bpmn|process flow|process map|process definition|"
                     r"process model|swimlane|gateway|pool|lane|user task|service task)", re.I)
# A mermaid/ASCII diagram fence that names BPMN elements in its own source text.
DIAGFENCE = re.compile(r"```(mermaid|text|plaintext)?[^\n]*\n(.*?)```", re.S)
BPMNWORD = re.compile(r"\b(bpmn|user task|service task|send message task|receive message task|"
                      r"business rule|exclusive gateway|parallel gateway|end event|start event|"
                      r"boundary event|intermediate event|sub-?process|pool|lane|swimlane|"
                      r"sequence flow)\b", re.I)


def strip_body(t):
    t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
    return re.sub(r"^>\s*## Documentation Index.*?(?=\n#|\Z)", " ", t, flags=re.S | re.M)


def page_text(url):
    slug = re.sub(r"^https://docs\.flowx\.ai", "", url).strip("/").replace("/", "__") or "root"
    for d in (PAGES, FALLBACK):
        p = os.path.join(d, slug + ".md")
        if os.path.exists(p):
            return strip_body(open(p, encoding="utf-8", errors="replace").read()
                              .replace("\r\n", "\n")), slug
    return None, slug


def classify(url, fm, sc):
    body, _ = page_text(url)
    if body is None:
        return None
    clean = re.sub(r"(?i)flowx\.?ai|docs\.flowx\.ai", "FlowX", body)
    figs = fm.get(url) or []
    bpmn_figs = [f for f in figs if BPMNFIG.search(f["name"]) or BPMNALT.search(f["alt"])]
    fences = DIAGFENCE.findall(body)
    bpmn_fences = [f for f in fences if BPMNWORD.search(f[1]) and ("-->" in f[1] or "-->" in f[1]
                                                                  or "->" in f[1] or "──" in f[1])]
    ascii_sketch = [f for f in fences if "→" in f[1] or "->" in f[1]]
    models = len(re.findall(r"\.bpmn\b", body))
    ai = bool(AILEX.search(clean))
    return {
        "url": url, "n_fig": len(figs), "n_bpmn_fig": len(bpmn_figs),
        "n_fence": len(fences), "n_bpmn_fence": len(bpmn_fences),
        "n_ascii": len(ascii_sketch), "n_model": models, "ai": ai,
        "bpmn_figs": [f["name"][:48] for f in bpmn_figs][:4],
    }


def main():
    pop = json.load(open(os.path.join(RAW, "population.json")))
    fm = json.load(open(os.path.join(RAW, "figmeta.json")))
    sc = {x["url"]: x for x in json.load(open(os.path.join(RAW, "screen.json")))}
    out = [classify(u, fm, sc) for u in pop]
    missing = [u for u, c in zip(pop, out) if c is None]
    print("population", len(pop), "classified", len(out) - len(missing), "missing", len(missing))
    if missing:
        print("MISSING:", missing[:6])
    json.dump(out, open(os.path.join(RAW, "classify.json"), "w", encoding="utf-8"), indent=0)
    buckets = {}
    for c in out:
        if not c:
            continue
        has_art = c["n_fig"] or c["n_fence"] or c["n_model"]
        if not has_art:
            k = "E0-no-artefact"
        elif c["n_bpmn_fig"] or c["n_bpmn_fence"]:
            k = "E2-candidate (BPMN artefact on page)"
        else:
            k = "E1-candidate (artefact, no BPMN)"
        k += " + AI" if c["ai"] else ""
        buckets[k] = buckets.get(k, 0) + 1
    for k, v in sorted(buckets.items()):
        print("%5d  %s" % (v, k))
    print()
    print("--- E2-candidate rows where the page also discusses AI (the false-negative zone) ---")
    for c in out:
        if c and (c["n_bpmn_fig"] or c["n_bpmn_fence"]) and c["ai"]:
            print("  %-88s figs=%d bpmn_figs=%s fences=%d" % (
                c["url"].replace("https://docs.flowx.ai", ""), c["n_fig"], c["bpmn_figs"], c["n_bpmn_fence"]))


if __name__ == "__main__":
    main()
