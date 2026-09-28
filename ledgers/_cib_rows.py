# -*- coding: utf-8 -*-
"""Build the cib-seven census: ledger rows, frontier, records and captures.

population (591) = 467 pages of docs.cibseven.org/manual/latest/ (global sidebar
order, ledgers/cib.raw/nav_latest.txt) + 124 urls of the cibseven.org marketing
site (Yoast sitemap index: page-sitemap 80, academy 12, galleryui 28, category 4;
de/en/es/pt).  Rows n=1..467 are docs, n=468..591 marketing (sorted url order).

Verdicts, in this order (first match wins):
  1. MANUAL_DOCS    the collected docs pages, judged by hand.
  2. JUDGED         pages whose exclusion had to be argued (judgment=true).
  3. DMN section    E1-not-bpmn  - the section title declares DMN 1.x.
  4. CMMN section   E1-not-bpmn  - the section title declares CMMN 1.1.
  5. BPMN XML       E2-no-ai-element - the page publishes BPMN 2.0 XML in a code
                    block (tight element-name match, so deployment descriptors and
                    processes.xml do not count).  The snippet is quoted.
  6. figures, and the figures are application UI / architecture / ERD / IDE
                    screenshots   E1-not-bpmn
  7. figures that are BPMN diagrams or BPMN element notation  E2-no-ai-element
  8. otherwise      E0-no-artefact (no figure, no BPMN XML, no model file)

judgment=true exactly when the page's own content names AI/LLM/agent (the dismissal
then had to be argued) or the page is in JUDGED/MANUAL_*; mechanical otherwise.
E3-duplicate is used only between language twins of the marketing site.
"""
import io, json, os, re, shutil
from collections import Counter
from PIL import Image

RAW = 'ledgers/cib-seven.raw'
NAV = 'ledgers/cib.raw/nav_latest.txt'
DOCS = 'https://docs.cibseven.org'
MKT = 'https://cibseven.org'
ACCESSED = '2026-09-25'
OUT = 'ledgers/cib-seven.jsonl'
FRONTIER = 'ledgers/cib-seven.frontier.txt'
CORPUS = 'corpus/cib-seven'
IMGDIR = {'doc': os.path.join(RAW, 'img'), 'mkt': os.path.join(RAW, 'mimg')}

# BPMN 2.0 element names; a trailing delimiter is required so that
# <process-archive> (a deployment descriptor) does not match <process>.
E_BPMN = re.compile(
    r'<(?:bpmn:)?(?:serviceTask|userTask|manualTask|scriptTask|sendTask|receiveTask|'
    r'businessRuleTask|callActivity|subProcess|startEvent|endEvent|intermediate\w+|'
    r'boundaryEvent|exclusiveGateway|parallelGateway|inclusiveGateway|eventBasedGateway|'
    r'complexGateway|sequenceFlow|definitions|process|collaboration|participant|laneSet|'
    r'lane|dataObject|textAnnotation|eventDefinition)[\s/>]')

CONTENT = {}

# --------------------------------------------------------------- MANUAL (docs)
MANUAL_DOCS = {
    '/manual/latest/reference/connect/ai-agent-connector/getting-started/': {
        'verdict': 'INCLUDE', 'reason': None, 'slug': 'ai-agent-connector-getting-started',
        'evidence': '"<bpmn:serviceTask id=\\"Task_Summarize\\" name=\\"Summarize feedback\\" camunda:modelerTemplate=\\"org.cibseven.connect.ai.agent\\" ...> ... <camunda:connectorId>cibseven-ai-agent</camunda:connectorId>"',
        'bpmn_evidence': ('the page publishes the BPMN 2.0 XML of a service task bound to the AI Agent connector: '
                          '<bpmn:serviceTask id="Task_Summarize" name="Summarize feedback" '
                          'camunda:modelerTemplate="org.cibseven.connect.ai.agent" camunda:modelerTemplateVersion="1" '
                          'implementation="##WebService"> with <bpmn:extensionElements><camunda:connector> and '
                          '<camunda:connectorId>cibseven-ai-agent</camunda:connectorId>. The XML is the page\'s own '
                          'published artefact, copied verbatim into the .bpmn capture next to this record.'),
        'bpmn_quote': 'bpmn:serviceTask id="Task_Summarize" name="Summarize feedback" camunda:modelerTemplate="org.cibseven.connect.ai.agent"',
        'ai_evidence': ('the AI element is inside the process: the service task is bound to the AI Agent connector '
                        '(cibseven-ai-agent) and carries the agent parameters agentName=Summarizer, instruction '
                        '"Summarize the core concern in 10 words or less.", apiKey and the output parameter '
                        'summaryResult.'),
        'ai_quote': 'camunda:connectorId>cibseven-ai-agent / inputParameter name="agentName">Summarizer / instruction>Summarize the core concern in 10 words or less.',
        'xml_file': os.path.join(RAW, 'xml', 'getting-started_0.xml'),
        'note': ('There is no diagram on this page: the collectible artefact is the published BPMN XML itself, which '
                 'is why the capture is a .bpmn file rather than a screenshot.'),
    },
    '/manual/latest/reference/connect/ai-agent-connector/examples/': {
        'verdict': 'UNCERTAIN', 'reason': None, 'slug': 'ai-agent-connector-examples',
        'evidence': '"<camunda:inputParameter name=\\"agentName\\">InvoiceExtractor</camunda:inputParameter> <camunda:inputParameter name=\\"instruction\\">Extract the invoice as JSON..."',
        'bpmn_evidence': ('the page publishes four XML blocks, each the <camunda:connector> / <camunda:inputOutput> '
                          'extension-element configuration of one AI-agent service task (agentName InvoiceExtractor; '
                          'McpAgent with mcpServers; Orchestrator with toolClasses '
                          '...ProcessStarterTool; and a chat-memory variant with useChatMemory/memoryId). The blocks '
                          'are BPMN extension elements, but the page prints them as fragments: it does not show the '
                          'enclosing <bpmn:serviceTask> element that the getting-started page shows. Copied verbatim '
                          'into the .bpmn capture next to this record.'),
        'bpmn_quote': 'camunda:inputParameter name="agentName">InvoiceExtractor</camunda:inputParameter>',
        'ai_evidence': ('the AI elements are inside the process configuration: four configured agents (invoice '
                        'extraction with a JSON output schema, an MCP-server agent, an orchestrator that starts '
                        'another process as a tool, and an agent with chat memory).'),
        'ai_quote': 'inputParameter name="agentName">McpAgent ... inputParameter name="mcpServers">[{"name": "engine", "url": "http://localhost:8080/mcp"}]',
        'xml_file': os.path.join(RAW, 'xml', 'examples.xml'),
        'needs_human_ruling': True,
        'question': ('This page prints the <camunda:connector> extension-element XML of four AI-agent service tasks '
                     'but not the enclosing <bpmn:serviceTask> element that the getting-started page prints. Does a '
                     'connector-configuration fragment count as a collected process artefact, or does only the full '
                     'BPMN element count?'),
    },
    '/manual/latest/reference/connect/ai-agent-connector/rag/': {
        'verdict': 'UNCERTAIN', 'reason': None, 'slug': 'ai-agent-connector-rag',
        'evidence': '"<camunda:connector> <camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId> ... <camunda:inputParameter name=\\"content\\">${documentText}</camunda:inputParameter>"',
        'bpmn_evidence': ('the page publishes the BPMN extension-element XML of the service task that ingests '
                          'documents into the knowledge base: <camunda:connector> with '
                          '<camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId>, input parameters '
                          'content=${documentText}, source=${documentSource}, pgHost, pgDatabase, pgUser and output '
                          'parameter ingestedChunks=${chunksIngested}. Same shape as the examples page: connector XML '
                          'without the enclosing <bpmn:serviceTask>. Copied verbatim into the .bpmn capture next to '
                          'this record.'),
        'bpmn_quote': 'camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId>',
        'ai_evidence': ('the AI element is the knowledge-ingestor connector inside the process: it is the retrieval '
                        'step that feeds the agent, configured (content, chunking, embedding) inside a service task.'),
        'ai_quote': 'inputParameter name="content">${documentText} (cibseven-knowledge-ingestor connector configuration)',
        'xml_file': os.path.join(RAW, 'xml', 'rag_0.xml'),
        'needs_human_ruling': True,
        'question': ('Same question as the examples page: this is the connector XML of a knowledge-ingestor service '
                     'task, published without the enclosing <bpmn:serviceTask>. Collected as a process artefact or '
                     'not?'),
    },
    '/manual/latest/webapps/cockpit/bpmn/process-instance-chat/': {
        'verdict': 'INCLUDE', 'reason': None, 'slug': 'process-instance-agent-chat',
        'evidence': '"Agent Chat is not an interactive chat with an AI about the process instance - it is the recorded history of every AI Agent Connector session"',
        'bpmn_evidence': ('the page publishes cockpit-instance-agent-chat.png (3840x2482, read at native resolution '
                          'in four tiles): the Cockpit Process Instance view with a rendered BPMN diagram of the '
                          'definition key "ai-agent-with-human", name "Human in the AI Agent Loop". Pool "AI Process" '
                          'runs Start Event > "User Input" > "Call AI Agent" > "Show AI Output" > End Event; pool '
                          '"Human in the AI Agent Loop" runs "Start Event AI" > gateway > "AI Agent Call" > gateway '
                          '"One Shot?" (labels "yes - no review" / "no - with review") > "Review AI Result" > gateway '
                          '"Is result approved?" (Yes / No) > "End Event AI". BPMN 2.0 shapes with sequence flows and '
                          'exclusive gateways; the bpmn.io renderer mark is visible bottom right. Captured next to '
                          'this record.'),
        'bpmn_quote': 'Pool "AI Process": User Input, Call AI Agent, Show AI Output. Pool "Human in the AI Agent Loop": AI Agent Call, One Shot?, Review AI Result, Is result approved?',
        'ai_evidence': ('the AI elements are inside the process: both pools exist to run and review the agent - the '
                        'service tasks "Call AI Agent" / "AI Agent Call" are the AI Agent Connector calls, and "Show '
                        'AI Output" / "Review AI Result" are the human steps that read the result. The right-hand '
                        'Agent Chat panel shows the recorded session for the instance: a Request bubble, an "AI '
                        'Agent" bubble carrying {"text": "...", "thinking": null}, and a Response bubble.'),
        'ai_quote': 'Agent Chat panel: Request / "AI Agent" {"text": "BPMN (Business Process Mo... interactions are clear.", "thinking": null} / Response "BPMN is a standardized way to diagram business processes."',
        'captures': [('doc', '281_webapps_cockpit_img_cockpit-instance-agent-chat.png', 'process-instance-agent-chat')],
        'note': ('This is the only page in the manual whose figure shows an AI agent *inside a rendered BPMN '
                 'diagram* rather than in a table or a code block.'),
    },
    '/manual/latest/webapps/modeler/user-guide/bpmn-ai-chat/': {
        'verdict': 'INCLUDE', 'reason': None, 'slug': 'bpmn-ai-agent',
        'evidence': '"The BPMN AI Agent adds an LLM-powered chat assistant to CIB seven Modeler."',
        'bpmn_evidence': ('two of the seven figures carry the artefact, both read at native resolution in tiles. '
                          'bpmn-ai-chat-overview.png (3454x1930) is the Modeler canvas on the process "Machine Part '
                          'Per...": start event > "Submit Permit Request" > "Screen Part Compliance" > "Derive '
                          'Compliance Verdict" > gateway "Compliant without warnings?" > "Issue Permit Automatically". '
                          'The properties panel beside it is headed "CIB SEVEN - AI AGENT / Screen Part Compliance", '
                          'with Template "Applied", Name "CIB seven - AI Agent", Version 1, Description "Element '
                          'template for the cibseven-ai-agent connector." and Input "Agent name: Compliance Auditor '
                          'Agent". bpmn-ai-chat-diff.png (5124x2378) is the Modeler on the process "Customer Onboa...": '
                          '"Perform Automated KYC" > gateway "KYC Verification Outcome?" > gateway "Approval Join" > '
                          '"Complete Customer Onboarding" (selected service task, Template "+ Select") > end event '
                          '"Onboarding Completed". BPMN 2.0 shapes with sequence flows and exclusive gateways; the '
                          'bpmn.io renderer mark is visible. Three figures are captured next to this record.'),
        'bpmn_quote': 'properties panel "CIB SEVEN - AI AGENT / Screen Part Compliance", Template "Applied", Name "CIB seven - AI Agent", Description "Element template for the cibseven-ai-agent connector."',
        'ai_evidence': ('the AI element is inside the process: the service task "Screen Part Compliance" carries the '
                        'applied element template "CIB seven - AI Agent" (the cibseven-ai-agent connector) with agent '
                        'name "Compliance Auditor Agent" and prompt "Screen the following machine part permit request '
                        'against the compliance guidelines.", and the model is annotated "AI Agent auditor: declares '
                        'the part compliant only when there are zero warnings; otherwise it flags the request for a '
                        'supervisor." The same page also documents the design-time agent (panel "BPMN Agent BETA", '
                        '"Review changes", "Changes applied") whose proposal names the connector parameters '
                        'agentName, message, instruction, instructionMode, useChatMemory and agentOutput, '
                        'agentOutput_aiMeta.'),
        'ai_quote': '"AI Agent auditor: declares the part compliant only when there are zero warnings; otherwise it flags the request for a supervisor." (green annotation in bpmn-ai-chat-overview.png)',
        'captures': [('doc', '349_webapps_modeler_user-guide_img_bpmn-ai-chat-overview.png', 'bpmn-ai-chat-overview'),
                     ('doc', '348_webapps_modeler_user-guide_img_bpmn-ai-chat-diff.png', 'bpmn-ai-chat-diff'),
                     ('doc', '346_webapps_modeler_user-guide_img_bpmn-ai-chat-agent-panel.png', 'bpmn-ai-chat-agent-panel')],
        'note': ('The assignment warns that a page about the Modeler wizard is the E2-no-ai-element case and asks for '
                 'the vendor\'s own "Design-time" label to be quoted when dismissing it. The label is real (the AI '
                 'Agent Connector overview distinguishes "Runtime - executes during a process instance" from the '
                 'Modeler wizard\'s "Design-time - helps you author BPMN"), but this page\'s figures also show the '
                 'runtime binding: the overview figure has the AI Agent element template *applied* on a service task '
                 'inside the process, so the page carries runtime AI and is collected, not dismissed.'),
    },
}

# ------------------------------------------- pages whose exclusion is a judgement
JUDGED = {
    '/manual/latest/webapps/modeler/user-guide/form-ai-chat/': {
        'reason': 'E2-no-ai-element',
        'evidence': ('"It is the same agent as the BPMN AI Agent, reached from the form editor instead of the canvas, '
                     'and it uses the same providers and models" [the assignment\'s rule for Modeler-wizard pages: the '
                     'AI here is design-time and writes .form schemas, never a process. The page publishes no BPMN '
                     'figure and no model at all; read strictly as "no process artefact on the page" the code would be '
                     'E0-no-artefact, so this row is flagged for the researcher]'),
    },
    '/manual/latest/reference/connect/ai-agent-connector/developer-guide/': {
        'reason': 'E0-no-artefact',
        'evidence': ('"For developers building or packaging the connector, or reasoning about its runtime behavior." '
                     '[the page\'s code block is a Java source tree (AgentConnector, AgentRequest/Response, '
                     'KnowledgeIngestor*), not a process model; no figure and no BPMN XML on the page]'),
    },
    '/manual/latest/reference/connect/ai-agent-connector/': {
        'reason': 'E0-no-artefact',
        'evidence': ('"The AI Agent Connector brings agentic AI into CIB seven business processes." [overview page: '
                     'the feature comparison table and prose only - no figure, no BPMN XML, no downloadable model]'),
    },
}
for _p, _q in [
    ('audit-trail', 'Every AI Agent invocation is recorded automatically.'),
    ('chat-memory', 'By default each AI Agent invocation is stateless - the model sees only the current message .'),
    ('configuration-reference', 'Complete reference for both connectors, the environment variables / system properties, and the default values.'),
    ('configuring-the-agent', 'This chapter is the Modeler-facing reference for the AI Agent service task ( connectorId = cibseven-ai-agent ).'),
    ('glossary', 'Short definitions of the terms used across this documentation.'),
    ('installation', 'The AI Agent connector ships with the CIB seven distributions as a removable overlay .'),
    ('security-and-data-handling', 'What a security reviewer, DPO, or cautious operator needs: where data goes , what is stored where , how to handle secrets'),
    ('tools', 'Tools let the agent do things, not just answer.'),
    ('troubleshooting', 'Common problems and where to look.'),
] + [
    ('getting-started', None), ('examples', None), ('rag', None),
]:
    _path = '/manual/latest/reference/connect/ai-agent-connector/%s/' % _p
    if _path in MANUAL_DOCS or not _q:
        continue
    JUDGED.setdefault(_path, {
        'reason': 'E0-no-artefact',
        'evidence': '"%s" [AI Agent Connector reference chapter: parameter tables, code and prose; the page '
                    'publishes no process figure, no BPMN XML and no downloadable model]' % _q})

# --------------------------------- figures that are demonstrably not BPMN notation
# (contact sheets ledgers/cib-seven.raw/sheets_nw/*.jpg and sheets_ws/*.jpg, read at
#  native resolution where a call was decisive)
FIGS_E1 = {
    '/manual/latest/introduction/':
        'architecture-overview.png - a box-and-arrow component diagram (browser, REST API, process engine, database)',
    '/manual/latest/introduction/architecture/':
        'clustered/embedded/shared/standalone-process-engine.png, process-engine-architecture.png, '
        'secure-communication-architecture*.png - deployment and component box diagrams',
    '/manual/latest/introduction/third-party-libraries/cibseven-bpm-platform-license-book/':
        'superjson-banner.png, polar.sh tiers.svg, vue-apexcharts.png - third-party library banners and logos',
    '/manual/latest/update/rolling-update/':
        'architecture-step1..5.png, architecture.png - box diagrams of engines, load balancer and database',
    '/manual/latest/user-guide/process-applications/maven-archetypes/':
        'eclipse-00..06-*.png - Eclipse IDE screenshots',
    '/manual/latest/user-guide/process-applications/process-application-event-listeners/':
        'process-application-events.png - a box-and-arrow diagram of application events',
    '/manual/latest/user-guide/process-applications/process-application-resources/':
        'process-application-context.png - a box-and-arrow diagram of application resources',
    '/manual/latest/user-guide/process-applications/the-processes-xml-deployment-descriptor/':
        'process-application-deployment.png, process-application-redeployment.png - box diagrams of deployments',
    '/manual/latest/user-guide/process-engine/database/database-schema/':
        'database-schema.png and erd_723_bpmn/cmmn/dmn/history/identity.svg - entity-relationship diagrams',
    '/manual/latest/user-guide/process-engine/history/custom-implementation/':
        'process-engine-history-architecture.png - a box diagram of the history architecture',
    '/manual/latest/user-guide/process-engine/multi-tenancy/':
        'multi-tenancy-process-engine.png, multi-tenancy-tenant-identifiers.png - box diagrams (tenant identifiers, '
        'authentication)',
    '/manual/latest/user-guide/process-engine/process-engine-api/':
        'api.services.png - a box diagram of the engine services',
    '/manual/latest/user-guide/process-engine/process-instance-restart/':
        'variables-3.png - a Cockpit dialog screenshot (variables table)',
    '/manual/latest/user-guide/runtime-container-integration/jboss/':
        'jboss-jconsole.png (a JConsole screenshot) and jboss-service-dependencies.png (a box diagram)',
    '/manual/latest/release-notes/release-notes-2.0.0-ce/':
        'images/img01..03.png - WebClient/Cockpit screenshot montages ("alt: WebClient Screenshot", the page\'s own '
        'alt text)',
}
WEB_E1 = ['/webapps/admin/', '/webapps/welcome/', '/webapps/tasklist/', '/webapps/cockpit/bpmn/batch/',
          '/webapps/cockpit/bpmn/dashboard/', '/webapps/cockpit/cleanup/', '/webapps/cockpit/dashboard/',
          '/webapps/cockpit/deployment-view/', '/webapps/cockpit/dmn/', '/webapps/cockpit/operation-log/',
          '/webapps/cockpit/reporting/', '/webapps/cockpit/tasks-dashboard/']
WEB_E1_DESC = {
    '/webapps/admin/': 'Administration UI screenshots (start page, forms, tables, metric charts, license dialogs)',
    '/webapps/welcome/': 'Welcome-page screenshot (application landing page)',
    '/webapps/tasklist/': 'Tasklist UI screenshots (task lists, forms, filters)',
    '/webapps/cockpit/bpmn/batch/': 'Cockpit batch-operation dialog screenshots',
    '/webapps/cockpit/bpmn/dashboard/': 'Cockpit process-definition and process-instance search tables and delete dialogs',
    '/webapps/cockpit/cleanup/': 'Cockpit cleanup dialog screenshot',
    '/webapps/cockpit/dashboard/': 'Cockpit dashboard tiles and icon',
    '/webapps/cockpit/deployment-view/': 'Cockpit deployment lists and deploy/redeploy dialogs',
    '/webapps/cockpit/dmn/': 'Cockpit decision-definition views - DMN decision tables, not BPMN',
    '/webapps/cockpit/operation-log/': 'Cockpit operation-log table',
    '/webapps/cockpit/reporting/': 'Cockpit report charts',
    '/webapps/cockpit/tasks-dashboard/': 'Cockpit human-task search tables',
}
WEB_E2_DESC = ('Cockpit application screenshots that render the process canvas (bpmn.io) inside the UI - a BPMN '
               'diagram is shown, and no AI/LLM element appears in it or is named on the page')

# ---------------------------------------------------------- MANUAL (marketing)
MANUAL_MKT = {
    '/': {
        'verdict': 'INCLUDE', 'reason': None, 'slug': 'home-ai-agent-template',
        'evidence': '"Bereit für KI-Erweiterungen" (ready for AI extensions), over the hero image that shows the Modeler with the AI Agent element template open on a BPMN service task.',
        'bpmn_evidence': ('the hero asset HG-cibseven_26_2.png (962x588) is the Modeler with a BPMN process on the '
                          'canvas (start event, "Task Manual", "Task External Service", an exclusive gateway, a task '
                          'annotated "CIB Flow Agent", further tasks), one service task selected, and the '
                          'element-template panel open headed "CIB SEVEN - AI AGENT / cibseven-ai-agent - Element '
                          'Template: CIB seven AI Agent" with the groups Agent (Agent Name, Agent Type), Prompt, '
                          'Knowledge Base, Memory Type, Guardrails. Read at native resolution; captured next to this '
                          'record.'),
        'bpmn_quote': 'CIB SEVEN - AI AGENT / cibseven-ai-agent / Element Template: CIB seven AI Agent (property panel of the selected service task in HG-cibseven_26_2.png)',
        'ai_evidence': ('the AI element is an agent configured as a BPMN service task: the hero shows the AI Agent '
                        'connector element template with agent name, agent type (provider/model), prompt, knowledge '
                        'base, memory type and guardrails.'),
        'ai_quote': 'Bereit für KI-Erweiterungen (hero text, over the AI Agent element-template panel)',
        'captures': [('mkt', '146_uploads_2026_06_HG-cibseven_26_2.png', 'home-ai-agent-template')],
        'note': 'The marketing host is the second sub-population the assignment asks for; this hero is its richest AI-in-BPMN image.',
    },
    '/blog/': {
        'verdict': 'INCLUDE', 'reason': None, 'slug': 'blog-bpmn-ai-agent-teaser',
        'evidence': '"CIB seven / BPMN AI Agent - Review changes / Apply" (blog-index teaser HG-cibseven.png)',
        'bpmn_evidence': ('the blog teaser HG-cibseven.png (1600x600) is the Modeler with "Token Simulation" active '
                          'on a BPMN process (start event, "Request Order", "Quality Check", gateways, end events), a '
                          'floating panel headed "BPMN AI Agent" showing a "Review changes" before/after BPMN diff '
                          '(green annotated "Check inventory" / "Create invoice" tasks, an "Apply" button), and a '
                          'second floating panel with a token-flow BPMN fragment marked up in colour (user task, '
                          'exclusive gateway, service task, end event). Read at native resolution; captured next to '
                          'this record. The index also publishes Preview-CIB-seven-2.jpg, a photograph of the Modeler '
                          'whose toolbar reads "Token Simulation" and whose BPMN diagram has no AI element, and '
                          'HG-openday.jpg, an icon-node illustration labelled "AI" that is not BPMN notation.'),
        'bpmn_quote': 'BPMN AI Agent / Review changes / Apply (panel in HG-cibseven.png, over the Modeler canvas and a coloured BPMN fragment)',
        'ai_evidence': ('the AI element is the labelled "BPMN AI Agent" panel inside the figure, showing proposed '
                        'changes to the BPMN model, i.e. an agent acting on the process.'),
        'ai_quote': 'BPMN AI Agent - Review changes (panel heading in the teaser asset HG-cibseven.png)',
        'captures': [('mkt', '145_uploads_2026_06_HG-cibseven.png', 'blog-bpmn-ai-agent-teaser')],
        'note': ('First recorded as E2-no-ai-element from the contact sheet and flipped to INCLUDE after reading '
                 'HG-cibseven.png at native resolution: at sheet scale the panel heading is not legible, and the '
                 'figure does carry an AI element.'),
    },
    '/online-session-preview-cibseven-2-2/': {
        'verdict': 'INCLUDE', 'reason': None, 'slug': 'online-session-bpmn-ai-agent',
        'evidence': '"CIB seven 2.2 - Web Modeler & AI Features" (session cover), over a laptop showing the Modeler with a "BPMN AI Agent" panel',
        'bpmn_evidence': ('the cover Video-cover-cib_4.jpg (890x501) shows the Modeler canvas with a BPMN process '
                          'and, floating over it, a panel headed "BPMN AI Agent" whose body contains a second BPMN '
                          'fragment with green and red annotated nodes. Read at native resolution; captured next to '
                          'this record.'),
        'bpmn_quote': 'BPMN AI Agent (panel heading on Video-cover-cib_4.jpg, over a coloured BPMN fragment)',
        'ai_evidence': 'the AI element is the "BPMN AI Agent" panel drawn over the BPMN model, with the model changes highlighted in colour.',
        'ai_quote': 'CIB seven 2.2 Web Modeler & AI Features ... BPMN AI Agent',
        'captures': [('mkt', '142_uploads_2026_05_Video-cover-cib_4.jpg', 'online-session-bpmn-ai-agent')],
        'note': '',
    },
    '/casestudy/': {
        'verdict': 'UNCERTAIN', 'reason': None, 'slug': 'casestudy-robot-hand-token-flow',
        'evidence': 'the case-study hero asset robot-hand_news.png draws a BPMN token-flow whose tokens are being moved by a robotic hand',
        'bpmn_evidence': ('robot-hand_news-e1769777651103.png (1273x500): a token-flow diagram in BPMN notation - '
                          'rounded-rectangle tasks, two diamond gateways marked with an X, sequence flows between '
                          'them, each task holding an orange token disc - with a white robotic hand entering from the '
                          'right, its fingers over the last token. Read at native resolution; captured next to this '
                          'record.'),
        'bpmn_quote': 'robot-hand_news-e1769777651103.png: BPMN-shaped token flow (task boxes, two X gateways) manipulated by a robotic hand',
        'ai_evidence': ('no AI/LLM element is labelled inside the process; what the figure does is couple the process '
                        'to an automation/AI metaphor - a robotic hand reaching into the flow and touching a token.'),
        'ai_quote': '(no text in the figure; the AI/automation element is the humanoid robot hand reaching into the diagram)',
        'captures': [('mkt', '106_uploads_2026_01_robot-hand_news-e1769777651103.png', 'casestudy-robot-hand-token-flow')],
        'needs_human_ruling': True,
        'question': ('The case-study hero is a BPMN 2.0 token-flow diagram (tasks, two X gateways, sequence flows) '
                     'whose tokens are manipulated by a robotic hand. Nothing inside the process is labelled as AI. '
                     'Does a robot hand acting on the process count as an AI element inside the process, or is it '
                     'decoration on a BPMN diagram?'),
    },
    '/preise/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the page\'s product figure (Diagram-cib-seven-2026) is a stack of nested blue blocks labelled "CIB flow" / "CIB seven Enterprise" / "CIB seven LTS" / "CIB seven Community" with product icons - a product-tier block diagram, not BPMN 2.0 notation',
    },
    '/warum-cib-seven/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the page figures (cib-seven-73 .. cib-seven-78) are marketing illustrations - a gears-and-medal graphic, a network of person icons joined by solid and dashed lines, support and analytics scenes - not BPMN 2.0 notation',
    },
    '/enterprise/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the page figures (cib-seven-73, cib-seven-78, cib-seven_30m, bottle-neck) are marketing illustrations - a product-UI scene, a "30 min" dashed network of laptops, a bottleneck graphic - not BPMN 2.0 notation',
    },
    '/ins7ght/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the page hero CIB-insigth-graphics.png is an icon-node graphic (rounded squares holding person, gear and clock icons, X marks and a tick, joined by dashed arrows) and the other figures are analytics dashboards - not BPMN 2.0 notation',
    },
    '/ix-cib-seven-bpm-alternative/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the page figures are portrait/product illustrations (HG-cibseven_clean, PSD-Bank-Nuernberg, RPK, Regierung-von-Oberbayern) - no BPMN 2.0 diagram',
    },
    '/medien/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the media/press figures are website screenshots and newsletter banners (image-web-2024, blog-and-newsletter_new, news-cib-seven-12/13/14) - web-page graphics, not BPMN 2.0 notation',
    },
    '/academy/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the course figures (analytics, developer, Course-3, HG_Kurse) are training-room illustrations whose screens carry abstract box-and-arrow graphics - marketing illustrations, not BPMN 2.0 notation',
    },
    '/academy/add-on-dmn-deep-dive/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the course-page figures (contact_cs, Course-3) are a contact illustration and a course-cover illustration - not BPMN 2.0 notation',
    },
    '/academy/cib-seven-developer-training/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the course-page figures (contact_cs, developer) are a contact illustration and a developer-training scene whose monitors carry abstract graphics - not BPMN 2.0 notation',
    },
    '/academy/workshop-cib-seven-quickcheck/': {
        'verdict': 'EXCLUDE', 'reason': 'E1-not-bpmn', 'judgment': True, 'slug': None,
        'evidence': 'the course-page figures (analytics, contact_cs) are training and contact illustrations - not BPMN 2.0 notation',
    },
    '/trainer/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'the page carries only portrait photographs of the trainers (Dominik, Marco, Thomas) and a contact illustration - no process artefact of any kind',
    },
    '/kontakt/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'the page carries a contact illustration and a features card graphic - no process artefact of any kind',
    },
    '/faq/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'the page\'s only figure is a support illustration (a person at a laptop) - no process artefact of any kind',
    },
    '/newsletter/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'the page carries newsletter banner graphics (nwes-seven, news-cib-seven-14) - no process artefact of any kind',
    },
    '/download/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'a download listing page with no figure and no process artefact',
    },
    '/datenschutzerklaerung/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'a data-protection (privacy policy) text page with no figure and no process artefact',
    },
    '/cib-seven-community-day-2025/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'the page carries event photographs, posters and partner graphics (robots-09, MCK, HG-community-event) - no process artefact of any kind',
    },
    '/cib-seven-day-2026/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'a registration page whose figures are a register graphic and an event photograph - no process artefact of any kind',
    },
    '/category/paid-courses/': {
        'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False, 'slug': None,
        'evidence': 'a category archive listing with no figure and no process artefact',
    },
}

GALLERY = ['administration-authotizations', 'aufgabenliste-filterauswahl',
           'cockpit-process-definition-information', 'cockpit-process-overview-2',
           'cockpit-process-overview', 'start-mit-prozessuebersicht',
           'tasklist-task-ausgewaehlt']

FAMILIES = [
    ('/', ['/', '/en/', '/es/', '/pt/']),
    ('/blog/', ['/blog/', '/en/blog/', '/es/blog/', '/pt/blog/']),
    ('/casestudy/', ['/casestudy/', '/en/casestudy/', '/es/casestudy/', '/pt/casestudy/']),
    ('/online-session-preview-cibseven-2-2/',
     ['/online-session-preview-cibseven-2-2/', '/en/online-session-preview-cibseven-2-2/',
      '/es/online-session-preview-cibseven-2-2/', '/pt/online-session-preview-cibseven-2-2/']),
    ('/preise/', ['/preise/', '/en/pricing/', '/es/precios/', '/pt/precos/']),
    ('/warum-cib-seven/', ['/warum-cib-seven/', '/en/why-cib-seven/', '/es/por-que-cib-seven/',
                           '/pt/porque-cib-seven/']),
    ('/enterprise/', ['/enterprise/', '/en/enterprise/', '/es/enterprise/', '/pt/enterprise/']),
    ('/ins7ght/', ['/ins7ght/', '/en/ins7ght/', '/es/ins7ght/', '/pt/ins7ght/']),
    ('/ix-cib-seven-bpm-alternative/',
     ['/ix-cib-seven-bpm-alternative/', '/en/ix-cib-seven-bpm-alternative/',
      '/es/ix-cib-seven-bpm-alternative/', '/pt/ix-cib-seven-bpm-alternative/']),
    ('/medien/', ['/medien/', '/en/medien/', '/es/medien/', '/pt/medien/']),
    ('/academy/', ['/academy/', '/en/academy/', '/es/academy/', '/pt/academy/']),
    ('/academy/add-on-dmn-deep-dive/', ['/academy/add-on-dmn-deep-dive/', '/en/academy/add-on-dmn-deep-dive/',
                                        '/es/academy/add-on-dmn-deep-dive/', '/pt/academy/add-on-dmn-deep-dive/']),
    ('/academy/cib-seven-developer-training/',
     ['/academy/cib-seven-developer-training/', '/en/academy/cib-seven-developer-training/',
      '/es/academy/cib-seven-developer-training/', '/pt/academy/cib-seven-developer-training/']),
    ('/academy/workshop-cib-seven-quickcheck/',
     ['/academy/workshop-cib-seven-quickcheck/', '/en/academy/workshop-cib-seven-quickcheck/',
      '/es/academy/workshop-cib-seven-quickcheck/', '/pt/academy/workshop-cib-seven-quickcheck/']),
    ('/trainer/', ['/trainer/', '/en/trainer/', '/es/trainer/', '/pt/trainer/']),
    ('/kontakt/', ['/kontakt/', '/en/contact/', '/es/contacto/', '/pt/contacto/']),
    ('/faq/', ['/faq/', '/en/faq/', '/es/faq/', '/pt/faq/']),
    ('/newsletter/', ['/newsletter/', '/en/newsletter/', '/es/newsletter/', '/pt/newsletter/']),
    ('/download/', ['/download/', '/en/download/', '/es/descargas/', '/pt/download/']),
    ('/datenschutzerklaerung/', ['/datenschutzerklaerung/', '/en/privacy-policy/', '/es/privacy-policy/',
                                 '/es/proteccion-de-datos/', '/pt/privacy-policy/', '/pt/protecao-de-dados/']),
    ('/cib-seven-community-day-2025/', ['/cib-seven-community-day-2025/', '/en/cib-seven-community-day-2025/',
                                        '/es/cib-seven-community-day-2025/', '/pt/cib-seven-community-day-2025/']),
    ('/cib-seven-day-2026/', ['/cib-seven-day-2026/', '/en/cib-seven-day-2026/', '/es/cib-seven-day-2026/',
                              '/pt/cib-seven-day-2026/']),
    ('/category/paid-courses/', ['/category/paid-courses/', '/en/category/paid-courses/',
                                 '/es/category/paid-courses/', '/pt/category/paid-courses/']),
] + [('/galleryui/%s/' % g, ['/galleryui/%s/' % g, '/en/galleryui/%s/' % g,
                             '/es/galleryui/%s/' % g, '/pt/galleryui/%s/' % g]) for g in GALLERY]


def load_json(p, default=None):
    if not os.path.exists(p):
        return default if default is not None else {}
    return json.load(io.open(p, encoding='utf-8'))


def collapse(s, n=None):
    s = re.sub(r'\s+', ' ', s or '').strip()
    if n:
        s = ' '.join(s.split(' ')[:n])
    return s


def docs_figures():
    img = load_json(os.path.join(RAW, 'img.json'))
    out = {}
    for src, e in img.items():
        f = e.get('file')
        if not f:
            continue
        p = os.path.join(IMGDIR['doc'], f)
        if not os.path.exists(p):
            continue
        try:
            w, h = Image.open(p).size
        except Exception:
            continue
        if max(w, h) < 120 or 'logo.png' in src or 'creativecommons' in src:
            continue
        for pg in e.get('pages') or []:
            out.setdefault(pg, []).append((f, w, h))
    return out


def mkt_fig_stems():
    out = load_json(os.path.join(RAW, 'mkt_figs.json'), [])
    return {o['u']: set(re.sub(r'^\d+_', '', f) for f, w, h, c in o['figs']) for o in out}


def content_of(url):
    c = CONTENT.get(url) or {}
    t = re.sub(r'^content-text"?>?\s*', '', c.get('text') or '')
    return (c.get('h1') or '').strip(), re.sub(r'\s+', ' ', t).strip()


def quote_for(url, scan, fallback=''):
    h1, txt = content_of(url)
    if txt:
        return collapse(txt, 25)
    v = scan.get(url) or {}
    q = collapse(v.get('text'), 25)
    if q and not q.startswith(('Docs Get Started', 'GDPR Cookie')):
        return q
    return collapse(v.get('t')) or h1 or fallback


def write_record(nnn, url, m, title, source_name):
    rec = os.path.join(CORPUS, '%s_%s.md' % (nnn, m['slug']))
    caps = []
    for kind, f, stem in m.get('captures') or []:
        src = os.path.join(IMGDIR[kind], f)
        dest = os.path.join(CORPUS, '%s_%s.png' % (nnn, stem))
        if os.path.exists(src) and not os.path.exists(dest):
            if f.lower().endswith('.png'):
                shutil.copyfile(src, dest)
            else:
                Image.open(src).convert('RGB').save(dest)
        try:
            w, h = Image.open(dest).size
        except Exception:
            w = h = None
        caps.append({'file': os.path.basename(dest), 'w': w, 'h': h, 'src': f})
    xml_name, xml_body = None, None
    if m.get('xml_file') and os.path.exists(m['xml_file']):
        xml_name = '%s_%s.bpmn' % (nnn, m['slug'])
        xml_body = io.open(m['xml_file'], encoding='utf-8').read()
        io.open(os.path.join(CORPUS, xml_name), 'w', encoding='utf-8').write(xml_body)
    shot = caps[0] if caps else None
    L = ['---',
         'n: %d' % int(nnn),
         'source: cib-seven',
         'source_name: %s' % source_name,
         'source_type: %s' % ('vendor documentation' if url.startswith(DOCS) else 'vendor marketing site'),
         'title: %s' % title,
         'url: %s' % url,
         'accessed: %s' % ACCESSED,
         'verdict: %s' % m['verdict'],
         'needs_human_ruling: %s' % str(bool(m.get('needs_human_ruling'))).lower(),
         'question: %s' % (collapse(m.get('question')) or 'null'),
         'needs_visual_check: %s' % str(bool(m.get('needs_visual_check'))).lower(),
         'bpmn_evidence: "%s"' % collapse(m.get('bpmn_evidence') or '').replace('"', "'"),
         'bpmn_evidence_quote: "%s"' % collapse(m.get('bpmn_quote') or '').replace('"', "'"),
         'ai_evidence: "%s"' % collapse(m.get('ai_evidence') or '').replace('"', "'"),
         'ai_evidence_quote: "%s"' % collapse(m.get('ai_quote') or '').replace('"', "'"),
         'artefacts:',
         '  screenshot: %s' % (shot['file'] if shot else 'null'),
         '  archive: null',
         '  bpmn_xml: %s' % (xml_name or 'null'),
         'duplicate_of: null',
         'access: public',
         'capture_source: %s' % ('page asset from docs.cibseven.org (same-origin)'
                                 if url.startswith(DOCS) else 'page asset from cibseven.org (same-origin)'),
         'capture_quality: %s' % ('legible' if (shot or xml_name) else 'null'),
         'capture_width_px: %s' % (shot['w'] if shot else 'null'),
         'capture_method: %s' % ('plain GET of the page asset (ledgers/cib-seven.raw/img/), '
                                 'or the page\'s own XML block copied verbatim'
                                 if url.startswith(DOCS) else
                                 'plain GET of the page asset (ledgers/cib-seven.raw/mimg/)'),
         '---', '',
         '## What the page shows', '',
         'Verbatim from the page:', '',
         '> %s' % collapse(m.get('evidence') or ''), '',
         '## Artefact reading (native resolution unless stated)', '',
         '- **BPMN:** %s' % collapse(m.get('bpmn_evidence') or ''),
         '- **AI element:** %s' % collapse(m.get('ai_evidence') or ''), '']
    if caps:
        L += ['## Captures', '']
        for c in caps:
            L.append('- `%s` (%sx%s) - from `%s`' % (c['file'], c['w'], c['h'], c['src']))
        L.append('')
    if xml_name:
        L += ['## BPMN XML published on the page (verbatim capture)', '', '```xml',
              (xml_body or '').strip()[:4000], '```', '']
    if m.get('note'):
        L += ['## Notes for the researcher', '', m['note'], '']
    io.open(rec, 'w', encoding='utf-8').write('\n'.join(L))
    return os.path.relpath(rec, '.').replace('\\', '/')


def ai_note(u):
    """The first AI keyword hit in the page's content region, for the researcher.

    Skipped when the hit is churn rather than page content: the marketing site's
    cookie banner carries a "CIB AI ChatBot" label on every page, and Oracle's
    "23ai" is a product name.
    """
    ai = (CONTENT.get(u) or {}).get('ai') or []
    for h in ai:
        ctx = collapse(h.get('ctx'))
        if re.search(r'cookie|zustimmen|einstellungen|23ai|ChatBot', ctx, re.I):
            continue
        return ctx[:120]
    return None


def main():
    global CONTENT
    CONTENT = load_json(os.path.join(RAW, 'content.json'))
    scan = load_json(os.path.join(RAW, 'scan.json'))
    figs = docs_figures()
    mkt_stems = mkt_fig_stems()
    docs_paths = [l.strip() for l in io.open(NAV, encoding='utf-8') if l.strip()]
    docs_urls = [DOCS + p for p in docs_paths]
    mkt_urls = sorted(load_json(os.path.join(RAW, 'mkt_pages.json')))
    os.makedirs(CORPUS, exist_ok=True)
    rows = []

    for i, (p, u) in enumerate(zip(docs_paths, docs_urls), 1):
        nnn = '%03d' % i
        h1, txt = content_of(u)
        title = h1 or (scan.get(u) or {}).get('t', '').replace(' | docs.cibseven.org', '')
        row = {'n': i, 'url': u, 'title': title, 'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact',
               'judgment': False, 'evidence': '', 'record': None, 'needs_visual_check': False,
               'needs_human_ruling': False, 'accessed': ACCESSED}
        has_ai = bool((CONTENT.get(u) or {}).get('ai'))
        m = MANUAL_DOCS.get(p)
        if m:
            mm = dict(m)
            row.update({'verdict': m['verdict'], 'reason': m.get('reason'), 'judgment': True,
                        'evidence': collapse(m.get('evidence'))})
            if m.get('needs_human_ruling'):
                row['needs_human_ruling'] = True
                row['question'] = m['question']
            if m['verdict'] in ('INCLUDE', 'UNCERTAIN'):
                row['record'] = write_record(nnn, u, mm, title,
                                             'CIB seven manual (docs.cibseven.org, /manual/latest/ pinned)')
        else:
            fl = figs.get(p) or []
            figtxt = '; '.join('%s (%dx%d)' % (f[0], f[1], f[2]) for f in fl[:4])
            pre = (scan.get(u) or {}).get('pre') or []
            xmlq = next((q for q in pre if E_BPMN.search(q)), None)
            q = quote_for(u, scan, title)
            jv = JUDGED.get(p)
            if jv:
                row['reason'] = jv['reason']
                row['evidence'] = jv['evidence']
                row['judgment'] = True
            elif re.search(r'/reference/dmn|/user-guide/dmn-engine/', p):
                row['reason'] = 'E1-not-bpmn'
                row['evidence'] = ('"%s" [page of the DMN section of the manual: DMN 1.x decision notation - decision '
                                   'tables, FEEL expressions, decision requirements graphs; not BPMN 2.0]' % q[:130])
            elif re.search(r'/reference/cmmn11/', p):
                row['reason'] = 'E1-not-bpmn'
                row['evidence'] = ('"%s" [page of the CMMN section of the manual: CMMN 1.1 case notation - case plan '
                                   'model, stages, sentries; not BPMN 2.0]' % q[:130])
            elif xmlq:
                row['reason'] = 'E2-no-ai-element'
                row['judgment'] = False
                row['evidence'] = ('"%s" [the page publishes BPMN 2.0 XML - %s - and the page names no AI/LLM element '
                                   'inside it]' % (collapse(xmlq, 25), collapse(xmlq, 18)))
            elif fl and (p in FIGS_E1 or any(p.startswith(w) for w in WEB_E1)):
                row['reason'] = 'E1-not-bpmn'
                desc = FIGS_E1.get(p)
                if not desc:
                    desc = dict((w, WEB_E1_DESC[w]) for w in WEB_E1)[
                        next(w for w in WEB_E1 if p.startswith(w))]
                row['evidence'] = ('"%s" [figures: %s]' % (q[:110], collapse(desc)))
                row['judgment'] = False
            elif fl:
                row['reason'] = 'E2-no-ai-element'
                row['evidence'] = ('"%s" [figures: %s - %s]' % (q[:100], figtxt[:150],
                                                                WEB_E2_DESC if p.startswith('/webapps/')
                                                                else 'the page\'s notation illustrations; no AI/LLM '
                                                                     'element appears in them or is named on the page'))
                row['judgment'] = False
            else:
                row['reason'] = 'E0-no-artefact'
                row['evidence'] = ('"%s" [no figure, no BPMN XML code block and no downloadable model on the '
                                   'page]' % q[:170])
                row['judgment'] = bool(jv)
            note = ai_note(u)
            if note and not jv and not xmlq:
                row['evidence'] += ' [content names AI: "%s"]' % note
        rows.append(row)

    canon = {}
    for key, urls in FAMILIES:
        for u in urls:
            canon[MKT + u] = key
    first_of_family = {}
    for u in mkt_urls:
        k = canon.get(u)
        if k and k not in first_of_family:
            first_of_family[k] = u
    n_of = dict((u, 468 + i) for i, u in enumerate(mkt_urls))
    for j, u in enumerate(mkt_urls, 468):
        nnn = '%03d' % j
        key = canon.get(u)
        h1, _t = content_of(u)
        title = h1 or (scan.get(u) or {}).get('t', '')
        row = {'n': j, 'url': u, 'title': title, 'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact',
               'judgment': False, 'evidence': '', 'record': None, 'needs_visual_check': False,
               'needs_human_ruling': False, 'accessed': ACCESSED}
        primary = first_of_family.get(key) if key else None
        m = MANUAL_MKT.get(key) if key else None
        stemset = mkt_stems.get(u, set())
        if m and u == primary:
            mm = dict(m)
            row.update({'verdict': m['verdict'], 'reason': m.get('reason'), 'judgment': m.get('judgment', True),
                        'evidence': collapse(m.get('evidence'))})
            if m.get('needs_human_ruling'):
                row['needs_human_ruling'] = True
                row['question'] = m['question']
            if m['verdict'] in ('INCLUDE', 'UNCERTAIN'):
                row['record'] = write_record(nnn, u, mm, title,
                                             'CIB seven marketing site (cibseven.org, WordPress + Yoast sitemap)')
        elif m and primary:
            base_n = n_of[primary]
            if m['verdict'] in ('INCLUDE', 'UNCERTAIN'):
                row['reason'] = 'E3-duplicate'
                row['duplicate_of'] = base_n
                row['judgment'] = False
                row['evidence'] = ('translated twin of n=%d (%s): same page in another language, byte-identical '
                                   'figure set, same diagram' % (base_n, primary.replace(MKT, '') or '/'))
            else:
                row['reason'] = m['reason']
                row['judgment'] = False
                row['evidence'] = ('translated twin of n=%d (%s): identical figure set, so the same call is recorded '
                                   'once - %s' % (base_n, primary.replace(MKT, '') or '/',
                                                  collapse(m['evidence'])[:150]))
        else:
            q = quote_for(u, scan, title)
            if not stemset:
                row['evidence'] = ('"%s" [no figure on the page: no process artefact]' % (title or q)[:170])
            else:
                row['evidence'] = ('"%s" [the page\'s figures (%d) are photographs, portraits, logos, banners or '
                                   'product art: no process artefact]' % (q[:130], len(stemset)))
            row['judgment'] = False
            note = ai_note(u)
            if note:
                row['evidence'] += ' [content names AI: "%s"]' % note
        rows.append(row)

    for r in rows:
        if not (r.get('evidence') or '').strip():
            r['evidence'] = (r.get('title') or r['url'])[:170]

    vc = Counter(r['verdict'] for r in rows)
    cc = Counter(r['reason'] for r in rows if r['verdict'] == 'EXCLUDE')
    je = [r for r in rows if r['verdict'] == 'EXCLUDE' and r['judgment']]
    header = {
        'type': 'header', 'source': 'cib-seven',
        'source_name': 'CIB seven (docs.cibseven.org manual + cibseven.org marketing site)',
        'source_type': 'vendor documentation + vendor marketing site',
        'census': True, 'population_size': len(rows),
        'enumeration_method': (
            'Two hosts, both enumerated in full, no keyword filter. (1) docs.cibseven.org has no sitemap, so the '
            'population is the global sidebar of the manual itself: the 467 <a> targets of the pinned version '
            '/manual/latest/ (ledgers/cib.raw/nav_latest.txt), closed by a link-union check over the crawled pages. '
            '(2) cibseven.org: the Yoast sitemap index lists page-sitemap (80), academy-sitemap (12), '
            'galleryui-sitemap (28) and category-sitemap (4) = 124 urls across de/en/es/pt. Total 591 rows. Release '
            'notes pages and the Examples & Tutorials section are inside the docs population and are judged like any '
            'other page.'),
        'entry_points': ['https://docs.cibseven.org/manual/latest/',
                         'https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/getting-started/',
                         'https://cibseven.org/', 'https://cibseven.org/sitemap_index.xml'],
        'access': 'public', 'date_start': '2026-09-24', 'agent_model': 'deepseek-v4.1-flash:cloud',
        'browser_tool': 'chrome-devtools-mcp --browser-url 127.0.0.1:9222', 'queries': [],
        'note': (
            'Every page of both populations was fetched and its content region scanned (visible text, <pre> blocks '
            'naming BPMN elements or connectors, .bpmn/.dmn/.cmmn download links, image assets); every image asset of '
            'both hosts was read on contact sheets (ledgers/cib-seven.raw/sheets*, sheets_nw, sheets_ws) and every '
            'candidate AI image at native resolution before the verdicts below. Mechanical rules, applied in this '
            'order: DMN section E1-not-bpmn and CMMN section E1-not-bpmn (the section title declares the notation); a '
            'page publishing BPMN 2.0 XML in a code block E2-no-ai-element (element names matched with a delimiter so '
            'deployment descriptors and processes.xml do not count - 47 pages); figure pages whose figures are '
            'application UI, architecture, ERD or IDE screenshots E1-not-bpmn; figure pages whose figures are BPMN '
            'diagrams or BPMN element notation E2-no-ai-element (Cockpit screenshots that render the process canvas '
            'are in this class, since the canvas is BPMN); nothing of the above E0-no-artefact. judgment=true exactly '
            'where the page content itself names AI/LLM/agent. Camunda 7 lineage (this is a Camunda 7 fork) is never '
            'an E3 reason. Translated marketing twins (de/en/es/pt) whose figure set is byte-identical to the '
            'primary-language page are E3-duplicate when the primary page was collected, and otherwise keep the '
            'primary page\'s code with judgment=false.'),
    }
    footer = {
        'type': 'footer', 'date_end': ACCESSED, 'rows': len(rows),
        'include': vc.get('INCLUDE', 0), 'uncertain': vc.get('UNCERTAIN', 0),
        'exclude': dict(cc), 'blocked': vc.get('BLOCKED', 0),
        'judgment_exclusion_share': '%d judgement EXCLUDE rows of %d (%.1f%%)'
                                    % (len(je), len(rows), 100.0 * len(je) / len(rows)),
        'self_audit_flips': (
            'The blog row was first recorded as E2-no-ai-element from the contact sheet and flipped to INCLUDE after '
            'reading HG-cibseven.png at native resolution, where the "BPMN AI Agent / Review changes" panel is '
            'legible. The same native pass over the marketing assets produced the other collected marketing rows. A '
            'second correction: pages whose only artefact is a BPMN 2.0 XML code block were first drafted as '
            'E0-no-artefact and were corrected to E2-no-ai-element once the <pre> blocks were enumerated (47 pages), '
            'and the process-engine figures were reclassified from E1 to E2 after the contact-sheet pass showed '
            'rendered BPMN diagrams in the Cockpit screenshots and BPMN illustrations in the reference pages.'),
        'status': 'DONE',
    }
    with io.open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(header, ensure_ascii=False) + '\n')
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
        fh.write(json.dumps(footer, ensure_ascii=False) + '\n')
    io.open(FRONTIER, 'w', encoding='utf-8').write('\n'.join(docs_urls + mkt_urls) + '\n')
    print('rows', len(rows), dict(vc))
    print('exclusions', dict(cc))
    print('judgement exclusions %d (%.2f%%)' % (len(je), 100.0 * len(je) / len(rows)))
    print('records written:', len([r for r in rows if r.get('record')]))
    for r in rows:
        if r.get('record'):
            print('  ', r['n'], r['verdict'], r['url'])


if __name__ == '__main__':
    main()
