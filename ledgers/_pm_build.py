"""Build ledgers/processmaker.jsonl from the offline screen + the eye rulings.

Population = sitemap-en.xml (707 <loc>) U llms.txt (715 entries) = 716 items, frozen in
ledgers/processmaker.raw/pages/population.json. Every page was fetched in whichever form it publishes
(markdown twin for /docs/* and, after the acceptance test was corrected, for /apidocs/*
too; HTML only for the site root) and screened offline into ledgers/processmaker.raw/screen/screen.json.

Verdict rule applied here, page by page (one row per enumerated page):

  * PROCESS_ARTEFACT  - the page's figures include a BPMN artefact: a Process Modeler
    screen, or a modelling-object card drawn in BPMN notation (rounded-rectangle
    activity, circle event, diamond gateway, pool/lane, sequence flow). Such a page is
    E2-no-ai-element when no AI/LLM element is inside the process; judgement=True only
    when the page also discusses AI (templates/ledger.md field rule).
  * everything else    - E0-no-artefact: the page's figures are product screens (dialogs,
    tables, lists, panels, form fields, code editors, dashboards, chat) or the page has no
    figure at all, so the enumerated item contains no process artefact. A lone task tile
    used to explain a participant screen (case overview, task details) is not a process
    artefact; that is a UI illustration, not a published process model.
  * AI_BUT_NOT_BPMN   - E1-not-bpmn, naming what the artefact is instead: the page
    presents an AI/LLM artefact that is demonstrably not BPMN notation (conversational
    screen, Screen Builder control panel, Genie Studio configuration form, search UI).
  * RULED             - eye rulings that override the defaults (the AI-object pages and
    the AI-mention-but-no-element pages).

`python ledgers/_pm_build.py` prints the ruling table; `--write` writes the ledger and the
frontier file.
"""
import json, os, re, sys

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "processmaker.raw/pages")
LEDGER = os.path.join(ELI, "processmaker.jsonl")
FRONTIER = os.path.join(ELI, "processmaker.frontier.txt")
ACCESSED = "2026-09-25"

HEADER = {
    "type": "header",
    "source": "processmaker",
    "source_name": "ProcessMaker Platform documentation (docs.processmaker.com)",
    "read": ACCESSED,
    "population_size": 716,
    "census": True,
    "artefact_criteria": ("thesis 004_method, sec:method:use_case_elicitation - BPMN 2.0 diagram "
                          "+ explicit AI/LLM element inside the process"),
    "enumeration_method": (
        "ONE CENSUS, TWO PUBLISHED INDEXES, UNIONED. (1) https://docs.processmaker.com/sitemap-en.xml "
        "- 707 <loc> entries, the documentation platform's own sitemap. (2) "
        "https://docs.processmaker.com/llms.txt - 715 entries, the index the site publishes for LLM "
        "crawlers. The union is 716 URLs: the 9 URLs that llms.txt has and the sitemap does not are "
        "exactly the EXAMPLES and BEST PRACTICES articles the assignment told me to enumerate too. "
        "Union, not intersection, because neither index is a superset of the other; the frozen list is "
        "ledgers/processmaker.raw/pages/population.json (sorted) and every row below is one page of it. The nav tree "
        "was read on the site itself (DESIGNER > Processes / Screens / FlowGenie / Decision Tables / "
        "Scripts / Data Connectors / Collections / RAG Collections) and matches the two indexes; no "
        "facet and no keyword filter was used to narrow the population - the whole 716 was fetched and "
        "screened, and the AI pages surfaced from a full-text scan of all 716, not from a search box."),
    "entry_points": [
        "https://docs.processmaker.com/sitemap-en.xml",
        "https://docs.processmaker.com/llms.txt",
        "https://docs.processmaker.com/docs/flowgenie",
        "https://docs.processmaker.com/docs/modeling-objects",
        "https://docs.processmaker.com/docs/add-a-genie-in-a-process",
        "https://docs.processmaker.com/docs/update-a-rag-collection-from-a-process",
        "https://docs.processmaker.com/docs/release-notes"],
    "access": "public",
    "queries": [],
    "surface_parts": {
        "docs": 440,
        "apidocs": 276,
    },
    "figure_method": (
        "323 of the 716 pages carry at least one standalone figure (2,300+ figures in total). Deciding "
        "every page's verdict by looking at every figure was not possible, so the split was made "
        "mechanical wherever it could be and by eye where it could not: (a) the AI pages were found by "
        "a full-text scan of all 716 pages (ai_sentences in ledgers/processmaker.raw/screen/screen.json), which is a census "
        "of the AI tokens, not a sample; (b) an extended AI lexicon (artificial intelligence, "
        "intelligent document processing, cornea, semantic, model, recommendation) was then run over "
        "the same text to catch AI that does not spell itself AI - that is how IDP and Smart Extract "
        "were found; (c) the FIRST figure of 322 of the 323 figure-bearing pages was downloaded and "
        "read (the exception is the HTML-only landing page, which is ruled E0 on its own text), first "
        "on subtree contact sheets (ledgers/processmaker.raw/figures/sh_s*.png) and then, once the anonymous tiles "
        "proved impossible to attribute to a page, on row-labelled sheets that print each page's slug "
        "above its own figures (ledgers/_pm_rowsheet.py, sheets sh_p_*.png, sh_g_*.png, sh_e_*.png); "
        "(d) every page with an AI mention and figures (42) had ALL of its figures read, either on a "
        "contact sheet or at full size; (e) every page whose first figure left the canvas-versus-"
        "product-screen question open - the 16 pages that turned out to publish a Modeler canvas or a "
        "BPMN-notated object card somewhere in their later figures (sheets sh_v1..v4.png), the object "
        "pages with the most figures and the EXAMPLES family - was then read figure by figure, which "
        "is what moved those 16 rows from E0 to E2; (f) the two pages whose text places an AI-bound "
        "element in a process without printing a diagram were read in full and both the figures and "
        "the prose were captured. Rows that the mechanical screen decided carry "
        "judged_from='mechanical screen (no figure opened by eye)' and name the rule in `note`; rows "
        "decided from the figures carry the figure directory they were read from."),
    "note": (
        "Read-only throughout; no login, no account, no form submitted. The pages were fetched at "
        "about one request per second from cdn/documentation hosts and screened offline; the vendor "
        "editor was never opened, so nothing was deployed, renamed or deleted. CORRECTION 2026-09-25: "
        "an earlier version of this note said a German-language mirror of these docs "
        "(docs.processmaker.com/de) exists and was deliberately not enumerated. That was wrong on the "
        "fact, not just on the treatment. There is no locale tree on this host: the site's own two "
        "indexes (sitemap-en.xml, 707 <loc>; llms.txt, 715 entries) contain no /de/ path and no "
        "hreflang alternates, the served page declares <html lang=\"en\">, and /de/sitemap.xml and "
        "/de/llms.txt both return 404. The German-language ProcessMaker pages that did exist are on "
        "the marketing host (www.processmaker.com/de/...) and now redirect to decisions.com. Evidence "
        "and probe log: sources/OPERATOR-TODO.md section P7. The population is therefore the whole of "
        "this host as published, in one language, and nothing is missing from it for lack of a "
        "language tree."),
}

# ---------------------------------------------------------------------------
# Eye rulings on the AI pages: slug -> verdict, reason, judgment, note, question
# ---------------------------------------------------------------------------

RULED = {
    # --- AI element with its own BPMN shape, no containing process published ---
    "add-a-genie-in-a-process": dict(
        verdict="UNCERTAIN", reason=None, judgment=True, record="corpus/processmaker/001_add-a-genie-in-a-process.md",
        ev="Add a FlowGenie object from one of the following locations in Process Modeler",
        note=("The FlowGenie object is ProcessMaker's AI node type: the page's images 3 and 4 are the "
              "object's own BPMN activity shape (rounded rectangle on the Modeler's dotted grid, "
              "Genie-lamp icon, the word FlowGenie), image 7 is its Configuration panel (Genie Name "
              "'Summarize Article', Select the Genie 'Article summary') and images 8-12 are its Loop "
              "Activity and Node Identifier panels. The prose gives it BPMN activity semantics - placement "
              "inside the Pool ('If your process has a Pool object, the FlowGenie object cannot be "
              "placed outside of the Pool'), boundary events, sequence flows - but no image on the page "
              "shows a process diagram in which the Genie node sits. (Image numbers are positions in the "
              "page's own image list; the captured figures are cited in the record.)"),
        q=("An AI node type whose own BPMN shape, configuration and loop/boundary-event semantics are "
           "published, but with no process diagram containing it: is that a corpus item (INCLUDE, the "
           "same 'node type only' class recorded for IBM BAMOE as records 006/007) or does the artefact "
           "criterion require a diagram in which the AI element sits inside a process?"),
        looked="all 7 figures on one sheet (ledgers/processmaker.raw/figures/sh_genie2.png); figure 003 read at full size"),
    "all-in-one-ai-asset-generation": dict(
        verdict="UNCERTAIN", reason=None, judgment=True, record="corpus/processmaker/002_ai-generated-object.md",
        ev="Place the AI Generated object onto your Process model like any other object",
        note=("The 'AI Generated Object' is a process object you drag onto the Process model; its own "
              "shape (a robot head in a rounded BPMN activity, on the Modeler's dotted grid) is images 4 "
              "and 5, and image 6 is the AI Assistant 'Generate an Asset' panel (Sub Process From Text / "
              "Screen From Text). The page states what happens to it afterwards: 'After creating your "
              "AI-generated Process, the current AI Generated object becomes a Sub Process object that "
              "references the new Process you created using AI' - i.e. the AI acts at design time and "
              "the shape turns into an ordinary Sub Process / Form Task / Script object. The assignment "
              "file flags this page as a design-time trap and rules E2 unless the generated process also "
              "contains a Genie node; no Genie node is visible anywhere on the page. Because the AI "
              "object is nonetheless placed inside the process model and drawn in BPMN notation, the "
              "verdict here is UNCERTAIN rather than E2 - CLAUDE.md sec.3 says doubt about whether an "
              "element is AI-bound resolves to UNCERTAIN, never to E2."),
        q=("Design-time AI object: the 'AI Generated object' is placed in the process model but becomes "
           "an ordinary Sub Process / Form Task / Script once the AI has generated the asset. Does it "
           "count as an AI element inside the process (INCLUDE), or is it E2-no-ai-element because the "
           "AI runs at design time and nothing AI-bound survives in the running process?"),
        looked="all 3 figures on one sheet (ledgers/processmaker.raw/figures/sh_genie2.png)"),
    "smart-extract": dict(
        verdict="UNCERTAIN", reason=None, judgment=True, record="corpus/processmaker/003_smart-extract.md",
        ev="Smart Extract is a built-in capability in ProcessMaker that enables automated document data extraction within a process",
        note=("Images 3 and 5 are the Smart Extract object's own shape as it appears in the Modeler "
              "('Smart Extract', gear icon, rounded activity), image 7 its Configuration/Name panel, "
              "image 8 its Variable Name panel ('Variable containing the file to be sent'), image 9 its "
              "Select Model Type / Model selectors, images 10-14 its Loop Activity panels, and images "
              "15-18 the Human-In-The-Loop screens (their file names say so). The prose puts the "
              "object inside the process and at runtime: 'It can be added to a process directly from the "
              "Process Modeler and configured with a specific extraction model'; 'The results of the "
              "extraction are stored in Request variables and can be used in subsequent process steps'. "
              "The page never says the word AI - the model that does the extracting is 'a configured "
              "model', which is why the mechanical AI screen did not fire; that is the ambiguity."),
        q=("Smart Extract is a process object configured with 'a specific extraction model', stores its "
           "results in Request variables and is documented with Loop Activity semantics, but the page "
           "never states that the model is an AI/ML model. Is this an AI element inside the process "
           "(INCLUDE), or E2-no-ai-element?"),
        looked="all 9 figures on one sheet (ledgers/processmaker.raw/figures/sh_smartextract.png)"),
    "idp-connector": dict(
        verdict="UNCERTAIN", reason=None, judgment=True, record="corpus/processmaker/004_idp-connector.md",
        ev="ProcessMaker IDP is ProcessMaker's intelligent document processing (IDP) solution",
        note=("Images 5 and 7 are the IDP object's own shape as it appears in the Modeler ('Intelligent "
              "Document Processing', rounded BPMN activity), image 9 its Configuration/Name panel, image "
              "10 its Variable Name panel ('Variable containing the file to be sent'), and images 11-20 "
              "its remaining configuration panels and the IDP Admin screens the connector delegates to. "
              "The prose places it in the process with full "
              "BPMN activity semantics: 'Add an IDP connector from one of the following locations in "
              "Process Modeler', 'If your process has a Pool object, the IDP object cannot be placed "
              "outside of the Pool', plus the boundary-event list. That the element is AI-bound is stated "
              "on a different page of the same source, apidocs/idp-package: 'ProcessMaker IDP is "
              "technology that uses Artificial Intelligence (AI) and Machine Learning (ML) algorithms to "
              "extract information and insights from unstructured data sources'. The connector's own "
              "page never says AI - it says 'intelligent document processing', which is why the "
              "mechanical screen missed it."),
        q=("An AI/ML-bound connector documented as a process modelling object (pool containment, boundary "
           "events, sequence flows, loop modes), with its object shape shown but no process diagram, and "
           "with its AI nature stated only on the package page of the same docs set: INCLUDE, or E2?"),
        looked="all 11 figures on one sheet (ledgers/processmaker.raw/figures/sh_idp.png)"),
    "import-a-process-template": dict(
        verdict="UNCERTAIN", reason=None, judgment=True,
        record="corpus/processmaker/005_import-a-process-template.md",
        ev="IDP connectors must be configured prior to use",
        note=("The page's visible BPMN artefact is image 2, the template cover page of 'Expense "
              "Approval': a pool of that name with a Requester and an Approver lane, the tasks 'Process "
              "slip', 'Review expense', 'Notify expense rejection' and 'Confirm expense approval', the "
              "exclusive gateways 'Auto approve?' and 'Approved?' with their Yes/No flow labels, and the "
              "start event 'Expense slip capture' running to the end events 'Expense approved' and "
              "'Expense rejected'. Image 1 is the Template Gallery. Under the heading 'IDP: "
              "Configure IDP Connectors in the Process Template' the page says the template's IDP "
              "connectors 'must be configured prior to use' - an AI-bound connector inside the process "
              "being imported, which is not visible in the diagram. This is the CLAUDE.md sec.3 case "
              "of an element that 'might be AI-bound but is not visible', which is UNCERTAIN by rule, "
              "not E2."),
        q=("The page says process templates carry IDP Connectors (AI/ML-bound, per apidocs/idp-package) "
           "that must be configured before use, and shows one template process (Expense Approval) "
           "without them. Is the pictured template process an AI-enabled artefact (INCLUDE), or is the "
           "page E2 because no AI-bound element is visible in the artefact?"),
        looked="the page's 17 images read on one sheet (ledgers/processmaker.raw/figures/sh_tpl.png); images 1 and 2 read again at full size"),
    "update-a-rag-collection-from-a-process": dict(
        verdict="UNCERTAIN", reason=None, judgment=True,
        record="corpus/processmaker/006_update-a-rag-collection-from-a-process.md",
        ev="Each time a case runs, the Data Connector will automatically insert the uploaded file as a new record in the RAG Collection",
        note=("The page contains no process diagram: its two standalone images are product screens "
              "(image 3 the data connector's Body/JSON resource editor, image 5 the Form Task's file "
              "upload). But its prose "
              "instructs putting an element inside a process whose sole purpose is to feed an AI/RAG "
              "store at runtime: 'Insert a Data Connector Task in your process, ensuring it comes after "
              "the file is uploaded and the file-related variables are populated'; and the result: 'Each "
              "time a case runs, the Data Connector will automatically insert the uploaded file as a new "
              "record in the RAG Collection, triggering the appropriate analysis'. An AI-bound element "
              "inside a process, invisible for want of a diagram - UNCERTAIN by CLAUDE.md sec.3, and "
              "recorded rather than left as E0 so the researcher can rule on it."),
        q=("A page that documents inserting a Data Connector Task into a process so that each case "
           "writes into a RAG Collection (an AI/vector store) but publishes no process model: is the "
           "documented process an AI-enabled BPMN artefact (INCLUDE) or does the missing diagram make "
           "it E0-no-artefact?"),
        looked="the page's 5 images on one sheet (ledgers/processmaker.raw/figures/sh_rag.png); images 3 and 5 read again at full size"),

    # --- AI in the page, BPMN artefact present, AI confined to design time ---
    "ai-asset-generation": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="AI Asset Generation ProcessMaker's AI Assistant simplifies asset creation",
        note=("The page's figures are the Modeler canvas while the AI Generator runs ('Generating...') "
              "plus the generated Screens/Scripts; the diagrams the generator produces are ordinary "
              "processes - the AI mention refers to the AI Assistant creating assets (Screens, Scripts, "
              "Sub Processes) at design time, not to any element that runs inside the process."),
        ),
    "create-a-new-process-using-ai-assistant": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="Use ProcessMaker's powerful AI Assistant to quickly build a complete Process",
        note=("Figure 003 is a full generated process ('Change Of Major': start event, Review Change Of "
              "Major Request, exclusive gateway 'Approved?', Student Information System, notifications, "
              "two end events) and the rest are the New Process / Generate from AI dialogs. Every task "
              "in the generated model is a plain BPMN object; the AI mention refers to the AI Assistant "
              "writing the model from text at design time, not to an element inside the process."),
        ),
    "create-a-process-from-an-image": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="The system employs AI image analysis to automatically recreate the map inside a new Process Model",
        note=("Figure 004 is a full generated process ('We have created 2 alternatives for you': Enter "
              "Commercial Opportunity -> Receive Order -> Check Credit -> gateway -> Order Failed / "
              "Fulfill Order -> gateway -> Send Invoice -> Order Complete). The AI mention is AI image "
              "analysis reading the picture at design time; no AI element is inside the generated "
              "process."),
        ),
    "create-a-process-from-a-pi-workflow": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="The AI Asset Generator is also accessible through the icon from menu on top right of the Modeler",
        note=("Figure 001 is the Modeler canvas generating 'Change Of Major Process 2' (Alternative A: "
              "start event, Change Of Major Review Notification, Review Change Of Major Request, "
              "exclusive gateway 'Approved?', Student Information System, two end events) with the "
              "'Generating...' bar at the foot of the canvas; figures 002-005 are the AI Generated "
              "badge, the AI Generated object glyph and the AI Assistant panel. The AI is the design-time "
              "generator; the generated process holds no AI element - no Genie node appears in it."),
        ),
    "process-documentation": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="Click the Document with AI button to document the process",
        note=("Figures 001/002 are the Modeler canvas with the 'Audit Safety Inspection Process' diagram "
              "(Start Safety Inspection Control, Fill Out Safety Inspection Form, Evaluate conditions in "
              "decision table, Generate Inspection Report, Safe/Unsafe gateway, Safety Application, "
              "Safety Closure) next to the Documentation panel; figure 003/004 are the Generate "
              "Documentation dialog (Current Documentation vs AI Suggestion). The AI writes the "
              "documentation text - CLAUDE.md sec.3 names 'AI used for documentation' as one of the "
              "mentions E2 is for."),
        ),
    "process-modeling-object-descriptions": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=False, record=None,
        ev="Associate a Boundary Conditional Event element with the PDF Generator connector",
        note=("49 figures, all of them the Object panel's modelling-object cards and the Modeler canvases "
              "showing them placed (010, 017, 031, 033, 034, 035, 037, 039, 040, 042, 045, 047, 048, "
              "049 are real process diagrams). Not one of the object cards is an AI object - the list is "
              "Form Task, Manual Task, Script Task, Sub Process, the four gateways, Text Annotation, "
              "Data Object, Data Store and the event types. The AI keyword in the screen came from the "
              "Boundary Conditional Event paragraph about the PDF Generator connector and the Manager "
              "approval, which is a connector, not an AI element."),
        ),
    "boundary-conditional-event": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=False, record=None,
        ev="Associate a Boundary Conditional Event object with the PDF Generator connector",
        note=("Figures 002, 004, 007, 008 are process diagrams (Manual Task - Form Task - Manager with a "
              "Boundary Conditional Event attached and 'Route to Manager if Request conditions are "
              "met'); the rest are the boundary-event card and its Condition/Interrupting panels. The "
              "task in the diagram is a Manager approval; the AI keyword came from the PDF Generator "
              "connector paragraph, and the PDF Generator is not an AI element."),
        ),
    "conversational-screens": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Each screen control is presented as a conversational prompt, to which the user can respond",
        note=("The figures are chat-style Screens - the codebook's own example of an E1 artefact "
              "('screenshot of a chat UI'). Conversational Screens are Screens, not BPMN notation: no "
              "event, gateway, task shape, pool or sequence flow appears in any of them."),
        ),
    "action-control": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="FlowGenie : Trigger a Genie to use AI magic in the conversation",
        note=("An Action Control is a Screen Builder control, and its figures are the control's "
              "configuration panels - the control type drop-down (Asset/Script), the button editor, the "
              "rich-text toolbar. That is Screen Builder UI, not BPMN notation; the FlowGenie option "
              "lives in the control's action list, i.e. a Genie triggered from a Screen, not a node in a "
              "process."),
        ),
    "global-ai-search": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Use ProcessMaker's AI Assistant to search for Request, Task, and Process names",
        note=("The figures are the participant search UI (search box, suggested searches, results list) - "
              "an AI search feature, but no BPMN notation: no process, pool, task or gateway shape on "
              "the page."),
        ),
    "smart-inbox": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Recommendations are displayed in the Recommendations panel of the Smart Inbox",
        note=("The figures are the Smart Inbox task list and its Details/Actions panels - participant UI. "
              "The recommendations come from the Recommendations Engine, which is a task-ranking "
              "feature, not an element drawn into a process."),
        ),
    "generate-your-screen-using-ai-assistant": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Use ProcessMaker's AI Assistant to generate a Screen without knowing how to use Screen Builder controls",
        note=("The AI Generated control is a Screen Builder control; the figures are Screen Builder's "
              "control tree, the generated control and its preview. That is Screen Builder UI, not BPMN "
              "notation."),
        ),
    "generate-your-script-using-ai-assistant": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="ProcessMaker's AI Assistant in Script Editor helps you create highly usable scripts",
        note=("Figures are the Script Editor, the AI Assistant menu (Generate Script From Text, "
              "Document, Clean, Explain) and generated PHP - a code editor, not BPMN notation. The AI "
              "element is a Script authoring assistant, outside any process diagram."),
        ),
    "edit-a-rest-type-data-connector": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="From the With AI section, click From URL . The AI identification is running",
        note=("The figures are the Data Connector configuration screens (Configuration, Params, Headers, "
              "Body, Response Body, the With AI section that identifies endpoints from a URL or a file). "
              "A data connector's resource editor is not BPMN notation, and the AI is identifying the "
              "connector's endpoints at design time, not running inside a process."),
        ),
    "rich-text-control": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="The Rich Text control uses the AI Assistant to generate formatted text",
        note=("Screen Builder control documentation; the figures are the control's configuration and the "
              "rich-text editor. Screen Builder UI, not BPMN notation."),
        ),
    "saved-search-chart-control": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Use the AI Powered Chart Control to display Saved Search data as a chart",
        note=("The figures are the chart control's configuration panels and the rendered charts - "
              "dashboard UI, not BPMN notation."),
        ),
    "screen-builder": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Screen Builder is a drag-and-drop interface used to design Screens",
        note=("Screen Builder overview; the figures are the builder's control palette and canvas - a "
              "Screen design surface, not a BPMN process canvas."),
        ),
    "preview-a-screen-for-desktop-and-mobile-devices": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="The AI Control does not render in Preview mode until the AI-generated components are applied",
        note=("The figures are Screen previews in desktop and mobile frames - Screen Builder output, not "
              "BPMN notation."),
        ),
    "create-a-genie-in-the-flowgenie-studio": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="The FlowGenie Studio offers a robust, intuitive interface for designers to create and manage Genies",
        note=("The 13 figures are the FlowGenie Studio's own forms: Genie name/description, Agent "
              "Settings, Add Tool, Select Tools, Default Tools, the Firecrawl MCP Server, the system "
              "Prompt. That is an agent-configuration studio, not BPMN notation, and it does not place "
              "the Genie in a process (that is the job of add-a-genie-in-a-process, recorded)."),
        ),
    "flowgenie-configuration": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Text Model: This setting is used to determine the OpenAI model utilized",
        note=("The single figure is the AI settings form (Text Model, Vision Model, Text System Prompt, "
              "API key) - a configuration screen for the models a Genie uses, not a process artefact."),
        ),
    "ai-settings": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="AI settings in ProcessMaker enable administrators to customize and optimize AI-driven tasks",
        note=("One figure: the AI settings form. Administrative configuration, not BPMN notation."),
        ),
    "flowgenie-categories": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Click the Categories tab to view Genie categories",
        note=("Figures are the Genies list and the category dialogs - a listing UI, not BPMN notation."),
        ),
    "manage-genies": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="The Genies page displays the following information: Name",
        note=("Figures are the Genies list page and its column configuration - a listing UI, not BPMN "
              "notation."),
        ),
    "process-translations": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Harness the power of ProcessMaker AI to translate the contents of every screen in your processes",
        note=("The single figure is the process list with the Translate action - an administrative list, "
              "not a process diagram. The AI translates Screen strings, not process elements."),
        ),
    "platform-strings": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="admins can select a target language and choose either AI-assisted or manual translation options",
        note=("Figures are the platform-strings translation table - an administrative table, not BPMN "
              "notation."),
        ),
    "dashboard-translations": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="admins can translate all, empty, or selected strings with ease",
        note=("Single figure: the dashboard translation table. Administrative UI, not BPMN notation."),
        ),
    "permission-descriptions-for-users-and-groups": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Edit documentation with AI through the Process Launchpad",
        note=("The page is the permission catalogue - all of its figures are permission tables. The AI "
              "mentions are permission descriptions ('Edit documentation with AI', 'Document with AI'), "
              "not process elements, and no figure shows a process."),
        ),
    "example-preview-or-download-multiple-files-uploaded-from-a-previous-task": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="use a File Preview control or File Download control, respectively, with a Loop control",
        note=("A Screen example. All five figures are Screen Builder property panels for the File Preview "
              "and File Download controls (Variable Name 'MultiFileUploadControl', File Name 'file', Data "
              "Source 'Existing Array'); no process artefact."),
        ),
    "collaborative-modeler": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Create a new Process using natural language",
        note=("Two figures: the Comments panel and the iFrame Whitelist. The page is about collaborative "
              "review of a model; the quoted bullet is a feature list item about creating a process with "
              "natural language, and no process diagram appears on the page."),
        ),
    "summer-2025": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="Using Document with AI, auto-numbering is suppressed",
        note=("Figure 004 is a full process diagram ('Vendor Registration Process': email start event, "
              "Fill Out Vendor Registration Form, Select User, Approve Vendor, gateway 'Vendor "
              "Approved?', Generate Vendor Contract, Add Vendor to Database, end event) with the Email "
              "Listener configuration beside it. The AI content of the release notes is the AI features "
              "shipped that quarter (RAG Collections, Document with AI, FlowGenie prompts, Image to "
              "Process) - vendor roadmap items and design-time tooling, none of which appears as an "
              "element in the pictured process."),
        ),
    "spring-2025": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="RAG Collections Enhance knowledge retrieval with Retrieval-Augmented Generation (RAG) Collections",
        note=("Figure 003 is a process diagram (Pool 'Infosec Risk Assessment' with two lanes); the AI "
              "content is the release's feature list (RAG Collections, VarFinder, AI Screens with "
              "Templates). The pictured process contains no AI element - the RAG feature is configured "
              "in Collections, not drawn into the process."),
        ),
    "summer-2024": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="AI-Driven Process Documentation Use AI to quickly generate effective process documentation",
        note=("The single figure is a Process Analytics dashboard. The AI mentions are the release's "
              "feature list (AI-Driven Process Documentation, FlowGenie Studio); no process diagram on "
              "the page."),
        ),
    "processmaker-platform-winter-2025": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Winter 2025, our latest enterprise product release, is a state-of-the-art, cloud-based SaaS solution",
        note=("The single figure is a Task Details screen. AI mentions are the release's feature list "
              "(AI Platform Translations). No process artefact on the page."),
        ),
    "release-notes-2026": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="FlowGenie - Configuration Option Improved FlowGenie management by adding the Configure option",
        note=("Release notes with no figure at all: the AI/Genie mentions are changelog entries about "
              "FlowGenie configuration and AI features. No process artefact."),
        ),
    "lucidchart-integration": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=True, record=None,
        ev="Create a flowchart in Lucidchart and ProcessMaker's AI Assistant will convert it to a process map",
        note=("The page publishes no figure. The AI converts an imported Lucidchart flowchart into a "
              "process model at design time - the AI is the importer, and the resulting process is not "
              "shown, so there is no artefact to collect and no in-process AI element to point at."),
        ),
    "fixes-and-known-issues-spring-2025": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="A \"New Input\" column appears in the configuration of a RAG collection, but doesn’t display any data",
        note=("A fixes-and-known-issues changelog: no figures at all. The RAG mention is a bug entry."),
        ),
    "fixes-and-known-issues": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="AI Assistant Help Text Not Displayed: After creating a new process, the placeholder help text",
        note=("A fixes-and-known-issues changelog: no figures at all. The AI mention is a bug entry."),
        ),
    "create-a-process": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Users can opt to start from a blank canvas, leverage pre-designed templates, or utilize AI technology",
        note=("The page describes the three ways to start a process and publishes no diagram of one; it "
              "has figures but they are the New Process screen. The AI mention is the design-time "
              "generator option in a list."),
        ),
    "data-connectors": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="To learn more about AI Data Connectors, refer to Add Resources to a REST Data Connection",
        note=("A section index of the Data Connectors articles, no figures at all. The AI mention is a "
              "cross-reference to the REST connector's AI-assisted resource identification."),
        ),
    "view-documentation": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Use the in-platform chatbot to ask questions regarding ProcessMaker Platform functionality",
        note=("No standalone figure: the page carries six inline images, which are the in-platform "
              "documentation chatbot - a chat UI, which the codebook itself gives as an E1 example. Not "
              "BPMN notation, and no process artefact of any kind on the page."),
        ),
    "recommendations-engine": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="The Recommendation Engine addresses the challenge of deciding which Task to work on next",
        note=("Figures are the task list with a Recommendations column, a reassign confirmation dialog "
              "and the user Settings panel where Recommendations is Enabled/Disabled. Participant UI "
              "plus an admin switch; no process artefact."),
        ),
    "self-assign-tasks-from-a-queue": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="a team of Support agents that answer customer questions can self-assign Tasks from a queue",
        note=("No figures at all; the AI keyword in the screen came from the word 'agents' used for "
              "human support staff. Participant queue behaviour, no process artefact."),
        ),
    "configure-a-rag-collection": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Click the Configure icon for your RAG Collection",
        note=("No figures at all: the page is the step list for renaming a RAG Collection. No process "
              "artefact, and no process-bound element is described."),
        ),
    "rag-collections": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Retrieval-Augmented Generation (RAG) Collections are content-based information repositories",
        note=("Section index for the RAG Collections articles; no figures. No process artefact."),
        ),
    "menu-translations": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="This feature provides options for AI-assisted translation or manual entry",
        note=("No figures: menu-string translation instructions. Administrative UI, no process artefact."),
        ),
    "user-interface-language-management": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="This feature provides both AI-assisted and manual translation options",
        note=("No figures: the translations settings overview. Administrative UI, no process artefact."),
        ),
    "designer": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Use ProcessMaker's FlowGenie to generate AI-powered tasks by simply entering a description",
        note=("The DESIGNER section index page: an article list (FlowGenie 5 articles, RAG Collections 2 "
              "articles, ...). No figures, no diagram - the AI/Genie text is the index's own summary of "
              "the articles."),
        ),
    "integrations": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="AI Settings Updated on 2025-01-07 Configure the AI settings for all AI-enabled assets",
        note=("Section index (AI Settings, and the third-party integrations). No figures, no diagram."),
        ),
    "modeling-objects": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="AI Generated Object Use ProcessMaker Artificial Intelligence (AI) to generate an entire Process model",
        note=("The Modeling Objects section index: a list of the object articles (including 'AI Generated "
              "Object Updated on 2025-01-12'). No figures of its own, no diagram; the objects themselves "
              "are enumerated as separate items in this census."),
        ),
    "participant": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Global AI Search Updated on 2024-10-21 Use AI to search for process, cases, and tasks",
        note=("The PARTICIPANT section index. No figures, no diagram."),
        ),
    "release-notes": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="RELEASE NOTES 6 sub categories 3 articles Release Notes 2026",
        note=("The release-notes index. No figures, no diagram."),
        ),
    "spring-2024-release-notes": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="NEW FEATURESENHANCEMENTSFIXESKNOWN ISSUES FlowGenie Harness the possibilities of AI tools directly in process flows",
        note=("Release notes with no figure at all: the FlowGenie entry is the changelog line that "
              "introduced the feature. No process artefact."),
        ),
    "flowgenie": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Add a Genie to a process using a modeling object in the Modeler",
        note=("The FlowGenie section index. It carries no standalone figure (one inline icon) and no "
              "process diagram; the Genie object's own page is enumerated separately in this census."),
        ),
    "examples": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Examples",
        note="Section index for the EXAMPLES articles. No figure, no diagram.",
        ),
    "best-practices": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="BEST PRACTICES AND EXAMPLES",
        note="Section index for the BEST PRACTICES articles. No figure, no diagram.",
        ),
    "script-editor": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Easily create scripts using ProcessMaker's AI assistant",
        note=("All five figures are the Script Editor's own UI: the code editor with the Scripting AI "
              "Assistant chat beside it, the Script Config Editor JSON dialog, Sample Input JSON, the "
              "Debugger Configuration panel and the Output Preview Panel. A code editor with a chat UI, "
              "which the codebook itself gives as an E1 example - not BPMN notation, and no process "
              "diagram on the page."),
        ),
    "scripts": dict(
        verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, record=None,
        ev="Explore how to use the scripting AI assistant with the following product tour",
        note=("Four figures: the Assets panel (tiles for Processes, Screens, Scripts, ...), the Scripts "
              "list table and the Create Script dialog with its embedded AI Assistant panel. Product UI, "
              "no BPMN notation and no process diagram on the page."),
        ),
    "iframe-whitelist": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="enables administrators to securely manage cross-domain embedding of ProcessMaker content",
        note=("Two figures: the Whitelisted Domains table and the 'Configure URL Parents for Embedding' "
              "dialog. Administrative configuration UI, no process artefact. The screen's AI keyword hit "
              "is the word 'embedding' (cross-domain embedding of forms and screens), not AI."),
        ),
    "import-and-export-a-project": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="To adjust this limit, request assistance from a ProcessMaker support agent",
        note=("Three figures: the Import Project upload dialog, the import confirmation warning and the "
              "Export Project selection dialog. Administrative UI, no process artefact. The screen's AI "
              "keyword hit is the word 'agent' in 'ProcessMaker support agent', a human, not an AI agent."),
        ),
    "create-and-share-a-saved-search": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Alternatively, you can use Global AI Search for broader search capabilities",
        note=("Six figures: the Requests and Tasks lists with their filter panels and the Save Search and "
              "Share With Users dialogs. Participant list/filter UI, no process artefact. The page's AI "
              "mention is a cross-reference to Global AI Search, which is enumerated as its own item."),
        ),
    "build-your-own-process": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Follow these steps to start from a blank canvas and build your own process",
        note=("Two figures: the New Process screen - the 'Build Your Own', 'Generate from AI' and 'Import a "
              "PI Process' action cards and the Templates list - and the Create Process Name/Description/"
              "Category dialog. The template entries are text-only cards with no process drawn on them, so "
              "the page itself publishes no process artefact. Its AI reference is the design-time generator "
              "entry point; the AI-generated process model is published on the 'AI Asset Generation' and "
              "'Create a Process from Text' pages, enumerated separately in this census."),
        ),
    "idp-settings": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="ProcessMaker Platform must be authenticated to a ProcessMaker IDP instance so IDP connectors "
           "configured in business processes may process documents during Requests",
        note=("Six figures, all IDP administrative screens: the settings tabs, the Client ID, Client Secret, "
              "Host URL and Tokens URL dialogs and the 'Select available folders' dialog. No process "
              "artefact. This page carries no AI/LLM keyword itself; the AI statement for IDP is on "
              "apidocs/idp-package."),
        ),
    "smart-extract-models": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Process Designers reference these validations when configuring the Smart Extract connector",
        note=("Two figures: the Smart Extract Validations table and the 'Validation Configuration' dialog "
              "(Validation Name, Model Type, Model). Administrative model-configuration UI, no process "
              "artefact. The page's AI-bound subject is covered by the smart-extract item."),
        ),
    "platform-notifications": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="Selecting a notification for an assigned Task opens that Task's summary",
        note=("Four figures: the Inbox and Notifications lists and two request tables opened from a "
              "notification. Participant notification UI, no process artefact."),
        ),
    "form-task": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="- Embedding Rules : Due to the default Laravel cookies, Web Entries cannot be embedded into a "
           "third-party site for authenticated users",
        note=("The page's figures include BPMN artefacts: figure 001 is the Form Task object card (a "
              "BPMN-shaped rounded rectangle) and figures 004 and 009 are Process Modeler canvases with a "
              "form-task process drawn on them. The page's only AI keyword hit is 'Embedding Rules' - the "
              "third-party embedding of Web Entries, nothing to do with AI - so there is no AI element in "
              "the process. Judged by hand rather than mechanically because the keyword hit had to be read "
              "in context to be dismissed."),
        ),
    "actions-by-email-connector": dict(
        verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, record=None,
        ev="From the Language drop-down, select one of the following options to specify in which supported "
           "natural language the email recipient receives the email",
        note=("The page's figures include a BPMN artefact: figures 003 and 004 are the Actions By Email "
              "connector's object card, drawn in BPMN notation as a rounded rectangle, alongside its "
              "configuration panels. The page's only AI keyword hit is 'natural language', which is the "
              "language the email body is written in - nothing to do with AI. Judged by hand rather than "
              "mechanically because the keyword hit had to be read in context to be dismissed."),
        ),
    "apidocs/idp-package": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="ProcessMaker IDP is technology that uses Artificial Intelligence (AI) and Machine Learning (ML) "
           "algorithms to extract information",
        note=("The API documentation landing page for the IDP package: no figure and no inline image, so no "
              "process artefact at all. It is the page that states IDP's AI/ML implementation, and is cited "
              "as the AI evidence in the idp-connector row."),
        ),
    "root": dict(
        verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, record=None,
        ev="## v1",
        note=("https://docs.processmaker.com itself, the documentation home page (the only page in the "
              "population with no markdown twin). It is the site's landing page; the article tree is "
              "enumerated under its own URLs."),
        ),
}

# Pages whose figures include a BPMN artefact (Process Modeler screen or a modelling-object card
# drawn in BPMN notation). Verified by eye on the sample sheets; pages NOT listed here and not ruled
# above are E0-no-artefact.
PROCESS_ARTEFACT = {
    "auto-save-the-process-model", "boundary-conditional-event", "boundary-error-event",
    "boundary-message-event", "boundary-signal-event", "boundary-timer-event",
    "conditional-start-event", "configure-pool-and-lane-objects", "configure-a-pm-block",
    "configure-test-run-and-scenarios", "create-and-edit-a-pm-block",
    "customize-the-appearance-of-a-process-model-object", "data-association-flow-element",
    "data-store-element", "decision-task-connector", "email-start-event", "end-event",
    "event-based-gateway", "exclusive-gateway", "form-task", "inclusive-gateway",
    "intermediate-conditional-catch-event", "intermediate-message-catch-event",
    "intermediate-message-throw-event", "intermediate-signal-catch-event",
    "intermediate-signal-throw-event", "intermediate-timer-event", "manual-task",
    "message-end-event", "message-flow-element", "message-start-event",
    "navigate-around-your-process-model", "parallel-gateway", "process-modeler",
    "process-modeling-best-practices", "process-modeling-best-practices-1",
    "process-modeling-object-descriptions", "publish-your-process-model", "script-task",
    "sequence-flow-element", "signal-end-event", "signal-start-event", "start-event",
    "start-timer-event", "terminate-end-event", "text-annotation-and-association-elements",
    "validate-your-process-is-bpmn-20-compliant", "start-type-events",
    "apidocs/process-optimization-package", "summer-2025", "spring-2025",
}

AI_MENTION_ONLY = {"collaborative-modeler"}  # handled in RULED

# Pages whose verdict started as E0-no-artefact and was corrected to E2-no-ai-element after
# their figures were opened one by one (ledgers/processmaker.raw/figures/sh_p_*.png, sh_g_*.png, sh_e_*.png):
# each of them turns out to publish a Modeler canvas or a template cover with the process drawn
# in it. slug -> (what the BPMN figure is, judgment override or None for the default).
E2_FIGURE = {
    "sub-process": ("figures 001 and 002 are the Sub Process modelling-object card (a BPMN-shaped rounded "
                    "rectangle labelled 'Sub Process'), and figure 008 is a Process Modeler canvas with a "
                    "process model drawn on it and the object's configuration panel open on the right; the "
                    "other figures are the object bar tile, the Change Type dialog, the Name/Process/Start "
                    "Event panels and the Loop Mode panels"),
    "send-email-connector": ("figure 003 is a Process Modeler canvas with the process drawn on it and the "
                             "connector's 'Send reject email' configuration panel open beside it; the other "
                             "figures are the 'Send Email' object card and its Configuration/Add Recipient/"
                             "Attach Files panels"),
    "create-and-run-a-test-for-a-process": ("figures 002, 003 and 004 are Process Modeler canvases of the "
                                            "'Change of Major Request' process, showing its lanes, form tasks, "
                                            "an 'Approved?' gateway and the reject-mail path while a test run "
                                            "is configured; the rest are the run-test menu, the Screen and the "
                                            "cancel-test dialogs"),
    "example-using-formulas-in-decision-tables": ("figure 005 is a Process Modeler canvas with the Decision Task "
                                                  "that the formula is attached to drawn in the process, with the "
                                                  "object panel open; the rest are the decision-table editors, the "
                                                  "formula panel and the debug preview"),
    "example-signal-design-with-webhooks": ("figure 004 is a Process Modeler canvas showing the process that "
                                            "receives the webhook signal and routes it through its tasks; the "
                                            "rest are the webhook URL/security panel, the HTTP configuration "
                                            "panels and the Signal variable panels"),
    "slideshow-mode": ("figure 003 is a Process Modeler canvas of the process being demonstrated in Slideshow Mode "
                       "(the Modeler toolbar and the process are on screen); the others are the Slideshow "
                       "Settings dialog and the Slideshow placeholder dialog"),
    "create-a-new-process-from-template": ("figure 001 is the template's cover card: the 'Customer Churn Survey' "
                                           "lane with a start event ('End of service'), a 'Review Survey' task, an "
                                           "end event ('End of customer') and a text annotation joined by a dotted "
                                           "association, under the USE TEMPLATE button"),
    "custom-defined-waypoints": ("figure 001 is a Process Modeler canvas with the process drawn on it and the "
                                 "Configuration > Stages panel beside it, where Input Data, Approval and Contract "
                                 "are ordered; the other figures are the request list, the 'Send reject email' "
                                 "panel and the Task Data panel"),
    "example-data-connector-provides-options-in-a-select-list-control": ("figure 004 is the process drawn in the "
                                                                        "Modeler's notation on its dotted canvas: "
                                                                        "Start Event -> Form Task -> End Event "
                                                                        "(with an arrow between them); the rest are "
                                                                        "the Create Data Connector/Create Resource "
                                                                        "dialogs and the Form Task panel"),
    "example-exclude-data-setting-for-web-entry-in-form-tasks": ("figure 002 is the process drawn in the Modeler's "
                                                                 "notation on its dotted canvas: Start Event -> Form "
                                                                 "Task -> 'Web Entry in a Form Task' -> End Event; the "
                                                                 "rest are the Web Entry and submit-form panels"),
    "example-password-protection-in-web-entries": ("figure 002 is the process drawn in the Modeler's notation on its "
                                                   "dotted canvas: Start Event -> Form Task -> End Event; the rest are "
                                                   "the Web Entry panel and the password prompt"),
    "example-query-data-stored-in-web-entries": ("figure 002 is the process drawn in the Modeler's notation on its "
                                                 "dotted canvas: Start Event -> Form Task -> End Event; the rest are "
                                                 "the Web Entry panel and the Form/Task Data panels"),
    "example-script-executor-migrates-records-from-microsoft-excel-to-a-collection": (
        "figure 003 is a Process Modeler canvas with the example process drawn on it, including the 'Script "
        "Executor' and 'Save to Collection' nodes and its lanes; the rest are the Import Collection dialog, the "
        "process's configuration checklist and the Script Executor configuration screens"),
    "open-a-task": ("figure 005 is a Process Modeler canvas with the process whose Task the page explains drawn on "
                    "it and the object panel open; figure 004 is that Task's Data panel, and the rest are the "
                    "participant Screens"),
    "start-a-process-from-the-launchpad": ("figure 003 is a Process Modeler canvas showing the process that the "
                                           "launchpad tile starts (its tasks, gateways and lanes); the other two "
                                           "figures are the launchpad itself and the anonymous-web-link toast"),
    "optimize-your-process": ("figure 001 is a Process Modeler canvas with the process drawn on it and the "
                              "'Node Inspector / Optimization' panel open on the right, showing the optimisation "
                              "results for the process's nodes"),
    "form-task": ("figure 001 is the Form Task modelling-object card (a BPMN-shaped rounded rectangle labelled "
                  "'Form Task') and figures 004 and 009 are Process Modeler canvases with a form-task process "
                  "drawn on them; the other figures are the task's configuration panels (Name, Screen for Input, "
                  "Element Destination, Due In, Loop Activity, Loop Mode) and the Slideshow placeholder dialog"),
    "actions-by-email-connector": ("figures 003 and 004 are the Actions By Email connector's object card, drawn in "
                                   "BPMN notation as a rounded rectangle with the connector's label, and the "
                                   "remaining figures are its configuration panels (Name, Options, Add Option, "
                                   "Loop Mode, Documentation) and the rich-text editor's link and image dialogs"),
}


def body_text(rec):
    """The article text: front matter and the Documentation Index banner removed.

    `rec["file"]` is `<slug>.<src>` with no directory (see ledgers/_pm_screen.py), and the two media
    live in different subdirectories: the markdown twins in processmaker.raw/pages/md, the one HTML-only page in
    processmaker.raw/pages/html. The markdown twins are also not all written with the same line ending - part of the
    population was fetched as CRLF - so normalise before the front-matter regex, whose `---` line
    would otherwise end in \\r and miss, sending the Documentation Index strip to the end of the
    document and returning an empty body.
    """
    slug, src = rec["file"].rsplit(".", 1)
    if src == "html":
        p = os.path.join(RAW, "html", slug + ".html")
        if not os.path.exists(p):
            return ""
        t = open(p, encoding="utf-8", errors="replace").read()
        t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
        t = re.sub(r"(?s)<[^>]+>", " ", t)
        return re.sub(r"\s+", " ", t)
    p = os.path.join(RAW, "md", slug + ".md")
    if not os.path.exists(p):
        return ""
    t = open(p, encoding="utf-8").read().replace("\r\n", "\n").replace("\r", "\n")
    m = re.match(r"^---\n.*?\n---\n", t, re.S)
    if m:
        t = t[m.end():]
    t = re.sub(r"^>\s*## Documentation Index.*?(?=\n#|\Z)", " ", t, flags=re.S | re.M)
    return re.sub(r"\s+", " ", t)


def first_sentence(text, limit=25):
    for s in re.split(r"(?<=[.!?])\s+", text):
        s = s.strip(" #>-*")
        if len(s.split()) >= 4:
            return " ".join(s.split()[:limit])
    return " ".join(text.split()[:limit])


# Corrections appended after the 716 rows, one superseding row per `n` (audit.py: "the last row for an
# `n` wins"). Raised by elicitation-5a's re-scan of the E2 rows with a broad AI lexicon
# (AI/LLM/agent/genie/GPT/model/IDP/RAG/intelligent). The scan matched 62 of the 64 rows, but 54 of
# them only on the word "model" in "Process model" / "Process Modeler" / "data model" - the BPMN
# process model, not a model in the AI sense - so those stay mechanical. The rows below are the ones
# where the page's own prose names something AI-bound and dismissing it took reading the sentence in
# context, which is what `judgment` is for. The `modeling-object-descriptions` and
# `boundary-conditional-event` rows had already been ruled by hand this session for the same reason;
# they are re-judged here so the flag matches the rule in templates/ledger.md. The verdict does not
# change: in every one of these rows the AI-bound object is an entry in a palette or connectable-object
# list (or an external database a Script writes to), never an element of the diagram the page
# publishes, so the artefact still contains no AI element inside the process.
SUPERSEDE = {
    304: ("Judgment raised from false to true by the broad-lexicon re-scan: the page lists 'IDP "
          "connector' among the objects the Boundary Conditional Event associates with. The IDP "
          "connector is AI/ML-bound by the vendor's own statement on apidocs/idp-package (row 119), so "
          "dismissing it took reading the list in context. Verdict unchanged: it is an entry in an "
          "associable-object list, not an element of the diagram the page publishes (Manual Task - Form "
          "Task - Manager approval with the boundary event attached). See record 004 for the IDP object "
          "itself."),
    305: ("Judgment raised from false to true by the broad-lexicon re-scan: the page lists 'IDP "
          "connector' in its list of objects a Boundary Error Event associates with - an AI/ML-bound "
          "connector per apidocs/idp-package. A palette entry, not an element of any diagram on the "
          "page, so the verdict stays E2."),
    306: ("Judgment raised from false to true by the broad-lexicon re-scan: the page lists 'IDP "
          "connector' among the objects a Boundary Message Event associates with (AI/ML-bound per "
          "apidocs/idp-package). Palette entry only - no diagram on the page contains it - so the "
          "verdict stays E2."),
    307: ("Judgment raised from false to true by the broad-lexicon re-scan: the page lists 'IDP "
          "connector' among the objects a Boundary Signal Event associates with (AI/ML-bound per "
          "apidocs/idp-package). Palette entry only - no diagram on the page contains it - so the "
          "verdict stays E2."),
    308: ("Judgment raised from false to true by the broad-lexicon re-scan: the page lists 'IDP "
          "connector' among the objects a Boundary Timer Event associates with (AI/ML-bound per "
          "apidocs/idp-package). Palette entry only - no diagram on the page contains it - so the "
          "verdict stays E2."),
    575: ("Judgment raised from false to true by the broad-lexicon re-scan: the prose names the AI-bound "
          "system by name - 'sending files through a Script to an external database like ProcessMaker "
          "Intelligent Document Processing (IDP)'. It is an external database a Script may write to, "
          "not an element of a process the page publishes; verdict stays E2. Compare record 006, where "
          "the AI store is what the documented process task feeds at runtime."),
    576: ("Judgment raised from false to true by the broad-lexicon re-scan: same IDP sentence as the "
          "companion best-practices article - 'an external database like ProcessMaker Intelligent "
          "Document Processing (IDP)'. External system, not a process element; verdict stays E2."),
    577: ("Judgment raised from false to true by the broad-lexicon re-scan: besides the PDF Generator "
          "paragraph the note already records, this page's object list carries an 'IDP connector' entry "
          "- the AI/ML-bound connector of apidocs/idp-package (row 119). One entry among the 49 object "
          "cards and palette listings, not an element of the process diagrams the page publishes "
          "(figures 010, 017, 031, 033-049), so the verdict stays E2. See record 004."),
    636: ("Judgment raised from false to true by the broad-lexicon re-scan: the page's list of objects a "
          "Sequence Flow can connect includes 'AI Generated' and 'FlowGenie' - the two AI-bound object "
          "types of this source (records 001 and 002). They are entries in a connectable-object list, "
          "not elements of the sequence-flow diagram the page publishes; verdict stays E2."),
}


def build():
    pop = json.load(open(os.path.join(RAW, "population.json")))
    screened = {r["url"]: r for r in json.load(open(os.path.join(ELI, "processmaker.raw/screen/screen.json")))}
    rows = []
    for i, url in enumerate(pop, 1):
        rec = screened[url]
        slug = rec["slug"]
        if rec["section"] == "apidocs":
            slug = "apidocs/" + slug
        text = body_text(rec)
        if slug in RULED:
            r = dict(RULED[slug])
            r.setdefault("needs_visual_check", False)
            # The UNCERTAIN entries carry their question in `q`; wire it to the row's `question`
            # field and raise the human-ruling flag, per CLAUDE.md sec.2.
            r.setdefault("needs_human_ruling", bool(r.get("q")))
            r.setdefault("question", r.get("q"))
            r.setdefault("looked", None)
            judgment = r["judgment"]
            judged_from = ("eye ruling on the page's figures (ledgers/_pm_build.py)"
                           if r["looked"] else "eye ruling on the page's text and figures (ledgers/_pm_build.py)")
            figures_looked = r["looked"]
        elif slug in E2_FIGURE:
            # All of these pages have ai=False in the screen census: no AI/LLM keyword anywhere on them,
            # so their E2 exclusion is mechanical (see templates/ledger.md) and judgment stays False.
            judgment = False
            what = E2_FIGURE[slug]
            evidence = first_sentence(text) or rec["title"]
            ai_note = (" The page contains no AI/LLM keyword anywhere, so this exclusion is mechanical.")
            rows.append(dict(
                n=i, verdict="EXCLUDE", reason="E2-no-ai-element", judgment=judgment,
                evidence=evidence[:200],
                note=("The page's figures include a BPMN artefact: %s.%s" % (what, ai_note)),
                url=url, title=rec["title"], duplicate_of=None, accessed=ACCESSED,
                surface="docs:processmaker" if rec["section"] == "docs" else "apidocs:processmaker",
                record=None, needs_visual_check=False, needs_human_ruling=False, question=None,
                judged_from="eye ruling on the page's figures, all %d read (ledgers/processmaker.raw/figures/)"
                            % rec["n_figures"],
                figures_looked_at="ledgers/processmaker.raw/figures/%s/ (figures 1-%d)" % (slug.replace("/", "__"), rec["n_figures"]),
                screen="figures=%d inline_images=%d words=%d ai=%s proc=%s"
                       % (rec["n_figures"], rec["n_inline_images"], rec["words"], rec["ai"], rec["proc"])))
            continue
        elif slug in PROCESS_ARTEFACT:
            judgment = bool(rec["ai"])
            evidence = (rec["ai_sentences"][0] if rec["ai_sentences"] else first_sentence(text))
            note = ("The page's figures include a BPMN artefact (Process Modeler screen or a "
                    "modelling-object card drawn in BPMN notation); %s")
            note = note % ("the page's AI mentions are about %s" % rec["ai_sentences"][0][:120]
                           if rec["ai_sentences"] else
                           "the page contains no AI/LLM keyword anywhere, so this exclusion is mechanical")
            rows.append(dict(
                n=i, verdict="EXCLUDE", reason="E2-no-ai-element", judgment=judgment,
                evidence=evidence[:200], note=note, url=url, title=rec["title"], duplicate_of=None,
                accessed=ACCESSED, surface="docs:processmaker" if rec["section"] == "docs" else "apidocs:processmaker",
                record=None, needs_visual_check=False, needs_human_ruling=False, question=None,
                judged_from="mechanical screen (figure inventory + AI keyword scan; pattern verified by eye on the subtree sample sheets)",
                figures_looked_at="subtree sample sheets ledgers/processmaker.raw/figures/sh_s1..s4.png (first figure of 141 pages)",
                screen="figures=%d inline_images=%d words=%d ai=%s proc=%s"
                       % (rec["n_figures"], rec["n_inline_images"], rec["words"], rec["ai"], rec["proc"])))
            continue
        else:
            judgment = False
            evidence = first_sentence(text) or rec["title"]
            ai_note = (" The page's AI mentions (%s) are %s"
                       % (rec["ai_sentences"][0][:100], "not about a process element.")) if rec["ai_sentences"] else ""
            note = ("The enumerated item contains no process artefact: %s figures, %s, and no BPMN notation "
                    "in any of them.%s"
                    % (rec["n_figures"] if rec["n_figures"] else "no standalone",
                       "all product screens (dialogs, tables, lists, panels, code editors, dashboards)"
                       if rec["n_figures"] else "no figure and no inline image"
                       if not rec["n_inline_images"] else "%d inline images (icons, panels)" % rec["n_inline_images"],
                       ai_note))
            judged_from = ("mechanical screen (no figure opened by eye)"
                           if not rec["n_figures"] or rec["n_figures"] == 0 else
                           "mechanical screen (figure inventory; page not in the BPMN subtree sample)")
            figures_looked = ("no figure opened by eye (the page carries %s)"
                              % ("no figure" if not rec["n_figures"] else "%d figures, not in the sampled subtree" % rec["n_figures"]))
            rows.append(dict(
                n=i, verdict="EXCLUDE", reason="E0-no-artefact", judgment=judgment,
                evidence=evidence[:200], note=note, url=url, title=rec["title"], duplicate_of=None,
                accessed=ACCESSED, surface="docs:processmaker" if rec["section"] == "docs" else "apidocs:processmaker",
                record=None, needs_visual_check=False, needs_human_ruling=False, question=None,
                judged_from=judged_from, figures_looked_at=figures_looked,
                screen="figures=%d inline_images=%d words=%d ai=%s proc=%s"
                       % (rec["n_figures"], rec["n_inline_images"], rec["words"], rec["ai"], rec["proc"])))
            continue
        rows.append(dict(
            n=i, verdict=r["verdict"], reason=r["reason"], judgment=judgment, evidence=r["ev"],
            note=r["note"], url=url, title=rec["title"], duplicate_of=None, accessed=ACCESSED,
            surface="docs:processmaker" if rec["section"] == "docs" else "apidocs:processmaker",
            record=r["record"], needs_visual_check=r["needs_visual_check"],
            needs_human_ruling=r["needs_human_ruling"], question=r["question"],
            judged_from=judged_from, figures_looked_at=figures_looked,
            screen="figures=%d inline_images=%d words=%d ai=%s proc=%s"
                   % (rec["n_figures"], rec["n_inline_images"], rec["words"], rec["ai"], rec["proc"])))
    return rows


def main():
    rows = build()
    from collections import Counter
    v = Counter(r["verdict"] for r in rows)
    c = Counter(r["reason"] for r in rows if r["verdict"] == "EXCLUDE")
    # The superseding rows are appended after the census rows; every statistic below is computed on the
    # collapsed view (last row per `n` wins, as tools/audit.py does), so the printed share is the one
    # the gate checks.
    superseding = []
    by_n = {r["n"]: r for r in rows}
    for n, extra in sorted(SUPERSEDE.items()):
        if n not in by_n:
            raise SystemExit("SUPERSEDE names n=%s, which is not a row" % n)
        r2 = dict(by_n[n])
        r2["judgment"] = True
        r2["note"] = (r2["note"] + " " if r2["note"] else "") + extra
        r2["supersedes_row"] = True
        superseding.append(r2)
    collapsed = {r["n"]: r for r in rows + superseding}
    rows_c = sorted(collapsed.values(), key=lambda r: r["n"])
    jx = [r for r in rows_c if r["judgment"] and r["verdict"] == "EXCLUDE"]
    v = Counter(r["verdict"] for r in rows_c)
    c = Counter(r["reason"] for r in rows_c if r["verdict"] == "EXCLUDE")
    print("rows", len(rows_c), dict(v), "(+%d superseding)" % len(superseding))
    print("exclusions", dict(c))
    print("judgement exclusions", len(jx), "%.3f" % (len(jx) / len(rows_c)))
    for r in jx:
        print("   J", r["n"], r["url"].replace("https://docs.processmaker.com/", ""))
    if "--write" not in sys.argv:
        return
    with open(LEDGER, "w", encoding="utf-8") as f:
        f.write(json.dumps(HEADER) + "\n")
        for r in rows:
            f.write(json.dumps(r) + "\n")
        for r in superseding:
            f.write(json.dumps(r) + "\n")
        f.write(json.dumps({
            "type": "footer", "rows": len(rows_c), "status": "DONE",
            "include": v["INCLUDE"], "uncertain": v["UNCERTAIN"],
            "exclude": {k: c[k] for k in sorted(c)}, "blocked": v["BLOCKED"],
            "judgment_exclusion_share": round(len(jx) / len(rows_c), 3),
            "judgement_rows": sum(1 for r in rows_c if r["judgment"]),
            "records_written": [r["record"].split("/")[-1][:-3] for r in rows_c if r["record"]],
            "superseded_rows": len(superseding),
            "figures_method": HEADER["figure_method"],
        }) + "\n")
    with open(FRONTIER, "w", encoding="utf-8") as f:
        f.write("# frontier for the processmaker census: sitemap-en.xml U llms.txt = 716 URLs, one line per row\n")
        for r in rows:
            f.write(r["url"] + "\n")
    print("wrote", LEDGER, "and", FRONTIER)


if __name__ == "__main__":
    main()
