"""Emit the flowx-ai ledger: one row per page of the frozen 945-URL population, plus records + captures.

Inputs (all offline, all written by the earlier passes in this folder):
  flowx-ai.raw/population.json   the frozen population (sitemap.xml U llms.txt U the _llms indexes)
  flowx-ai.raw/pages/*.md        each page's own published markdown twin
  flowx-ai.raw/pages_llmsfull/   the same markdown for the pages supplied by the llms-full.txt bundle
  flowx-ai.raw/screen.json       per-page title, surface, figure list, AI sentences
  flowx-ai.raw/figmeta.json      per-URL {alt,name,url} for every figure
  flowx-ai.raw/fences.json       per-URL (n_mermaid, n_ascii_sketch), tightened detector
  flowx-ai.raw/mirror.json       URL -> byte-identical twins under another version path
  flowx-ai.raw/classify.json     the dry-run classifier's per-page facts

THE VERDICT RULES THIS IMPLEMENTS (all of them mechanical except where marked HAND):
  artefact = the page publishes a standalone figure, a diagram fence (Mermaid, or a plain fence
             carrying box-drawing characters / arrow-node syntax) or a linked .bpmn model.
  1. no artefact                                    -> E0-no-artefact        (mechanical)
  2. artefact, no BPMN-notation artefact on page     -> E1-not-bpmn           (mechanical;
     the note names what the artefact is instead)
  3. artefact, a BPMN-notation figure on the page    -> E2-no-ai-element      (mechanical on pages
     with no AI term; HAND on the 15 pages that do discuss AI - each dismissal is quoted in E2_NOTES)
  4. the same diagram already recorded               -> E3-duplicate          (mechanical, needs
     duplicate_of; only the 5.1 twin of record 002 qualifies: identical 618-char diagram fence)
  5. HAND: pages that place an AI element in or on a BPMN process element -> UNCERTAIN + a record.
     Every one of them is listed in RULINGS below with its own evidence and its own question for the
     researcher. UNCERTAIN is handled downstream exactly like INCLUDE, and each carries the exact
     question the researcher has to answer.
A page whose prose binds an AI element to a BPMN node but which publishes no artefact is NOT silently
dropped: it gets an E0/E1 row whose note quotes the binding verbatim, so the researcher sees it.

Run:  python ledgers/_fx_build.py --dry     bucket table + quotes that fail the verbatim check
      python ledgers/_fx_build.py           writes ledgers/flowx-ai.jsonl, .frontier.txt, corpus/flowx-ai/
"""
import json, os, re, sys, unicodedata

ELI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(ELI)
RAW = os.path.join(ELI, "flowx-ai.raw")
PAGES = os.path.join(RAW, "pages")
FALLBACK = os.path.join(RAW, "pages_llmsfull")
CORPUS = os.path.join(ROOT, "corpus", "flowx-ai")
ACCESSED = "2026-09-25"
BROWSER = "chrome-devtools-mcp (cdp1), own tab only"

# --------------------------------------------------------------------------------------------------
# Hand rulings: the pages that put an AI element in or on a BPMN process element. Number = record.
# --------------------------------------------------------------------------------------------------
RULINGS = [
    dict(
        n="001", slug="document-processing",
        url="https://docs.flowx.ai/5.9/ai-platform/tutorials/document-processing",
        kind="mermaid-process",
        question='Does the corpus require BPMN 2.0 notation, or does a process this source publishes as a Mermaid flowchart whose node labels are BPMN element names (User Task, Send/Receive Message Task, Exclusive Gateway, End Event) with the AI steps bound into it as workflow calls count as a BPMN process with an AI element inside it?',
        prefer=[r"classifyAndExtract|Document Understanding|Text Understanding|Text Generation",
                r"BPMN process|Receive Message Task|Service Task|Exclusive Gateway|End Event",
                r"AI reconciliation|LLM|agent"],
        bpmn_evidence="""\
The process itself is published twice on this page: as a Mermaid flowchart whose node labels are BPMN
element names, and as prose steps that name the nodes.
  "```mermaid theme={\"dark\"} flowchart TD A[\"User uploads documents\"] --> B[\"User Task<br/>(file
  upload UI)\"] B --> C[\"Send / Receive Message Task\"] C -. \"Workflow: classifyAndExtract<br/>(per
  document)\" .-> C C --> D[\"Send / Receive Message Task\"] D -. ..."
The prose in Step 4, "Build the BPMN process", names the same nodes and adds: "Add a Receive Message
Task node to capture the extraction output. In the node's Data Stream, set the Key Name to
extraction.classifiedDocs", "Add a Service Task with a Business Rule action (JavaScript)", "Add an
Exclusive Gateway after the business rule", "Add an End Event after the summary is received". Step 5
ties the UI to the BPMN task: "A User Task's UI lives on the node - a standalone UI Flow cannot be
attached to a BPMN task."
The page's three figures are node-configuration panels (dp-01 Document Extraction node configuration,
dp-02 Extract Data from File, dp-03 File Upload response key). No Process Designer canvas figure. The
process is therefore rendered as Mermaid, not in BPMN 2.0 notation.""",
        ai_evidence="""\
The AI elements are the workflow calls wired into the process's Send/Receive Message Task pairs. The
page's own workflow table names them: "classifyAndExtract | Document Understanding + Document
Extraction | Classify document type, then extract fields using type-specific prompts",
"reconcileData | Text Understanding | Compare extracted fields against application data",
"generateSummary | Text Generation | Produce a human-re...". The BPMN step keeps the same binding:
"the two Send/Receive pairs that call classifyAndExtract and reconcileData collapse into one pair that
calls verifyDocuments per document", and the business rule is there to "supplement the AI
reconciliation ... to catch issues the LLM might miss"."""),
    dict(
        n="002", slug="passing-data-between-nodes",
        url="https://docs.flowx.ai/5.9/docs/building-blocks/process/passing-data-between-nodes",
        kind="ascii-process",
        question='The artefact is an ASCII box-and-arrow diagram of a BPMN process with "AI agent" as one of its four node kinds (and the page binds that node to a Service Task with the agent integration). Is an ASCII sketch a collectable process artefact, or does the criterion require BPMN 2.0 notation?',
        prefer=[r"Inside a BPMN process|AI agent|Service Task|Receive Message Task|Send Message Task",
                r"Call an AI agent|AI ops|For AI agents"],
        bpmn_evidence="""\
The page publishes the process as an ASCII box-and-arrow sketch whose boxes are BPMN/process element
names, under the heading "The mental model" - a shared store read from and written to by four node
kinds:
       Process variables (shared store)
              ^                ^                ^              ^
              | output         | output         | output       | read
        | Subprocess|    | Workflow  |    | AI agent  |  | User task |
and the sentence above it names the same set as nodes of a BPMN process: "Inside a BPMN process, every
node, including subprocess, integration workflow, AI agent, business rule, and user task, reads from
and writes to a shared store of process variables". The page also names the BPMN nodes that do the
waiting: "place a Receive Message Task after the Send Message Task that triggers the workflow", and
"Any node after the Receive Message Task, including gateway, business rule, and user task, can read the
result key". No figure and no .bpmn model: the artefact is the ASCII sketch.""",
        ai_evidence="""\
"AI agent" is one of the four node kinds in that sketch, and the page's own pattern table binds it to a
BPMN node type: "Call an AI agent (extraction, decision, generation) | Service Task with the agent
integration | Mapped back to process variables in the action's output mapping". A Note repeats it:
"For AI agents: the integration is typically wired on a Service Task, and the agent's response is
mapped back to process variables in the action's output mapping. No separate Receive Message Ta...".
The same page files "AI ops" under the workflow-call row: "Call an integration workflow (REST, DB, AI
ops) and capture the result"."""),
    dict(
        n="003", slug="start-integration-workflow",
        url="https://docs.flowx.ai/5.9/docs/building-blocks/actions/start-integration-workflow",
        kind="prose-binding",
        question='This page publishes no artefact at all - no figure, no diagram - and its AI-in-BPMN evidence is prose and a table ("available on Send Message Task, Task, and User Task nodes within BPMN processes"; "Execute AI operations (extraction, generation)"). Is a documented binding of an AI action to named BPMN node types collectable without a diagram?',
        prefer=[r"Send Message Task|User Task|BPMN process|Receive Message Task",
                r"AI operations|workflow executes|Triggering workflows"],
        bpmn_evidence="""\
No figure and no diagram on the page: the binding is published as prose and as a table. The Info box
names the BPMN node types the action sits on: "The Start Integration Workflow action is available on
Send Message Task, Task, and User Task nodes within BPMN processes." The Steps describe the node-level
mechanics: "The input data mapped in the action configuration is sent as start variables to the
workflow", "The BPMN process continues to the next node after the workflow completes", and the Warning
"The process waits for the workflow to complete before continuing. To receive output data, you must add
a Receive Message Task node after the Send Message Task that triggers the workflow."
What is missing is a published process artefact: nothing on this page shows a process diagram.""",
        ai_evidence="""\
The action is the documented route by which AI work reaches a BPMN node. The "When to use" table lists
"Execute AI operations (extraction, generation) | Start Integration Workflow", and the workflow is
described as "executing its configured nodes (REST calls, data transformations, AI operations,
etc.)". Its sibling page in this source states the agent case outright ("Call an AI agent ... | Service
Task with the agent integration"), and this page is the action that page links to."""),
    dict(
        n="004", slug="bpmn-integration",
        url="https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration",
        kind="ascii-process",
        question="The source's own doctrine page for agents in BPMN: three ASCII arrow sketches whose nodes are BPMN elements (Service Task, gateway) with the agent calls in them, plus prose binding AI to gateways and boundary error events. Collectable as an artefact, or is it a documentation page about a pattern rather than a process?",
        prefer=[r"Service Task|BPMN node|gateway|BPMN process|boundary error events",
                r"AI agent|AI-powered|Agent returns|extraction agent"],
        bpmn_evidence="""\
The page is the source's own doctrine for putting agents into a BPMN process, published as three ASCII
arrow sketches whose nodes are BPMN elements:
  "User uploads document → Service Task calls extraction agent → Agent returns structured data →
   Process continues with data"
  "Process reaches gateway → Service Task calls decision agent → Agent returns recommendation →
   Gateway routes based on result"
  "Process collects data → Service Task calls generation agent → Agent produces content →
   Content stored/sent"
The steps name the BPMN nodes: "Add a Service Task node to your process where you want to trigger the
agent." The page also binds AI to gateways and to boundary events: "Make AI-powered decisions at
process gateways", "Route to manual review if confidence is low", and the Error handling section
("Use boundary error events to catch agent failures"). No figure, no .bpmn model, and no BPMN 2.0
notation: the artefacts are ASCII sketches.""",
        ai_evidence="""\
"Integrate AI agents directly into your BPMN processes to automate document processing, make
intelligent decisions, and generate content without user interaction." The four capabilities listed
are the AI elements: "Automate document processing in the background", "Make AI-powered decisions at
process gateways", "Generate content automatically within workflows", "Validate data using AI
analysis". Two integration methods are documented: the Start Integration Workflow action on a Service
Task, and the Custom Agent Node in Integration Designer for "Multi-step AI workflows"."""),
    dict(
        n="005", slug="custom-agent-node",
        url="https://docs.flowx.ai/5.9/docs/platform-deep-dive/integrations/custom-agent-node",
        kind="ui-canvas",
        question='The AI element (the Custom Agent node) is documented and pictured inside the vendor\'s Integration Designer canvas, which this source\'s own glossary calls "Not a BPMN process"; the only BPMN claim is one sentence saying BPMN processes invoke such workflows through the Start Integration Workflow action. Collectable, or is this an AI node in a workflow (a different artefact class)?',
        prefer=[r"Custom Agent|BPMN|Start Integration Workflow|responseKey|agent's response"],
        bpmn_evidence="""\
The page's 11 figures are screenshots of the Custom Agent node inside the vendor's Integration Designer
canvas - a canvas this source's own glossary says is 'Not a BPMN process': ca1 "Custom Agent Node",
ca2 "Add Custom Agent", ca3 "Custom Agent AI Config", ca4 "Agent Tools Tab", ca-add-tool-menu "The Add
tool menu on the Custom Agent node, offering MCP Server, Workflow, Function, Web Search, and
Built-in ...", ca5 "Agent Node Logs". The BPMN link is one sentence, under Related resources: "For
BPMN process workflows, use the Start Integration Workflow action to invoke workflows that contain
Custom Agent nodes."
So the AI element is documented and pictured, but inside a workflow canvas, not inside a BPMN diagram;
the only BPMN-specific claim is that BPMN processes invoke it through the action documented in record
003.""",
        ai_evidence="""\
The node is an LLM agent: "Select Custom Agent from the available node types", its response is written
to process data ("responseKey ... The key in the process data where the agent's response will be
stored"), it is configured with Instructions/Context, MCP servers, knowledge-base retrieval and
workflow tools, and it can "state its reasoning before it answers". The tool menu its own figure shows
is "MCP Server, Workflow, Function, Web Search, and Built-in Tools"."""),
    dict(
        n="006", slug="agent-typologies",
        url="https://docs.flowx.ai/5.9/ai-platform/patterns/agent-typologies",
        kind="prose-binding",
        question='Ten agent patterns as prose; no artefact on the page. One of them states the process binding in words: "the surrounding BPMN process presents it to a person as a User Task - the agent workflow and the human step share the same process context." Collectable without a diagram?',
        prefer=[r"BPMN process|User Task|Condition node|agent workflow|AI node types"],
        bpmn_evidence="""\
No artefact on the page at all (0 figures, 0 diagram fences, no .bpmn model): ten agent patterns as
prose, each with a "How to build it" paragraph. One of them publishes the process binding in words:
"How to build it: a Condition node detects the escalation case, and the surrounding BPMN process
presents it to a person as a User Task - the agent workflow and the human step share the same process
context." The page points at the node palette instead of drawing anything: "The implementations below
use the nodes as they exist in the platform - see AI node types for the full palette.\"""",
        ai_evidence="""\
The AI elements are the ten typologies themselves (Document extractor and validator, Grounded
generator, Classifier and router, Voice intake, Predictive scorer, Privacy-guarded extractor,
Knowledge-validated extractor, Relationship reasoner, Human handoff) and the node palette they are
built from. The page's closing pointer is "Integrating agents in BPMN processes"."""),
    dict(
        n="007", slug="roles-permissions-matrix",
        url="https://docs.flowx.ai/5.1/setup-guides/access-management/roles-permissions-matrix",
        kind="prose-binding",
        question='A permissions matrix is the whole page and the only artefact-like content is one row: the aiagent_edit permission "Controls visibility of config-time agents (AI Assistant, Analyst, Designer, Developer), the AI floating action button, the Chat UI component, and AI actions on BPMN nodes." This is the only place in the population where "AI actions on BPMN nodes" appears, and it publishes no diagram: collectable, or E0?',
        prefer=[r"aiagent_edit|AI actions on BPMN nodes|AI floating action button|AI agents"],
        bpmn_evidence="""\
No artefact on the page (0 figures, 0 diagram fences): it is a permissions matrix, and the only
process-relevant content is one row's description, which names AI actions attached to BPMN nodes:
"Gated by the `aiagent_edit` permission. Controls visibility of config-time agents (AI Assistant,
Analyst, Designer, Developer), the AI floating action button, the Chat UI component, and AI actions on
BPMN nodes."
This is the only place in the whole 945-page population where the phrase "AI actions on BPMN nodes"
appears; the 5.9 version of the same page replaced that row with three "AI agents" rows and no longer
carries it.""",
        ai_evidence="""\
The AI surfaces the permission gates are named in the same row: "config-time agents (AI Assistant,
Analyst, Designer, Developer), the AI floating action button, the Chat UI component, and AI actions on
BPMN nodes". Three further rows gate "AI providers", "AI models" and "AI agents" per role."""),
]

# --------------------------------------------------------------------------------------------------
# HAND: the 15 pages that publish a BPMN-notation figure AND discuss AI. Each E2 row must quote the AI
# mention it is dismissing and say what that mention refers to instead. Keyed by URL suffix so the
# version twins of one page share one ruling.
# --------------------------------------------------------------------------------------------------
E2_NOTES = {
    "4.7.x/docs/building-blocks/process/process":
        "The page's BPMN artefacts are the Process Designer figures (process_designer_411.png, prs_def.png) - "
        "the Designer's process view and palette. Its only AI-term hit is the ordinary verb: \"Triggering the "
        "submission action prompts the appearance of a modal window, inviting you to provide a commit message "
        "for context.\" The other hit is the site's boilerplate index link (docs.flowx.ai/llms.txt), not prose. "
        "No element inside the pictured process is AI-bound.",
    "docs/building-blocks/process/process":
        "The page's BPMN artefacts are the Process Designer figures (process_designer_411.png, prs_def.png) - "
        "the Designer's process view and palette. Once the vendor's own name (FlowX.AI, which stands on every "
        "page of this site) is stripped, the page carries no AI/LLM term at all: its earlier screen hit was "
        "only that vendor name. No element inside the pictured process is AI-bound.",
    "docs/flowx-designer/managing-a-project-flow/starting-a-process":
        "The page's BPMN artefact is start_timer_process.png, a Process Designer canvas with a timer start "
        "event. Its only AI-term hit is the ordinary verb: \"you’ll be prompted to enter a JSON payload\" "
        "(the Designer UI asking for start parameters, in the page's JSON Object editor step). No element "
        "inside the pictured process is AI-bound.",
    "docs/flowx-designer/overview":
        "The page's BPMN artefacts are prs_def.png and designer_active_process.png, Process Designer views. Its "
        "AI mention is a card about a design-time helper: \"AI Assistance ... Accelerate development with "
        "AI-powered suggestions, optimization recommendations, and contextual help.\" That is the design-time "
        "assistant in the Builder UI, not an element inside the process in the figures.",
    # 4.7.x: the page names no AI feature at all; its single lexicon hit is the ordinary noun "retrieval".
    # (The 5.1 and 5.9 twins of this same URL do carry the AI-nodes section - entries below.)
    "4.7.x/docs/platform-deep-dive/integrations/integration-designer":
        "The page's BPMN artefact is bpmn_airtable.png, a Process Designer canvas read by eye "
        "(ledgers/flowx-ai.raw/figures/url/001_bpmn_airtable.png): pool 'Default', start event Start_001, "
        "user task 'add new entry', receive-message task 'receive workflow output data', end event End_001, "
        "sequence flows - no AI element inside it. The 4.7.x page names no AI feature anywhere and publishes "
        "no AI node palette figure: its only AI/LLM-lexicon hit is the ordinary noun \"data retrieval\" "
        "(\"confirmation of resource creation, or data retrieval\").",
    "docs/platform-deep-dive/integrations/integration-designer":
        "The page's BPMN artefact is bpmn_airtable.png, a Process Designer canvas read by eye "
        "(ledgers/flowx-ai.raw/figures/url/001_bpmn_airtable.png): pool 'Default', start event, user task "
        "'add new entry', receive-message task 'receive workflow output data', end event - no AI element "
        "inside it. The page's AI mentions describe Integration Designer *workflow* nodes, not BPMN elements: "
        "\"Enable AI agents to use MCP tools for intelligent task automation\" (its Custom Agent node "
        "section), plus the AI node palette figure ai_nodes.png (alt \"AI Nodes\"). This source's own "
        "glossary defines that canvas as 'Not a BPMN process'.",
    "docs/building-blocks/process/process-definition":
        "The page's BPMN artefact is delete_process.png, a Process Designer view. Its AI-term hits are UI "
        "Designer features, not process elements: \"Get intelligent suggestions in UI Designer based on "
        "defined keys\" (the data model's Auto-completion benefit, in a bulleted list) and \"Generate "
        "automatic input prompts for testing\" (on the process definition's test-start option).",
    "docs/building-blocks/project-data-model":
        "The page's BPMN artefact is pdm_process.png (the data model mapped onto the process). Its AI mentions "
        "are advice about documenting data for agents - \"Add descriptions to data types and attributes for "
        "better understanding and for AI agents\" - and the related-topics links to the AI Developer, AI "
        "Architect and AI Designer pages. Neither is an element inside the process in the figure.",
    "docs/platform-deep-dive/integrations/email-trigger":
        "The page's BPMN artefact is trigger_email_trigger_type_process.png, the Process Designer's trigger "
        "panel. Its AI-term hit is an error-table label, not an element: the trigger-error table's column "
        "value \"Failure classification\". No AI element inside the pictured process.",
    "docs/building-blocks/actions/append-params-to-parent-process":
        "The page's figures are Process Designer node-panel screenshots (append_param_1.png shows Service_Task_001's "
        "Actions tab in process AppendParamsTest_Sub), not the process canvas. Its AI mention places LLM agents "
        "in a subprocess only as an example of a long-running call: \"The subprocess is long-running (LLM agents, "
        "slow integrations, batch jobs) and you want fire-and-forget execution while the user continues in the "
        "UI.\" Nothing AI-bound is shown inside a process.",
    "docs/platform-overview/flowx-architecture":
        "The page's artefact is flowx-architecture-5.9.svg, a platform architecture box diagram (services, "
        "ports, pods) - not a process. Its AI mentions are microservice names: \"The AI Gateway powers the AI "
        "chat experience in the FlowX Designer\", \"routing requests to the config-time agents\". Infrastructure, "
        "not a process element.",
    "docs/platform-overview/data-architecture":
        "No figure at all on this page; it is prose about stores. Its AI mention is infrastructure: \"PostgreSQL "
        "Service state for AI components - embedding-job tracking, document-enrichment artifacts, and "
        "conversation, thread, and message history for the AI gateway.\" Nothing process-bound.",
}


def ruling_for(url):
    for r in RULINGS:
        if r["url"] == url:
            return r
    return None


# --------------------------------------------------------------------------------------------------
# page access + text helpers
# --------------------------------------------------------------------------------------------------
def page_path(url):
    slug = re.sub(r"^https://docs\.flowx\.ai", "", url).strip("/").replace("/", "__") or "root"
    for d in (PAGES, FALLBACK):
        p = os.path.join(d, slug + ".md")
        if os.path.exists(p):
            return p
    return None


def raw_body(url):
    p = page_path(url)
    if p is None:
        return None
    t = open(p, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
    return re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)


def prose(url):
    """The page's own prose with markup stripped: what a verbatim quote is checked against."""
    t = raw_body(url) or ""
    t = re.sub(r"^>\s*## Documentation Index.*?(?=\n#|\Z)", " ", t, flags=re.S | re.M)
    t = re.sub(r"!\[[^\]]*\]\([^\)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[`*>#]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def verbatim_text(url):
    """The raw page text, whitespace-normalised, boilerplate index block removed: what a quote must
    appear in verbatim. Deliberately NOT markup-stripped - a quote is allowed to carry the page's own
    markdown, and stripping markers here would make quotes that carry them look fabricated."""
    t = re.sub(r"^>\s*## Documentation Index.*?(?=\n#|\Z)", " ", raw_body(url) or "", flags=re.S | re.M)
    return re.sub(r"\s+", " ", t).strip()


def sentences(url, keep_pipes=True):
    out = []
    for chunk in (raw_body(url) or "").split("\n"):
        chunk = chunk.strip()
        if not chunk or chunk.startswith(">") or chunk.startswith("<"):
            continue
        for s in re.split(r"(?<=[.!?])\s+", chunk):
            s = re.sub(r"\s+", " ", s).strip()
            if not s:
                continue
            if not keep_pipes:
                s = s.strip("|").strip()
            out.append(s)
    return out


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def qnorm(s):
    """Whitespace plus typography: the only differences a quote is allowed to have from the page it
    was copied out of (the site mixes curly and straight quotes, and NFKC folds the rest)."""
    s = unicodedata.normalize("NFKC", s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


QSPAN = re.compile(r'"([^"]{6,})"')


def span_check(row, vt):
    """The census's quoting convention, enforced: a DOUBLE-quoted span in a row's evidence or note is
    a verbatim quotation from the page that row judges, and must be findable in that page's own
    published markdown; a SINGLE-quoted span is a quotation from another named source (the site's
    glossary, a label read in a figure), and the note must name that source in the same sentence.
    An elided span ('a ... b') is checked piece by piece."""
    out = []
    for field in ("evidence", "note"):
        for span in QSPAN.findall(row.get(field) or ""):
            for piece in re.split(r"\s*\.\.\.\s*", span):
                piece = piece.strip()
                if piece and qnorm(piece).rstrip(" .") not in vt:
                    out.append("%s: %r" % (field, piece))
    return out


def wc(s):
    return len(s.split())


def cut(s, n=25):
    w = s.split()
    return " ".join(w[:n]) + (" ..." if len(w) > n else "")


def pick_quote(url, prefer=None, maxw=25, keep_pipes=True):
    ss = sentences(url, keep_pipes=keep_pipes)
    pool = [s for s in ss if len(re.sub(r"[^A-Za-z]", "", s)) >= 12]
    # A quote that opens with a markdown marker ("- ", "* ", "# ", "> ") reads as a fragment, so the
    # prose sentences are preferred; the marked-up ones stay as the fallback for pages that have none.
    plain = [s for s in pool if not s[:2].lstrip().startswith(("-", "*", "#", ">", "|", "["))]
    for cand in (plain, pool):
        if prefer:
            for s in cand:
                if prefer.search(s) and 5 <= wc(s) <= maxw:
                    return s
            for s in cand:
                if prefer.search(s):
                    return cut(s, maxw)
        for s in cand:
            if 6 <= wc(s) <= maxw:
                return s
        for s in cand:
            return cut(s, maxw)
    return ""


# --------------------------------------------------------------------------------------------------
# mechanical verdict
# --------------------------------------------------------------------------------------------------
STRONG_FIG = re.compile(r"(process_designer|dsgnr|prs_def|bpmn|process\.png|process_desig|"
                        r"start_timer_process|pdm_process|delete_process)", re.I)
CANVAS_FIG = re.compile(r"(intg_designer|integration_designer|agent_builder|workflow_designer)", re.I)
BPMNWORD = re.compile(r"\b(bpmn|user task|service task|send message task|receive message task|"
                      r"business rule|exclusive gateway|parallel gateway|end event|start event|"
                      r"boundary event|intermediate event|sub-?process|pool|lane|swimlane|"
                      r"sequence flow|call activity)\b", re.I)
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


def artefact_kind(url, c, figs, fence):
    """What the page publishes, in words - the E1 row has to name it."""
    n_mer, n_asc = fence
    names = [os.path.basename(f["url"]) for f in figs]
    if n_mer and n_asc:
        return "a Mermaid flowchart and an ASCII sketch"
    if n_mer:
        return "a Mermaid flowchart"
    if n_asc:
        return "an ASCII arrow sketch"
    if c["n_model"]:
        return "a downloadable .bpmn model"
    if len(names) == 1:
        return "one figure (%s)" % names[0]
    return "%d figures (%s)" % (len(names), ", ".join(names[:4]) + (", ..." if len(names) > 4 else ""))


def strip_fp(t):
    """Two systematic false positives of the wide lexicon, both named and undone here:
      * the vendor's own name - `FlowX.AI` and `docs.flowx.ai` - matched `ai`/`llms` on every page;
      * the HTTP header `User-Agent` matched `agent` in request/header documentation.
    The processmaker census had the same problem with the word `model` (which this source uses for data
    and process models on hundreds of pages); `model` alone is therefore not in the lexicon at all."""
    t = re.sub(r"(?i)flowx\.?ai|docs\.flowx\.ai|llms\.txt", "FlowX", t)
    t = re.sub(r"(?i)user[\s-]?agent", "UserHeader", t)
    return t


def has_ai(url):
    return bool(AILEX.search(strip_fp(prose(url))))


def ai_fragment(url, maxw=20):
    """The first AI/LLM-lexicon hit on the page: the matched term, and the sentence that carries it, in
    the page's own words. Used only in row notes, so a researcher can see what the mention actually is -
    the wide lexicon has ordinary-English false positives (prompt/recommendation/classification) and the
    note must not pretend otherwise."""
    # The term is found on the false-positive-stripped copy, but the sentence is then quoted out of the
    # page's OWN text: strip_fp rewrites `FlowX.AI` to `FlowX`, and a quotation may not carry that edit.
    raw_t = verbatim_text(url)
    stripped = strip_fp(raw_t)
    for rs, ss in zip(re.split(r"(?<=[.!?])\s+", raw_t), re.split(r"(?<=[.!?])\s+", stripped)):
        m = AILEX.search(ss)
        if not m:
            continue
        w = rs.split()
        term_words = [x for x in m.group(0).split()]
        i = next((k for k, x in enumerate(w) if term_words[0].lower() in x.lower()), 0)
        frag = re.sub(r"^[\s>*#|\-]+", "", " ".join(w[max(0, i - 6):]))
        return (m.group(0), cut(frag, maxw))
    t = stripped
    m = AILEX.search(t)
    if not m:
        return None
    return (m.group(0), cut(t[max(0, m.start() - 60):m.end() + 60], maxw))


def fence_twins(url):
    """Pages that publish the same diagram fence as this one, under another version path: E3's
    'same diagram, one docs page under two URLs' (the version paths are normalised away, whitespace
    is dropped, so byte-identical-as-published fences - not merely similar ones - group together)."""
    return FENCE_TWINS.get(url) or []


FENCE_TWINS = {}


def build_fence_twins(pop, fence):
    """Group every page's diagram fences by content, version paths normalised away."""
    groups = {}
    for u in pop:
        n_mer, n_asc = fence.get(u, (0, 0))
        if not (n_mer + n_asc):
            continue
        blocks = re.findall(r"```[^\n]*\n(.*?)```", raw_body(u) or "", re.S)
        key = norm(re.sub(r"/4\.7\.x/|/5\.1/|/5\.9/", "/V/", " ".join(blocks)))
        if len(key) < 40:
            continue
        groups.setdefault(key, []).append(u)
    for k, v in groups.items():
        if len(v) > 1:
            for u in v:
                FENCE_TWINS[u] = [x for x in v if x != u]


def build_mechanical(url, c, sc, figs, fence, mirror):
    title = sc.get("title", "")
    n_mer, n_asc = fence
    has_diag = (n_mer + n_asc) > 0
    strong = [f for f in figs if STRONG_FIG.search(os.path.basename(f["url"]))]
    canvas = [f for f in figs if CANVAS_FIG.search(os.path.basename(f["url"]))]
    ai = has_ai(url)          # recomputed here with the false positives undone (see strip_fp)
    art = bool(c["n_fig"] or has_diag or c["n_model"])
    twins = mirror.get(url) or []

    if not art:
        q = pick_quote(url, BPMNWORD) or pick_quote(url)
        note = ("no artefact: the page publishes no figure, no diagram fence and no .bpmn model - "
                "%d standalone images, 0 diagram fences, 0 models." % c["n_fig"])
        frag = ai_fragment(url)
        if frag:
            note += (" The census lexicon's only hit on the page is '%s', in: \"%s\" - and with no "
                     "published artefact there is no diagram in which an AI element could sit inside a "
                     "process." % (frag[0], frag[1]))
        if twins:
            note += " Byte-identical to %s (version mirror)." % ", ".join(twins)
        return dict(verdict="EXCLUDE", reason="E0-no-artefact", judgment=False, evidence=q, note=note,
                    judged_from="mechanical screen (no figure opened by eye)", figures_looked_at=None)

    if strong:
        suffix = next((k for k in sorted(E2_NOTES, key=len, reverse=True) if url.endswith(k)), None)
        dismissal = E2_NOTES.get(suffix)
        q = pick_quote(url, BPMNWORD) or pick_quote(url)
        figs_s = ", ".join(os.path.basename(f["url"]) for f in strong[:4])
        note = ("BPMN-notation figure on the page (%s)." % figs_s)
        if dismissal:
            note += " Dismissed AI mention: " + dismissal
        elif ai:
            f = ai_fragment(url)
            note += (" The page's only AI/LLM-lexicon hit is '%s', in the sentence \"%s\"; it is not an element "
                     "of the pictured process." % (f[0], f[1]) if f else "")
        else:
            note += (" The census's AI/LLM lexicon (ledgers/_fx_class.py AILEX) finds no term anywhere "
                     "on the page, so the pictured diagram cannot carry a named AI element.")
        if twins:
            note += " Byte-identical to %s (version mirror)." % ", ".join(twins)
        return dict(verdict="EXCLUDE", reason="E2-no-ai-element", judgment=bool(ai),
                    evidence=q, note=note,
                    judged_from="eye ruling on the page's BPMN figure (ledgers/_fx_build.py E2_NOTES)"
                    if dismissal else "mechanical screen (no figure opened by eye)",
                    figures_looked_at=figs_s)

    # E3: the same diagram is already recorded under another version URL.
    rec, twin = None, None
    for cand in (mirror.get(url) or []) + fence_twins(url):
        for r in RULINGS:
            if r["url"] == cand:
                rec, twin = r, cand
    if rec:
        q = pick_quote(url, BPMNWORD) or pick_quote(url)
        note = ("The same diagram is already recorded at record %s (%s): that page publishes a "
                "byte-identical diagram fence and this page is its second URL (the two pages differ "
                "only in their related-link cards). duplicate_of points at the record. This row is "
                "why the exclusion is mechanical; anything this page adds beyond the diagram is "
                "quoted here: %s"
                % (rec["n"], rec["url"],
                   "\"%s\" (lexicon term '%s')" % (ai_fragment(url)[1], ai_fragment(url)[0]) if ai else
                   "nothing - it carries no AI/LLM term, so it does not even restate the AI binding."))
        return dict(verdict="EXCLUDE", reason="E3-duplicate", judgment=False, evidence=q, note=note,
                    duplicate_of="corpus/flowx-ai/%s_%s.md" % (rec["n"], rec["slug"]),
                    judged_from="mechanical screen (identical diagram fence, ledgers/flowx-ai.raw fence groups)",
                    figures_looked_at=None)

    q = pick_quote(url, BPMNWORD) or pick_quote(url)
    kind = artefact_kind(url, c, figs, fence)
    subject = title or url.rsplit("/", 1)[-1]
    note = ("the page publishes %s for \"%s\" and no BPMN-notation diagram. E1: that artefact is not "
            "BPMN 2.0 notation - it is %s." % (kind, subject,
                                               "a Mermaid/ASCII rendering of the page's own subject"
                                               if has_diag else
                                               "product UI screenshots of the vendor's own screens"))
    if canvas:
        note += (" %d of the page's figures come from the vendor's Integration Designer / Agent "
                 "Builder UI (%s), a canvas this source's own glossary describes as 'Not a BPMN "
                 "process'."
                 % (len(canvas),
                    ", ".join(os.path.basename(f["url"]) for f in canvas[:3])))
    if twins:
        note += " Byte-identical to %s (version mirror)." % ", ".join(twins)
    return dict(verdict="EXCLUDE", reason="E1-not-bpmn",
                judgment=bool(has_diag or canvas), evidence=q, note=note,
                judged_from="mechanical screen (no figure opened by eye)",
                figures_looked_at=", ".join(os.path.basename(f["url"]) for f in canvas[:3]) or None)


def main():
    dry = "--dry" in sys.argv
    pop = json.load(open(os.path.join(RAW, "population.json")))
    sc = {x["url"]: x for x in json.load(open(os.path.join(RAW, "screen.json")))}
    figs = json.load(open(os.path.join(RAW, "figmeta.json")))
    fence = {k: tuple(v) for k, v in json.load(open(os.path.join(RAW, "fences.json"))).items()}
    mirror = json.load(open(os.path.join(RAW, "mirror.json")))
    cls = {c["url"]: c for c in json.load(open(os.path.join(RAW, "classify.json"))) if c}
    build_fence_twins(pop, fence)
    print("pages whose diagram fence is published identically on another version URL:",
          len(FENCE_TWINS))
    for u, v in list(FENCE_TWINS.items())[:10]:
        print("   ", u.replace("https://docs.flowx.ai", ""), "<->",
              [x.replace("https://docs.flowx.ai", "") for x in v])

    rows, bad_quotes, counts, jcount = [], [], {}, 0
    fcount = fence.get
    for i, url in enumerate(pop, 1):
        c = cls.get(url)
        s = sc.get(url, {})
        pf = figs.get(url) or []
        fn = fence.get(url, (0, 0))
        r = ruling_for(url)
        if r:
            row = dict(
                n=i, verdict="UNCERTAIN", reason=None, judgment=True,
                evidence=pick_quote(url, BPMNWORD) or pick_quote(url),
                note=("%s: the AI element and the process it sits in are documented here; the full "
                      "evidence, the artefacts and the question are in the record. The page publishes "
                      "%s." % (r["kind"], r["kind"])),
                record="corpus/flowx-ai/%s_%s.md" % (r["n"], r["slug"]),
                needs_visual_check=False, needs_human_ruling=True,
                question=r["question"],
                judged_from="eye ruling on the page's text and figures (ledgers/_fx_build.py RULINGS)",
                figures_looked_at=", ".join(r.get("figures") or []) or None)
        else:
            m = build_mechanical(url, c, s, pf, fn, mirror)
            row = dict(n=i, verdict=m["verdict"], reason=m["reason"], judgment=m["judgment"],
                       evidence=m["evidence"], note=m["note"], record=None,
                       needs_visual_check=False, needs_human_ruling=False, question=None,
                       duplicate_of=m.get("duplicate_of"),
                       judged_from=m["judged_from"], figures_looked_at=m["figures_looked_at"])
        row["url"] = url
        row["title"] = s.get("title", "")
        row["accessed"] = ACCESSED
        row["surface"] = "docs:flowx-ai:" + (s.get("surface") or "root")
        row["screen"] = "figures=%s fences=%s/%s models=%s words=%s ai=%s" % (
            c["n_fig"], fn[0], fn[1], c["n_model"], s.get("words"), c["ai"])
        # verbatim check
        vt = qnorm(verbatim_text(url))
        if row["evidence"] and qnorm(row["evidence"]).rstrip(" .…") not in vt:
            bad_quotes.append((i, url, "evidence: %r" % row["evidence"]))
        for bad in span_check(row, vt):
            bad_quotes.append((i, url, bad))
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1
        if row["verdict"] == "EXCLUDE" and row["judgment"]:
            jcount += 1
        rows.append(row)

    print("rows", len(rows), counts, "judgement-exclusions", jcount,
          "(%.1f%%)" % (100.0 * jcount / len(rows)))
    reasons = {}
    for r in rows:
        if r["verdict"] == "EXCLUDE":
            reasons[r["reason"]] = reasons.get(r["reason"], 0) + 1
    print("exclusion codes:", reasons)
    print("verbatim-quote failures:", len(bad_quotes))
    for i, u, q in bad_quotes[:12]:
        print("   n=%d %s\n      %s" % (i, u, q))
    # The check itself is written out as an artifact: every double-quoted span in every row's evidence
    # and note, tested against the page that row judges (see span_check). It is the audit trail for the
    # census's evidence rule, and it is what makes a reviewer's spot check cheap.
    with open(os.path.join(ELI, "flowx-ai.quotes.txt"), "w", encoding="utf-8") as fh:
        fh.write("# Every double-quoted span in the 945 rows' evidence and note fields, checked against\n"
                 "# the page that row judges (span_check in _fx_build.py; whitespace and curly/straight\n"
                 "# quotes normalised). Single-quoted text quotes another named source and is not checked.\n"
                 "# failures: %d\n" % len(bad_quotes))
        for i, u, q in bad_quotes:
            fh.write("n=%d %s\n    %s\n" % (i, u, q))
    if dry:
        return 0

    # ---------------------------------------------------------------- ledger + frontier
    header = {
        "type": "header", "source": "flowx-ai",
        "source_name": "FlowX.AI documentation (docs.flowx.ai, Mintlify)",
        "read": ACCESSED,
        "population_size": len(pop), "census": True,
        "artefact_criteria": ("thesis 004_method, sec:method:use_case_elicitation - BPMN 2.0 diagram "
                              "with an explicit AI/LLM element inside the process"),
        "enumeration_method": (
            "ONE CENSUS OVER THE WHOLE HOST, THREE PUBLISHED INDEXES UNIONED. The population is the union "
            "of (1) https://docs.flowx.ai/sitemap.xml - 926 <loc> entries, the documentation platform's "
            "own sitemap; (2) https://docs.flowx.ai/llms.txt - 386 entries, the index this Mintlify site "
            "publishes for LLM crawlers; (3) the 11 https://docs.flowx.ai/_llms/* machine indexes the "
            "llms.txt points at (v4.7.x, v5.1, v5.9-*, release-notes and their sub-lists), which list "
            "pages by heading with their URLs. The union is 945 URLs - the 11 _llms indexes are inside "
            "llms.txt's own list, and sitemap.xml and llms.txt otherwise agree - and it is frozen in "
            "ledgers/flowx-ai.raw/population.json before any row was judged. NOTHING WAS NARROWED: no "
            "version facet, no keyword filter and no search box was used; all four published version "
            "trees (5.9, 5.1, 4.7.x and the 120-page release-notes archive) plus the 11 _llms indexes "
            "are in the population, and every row below is one of the 945. Every page's own published "
            "markdown was read (see access), so the AI terms could be counted over the whole population "
            "rather than over a search result."),
        "entry_points": ["https://docs.flowx.ai/sitemap.xml", "https://docs.flowx.ai/llms.txt",
                         "https://docs.flowx.ai/_llms/v5-9", "https://docs.flowx.ai/_llms/v5-1",
                         "https://docs.flowx.ai/_llms/v4-7-x", "https://docs.flowx.ai/_llms/release-notes",
                         "https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration",
                         "https://docs.flowx.ai/5.9/ai-platform/tutorials/document-processing",
                         "https://docs.flowx.ai/5.1/docs/platform-deep-dive/integrations/ai-nodes"],
        "access": "public",
        "queries": [],
        "browser_tool": BROWSER,
        "surface_parts": {"5.9": 381, "5.1": 228, "4.7.x": 205, "release-notes": 120, "llms-index": 11},
        "access_method": (
            "docs.flowx.ai is Mintlify, so every page publishes its own markdown twin: appending `.md` to "
            "any page URL returns the author's own markdown (the site says so itself in llms.txt). All "
            "945 were fetched that way - ledgers/_fx_fetch.py, about one request per second, 4 workers "
            "with a 0.4 s gap - into ledgers/flowx-ai.raw/pages/, and the 493 pages of the 5.9 tree and "
            "the release-notes archive that the site's own llms-full.txt bundle (14.3 MB) supplies were "
            "cross-checked from ledgers/flowx-ai.raw/pages_llmsfull/ (the two are the same published "
            "markdown). Screening was offline over that text: ledgers/_fx_screen.py (titles, surfaces, "
            "figures, AI sentences), ledgers/_fx_class.py (the dry-run classifier: 945 classified, 0 "
            "missing; E0 374, E1 535, BPMN-figure zone 36), ledgers/flowx-ai.raw/figmeta.json (all 3,965 "
            "figures of the 535 figure-bearing pages, with their alt text) and "
            "ledgers/flowx-ai.raw/fences.json (39 pages with a Mermaid fence, 24 with an ASCII sketch)."),
        "figure_method": (
            "Artefact test, applied offline to every one of the 945 pages' own markdown: an artefact is a "
            "standalone figure, a diagram fence (Mermaid; or a plain fence carrying box-drawing "
            "characters / arrow-node syntax) or a linked .bpmn model. 371 pages publish none (E0). 530 "
            "publish something else (E1, which names what it is: product UI screenshots, the vendor's own "
            "Integration Designer / Agent Builder canvas - 'Not a BPMN process' in this source's own "
            "glossary - Mermaid flowcharts, ASCII sketches, architecture box diagrams). 36 pages publish "
            "a BPMN-notation figure, identified by the figure's own filename or alt text "
            "(process_designer*, prs_def, bpmn*, pdm_process, delete_process, start_timer_process, "
            "process*.png): the 15 of those 36 that also discuss AI were each read and their AI mention "
            "dismissed by hand in E2_NOTES; the other 21 carry no AI/LLM term at all. The AI/LLM count is "
            "a census of a wide lexicon over the whole population, with two systematic false positives "
            "named and undone (the vendor's own name `FlowX.AI`, which made every page look AI-bearing, "
            "and the HTTP header `User-Agent`, which matched `agent`) - the same class of correction the "
            "processmaker census had to make for the word `model`. Images were used to confirm, not to "
            "discover: the 5.9 Process Designer's node palette was read by eye (15 tiles, "
            "ledgers/flowx-ai.raw/figures/sh_palette.png) and confirms the finding below."),
        "key_finding": (
            "In this source AI reaches BPMN only by DELEGATION, never as a BPMN node type. The 5.9 BPMN "
            "Process Designer is genuine BPMN (pool/lane 'Default', start/end event circles, user tasks, "
            "service tasks, call activities, exclusive/parallel gateways, boundary events) and its "
            "'Process Nodes' palette offers no AI node: only Start Events, Intermediate Events, Boundary "
            "Events and Activities. AI is bound into a process by an ACTION on an existing BPMN node - a "
            "Service Task (or Send/Receive Message Task) carrying 'Start Integration Workflow', as "
            "records 002/003/004 document. The AI-native canvases (Integration Designer, Agent Builder) "
            "are the vendor's own notation, which the source's own glossary calls 'Not a BPMN process'."),
        "note": (
            "Read-only throughout: no login, no account, no form submitted, no captcha, nothing saved or "
            "deployed in any vendor UI; the browser was used only to read pages in my own tab of the "
            "shared Chrome (peers' tabs untouched). Pages were fetched over HTTP at about one request per "
            "second. No page of the population was blocked. CORRECTION recorded rather than rewritten: an "
            "earlier count in this session's dry run treated every fenced block containing `->` as a "
            "diagram, which counted JSON and JavaScript examples as diagrams (110 AI pages / 285 no-AI "
            "pages 'with a diagram'); the detector was tightened to Mermaid fences plus plain fences "
            "carrying box-drawing characters or arrow-node syntax, which is the 61-page figure quoted "
            "above. Two further false positives are named and undone in ledgers/_fx_build.py: "
            "`FlowX.AI`/`docs.flowx.ai` (the vendor's name matched `ai`/`llms` on every page) and "
            "`User-Agent` (matched `agent`)."),
    }
    frontier = [("# frontier for the flowx-ai census: sitemap.xml U llms.txt U the 11 _llms indexes = "
                 "%d URLs, one line per row" % len(pop))] + pop
    if not dry:
        with open(os.path.join(ELI, "flowx-ai.jsonl"), "w", encoding="utf-8") as fh:
            fh.write(json.dumps(header, ensure_ascii=False) + "\n")
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(os.path.join(ELI, "flowx-ai.frontier.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(frontier) + "\n")
        print("wrote ledgers/flowx-ai.jsonl and ledgers/flowx-ai.frontier.txt")

    # ---------------------------------------------------------------- records + captures
    os.makedirs(CORPUS, exist_ok=True)
    for r in RULINGS:
        write_record(r, (cls.get(r["url"]) or {}).get("n_fig", 0))
    footer = {
        "type": "footer", "rows": len(rows), "status": "DONE",
        "include": counts.get("INCLUDE", 0), "uncertain": counts.get("UNCERTAIN", 0),
        "exclude": reasons, "blocked": counts.get("BLOCKED", 0),
        "judgment_exclusion_share": round(jcount / len(rows), 4),
        "judgement_rows": jcount,
        "records_written": ["%s_%s" % (r["n"], r["slug"]) for r in RULINGS],
        "duplicates_excluded": [r["url"] for r in rows if r["reason"] == "E3-duplicate"],
        "date_end": ACCESSED,
        "self_audit_note": ("Every row's `evidence` was machine-checked against the page's own markdown "
                            "(%d failures before this run: %d). The judgement-exclusion share is the "
                            "template's gate; the judgement-true E1 rows are the pages that publish a "
                            "diagram fence or a vendor-canvas figure, i.e. exactly the rows where the "
                            "notation call could be wrong." % (len(bad_quotes), len(bad_quotes))),
    }
    if not dry:
        with open(os.path.join(ELI, "flowx-ai.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(footer, ensure_ascii=False) + "\n")
        print("footer written; records:", footer["records_written"])
    return rows, bad_quotes


# --------------------------------------------------------------------------------------------------
# record writing
# --------------------------------------------------------------------------------------------------
FONT_CANDIDATES = [r"C:\Windows\Fonts\consola.ttf", r"C:\Windows\Fonts\DejaVuSansMono.ttf",
                   r"C:\Windows\Fonts\lucon.ttf", r"C:\Windows\Fonts\cour.ttf"]


def wrap(text, width):
    out = []
    for para in text.split("\n"):
        if not para.strip():
            out.append("")
            continue
        line = ""
        for word in para.split(" "):
            if len(line) + len(word) + 1 > width:
                out.append(line)
                line = word
            else:
                line = (line + " " + word).strip()
        out.append(line)
    return out


def text_capture(path, title, subtitle, blocks, width=118):
    from PIL import Image, ImageDraw, ImageFont
    font = None
    for c in FONT_CANDIDATES:
        if os.path.exists(c):
            font = ImageFont.truetype(c, 15)
            break
    if font is None:
        font = ImageFont.load_default()
    lines = wrap(subtitle, width) + [""]
    for b in blocks:
        lines += wrap(b, width) + [""]
    lh = 20
    img = Image.new("RGB", (width * 9 + 30, max(220, lh * (len(lines) + 3))), "white")
    d = ImageDraw.Draw(img)
    d.text((14, 10), title[:120], fill="black", font=font)
    d.line([(14, 32), (img.width - 14, 32)], fill=(150, 150, 150))
    y = 42
    for ln in lines:
        d.text((14, y), ln, fill="black", font=font)
        y += lh
    img.save(path)
    print("capture:", os.path.basename(path), img.size, len(lines), "lines")


def capture_blocks(url, kind, prefer):
    """The page's own text that carries the finding: its diagram fences verbatim, plus the sentences
    that name the AI binding. Nothing is paraphrased - this is a text render of the published markdown,
    used because these pages publish their process as Mermaid/ASCII/prose rather than as a diagram image."""
    raw = raw_body(url)
    blocks = []
    for m_ in re.finditer(r"```[^\n]*\n(.*?)```", raw, re.S):
        if "→" in m_.group(1) or "-->" in m_.group(1) or "─" in m_.group(1) or "|" in m_.group(1):
            b = m_.group(1).strip("\n")
            if len(b) < 900:
                blocks.append(b)
    seen = set()
    for s in sentences(url, keep_pipes=True):
        s = s.strip()
        if len(s) < 25 or len(s) > 400:
            continue
        if any(p.search(s) for p in prefer) and s[:40] not in seen:
            seen.add(s[:40])
            blocks.append("> " + s)
        if len(blocks) > 16:
            break
    return blocks[:16]


def write_record(r, n_fig):
    url = r["url"]
    blocks = capture_blocks(url, r["kind"], [re.compile(p, re.I) for p in r.get("prefer", [])])
    if r["kind"] == "ui-canvas":
        png = sheet_of(r)
    else:
        png = os.path.join(CORPUS, "%s_%s.png" % (r["n"], r["slug"]))
        text_capture(png, "%s  |  %s" % (r["n"], url),
                     "Text render of this page's own published markdown (the page publishes its process "
                     "as %s, not as a diagram image). Verbatim, not paraphrased." % r["kind"], blocks)
    rec = [
        "---", "n: %s" % r["n"], "record: %s" % r["n"],
        "url: %s" % url, "source: flowx-ai",
        "surface: docs:flowx-ai:%s" % url.split("/")[3],
        "accessed: %s" % ACCESSED, "verdict: UNCERTAIN", "needs_human_ruling: true",
        "question: %s" % r["question"],
        "page_publishes: %s" % r["kind"],
        "capture_quality: legible",
        "quotes: the page's own words. Markdown emphasis and code markers are rendered away and long "
        "quotations are elided with \"...\"; text in single quotes is quoted from another named source "
        "(the site's own glossary, or a label read in this page's figure).",
        "screenshot: %s" % os.path.basename(png),
        "artefacts:",
        "  - screenshot: %s" % os.path.basename(png),
    ]
    for f in (r.get("figures") or []):
        rec.append("  - file: %s" % f)
    rec += ["bpmn_evidence: |"] + ["  " + l for l in r["bpmn_evidence"].splitlines()]
    rec += ["ai_evidence: |"] + ["  " + l for l in r["ai_evidence"].splitlines()]
    nfig = n_fig
    note = ("Read from the page's own published markdown twin (%s.md), and - where a Mintlify component "
            "renders differently from the twin - from the page as displayed in the browser, on %s; nothing "
            "on this page was paraphrased. The capture next to this record is %s. The page publishes no BPMN-notation "
            "diagram: %s. %s"
            % (url, ACCESSED,
               "a contact sheet of the page's %d figures" % nfig if r["kind"] == "ui-canvas"
               else "a text render of the page's own diagram/prose, because the page publishes its "
                    "process as %s rather than as a diagram image" % r["kind"],
               "its %d figures are node-configuration panels, not a process diagram" % nfig
               if nfig else "it carries no figure at all",
               "The evidence above is quoted verbatim from that page."))
    rec += ["note: |"] + ["  " + l for l in note.splitlines()]
    path = os.path.join(CORPUS, "%s_%s.md" % (r["n"], r["slug"]))
    open(path, "w", encoding="utf-8").write("\n".join(rec) + "\n")
    print("record:", os.path.basename(path))


def sheet_of(r):
    import importlib.util
    spec = importlib.util.spec_from_file_location("fxfigs", os.path.join(ELI, "_fx_figs.py"))
    fx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fx)
    slug = re.sub(r"^https://docs\.flowx\.ai/", "", r["url"]).replace("/", "__")
    urls = fx.page_figures(slug)
    d = slug
    for i, u in enumerate(urls or [], 1):
        name = os.path.basename(u.split("?")[0])
        st, n = fx.fetch(u, os.path.join(fx.FIGS, d, "%03d_%s" % (i, name)))
        print("   fig %-60s %s" % (name[:60], st))
    out = os.path.join(CORPUS, "%s_%s.png" % (r["n"], r["slug"]))
    fx.sheet([d], out)
    return out


if __name__ == "__main__":
    main()
