"""trisotech: build batch5.json -- the 32 video-family pages.

Verdict rule for this family (recorded in the ledger header):
  - the page publishes no model; the artefact would be inside the recording, which was not watched;
  - so every AI-signal video page is UNCERTAIN with needs_visual_check, except
      * 9 pages whose own text never names a modelling notation AND which have no paired slide deck
        -> E0-no-artefact (recorded in one family line in the header so they can be reopened together);
      * 1 page whose published poster frame is a tool screenshot -> E1-not-bpmn.
Evidence is extracted verbatim from the page's own text so nothing is paraphrased.

  python ledgers/_ts_batch5.py > ledgers/trisotech.raw/batch5.preview.txt
  python ledgers/_ts_batch5.py --write
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
C = json.load(open(os.path.join(RAW, "content.json"), encoding="utf-8"))

NOTATION = re.compile(r"(?<![A-Za-z])(BPMN|CMMN|DMN|BPM\+|DRD|BPMN\+)(?![A-Za-z])|Business Process Model and Notation|Decision Model and Notation|Case Management Model and Notation")
AIW = re.compile(r"(?i)\b(AI|artificial intelligence|LLM|GPT|ChatGPT|OpenAI|machine learning|neural|agentic|generative|GenAI|RAG|predictive|AI agent)")
NAV = re.compile(r"(?i)^(edit profile|cookie|logout|toggle navigation|request pricing|search|accept|subscribe|sign up|privacy|contact|about us|careers)")

# slug -> (verdict, record number or None, deck slug or "", note)
V = {
 "5-min-intro-to-bpmn": ("U", 4, "5-min-intro-to-bpmn-presentation", "The recording of this source's own short BPMN introduction."),
 "bpmn-user-tasks-for-humans-and-ai-agents": ("U", 5, "bpmn-user-tasks-for-humans-and-ai-agents-presentation", "Strongest video candidate in the source: AI agents as BPMN user-task performers."),
 "contracts-and-the-knowledge-worker-copilot": ("U", 6, "contracts-and-the-knowledge-worker-copilot-presentation", "RAG-based copilot inside contract workflows."),
 "decision-framework-for-machine-learning-webinar": ("U", 7, "", "No paired deck; abstract describes a BPMN+DMN framework wrapping machine-learning models."),
 "how-bpm-health-complements-fhir": ("U", 8, "how-bpm-health-complements-fhir-presentation", "The clearest notation talk in the family; names BPMN, DMN and CMMN."),
 "ai-agents-in-healthcare": ("U", 9, "ai-agents-in-healthcare-presentation", "Governed AI agents in clinical automation."),
 "ai-driven-healthcare-orchestration": ("U", 10, "ai-driven-healthcare-orchestration-presentation", "AI inside BPM+ Health clinical workflows."),
 "ai-fhir-and-bpm-in-suicide-prevention": ("U", 11, "ai-fhir-and-bpm-in-suicide-prevention-presentation", "Recording of the talk whose written version is corpus record 001."),
 "automation-of-loan-origination": ("U", 12, "automation-of-loan-origination-presentation", "Loan origination automated from visual process and decision models."),
 "clinician-centric-data-and-ai-integration-in-healthcare": ("U", 13, "clinician-centric-data-and-ai-integration-in-healthcare-presentation", "AI orchestrated into clinical decision-making."),
 "enterprise-ai-in-2026": ("U", 14, "enterprise-ai-in-2026-presentation", "Enterprise AI in production under governance."),
 "generative-ai-and-regulatory-compliance": ("U", 15, "generative-ai-and-regulatory-compliance-presentation", "GenAI extracting terms and generating rules/concept models."),
 "harness-genai-and-agentic-ai": ("U", 16, "harness-genai-and-agentic-ai-presentation", "Argues BPM+ models are the harness for GenAI and agentic AI."),
 "hl7-ai-challenge-winners": ("U", 17, "hl7-ai-challenge-winners-presentation", "BPM+ models driving governable AI agents."),
 "it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision": ("U", 18, "it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision-presentation", "Human and AI decision-makers combined."),
 "knowledge-worker-copilot-in-the-loop": ("U", 19, "knowledge-worker-copilot-in-the-loop-presentation", "Copilot orchestrating BPM+ workflows and AI reasoning."),
 "low-code-neuro-symbolic-agents": ("U", 20, "low-code-neuro-symbolic-agents-presentation", "Neuro-symbolic AI driven by process and decision orchestration."),
 "mastering-decision-orchestration": ("U", 21, "mastering-decision-orchestration-presentation", "AI types supporting decision automation."),
 "optimizing-preoperative-assessments": ("U", 22, "optimizing-preoperative-assessments-presentation", "BPM+ visual models feeding predictive analytics."),
 "the-role-of-genai": ("U", 23, "the-role-of-genai-presentation", "LLMs turning unstructured text into business actions."),
 "who-made-that-decision-governing-decisions-in-the-age-of-ai-agents": ("U", 24, "who-made-that-decision-governing-decisions-in-the-age-of-ai-agents-presentation", "AI participation classified by role inside BPM+ orchestration; its paired deck is the substantive artefact."),
 "ai-and-bpm": ("U", 25, "", "No paired deck; a vlog about where AI and BPM meet."),
 "ai-and-automation-friends-or-foes": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "best-practices-in-business-automation-application-implementation": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "beyond-automation-orchestrating-the-insurance-lifecycle-from-underwriting-to-claims": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "business-automation-best-practices-1-introduction": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "business-automation-best-practices-3-application-development-design-part-2": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "composability-leveraging-best-of-breed": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "future-proofing-your-business-with-bpm": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "process-latency-not-always-a-bad-thing": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording family is ruled in scope."),
 "saugatalks-digital-transformation-automation": ("E0", None, "", "The page's own text names no modelling notation and there is no paired slide deck; the recording was not watched. Reopen with the other E0 video rows if the recording is ruled in scope."),
}

E1_SLUG = "bpmnext-2015-trisotech-bpm-graph-semantic-layer-for-businessit-divide"
BPMN_REC = {
 4: "004_5-min-intro-to-bpmn", 5: "005_bpmn-user-tasks-for-humans-and-ai-agents",
 6: "006_contracts-and-the-knowledge-worker-copilot", 7: "007_decision-framework-for-machine-learning-webinar",
 8: "008_how-bpm-health-complements-fhir", 9: "009_ai-agents-in-healthcare",
 10: "010_ai-driven-healthcare-orchestration", 11: "011_ai-fhir-and-bpm-in-suicide-prevention",
 12: "012_automation-of-loan-origination", 13: "013_clinician-centric-data-and-ai-integration-in-healthcare",
 14: "014_enterprise-ai-in-2026", 15: "015_generative-ai-and-regulatory-compliance",
 16: "016_harness-genai-and-agentic-ai", 17: "017_hl7-ai-challenge-winners",
 18: "018_it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision",
 19: "019_knowledge-worker-copilot-in-the-loop", 20: "020_low-code-neuro-symbolic-agents",
 21: "021_mastering-decision-orchestration", 22: "022_optimizing-preoperative-assessments",
 23: "023_the-role-of-genai",
 24: "024_who-made-that-decision-governing-decisions-in-the-age-of-ai-agents", 25: "025_ai-and-bpm",
}


CHROME = re.compile(r"^(Home|Resources|Webinars|Blog|Our|Presented|Play|Description|By |Search|Videos|Podcasts|Events|Contact|About|Solutions|Capabilities|Use Cases)\b")
CHROME2 = re.compile(r"Webinars Home|Presented By|Video Time|Read Time|Toggle navigation|Request Pricing")


def sents(slug):
    t = (C.get(slug) or {}).get("text") or ""
    out = []
    for s in re.split(r"(?<=[.!?])\s+", t):
        s = " ".join(s.split())
        if 25 <= len(s) <= 400 and not NAV.match(s) and not CHROME.match(s) and not CHROME2.search(s):
            out.append(s)
    return out


def cut(s, n=25):
    w = s.split()
    return " ".join(w[:n]) + ("…" if len(w) > n else "")


def pick(slug, prefer_notation=False):
    ss = sents(slug)
    if not ss:
        return ""

    def score(s):
        return 3 * len(NOTATION.findall(s)) + len(AIW.findall(s)) + (1 if NOTATION.search(s) and AIW.search(s) else 0)
    pool = [s for s in ss if (NOTATION.search(s) and AIW.search(s))] if prefer_notation else []
    for p in ([s for s in ss if AIW.search(s)], [s for s in ss if NOTATION.search(s)], ss):
        if not pool:
            pool = p
    best = max(pool, key=score)
    return cut(best)


rows = []
for slug, (verdict, num, deck, note) in sorted(V.items(), key=lambda kv: (kv[1][1] or 99, kv[0])):
    ev = pick(slug, prefer_notation=(verdict == "U"))
    row = {"key": slug, "judged_from": "opened https://www.trisotech.com/%s/ (saved page text) on 2026-09-25; "
           "viewed the page's only content image, the video poster frame, at full size" % slug}
    if verdict == "U":
        rec = BPMN_REC[num]
        row.update(verdict="UNCERTAIN", code="", judgment=True, evidence=ev, note=note,
                   record="corpus/trisotech/%s.md" % rec,
                   capture="corpus/trisotech/%s-poster-frame.png" % rec,
                   needs_visual_check=True, needs_human_ruling=False)
    else:
        row.update(verdict="EXCLUDE", code="E0-no-artefact", judgment=False, evidence=ev, note=note,
                   record=None, capture=None, needs_visual_check=False, needs_human_ruling=False)
    rows.append(row)

# the one published frame that shows a tool, not a model
ss = sents(E1_SLUG)
ev = cut(next((s for s in ss if "BPM Graph" in s or "semantic" in s), ss[0] if ss else ""))
rows.append({
 "key": E1_SLUG, "verdict": "EXCLUDE", "code": "E1-not-bpmn", "judgment": False, "evidence": ev,
 "note": "Not BPMN: the published poster frame is a screenshot of the Trisotech modeller's rule/decision-table "
         "editor (a table pane headed 'Policy1' with rule rows beside a business-item navigation tree), i.e. "
         "the authoring tool's UI, not a BPMN diagram. No diagram of any notation is published on the page.",
 "judged_from": "opened https://www.trisotech.com/%s/ (saved page text) on 2026-09-25; viewed the poster frame at full size" % E1_SLUG,
 "record": None, "capture": None, "needs_visual_check": False, "needs_human_ruling": False,
})

print("# batch5: %d rows (%d U / %d E0 / 1 E1)" % (len(rows),
      sum(1 for r in rows if r["verdict"] == "UNCERTAIN"),
      sum(1 for r in rows if r.get("code") == "E0-no-artefact")))
bad = 0
for r in rows:
    t = (C.get(r["key"]) or {}).get("text") or ""
    e = r["evidence"].rstrip("…")
    ok = e in t or e in " ".join(t.split())
    if not ok:
        bad += 1
    print("\n%-58s %-9s %-14s j=%-5s verbatim=%s  rec=%s" % (r["key"][:58], r["verdict"], r["code"] or "-",
          r["judgment"], "y" if ok else "NO", (r["record"] or "-").split("/")[-1]))
    print("   ev: %s" % r["evidence"])
print("\nnon-verbatim: %d" % bad)

if "--write" in sys.argv:
    json.dump({"source": "trisotech", "batch": 5, "family": "video", "dispositions": rows},
              open(os.path.join(RAW, "batch5.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote trisotech.raw/batch5.json")
