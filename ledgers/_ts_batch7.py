"""trisotech: build batch7 -- the deck pages whose *published per-slide text* carries an AI term.

Why a separate batch: the emit() mechanical branch decides deck pages on the page's own text and its
image file names only. 105 of the 106 decks in this source publish their per-slide text ("transcript")
on the host page, and that text is part of the published artefact -- the deck's own slides. 43 decks
carry an AI/LLM term there (trisotech.raw/deck_ai.txt is the worklist), and this batch records the
hand verdict for every one of them, plus 5-min-intro-to-bpmn-presentation, whose own page text
narrates an "AI kind of task" inside its BPMN diagram.

  python ledgers/_ts_batch7.py dry    -- print the chosen verbatim quote for every deck, write nothing
  python ledgers/_ts_batch7.py build  -- write trisotech.raw/batch7.json (dispositions + captures)

Evidence quotes are contiguous verbatim substrings of the page: either a supplied literal (verified
against the saved page text + the deck transcript) or a 25-word window of the slide text around a
`must` token.
"""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
_spec = importlib.util.spec_from_file_location("deck3", os.path.join(ROOT, "_ts_deck3.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)

SCREEN = {r["slug"]: r for r in json.load(open(os.path.join(RAW, "screen.json"), encoding="utf-8"))}


def norm(s):
    return " ".join((s or "").replace(" ", " ").split())


def deck_text(slug):
    return norm(" ".join(D.trans(slug)))


def page_text(slug):
    return norm(SCREEN[slug]["text"])


def window(text, must, n=25):
    """A <=25-word verbatim window of `text` around the first occurrence of `must`."""
    w = text.split()
    i = text.lower().find(must.lower())
    if i < 0:
        return None
    k = len(text[:i].split())            # word index of the match
    start = max(0, k - 8)
    return " ".join(w[start:start + n])


A = "https://www.trisotech.com/%s/"
VIEWED = ("opened https://www.trisotech.com/%s/ and read its published per-slide text (all %d slides) "
          "plus 5-column overview sheets of every slide, with full-size views of the diagram slides "
          "named in the note, 2026-09-25")

# slug, verdict, code, judgment, must/q, note, record, capture, nvc, nhr, question, full-size views
DECK = [
 # ---- E1-not-bpmn: drawn figures, but not BPMN 2.0 -------------------------------------------------
 dict(slug="harness-genai-and-agentic-ai-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="GenAI",
      note="No BPMN 2.0 process diagram anywhere in the 40 slides: what the deck draws are layer/box "
           "architecture pictures (the BPM+ stack, the agentic automation layers) and product "
           "screenshots. The AI content is the talk's own argument about governing GenAI and agentic "
           "AI - prose and architecture drawings, not an AI element inside a process diagram.",
      seen="overview sheets of all 40 slides"),
 dict(slug="reimagining-insurance-claims-performance-growth-presentation", verdict="EXCLUDE", code="E1-not-bpmn",
      judgment=True, must="Business Agents",
      note="Not BPMN 2.0: the deck's model picture is the 'Case Mgmt. Model - The Insurance Claim "
           "Control Tower' slide, a case-management/architecture drawing with an SDMN role column. The "
           "AI term the screen caught is 'Business Agents', the SDMN name for a business-actor role, "
           "not an AI element.",
      seen="overview sheet of all 11 slides + slide 2 and 3 at full size"),
 dict(slug="dynamically-mastering-insurance-claims-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Business Agents",
      note="Not BPMN 2.0: the model-like slides are the SDMN / 'Business Agents' role matrix and "
           "architecture drawings from the same Case Management talk. 'Business Agents' is an SDMN "
           "business-actor role name; the deck's AI-flavoured sentence ('Need for empowering humans "
           "and systems for best outcomes') is a goal statement, not a task in a process.",
      seen="overview sheets of all 34 slides + slide 4 at full size"),
 dict(slug="revolutionizing-credit-risk-management-in-banking-presentation", verdict="EXCLUDE", code="E1-not-bpmn",
      judgment=True, must="Business Agents",
      note="Not BPMN 2.0: DecisionCAMP 2024 slide set whose model pictures are the SDMN / 'Business "
           "Agents' role matrix (IT Business / Traditional IT Developers / Business Logic Developers / "
           "Data Scientists / Data Steward) and architecture drawings. 'Business Agents' is the SDMN "
           "actor-role name, not an AI task inside a process.",
      seen="overview sheet of all 19 slides + the Business Agents slide at full size"),
 dict(slug="who-made-that-decision-governing-decisions-in-the-age-of-ai-agents-presentation",
      verdict="EXCLUDE", code="E1-not-bpmn", judgment=True, must="AI performs work",
      note="The deck argues about governing decisions made by AI agents and contrasts modelling "
           "notations ('BPMN: structured processes / Tasks show exactly where AI performs work') in "
           "comparison slides, but the pictures it publishes are the Decision Canvas / SDMN "
           "architecture drawings and product screenshots - no BPMN 2.0 process diagram with an AI "
           "element inside it.",
      seen="overview sheets of all 52 slides + slides 30 and 31 at full size"),
 dict(slug="automating-and-orchestrating-processes-and-decisions-presentation", verdict="EXCLUDE", code="E1-not-bpmn",
      judgment=True, must="AI",
      note="Not BPMN 2.0: the deck's diagrams are the orchestration/architecture layer pictures from "
           "the S&P Global session. Its AI material is the analyst argument about orchestrating "
           "process and decision automation.",
      seen="overview sheets of all 56 slides + the diagram-like slides at full size"),
 dict(slug="how-bpm-health-complements-fhir-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      q="we can even orchestrate AI and machine learning into that orchestration",
      note="Four-slide deck. Its only drawing is the 'BPM+ Value Add' layered stack (Workflow and "
           "Decision Automation / Orchestration of knowledge / Machine Learning listed as a layer). "
           "That is an architecture picture, not a BPMN 2.0 process diagram. The AI mention the page "
           "carries ('we can even orchestrate AI and machine learning into that orchestration') is the "
           "same orchestration-layer claim.",
      seen="overview sheet of all 4 slides"),
 dict(slug="improving-care-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Intelligent Healthcare Automation",
      note="Not BPMN 2.0: the deck's model-like pictures are the 'BPM+ Value Add' layered stack and "
           "the telemedicine architecture drawings. No process diagram with tasks/gateways is "
           "published, and no AI element sits inside one.",
      seen="overview sheets of all 26 slides"),
 dict(slug="explainable-ai-using-dead-simple-decision-management", verdict="EXCLUDE", code="E1-not-bpmn",
      judgment=True, must="Explainable AI is required",
      note="Not BPMN 2.0: the artefacts are DMN decision requirement diagrams / decision-model "
           "pictures and decision tables - the 'dead simple decision management' of the title. Under "
           "the operator's ruling a drawn DMN DRD with no AI element inside the model is E1-not-bpmn.",
      seen="overview sheets of all 35 slides"),
 dict(slug="decision-automation-using-models-services-dashboards", verdict="EXCLUDE", code="E1-not-bpmn",
      judgment=True, must="artificial Intelligence",
      note="Not BPMN 2.0: the slide set is about DMN decision models, decision services and "
           "dashboards; the deck states that symbolic and sub-symbolic AI approaches can be used "
           "jointly with DMN, but the artefacts it publishes are DMN models and dashboard/service "
           "screenshots, not a BPMN process diagram.",
      seen="overview sheets of all 34 slides"),
 dict(slug="ai-agents-in-healthcare-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="AI Agents",
      note="Not BPMN 2.0: the deck's pictures are governance/architecture drawings and the agent "
           "landscape tables. Its AI content (trusted AI agents in healthcare, from opaque to "
           "governed automation) is presented in prose and architecture diagrams, not as an AI element "
           "inside a BPMN process.",
      seen="overview sheets of all 18 slides"),
 dict(slug="low-code-neuro-symbolic-agents-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Neuro-Symbolic AI Field",
      note="Not BPMN 2.0: the deck's artefacts are the neuro-symbolic architecture drawings (FEEL, "
           "DMN decision models, prompt-engineering layers) and product screenshots. No BPMN 2.0 "
           "process diagram is published.",
      seen="overview sheets of all 55 slides"),
 dict(slug="enterprise-ai-in-2026-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="neuro-symbolic architecture",
      note="Not BPMN 2.0: a forward-looking enterprise-AI talk whose slides are text, icons and "
           "architecture/maturity drawings ('AI and BPM+ A neuro-symbolic architecture', 'the "
           "architecture of authority', the control/context/AI layer picture); no process diagram is "
           "published.",
      seen="overview sheets of all 22 slides"),
 dict(slug="knowledge-worker-copilot-in-the-loop-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Neuro-Symbolic AI",
      note="Not BPMN 2.0: the deck's pictures are copilot/architecture drawings ('KW CoPilot "
           "leverages Neuro-Symbolic AI - The KW Copilot combines the adaptability of Generative AI "
           "with deterministic BPM+ models') and product screenshots of the Knowledge Worker Copilot; "
           "the AI content is the copilot's design argument, not an AI element inside a BPMN diagram.",
      seen="overview sheets of all 34 slides"),
 dict(slug="mastering-decision-orchestration-presentation", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Role of AI in Decision",
      note="Not BPMN 2.0: decision-orchestration talk; the artefacts are DMN decision models, AI "
           "taxonomy slides ('Various Forms of AI', 'Generative AI (GenAI)') and an orchestration "
           "reference architecture ('Predictive AI / Generative AI / Symbolic AI / PMML / AI Models / "
           "Decision Orchestration Layer') - no BPMN process diagram.",
      seen="overview sheets of all 51 slides"),
 dict(slug="it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision-presentation",
      verdict="EXCLUDE", code="E1-not-bpmn", judgment=True, must="Developing AI-Driven Decision Frameworks",
      note="Not BPMN 2.0: the deck's model pictures are DMN decision models and decision-centric "
           "orchestration drawings; its AI material is taxonomy and decision-framework prose; no BPMN "
           "2.0 process diagram is published.",
      seen="overview sheets of all 32 slides"),
 dict(slug="ai-microservices-apis-and-business-automation-as-a-service", verdict="EXCLUDE", code="E1-not-bpmn",
      judgment=True, must="three tiers of Artificial",
      note="Not BPMN 2.0: the deck's artefacts are microservice/API architecture and deployment "
           "drawings (containers, gateways, REST endpoints), plus AI taxonomy slides ('The three tiers "
           "of Artificial Intelligence', 'The AI Black Box Problem'); not process diagrams with tasks "
           "and gateways.",
      seen="overview sheets of all 39 slides"),
 dict(slug="decision-service-daas-dmn-platform-revolution", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Black Box AI",
      note="Not BPMN 2.0: 20 slides of platform/architecture box diagrams (Decision as a Service "
           "platform, DMN modeler, cloud execution, service library, REST executions, OpenAPI) plus "
           "the 'Business Rule Management Systems (BRMS) vs Current AI Resurgence: Deep Neural Nets' "
           "comparison. The AI material ('Black Box AI', 'Explainable AI is required') is platform "
           "positioning, and the drawings are architecture pictures, not process diagrams.",
      seen="overview sheet of all 20 slides (the deck's only sheet)"),
 dict(slug="digital-enterprise-graph", verdict="EXCLUDE", code="E1-not-bpmn", judgment=True,
      must="Agent based execution",
      note="Not BPMN 2.0: the artefacts are node-link views of the Digital Enterprise Graph / Insight "
           "Analyzer (screenshots of graph visualisations, whose insight pane lists BPMN/CMMN/DMN as "
           "node types) and marketing infographics (head icons, network drawings, triangles). The AI "
           "terms the screen caught are 'Agent based execution' in the coexistence list (a "
           "business-agent/responsibility item, next to 'Business Policies and Decision "
           "Specification') and 'Analyzed (Mining) Machine Learning' in a capability list.",
      seen="overview sheets of all 32 slides + slide 25 at full size"),
 # ---- E2-no-ai-element: BPMN 2.0 present, AI mention dismissed -------------------------------------
 dict(slug="adding-smarts-to-drug-package-inserts-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="BPM+ Value Add",
      note="BPMN 2.0 pathways are published (the drug-package-insert clinical pathway), but the AI "
           "wording the screen caught is the shared 'BPM+ Value Add' layer slide listing 'Intelligent "
           "Healthcare Automation' and 'Machine Learning' as a stack layer - an architecture claim, "
           "not an element inside a process diagram.",
      seen="overview sheets of all 30 slides + the pathway slides at full size"),
 dict(slug="pharma-fhir-workflows-and-decisions-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="BPM+ Value Add",
      note="Same family as the other BPM+ Health decks: the AI term sits in the 'BPM+ Value Add' "
           "layer slide (Machine Learning as a stack layer), while the published models are BPMN "
           "workflows and DMN decisions with no AI element inside them.",
      seen="overview sheets of all 26 slides"),
 dict(slug="integrating-clinical-workflows-and-decisions-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="BPM+Value Add",
      note="The BPMN clinical workflows and DMN decisions are published, but the only AI mention is "
           "the 'BPM+Value Add' stack slide (Machine Learning listed as a layer of the automation "
           "stack), not an AI element inside the process.",
      seen="overview sheets of all 35 slides"),
 dict(slug="optimizing-preoperative-assessments-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="AI|Machine|intelligent",
      note="BPMN 2.0 preoperative-assessment workflows are published; the AI wording comes from the "
           "same BPM+ Value Add / intelligent-automation framing, not from a task inside the process "
           "diagram.",
      seen="overview sheets of all 21 slides + the workflow slides at full size"),
 dict(slug="process-automation-in-telemedicine-the-italian-perspective-presentation",
      verdict="EXCLUDE", code="E2-no-ai-element", judgment=True, must="Machine|Intelligent|AI",
      note="Telemedicine BPMN pathways are published; the AI mention is the 'BPM+ Value Add' stack "
           "slide (Machine Learning / Intelligent Healthcare Automation as a layer), not an element "
           "inside the process.",
      seen="overview sheets of all 23 slides"),
 dict(slug="process-automation-in-telemedicine-reducing-risks-presentation", verdict="EXCLUDE",
      code="E2-no-ai-element", judgment=True, must="Machine|Intelligent|AI",
      note="Telemedicine BPMN pathways are published; the AI mention is the 'BPM+ Value Add' stack "
           "slide, not an element inside the process.",
      seen="overview sheets of all 26 slides"),
 dict(slug="bpm-automation-combined-to-fhir-consent-resource-presentation", verdict="EXCLUDE",
      code="E2-no-ai-element", judgment=True, must="BPM+ Value Add",
      note="BPMN consent workflows are published; the AI mention is the shared 'BPM+ Value Add' stack "
           "slide, not an element inside the process.",
      seen="overview sheets of all 31 slides + the consent pathway slides at full size"),
 dict(slug="how-to-capture-business-decisions-using-dmn-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="may invoke predictive models",
      note="DMN/BPMN teaching deck: the AI-adjacent wording is about PMML predictive models sitting "
           "beside BPMN and DMN ('BPMN: deals with Business Processes ... May invoke decisions, and "
           "may invoke predictive models'). The published process diagrams themselves carry no AI "
           "element; the predictive-model material is drawn as separate DMN/PMML pictures.",
      seen="overview sheets of all 40 slides + slides 13 and 34 at full size"),
 dict(slug="beyond-decision-models-slides", verdict="EXCLUDE", code="E2-no-ai-element", judgment=True,
      must="AI techniques alone",
      note="DecisionX 2019 deck on decision management and digital transformation: the AI mentions "
           "are analyst framing (Forrester's tech radar ranking decision management as the top AI "
           "technology; RPA/Blockchain/Decision Management/AI listed as new tech). The published "
           "models are DMN decision models, not BPMN processes carrying an AI element.",
      seen="overview sheets of all 52 slides + slides 42 and 48 at full size"),
 dict(slug="hl7-ai-challenge-winners-presentation", verdict="UNCERTAIN", code="", judgment=True,
      q="Call any LLM API of your choice with mappings in and out of the task",
      note="Slide 7 ('Some Trisotech AI Features') draws three BPMN-styled task boxes with AI "
           "bindings annotated onto them - 'REST call to an LLM' carrying the gear service-task marker "
           "and the OpenAI swirl ('Call any LLM API of your choice with mappings in and out of the "
           "task'), 'A user Task' with an agent marker ('Agent is provided with task description, "
           "Inputs and expected outputs') and an LLM/brain icon wired by 'MCP' to a dashed BPM+ box "
           "holding the DMN, BPMN and CMMN model icons. The deck's own headline claim is 'BPM+ "
           "Determinism and HL7 Integration for AI Agents' (slide 2). But the slide is a capability "
           "listing, not a process: the task boxes carry no sequence flows, no start/end events, and "
           "the red curved arrows on them are annotations. Slide 3 is an architecture/icon drawing and "
           "the other eight slides are text. Whether a BPMN task shape with an LLM binding counts as "
           "an AI element inside a process-artefact is the open question, so this is UNCERTAIN rather "
           "than E1 or E2.",
      record="corpus/trisotech/036_hl7-ai-challenge-winners-presentation.md",
      capture="corpus/trisotech/036_hl7-ai-challenge-winners-agent-as-performer-features.png",
      nvc=True, nhr=True,
      question="Slide 7 shows three Trisotech task boxes drawn in BPMN task shape, one a service task "
               "bound to an LLM ('REST call to an LLM', gear marker + OpenAI swirl) and one a user task "
               "labelled 'Agent as Performer', but with no sequence flows or start/end events - a "
               "capability listing rather than a process. Does a BPMN task shape with an LLM/agent "
               "binding, published outside any process flow, count as an AI element inside a process "
               "artefact?",
      seen="overview sheet of all 10 slides + slides 2, 3 and 7 at full size"),
 dict(slug="contracts-and-the-knowledge-worker-copilot-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="RAG|retrieval",
      note="The AI content is the Knowledge Worker Copilot and RAG over real-estate contracts; the "
           "published BPMN process diagrams of the contract workflows do not carry an AI element "
           "inside the process - the copilot is shown in product screenshots and prose.",
      seen="overview sheets of all 28 slides"),
 dict(slug="clinician-centric-data-and-ai-integration-in-healthcare-presentation", verdict="EXCLUDE",
      code="E2-no-ai-element", judgment=True, must="AI|Machine|generative",
      note="The deck discusses generative AI / machine learning for clinician-centric integration, "
           "but the published BPMN pathways and DMN decisions carry no AI element inside the model; "
           "the AI material is the argument and the architecture slides.",
      seen="overview sheets of all 31 slides"),
 dict(slug="automation-of-loan-origination-presentation", verdict="EXCLUDE", code="E2-no-ai-element",
      judgment=True, must="newest shiny toy",
      note="Loan-origination BPMN process and DMN decisions are published with no AI element inside "
           "them; the AI mentions are the speaker's title ('Brian Stucky leads the Rocket Technology "
           "Ethical Artificial Intelligence team at Quicken Loans') and the caution 'Too much focus on "
           "the newest shiny toy! Blockchain Data aggregation AI - Focus should be here!', i.e. AI as "
           "a distraction from modelling the process.",
      seen="overview sheets of all 18 slides"),
 # ---- E3 duplicate ---------------------------------------------------------------------------------
 dict(slug="ai-fhir-and-bpm-in-suicide-prevention-presentation", verdict="EXCLUDE", code="E3-duplicate",
      judgment=False, must="AI, FHIR",
      dup_of="suicide-prevention-with-modeling-tools",
      note="The same talk as the blog post 'suicide prevention with modeling tools' already recorded "
           "(record 001): the deck republishes the same two BPMN diagrams (the Generative-AI "
           "'Monitor Suicide Ideation' task model and its human-only baseline). Same diagram, second "
           "URL: E3 with duplicate_of.",
      seen="overview sheet of all 15 slides + the two BPMN diagram slides at full size"),
 # ---- INCLUDE --------------------------------------------------------------------------------------
 dict(slug="bpmn-user-tasks-for-humans-and-ai-agents-presentation", verdict="INCLUDE", code="", judgment=True,
      must="AI Performer",
      note="BPMN 2.0 process diagrams with AI elements inside them. Slide 20 ('DEMO 4: Dynamic "
           "supervision') is a full BPMN model - start event, user task 'Evaluate Appraisal Quality' "
           "carrying the blue 'AI Reviewer' performer badge, the business-rule task 'Determine Next "
           "Available Actions', 'Manual Review' carrying a 'Collateral R...' badge, 'Senior Review' "
           "with 'Senior Colla...' badge, exclusive gateways, end events 'Appraisal Approved' / "
           "'Request more comparables' / 'Appraisal Rejected' and data objects (House Appraisal, "
           "Appraisal Quality, Next Available Actions, Next Action). Slide 23 ('DEMO 5: Unsupervised "
           "Autonomous AI Performer') is the same notation with the 'AI Reviewer' badge on 'Evaluate "
           "Appraisal Quality' and the bullets 'Context provided to the AI Performer: Task "
           "Description, Data Input(s), Output format dictated by Data Output(s)'. Verified at full "
           "size.",
      record="corpus/trisotech/027_bpmn-user-tasks-for-humans-and-ai-agents-presentation.md",
      capture="corpus/trisotech/027_bpmn-user-tasks-for-humans-and-ai-agents-demo4-dynamic-supervision.png",
      seen="overview sheets of all 25 slides + slides 13, 20 and 23 at full size"),
 dict(slug="the-role-of-genai-presentation", verdict="INCLUDE", code="", judgment=True, must="LLM",
      note="BPMN 2.0 process with a prompt-execution task inside it: slide 24 ('Using BPMN for "
           "Effective Prompt Management') publishes a 'Notional BPMN Diagram to ease understanding' - "
           "start event 'Execute Prompt', user tasks 'Entry Prompts', 'Build EE by Topic Prompt', "
           "'Prompt Execution', 'Decide Output from Prompt Output', 'Assign String to Object' (in the "
           "'Stress test loop'), the exclusive gateways, the end event 'Prompt Execution Results' and "
           "the data objects Prompt / Free Text / Prompt Type / Prompt Output / Prompt Result / EE "
           "Prompt Object / Prompt Datastore (database icon). The slide's own bullets name the "
           "generative-AI element: 'Store prompts in datastores', 'The interactions between the prompt "
           "and the LLM is complex', 'Consider provisions for stress testing prompts'. Verified at "
           "full size.",
      record="corpus/trisotech/028_the-role-of-genai-presentation.md",
      capture="corpus/trisotech/028_the-role-of-genai-bpmn-prompt-management.png",
      seen="overview sheets of all 27 slides + slide 24 at full size"),
 dict(slug="generative-ai-and-regulatory-compliance-presentation", verdict="INCLUDE", code="", judgment=True,
      must="prompt|LLM|GenAI|generative",
      note="BPMN 2.0 process carrying prompt-execution tasks: slide 19 ('Term Extraction Process') is "
           "a full BPMN model - start event 'Terms extraction Start', tasks 'Initialize', 'Extract "
           "Terms', the highlighted 'Execute Term Prompt', 'Flatten Term List', 'Clean up Term List', "
           "'Clean Terms', the loop back labelled 'next citation', end event 'Next Definition'; a "
           "second pool chain below ('Print Prompt', 'Make term definition', 'Final Term Definitions', "
           "'Term End') with its own data objects (Extracts, terms, term list, Clean term list, List "
           "count, Cleaned Term List, Result, Term Definitions, cql, Definitions). The two "
           "'...Prompt' tasks are the generative-AI steps of the pipeline. Verified at full size.",
      record="corpus/trisotech/029_generative-ai-and-regulatory-compliance-presentation.md",
      capture="corpus/trisotech/029_generative-ai-and-regulatory-compliance-bpmn-term-extraction.png",
      seen="overview sheets of all 28 slides + slide 19 at full size"),
 dict(slug="5-min-intro-to-bpmn-presentation", verdict="INCLUDE", code="", judgment=True,
      q="The next task is a PMML or Predictive Model task (an AI kind of task).",
      note="BPMN 2.0 process with an AI task inside it. Slide 7 ('Visual Story of what needs to be "
           "done') is a BPMN model - a pool ('External participant to the process'), start event, "
           "'External Service Task' (gear marker), the 'PMML Predictive Model Task' (P badge), 'CQL "
           "Clinical Measure Task' (C badge), 'DMN Decision Task' (table marker), the exclusive "
           "gateway ('Routing behavior'), the CMMN case task and the collapsed BPMN sub-process, two "
           "end events, an intermediate message event, and a data object with its data association. "
           "The page's own narration of that diagram says: 'The gear marker here says that this is a "
           "service task ... The next task is a PMML or Predictive Model task (an AI kind of task). "
           "Next, we have a CQL task.' Verified at full size.",
      record="corpus/trisotech/030_5-min-intro-to-bpmn-presentation.md",
      capture="corpus/trisotech/030_5-min-intro-to-bpmn-bpmn-pmml-predictive-task.png",
      seen="overview sheet of all 9 slides + slide 7 at full size"),
 dict(slug="intelligent-assistance-for-knowledge-workers-presentation", verdict="INCLUDE", code="",
      judgment=True,
      q="Both the Intelligent Agent and the NLP Situational Lifting presented herein were implemented using Low Code language FEEL and BPM+ Models",
      note="BPMN 2.0 process whose tasks are the AI pipeline: slide 47 ('NLP Situational Lifting - "
           "Process in BPMN') is a BPMN model - start event 'Start NLP Situational Lifting', the three "
           "tasks 'NLP Detection', 'Concept Lifting', 'Semantic Lifting' (each with the collapsed "
           "sub-process marker), end event 'NLP Situational Lifting End', and the data objects "
           "Paragraph, Entities, Sentences, Differentiated Entities, Situational Business Events, "
           "Situational Business Objects with their data associations. The deck's own text names the "
           "AI: 'The key AI techniques for NLP are: Optical Character Recognition ... Entity "
           "Extraction ...' and 'Both the Intelligent Agent and the NLP Situational Lifting presented "
           "herein were implemented using Low Code language FEEL and BPM+ Models'; slides 35/38-40 "
           "name the pre-trained models used (Google Natural Language, Amazon Comprehend, Microsoft "
           "LUIS). Verified at full size.",
      record="corpus/trisotech/031_intelligent-assistance-for-knowledge-workers-presentation.md",
      capture="corpus/trisotech/031_intelligent-assistance-nlp-situational-lifting-bpmn.png",
      seen="overview sheets of all 57 slides + slide 47 at full size"),
 # ---- UNCERTAIN ------------------------------------------------------------------------------------
 dict(slug="ai-driven-healthcare-orchestration-presentation", verdict="UNCERTAIN", code="", judgment=True,
      must="AI supporting",
      note="The deck's process pictures are BPMN-flavoured drawings rendered inside a monitor mock-up "
           "(slide 19: start event, 'Listen for new data', 'Aggregate risk factor data', 'CDS risk "
           "calculation', 'Provider 1 determine risk level', a decision gateway, the 'CDS "
           "recommendation' data object and an 'Unlikely' loop), with an AI robot drawn above the "
           "process rather than bound to a task. The AI element's implementation is not visible "
           "inside the published model, so this is UNCERTAIN rather than E2.",
      record="corpus/trisotech/032_ai-driven-healthcare-orchestration-presentation.md",
      capture="corpus/trisotech/032_ai-driven-healthcare-orchestration-digital-health-team-process.png",
      nvc=True,
      question="Slide 19 draws a process (listen/aggregate/CDS risk calculation/provider decision) "
               "with an AI robot illustrated above it, and the talk is about AI agents performing in "
               "healthcare orchestration. Is that drawing a BPMN 2.0 model whose AI performer is "
               "simply not visible in the published frame, and does an AI agent illustrated beside "
               "(rather than bound inside) the process count as the AI element?",
      seen="overview sheets of all 26 slides + slide 19 at full size"),
 dict(slug="himss2026-dana-farber-presentation", verdict="UNCERTAIN", code="", judgment=True,
      q="AI agents act as performers within orchestrated pathways, analyzing symptom severity and routing escalations to the right nurse navigator in real time.",
      note="Slide 5 is a real BPMN 2.0 model ('Using BPMN to model shareable preemptive symptom "
           "management pathways': start event, 'Extract Active Care Plan', the 'Has an active Care "
           "Plan?' gateway, 'Extract Care Plan Information', 'Diagram Care Plan', 'Diagram Care Plan "
           "Fake DB', the 'Existing regimen information?' gateway, 'Generate No Information CDS Card', "
           "'Generate CDS Card Details', 'Generate Service Request', 'Generate Information CDS Card', "
           "two end events, ten data objects and their data associations) - and it carries no AI "
           "element: no AI performer badge, no AI task. The deck nevertheless claims agents inside "
           "these pathways in prose: slide 17 says 'Intelligent Triage Routing: AI agents act as "
           "performers within orchestrated pathways ... Agent as Performer', and slide 18 says the "
           "pathways are 'AI-augmented'. So the AI element is asserted but not visible inside the "
           "published model: UNCERTAIN, not E2. Slide 14 and 16 are Trisotech/CDS-Hooks/Epic "
           "architecture drawings.",
      record="corpus/trisotech/033_himss2026-dana-farber-presentation.md",
      capture="corpus/trisotech/033_himss2026-dana-farber-bpmn-preemptive-pathway.png",
      nhr=True,
      question="The deck states 'AI agents act as performers within orchestrated pathways' and shows "
               "the tag 'Agent as Performer', but its published BPMN model (slide 5) carries no AI "
               "performer marker and no AI task. Does the vendor's prose claim count as the AI "
               "element inside the process, or is a visible AI element inside the diagram required?",
      seen="overview sheet of all 19 slides + slides 5 and 17 at full size"),
 dict(slug="novel-coronavirus-covid-19-presentation", verdict="UNCERTAIN", code="", judgment=True,
      q="Prediction PMML: Predictive Model Markup Language A standard from the Data Mining Group System acts based on the PMML Prediction",
      note="Slide 11 ('COVID Decision Automation') publishes a BPMN 2.0 process - start event 'Patient "
           "under restrictions', the business-rule task 'Signs of acute respiratory infection?' "
           "(table marker), the exclusive gateway 'Symptomatic?' with the flows 'Yes, acute', 'Yes, "
           "subacute or chronic', 'No', three end events, five data objects (Do you have a Fever?, "
           "What is your temperature in degrees Centigrade?, Do you have a Cough?, Did the symptoms "
           "start in the past week?, Is there evidence of an acute respiratory infection?) with data "
           "associations - beside a DMN decision requirements diagram. The BPMN diagram itself "
           "carries no AI element: its automation is a DMN decision. The deck's AI-adjacent material "
           "is the 'Predictive' perspective ('System acts based on the PMML Prediction', PMML = "
           "Predictive Model Markup Language, a Data Mining Group standard) drawn as its own "
           "schematic, plus 'Machine Learning' named in the API-container architecture slide. Whether "
           "a PMML predictive model counts as the AI element, and whether it sits inside a process "
           "here, is a method question.",
      record="corpus/trisotech/034_novel-coronavirus-covid-19-presentation.md",
      capture="corpus/trisotech/034_novel-coronavirus-covid-19-bpmn-decision-automation.png",
      nvc=True, nhr=True,
      question="Two questions. (a) Does a PMML predictive model ('Predictive Model Markup Language', "
               "Data Mining Group) count as an AI element for this study, or only LLM/ML-model "
               "elements? (b) If it counts, does it count when the deck draws it as its own "
               "'Prediction' schematic rather than as an element inside the published BPMN process "
               "(slide 11's process is driven by a DMN decision)?",
      seen="overview sheet of all 18 slides + slides 10 and 11 at full size"),
 dict(slug="automated-guidelines-for-healthcare-reimbursement-series-part-2", verdict="UNCERTAIN", code="",
      judgment=True, q="Introducing AI",
      note="Slide 22 is titled 'Introducing AI' and shows a DMN decision requirements diagram - the "
           "decision 'Is there established evidence of efficacy?' taking the green 'Efficacy "
           "Prediction Model' decision input, with the sub-decisions 'What off label usage is "
           "planned?', 'Are there published reports of well controlled studies in peer reviewed "
           "journals?', 'Standard Reference Compendia supporting request' - beside a DMN decision "
           "table. The slide image carries the annotation 'Predictive model of the Quality of "
           "Evidence based on Machine Learning of Clinical Trials'. The same deck publishes BPMN 2.0 "
           "pathways (the preauthorization workflow pattern and the off-label request pathway) whose "
           "decision tasks invoke these DMN decisions. Whether the ML-backed decision counts as the "
           "AI element inside those BPMN processes is the open question.",
      record="corpus/trisotech/035_automated-guidelines-for-healthcare-reimbursement-series-part-2.md",
      capture="corpus/trisotech/035_automated-guidelines-part-2-introducing-ai-ml-prediction.png",
      nhr=True,
      question="Under the operator's ruling a DMN decision invoked from a BPMN business-rule task is "
               "judged on the BPMN diagram. Here the invoked decision takes an ML prediction model as "
               "input ('Efficacy Prediction Model', annotated 'Predictive model of the Quality of "
               "Evidence based on Machine Learning of Clinical Trials') while the slide that shows it "
               "is a DMN diagram. Is that an AI element inside the BPMN process?",
      seen="overview sheets of all 24 slides + slide 22 at full size"),
 # ---- E2 rows for the remaining decks judged on their slides ---------------------------------------
 dict(slug="red-hat-summit-2019-clinical-decision-support-as-a-service", verdict="EXCLUDE",
      code="E2-no-ai-element", judgment=True,
      q="Leverages AI/ML ● Complements AI / ML / Analytics solutions ○ Explainable, white-box decisions",
      note="BPMN 2.0 is published (slide 22, 'Hypothyroid Pregnancy: Sharable Clinical Pathway "
           "Model': start event 'Patient Visit', the 'First Visit?' gateway, the user tasks 'Counsel "
           "about dose follow up', 'Assess gestational age', 'Review current dose/medication', "
           "'Determine dose based on TSH value', the business-rule tasks 'Review TSH value' and "
           "'Analyze adequacy of dose', 'Order TSH', the 'TSH will not be within range' branch, the "
           "end events 'Not pregnant', 'Get order for next TSH draw', and ten data objects). The two "
           "AI mentions are dismissed: 'Leverages AI/ML / Complements AI / ML / Analytics solutions / "
           "Explainable, white-box decisions' (slide 6) refers to DMN complementing AI/ML solutions - "
           "the slide draws a data-science pipeline (documents/images, machine learning, predictive "
           "model, decision model), not a process - and 'Explainable AI Inside CDS as a Service "
           "Platform' (slide 15) refers to the platform's explainability claim, drawn as a "
           "lightbulb/platform graphic. Neither is an AI element inside the BPMN pathway.",
      seen="overview sheets of all 27 slides + slide 22 at full size"),
 dict(slug="la-gestion-des-processus-daffaires", verdict="EXCLUDE", code="E2-no-ai-element", judgment=True,
      must="Handler Agents",
      note="A 2011 French BPM training deck that publishes BPMN 2.0 teaching diagrams (the elements "
           "of BPMN, a process diagram with start/end events and a gateway, sub-processes, pools and "
           "lanes, and a worked example). Its only AI-lexicon hit is the WfMC Workflow Reference "
           "Model architecture slide: 'Enactment Engine Other Engines Wf-XML Client Worklist Tool "
           "Invoked Apps Handler Agents Apps' - 'Handler Agents' are the WfMC reference model's "
           "software handler components, nothing to do with AI, and the slide is a workflow "
           "architecture box diagram, not a process.",
      seen="published per-slide text of all 65 slides + overview sheets of all 4 sheet ranges"),
]

CAPTURES = [
 {"from": "ledgers/trisotech.raw/deckfull/bpmn-user-tasks-for-humans-and-ai-agents__s20.png",
  "to": "corpus/trisotech/027_bpmn-user-tasks-for-humans-and-ai-agents-demo4-dynamic-supervision.png"},
 {"from": "ledgers/trisotech.raw/deckfull/bpmn-user-tasks-for-humans-and-ai-agents__s23.png",
  "to": "corpus/trisotech/027_bpmn-user-tasks-for-humans-and-ai-agents-demo5-ai-performer.png"},
 {"from": "ledgers/trisotech.raw/deckfull/the-role-of-genai-presentation__s24.png",
  "to": "corpus/trisotech/028_the-role-of-genai-bpmn-prompt-management.png"},
 {"from": "ledgers/trisotech.raw/deckfull/generative-ai-and-regulatory-compliance-__s19.png",
  "to": "corpus/trisotech/029_generative-ai-and-regulatory-compliance-bpmn-term-extraction.png"},
 {"from": "ledgers/trisotech.raw/deckfull/5-min-intro-to-bpmn-presentation__s07.png",
  "to": "corpus/trisotech/030_5-min-intro-to-bpmn-bpmn-pmml-predictive-task.png"},
 {"from": "ledgers/trisotech.raw/deckfull/intelligent-assistance-for-knowledge-wor__s47.png",
  "to": "corpus/trisotech/031_intelligent-assistance-nlp-situational-lifting-bpmn.png"},
 {"from": "ledgers/trisotech.raw/deckfull/ai-driven-healthcare-orchestration-prese__s19.png",
  "to": "corpus/trisotech/032_ai-driven-healthcare-orchestration-digital-health-team-process.png"},
 {"from": "ledgers/trisotech.raw/deckfull/himss2026-dana-farber-presentation__s05.png",
  "to": "corpus/trisotech/033_himss2026-dana-farber-bpmn-preemptive-pathway.png"},
 {"from": "ledgers/trisotech.raw/deckfull/himss2026-dana-farber-presentation__s17.png",
  "to": "corpus/trisotech/033_himss2026-dana-farber-agent-as-performer-claim.png"},
 {"from": "ledgers/trisotech.raw/deckfull/novel-coronavirus-covid-19-presentation__s11.png",
  "to": "corpus/trisotech/034_novel-coronavirus-covid-19-bpmn-decision-automation.png"},
 {"from": "ledgers/trisotech.raw/deckfull/automated-guidelines-for-healthcare-reim__s22.png",
  "to": "corpus/trisotech/035_automated-guidelines-part-2-introducing-ai-ml-prediction.png"},
 {"from": "ledgers/trisotech.raw/deckfull/hl7-ai-challenge-winners-presentation__s07.png",
  "to": "corpus/trisotech/036_hl7-ai-challenge-winners-agent-as-performer-features.png"},
]


def build_rows(write):
    rows, problems = [], []
    known = D.deckinfo()
    for d in DECK:
        slug = d["slug"]
        if slug not in SCREEN or slug not in known:
            problems.append("%s: not a known deck" % slug)
            continue
        t = deck_text(slug)
        p = page_text(slug)
        hay = (p + " " + t).strip()
        if d.get("q"):
            q = norm(d["q"])
            if q not in hay:
                problems.append("%s: literal quote not found" % slug)
            ev = q
            src = "page text" if q in p else "deck per-slide text"
        else:
            ev, src = None, ""
            must = d.get("must", "")
            for tok in must.split("|"):
                if not tok:
                    continue
                for i, s in enumerate(D.trans(slug), 1):
                    c = norm(s)
                    if tok.lower() in c.lower():
                        w = window(c, tok)
                        if w:
                            ev, src = w, "deck slide %d" % i
                            break
                if ev:
                    break
        if not ev:
            # last resort: 25-word window of the page text around any AI token
            ev = " ".join(p.split()[:25]); src = "page text (fallback)"
        n = len(ev.split())
        if n > 25:
            problems.append("%s: quote is %d words" % (slug, n))
        row = {
            "key": slug,
            "verdict": d["verdict"],
            "code": d.get("code", ""),
            "judgment": d["judgment"],
            "evidence": ev,
            "note": d["note"],
            "record": d.get("record"),
            "capture": d.get("capture"),
            "needs_visual_check": bool(d.get("nvc")),
            "needs_human_ruling": bool(d.get("nhr")),
            "judged_from": VIEWED % (slug, len(D.trans(slug))) + ("; " + d["seen"] if d.get("seen") else ""),
        }
        if d.get("question"):
            row["question"] = norm(d["question"])
        if d.get("dup_of"):
            row["duplicate_of"] = d["dup_of"]
        if not d.get("code"):
            row.pop("code")
        rows.append((row, "%s  [%s%s]  evidence(%s): %s" % (
            slug, d["verdict"], " " + d["code"] if d["code"] else "", src, ev)))
    for r, line in rows:
        print(line)
    print("\nrows: %d  captures: %d" % (len(rows), len(CAPTURES)))
    for m in problems:
        print("  PROBLEM:", m)
    if write and problems:
        print("refusing to write with problems")
        return 1
    if write:
        batch = {"dispositions": [r for r, _ in rows], "captures": CAPTURES}
        out = os.path.join(RAW, "batch7.json")
        json.dump(batch, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print("wrote %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(build_rows(len(sys.argv) > 1 and sys.argv[1] == "build"))
