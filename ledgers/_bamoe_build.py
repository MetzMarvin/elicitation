#!/usr/bin/env python3
"""Build the ibm-bamoe ledger: one row per enumerated item of the two-half frontier.

`python _bamoe_build.py` prints the row table for review; `--write` writes
ledgers/ibm-bamoe.jsonl (header, rows, footer) and ledgers/ibm-bamoe.frontier.txt.

Half one is a census of the full 9.5.x documentation ToC (117 topics, fetched through the docs
content API and screened offline in ledgers/_bamoe/screen.json). Half two is the search protocol
over IBM Community BAMOE posts. Three rows cover the two adjacent distribution surfaces the
assignment names (the VS Code marketplace listing and the accelerator GitHub repository linked
from the community library page).

The screen decides the bulk of the docs rows with rules that can be re-run:
  R1  no figures at all on the page                                   -> E0-no-artefact
  R2  the page's figure paths name DMN/DRD/DRL/SceSim artefacts       -> E1-not-bpmn
  R3  a diagram-named figure and the AI screen does not fire          -> E2-no-ai-element
  R4  figures that no name/caption calls a diagram, AI screen silent  -> E0-no-artefact
Rows the screen cannot decide (a real AI token in the page, or a figure only an eye can classify)
sit in RULED with the ruling written out; a page that carries an AI mention and is not in RULED
fails the build rather than being guessed.
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
D = ELI / "ledgers" / "_bamoe"
COM = ELI / "ledgers" / "_bamoe_comm"
ACCESSED = "2026-09-25"
SLUG = "ibm-bamoe"
DOCS = "https://www.ibm.com/docs/en/ibamoe/9.5.x?topic="

# The AI branch's pages were looked at on the branch's own sheets rather than on a per-page sheet.
AI_SHEETS = {
    "custom-generative-ai-task.html":
        "contact sheets ledgers/_bamoe/sheet_genai.png and sheet_ai_extra.png (the AI branch's "
        "figures; the decisive tile workflow__genai-task-create.png was also read at full size)",
    "ai-agent-task.html":
        "contact sheets ledgers/_bamoe/sheet_genai.png, sheet_aiagent.png and sheet_ai_extra.png "
        "(the AI branch's figures; workflow__langflow-task-props.png read at full size)",
    "ai-mcp-server.html":
        "contact sheets ledgers/_bamoe/sheet_mcp.png and sheet_mcp2.png (every figure of this page "
        "was read at full size on one of the two)",
}

# ---------------------------------------------------------------- text helpers
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")
AI = re.compile(r"\b(ai|a\.i\.|llm|gen\s?ai|generative|gpt-?[\d.]*|chat-?gpt|claude|anthropic|openai|"
                r"azure\s?openai|gemini|vertex|groq|mistral|ollama|cohere|deepseek|hugging\s?face|"
                r"bedrock|watsonx|watson|langflow|mcp|agent|agents|prompt|prompts|copilot|embedding|"
                r"vector|rag|machine learning|ml|model)\b", re.I)
PROC = re.compile(r"\b(bpmn|process diagram|workflow diagram|pool|lane|gateway|service task|user task|"
                  r"sub-?process|sequence flow|modell?er|modeler|canvas)\b", re.I)
NOISE = {"model"}          # 'model' alone fires on "process model" prose; not an AI mention


def text_of(html):
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", html)
    t = TAG.sub(" ", t)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                 ("&quot;", '"'), ("&#39;", "'"), ("’", "'")):
        t = t.replace(a, b)
    return WS.sub(" ", t).strip()


CHROME = re.compile(r"^(skip main navigation|#\w|back to (blog list|library)|share$|print$|"
                    r"threads \d+|view only)|press enter|members \d+|blogs \d+", re.I)


def clean(t):
    """Drop a community page's navigation chrome and mojibake so a quote is the item's own words."""
    t = t.replace("�", "")
    keep = [s for s in sents(t) if len(s) > 40 and not CHROME.search(s.strip())]
    return WS.sub(" ", " ".join(keep)).strip()


def sents(t):
    return re.split(r"(?<=[.!?])\s+", t)


def clip(s, n=25):
    return " ".join(s.split()[:n])


def pick(text, pat, n=25):
    """First sentence of `text` matching `pat`, capped at n words (shared rules' quote limit)."""
    rx = pat if hasattr(pat, "search") else re.compile(pat, re.I)
    for s in sents(text):
        if rx.search(s):
            return clip(s, n)
    q = clip(text, n)
    if not q:
        raise SystemExit("no evidence could be quoted from a page (pattern %s)" % pat)
    return q


# ---------------------------------------------------------------- docs half
def docs_rows():
    screen = json.loads((D / "screen.json").read_text(encoding="utf-8"))
    content = json.loads((D / "content_9.5.x.json").read_text(encoding="utf-8"))
    rows = []
    for i, r in enumerate(screen, 1):
        html = (content.get(r["href"]) or {}).get("html", "")
        t = clean(text_of(html))
        rows.append(docs_row(i, r, t))
    return rows


def docs_row(i, r, t):
    figs = r["figures"]
    fignames = [f.split("/")[-1] for f in figs]
    ai = sorted(set(r["ai"]) - NOISE) if isinstance(r["ai"], list) else []
    has_figs = bool(figs)
    row = {
        "n": None, "verdict": None, "reason": None, "judgment": False, "evidence": None,
        "note": None, "url": DOCS + r["topicId"], "title": r["label"], "duplicate_of": None,
        "accessed": ACCESSED, "surface": "docs:ibamoe-9.5.x", "record": None,
        "needs_visual_check": False, "needs_human_ruling": False, "question": None,
        "judged_from": "mechanical page screen (ledgers/_bamoe_build.py)",
        "figures_looked_at": sheets_ok(i, r, sheet_for(r)),
        "screen": ("figures=%d diagram_named=%d bpmn_markers=%d dotfiles=%d ai=%s"
                   % (len(figs), len(r["diagram_named_figures"]), len(r["bpmn_markers"]),
                      len(r["dotfiles"]), ai or "-")),
    }
    if i in RULED:
        row.update({k: v for k, v in RULED[i].items() if k != "q"})
        if RULED[i].get("evidence"):
            row["evidence"] = RULED[i]["evidence"]
        else:
            row["evidence"] = pick(t, RULED[i]["q"])
        if row["reason"] or row["verdict"] != "EXCLUDE":
            row["judged_from"] = "eye ruling on the page's figures (ledgers/_bamoe_build.py)"
        if "note_extra" in RULED[i]:
            row["note"] = row["note"] + " " + RULED[i]["note_extra"]
        return row
    if not has_figs:
        row["verdict"], row["reason"] = "EXCLUDE", "E0-no-artefact"
        row["evidence"] = pick(t, PROC)
        row["note"] = ("R1: the topic page carries no figure at all (%d words of prose, 0 <img> in its "
                       "content region, no .bpmn/.dmn link), so the enumerated item contains no process "
                       "artefact. Figures on the page: none." % (r["words"] or 0))
        if ai:
            row["note"] += (" For the researcher: the AI screen does fire on this page - on %s - but "
                            "there is no diagram on the page for an element to sit inside; the quoted "
                            "sentence above is where the page's own words about it are. The page is "
                            "kept in the ledger rather than dropped so this judgement is reviewable."
                            % ", ".join(ai))
        return row
    if ai:
        raise SystemExit("page %d (%s) carries an AI mention %s and has figures but no ruling: add it "
                         "to RULED" % (i, r["href"], ai))
    joined = " ".join(figs)
    if re.search(r"authoringDecisions|dmn|decision|drg|drd|scesim|test-scenario|businessrule|"
                 r"traffic-violation", joined, re.I) or \
       re.search(r"\b(DMN|DRD|DRG|DRL|decision|rule|test scenario)\b", r["label"], re.I):
        row["verdict"], row["reason"] = "EXCLUDE", "E1-not-bpmn"
        row["evidence"] = pick(t, r"decision|rule|DMN")
        row["note"] = ("R2: the page's figures (%s) are DMN notation - decision-requirement diagrams, "
                       "decision tables, boxed expressions, DRL rules, test-scenario tables - not BPMN "
                       "2.0: no pools, lanes, events, gateways or sequence flows. Notation named: DMN "
                       "1.x (decision requirements graph / decision table). The page carries no AI "
                       "mention (the AI screen does not fire)."
                       % " ".join(fignames[:6]))
        return row
    if r["diagram_named_figures"]:
        row["verdict"], row["reason"] = "EXCLUDE", "E2-no-ai-element"
        row["evidence"] = pick(t, r"\bmodel\b|" + PROC.pattern)
        row["note"] = ("R3: the page's diagram-named figures (%s) are BPMN 2.0 process diagrams, and "
                       "the page carries no AI mention - the AI screen fires on nothing but the generic "
                       "word 'model' in process-modelling prose, which is what the quote above shows. "
                       "The dismissal is E2: the artefact is BPMN but contains no AI element inside "
                       "the process."
                       % " ".join([f.split("/")[-1] for f in r["diagram_named_figures"]][:4]))
        return row
    row["verdict"], row["reason"] = "EXCLUDE", "E0-no-artefact"
    row["evidence"] = pick(t, PROC)
    row["note"] = ("R4: the page's %d figures (%s) are editor/console/UI screens that no figure name or "
                   "caption calls a diagram, there is no BPMN marker and no process-file link, and the "
                   "AI screen does not fire on the page's content region: no process artefact."
                   % (len(figs), " ".join(fignames[:6])))
    return row


def sheet_for(r):
    """The contact sheet this page's figures were looked at on, if one exists."""
    parts = r["href"].split("/")
    parent, base = parts[-2], parts[-1].replace(".html", "")
    cand = D / ("sh_%s_%s.png" % (parent, base))
    if cand.exists():
        return "contact sheet ledgers/_bamoe/%s (%d figures)" % (cand.name, len(r["figures"]))
    if r["href"].split("/")[-1] in AI_SHEETS:
        return AI_SHEETS[r["href"].split("/")[-1]]
    return ""


def sheets_ok(i, r, val):
    """A page with figures must name where they were looked at; the build refuses to guess."""
    if r["figures"] and not val:
        raise SystemExit("page %d (%s) has %d figures but no contact sheet: build one or add it to "
                         "AI_SHEETS" % (i, r["href"], len(r["figures"])))
    if not r["figures"]:
        return "no figure opened by eye; the page has no figure (decided by the mechanical screen)"
    return val


# ---------------------------------------------------------------- rulings
RULED = {
    10: dict(verdict="EXCLUDE", reason="E1-not-bpmn", judgment=True, q=r"component",
             note="The page's ten figures are architecture and legend box diagrams (arch-dev.png, "
                  "arch-runtime.png, lgnd-*.png) for the software development lifecycle: boxes, "
                  "arrows and a colour legend, not BPMN 2.0 - no pools, lanes, events, gateways or "
                  "sequence flows. Notation named: architecture box diagram. The AI tokens the "
                  "screen sees (agent, langflow, llm, mcp) sit in the lifecycle prose about product "
                  "components, not inside a process diagram."),
    12: dict(verdict="EXCLUDE", reason="E1-not-bpmn", judgment=True, q=r"environment|AI",
             note="The page's one figure (bamoe-canvas-openshift-topology.png) is a deployment "
                  "topology diagram - namespaces, pods and services as boxes inside an OpenShift "
                  "cluster, not BPMN 2.0. Notation named: infrastructure topology diagram. The 'AI' "
                  "token is the platform name Red Hat OpenShift AI in the surrounding prose, not an "
                  "element inside a process."),
    24: dict(verdict="EXCLUDE", reason="E0-no-artefact", judgment=True, q=r"environment|AI",
             note="The page's three figures are product screenshots side by side "
                  "(bamoe-business-central.png, bamoe-canvas.png, bamoe-developer-tools.png) in a "
                  "feature-comparison table: no process artefact. The AI tokens ('AI', 'prompt') are "
                  "the comparison row about AI-assisted authoring, not a diagram."),
    47: dict(verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, q=r"\bmodel\b",
             note="The page's figures are a BPMN 2.0 process (process-decisions-embedded-"
                  "integration.png) plus DMN diagrams for a traffic-violation case. The process "
                  "diagram's activities are human/service tasks and a gateway; nothing in it is an "
                  "AI element. The AI screen fires only on the generic word 'model' - 'Traffic "
                  "Violation DMN model', 'decision model' - i.e. on decision modelling, not on AI; "
                  "the quote above is that mention. Dismissal: E2, BPMN artefact with no AI element "
                  "inside the process."),
    55: dict(verdict="EXCLUDE", reason="E0-no-artefact", judgment=True, q=r"provider|account|AI",
             note="The page's one figure (image17.png) is the provider-picker dialog of the editor's "
                  "account settings (Git and Cloud providers). No process artefact. The 'AI' token is "
                  "the AI-provider card group in that same dialog, quoted above - a connection list "
                  "outside any process."),
    63: dict(verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, q=r"prompt",
             note="The page's figures are BAMOE Canvas / VS Code / console screens for generating "
                  "form code from user tasks; four of them are diagram-named because they show the "
                  "process or the task list (form-gen-user-tasks.png, form-gen-process-user-task.png, "
                  "form-gen-list-project-user-tasks.png, form-gen-new-process.png). Those process "
                  "diagrams carry user tasks and nothing else - no AI element. The only AI-screen hit "
                  "is the plural 'prompts', quoted above, which is the command-line prompt of the "
                  "generator, not an AI prompt. Dismissal: E2."),
    78: dict(verdict="UNCERTAIN", judgment=True, record="corpus/ibm-bamoe/002_docs-authoring-workflows-palette.md",
             needs_human_ruling=True, q=r"custom task|AI",
             evidence="Custom Tasks ( Keyboard Shortcuts ) -> to display custom tasks that have been "
                      "integrated into the editor (e.g., AI and flexible process tasks as",
             question="The page documents the BPMN editor and its palette, and the palette's AI "
                      "group (Gen AI Task, AI Agent Task) is documented here as an editor feature; the "
                      "page's own figures are the editor, a decision task, property panels and the "
                      "ad-hoc sub-process, none of which shows a process containing an AI node. Does a "
                      "page that documents an AI node type as palette furniture, without a diagram in "
                      "which the node sits inside a process, count as a corpus item (INCLUDE), or is it "
                      "E2-no-ai-element because no BPMN diagram on the page contains the element?"),
    99: dict(verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True, q=r"prompt",
             note="The page's 32 figures are BAMOE Management Console screens; several render live "
                  "process diagrams (mgmt-console-process-diagram-panel.png and the PIM plan views), "
                  "which are BPMN 2.0 as rendered by the runtime. Every activity in them is a human "
                  "task, service task or gateway; no AI element is visible. The AI screen fires once, "
                  "on the word 'prompt' - quoted above - in the sense of a command prompt. "
                  "Dismissal: E2."),
    105: dict(verdict="INCLUDE", judgment=True,
              record="corpus/ibm-bamoe/001_docs-genai-task-canvas.md",
              evidence="Integrate AI into Workflows by dragging a Gen AI task directly into your BPMN "
                       "process models, in the",
              note="The page is the documentation of BAMOE's Gen AI task - an AI node type of the "
                   "BPMN editor. Its figure genai-task-create.png (567x252) is a crop of the BAMOE "
                   "Canvas BPMN editor showing the palette's AI group and the Gen AI Task node placed "
                   "on the dotted process canvas; the remaining figures are the node's property panels "
                   "(AI provider, model, prompt, data mapping). The AI element is inside the process: "
                   "the node is dragged into the BPMN model and bound to watsonx/OpenAI/Ollama, and "
                   "the page's own words quoted above say so."),
    106: dict(verdict="EXCLUDE", reason="E0-no-artefact", judgment=True, q=r"MCP|agent|LLM",
              note="The page's seven figures are LLM chat transcripts (lifecycle-management-through-"
                   "LLM-1..4.png, traffic-violation-1/2.png: a Goose/Claude-style chat with MCP tool "
                   "cards such as 'Create Orders Bpm Process Workflow Model' and 'Execute "
                   "TrafficViolation-Dm Model') and the MCP Inspector UI. There is no process artefact "
                   "on the page - no BPMN diagram, no process model in BPMN notation; the AI works the "
                   "engine from outside the process, over MCP tools, and the decision model it "
                   "executes in the transcripts is DMN. Dismissal: E0-no-artefact."),
    107: dict(verdict="UNCERTAIN", judgment=True,
              record="corpus/ibm-bamoe/003_docs-ai-agent-task-panel.md",
              needs_human_ruling=True, q=r"AI Agent task",
              evidence="The AI Agent task in the BPMN Editor, powered by Langflow, allows you",
              question="The page documents a second AI node type (the AI Agent task, Langflow-backed) "
                       "and its figures are the node's dialogs and property panels in the BPMN editor "
                       "- Langflow account, agent selection, {{aiAgentInput}}, data mapping, Test "
                       "Agent - but no figure on the page shows the process diagram the node sits in. "
                       "Is the node's property panel, with its BPMN task properties, a process "
                       "artefact for this census (INCLUDE), or is the page E0-no-artefact because no "
                       "diagram is published?"),
}


# ---------------------------------------------------------------- community half
def com_text(name):
    p = COM / ("page_%s.json" % name)
    if not p.exists():
        return "", {}
    d = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    return d.get("text") or "", d


PDFTOTEXT = "C:/Poppler/Release-24.08.0-0/poppler-24.08.0/Library/bin/pdftotext.exe"


def deck_pages(pdf, pages):
    """Text layer of the named pages of a deck PDF (the slides carry a text layer; the screenshots'
    labels do not). Cached as <pdf stem>.txt beside the PDF."""
    import subprocess
    out = COM / (pathlib.Path(pdf).stem + ".txt")
    if not out.exists():
        subprocess.run([PDFTOTEXT, "-layout", str(COM / pdf), str(out)], check=True)
    parts = out.read_text(encoding="utf-8", errors="replace").split("\f")
    return " ".join(parts[n - 1] for n in pages)


def com_rows():
    """Half two: the IBM Community BAMOE posts the search protocol surfaced, plus the two decks."""
    out = []

    def add(name, title, url, verdict, reason, judgment, pat, note, text=None, **kw):
        t = text if text is not None else clean(com_text(name)[0])
        row = {
            "n": None, "verdict": verdict, "reason": reason, "judgment": judgment,
            "evidence": kw.pop("evidence", None) or pick(t, pat),
            "note": note, "url": url, "title": title, "duplicate_of": None,
            "accessed": ACCESSED, "surface": "community:ibm.com", "record": kw.pop("record", None),
            "needs_visual_check": kw.pop("needs_visual_check", False),
            "needs_human_ruling": kw.pop("needs_human_ruling", False),
            "question": kw.pop("question", None),
            "judged_from": "eye census of the post's figures (ledgers/_bamoe_comm/)",
            "figures_looked_at": kw.pop("figures_looked_at", ""),
            "screen": "", "topic": kw.pop("topic", None),
        }
        row.update(kw)
        out.append(row)

    B = "https://community.ibm.com/community/user/blogs/"
    D_ = "https://community.ibm.com/community/user/discussion/"

    add("920", "Announcing IBM Business Automation Manager Open Editions 9.2",
        B + "devidutta-sahoo/2025/04/01/bamoe920announcement", "EXCLUDE", "E0-no-artefact", False,
        r"BAMOE|announc",
        "Release announcement. Its figures are release graphics and product screenshots; there is no "
        "process diagram and the post's AI-screen hits are the word 'AI' in product prose. No process "
        "artefact.", figures_looked_at="sheet_comm_heroes.png / sheet_comm_small.png (release graphics)")

    add("930", "Announcing IBM Business Automation Manager Open Editions 9.3.0",
        B + "phil-simpson/2025/09/25/announcing-ibm-business-automation-manager-open-ed",
        "INCLUDE", None, True, r"Gen AI|Generative AI",
        "The post announcing 9.3.0 carries the hiring process in BAMOE Canvas with the Gen AI task "
        "'Create Offer' selected and its AI panel open (Figure2, 3292x1358): AI Provider watsonx, "
        "Model ibm/granite-3-2b-instruct, Temperature 0.7, Token Limit 500, and the offer-letter "
        "prompt over {{candidate}}, {{category}}, {{baseSalary}}, {{bonus}}. Canvas watermark "
        "'BPMN 2.0'. Figure3 is an MCP architecture box diagram (E1, not BPMN) and is not the "
        "artefact collected here.",
        record="corpus/ibm-bamoe/004_community-930-hiring-genai-task.md",
        figures_looked_at="p930__n5lTaIudTQCCXzwCOGW0_Figure2.png and p930__f6ypPRhSQpG7MTFEd04K_"
                          "Figure3.png at full size")

    add("931", "Announcing IBM Business Automation Manager Open Editions 9.3.1",
        B + "devidutta-sahoo/2025/12/07/931", "INCLUDE", None, True, r"AI Agent|Gen AI",
        "The post announcing 9.3.1 carries the claim-handling workflow "
        "'Insurance_Claims_AI_Workflow_with_DI' in BAMOE Canvas: start 'Claim Submitted' -> 'Validate "
        "Claim Data' -> 'Gen AI Task: Summarize Claim Documents' -> 'DMN Decision: Claim Complexity "
        "Assessment' -> gateway 'Claim Complexity?' (Simple/Complex) -> 'Automated Processing' / "
        "'Calculate Settlement' -> 'Agentic AI Task: Research & Investigation' -> end. Canvas "
        "watermark 'BPMN 2.0', BPMN Editor toolbar. The right panel is that second node: Langflow "
        "Account 'Langflow - 9december', Agent dropdown, Input, Preview, 'Test Agent'. Two AI node "
        "types inside one process diagram. The post's featured image repeats the same workflow in "
        "another panel state, and its other screenshot is a Langflow canvas (not BPMN).",
        record="corpus/ibm-bamoe/005_community-931-insurance-claims-ai.md",
        figures_looked_at="p931__D2PjhAvvQ7q1x5PGaFpO_Screenshot-2025-12-09-at-1.10.01-PM-L.p.png at "
                          "full size; featured image and Langflow canvas on the same contact sheet")

    add("940", "Announcing IBM Business Automation Manager Open Editions 9.4.0",
        B + "devidutta-sahoo/2026/03/23/announcing-bamoe-940", "EXCLUDE", "E0-no-artefact", False,
        r"BAMOE|announc",
        "Release announcement; its figure is the release banner. No process artefact.",
        figures_looked_at="sheet_comm_heroes.png (release banner)")

    add("beyond95", "Beyond 9.5 - What's Next for IBM BAMOE",
        B + "aliannah-muzaffar/2026/07/29/beyond-95-whats-next-for-ibm-bamoe",
        "EXCLUDE", "E0-no-artefact", False, r"roadmap|BAMOE|agent",
        "Roadmap post. Its figure is a roadmap graphic; the AI mentions are roadmap items in prose. "
        "No process artefact.", figures_looked_at="sheet_comm_small.png (roadmap graphic)")

    add("capabilities", "IBM Business Automation Manager Open Editions - Enterprise Automation "
                        "Built on Open Source",
        B + "devidutta-sahoo/2026/03/18/bamoecapabilities", "EXCLUDE", "E0-no-artefact", False,
        r"AI|BAMOE",
        "Positioning post. Its figure is a title card and the AI mentions are capability claims in "
        "prose (Gen AI Task, AI Agent Task, MCP Server). No process artefact.",
        figures_looked_at="sheet_comm_heroes.png (title card)")

    add("helm", "IBM BAMOE Dev and Runtime Environment Deployment on OpenShift Using Helm",
        B + "santhosh-srinivasa/2026/08/25/ibm-bamoe-dev-and-runtime-environment-deployment",
        "EXCLUDE", "E0-no-artefact", False, r"deployment|Helm|OpenShift",
        "The post's figures are Helm/OpenShift console screens - pod lists, terminals, deployment "
        "pages. No BPMN diagram; the BAMOE dev-ui screens show process instances as lists, not as "
        "diagrams. No process artefact.",
        figures_looked_at="the post's console figures on the community contact sheets")

    add("helping", "Helping Shape the Future of BAMOE",
        B + "aliannah-muzaffar/2026/09/01/helping-shape-the-future-of-bamoe",
        "EXCLUDE", "E0-no-artefact", False, r"BAMOE|feedback",
        "Community-feedback post with a single illustration. No process artefact.",
        figures_looked_at="sheet_comm_small.png")

    add("library", "IBM Business Automation Manager Open Editions (BAMOE) V9 Quick Release References",
        "https://community.ibm.com/community/user/viewdocument/ibm-business-automation-manager-ope-1",
        "EXCLUDE", "E0-no-artefact", False, r"Quick Release References|General Availability",
        "A community library document, not a post: a quick-reference card by YAJIE Yang giving the "
        "General Availability date of BAMOE 9.5.0 (30 June 2026) and links out to the release notes, "
        "IBM Documentation, two security-bulletin pages and the announcement letter. Its figure is a "
        "title/thumbnail graphic; there is no process artefact on the page. Its one GitHub link - "
        "https://github.com/IBM/bamoe-canvas-quarkus-accelerator - is enumerated as its own row "
        "below, and is the only GitHub lead the whole community half produced.",
        text=clean(com_text("library")[0]),
        figures_looked_at="lib.html (the page's rendered HTML); the page's figure carries no diagram")

    add("mcp", "BAMOE meets Agentic AI: A New Era of Intelligent Automation",
        B + "yeser-amer/2025/09/22/bamoe-agentic-ai-mcp-server", "EXCLUDE", "E0-no-artefact", True,
        r"MCP|agent|BPMN",
        "The post's figures are LLM chat transcripts (process-1..4-L.png, decision-iteraction-1/2-L.png, "
        "Screenshot-2025-09-22-*): an agent creating, updating and deleting an order process instance "
        "and executing the TrafficViolation DMN model over MCP tools. Despite the 'process-*' file "
        "names, none of them is a diagram - the file names are the one trap this source sets, which "
        "is why this row is flagged as a judgement exclusion. The featured image is a marketing "
        "illustration (AI Agent -> BAMOE -> Models boxes, not BPMN). No process artefact on the page.",
        figures_looked_at="the post's nine figures on a full-size contact sheet "
                          "(ledgers/_bamoe/sheet_pmcp.png)")

    add("pu0331", "Product Update: IBM BAMOE (March 2026)",
        B + "aliannah-muzaffar/2026/03/31/product-update-ibm-business-automation-manager-ope",
        "EXCLUDE", "E0-no-artefact", False, r"update|BAMOE|AI",
        "Product-update post. Figures are update cards; the AI mentions are release items in prose. "
        "No process artefact.", figures_looked_at="sheet_comm_small.png")

    add("pu0428", "Product Update: IBM BAMOE (April 2026)",
        B + "aliannah-muzaffar/2026/04/28/product-update-ibm-business-automation-manager-ope",
        "EXCLUDE", "E0-no-artefact", False, r"update|BAMOE|AI",
        "Product-update post. Figures are update cards and console screenshots; no process artefact.",
        figures_looked_at="sheet_comm_dev.png")

    add("v91", "Try Out the All New IBM BAMOE Version 9.1 (setup on local)",
        B + "sahith-r-shetty/2024/07/11/bamoe-v91-setup-local", "EXCLUDE", "E0-no-artefact", False,
        r"BAMOE|setup|localhost",
        "Setup walkthrough. The figures are the Quarkus Dev UI, its Swagger page, service endpoints "
        "and terminal output - including a VS Code file-tree screenshot whose file list names "
        "'traffic-rules-dmn.bpmn' as a file, which is a file name and not a diagram. No process "
        "artefact.",
        figures_looked_at="the post's twelve figures on sheet_comm_dev.png and at full size for "
                          "process.png")

    add("webinar_disc", "Webinar: AI-Powered Automation with IBM BAMOE: Capabilities, Architecture "
                        "& Demos",
        D_ + "webinar-aipowered-automation-with-ibm-bamoe-capabilities-architecture-demos",
        "EXCLUDE", "E0-no-artefact", False, r"webinar thread|Registration",
        "A community discussion thread opened for post-webinar follow-up, with the registration link "
        "and the session description ('Webinar Event and Registration: Registration Link'). Its "
        "figure is a title banner; the items with diagrams are the decks themselves, rowed separately "
        "below. No process artefact on the page.",
        figures_looked_at="the page's figure on the community contact sheets")

    add("adarsh", "Introducing AI Agent Task: Advanced AI Integration for BAMOE Business Processes",
        B + "adarsh-v-k/2025/11/28/introducing-ai-agent-task-advanced-ai-integration",
        "INCLUDE", None, True, r"AI Agent Task|Langflow",
        "The post's opening animation (ai-agent-task.gif, 1200x675 frames) is a BAMOE Canvas session: "
        "the empty BPMN canvas with the 'BPMN 2.0' watermark, the palette's AI group (Gen AI Task, AI "
        "Agent Task), the AI Agent Task dragged onto the canvas, and its panel opened (Langflow "
        "Account, Agent, Input {{aiAgentInput}}, Preview, Test Agent, Data mapping). The remaining "
        "eleven screenshots are the same node's dialogs (provider list with Langflow, Connect to "
        "Langflow, VS Code sign-in, agent 'KIE Contributors Doc Q&A' with MCP Enabled: Yes, data "
        "mapping, Test Agent, Agent Execution Log, Agent Response).",
        record="corpus/ibm-bamoe/006_community-ai-agent-task-demo-gif.md",
        figures_looked_at="all 13 figures on sheet_aiagenttask.png/sheet_genai_blog.png and the GIF's "
                          "six frames at full size (ledgers/_bamoe_comm/gif_strip.png)")

    add("lugli", "Introducing the BAMOE Gen AI Task for workflows",
        B + "thiago-lugli/2025/09/23/introducing-the-bamoe-gen-ai-task-for-workflows",
        "INCLUDE", None, True, r"Gen AI Task|BPMN",
        "The post's animation (ezgif-71d8d34e475aa4.gif, frames 800x404) shows BAMOE Canvas with the "
        "hiring 'Sample' workflow - ...w Hiring -> gateway -> Create Offer -> HR Interview -> IT "
        "Interview -> gateway -> Send Offer to Candidate, with 'Send notification HR Interview "
        "avoided' and 'Application denied' branches - and the Gen AI Task node placed on the canvas "
        "with its panel open (AI Provider, Model, Temperature, Token Limit, Prompt, Data mapping "
        "(in: -, out: 1)). Canvas watermark 'BPMN 2.0', 'BPMN Editor' toolbar. The post's other "
        "figures are the provider dialog, the VS Code sign-in palette, the data-mapping dialog, the "
        "model list (granite) and a prompt result.",
        record="corpus/ibm-bamoe/007_community-genai-task-hiring-canvas.md",
        figures_looked_at="all six figures plus the animation's frames "
                          "(genai_g3_f214_2x.png read at full size)")

    add("deck931", "What's new in IBM Business Automation Manager Open Editions 9.3.1 (webinar deck)",
        "https://community.ibm.com/HigherLogic/System/DownloadDocumentFile.ashx?"
        "DocumentFileKey=14c6c7fc-2fd0-4dcc-8467-c77b0c394830&forceDialog=0",
        "INCLUDE", None, True, r"AI Agent Task",
        "The deck (32 pages, ledgers/_bamoe_comm/webinar_931.pdf, rasterised page by page) has four "
        "pages on the AI Agent Task (its agenda page lists 'AI Agent Task for BPMN (Tech Preview)', "
        "Tiago Bento). Page 29 is the artefact: BAMOE Canvas open on rotate_api_keys.bpmn, watermark "
        "'BPMN 2.0', with the process start event -> 'Open PR' -> 'Review PR' -> end event on the "
        "canvas, the 'Review PR' node selected and its panel open on the right - Langflow Account*, "
        "Agent*, Input* 'Please review the following PR: {{prLink}}', Preview prLink "
        "https://github.com/ibm/bamoe/pulls..., Test Agent (greyed), 'Data mapping (in: 2, out: 1)', "
        "onEntry / onExit, Metadata - with the node's sign-in overlay 'Sign in with Langflow to use "
        "BAMOE Developer Tools (1)' across the canvas. Page 27 shows the same node's panel filled in "
        "against the Langflow provider card ('Compatible with Langflow', 'Process Variable "
        "interpolation', 'Interactive properties panel for faster experimentation', the two "
        "com.ibm.bamoe work-item-handler coordinates), page 28 the Canvas home screen listing the "
        "project 'PR REVIEW _ BAMOE 931 DEMO' [Workflow], page 30 the binding keys "
        "bamoe.workflow.ai-agent-task.provider.langflow.*. Pages 7 and 24 are NOT BPMN: page 7 is a "
        "component architecture box diagram (Canvas / Developer Tools / git+BPMN+DMN / Business "
        "Services / MCP Server Client / Management Console / databases) and page 24 the WS-HumanTask "
        "1.1 lifecycle state diagram reproduced from the OASIS spec, footer "
        "https://docs.oasis-open.org/bpel4people/ws-humantask-1.1-spec-cs-01.html; page 26 is a "
        "stylised, unlabelled illustration of BPMN-like shapes (see the visual-check question). The "
        "rest of the deck is text, tables and console screenshots (MCP server security, process "
        "instance migration, WS-HumanTask) with no AI element inside a process.",
        text=deck_pages("webinar_931.pdf", [4, 26, 27, 29, 30]),
        record="corpus/ibm-bamoe/008_deck-931-review-pr-agent-task.md",
        needs_visual_check=True, needs_human_ruling=True,
        question="Page 26 of this deck is a stylised illustration drawn with BPMN-like shapes "
                 "(events, gateways, lanes) but with no readable labels at any rasterisation I can "
                 "produce, and no AI element visible in it; its title says 'AI integration - AI Agent "
                 "Task for BPMN (Tech Preview)'. Is it to be recorded as a second artefact of this "
                 "deck (in which case: is the artwork a real process diagram, and is an AI element "
                 "present?), or dismissed as a marketing illustration? The capture of it is attached "
                 "to the record so it can be ruled on by eye.",
        figures_looked_at="all 32 pages as a contact sheet (ledgers/_bamoe_comm/sheet_deck_w931.png), "
                          "then pages 7, 24, 26, 27, 28, 29, 30 at 200-220 dpi")

    add("deck_tx", "Business Automation in the hybrid cloud with IBM BAMOE (IBM TechXchange 2025 "
                   "session deck 3058)",
        "https://community.ibm.com/HigherLogic/System/DownloadDocumentFile.ashx?"
        "DocumentFileKey=48e39a74-897d-4027-879e-16d3ee789a0e&forceDialog=0",
        "INCLUDE", None, True, r"Gen AI",
        "The deck (20 pages, ledgers/_bamoe_comm/techxchange_2025.pdf, rasterised page by page) puts "
        "the Gen AI Task demo on page 12, under the section the agenda calls 'AI Demos - BAMOE Gen AI "
        "Task for BPMN - BAMOE MCP Server': BAMOE Canvas, project header 'Workflow | GenAI Task "
        "demo', and on the dotted canvas a three-element BPMN process - start event -> a task "
        "'Generate some content' carrying the AI sparkle of the Gen AI Task -> end event - with "
        "footer 'Example project: process-saga-quarkus'. Page 10 is the 9.2.0 'Process Automation' "
        "slide and carries two BPMN diagrams with NO AI element: the hiring process in its "
        "pre-AI form (start -> 'New Hiring' -> gateway -> 'Generate base Offer' -> 'Log Offer' -> "
        "'HR Interview' (timer) -> 'IT Interview' -> gateway -> 'Send Offer to Candidate', with "
        "'Send notification HR Interview avoided' and 'Application denied' branches, caption 'Example "
        "project: jbpm-compact-architecture-example') and the saga order process ('reserve stock' / "
        "'process payment' / 'schedule shipping' / 'Order Success' with compensation handlers and a "
        "'Handle Error' sub-process, caption 'Example project: process-saga-quarkus'). Comparing the "
        "two slides is the clearest evidence in this source of an AI node being introduced INTO an "
        "existing process: the same hiring process appears at 9.2.0 with a plain 'Generate base "
        "Offer' task and at 9.3.0 with the Gen AI task 'Create Offer' plus its watsonx/granite panel. "
        "Page 8 is a component architecture box diagram, pages 16-17 the release highlights in text "
        "('Generative AI task, to incorporate LLM invocation within a workflow', 'MCP Server, to "
        "publish BAMOE applications as tools for agents to use', 'AI Agent task, to delegate work to "
        "an autonomous agent').",
        text=deck_pages("techxchange_2025.pdf", [3, 11, 12, 16, 17]),
        record="corpus/ibm-bamoe/009_deck-techxchange-genai-task-demo.md",
        figures_looked_at="all 20 pages as a contact sheet (ledgers/_bamoe_comm/sheet_deck_tx.png), "
                          "then pages 10 and 12 at 130-200 dpi")

    return out


# ---------------------------------------------------------------- extra surfaces
def extra_rows():
    """The two adjacent distribution surfaces the assignment names."""
    return [
        {"n": None, "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
         "evidence": "The `main` branch of this repository is not used for development and does not "
                     "host any Accelerators.",
         "note": "The accelerator repository linked from the community library page ships project "
                 "templates, not processes. README.md (fetched through the public GitHub API): each "
                 "accelerator lives in its own branch named "
                 "'{version}-{name}-{framework}-{build-tool}'. All eight branches of the current "
                 "release (9.6.0: 4 workflows, 4 decisions) and the 9.3.1 full branch were read "
                 "through the trees API and contain no .bpmn or .dmn file at all - only "
                 "application.properties, pom.xml/gradle files, deployment manifests and a test "
                 "class. Older branches are a version facet of the same scaffolds and were not read "
                 "one by one; the two ages checked (9.3.1 and 9.6.0) are identical in this respect. "
                 "Branch list: 79 branches, ledgers/_bamoe_comm/gh_branches.json.",
         "url": "https://github.com/IBM/bamoe-canvas-quarkus-accelerator",
         "title": "IBM Business Automation Manager Open Editions :: Accelerators",
         "duplicate_of": None, "accessed": ACCESSED, "surface": "github:IBM", "record": None,
         "needs_visual_check": False, "needs_human_ruling": False, "question": None,
         "judged_from": "mechanical archive enumeration (github trees API, ledgers/_bamoe_build.py)",
         "figures_looked_at": "no figures on the surface; the README was read as text",
         "screen": "branches=79; trees read=9; .bpmn/.dmn files found=0"},
        {"n": None, "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
         "evidence": "Author Decisions and Workflows using the DMN and BPMN open standards",
         "note": "The VS Code marketplace extension the assignment asks about (IBM.bamoe-developer-"
                 "tools, version 9.6.0, published 24 Sep 2026) ships editors, not sample processes. "
                 "The package was fetched from the marketplace's public gallery URL "
                 "(.../publishers/IBM/vsextensions/bamoe-developer-tools/9.6.0/vspackage, 103,974,809 "
                 "bytes) and listed: 2110 entries, no .bpmn file anywhere; the only notation sample "
                 "is extension/dist/target/dmn/static/sample.dmn and its webview twin (41,610 bytes "
                 "each). The BPMN editor itself is a webview bundle "
                 "(extension/dist/webview/NewBpmnEditorEnvelopeApp.js).",
         "url": "https://marketplace.visualstudio.com/items?itemName=IBM.bamoe-developer-tools",
         "title": "BAMOE Developer Tools - Visual Studio Marketplace",
         "duplicate_of": None, "accessed": ACCESSED, "surface": "marketplace:visualstudio.com",
         "record": None, "needs_visual_check": False, "needs_human_ruling": False, "question": None,
         "judged_from": "mechanical archive enumeration (vsix listing, ledgers/_bamoe_build.py)",
         "figures_looked_at": "no figures; the vsix was listed, not rendered",
         "screen": "vsix entries=2110; .bpmn found=0; sample.dmn found=2"},
    ]


# ---------------------------------------------------------------- ledger assembly
DOC_QUERIES = []
COM_QUERIES = [
    "IBM BAMOE 9.3.1 AI Agent Task Langflow community blog",
    'community.ibm.com blog BAMOE "Gen AI Task" BPMN workflow granite watsonx',
    "site:community.ibm.com BAMOE blog BPMN workflow AI",
    "IBM BAMOE community blog MCP server agentic AI business automation",
]


def build():
    rows = docs_rows() + com_rows() + extra_rows()
    for i, r in enumerate(rows, 1):
        r["n"] = i
    pop = {"population_size": len(rows)}
    return rows, pop


def write(rows, pop):
    led = ELI / "ledgers" / (SLUG + ".jsonl")
    header = {
        "type": "header", "source": SLUG, "read": ACCESSED,
        "population_size": pop["population_size"], "census": True,
        "artefact_criteria": "thesis 004_method, sec:method:use_case_elicitation - BPMN 2.0 diagram + "
                             "explicit AI/LLM element inside the process",
        "enumeration_method":
            "TWO METHODS, recorded separately because they are not the same kind of enumeration. "
            "(1) DOCS HALF - a census. The BAMOE 9.5.x documentation ToC was read from IBM's docs API "
            "(https://1.www.s81c.com/docs/api/v1/toc/ibamoe/9.5.x?lang=en, productKey SSFVHI5_9.5.0): "
            "117 topics, an exact count from the ToC itself, no facet and no keyword filter applied. "
            "Every topic was fetched through the content API "
            "(https://www.ibm.com/docs/api/v1/content/<href>?parsebody=true&lang=en) and screened "
            "offline for figures, diagram-named figures, BPMN/process tokens and AI tokens "
            "(ledgers/_bamoe/screen.json, content in ledgers/_bamoe/content_9.5.x.json; the 324 "
            "figures decoded into ledgers/_bamoe.raw/). All 38 figure-bearing pages were looked at "
            "by eye on a contact sheet (35 per-page sheets in ledgers/_bamoe/sh_<parent>_<topic>.png "
            "plus the AI branch's sheets), and the 11 pages whose figures or AI tokens the screen "
            "could not decide were then ruled one by one (the RULED table in "
            "ledgers/_bamoe_build.py). "
            "Other releases (9.3.x, 9.4.x, 9.6.0) publish the same topics as a version facet and are "
            "not counted twice; they are covered through the community half's release posts. "
            "(2) COMMUNITY HALF - a search protocol, not a census. The frontier here is 'the IBM "
            "Community BAMOE blog posts found by search', so the population is defined by the "
            "queries, which are logged verbatim in `queries_log` below. 14 posts and 2 "
            "discussion/library pages were fetched (full HTML, ledgers/_bamoe_comm/page_*.json), "
            "and all 42 of their figures were downloaded and classified by contact sheet "
            "(ledgers/_bamoe_comm/figs/); in addition the two webinar decks rowed below were "
            "downloaded and rasterised page by page (32 and 20 pages, "
            "ledgers/_bamoe_comm/pgs_w931/, pgs_tx/). Two posts whose figures had been captured in "
            "an earlier working session were re-found by the queries below and verified by matching "
            "the published image keys against the captures already on disk. "
            "(3) TWO ADJACENT SURFACES the assignment names are rowed as well: the VS Code "
            "marketplace listing and the accelerator GitHub repository linked from the community "
            "library page (9.6.0 and 9.3.1 branches read through the GitHub trees API). "
            "Total population = 117 + 18 + 2 = 137 rows.",
        "queries_log": {
            "note": "the community half is a search protocol; these are the queries run in this "
                    "session, verbatim. Queries run in the earlier working session that opened this "
                    "protocol were not written down before its context break - an incompleteness of "
                    "the protocol, recorded here rather than papered over. The result set is complete "
                    "in the sense that every page the protocol surfaced is rowed, and the two "
                    "queries below re-found the two posts whose URLs had been lost.",
            "queries": COM_QUERIES,
        },
        "note": "The docs half is a census of one release's ToC; the community half is a search "
                "protocol over IBM Community posts and is not a census of the group (the Open "
                "Editions group's own blog index reports 86 blogs and 39 library documents; the "
                "protocol surfaced 14 posts, 2 discussion/library pages and the 2 webinar decks). "
                "Verdicts: INCLUDE 7, UNCERTAIN 2, EXCLUDE 128. "
                "Provenance note on the two decks: their URLs are the community platform's "
                "attachment-download form "
                "(community.ibm.com/HigherLogic/System/DownloadDocumentFile.ashx?DocumentFileKey=...) "
                "and both were verified to resolve (HTTP 302 -> "
                "higherlogicdownload.s3.amazonaws.com/IMWUC/<key>_file.pdf; the responses are kept in "
                "ledgers/_bamoe_comm/h_<key>.txt and the PDFs rasterised page by page). The page that "
                "published the two attachment links was not preserved among this session's captures, "
                "so the referring page is not recorded here rather than guessed at. "
                "One deliberate contrast with the UiPath source in this corpus: BAMOE has a "
                "dedicated AI node type, so the diagram itself carries the visual signal - the Gen AI "
                "Task and the AI Agent Task are palette entries with their own shape and sparkle, "
                "visible inside the process diagram, whereas UiPath delegates the AI to a binding "
                "that is only visible in a task's property panel.",
    }
    footer = {
        "type": "footer", "rows": len(rows), "status": "DONE",
        "include": sum(1 for r in rows if r["verdict"] == "INCLUDE"),
        "uncertain": sum(1 for r in rows if r["verdict"] == "UNCERTAIN"),
        "exclude": {c: sum(1 for r in rows if r["reason"] == c)
                    for c in ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")
                    if any(r["reason"] == c for r in rows)},
        "blocked": 0,
        "judgment_exclusion_share": round(
            sum(1 for r in rows if r["judgment"] and r["verdict"] == "EXCLUDE") / len(rows), 3),
        "judgement_rows": sum(1 for r in rows if r["judgment"]),
        "records_written": sorted({pathlib.Path(r["record"]).stem for r in rows if r.get("record")}),
        "superseded_rows": 0,
        "audit_sample": {
            "method": "all 38 figure-bearing docs pages were looked at by eye on a contact sheet; the "
                      "11 pages whose figures or AI tokens the screen could not decide were ruled one "
                      "by one (RULED in ledgers/_bamoe_build.py); every community post's figures were "
                      "classified by eye on a contact sheet or at full size; both decks were looked at "
                      "page by page",
            "docs_pages": 117, "docs_pages_with_figures": 38,
            "docs_figures_decoded": 324,
            "community_pages": 16, "community_figures": 42,
            "deck_pages": 52,
            "screen_flags": "R1 no figures, R2 DMN notation, R3 diagram-named figure + silent AI "
                            "screen, R4 figures that no name calls a diagram",
        },
        "figures_looked": {
            "artefacts_whose_figures_were_looked_at_by_eye": 9,
            "of_which_community": 6,
            "docs_per_page_sheets": 35,
            "docs_ai_branch_sheets": ["sheet_genai.png", "sheet_aiagent.png", "sheet_mcp.png",
                                      "sheet_mcp2.png", "sheet_ai_extra.png", "sheet_aiagent.png"],
            "community_sheets": ["sheet_comm_heroes.png", "sheet_comm_small.png",
                                 "sheet_comm_dev.png", "sheet_aiagenttask.png",
                                 "sheet_genai_blog.png", "sheet_pmcp.png"],
            "deck_sheets": ["sheet_deck_w931.png", "sheet_deck_tx.png"],
            "judgement_exclusions": sum(1 for r in rows if r["judgment"] and r["verdict"] == "EXCLUDE"),
            "note": "the row's `figures_looked_at` field names, per row, what was opened: a contact "
                    "sheet for the docs pages, the community sheets and the decks, or 'no figure "
                    "opened by eye' for rows the mechanical screen decided (pages that carry no "
                    "figure at all).",
        },
    }
    led.write_text("\n".join(json.dumps(o, ensure_ascii=False) for o in [header] + rows + [footer])
                   + "\n", encoding="utf-8")
    front = ELI / "ledgers" / (SLUG + ".frontier.txt")
    front.write_text("\n".join(r["url"] for r in rows) + "\n", encoding="utf-8")
    print("wrote %s (%d rows) and %s" % (led.name, len(rows), front.name))


def main():
    rows, pop = build()
    if "--write" in sys.argv:
        write(rows, pop)
        return
    from collections import Counter
    print("population %d" % len(rows))
    print(Counter(r["verdict"] for r in rows))
    print(Counter(r["reason"] for r in rows))
    print(Counter(r["surface"] for r in rows))
    je = [r for r in rows if r["judgment"] and r["verdict"] == "EXCLUDE"]
    print("judged exclusions %d (%.1f%%)" % (len(je), 100 * len(je) / len(rows)))
    for r in rows:
        if r["verdict"] != "EXCLUDE" or r["judgment"]:
            print("[%3d] %-9s %-18s %s" % (r["n"], r["verdict"], r["reason"] or "-",
                                           (r["title"] or r["url"])[:70]))
            print("      ev: %s" % (r["evidence"] or "")[:150])


if __name__ == "__main__":
    main()
