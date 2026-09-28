# -*- coding: utf-8 -*-
"""Build the uipath-maestro-docs ledger, frontier and corpus records.

Population (323 rows), recorded in the ledger header:
  226 urls under /maestro/automation-cloud/latest/  = the 222 urls the vendor sitemap for
      the Maestro product lists (products/maestro/sitemaps/en/sitemap.xml) + 4 pages that
      sitemap omits but the docs link to (automate-getting-started,
      choosing-maestro-orchestrate-or-maestro-automate,
      maestro-automate-capabilities-comparison, node-human)
   95 urls under /maestro/automation-suite/2.2510/  = the same manual on the other
      publication line, enumerated as well rather than pinning one line (deliberate
      over-inclusion: the two lines differ on 9 pages)
  +  2 closure-only urls (introduction-to-maestro, process-monitoring) that redirect to
      /user-guide/overview.
The English tree is enumerated; the /de/ tree is a lagging translation of it.

Verdicts: explicit entries below (pages opened and judged by hand), then the E3 twin rule
(a 2.2510 page whose figures and model files are identical to its Cloud twin is one docs
page under two URLs), then mechanical families (no artefact -> E0; figures not BPMN -> E1
naming the notation; BPMN figures with no AI element -> E2).

Every row carries a verbatim quote taken from the page itself (evidence rule 5).
"""
import io, json, os, re, shutil, sys

RAW = 'ledgers/uipath-maestro-docs.raw'
SCAN = os.path.join(RAW, 'scan.json')
IMG = os.path.join(RAW, 'img')
XML = os.path.join(RAW, 'xml')
LEDGER = 'ledgers/uipath-maestro-docs.jsonl'
FRONTIER = 'ledgers/uipath-maestro-docs.frontier.txt'
CORPUS = 'corpus/uipath-maestro-docs'
CLOUD = '/maestro/automation-cloud/latest'
SUITE = '/maestro/automation-suite/2.2510'
DATE = '2026-09-25'

scan = json.load(io.open(SCAN, encoding='utf-8'))
FIG = {u: [i for i in (v.get('imgs') or []) if 'logo' not in i['src']] for u, v in scan.items()}


def text(u):
    return re.sub(r'\s+', ' ', (scan.get(u, {}).get('text') or '')).strip()


def alts(u):
    return [i.get('alt') or '' for i in FIG.get(u, [])]


def files(u):
    return scan.get(u, {}).get('files') or []


def wquote(s, n=25):
    return ' '.join(re.sub(r'\s+', ' ', s or '').split()[:n])


def page_quote(u, n=25):
    t = re.sub(r'^(theme-doc-markdown markdown">\s*)', '', text(u))
    m = re.search(r'\.\s', t)
    return wquote(t[:m.start() + 1] if m and m.start() > 40 else t, n)


def ai_mention(u, drop=(), n=25):
    for h in (scan.get(u, {}).get('ai') or []):
        if any(re.search(d, h.get('ctx') or '', re.I) for d in drop):
            continue
        return wquote(h['ctx'], n)
    return ''


def local(src):
    return os.path.join(IMG, re.sub(r'[^A-Za-z0-9._-]', '_', src.split('/')[-1]))


def pick(u, needle):
    for i in FIG.get(u, []):
        if needle.lower() in i['src'].lower() or needle.lower() in (i.get('alt') or '').lower():
            return i['src']
    return None


NOTATION = [
    (r'(flow canvas|node on the canvas|node, followed|handles|palette|chat|voice|studio web node)',
     'Maestro Flow node-graph canvas (nodes joined by named handles)'),
    (r'(stage|case app|case type|primary stages|case lifecycle|case management)',
     'Maestro Case canvas (stage containers and stage-task cards, CMMN-style case model)'),
    (r'(lifecycle|architecture|differentiators|agentic automation|end-to-end)',
     'vendor architecture / lifecycle illustration'),
    (r'(properties|panel|dialog|dropdown|table|dashboard|view|editor|toolbar|picker|field|form|wizard|selector|configuration|settings|tab)',
     'Studio Web user-interface screenshot'),
]
BPMN_ALT = re.compile(r'(bpmn|process diagram|diagram of|gateway|pool|lane|subprocess|sequence flow|task icon|event icon|boundary|start event|end event|intermediate|exclusive|parallel|process|flow)', re.I)


def notation_note(u):
    a = ' ; '.join(alts(u))
    for pat, name in NOTATION:
        if re.search(pat, a, re.I):
            return name
    return 'Studio Web user-interface screenshot'


def figure_kind(u):
    a = ' ; '.join(alts(u))
    if not a:
        return 'none'
    if re.search(r'(flow canvas|node on the canvas|node, followed|trigger connected|handles:|autonomous agent node|voice agent|conversational)', a, re.I):
        return 'flow'
    if re.search(r'(stage|case app|case type|primary stages|case lifecycle)', a, re.I):
        return 'case'
    if re.search(r'(align bpmn elements|connecting bpmn|bpmn diagram|process diagram|diagram of|gateway diagram|sequence flow|pool example|lane example|subprocess|event icon|task icon|event-based wait|loop over|boundary messages|process diagram|process view|instances view|incidents view|heatmap|execution counts)', a, re.I):
        return 'bpmn'
    if re.search(r'(properties|panel|dialog|dropdown|table|dashboard|view|editor|toolbar|picker|field|form|wizard|selector|configuration|settings|tab|chart|list)', a, re.I):
        return 'ui'
    return 'bpmn' if BPMN_ALT.search(a) else 'ui'


# ------------------------------------------------------------ pages judged by hand
# slug/tail -> dict(verdict, note, bpmn, bpmn_quote, ai, ai_quote, caps, ruling?, question?)
MANUAL = {
 'how-to-complex-process': dict(v='INCLUDE',
  note='BPMN 2.0 invoice process whose service task "Resolve discrepancies" carries the UiPath agent '
       'marker and an "Agent" bracket annotation; the same page also publishes the instance view of that '
       'process. Read at native resolution.',
  bpmn='BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths: start '
       'event "Invoice received" -> service task "Invoice to PO matching" -> exclusive gateway "Is '
       'resolution required?" -> (Yes) service task "Resolve discrepancies" with the circular UiPath agent '
       'marker and an "Agent" bracket annotation -> ... -> user task "Invoice approval" -> service task '
       '"Post invoice to SAP" -> end event "Invoice processed"; rejects go to send task "Notify vendor".',
  bq='BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths',
  ai='The AI element sits inside the process: the service task "Resolve discrepancies" is bracketed "Agent" '
     'in the diagram (the same glyph marks the second, non-agent "Resolve discrepancies" task as "Action '
     'Center Action app"). The page instructs: "Add Agent as an annotation to indicate this will be an '
     'agent task."',
  aq='Add Agent as an annotation to indicate this will be an agent task.',
  caps=[('maestro-process-diagram-599989', 'png', 'the full process diagram (agent task + "Agent" bracket)'),
        ('maestro-all-instances-view-complex-process-599937', 'png', 'the same process in the instance view')]),
 'purchase-to-pay': dict(v='INCLUDE',
  note='Use-case BPMN diagram with one task explicitly named after its AI implementation.',
  bpmn='BPMN diagram of a purchase-to-pay process: task cards with BPMN task-type icons, exclusive and '
       'event-based gateways, boundary timer/message events, end event "Invoice Processing Complete".',
  bq='purchase to pay',
  ai='The task "Invoice Dispute Analysis (3rd Party AI Agent)" is part of the process flow, on the No '
     'branch of "Match Successful?"; its card carries the circular UiPath agent marker.',
  aq='Invoice Dispute Analysis (3rd Party AI Agent)',
  caps=[('maestro-purchase-to-pay', 'png', 'the whole P2P diagram; the agent task is on the No branch')]),
 'loan-origination': dict(v='INCLUDE',
  note='Use-case BPMN diagram in which "Underwriting Review" carries the same circular agent marker that '
       'marks the explicitly named "(3rd Party AI Agent)" task in the purchase-to-pay diagram of the same '
       'use-case family. The prose of the page does not name agents, so this rests on the marker.',
  bpmn='BPMN diagram of a loan-origination process: start event, user/service/send task cards, exclusive '
       'and parallel gateways, end event "End of loan application process".',
  bq='loan origination',
  ai='The task card "Underwriting Review" carries the circular UiPath agent marker on its bottom edge '
     '(read at native resolution at 4x; identical glyph to the agent marker on the task named "(3rd Party '
     'AI Agent)" in the sibling purchase-to-pay diagram).',
  aq='The following diagram shows a loan-origination process in Maestro',
  visual=True,
  caps=[('maestro-loan-origination', 'png', 'the whole loan-origination diagram')]),
 'markers-implementation': dict(v='INCLUDE',
  note='BPMN modelling pattern (multi-instance service task) whose implementation is an agent, evidenced by '
       'the properties panel and the prose.',
  bpmn='BPMN service task inside a subprocess with a sequential multi-instance marker; the figures are the '
       'element toolbar, the properties panels of those BPMN elements, the execution trail and the outputs '
       'section of the marked BPMN task.',
  bq='Use markers to configure a task to run once for each element in a List variable',
  ai='The captured properties panel shows the Action section with "Start and wait for agent" selected and an '
     'agent configured; the prose runs "Action: Select Start and wait for agent. Agent: Select the agent '
     'responsible for validating invoices."',
  aq='Action: Select Start and wait for agent. Agent: Select the agent responsible for validating invoices.',
  caps=[('agent-implementation', 'png', 'Action = Start and wait for agent, with the agent selector filled'),
        ('subprocess-properties', 'png', 'the service task inside the subprocess, properties panel open')]),
 'debugging': dict(v='INCLUDE',
  note='The debugging page publishes a full agent-rich BPMN process (four agent service tasks) plus its '
       'execution trail. Read at native resolution.',
  bpmn='BPMN 2.0 diagram on the Maestro canvas in a debug session: message start event "New Contact '
       'Created", send task "Get Contact Details", service task "Contact-Validation-Agent" with the agent '
       'marker, exclusive/parallel gateways, service tasks "Langchain - Company Research...", "Lead Scoring '
       'Agent" and "Salesforce Summary Agent", user task "Curate contact and Validate", end event "Process '
       'Complete".',
  bq='Tooltip "Click to add a breakpoint" on a process element',
  ai='Four of the process steps are agents, named as such on the canvas and annotated: "UiPath Agent - '
     'Contact Validation before proceeding to next steps", "Langchain Company research Agent", "UiPath '
     'Lead Scoring Agent", "Salesforce Agent to get Contact summary details". The execution trail lists '
     '"Contact-Validation-Agent (Service task)" followed by "Agent run - Contact Validation Agent".',
  aq='Agent run - Contact Validation Agent',
  caps=[('maestro-docs-image-587615', 'png', 'the whole agent process canvas with the debug trail')]),
 'instance-diagram-view': dict(v='INCLUDE',
  note='Instance diagram view of the same agent process, with execution counts and a P50 heatmap; the agent '
       'tasks and their markers stay visible. Read at native resolution.',
  bpmn='BPMN diagram of the process Maestro.Contact.to.Opportunity rendered as an instance diagram view: '
       'per-element execution counts, P50 heatmap shading, exclusive/parallel gateways, message start event, '
       'end event "Process Complete".',
  bq='Heatmap view with elements shaded from blue (shortest) to red (longest) based on P50 duration',
  ai='Agent service tasks "Contact-Validation-Agent" (circular agent marker on the card), "Langchain - '
     'Company Research Agent", "Lead Scoring Agent", "Salesforce Summary Agent", each with an agent bracket '
     'annotation.',
  aq='Screenshot of the instance diagram view with a heatmap',
  caps=[('maestro-docs-image-588287', 'png', 'the heatmap instance view of the agent process')]),
 'references-templates': dict(v='INCLUDE',
  note='Downloads page publishing three BPMN 2.0 model files; the invoice model contains a textAnnotation '
       '"(Agent) Dispute investigation and resolution" next to its service task.',
  bpmn='Published .bpmn 2.0 XML: bpmn:definitions with the uipath namespace, bpmn:process isExecutable='
       '"false", serviceTask/userTask/sendTask/receiveTask/manualTask, exclusiveGateway/parallelGateway/'
       'eventBasedGateway, boundaryEvent, intermediateCatchEvent, bpmndi diagram interchange.',
  bq='bpmn:process id="Process_1" isExecutable="false"',
  ai='Invoice_Processing_Template.bpmn carries the text annotation "(Agent) Dispute investigation and '
     'resolution" (sibling annotations: "(Automation) 2-way matching process", "(Action Center) App Task '
     'form ...", "(Integration Service) Send email", "(Business Rule) decision table ...").',
  aq='(Agent) Dispute investigation and resolution',
  caps=[('Invoice_Processing_Template.bpmn', 'bpmn', 'the published invoice model (contains the Agent annotation)'),
        ('Loan_Processing_Template.bpmn.bpmn', 'bpmn', 'the published loan model'),
        ('Supplier_Onboarding_Template.bpmn.bpmn', 'bpmn', 'the published supplier-onboarding model')]),
 'using-agents-in-maestro@s': dict(v='INCLUDE',
  note='The 2.2510 line publishes a page whose whole subject is agents as BPMN service tasks, with the '
       'properties panel showing the agent binding. The Cloud URL of the same slug redirects to '
       'integrating-systems-and-data, so this artefact exists on the 2.2510 line only.',
  bpmn='BPMN service task "VALIDATE against State requirement" shown in the Studio Web properties panel of '
       'the Maestro BPMN modeller (Service task, General, Implementation, Inputs, Outputs, Update '
       'variables).',
  bq='Properties panel of a Service task named VALIDATE against State requirement',
  ai='The panel sets Action = "Start and wait for agent" with an "Agent *" selector under it; the page '
     'states "Agents are represented in Maestro BPMN workflows as Service Tasks."',
  aq='Agents are represented in Maestro BPMN workflows as Service Tasks.',
  caps=[('maestro-start-and-wait-for-agent-properties-587972', 'png', 'Service task, Action = Start and wait for agent'),
        ('maestro-start-and-wait-for-agent-properties2-587968', 'png', 'the second agent properties capture')]),
 'errors-and-recovery@s': dict(v='INCLUDE',
  note='The 2.2510 page publishes a BPMN error-handling diagram whose service task carries the agent '
       'marker; the Cloud page of the same slug has a different (smaller) figure set.',
  bpmn='BPMN diagram: start event, service task "Sync data" with an agent marker and an error event on its '
       'boundary, task "Increment retry counter", exclusive gateway "Retry limit reached?", user task '
       '"Escalate issue", end events "Synced" and "Escalated", plus a "No, retry" loop-back flow.',
  bq='A service task with a retry loop and a final escalation path.',
  ai='The service task "Sync data" carries the circular UiPath agent marker on its bottom edge (same glyph '
     'as on the explicitly agent-named tasks elsewhere in this source).',
  aq='A service task with a retry loop and a final escalation path.',
  visual=True,
  caps=[('620687', 'png', 'the retry-loop diagram; "Sync data" carries the agent marker')]),
 'align-and-connect-bpmn-elements': dict(v='EXCLUDE', code='E2-no-ai-element',
  note='BPMN canvas fragments showing alignment/connection mechanics; the only AI mention is about the '
       'editing tool, not about an element.',
  ai='the page says alignment is "especially useful when building complex workflows with branching logic, '
     'agent calls, or queues", i.e. a mention of agent calls as a workflow feature, not an element in the '
     'diagram shown on the page'),
 'december-2025': dict(v='EXCLUDE', code='E2-no-ai-element',
  note='Release-note page with one BPMN canvas fragment (an event subprocess with a start event); every AI '
       'mention is Autopilot design-time assistance.',
  ai='the AI mentions are Autopilot: "You can use Autopilot to generate an initial BPMN model from a '
     'written description or supporting files", i.e. AI that writes the diagram, not AI inside it'),
 'january-2026': dict(v='EXCLUDE', code='E1-not-bpmn',
  note='Release-note page whose two figures are instance-management UI captures; no process diagram.',
  ai='the AI mentions are Autopilot for Script tasks and "Agents, RPA jobs, or other orchestrated '
     'activities" invoked downstream, i.e. product features listed in a changelog'),
 'subprocesses-and-modularity': dict(v='EXCLUDE', code='E2-no-ai-element',
  note='BPMN subprocess/call-activity example diagrams with no AI element.',
  ai='every AI mention is the project type: "Call activities are supported for invoking a separate agentic '
     'process (project)", i.e. the name of the Studio project, not an element in the diagram'),
 'pools-and-lanes': dict(v='EXCLUDE', code='E2-no-ai-element',
  note='BPMN pool and lane example diagrams; no AI element.',
  ai='the single AI mention is "foundational for understanding responsibility boundaries in cross-'
     'functional and agentic processes", i.e. the project type again'),
 'introduction-to-maestro-case': dict(v='EXCLUDE', code='E1-not-bpmn',
  note='One case-lifecycle illustration (stage containers), not a BPMN diagram.',
  ai='the AI mentions describe the Case capability ("dependent on human and AI agent judgment at key '
     'decision points"), not an element in the illustration'),
 'claims-processing': dict(v='EXCLUDE', code='E2-no-ai-element',
  note='BPMN diagram with pool/lane "Claims Department"; task cards use user, service and send task icons '
       'only - no agent marker anywhere. Read at native resolution.',
  ai='the page says "Integrate AI tools for document understanding, medical record analysis, and anomaly '
     'detection", i.e. a "How Maestro adds value" statement, not an element in the diagram'),
 'common-implementation-scenarios': dict(v='EXCLUDE', code='E0-no-artefact',
  note='The page names agent-orchestrated BPMN patterns ("Pattern: Service Task -> Start and wait for '
       'agent") but publishes no figure, no model file and no BPMN XML block, so there is no artefact to '
       'collect.',
  ai='the AI content is pattern prose: "Delegate a complex or intelligent task to an AI agent or planning '
     'system ... Pattern: Service Task -> Start and wait for agent"'),
 'node-human': dict(v='EXCLUDE', code='E1-not-bpmn',
  note='Flow node reference: the figures are the Human node properties panel and a schema editor, i.e. '
       'Maestro Flow UI, not a BPMN process model.',
  ai='the schema figure lists a field "Agent Confidence Score", i.e. agent data consumed by this Flow '
       'node, not an AI element inside a BPMN process'),
 'how-to-simple-process': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='The page publishes its completed BPMN diagram ("Final BPMN diagram of the completed simple process '
       'with gateway, two tasks, and two end events"). Read at native resolution: a manual start event, a '
       'delay, an exclusive gateway "Which path?", two blank task cards "A task" and "B task" (no task-type '
       'icon, no marker, no badge) and two end events. No AI element inside the process.',
  ai='the AI mention is a capability statement: "This guide demonstrates how to implement a simple process '
     'that highlights the core agentic orchestration capabilities", i.e. Maestro being agentic, not an '
     'element in the diagram'),
 'understanding-process-implementation': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='One BPMN process diagram ("Purchase request approval process diagram"). Read at native resolution: '
       'manual start "Request Submitted", two user tasks (person icon) "Manager review" and "CFO approval", '
       'two exclusive gateways, a service task (gear icon) "Trigger PO Creation", a send task (envelope '
       'icon) "Email Requester", end event "Process Complete", with a 24h escalation boundary timer. The '
       'task-type icons are the only badges on the cards: no circular agent marker anywhere.',
  ai='the AI mention is a concept statement: "Process implementation in Maestro: converting a BPMN model '
     'into an executable agentic workflow with runtime ins...", i.e. what the platform does with any model'),
 'sequence-flows': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='BPMN canvas fragment: start event, one blank task card, an exclusive gateway with the properties '
       'panel open (Conditions, Flow A/Flow B labels, "amount > 10000"), and two named task cards "Task A" '
       'and "Task B". Read at native resolution: no task-type icon and no agent marker on the cards.',
  ai='the AI mention is a scope statement: "defining execution order between tasks, events, and gateways '
     'and orchestrating work across agents, robots, and humans", i.e. what sequence flows do in general'),
 'subprocess': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='BPMN subprocess model (OuterSP) with call activities. Read at native resolution: send-task cards '
       '"List All Users" and "List All Messages" and a selected multi-instance "InnerTask" inside the '
       'subprocess, properties panel open with Implementation > Action still unset ("Select..."). The '
       'cards carry task-type icons and, at the bottom-right corner, a small blue square badge; that badge '
       'is not the circular agent marker (it is on every executable card here, including ones with no '
       'action configured). No agent element.',
  ai='the AI mention is about the project type invoked by a call activity: "Such an agentic process, with '
     'an independent lifecycle, can be invoked as a call activity", i.e. the Studio project, not an element '
     'in this diagram'),
 'repetition': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='Primer page on repeating a task. Read at native resolution: start event, service task (gear icon) '
       '"Get list of invoices", user task (person icon) "Approve invoice payout" carrying the parallel '
       'multi-instance marker (the bar glyph at the bottom of the card), then the end event. The page '
       'carries no AI vocabulary at all and the cards carry no agent marker.',
  ai='none - the page carries no AI vocabulary at all'),
 'messages-and-updates': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='BPMN primer diagram for non-interrupting boundary messages. Read at native resolution: user tasks '
       '(person icon) "Deliverable Preparation", "Review rule change", "Log new requirements" and service '
       'tasks (gear icon) "Update compliance checklist", "Adjust project plan", with two message boundary '
       'events (envelope in a dashed circle) and their end events. No agent marker on any card; the page '
       'carries no AI vocabulary at all.',
  ai='none - the page carries no AI vocabulary at all'),
 'gateways-flow-logic': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='Primer page on gateways; the figure is an exclusive-gateway diagram with the routing logic and the '
       'gateway properties panel. The page carries no AI vocabulary at all.',
  ai='none - the page carries no AI vocabulary at all'),
 'events-in-bpmn-modeling-perspective': dict(v='EXCLUDE', code='E2-no-ai-element', j=True,
  note='Primer page on BPMN events: the figures are the event icons and event diagrams (message start '
       'event, timer start events, message catch event, entry point). Events carry no implementation, and '
       'the page carries no AI vocabulary at all.',
  ai='none - the page carries no AI vocabulary at all'),
 'all-instances-view': dict(v='EXCLUDE', code='E1-not-bpmn', j=True,
  note='No process model: the figure is the Maestro "Process instances" dashboard (a table of process '
       'names with Running/Completed/Faulted/Total/Versions/Location counts plus a stacked bar chart and '
       '"Top processes by instances/duration" lists), captured at native resolution. The alt text calls it '
       'a "BPMN instances view" but the artefact is a dashboard, not BPMN notation. It does name the three '
       'agent-bearing processes of this source (Loan.Origination.and.Review, Invoice.to.PO.Match, '
       'Maestro.Contact.to.Opportunity) as rows.',
  ai='none - the page carries no AI vocabulary at all'),
 'all-incidents-view': dict(v='EXCLUDE', code='E1-not-bpmn', j=True,
  note='No process model: the figure is the Maestro incidents table view (faulted instances grouped by '
       'error message). The alt says "BPMN incidents view" but the artefact is a user-interface table.',
  ai='none - the page carries no AI vocabulary at all'),
 'process-overview-homepage': dict(v='EXCLUDE', code='E1-not-bpmn', j=True,
  note='Process monitoring landing page: every figure is a dashboard, table or dialog (all active '
       'instances, incidents table, processes list, instance dashboards, retry/migrate/move dialogs, '
       'instance view). No process model is published.',
  ai='the AI mention is about the execution trail feature: "each step in the process\'s execution, '
     'including hierarchical steps such as agents and subprocesses", i.e. how the trail renders nested '
     'runs, not an element shown in a diagram on this page'),
 'monitoring-dashboard': dict(v='EXCLUDE', code='E1-not-bpmn', j=True,
  note='Monitoring dashboards and analytics views (execution count, duration, heatmap), not process '
       'models.',
  ai='none - the page carries no AI vocabulary at all'),
 'case-instances-view': dict(v='EXCLUDE', code='E1-not-bpmn', j=True,
  note='Maestro Case instance view (case dashboard), not BPMN notation; the case canvas is a '
       'CMMN-style stage model, which is a different notation from BPMN 2.0.',
  ai='none - the page carries no AI vocabulary at all'),
 'case-incidents-view': dict(v='EXCLUDE', code='E1-not-bpmn', j=True,
  note='Maestro Case incidents view (case dashboard), not BPMN notation.',
  ai='none - the page carries no AI vocabulary at all'),
 'markers-implementation@s': dict(v='INCLUDE',
  note='The 2.2510 revision of the multi-instance markers page. Its own figures are the marker diagrams '
       '(markers, marker on a task, subprocess marker, example multi instance) rather than the Cloud '
       'revision\'s agent-bound properties-panel capture, but it carries the same implementation step in '
       'its prose, so the agent-bound BPMN task is documented on this line too. Recorded separately rather '
       'than folded into the Cloud row because the figures differ; the two pages are revisions of one '
       'topic and the researcher may want to merge them.',
  bpmn='BPMN task cards with markers (element toolbar with "Select markers", a marker on a task, a '
       'subprocess marker, an example multi-instance task), i.e. BPMN 2.0 element diagrams.',
  bq='Use markers to configure the execution of a certain task type to create multiple executions of that '
     'task by iterating over a List variable',
  ai='The page instructs the reader to bind the multi-instance BPMN service task to an agent: "Action: '
     'Start and wait for agent Agent: your invoice validation agent".',
  aq='Action: Start and wait for agent Agent: your invoice validation agent',
  caps=[('example-multi-instance', 'png', 'the multi-instance example diagram on the 2.2510 page'),
        ('subprocess_marker', 'png', 'the subprocess marker diagram')]),
}

# 2.2510 URLs that are the same docs page as a Cloud URL although their figure sets differ
# (different publication revisions of one page): the agent-bearing diagram is the same file.
SUITE_E3 = {
 'how-to-complex-process': ('how-to-complex-process',
  'The 2.2510 revision of the same page publishes the same invoice process diagram file '
  '(maestro-process-diagram-599989) as the automation-cloud revision, so the diagram is already recorded. '
  'The two revisions differ in surrounding figures (the 2.2510 one adds intermediate-event captures).'),
}

UNCERTAIN_NOTE = (
 'Reference page for one BPMN task type. The page\'s figures are the BPMN task icon and Studio Web '
 'properties panels, one of which is the Action dropdown; that dropdown lists agent actions, so the page '
 'documents which implementations a BPMN task of this type can be bound to. It is not a process diagram, '
 'which is why it is not recorded as a plain include.')
UNCERTAIN_QUESTION = (
 'Is a Studio Web properties-panel screenshot showing the Action list of a BPMN task (including "Start and '
 'wait for agent" and "Start and wait for external agent") an acceptable process artefact for this source, '
 'or does it fail E1-not-bpmn because it is not a process diagram? The same question covers the other five '
 'task-reference pages in this ledger.')
for _slug in ('business-rule-task', 'receive-task', 'script-task', 'send-task', 'service-task', 'user-task'):
    MANUAL[_slug] = dict(v='UNCERTAIN', note=UNCERTAIN_NOTE, ruling=True, question=UNCERTAIN_QUESTION,
        bpmn='The BPMN element itself (its task-type icon) plus the Studio Web properties panels of that '
             'element: General, the Action dropdown under Implementation, Inputs, Outputs, "Add new" and '
             'the "Set variable value" option.',
        bq='Available actions dropdown in the ' + _slug.replace('-', ' ').title() + ' Properties panel',
        ai='The Action dropdown lists "Start and wait for agent", "Start and wait for external agent", '
           '"Start agentic process" and "Start and wait for agentic process"; the page text reads "Start and '
           'wait for agent  Starts a UiPath agent (a reusable logic block) and waits for it to finish '
           'execution."',
        aq='Start and wait for agent : Starts a UiPath agent (a reusable logic block) and waits for it to finish execution.',
        caps=[('properties-actions', 'png', 'the Action dropdown of this BPMN task type')])

# E3: urls that are the same docs page under another url (not in the sitemap / alias of a page)
DUP = {
 CLOUD + '/user-guide/introduction-to-maestro': (CLOUD + '/user-guide/overview',
  'Url is not in the product sitemap and resolves to the Overview page (status 200, final URL '
  '/user-guide/overview, canonical https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/'
  'overview, title "Overview").'),
 CLOUD + '/user-guide/process-monitoring': (CLOUD + '/user-guide/overview',
  'Url is not in the product sitemap and serves the Overview page with '
  '?fallbackReason=invalidTopic&isFallback=true (canonical .../user-guide/overview, title "Overview").'),
 CLOUD + '/user-guide/using-agents-in-maestro': (CLOUD + '/user-guide/integrating-systems-and-data',
  'The Cloud url of this slug serves the "Integrating systems and data" page (same title, canonical '
  '.../integrating-systems-and-data); the agent-tasks page itself is published on the 2.2510 line and is '
  'recorded there.'),
 CLOUD + '/user-guide/node-human-task': (CLOUD + '/user-guide/node-human',
  'Same title "Human" and the same two figures (node-human-configuration-panel, node-human-schema-fields) '
  'as /user-guide/node-human: one docs page under two urls.'),
}
# The two closure-only urls are not in scan.json (they serve the Overview page), so they are handled
# separately at the end of the row loop.
CLOSURE = [
 (CLOUD + '/user-guide/introduction-to-maestro', 'Introduction to Maestro',
  'Url is not in the product sitemap; fetched, it returns status 200 and serves the Overview page '
  '(final URL and canonical .../user-guide/overview, title "Overview"): one docs page under two urls, so '
  'the artefact is the one recorded for the Overview page.'),
 (CLOUD + '/user-guide/process-monitoring', 'Process monitoring',
  'Url is not in the product sitemap; fetched, it serves the Overview page with '
  '?fallbackReason=invalidTopic&isFallback=true (canonical .../user-guide/overview, title "Overview"): one '
  'docs page under two urls.'),
]


# ------------------------------------------------------------ record + capture writing
def capture(nnn, slug, url, cap):
    """Copy/convert one page asset into corpus/<slug>/NNN_*.png|.bpmn. Returns (filename, w, h)."""
    needle, kind, _desc = cap
    if kind == 'bpmn':
        src = None
        for f in os.listdir(XML):
            if needle.lower() in f.lower():
                src = os.path.join(XML, f)
        assert src, 'no model file for ' + needle
        name = '%03d_%s.bpmn' % (nnn, re.sub(r'[^A-Za-z0-9]+', '-', os.path.splitext(os.path.basename(src))[0]).strip('-').lower())
        shutil.copyfile(src, os.path.join(CORPUS, name))
        return name, None, None
    src = pick(url, needle)
    assert src, 'no figure %r on %s' % (needle, url)
    lp = local(src)
    if not os.path.exists(lp):                      # not yet in raw/img: plain GET, paced as usual
        import time as _t, urllib.request
        d = urllib.request.urlopen(urllib.request.Request(src, headers={
            'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}), timeout=45).read()
        io.open(lp, 'wb').write(d)
        _t.sleep(0.9)
    from PIL import Image
    im = Image.open(lp)
    try:
        im.seek(0)
    except Exception:
        pass
    im = im.convert('RGB')
    w, h = im.size
    base = re.sub(r'[^A-Za-z0-9]+', '-', os.path.splitext(os.path.basename(src))[0]).strip('-').lower()[:52].strip('-')
    name, k = '%03d_%s.png' % (nnn, base), 1
    while os.path.exists(os.path.join(CORPUS, name)):    # two captures of one record must not collide
        k += 1
        name = '%03d_%s-%d.png' % (nnn, base, k)
    im.save(os.path.join(CORPUS, name))
    return name, w, h


def record(nnn, url, tail, m):
    os.makedirs(CORPUS, exist_ok=True)
    caps = []
    for c in m['caps']:
        caps.append((c, capture(nnn, 'uipath-maestro-docs', url, c)))
    title = scan[url].get('t') or tail
    shots = [c[1][0] for c in caps if c[0][1] == 'png']
    xmls = [c[1][0] for c in caps if c[0][1] == 'bpmn']
    wmax = max([c[1][1] or 0 for c in caps] or [0])
    if xmls:
        q = 'legible'
    elif m.get('visual'):
        q = 'legible' if wmax >= 1200 else 'marginal'
    else:
        q = 'legible' if wmax >= 900 else 'marginal'
    body = ['---', 'n: %d' % nnn, 'source: uipath-maestro-docs',
            'source_name: UiPath Maestro user guide (docs.uipath.com)',
            'source_type: vendor documentation', 'title: %s' % title, 'url: https://docs.uipath.com' + url,
            'accessed: %s' % DATE, 'verdict: %s' % m['v'],
            'needs_human_ruling: %s' % str(bool(m.get('ruling'))).lower(),
            'question: %s' % (m.get('question') or 'null'),
            'needs_visual_check: %s' % str(bool(m.get('visual'))).lower(),
            'bpmn_evidence: "%s"' % m['bpmn'].replace('"', "'"),
            'bpmn_evidence_quote: "%s"' % m['bq'].replace('"', "'"),
            'ai_evidence: "%s"' % m['ai'].replace('"', "'"),
            'ai_evidence_quote: "%s"' % m['aq'].replace('"', "'"),
            'artefacts:',
            '  screenshot: %s' % (', '.join(shots) if shots else 'null'),
            '  archive: null',
            '  bpmn_xml: %s' % (', '.join(xmls) if xmls else 'null'),
            'duplicate_of: null', 'access: public',
            'capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page\'s own downloadable model file',
            'capture_quality: %s' % q, 'capture_width_px: %s' % (wmax or 'null'),
            'capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)',
            '---', '', '## What the page shows', '', 'Verbatim from the page:', '',
            '> "%s"' % page_quote(url), '']
    if m.get('note'):
        body += ['## Judgement', '', m['note'], '']
    body += ['## Artefact reading (native resolution unless stated)', '',
             '- **BPMN:** ' + m['bpmn'],
             '- **AI element:** ' + m['ai'], '']
    for c, (name, w, h) in caps:
        body.append('- `%s` - %s' % (name, c[2]))
    body += ['', '## Notes for the researcher', '',
             'Figure alt text on the page (verbatim): ' + ' | '.join(repr(a) for a in alts(url)[:6]), '']
    path = os.path.join(CORPUS, '%03d_%s.md' % (nnn, tail))
    io.open(path, 'w', encoding='utf-8').write('\n'.join(body))
    return 'corpus/uipath-maestro-docs/%03d_%s.md' % (nnn, tail)


# ------------------------------------------------------------ build rows
cloud = sorted(u for u in scan if u.startswith(CLOUD))
suite = sorted(u for u in scan if u.startswith(SUITE))
order = cloud + suite + [u for u, _t, _w in CLOSURE]
n_of = {u: i + 1 for i, u in enumerate(order)}
rows = []

# Every numbered file in the corpus directory is generated by this script, so clear the previous run's
# output first: names stay stable and a record can never pick up a stale capture.
os.makedirs(CORPUS, exist_ok=True)
for _f in os.listdir(CORPUS):
    if re.match(r'^\d{3}_', _f):
        os.remove(os.path.join(CORPUS, _f))


def slug_of(u):
    """Ledger/file tail for a url: the slug under /user-guide/, else a suite path tail."""
    if '/user-guide/' in u:
        t = u.split('/user-guide/', 1)[-1]
    else:
        t = 'suite' + u[len(SUITE):]
    t = re.sub(r'[^A-Za-z0-9.-]+', '-', t).strip('-')
    return t or 'suite-root'


def figset(u):
    return (tuple(sorted(os.path.basename(i['src']) for i in FIG.get(u, []))),
            tuple(sorted(files(u))))


def twin(u):
    """A 2.2510 url whose figure set and model-file set are identical to its Cloud url."""
    t = CLOUD + '/user-guide/' + slug_of(u)
    if t in scan and figset(u) == figset(t):
        return t
    return None


for u in order:
    n = n_of[u]
    if u not in scan:
        continue                      # the two closure-only urls are appended after this loop
    tail = slug_of(u)
    is_suite = u.startswith(SUITE)
    ttl = scan[u].get('t') or tail
    m = MANUAL.get(tail + '@s' if is_suite else tail)
    if u in DUP:
        target, why = DUP[u]
        rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                         reason='E3-duplicate', judgment=False, duplicate_of=n_of.get(target),
                         evidence='"The "Integrations" section on this page mirrors the "Integrations" '
                                  'section of the Overview." [' + why + ']',
                         record=None, needs_visual_check=False, needs_human_ruling=False, accessed=DATE))
        continue
    if is_suite and tail in SUITE_E3:
        ct, why = SUITE_E3[tail]
        rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                         reason='E3-duplicate', judgment=False,
                         duplicate_of=n_of.get(CLOUD + '/user-guide/' + ct),
                         evidence='"BPMN diagram of the invoice processing process showing all tasks, '
                                  'gateways, and flow paths" [' + why + ']',
                         record=None, needs_visual_check=False, needs_human_ruling=False, accessed=DATE))
        continue
    if m:
        if m['v'] == 'EXCLUDE':
            ai = m.get('ai') or ai_mention(u, drop=(r'cookie',)) or \
                 'none - the page carries no AI vocabulary at all'
            ev = '"%s" [%s; dismissed AI mention: %s]' % (page_quote(u), m.get('note', ''), ai)
            rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                             reason=m['code'], judgment=bool(m.get('j', True)), evidence=ev, record=None,
                             needs_visual_check=False, needs_human_ruling=False, accessed=DATE))
        else:
            rec = record(n, u, tail, m)
            ev = '"%s" [%s]' % (m['aq'], m['note'])
            rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict=m['v'],
                             reason=None, judgment=True, evidence=ev, record=rec,
                             needs_visual_check=bool(m.get('visual', False)),
                             needs_human_ruling=bool(m.get('ruling', False)),
                             question=m.get('question'), accessed=DATE))
        continue
    tw = twin(u) if is_suite else None
    if tw:
        ev = ('"%s" [2.2510 page with the same slug, title and figure files as its automation-cloud '
              'twin %s - one docs page under two urls]' % (' | '.join(alts(u))[:180] or ttl, tw)) \
            if FIG.get(u) else \
            ('"%s" [same slug and title on the 2.2510 line as on the automation-cloud line, and neither '
             'page carries a figure or a model file - one docs page under two urls]' % page_quote(u))
        rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                         reason='E3-duplicate', judgment=False, duplicate_of=n_of[tw],
                         evidence=ev, record=None, needs_visual_check=False,
                         needs_human_ruling=False, accessed=DATE))
        continue
    # mechanical families
    kind = figure_kind(u)
    if not FIG.get(u) and not files(u) and not any(re.search(r'<(?:bpmn:)?\w*(?:Task|Event|Gateway|process)\b', p)
                                                   for p in (scan[u].get('pre') or [])):
        ai = ai_mention(u, drop=(r'cookie',))
        ev = '"%s" [no figure, no BPMN XML code block and no downloadable model on the page%s]' % (
            page_quote(u), '; the page AI mention is ' + ai if ai else '')
        rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                         reason='E0-no-artefact', judgment=False, evidence=ev, record=None,
                         needs_visual_check=False, needs_human_ruling=False, accessed=DATE))
        continue
    a = ' | '.join(alts(u))[:220]
    ai = ai_mention(u, drop=(r'cookie',))
    if kind == 'bpmn':
        ev = '"%s" [BPMN figure(s) with no AI element inside the process; dismissed AI mention: %s]' % (
            a, ai if ai else 'none - the page carries no AI vocabulary at all')
        code = 'E2-no-ai-element'
    else:
        ev = '"%s" [figures are %s, not BPMN notation; dismissed AI mention: %s]' % (
            a, notation_note(u), ai if ai else 'none - the page carries no AI vocabulary at all')
        code = 'E1-not-bpmn'
    rows.append(dict(n=n, url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                     reason=code, judgment=False, evidence=ev, record=None,
                     needs_visual_check=False, needs_human_ruling=False, accessed=DATE))

# the two closure-only urls: fetched, they serve the Overview page, so the artefact is the Overview page
for u, ttl, why in CLOSURE:
    rows.append(dict(n=n_of[u], url='https://docs.uipath.com' + u, title=ttl, verdict='EXCLUDE',
                     reason='E3-duplicate', judgment=False,
                     duplicate_of=n_of[CLOUD + '/user-guide/overview'],
                     evidence='"%s" [%s]' % (page_quote(CLOUD + '/user-guide/overview'), why),
                     record=None, needs_visual_check=False, needs_human_ruling=False, accessed=DATE))

# ------------------------------------------------------------ write ledger + frontier
header = {
 'type': 'header', 'source': 'uipath-maestro-docs',
 'source_name': 'UiPath Maestro user guide (docs.uipath.com)',
 'source_type': 'vendor documentation', 'census': True, 'population_size': len(order),
 'enumeration_method':
  'Vendor sitemap + link-union closure, no keyword filter. The docs.uipath.com sitemap index lists 329 '
  'sitemaps; the one for this product is https://docs.uipath.com/products/maestro/sitemaps/en/sitemap.xml '
  'and it yields 317 urls: 222 under /maestro/automation-cloud/latest (Automation Cloud line) and 95 under '
  '/maestro/automation-suite/2.2510 (Automation Suite line). Both lines are enumerated (deliberate '
  'over-inclusion: 15 of the 95 pages differ from their Cloud counterpart and are judged in their own '
  'right, the other 80 are the same page under two urls and are E3 rows). The link union of the crawled '
  'pages adds 4 pages the sitemap omits '
  '(automate-getting-started, choosing-maestro-orchestrate-or-maestro-automate, '
  'maestro-automate-capabilities-comparison, node-human) and 2 closure-only urls that redirect to '
  '/user-guide/overview (introduction-to-maestro, process-monitoring). 226 + 95 + 2 = 323 rows. The '
  'English tree is the one enumerated (/de/ is a lagging translation of it; the docs themselves warn that '
  'localisation lags), so the German tree carries no artefact the English tree lacks. academy.uipath.com is '
  'a different property and is not part of this source.',
 'entry_points': [
   'https://docs.uipath.com/products/maestro/sitemaps/en/sitemap.xml',
   'https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/overview',
   'https://docs.uipath.com/maestro/automation-suite/2.2510/user-guide/overview'],
 'access': 'public, no login', 'date_start': DATE, 'date_end': DATE, 'agent_model': 'claude',
 'browser_tool': 'mcp cdp1 (own tab) + python urllib paced ~1 req/s',
 'queries': ['none - full enumeration, no keyword filter'],
 'note': 'Page = enumeration unit. Evidence order per rule 5: published .bpmn XML, then the page\'s own '
         'figure alt text and figure assets (alt text on this docs site is descriptive English, e.g. '
         '"BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths"), '
         'then native-resolution reading of the .webp asset. Figures are captured as the page asset at its '
         'native URL (never a screenshot of the rendered page). The UiPath agent marker on a BPMN task card '
         'is a small circular badge with a zigzag glyph at the bottom edge of the task; it was verified '
         'against three tasks that are also agent-labelled in text ("Resolve discrepancies" bracketed '
         '"Agent", "Invoice Dispute Analysis (3rd Party AI Agent)", "Contact-Validation-Agent"). It is '
         'distinct from the two other card markings: the task-type icon in a rounded square at the top left '
         '(person = user task, gear = service task, envelope = send task, shown side by side on '
         'understanding-process-implementation) and the marker glyphs at the bottom edge (multi-instance, '
         'loop, ad-hoc). A small blue square badge at the bottom right is NOT the agent marker: it appears '
         'on every executable card of the subprocess primer page, including cards whose Implementation > '
         'Action is still unset. The mechanical E2 family (a BPMN figure with no agent badge and an AI '
         'mention about the platform rather than an element) was calibrated by reading these primer '
         'diagrams at native resolution: how-to-simple-process, understanding-process-implementation, '
         'sequence-flows, subprocess, repetition, messages-and-updates, all-instances-view; none of their '
         'task cards carries an agent marker.',
}
footer = {
 'type': 'footer', 'date_end': DATE,
 'rows': len(rows), 'status': 'DONE',
 'include': sum(1 for r in rows if r['verdict'] == 'INCLUDE'),
 'uncertain': sum(1 for r in rows if r['verdict'] == 'UNCERTAIN'),
 'exclude': {}, 'blocked': 0,
 'judgement_exclusion_share': '', 'self_audit_flips': 0,
}
for r in rows:
    if r['verdict'] == 'EXCLUDE':
        footer['exclude'][r['reason']] = footer['exclude'].get(r['reason'], 0) + 1
judged_ex = sum(1 for r in rows if r['verdict'] == 'EXCLUDE' and r.get('judgment'))
footer['judgement_exclusion_share'] = '%d judgement EXCLUDE rows of %d (%.1f%%)' % (
    judged_ex, len(rows), 100.0 * judged_ex / len(rows))

with io.open(LEDGER, 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(header, ensure_ascii=True) + '\n')
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=True) + '\n')
    fh.write(json.dumps(footer, ensure_ascii=True) + '\n')
io.open(FRONTIER, 'w', encoding='utf-8').write('\n'.join(r['url'] for r in rows) + '\n')

print('rows', len(rows), 'include', footer['include'], 'uncertain', footer['uncertain'])
print('exclude', footer['exclude'], footer['judgement_exclusion_share'])
print('records', len([r for r in rows if r['record']]))

