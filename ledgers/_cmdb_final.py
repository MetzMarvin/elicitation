"""camunda-docs-blog: the final disposition of every frontier item, from the evidence on disk.

Inputs, all of them produced by earlier steps and re-runnable:
  ledgers/camunda-docs-blog.raw/blog/NNNN.html      the fetched page (fetched 2026-09-26)
  ledgers/camunda-docs-blog.raw/screen.jsonl        the screen of that page (DOM text, alts, links)
  ledgers/camunda-docs-blog.raw/viz/report_*.txt    the visual pass over the contact sheets,
                                                    one line per cell: n.k | class | ai_visible | note
  ledgers/camunda-docs-blog.frontier.txt            the frozen population (1439 items)

Decision rule (recorded in the ledger header):
  A. item 1436-1439 (docs entry points the host refuses)          -> BLOCKED
  B. post links a .bpmn/.dmn/.cmmn model                          -> judged from the XML
  C. post shows no figure at all                                  -> E0-no-artefact
  D. figures exist, none of them a diagram (visual pass)           -> E0, or E1 if one is a
                                                                     non-BPMN diagram
  E. a BPMN diagram is shown and the page carries no AI/LLM term    -> E2-no-ai-element
  F. a BPMN diagram is shown and the page carries AI/LLM terms      -> the AI judgement:
       an AI element bound to a process element  -> INCLUDE (record)
       AI only as tooling around the diagram     -> E2-no-ai-element
       neither, or the visual could not settle it -> UNCERTAIN (record + question)

Usage
  python ledgers/_cmdb_final.py plan [-v]     # classify everything, print, write nothing
  python ledgers/_cmdb_final.py apply         # append the rows to raw/dips.jsonl
  python ledgers/_cmdb_final.py why N         # why one item got the row it got
"""
import collections, glob, json, os, re, sys

import _cmdb_aijudge as A
import _cmdb_figs as F

RAW = "ledgers/camunda-docs-blog.raw"
VIZ = os.path.join(RAW, "viz")
DIPS = os.path.join(RAW, "dips.jsonl")
FRONTIER = "ledgers/camunda-docs-blog.frontier.txt"
# frontier items already written up as corpus records
DONE = {1274: "corpus/camunda-docs-blog/001_song-requests.md",
        300: "corpus/camunda-docs-blog/002_ai-task-agent-visibility.md"}
# ... and every record the generator has written since (records.json is its manifest)
_manifest = os.path.join(RAW, "records.json")
if os.path.exists(_manifest):
    with open(_manifest, encoding="utf-8") as _fh:
        DONE.update({int(k): v for k, v in json.load(_fh).items()})

RANK = {"bpmn": 5, "other-diagram": 4, "unclear": 3, "screenshot": 2, "chart": 1, "photo": 0, "card": 0}
NOTATION = [
    (r"(?i)flow ?chart", "a flow chart"),
    (r"(?i)architecture|layer|tier|topology|component|stack|product house", "an architecture diagram"),
    (r"(?i)timeline|roadmap|maturity|gantt", "a timeline"),
    (r"(?i)chart|graph|plot|bars?|axis|histogram|donut", "a chart"),
    (r"(?i)table|matrix|list", "a table"),
    (r"(?i)screenshot|ui|dashboard|console|panel|form|wizard|dialog", "a product-UI screenshot"),
    (r"(?i)logo|portrait|photo|headshot|stage|audience|people|banner", "a photograph or brand card"),
]
STRUCT = re.compile(r"(?i)\b(bpmn|process model|process diagram|ad-?hoc sub-?process|sub-?process|"
                    r"gateway|service task|user task|business rule task|script task|pool|lane|"
                    r"modeler|sequence flow|process instance|event sub-?process)\b")
# the visual pass's own words for "I could not read the labels", i.e. the AI call on the
# artefact itself cannot rest on that cell
UNREAD = re.compile(r"(?i)unreadable|illegible|not legible|cannot read|too small|too tiny|"
                    r"blurry|blurred|faint|cut off|partially visible")
# A cell the contact sheet classed as an application window (Modeler, Operate, Optimize,
# Tasklist) can still hold the process diagram itself. E0 is "the item contains no process
# artefact at all" (pricing page, login form, empty listing), and a window showing a process
# model is not that: the page shows the artefact through the vendor's own UI. So a
# window-classed cell whose note names both a visual surface and process structure is judged
# as a diagram, with the note quoted as the evidence for that reading. A note saying the
# window holds no diagram (or no process) is left to E0.
SCREENS = ("screenshot", "chart", "photo", "card")
DRAWW = re.compile(r"(?i)\b(diagram|canvas|modeler|modeller|heat ?map|heatmap|inset|"
                   r"process (view|map|canvas)|bpmn\.io|cockpit|operate|optimize|tasklist|"
                   r"report page)\b")
PROCW = re.compile(r"(?i)\b(bpmn|process|pool|lane|gateway|sub-?process|task|tasks|activity|"
                   r"activities|event|events|flow node|sequence flow)\b")
NEGW = re.compile(r"(?i)\b(no|not|without|none|absent|empty)\b[^.]{0,30}?"
                  r"\b(diagram|process|bpmn|canvas|model|shapes?|tasks?)\b")


def visual():
    """(n -> best class, n -> set of ai_visible values, n.k -> (class, ai_visible, note))"""
    cls, aiv, vnt = {}, {}, {}
    for p in sorted(glob.glob(os.path.join(VIZ, "report_*.txt"))):
        for line in open(p, encoding="utf-8", errors="replace"):
            m = re.match(r"\s*(\d+)\.(\d+)\s*\|\s*([a-z][a-z-]*)\s*\|\s*(yes|no|unclear)\s*\|(.*)",
                         line)
            if not m:
                continue
            n, k, c, a = int(m.group(1)), m.group(2), m.group(3), m.group(4)
            if RANK.get(c, -1) > RANK.get(cls.get(n, ""), -1):
                cls[n] = c
            aiv.setdefault(n, set()).add(a)
            vnt["%d.%s" % (n, k)] = (c, a, m.group(5).strip())
    return cls, aiv, vnt


def notes_for(n, vnt):
    """The report notes for post n's cells, in cell order."""
    out = []
    for k in ("1", "2", "3"):
        if "%d.%s" % (n, k) in vnt:
            out.append(vnt["%d.%s" % (n, k)])
    return out


def altquote(alt):
    """The figure's own alt text, verbatim: it is page material (the img alt attribute) and
    the strongest textual evidence a picture-only post has. No prefix is added - the ledger's
    `evidence` field must be a verbatim quote, not a citation of one."""
    return " ".join(alt.split()[:25]) if alt else ""


def first_sentence(text):
    for line in text.split("\n"):
        line = " ".join(line.split())
        if len(line) >= 40 and not line.startswith("Read more"):
            return " ".join(line.split()[:25])
    return " ".join(text.split()[:25])


AIPAT = re.compile(r"(?i)(?:\bai\b|\bllm\b|gpt|openai|anthropic|claude|bedrock|vertex|gemini|"
                   r"hugging\s?face|comprehend|textract|\bagent\b|\bcopilot\b)")
TMPL = re.compile(r'zeebe:modelerTemplate="([^"]*)"')
ELNAME = re.compile(r'<bpmn:(?:serviceTask|userTask|task|scriptTask|businessRuleTask|'
                    r'callActivity|subProcess|receiveTask|sendTask)\b[^>]*\bname="([^"]*)"')


def model_files(n):
    return sorted(glob.glob(os.path.join(RAW, "bpmn", "%04d_*" % n)))


def model_verdict(r, cls=None):
    """A post that links a downloadable model: the model's own XML settles the call.
    Returns None when no model was downloaded, or when the model is not BPMN and the page
    shows a BPMN diagram of its own - the figure route judges that one."""
    got = [f for f in r["files"] if re.search(r"\.(bpmn|dmn|cmmn)(\?.*)?$", f, re.I)]
    paths = model_files(r["n"])
    if not got or not paths:
        return None
    names, tmpls, nonbpmn, hits, verb = [], set(), [], [], []
    for p in paths:
        xml = open(p, encoding="utf-8", errors="replace").read()
        if p.lower().endswith(".dmn"):
            nonbpmn = True
        # every XML here has at least one id=, so the row always has a verbatim run to quote
        for m in re.finditer(r'(?:process|decision|definitions|collaboration)\s+id="([^"]+)"',
                             xml, re.I):
            verb.append('id="%s"' % m.group(1))
        first_id = re.search(r'id="([^"]+)"', xml)
        verb.append('id="%s"' % first_id.group(1) if first_id else "")
        for nm in ELNAME.findall(xml):
            names.append(nm)
            verb.append('name="%s"' % nm)
            if AIPAT.search(nm):
                hits.append('name="%s"' % nm)
        for t in TMPL.findall(xml):
            tmpls.add(t)
            verb.append('zeebe:modelerTemplate="%s"' % t)
            if AIPAT.search(t):
                hits.append('zeebe:modelerTemplate="%s"' % t)
    base = os.path.basename(paths[0])
    # the row's evidence has to be a verbatim run of the model's own XML, not a summary of it
    quote = hits[0] if hits else next((v for v in verb if re.search(r"modelerTemplate=", v)),
                                     verb[0] if verb else "")
    ev = ("linked model %s: connector element templates %s; task names %s"
          % (base, sorted(tmpls) or "none", ", ".join(names[:6]) or "none"))
    if hits:
        return ("INCLUDE", "", True, hits[0],
                "the model the page links carries an AI-bound element, read from its XML - "
                "linked model %s" % ev, False, "")
    if nonbpmn:
        if cls is not None and cls.get(r["n"]) == "bpmn":
            return None  # the page shows a BPMN diagram of its own: let the figure route run
        return ("EXCLUDE", "E1-not-bpmn", True, quote,
                "the model the page links is a DMN decision model, not BPMN 2.0 notation - "
                "its XML, quoted above, is %s; page's own diagram left to the figure route" % ev,
                False, "")
    return ("EXCLUDE", "E2-no-ai-element", False, quote,
            "the BPMN model the page links contains no AI/LLM element; its XML reads %s" % ev,
            False, "")


# ---------------------------------------------------------------------------
# Rulings made by reading the page, where the lexicon's mechanical match is not the
# whole story. Each entry: (verdict, reason, judgment, evidence, note, needs_visual,
# question, capture hint). The evidence is a verbatim page line of <=25 words.
# ---------------------------------------------------------------------------
RULED = {
    9: ("INCLUDE", "", True,
        "In the simple BPMN example below, you can see a service task that accesses an AI"
        " engine to read a customer request",
        "the page names a service task that accesses an AI engine and shows the BPMN model "
        "it refers to; the OpenAI Connector is also named in the same section", True, None,
        "figure 2 (bpmn cell, alt 'Connectors-ai')"),
    18: ("INCLUDE", "", True,
         "the heatmap can display the average time each trivia game spends at a specific"
         " task, in this case getting a hint from OpenAI",
         "the BPMN model shown in Optimize contains a task that calls OpenAI, named in the "
         "page text; the diagram's own labels are not legible in the thumbnail", True, None,
         "figure 1 (bpmn cell, alt 'Trivia-task-analysis-optimize')"),
    59: ("EXCLUDE", "E2-no-ai-element", True,
         "There is a native OpenAI Connector you can use while building your process models",
         "the AI mention refers to Camunda's connector library as a capability, not to an "
         "element of the BPMN symbols figure the page shows", False, None, "none"),
    98: ("INCLUDE", "", True,
         "a machine learning model runs using our Hugging Face Connector that will take the"
         " following inputs:",
         "the BPMN model shown calls a Hugging Face model (roberta-base-go_emotions) and "
         "branches on its confidence score; the figures have no alt text at all", True, None,
         "figure 1 (bpmn cell, 1024x333, no alt)"),
    248: ("INCLUDE", "", True,
          "An OpenAI bot checks the data provided for any indication of fraud. The AI bot will"
          " determine which tasks, from a list of tasks, to perform",
          "the guide's own figure is 'A BPMN model of an AI agent in an ad-hob sub-process using"
          " Camunda.' - an OpenAI-bound agent inside a fraud-detection process", True, None,
          "figure 1 (bpmn cell, gif, alt 'A BPMN model of an AI agent in an ad-hob sub-process"
          " using Camunda.')"),
    110: ("INCLUDE", "", True,
          "An example: In input management an AI classifies incoming business documents and"
          " forwards them to the responsible processes.",
          "the page is a pattern catalogue for orchestrating AI services in BPMN and says an"
          " AI component is called before a human decision, with an XOR gateway controlling "
          "the automation level", True, None,
          "figure 2 (bpmn cell, alt 'Process Choice')"),
    130: ("INCLUDE", "", True,
          "In Modeler, you see that the first human task is providing a customer inquiry that"
          " will be routed using the results of the OpenAI Connector.",
          "an Azure OpenAI Connector task sits inside the blueprint's BPMN process; the page "
          "prints the prompt expression and the temperature used", True, None,
          "the figure whose alt is 'A BPMN workflow diagram for determining correct route for"
          " customer inquiry'"),
    131: ("UNCERTAIN", "", True,
          "An AI agent is a software program that autonomously gathers data and carries out"
          " tasks using this information",
          "the page is an AI-agent explainer with two BPMN figures (alt 'Kyc-bpmn-camunda', "
          "'Intelligent-routing-ai-camunda') whose labels are not legible, and nothing in the"
          " text binds an AI element to a process element", True,
          "Does either BPMN figure on this page contain an AI/LLM element? The page is about "
          "AI agents but never binds one to a process element.", "figure 2 (bpmn cell)"),
    152: ("INCLUDE", "", True,
          "If the DMN table did manage to find a beer for you, I use the OpenAI Connector to"
          " ask ChatGPT to suggest places to find",
          "an OpenAI connector task sits in the BPMN model next to the DMN decision", True,
          None, "the figure whose alt is 'Bpmn-beer-recommendations-camunda'"),
    182: ("INCLUDE", "", True,
          "The filing process can invoke AI agents that can take the rate and line changes as"
          " input to locate all the affected tariffs",
          "the page shows a process model annotated with the places AI integrates and names "
          "the agent's input and its assistive use", True, None,
          "figure 2 (bpmn cell, alt 'Process model showing opportunities for AI integration')"),
    227: ("UNCERTAIN", "", True,
          "BPMN has a construct called an ad-hoc subprocess in which a small part of the"
          " process decision-making can be handed over to a human",
          "the page argues for AI agents inside BPMN and shows model screenshots, but the AI "
          "binding is conceptual; the cells are not legible, so whether a given element is "
          "AI-bound is not visible", True,
          "Do the BPMN screenshots on this page contain an AI element (an AI agent or "
          "ad-hoc sub-process step), or only ordinary tasks? The text argues the case "
          "without binding an element.", "figure 2 (bpmn cell, alt 'Screenshot')"),
    230: ("EXCLUDE", "E2-no-ai-element", True,
          "Thanks to Camunda’s integrated BPMN Copilot for SaaS, anybody can go from 0 to 80%"
          " of a process diagram in minutes.",
          "the release notes' AI is the BPMN Copilot that generates diagrams and the modeler "
          "assistance around them; the new ad-hoc subprocess element is not itself an AI "
          "element", False, None, "none"),
    257: ("EXCLUDE", "E2-no-ai-element", True,
          "With this alpha release of Camunda Copilot, you can not only generate BPMN"
          " diagrams, but Camunda now offers support to generate text from the BPMN",
          "the release notes' AI generates diagrams and documentation; the ad-hoc subprocess "
          "validation mentioned is not an AI element, and the only diagram with an 'AI' label"
          " is the product-house card", False, None, "none"),
    270: ("INCLUDE", "", True,
          "We’re excited to announce the general availability of new agentic process"
          " orchestration capabilities to model, deploy and manage AI agents",
          "the release shows an 'Ai-agent-ad-hoc-sub-process-camunda' model: AI agents are "
          "modelled as BPMN ad-hoc sub-processes inside the process", True, None,
          "figure 2 (bpmn cell, alt 'Ai-agent-ad-hoc-sub-process-camunda')"),
    288: ("INCLUDE", "", True,
          "Each agent’s task is represented as a discrete service task with well-defined"
          " inputs and expected outputs.",
          "the page states that AI agents are BPMN service tasks and shows the diagrams "
          "('AI agent inserted into BPMN diagram for process visibility')", True, None,
          "figure 1 (bpmn cell, alt 'AI agent inserted into BPMN diagram for process"
          " visibility')"),
    292: ("INCLUDE", "", True,
          "At the core of this approach is our use of the BPMN ad-hoc sub-process construct,"
          " which allows for tasks to be executed in any order",
          "the step-by-step guide builds an AI Task Agent as a BPMN ad-hoc sub-process and "
          "shows the sub-process figures", True, None,
          "figure 2 (bpmn cell, alt 'Sub-process')"),
    1263: ("INCLUDE", "", True,
           "The Connector is an easy way to start experimenting with ways to use ChatGPT and"
           " OpenAI’s Moderation API in your processes.",
           "an OpenAI connector task sits in the Community Market evaluation process the page"
           " documents with its own BPMN diagram", True, None,
           "figure 1 (bpmn cell, alt 'A BPMN diagram showing the evaluation process for the"
           " Community Market.')"),
    1340: ("INCLUDE", "", True,
           "Camunda provides an out-of-the-box OpenAI Connector which is used to compose an"
           " email to the adjuster the claimant is waiting for an estimate.",
           "the claims process diagram is annotated by the page as using the OpenAI Connector"
           " inside the adjuster subprocess", True, None,
           "figure 1 (bpmn cell, alt 'Auto-claim-adjuster-tasks-bpmn-camunda')"),
    1376: ("INCLUDE", "", True,
           "I used the OpenAI connector and added the prompt:",
           "the trivia process uses an OpenAI connector task and a second call for hints; the "
           "page's own figure 'Basic-trivia-bpmn-model-plus-openai' is the model with the "
           "connector in it", True, None,
           "the figure whose alt is 'Basic-trivia-bpmn-model-plus-openai'"),
    1390: ("UNCERTAIN", "", True,
           "you simply model the tasks and flows that may be required and then let the LLM decide"
           " what gets triggered",
           "the figures are the agentic-orchestration models ('Fig 3 – Agentic and"
           " deterministic orchestration combined in a single end-to-end process') but no "
           "page line binds an AI element to a process element, and the cells are not legible",
           True,
           "Does the process figure in this post show an AI element (agent / ad-hoc "
           "sub-process) or only deterministic tasks? The alt text says agentic and "
           "deterministic orchestration are combined, but nothing in the text binds an "
           "element.", "figure 1 (bpmn cell, alt 'Fig 3 …')"),
    1399: ("INCLUDE", "", True,
           "Both are built on the same principle: the agent reasons inside an ad-hoc"
           " sub-process, while everything around it stays deterministic and controlled",
           "the page describes the agent living in a BPMN ad-hoc sub-process with a boundary "
           "event for high-risk escalation, and shows the resulting process; the same page "
           "also used Claude to design the model, which the E2 code would dismiss on its own",
           True, None,
           "the figure whose alt is 'Resulted BPMN by AI' or 'BPMN diagram generated by AI'"),
    1405: ("INCLUDE", "", True,
           "Its job is to pick the best-fitting mechanism for each step of a process: DMN,"
           " API, Connector, User Task, or AI Agent.",
           "the page shows a process that uses several mechanisms per step and names AI Agent"
           " as one of the steps it chooses between", True, None,
           "figure 1 (bpmn cell, alt 'Process using multiple mechanisms')"),
    1410: ("INCLUDE", "", True,
           "A loan support agent in Camunda Modeler. The ad-hoc subprocess (purple star) is"
           " the agent's reasoning space.",
           "the figure's own alt text describes the agent's reasoning space as a BPMN ad-hoc "
           "sub-process whose boxes are tools the LLM invokes", True, None,
           "figure 1 (bpmn cell, alt 'Inner and outer orchestration in a loan origination"
           " process …')"),
    1413: ("INCLUDE", "", True,
           "I needed to build an end-to-end full Policy Change for automobile insurance"
           " process with AI agents.",
           "the resulting policy change process contains AI agents; the page shows its AI "
           "Agent Tool Optimize dashboard with the tool calls made by agents", True, None,
           "figure 2 (bpmn cell, alt 'The resulting policy change process')"),
    1434: ("INCLUDE", "", True,
           "This pattern is Camunda as an MCP client . It lives inside the AI Agent"
           " connector's ad-hoc sub-process model.",
           "the MCP client pattern is placed inside the AI Agent connector's ad-hoc "
           "sub-process, i.e. an AI element inside the process model", True, None,
           "the bpmn figure of the post"),
    # ---- the 18 figures read at 1400 px (a subagent was sent to capture and read them) ----
    # 8.5 release: the diagram the post shows is the dinner model, which has no AI element,
    # while the AI mention is a shipped LLM-bound connector, i.e. neither diagram generation
    # nor roadmap, so E2 is not available and the call stays open
    46: ("UNCERTAIN", "", True,
         "We now provide customized model selection and temperature input for the OpenAI"
         " outbound Connector.",
         "the 8.5 release announces the OpenAI outbound connector (an LLM-bound element type) "
         "but the diagram the post shows is a dinner model - read at 1400 px: start 'Hungry', "
         "user task 'Decide what's for dinner', gateway 'Meal?', tasks 'Prepare chicken'/'Prepare "
         "salad', end 'Happy' - and binds no AI element", True,
         "The release post announces the OpenAI outbound connector, but the BPMN diagram it "
         "shows (the dinner model) binds no AI element. Should the announced connector count as "
         "an AI-in-process artefact here?", "figure 11 of `all 46` (the BPMN canvas, alt "
         "'Simplified-bpmn-modeling-canvas'); figure 1 is an 'Apply filters' dialog"),
    185: ("UNCERTAIN", "", True,
          "Azure OpenAI : We no longer send null values to the REST Connector.",
          "the alpha release notes name the Azure OpenAI connector; the captured migration view "
          "is read at 1400 px as two BPMN pools (orderProcessMigration v1/v2) with Send Task, "
          "Assign Task, Review Task, gateways and a multi-instance sub-process, and carries no "
          "AI element", True,
          "Do the release notes' Azure OpenAI connector and the migration view on this page "
          "together present an AI element inside a process, or is the connector a platform "
          "capability the diagram does not use?", "figure 1 (Operate migration view, 1400 px)"),
    272: ("INCLUDE", "", True,
          "We accompany this investment in AI with the power of Intelligent Document Management"
          " (IDP)",
          "the captured IDP process (read at 1400 px) runs three parallel extraction service "
          "tasks - 'Extract IDs', 'W2 Extraction', 'Paystub Extraction' - whose properties bind "
          "the 'IDENTIFICATION EXTRACTION' template to AWS Textract and an S3 bucket "
          "(idp-extraction-connector, us-east-1, 'stored temporarily during Textract analysis'); "
          "the page frames IDP as its AI investment. The AI-ness rests on the connector template "
          "and the page's words, not on a model name printed on the canvas", False, None,
          "figure 2 of `all 272` (the IDP extraction process); figure 1 is a BPMN-file "
          "dependency map, not a process"),
    277: ("EXCLUDE", "E2-no-ai-element", True,
          "Camunda 8 Run is free for local development, but our complete agentic orchestration"
          " platform lets you take full advantage",
          "the diagram is one user task in a Modeler screenshot (read at 1400 px: start -> user "
          "task 'User Task' -> end, with the Deploy dialog and PROCESS 'Test process'), and "
          "carries no AI element; the page's only AI words are this platform blurb in the "
          "closing call to action, which refers to the platform, not to any element of the "
          "diagram", False, None, "none"),
    338: ("UNCERTAIN", "", True,
          "Camunda Modeler's AI copilots-for FEEL and BPMN-are capable of some fantastic data"
          " parsing.",
          "the artefact is an AI-generated BPMN model (an animation of the Copilots): the AI "
          "here generates the diagram, which the rules put in the E2 case, but only frame 1 of "
          "the GIF is readable and it shows an empty canvas with a single start event, so what "
          "the generated model contains could not be checked", True,
          "The artefact is an animated GIF of Camunda Copilots; only its first frame (an empty "
          "canvas with one start event) could be read. Is the AI on this page only the copilot "
          "that generates the model, or does the generated model contain an AI-bound element?",
          "figure 1 (the copilot animation)"),
    340: ("UNCERTAIN", "", True,
          "Tools for agentic orchestration . Dynamic AI agents rely on a collection of tasks to"
          " accomplish their goals.",
          "the prose describes AI agents selecting element and connector templates at runtime, "
          "but the process the post shows (Operate view of 'Test Joke', read at 1400 px: start "
          "'Request Joke' -> 'Obtain Joke' -> 'Display Joke' -> end 'Joke Requested', variables "
          "jokeSetup/jokePunchline) binds no AI element", True,
          "Does the page present an AI-in-process artefact, or only the platform capability of "
          "agent-ready templates? The prose describes AI agents choosing tasks, but the process "
          "it shows is a joke REST process with no AI element.",
          "figure 2 of `all 340` (the Operate view); figure 1 is the post's title card"),
    398: ("UNCERTAIN", "", True,
          "Since we are a bit new to adding AI into our processes at Horse & Hawk Habitat, we"
          " wanted to add a check",
          "the post is about migrating agentic processes and names 'a call to an LLM' and "
          "ad-hoc sub-processes, but both versions of the order process in the capture (read at "
          "1400 px: 'Order received' -> 'Check payment' -> 'Payment OK?' -> 'Ship Articles' / "
          "'Request for payment'; v2 adds 'Notify Customer') carry no AI element", True,
          "Do the agentic versions of the order process on this page bind an AI element? The "
          "post speaks of a call to an LLM and of ad-hoc sub-processes, but the two versions "
          "shown in the capture contain no AI element.",
          "figure 1 (Operate migration view of the two versions, 1400 px)"),
    445: ("INCLUDE", "", True,
          "Camunda 8's new AI Agent connector makes it easy to integrate large language models"
          " (LLMs) into your process workflows.",
          "the capture (Operate, read at 1400 px) shows the 'AI Agent' ad-hoc sub-process "
          "container with a tilde marker holding Task A and Task B, the instance variables "
          "agent and toolCallResults, and the history entry 'AI Agent (ad-hoc sub-process icon)'; "
          "the tasks inside carry no AI label, the container does", False, None,
          "figure 2 of `all 445` (the Operate instance view); figure 1 is the post's title card"),
    496: ("INCLUDE", "", True,
          "Users can easily select a connector and remain focused on building their automation"
          " rather than hunting down connector configuration parameters.",
          "the capture (Modeler, read at 1400 px) shows a task labelled 'Bedrock Connector' with "
          "the applied template 'AWS BEDROCK OUTBOUND CONNECTOR' and Configuration Action 'Invoke "
          "Model' - an LLM-bound task inside the process; the page text never names Bedrock, so "
          "the AI element is visible in the figure only", False, None,
          "figure 2 of `all 496` (the Modeler capture with the Bedrock connector task); figure 1 "
          "is a chat panel"),
    511: ("INCLUDE", "", True,
          "For this example, we replaced the job worker Evaluate Risk in our existing BPMN"
          " process with an AI Task Agent connector that will take input",
          "the page states the AI Task Agent connector replaced a job worker in the BPMN process "
          "it shows; the capture (Modeler 'Implement' tab, breadcrumb 'Loan Process w AI', read "
          "at 1400 px) shows the 'Credit Risk Value?' gateway whose branch carries the pink task "
          "'Determine Risk' - the node label itself carries no AI token, so the binding rests on "
          "the page's words", True, None,
          "figure 1 (the Modeler canvas of the loan process, 1400 px)"),
    512: ("EXCLUDE", "E2-no-ai-element", True,
          "This server gives teams a consistent way to connect AI agents to Camunda, reduces"
          " custom integration work, and makes it easier to scale from isolated",
          "the AI on this page is an integration surface for external AI agents (the 8.9 "
          "Orchestration Cluster MCP Server, an API AI applications call to reach Camunda) - AI "
          "around the process; the captured view (read at 1400 px) maps user-task features "
          "between two process versions and shows no AI element", False, None, "none"),
    531: ("INCLUDE", "", True,
          "AI Firewall Agent . This is the safeguard agent that sits between the communication"
          " agent's reasoning and its execution.",
          "the capture (Operate view of 'safeguard-agent', read at 1400 px) shows an end event "
          "'AI Agent task failed' inside the process, the task 'Safeguard user prompt', a "
          "'Confidence level sufficient?' gateway, an on-canvas annotation naming 'The AI "
          "Firewall' with its safeGuardResult FEEL context (decision allow/warn/block, "
          "confidence 0.00-1.00), and the variables messageContext and safeGuardResult", False,
          None, "figure 1 (the Operate view of the safeguard agent, 1400 px)"),
    570: ("EXCLUDE", "E2-no-ai-element", True,
          "In this release, we added a more compact version of the report/dashboard share page"
          " that is used when embedding it in other applications.",
          "the page's AI-term hit is 'embedding' - embedding a report in another application, "
          "not an AI embedding; the captured heatmap (read at 1400 px) is drawn over a real "
          "BPMN invoice process with lanes 'Inns Assistent', 'Invoice Recipient / Approver' and "
          "'Accountant' and carries no AI element", False, None, "none"),
    583: ("EXCLUDE", "E0-no-artefact", False,
          "Optimize provides an easy way to embed your report in other websites.",
          "the page's figures are a bar chart of user-task counts and a process-instance "
          "duration table - read at 1400 px and confirmed as a report UI, with no BPMN diagram "
          "anywhere; the word 'embed' refers to embedding a report in another website", False,
          None, "none"),
    624: ("UNCERTAIN", "", True,
          "Human workers have creativity, judgment and other soft skills that robots, explicitly"
          " programmed software or machine learning can't replicate efficiently.",
          "the post's only AI/ML mention is a contrast about human skills; the captured Optimize "
          "heatmap is drawn over a BPMN diagram with lanes ('Hiring Manager', 'Reviewer'), but "
          "the heat glow blurs the heated task labels at 1400 px, so whether an element calls an "
          "AI service cannot be read", True,
          "Does any element of the hiring process under the Optimize heatmap call an AI/LLM "
          "service? The heat glow obscures most task labels and the page mentions machine "
          "learning only in passing.",
          "figure 2 of `all 624` (the user-task heatmap); figure 1 is a report table"),
    685: ("EXCLUDE", "E2-no-ai-element", True,
          "Camunda Automation Platform 7.17.0 adds a little safeguard that prompts the user to"
          " confirm their change to the TTL before applying it.",
          "the page's only AI-term hit is the verb 'prompts' (a safeguard prompts the user), not "
          "an AI prompt; the captured Cockpit view (read at 1400 px: 'Workday over' -> 'Crank up "
          "radio' -> 'Celebrate' -> end 'Tired', definition 'after-work') carries no AI element",
          False, None, "none"),
    732: ("EXCLUDE", "E2-no-ai-element", False,
          "In a current customer project we faced the issue that there were two executable"
          " processes - independent of each other.",
          "the page never mentions AI or LLM at all; the captured Cockpit plugin view (read at "
          "1400 px) shows two collaborating BPMN pools - lane 'Change' and lane 'Perform' - with "
          "message flows 'Request Change' and 'Request Verification', and carries no AI element",
          False, None, "none"),
    1287: ("EXCLUDE", "E2-no-ai-element", True,
           "for User Tasks , BPMN diagrams for Call Activities , and DMN diagrams for Business"
           " Rule Tasks from the contextual menu used for embedding/linking .",
           "the page's AI-term hit is 'embedding/linking' (sub-resources linked from the "
           "contextual menu), not an AI embedding; the captured Modeler view (read at 1400 px: "
           "'Invoice received' -> 'Check for completeness', with the Problems panel 'Rule "
           "<custom/rule-error> errored with the following message: I blow up') has no AI "
           "element", False, None, "none"),
    271: ("EXCLUDE", "E2-no-ai-element", True,
          "As soon as I saw this plugin demoed, I installed it. It’s been a massive time saver"
          " for me, being able to see properties by scanning the mouse across the model",
          "the page never mentions AI or LLM at all - its one 'model' hit is the Camunda "
          "Modeler / the process model of this tooltip-plugin demo; the captured first frame "
          "of the 230-frame animation (1270x817, read at 1400 px, where the labels are fully "
          "legible, unlike the 340 px contact-sheet cell that forced the earlier UNCERTAIN) is "
          "a Camunda Modeler canvas holding pool 'Payment process' - message start event "
          "'Payment start', exclusive gateway 'Amount?' (low / medium / high), service task "
          "'Payment execution', user task 'Check payment execution', service task 'Financial "
          "payment evaluation', boundary error -> 'Handle Error', 'Prepare rejection data', "
          "user task 'Reject payment' and their end events - with no AI element anywhere in "
          "the pool", False, None, "none"),
    338: ("EXCLUDE", "E2-no-ai-element", True,
          "Camunda Modeler’s AI copilots—for FEEL and BPMN—are capable of some fantastic data"
          " parsing. Take a tour with these brief experiments.",
          "the quoted AI mention is about the Copilot that *writes* the model, not about an "
          "element inside it: the animation (122-frame GIF, 1274x817, read at 1400 px across "
          "its frames) shows the Camunda Copilot panel - prompt 'build a simple process for "
          "applying for a mortgage' - building 'Submit mortgage application' -> 'Review "
          "mortgage application' -> exclusive gateway 'Application decision' -> end events "
          "'Mortgage application approved' / 'Mortgage application rejected', a plain "
          "human-task / gateway model carrying no AI activity of its own, which the rules put "
          "in the E2 case ('AI generating the diagram'); the post's FEEL-Copilot figure is a "
          "FEEL expression editor, not a process", False, None,
          "figure 1 of `all 338` (frame 91 of the animation, the built model); the FEEL "
          "editor is figure 2"),
}


def classify(r, cls, aiv, vnt):
    """(verdict, reason, judgment, evidence, note, needs_visual, question)

    The notation call is the visual pass's (every post with a figure has a cell in a
    contact sheet); the AI call is the page's own words where they bind an AI element to a
    process element, and the visual pass's reading of the artefact otherwise. A cell whose
    note says the labels were unreadable cannot carry the AI call: it is UNCERTAIN.
    """
    n = r["n"]
    figs = F.figs(r)
    vc = cls.get(n)
    vai = aiv.get(n, set())
    nt = notes_for(n, vnt)
    nts = " | ".join("%s/%s: %s" % (c, a, x[:90]) for c, a, x in nt) or "no visual line"
    # AI material to judge: an AI/LLM term in the page text, or a model whose XML is on
    # disk. A link that only looks like a model (a marketplace plugin path) is neither.
    ai_post = bool(r["n_ai"]) or bool(model_files(r["n"]))
    alts = [f["alt"] for f in figs if f["alt"]]
    altstr = "; ".join(a[:60] for a in alts[:4]) or "none"
    bpmn_prose = bool(re.search(r"(?i)\bbpmn\b", r["text"])) or any("bpmn" in a.lower()
                                                                    for a in alts)
    src = src_for(r, cls, aiv)

    if r["files"] and model_files(r["n"]):
        # the page links a model and its XML is on disk; the XML is the artefact (handled by
        # the caller). A link that only *looks* like a model - a marketplace plugin path such
        # as .../de.viadee.confluence.bpmn - downloads nothing, so that post is judged here
        # from its figures rather than dropped for want of a route.
        return None

    if not figs:
        return ("EXCLUDE", "E0-no-artefact", False, first_sentence(r["text"]),
                "the page carries no figure and links no .bpmn/.dmn/.cmmn file: no process "
                "artefact of any kind, whatever the text discusses", False, "")

    if vc is None:
        return ("UNCERTAIN", "", True, altquote(alts[0]) if alts else first_sentence(r["text"]),
                "this post's figures were never put in front of anyone: it fell outside the "
                "contact-sheet selection and the page gives no usable alt text", True,
                "What does the figure on this page show - is it a BPMN 2.0 diagram, and does "
                "any element in it call an AI/LLM service?")

    # a diagram that is not BPMN: named from the visual pass and the alt text
    if vc == "other-diagram":
        a = next((a for a in alts if any(re.search(p, a) for p, _ in NOTATION)),
                 alts[0] if alts else "")
        what = next((w for p, w in NOTATION if a and re.search(p, a)), "a diagram")
        return ("EXCLUDE", "E1-not-bpmn", True, altquote(a) or first_sentence(r["text"]),
                "the page's diagram is %s, named by its alt text %r and read on the contact "
                "sheet (%s): not BPMN 2.0 notation" % (what, a[:80], nts), False, "")

    # a window-classed cell whose note names a drawn surface and process structure: the
    # artefact is the diagram the window shows, so it is judged as a diagram (see DRAWW/PROCW)
    resc = [(a, x) for c, a, x in nt
            if c in SCREENS and DRAWW.search(x) and PROCW.search(x) and not NEGW.search(x)]

    # figures exist and none of them is a diagram: no process artefact
    if vc in SCREENS and not resc:
        return ("EXCLUDE", "E0-no-artefact", False, first_sentence(r["text"]),
                "the page's %d figures are screenshots, charts, photographs or brand cards "
                "(alt texts: %s; contact sheet: %s): no process artefact"
                % (len(figs), altstr, nts), False, "")

    # the notation could not be read and the page never names BPMN either
    if vc == "unclear" and not bpmn_prose:
        return ("UNCERTAIN", "", True, altquote(alts[0]) if alts else first_sentence(r["text"]),
                "the figure could not be classified from the contact sheet (%s) and the page "
                "never names a notation" % nts, True,
                "Is the diagram on this page BPMN 2.0, and does any element in it call an "
                "AI/LLM service? The contact-sheet thumbnail is too small to read its labels.")

    # a BPMN diagram is on the page (vc == "bpmn", or "unclear" with the page naming BPMN, or
    # a window-classed cell whose note names a diagram - the `resc` list above)
    bcells = [(a, x) for c, a, x in nt if c == "bpmn"] or resc
    unread = any(UNREAD.search(x) for _, x in bcells) or not bcells
    bai = {a for a, _ in bcells}
    if resc:
        nts = ("the figure is a %s window, and the cell's own reading of it is %r; the "
               "artefact taken is the process model the window shows. %s"
               % (vc, resc[0][1][:120], nts))
    if not ai_post:
        if unread:
            return ("UNCERTAIN", "", True,
                    altquote(alts[0]) if alts else first_sentence(r["text"]),
                    "the page shows a BPMN diagram and carries no AI/LLM term anywhere, but "
                    "the cell that covers it is unreadable (%s), so whether any element in it "
                    "is AI-bound is not visible" % nts, True,
                    "Does the BPMN diagram on this page contain an AI/LLM element? The page "
                    "text never mentions AI and the contact-sheet thumbnail is unreadable.")
        return ("EXCLUDE", "E2-no-ai-element", False,
                _bpmn_quote(r, alts) or altquote(alts[0] if alts else ""),
                "the page shows a BPMN diagram, carries no AI/LLM term anywhere in its text "
                "or alt texts%s, and the visual pass read the artefact without seeing an AI "
                "element (%s): no AI element is inside the process"
                % (" (it does describe the process)" if STRUCT.search(r["text"]) else "", nts),
                False, "")

    if "yes" in bai:
        return ("INCLUDE", "", True, _bpmn_quote(r, alts) or altquote(alts[0] if alts else ""),
                "the page text does not name AI, but the visual pass read an AI element in "
                "the diagram itself (%s); record to be written from this page" % nts,
                True, "")

    # an AI-bearing post that shows a BPMN diagram: the judgement
    ins = A.find(r, A.INSIDE)
    outs = A.find(r, A.OUTSIDE)
    if ins:
        name, line = ins[0]
        return ("INCLUDE", "", True, " ".join(line.split()[:25]),
                "the page names %r, an AI element bound to a process element; record to be "
                "written from this page" % name, unread, "")
    if outs and not ins and not unread:
        name, line = outs[0]
        return ("EXCLUDE", "E2-no-ai-element", True, " ".join(line.split()[:25]),
                "the only AI the page points at is %r - tooling around the diagrams (model "
                "suggestions, documentation, coding help, roadmap), not an element inside the "
                "process" % name, False, "")
    return ("UNCERTAIN", "", True, first_sentence(r["text"]),
            "the page shows a BPMN diagram and carries AI/LLM terms, but names no AI element "
            "bound to a process element%s" % (", and the cell that covers it is unreadable (%s)"
                                              % nts if unread else ""), True,
            "Does any element of the BPMN diagram on this page call an AI/LLM service? The page "
            "text mentions AI but never binds it to a process element.")


def _bpmn_quote(r, alts):
    for line in r["text"].split("\n"):
        line = " ".join(line.split())
        if "BPMN" in line and len(line) > 25:
            return " ".join(line.split()[:25])
    for a in alts:
        if "bpmn" in a.lower():
            return altquote(a)
    return first_sentence(r["text"])


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    verbose = "-v" in sys.argv
    cls, aiv, vnt = visual()
    print("visual pass: %d posts classified, %d with any ai_visible=yes"
          % (len(cls), sum(1 for v in aiv.values() if "yes" in v)))
    # no row may rest on a figure nobody looked at: every post that shows a figure must have
    # a line in a visual report, or the plan refuses to run
    import _cmdb_shots as S
    uncovered = [r["n"] for r in F.rows()
                 if r["n"] <= 1435 and F.figs(r) and r["n"] not in cls]
    if uncovered:
        print("REFUSING: %d posts with figures still unlooked-at (first 20: %s)"
              % (len(uncovered), uncovered[:20]))
        return []
    rows, counter = [], collections.Counter()
    # how many posts the hand rulings had to overrule the mechanical call on, for the footer
    flips = []
    for n, rr in sorted(RULED.items()):
        v, reason = rr[0], rr[1]
        r = next((x for x in F.rows() if x["n"] == n), None)
        if r is None:
            continue
        m = model_verdict(r, cls) or classify(r, cls, aiv, vnt)
        if m is None:
            continue
        if (m[0], m[1] or "") != (v, reason or ""):
            flips.append({"n": n, "mechanical": [m[0], m[1]], "ruled": [v, reason]})
    print("self-audit: %d of %d hand rulings flip the mechanical call" % (len(flips), len(RULED)))
    if cmd == "apply":
        with open(os.path.join(RAW, "self_audit.json"), "w", encoding="utf-8",
                  newline="\n") as fh:
            json.dump({"flips": len(flips), "rulings": len(RULED), "detail": flips}, fh,
                      ensure_ascii=False, indent=1)
    for line in open(FRONTIER, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 2:
            continue
        n, url = int(parts[0]), parts[1]
        if n > 1435:
            rows.append({"n": n, "url": url, "verdict": "BLOCKED", "reason": None,
                         "judgment": False,
                         "evidence": "docs.camunda.io and docs.camunda.org refuse this "
                                     "machine's egress (curl exit 7, Chrome "
                                     "net::ERR_CONNECTION_REFUSED) while camunda.com answers 200",
                         "note": "the docs host is unreachable from this machine; see "
                                 "notes/elicitation/sources/OPERATOR-TODO.md P10. Not worked "
                                 "around on purpose.",
                         "needs_visual_check": False, "needs_human_ruling": False,
                         "question": None,
                         "blocker": "docs.camunda.io / docs.camunda.org refuse this machine's "
                                    "egress; see notes/elicitation/sources/OPERATOR-TODO.md P10"})
            counter["BLOCKED"] += 1
            continue
        r = next(x for x in F.rows() if x["n"] == n)
        c = RULED.get(n) or model_verdict(r, cls) or classify(r, cls, aiv, vnt)
        if c is None:
            continue
        v, reason, judg, ev, note, nvc, q = c[:7]
        # the evidence rule caps a quote at 25 words; a prefix of a verbatim run is still
        # verbatim, so the cap is applied mechanically rather than trusted to each branch
        ev = " ".join((ev or "").split()[:25])
        if len(c) > 7 and c[7] and c[7] != "none":
            note += "; the record should capture %s" % c[7]
        rec = DONE.get(n)
        if rec:
            # the record's own frontmatter is authoritative for the row: a record written up as
            # UNCERTAIN must not be reported as an INCLUDE here (the two must agree)
            rv, rq = record_ruling(rec)
            v, judg = rv or "INCLUDE", True
            reason = ""
            q = rq if rv == "UNCERTAIN" else None
            nvc = nvc or rv == "UNCERTAIN"
            note = "this item is already written up as a corpus record: %s" % rec
        counter[(v, reason)] += 1
        rows.append({"n": n, "verdict": v, "reason": reason, "judgment": judg, "evidence": ev,
                     "record": rec, "needs_visual_check": nvc, "needs_human_ruling": v == "UNCERTAIN",
                     "question": q, "note": note, "judged_from": src_for(r, cls, aiv)})
        if verbose and v != "EXCLUDE":
            print("%5d %-9s %-16s %s" % (n, v, reason or "-", r["title"][:52]))
    print(counter)
    if cmd == "apply":
        with open(DIPS, "a", encoding="utf-8") as fh:
            for x in rows:
                fh.write(json.dumps(x, ensure_ascii=False) + "\n")
        print("appended", len(rows))
    return rows


def record_ruling(path):
    """(verdict, question) as the record's own frontmatter states them."""
    import _cmdb_verify as V
    fm = V.frontmatter(path)[0] or {}
    v = (fm.get("verdict") or "").upper() or None
    return v, (fm.get("question") or None)


def src_for(r, cls, aiv):
    n = r["n"]
    return ("screen of the saved page ledgers/camunda-docs-blog.raw/blog/%04d.html (fetched "
            "2026-09-26) + contact-sheet visual pass (viz/report_*, cell class %r, ai_visible %s): "
            "%d figures, %d with alt text, model XMLs downloaded: %d, AI/LLM terms in the "
            "text: %d"
            % (n, cls.get(n), "/".join(sorted(aiv.get(n, []))) or "-", len(F.figs(r)),
               len([f for f in F.figs(r) if f["alt"]]), len(model_files(r["n"])), r["n_ai"]))


if __name__ == "__main__":
    main()
