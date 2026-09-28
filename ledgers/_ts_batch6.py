"""trisotech: batch6 -- the figure pass (every figure-bucket page carrying an AI/LLM signal).

Every row here is grounded in a page whose own images were viewed at published size on 2026-09-25
(contact sheets + full-size views). Convention used, recorded in the ledger header:

  E0-no-artefact   the page publishes only icons, logos, photographs, badges or decorative header
                   art - nothing depicting a process, a decision or a data flow.
  E1-not-bpmn      the page publishes a drawn figure (DMN DRD / decision table / boxed expression,
                   KNIME workflow, plain activity flowchart, architecture box diagram, infographic,
                   marketing illustration that draws a flow, or a photograph whose subject is a
                   screen showing a model). The note names what it is.
  E2-no-ai-element the page publishes a BPMN 2.0 diagram with no AI element inside it; the note
                   quotes the page's AI mention and says what that mention refers to instead.

  python ledgers/_ts_batch6.py            -- preview
  python ledgers/_ts_batch6.py --write    -- write trisotech.raw/batch6.json
"""
import json, os, re, sys

import _ts_figs as F
import _ts_fig2 as G
import _ts_rows as R


NOTATION = re.compile(r"(?<![A-Za-z])(BPMN|CMMN|DMN|BPM\+|DRD|BPMN\+)(?![A-Za-z])|Business Process Model and Notation|Decision Model and Notation|Case Management Model and Notation")
CHROME = re.compile(r"^(Home|Resources|Webinars|Blog|Our|Presented|Play|Description|By |Search|Videos|Podcasts|Events|Contact|About|Solutions|Capabilities|Use Cases)")
CHROME2 = re.compile(r"Webinars Home|Presented By|Video Time|Read Time|Toggle navigation|Request Pricing")
NAV = re.compile(r"(?i)^(edit profile|cookie|logout|toggle navigation|request pricing|search|accept|subscribe|sign up|privacy|contact|about us|careers)")


def sents(page):
    t = (C.get(page) or {}).get("text") or ""
    out = []
    for s in re.split(r"(?<=[.!?])\s+", t):
        s = " ".join(s.split())
        if 25 <= len(s) <= 400 and not NAV.match(s) and not CHROME.match(s) and not CHROME2.search(s):
            out.append(s)
    return out


def cut(s, n=25):
    w = s.split()
    return " ".join(w[:n]) + ("…" if len(w) > n else "")


RAW = F.RAW
C = json.load(open(os.path.join(RAW, "content.json"), encoding="utf-8"))

# slug -> (verdict, code, judgment, note)
D = {
 # ---- artefacts that are not BPMN ---------------------------------------------------------
 "dmn-meet-machine-learning": ("E", "E1-not-bpmn", True,
   "Not BPMN: 12 of the 15 figures are DMN. Figure 12 is a decision requirements diagram (decision "
   "'Churn risk', business knowledge model 'Churn prediction PMML', input data 'Customer'); figures "
   "1, 5 and 14 are DMN decision tables ('Customer Calls' / 'Churn'); figures 3, 4, 8, 10, 11, 13 are "
   "the modeller's boxed-expression and decision-table panels; figures 6 and 7 are data tables. The "
   "DRD's BKM knowledge requirement is a PMML machine-learning model, so an AI element does sit "
   "inside the model - the ruling that DMN is not BPMN is what excludes it, not an absence of AI."),
 "modeling-virus-transmission-on-an-airplane": ("E", "E1-not-bpmn", True,
   "Not BPMN: figure 'drd-1.png' is a DMN decision requirements diagram (decision 'SARS transmission "
   "probability', BKM 'fit', input data 'row delta'); 'bkm.png' and 'invocation-2.png' are DMN boxed "
   "expressions - the 'fit' business knowledge model declares a model knowledge requirement, 'KNIME "
   "Linear Regression', and the invocation feeds it 'regression.tx'/'regression.txsq'; "
   "'knime-regression2.png' is a KNIME visual data-flow workflow (File Reader, Linear Regression "
   "Learner, Regression Predictor, PMML Writer); the remaining figures are line charts and data "
   "tables. A regression model does sit inside the DMN decision model, but DMN is not BPMN."),
 "covid-19": ("E", "E1-not-bpmn", True,
   "Not BPMN: the page's 30 clinical figures are DMN decision requirements diagrams and boxed "
   "expressions (decisions drawn as rectangles with the decision-table marker, input data as ovals, "
   "knowledge sources as folded-corner shapes, e.g. 'COVID19 Adult Mortality Model Zhou', "
   "'Coronavirus Lancet Flow Diagram', 'COVID19QuarantineRelease'), plus one image of a Business "
   "Rules text listing. The page's AI mention is about the cited literature (see the article text on "
   "machine-learning prognostic models) rather than about an element inside these diagrams."),
 "digital-automation-suite": ("E", "E1-not-bpmn", True,
   "Not BPMN: the page's one real figure, 'diagrams_automate-everything.jpg' (2030x1231), is a "
   "product architecture box diagram - persona icons feeding the BPMN / CMMN / DMN / CQL / PMML "
   "components of the Digital Enterprise Suite, with OpenAPI and docker. The other eight images are "
   "140x140 feature icons (Workflow Automation, PMML, Decision Automation, Service Library, CQL, "
   "Case Automation, Cloud Execution, DDC)."),
 "the-case-for-a-business-automation-center-of-excellence": ("E", "E1-not-bpmn", True,
   "Not BPMN: Figure 01 is a taxonomy infographic (three columns 'Analysis technologies / Automation "
   "technologies / Monitoring technologies' whose rows are labelled buttons: Process modeling, "
   "Decision modeling, Process mining, Simulation, ML training, Capture, Task (RPA), Process (BPM), "
   "Case (DCM), Decisions/rules, AI/ML, Event handling, Visualization, Predictive analytics, "
   "Recommendations, Digital twin); Figure 02 is a bubble-chart illustration ('Our completely unique "
   "tool that does everything')."),
 "discovering-processes-in-unusual-places": ("E", "E1-not-bpmn", True,
   "Not BPMN: 'sandy-kemsley-discovering-processes-diagram.png' (2370x588) is a plain activity "
   "flowchart reproduced from the cited research paper - labelled boxes 'Step 1: Pre-processing', "
   "'Step 2: Group emails by sender', 'Step 3: Discover frequent activities per employee' (containing "
   "'Learning frequent patterns of concepts', 'Group patterns into activities', 'Classifying frequent "
   "patterns'), 'Step 4: Group Similar Activities of Different Employees', with arrows annotated by "
   "data ('Emails sent by employees', 'WordNet Synonyms'). No events, gateways, pools or lanes. Its "
   "AI mention ('what the addition of AI techniques to these researchers' pattern discovery "
   "techniques could do') is a proposal about the cited research, not an element of the figure."),
 "healthcare-feature-set": ("E", "E1-not-bpmn", True,
   "Not BPMN: the page's figure 'webinar-clinical-workflows-and-decisions-page-M.jpg' (1200x848) is a "
   "promotional graphic - a laptop mock-up carrying a YouTube play button over a decorative "
   "rounded-rectangle-and-two-circles schematic with a stethoscope; the other image is a stock "
   "photograph with overlaid circular icons. Neither is a notation."),
 "caring-about-care-plans": ("E", "E1-not-bpmn", True,
   "Not BPMN: the page's only image is the decorative header illustration "
   "'Caring-about-Care-Plans-Header.jpg' (800x600) - a document outline, a heart, a circle and two "
   "rounded rectangles joined by arrows. The page's AI mention is about AI *producing* models "
   "(\"Claude and other LLMs have the ability to create BPMN and DMN models from documents if "
   "suitable skills are used.\"), not about an element inside a diagram."),
 "composability-and-packaged-business-capabilities": ("E", "E1-not-bpmn", True,
   "Not BPMN: the page's images are an icon and two 680x470 marketing photographs; in "
   "'banner-composability-healthcare.jpg' the tablet a person holds displays a small model diagram "
   "(yellow boxes on a flow), which is legible only as a shape at published size. A photograph of a "
   "screen is not a published artefact; no figure of any notation is published on the page."),
 "turn-your-legacy-erp-into-a-business-execution-platform": ("E", "E1-not-bpmn", True,
   "Not BPMN: the page's only image is the header 'Turn-Your-Legacy-ERP-into-a-Business-Execution-"
   "Platform.jpg' (800x600): boxes labelled 'ERP' with an arrow into a stack of boxes labelled "
   "'DMN', 'BPMN', 'CMMN'. It is a marketing illustration that names the notations, not a diagram "
   "drawn in any of them."),
 "low-code-no-code-and-pro-code": ("E", "E1-not-bpmn", True,
   "Not BPMN: 'diagrams-lcnc.jpg' (990x795) is an infographic - a segmented semicircular gauge whose "
   "callout lines descend to three labelled branches ('No Code: Drag-and-drop visual modeling and "
   "Stylegable Generated Forms via CSS', 'Low Code: Using Friendly Enough Expression Language (FEEL) "
   "for Logic, Mappings, Scripts +', 'Pro Code: Orchestrated via APIs'). The page's other images are "
   "an icon and two banner photographs whose screens show unreadable modelling-tool windows."),
 # ---- BPMN but no AI element inside the process --------------------------------------------
 "better-process-analysis-using-analytical-techniques": ("E", "E2-no-ai-element", True,
   "The page publishes BPMN 2.0: figures 1 and 4 show a pool ('Consolidated Process Model') with "
   "lanes 'BPM System', 'Legacy System', 'ERP System', a start event, the user tasks 'Start customer "
   "data entry' / 'Finish customer data entry' / 'Create customer record' / 'Create address record', "
   "exclusive gateways, the service tasks 'Check credit', 'Check PO', 'Enter order', 'Create order', "
   "an end event, and data stores ('Legacy System Event Log', 'ERP System Event Log', 'Consolidated "
   "Event Log') on data associations. No AI element appears inside either diagram. The AI mentions "
   "dismissed here are \"process mining (including desktop agents that monitor user actions across "
   "multiple applications) will be a critical tool for business analysts\" and the cited paper's use "
   "of machine learning to predict incident resolution times: both refer to the analytics applied to "
   "event logs (the logs the diagrams feed), described in prose, not drawn as a task or service in "
   "the models."),
 # ---- icons, logos, photographs, decorative headers only ----------------------------------
 "governed-agentic-orchestration": ("E", "E0-no-artefact", False,
   "No process artefact: the page publishes three 268x268 icons - the Model Context Protocol glyph, "
   "a shield-with-brain 'governed AI' icon and the Digital Enterprise Suite building icon. The page "
   "text is prose about BPM+ models as behavioural contracts for agents."),
 "the-changing-nature-of-work": ("E", "E0-no-artefact", False,
   "No process artefact: five 397x397 same-style line pictograms (stacked documents with a cross, an "
   "org chart, a worker at a laptop with ticked boxes, a gear routing to two people, a checklist with "
   "a gear). Icons used as article section markers, not a diagram of any notation."),
 "index": ("E", "E0-no-artefact", False,
   "No process artefact: the homepage publishes a rocket icon ('get-started.png') and the HL7 "
   "International 2025 AI Challenge awardee badge. The page text is prose about the platform."),
 "artificial-intelligence": ("E", "E0-no-artefact", False,
   "No process artefact: despite the filename 'diagram-innovation-ai.jpg' (1654x476), the image is a "
   "chip-with-brain glyph centred on a rounded diamond - an icon, like the 298x298 "
   "'innovation-loz_artificial-intelligence.png' beside it."),
 "agentic-ai": ("E", "E0-no-artefact", False,
   "No process artefact: a 268x268 network-with-brain icon and a 680x470 banner of the same icon."),
 "ai-without-losing-control": ("E", "E0-no-artefact", False,
   "No process artefact: the page publishes only the webinar thumbnail 'webinar-ai-without-losing-"
   "control-thumb.png' (298x298, a hand-shield-brain glyph). The page text describes AI 'On "
   "Orchestration, In Orchestration, and As Orchestration' but no model is published as a figure."),
 "are-you-standing-on-thin-ice-when-using-ai-for-healthcare": ("E", "E0-no-artefact", False,
   "No process artefact: the only image is the blog header 'thin-ice-Header.jpg' (800x600), a heart "
   "and cross with a circuit-brain glyph."),
 "bpm-plus-community-of-practice": ("E", "E0-no-artefact", False,
   "No process artefact: the page publishes no in-region image at all; its text describes the BPM+ "
   "Health member programme and Trisotech's decision, case and workflow modelling services."),
 "bpmn": ("E", "E0-no-artefact", False,
   "No process artefact: two 680x470 photo banners (a laptop screen, a clinician team) and "
   "'dms-workflow-modeler.png', which is a blue tile carrying a white letter 'B'. No BPMN diagram is "
   "published on the notation's own landing page."),
 "bring-your-own-ai": ("E", "E0-no-artefact", False,
   "No process artefact: a briefcase-with-brain icon and its banner rendering."),
 "business-intelligence": ("E", "E0-no-artefact", False,
   "No process artefact: a 298x298 dashboard icon and two 680x470 photo banners used as section "
   "headers."),
 "business-orchestration-and-automation-technologies": ("E", "E0-no-artefact", False,
   "No process artefact: a 268x268 icon of a person holding a chart and a gear, plus its banner "
   "rendering."),
 "business-rules-and-decision-management": ("E", "E0-no-artefact", False,
   "No process artefact: icons and photographs - 'innovation-loz_brms-to-dmn.png' is a 288x288 "
   "pictogram of three rounded rectangles under a rectangle, 'brms-to-dmn-manager.jpg' is a 2249x1500 "
   "stock photograph of a man at a desk, and 'business-rules.jpg' is a photograph of three "
   "clinicians."),
 "business-workflow-automation-software": ("E", "E0-no-artefact", False,
   "No process artefact: two 298x298 icons (a gear around a building, a gear around a bank) and the "
   "Digital Enterprise Suite / Digital Modeling Suite / Digital Automation Suite feature icons."),
 "cognitive-enterprise": ("E", "E0-no-artefact", False,
   "No process artefact: a single 298x298 brain-with-circuit icon."),
 "decision-centric-orchestration": ("E", "E0-no-artefact", False,
   "No process artefact: a lightbulb-and-people icon (268x268) and the same icon rendered on a "
   "banner."),
 "dmn": ("E", "E0-no-artefact", False,
   "No process artefact: two 680x392 photo banners (a financial-services desk, a clinical team) and "
   "'tile-dmn-modeler.png', an orange product tile carrying a stylised decision-table glyph with the "
   "words 'DMN Modeler'. No decision diagram is published on the notation's own landing page."),
 "explainable-artificial-intelligence": ("E", "E0-no-artefact", False,
   "No process artefact: a single 298x298 icon of a head profile with a circuit."),
 "fhirball": ("E", "E0-no-artefact", False,
   "No process artefact: the page publishes the 'FHIRBall - The FHIR Business Alliance' wordmark."),
 "intelligent-process-automation": ("E", "E0-no-artefact", False,
   "No process artefact: a single 298x298 icon of a lightbulb and a gear."),
 "model-context-protocol-mcp": ("E", "E0-no-artefact", False,
   "No process artefact: the Model Context Protocol wordmark (two sizes) and the Digital Automation "
   "Suite logo."),
 "openehr": ("E", "E0-no-artefact", False,
   "No process artefact: the openEHR wordmark, its 800x600 header, and a 'FHIRBall' illustration of "
   "two figures embracing."),
 "post-implementation-review": ("E", "E0-no-artefact", False,
   "No process artefact: the blog header 'From-Project-to-Program-Header.jpg' (800x600) is a "
   "decorative trend-curve illustration on an orange field with the letters 'PIR' and 'P1'."),
 "predictive-analytics": ("E", "E0-no-artefact", False,
   "No process artefact: a single 298x298 icon of a monitor showing a line chart."),
 "process-orchestration": ("E", "E0-no-artefact", False,
   "No process artefact: a lightbulb-and-people icon (268x268) and a 680x470 photograph of a man "
   "holding a tablet."),
 "robotic-process-automation": ("E", "E0-no-artefact", False,
   "No process artefact: a single 298x298 icon of a robotic arm over a conveyor with a gear."),
 "setting-the-world-on-fhir": ("E", "E0-no-artefact", False,
   "No process artefact: the page publishes a photograph of the printed case-study document "
   "('2025-setting-the-world-on-fhir-article.jpg'), not a figure."),
 "smart-on-fhir": ("E", "E0-no-artefact", False,
   "No process artefact: the HL7 FHIR wordmark and the Healthcare Feature Set icon (a stethoscope "
   "over a laptop)."),
 "the-roles-of-ai": ("E", "E0-no-artefact", False,
   "No process artefact: a network-with-brain icon (268x268) and its banner rendering."),
 "why-byoai": ("E", "E0-no-artefact", False,
   "No process artefact: the blog header 'why-byoai-Header.jpg' (800x600), a briefcase with a brain "
   "chip and a question mark."),
}


def pick(page):
    ss = sents(page)
    if not ss:
        t = (C.get(page) or {}).get("text") or ""
        ss = [" ".join(s.split()) for s in re.split(r"(?<=[.!?])\s+", t) if 25 <= len(s) <= 400]
    def score(s):
        return 3 * len(NOTATION.findall(s)) + len(F.AI.findall(s))
    return cut(max(ss, key=score))


rows = []
todo = [s for b, s in G.todo() if b == "figures"]
print("figure pages in this batch: %d" % len(todo))
extra = {
 "orchestrating-generative-ai-in-business-process-models": {
   "verdict": "INCLUDE", "code": "", "judgment": True,
   "record": "corpus/trisotech/003_orchestrating-generative-ai-in-business-process-models.md",
   "capture": "corpus/trisotech/003_orchestrating-generative-ai-figure1-bpmn-chatgpt-task.png",
   "note": "Already collected in this session: figure 1 is a BPMN 2.0 fragment whose task 'Generate "
           "Explanation' carries an OpenAI/ChatGPT connector marker, downstream of the DMN-annotated "
           "task 'WHO Anemia Grades'.",
   "needs_visual_check": False, "needs_human_ruling": False},
 "decision-orchestration-with-agentic-ai": {
   "verdict": "INCLUDE", "code": "", "judgment": True,
   "record": "corpus/trisotech/026_decision-orchestration-with-agentic-ai.md",
   "capture": "corpus/trisotech/026_decision-orchestration-with-agentic-ai-figure10-bpmn-user-task.png",
   "note": "Figure 10 is a BPMN 2.0 diagram whose user task 'Validate Prescription' is bound to an "
           "OpenAI agent in figure 12; record 026.",
   "needs_visual_check": False, "needs_human_ruling": False},
}
for page in todo:
    if page in extra:
        r = {"key": page, "judged_from": "opened https://www.trisotech.com/%s/ and viewed every "
             "in-region image at published size on 2026-09-25" % page, "evidence": pick(page)}
        r.update(extra[page])
    else:
        v, code, j, note = D[page]
        r = {"key": page, "verdict": "EXCLUDE", "code": code, "judgment": j,
             "evidence": pick(page), "note": note, "record": None, "capture": None,
             "needs_visual_check": False, "needs_human_ruling": False,
             "judged_from": "opened https://www.trisotech.com/%s/ and viewed every in-region image "
             "at published size (contact sheets + full-size views of the diagram-like ones) on "
             "2026-09-25" % page}
    rows.append(r)

missing = [p for p in todo if p not in D and p not in extra]
if missing:
    print("NO DECISION FOR: %s" % missing)
bad = 0
for r in rows:
    t = " ".join(((C.get(r["key"]) or {}).get("text") or "").split())
    if r["evidence"].rstrip("…") not in t:
        bad += 1
        print("NON-VERBATIM %s: %s" % (r["key"], r["evidence"]))
print("rows %d  non-verbatim %d  E0 %d  E1 %d  E2 %d  INCLUDE %d" % (
    len(rows), bad,
    sum(1 for r in rows if r.get("code") == "E0-no-artefact"),
    sum(1 for r in rows if r.get("code") == "E1-not-bpmn"),
    sum(1 for r in rows if r.get("code") == "E2-no-ai-element"),
    sum(1 for r in rows if r["verdict"] == "INCLUDE")))
if "--write" in sys.argv:
    json.dump({"source": "trisotech", "batch": 6, "family": "figures", "dispositions": rows},
              open(os.path.join(RAW, "batch6.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote trisotech.raw/batch6.json")
