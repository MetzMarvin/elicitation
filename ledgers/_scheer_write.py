#!/usr/bin/env python3
"""Write the scheer-pas ledger (doc.scheer-pas.com) - one row per page of every doc space.

Population: all 1333 pages of the 14 doc-space page trees the site publishes as JSON
(`/<space>/latest/__pagetree.json`, and `/<space>/__pagetree.json` for the two un-versioned spaces
`help` and `release-notes`). Version `latest` (= 26.2 at access time) is pinned; the versioned URLs
(`/designer/25.3/...`) are a facet of the same pages, not additional items.

The screen (applied to every page's own article region, with the site chrome removed):

  * a page with no figure at all carries no artefact                       -> E0, mechanical
  * a page whose figures' own attachment names or whose prose name a
    process model (BPMN / process model / gateway / pool / lane / ...)     -> judged by eye
  * anything else                                                          -> E0, mechanical

Every judgment row says which figures were looked at. The screen's residual risk (a page
publishing a process diagram under UI-ish figure names, with no process word in its prose) is
measured by the randomised visual audit recorded in the header, not assumed away.

  python ledgers/_scheer_write.py --survey           # what the screen fires on
  python ledgers/_scheer_write.py --phase1 [--write]  # mechanical rows
  python ledgers/_scheer_write.py --phase2 [--write]  # judgment rows
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_scheer"
PAGES = OUT / "pages"
LEDGER = ELI / "ledgers" / "scheer-pas.jsonl"
FRONTIER = ELI / "ledgers" / "scheer-pas.frontier.txt"
TODAY = "2026-09-24"
sys.path.insert(0, str(ELI / "ledgers"))
import _scheer_rows as S  # noqa: E402

# --- per-page rulings -------------------------------------------------------------------------
# link (the page's path) -> (verdict, reason, notation, artefacts, figures_looked, note,
#                            record_stem, question)
RULINGS = {
    # ---- the source's artefact: the Insurance_Case_Process, AI-bound through the execution model
    "/academy/latest/preparations-ai-tutorial-1": (
        "UNCERTAIN", None, "BPMN 2.0 (Scheer PAS Designer process editor)",
        "fig 1 tutorial_process.png: the BPMN model of Insurance_Case_Process - start event "
        "'Start insurance case auto-processing', user task 'Enter insurance request', service "
        "task 'Analyze customer request', user task 'Show case information', terminate end "
        "event. fig 2 aitutorial_start_process.png: the same model in the Designer with the "
        "tutorial's annotations over it.",
        "the page's two model figures (aitutorial_start_process.png, tutorial_process.png) at "
        "native size, 1.02x and 1.27x, and its other 2 figures "
        "(create_folder_in_sandbox.png, import_service.png) in the 75-figure contact sheet",
        "The page publishes the process model of the tutorial service and its own process-step "
        "table binds the service task 'Analyze customer request' to the AI agent: \"The AI agent, "
        "that you are going to create during this tutorial, will process the insurance request "
        "into insurance case information.\" The BPMN notation itself carries no AI element - the "
        "binding lives in the task's execution model (records 002/003).",
        "001_insurance-case-process-bpmn",
        "The published BPMN model carries an ordinary service task, 'Analyze customer request'; "
        "the AI agent is bound to that task in the xUML execution model (operation execute, in "
        "CaseRequest / out AgentResponse) documented on sibling pages, so the AI element is "
        "delegated and invisible in the BPMN notation. Does the corpus accept this as an "
        "AI-enabled BPMN artefact (BPMN model plus its published AI binding, records 001+002), or "
        "does it require the AI element to be a labelled element inside the BPMN diagram itself?"),

    "/academy/latest/step-3-integrating-the-agent-to-the-process": (
        "UNCERTAIN", None, "xUML execution model (proprietary) inside the Designer, BPMN tab "
        "alongside",
        "fig 1 open_execution_model.png and fig 2 drop_execute_operation.png: the Designer with "
        "the BPMN tab (Insurance_Case_Process) and the task's execution model below, the AI "
        "agent's execute operation dragged into it. The other 9 figures are Designer panels of "
        "the same binding (REST extension, agent alias, pins, persisted variables, "
        "getAuthorizationOptions).",
        "the page's two model figures (open_execution_model.png, drop_execute_operation.png) at "
        "native size, 1.00x, and its other 9 figures in the 75-figure contact sheet",
        "This is the tutorial's binding step: \"You created the CaseAgent to execute process step "
        "Analyze customer request .\" -> \"drag & drop the agent's execute operation to the "
        "execution model\". AI element present and documented, but not drawn in BPMN notation.",
        "002_agent-binding-step-3",
        "This page is where the AI agent becomes part of the process (its execute operation is "
        "dragged into the execution model of the BPMN service task 'Analyze customer request'), "
        "but the diagrams it publishes to show that are xUML execution-model diagrams and "
        "Designer screenshots, not BPMN 2.0. Is it an artefact in its own right, or the binding "
        "evidence for record 001?"),

    "/designer/latest/using-an-ai-agent-in-an-xuml-service": (
        "UNCERTAIN", None, "xUML execution model / activity diagram (proprietary), not BPMN 2.0",
        "fig drag_execute_to_execution_model.png: the Designer with the BPMN tab (the process of "
        "record 001) and the execution model where the AI agent's execute operation is dropped. "
        "The other 4 figures: the Implementation tree with Agents > CaseAgent > "
        "CaseAgentInterface > execute (in CaseRequest / out AgentResponse), the REST extension on "
        "that operation, the AuthService operation setAuthorizationOptions, and the "
        "request_options wiring.",
        "the model figure drag_execute_to_execution_model.png at native size, 1.00x, and the "
        "page's other 4 figures in the 75-figure contact sheet",
        "The reference page for the delegated binding: \"for each AI agent a default operation "
        "execute is created\" and \"you can use the execute operation in execution and activity "
        "diagrams\". The AI agent is a first-class element of the *execution model*, and no BPMN "
        "diagram is published on this page.",
        "003_using-an-ai-agent-in-an-xuml-service",
        "This reference page shows the AI agent as a first-class element of the process model (a "
        "default execute operation per agent, dragged into 'execution and activity diagrams' with "
        "typed input/output), but every figure is the proprietary xUML notation, not BPMN. Does "
        "the corpus take this as an AI-enabled process artefact, or only as the notation "
        "reference for the binding documented in records 001 and 002?"),

    # ---- BPMN model published, no AI element anywhere in the process -------------------------
    "/designer/latest/modeling-bpmn": (
        "EXCLUDE", "E2-no-ai-element", "BPMN 2.0 (Scheer PAS Designer BPMN editor)",
        "fig bpmn_editor.png: a BPMN model 'JanesFirstBPMN' in the Designer's BPMN editor - "
        "'Janes Start Event' -> 'Janes First User Task' -> 'Janes Gateway' (exclusive) -> "
        "'Janes First Receive Task' / 'Janes End Event' (terminate), with the Validation panel. "
        "The other figures are Designer screenshots: create_process_via_context_menu, "
        "create_bpmn (Create Process dialog), bpmn_new_tab, bpmn_created, process_context_menu, "
        "bpmn_diagram_attributes (the model's attributes: Name JanesFirstBPMN).",
        "bpmn_editor.png at 0.95x (native) for the model itself, and all 8 figures of the page in "
        "the 75-figure contact sheet",
        "A genuine AI-free BPMN model: start event, user task, exclusive gateway, receive task, "
        "terminate end event, all named 'Janes ...'. The page's article region contains no "
        "AI/LLM token at all (the AI screen fires 0 times; the only 'AI'-like string on the page "
        "is the site chrome's 'Ask the PAS Chatbot!', which sits outside the article), so there "
        "is no AI mention to dismiss. The AI-adjacent prose on sibling pages ('Using AI Agents') "
        "is about the Designer's agent feature, not about this model.",
        None, None),

    # ---- pages of the in-scope AI subtree that publish no process artefact -------------------
    "/academy/latest/ai-tutorials": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> and no diagram canvas in the "
        "article region)",
        "none (0 figures)",
        "Landing page of the AI tutorial: prerequisites, supported AI service providers (Google, "
        "Mistral, OpenAI, LLMs hosted by Microsoft Foundry) and links to the four tutorial steps. "
        "Its only BPMN sentence is a collapsed 'Good to Know' blurb about the Designer itself - "
        "\"The easy-to-use, innovative and model-based tool allows you to create processes in "
        "BPMN 2.0 format via a graphical user interface.\" - i.e. about the tool that would draw "
        "a process, not about a process on this page.",
        None, None),

    "/academy/latest/tutorial-1-using-an-ai-agent": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> in the article region)",
        "none (0 figures)",
        "Tutorial overview page: it states the user story (\"David Stringer of ACME Corp. ... "
        "wants to build a service in which an AI agent extracts the necessary data from these "
        "unstructured queries and presents them in a request form\") and links to steps 1-4. The "
        "process it describes is published on the step pages, not here.",
        None, None),

    "/designer/latest/using-ai-agents": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> in the article region)",
        "none (0 figures)",
        "Chapter landing page of the Designer's AI guide. It argues for the approach - "
        "\"Integrating AI agents into your BPMN-based processes is a strong strategy ...\" - and "
        "lists use cases in prose only ('In a loan approval process, an AI agent can analyze "
        "credit scores ...', 'Automatically routing support tickets ...'), each an 'Example Use "
        "Case' sentence with no diagram. The concrete process models live in the tutorial "
        "(records 001/002) and in the xUML service page (record 003).",
        None, None),

    "/designer/latest/ai-service-provider": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page's single figure (ai_service_provider_aliases.png) is the "
        "Designer's alias list dialog, not a diagram",
        "all 1 figure of the page at native size",
        "Reference page for the alias construct: what an AI service provider alias is, which "
        "providers are supported and how aliases are added. Nothing process-shaped is published "
        "here; the AI content is about configuring providers, not about an element in a process.",
        None, None),

    "/designer/latest/ai-service-provider-reference": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> in the article region)",
        "none (0 figures)",
        "Reference table page: provider, standard, model and API key fields for each supported AI "
        "service provider. Prose and tables only; no process artefact.",
        None, None),

    "/designer/latest/google-ai-service-provider-reference": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> in the article region)",
        "none (0 figures)",
        "Reference page for the Google AI service provider alias fields. Prose and tables only; "
        "no process artefact.",
        None, None),

    "/designer/latest/microsoft-foundry-ai-service-provider-reference": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> in the article region)",
        "none (0 figures)",
        "Reference page for the Microsoft Foundry AI service provider alias fields. Prose and "
        "tables only; no process artefact.",
        None, None),

    "/designer/latest/prompts-tips-and-examples": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page publishes no figure at all (0 <img> in the article region)",
        "none (0 figures)",
        "Prompt-writing guidance for AI agents (structure, role, context, output format). Its "
        "content is text about prompting; the AI screen fires 0 times in the article region and "
        "nothing process-shaped is published. The 'AI' in the site chrome is excluded.",
        None, None),

    # ---- AI pages whose figures are the agent's own configuration/testing UI ------------------
    "/academy/latest/step-1-creating-the-ai-agent": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the 13 figures are Designer UI of the agent's construction - "
        "create_package, create_agent, agent_in_service_panel, rest_alias_in_service_details, "
        "select_ai_service_provider_alias, create_service_provider_alias, ai_aliases, "
        "class_case_request, class_agent_response, agent_input, agent_input_attributes, "
        "agent_input_change_type, agent_parameters_changed. None is a process model.",
        "all 13 figures of the page in the 75-figure contact sheet (tile scale <= 1.0)",
        "The page's process talk is about the process *to come* - \"We have integrated AI agents "
        "into Scheer PAS Designer so that our customers can leverage the benefits of AI agents in "
        "their BPMN-based business processes.\" and \"David has modeled the business process.\" - "
        "while every figure shows the Implementation tree, class editors or the alias dialog. "
        "The process model itself is published on the preparations page (record 001).",
        None, None),

    "/academy/latest/step-2-prompting-and-testing-the-ai-agent": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the 8 figures are the agent's own configuration and test UI - "
        "open_the_case_agent, set_provider_tool_alias, user_prompt_input_model, user_prompt, "
        "system_prompt_output_model, open_tab_testing, agent_status_online, analyze_test_output. "
        "None is a process model; a figure of a running agent test is a chat/test panel, not a "
        "process diagram.",
        "all 8 figures of the page in the 75-figure contact sheet (tile scale <= 1.0)",
        "The page contains no process-model language at all (the process screen fires 0 times): "
        "it is about writing system and user prompts and testing the agent in the Testing tab.",
        None, None),

    "/academy/latest/step-4-testing-the-process": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the 6 figures are deployment and application UI - deploy_ai_service (the "
        "Deployment controls), the application's process list, the Form_CaseRequest form, the "
        "Form_CaseOverview result page, and the tutorial's trophy icon. The process list shows "
        "the deployed 'Insurance_Case_Process' as a row with a 'Start instance' button, not as a "
        "diagram.",
        "all 6 figures of the page in the 75-figure contact sheet (tile scale <= 1.0)",
        "The page's own summary is \"In this step you tested the execution of a business process "
        "that contains an AI agent.\" - a statement about the process of record 001, of which "
        "this page publishes no diagram.",
        None, None),

    "/designer/latest/creating-an-ai-agent": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the 11 figures are the agent's construction UI - create_ai_agent, "
        "ai_agent_elements, one_alias_per_agent, agent_alias_configuration, open_ai_configuration, "
        "tab_prompt, select_pas_tools, select_service_api, empty_api_tab, mcp_server_selection, "
        "testing_tab_progress_bar. The one process word in the article ('xUML service') appears "
        "in the sentence that says the agent is created *in* a service.",
        "all 11 figures of the page in the 75-figure contact sheet (tile scale <= 1.0)",
        "Guide page for building an AI agent in the Designer: Explorer context menu, agent "
        "elements, aliases, prompt/tools/API tabs and the test bar. No process model is "
        "published.",
        None, None),

    "/designer/latest/testing-an-ai-agent": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the 8 figures are the Testing tab UI of the agent editor - "
        "testing_tab_progress_bar, note_for_agent_with_apis, test_input, button_execute, "
        "button_open_log_analyzer, test_output, icon_download_test_input, "
        "icon_copy_to_clipboard.",
        "all 8 figures of the page in the 75-figure contact sheet (tile scale <= 1.0)",
        "How to test an agent on its own (test input, execute, log analyzer, test output). The "
        "article names no process model; the agent is exercised standalone, outside any process.",
        None, None),

    "/designer/latest/error-handling-ai-agents": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the page's single figure (grafik-20251010-075457.png) is the agent host "
        "field of the agent's configuration panel (a Host input with a 'test-base-agent-...' "
        "value), not a diagram.",
        "all 1 figure of the page at native size",
        "Error handling for AI agents at the agent level (what to do when the provider is "
        "unreachable). The page's AI mention is about the agent's own error behaviour, not about "
        "an element inside a process.",
        None, None),

    # ---- BPMN notation published, but not as a process model, and no AI anywhere ---------------
    "/analyzer/latest/how-bpmn-elements-are-generated-to-xuml": (
        "EXCLUDE", "E2-no-ai-element", "BPMN 2.0 notation (single-element snippets), shown next "
        "to the xUML/UML each element compiles to",
        "the page's six BPMN figures are one element each, cropped from a BPMN model: "
        "BPMN_start_event.png (a start event circle with its outgoing sequence flow, 322x242), "
        "BPMN_event.png, BPMN_service_task.png (rounded task with the gear icon, 945x247), "
        "BPMN_user_task.png, BPMN_user_task_get.png, BPMN_gateway.png (a gateway diamond with its "
        "flows, 337x278). Each sits beside the Analyzer's own icon of the generated artefact "
        "(start_event_icon, service_task_icon, exclusive_gateway_icon, ...) and beside "
        "root_state_machine_analyzer.png, the generated state machine.",
        "the page's six BPMN element figures in the site-wide sweep sheet (sw_bpmn.png), and "
        "BPMN_start_event.png, BPMN_service_task.png and BPMN_gateway.png again at native size "
        "(sw_bpmn2.png, 322x242 / 945x247 / 337x278)",
        "This is a mapping reference: \"This page describes how the BPMN definitions from the "
        "Designer are compiled to UML, how they are presented in the Analyzer, and where the "
        "BPMN elements can be found again in the generated model.\" The BPMN it publishes is one "
        "element per figure, not a process; the rest of the page's figures are the Analyzer's "
        "icons and the generated state machine. Its article region carries no AI/LLM token at "
        "all (the AI screen fires 0 times), so no AI element is inside any of these BPMN "
        "fragments.",
        None, None),

    "/business-modeler/latest/model-processes": (
        "EXCLUDE", "E0-no-artefact", None,
        "no artefact: the eight figures are the model-type icons of the Business Modeler's "
        "catalogue - model_processes.png, value_added_chain.png, event_driven_process_chain.png, "
        "organizational_chart.png, data_model.png, system_landscape.png, bpmn_collaboration.png "
        "(an icon, 60x46 px) and free_model.png. None is a diagram of a process.",
        "bpmn_collaboration.png at native size (60x46 px - an icon, not a diagram) and the page's "
        "other seven figures in the site-wide sweep sheets",
        "The page is the model-type table of the Business Modeler: \"Seven model types are "
        "available to create a new model.\" Each row carries the model type's icon, and the "
        "figures are those icons. The page's BPMN talk is the name of one model type (BPMN "
        "Collaboration) in that table, not a published process model; its article region carries "
        "no AI/LLM token.",
        None, None),

    # ---- the AI-mentioning pages whose figures the AI-page pass looked at (2026-09-25) ---------
    # These are the pages the screen would have excluded mechanically although their article
    # region mentions AI: their figures are NOT diagram-named, so the site-wide sweep never saw
    # them. All 264 of their figures were downloaded (ledgers/_scheer_aipp.py) and looked at
    # (ai_s0/64/128/192.png, zoom sheets ai_zA/B/C.png). The rulings below record what that pass
    # found: three diagrams that are not BPMN (E1), two pages that publish BPMN 2.0 notation and
    # whose AI mention is not dismissible (UNCERTAIN, records 004/005), and three pages that
    # publish BPMN 2.0 notation whose only AI mention is a documentation link (E2). Every other
    # AI-mentioning page's figures were UI screenshots, icons, portal tiles, chat-bot captures or
    # diagrams of the Administration, and keep their mechanical rows.

    # -- a diagram the mechanical row said was not there, in a notation that is not BPMN -------
    "/academy/latest/an-introduction-to-scheer-pas": (
        "EXCLUDE", "E1-not-bpmn",
        "software component / architecture overview diagram (box-and-arrow), not BPMN 2.0",
        "pas_components_overview.png (873x1181): the PAS toolchain as labelled boxes - PAS "
        "Designer, Pro-Code DevKit, Asset Repository, PAS Compiler, Angular UI, xUML Runtime, PAS "
        "Administration, trace files / runtime logs / persistent state DB, feeding PAS Process "
        "Mining, Alerting and PAS Log Analyzer - joined by arrows labelled 'import model', 'run "
        "tests', 'configure trace', 'read trace'. The only process-shaped glyph on the whole "
        "canvas is a ~60 px icon inside the xUML Runtime box.",
        "the page's single figure pas_components_overview.png (873x1181) at native size in the "
        "AI-page zoom sheet (ledgers/_scheer/ai_zA.png)",
        "The introduction page's one figure is the component overview of the product itself: a "
        "software architecture box diagram, in no way a process model - no pool, lane, event, "
        "gateway or sequence flow, and no AI element. The row is E1 rather than E0 because a "
        "diagram *is* published on the page, just not a BPMN one. The page's process language is "
        "\"Scheer PAS supports developers from initial process and execution modeling to server "
        "deployment, administration and process/error analysis.\"; its AI mention (\"It brings "
        "together workflows, data, APIs, and AI agents to operationalize process automation "
        "across complex organizations ...\") is the product blurb, not an element in a diagram.",
        None, None,
        "Scheer PAS supports developers from initial process and execution modeling to server "
        "deployment, administration and process/error analysis."),

    "/designer/latest/validating-a-service": (
        "EXCLUDE", "E1-not-bpmn",
        "concept / marketing illustration (a wheel and a circle joined by an arrow), not BPMN 2.0 "
        "and not a process diagram",
        "development_cycle.png (837x355): a red three-segment wheel labelled 'Development-related "
        "Testing', 'Finished Milestone (Feature, Bugfix..)' and 'Continuous Development', and a "
        "green disc labelled 'Development-independent Testing', joined by a grey arrow labelled "
        "'Deployment'.",
        "the page's single figure development_cycle.png (837x355) at native size in the AI-page "
        "zoom sheet (ledgers/_scheer/ai_zA.png)",
        "The page's only figure is the release's illustration of the development cycle - the same "
        "kind of concept graphic the corpus excludes as E1, with no process elements at all. The "
        "page's 'BPMN' and 'AI' tokens both come from the Designer guide's chapter list in the "
        "article region ('... Modeling BPMN ... Using AI Agents ...'), i.e. from documentation "
        "navigation, not from the figure.",
        None, None,
        "With PAS 23.1, the development process in the Designer has been optimized."),

    "/release-notes/pas-26-0-release-notes": (
        "EXCLUDE", "E1-not-bpmn",
        "xUML activity diagram (Scheer PAS's execution-model notation: start node, data node, "
        "action box with input/output pins, end node) - the notation the page itself names",
        "extension.gif (1712x890, 87 frames): the activity diagram of an adapter operation - a "
        "black start node, the data node 'in EmployeeID: Integer', the action 'createEmployee' "
        "with its pins 'northwindEmployee' / 'employee' feeding 'out response: Employee...', and "
        "the end node. The page's other three figures are Administration UI of an AI agent "
        "(grafik-20260126-145622.png: 'Agent Name: claim-agent', 'As Service Provider: Google "
        "AI', System Prompt / User Prompt, 'Agent successfully deployed'), of a service's AI "
        "Agents table (grafik-20260123-084729.png: 'Agent Name: case-agent', 'Status: Online') and "
        "of the Update Runtime dialog (grafik-20260123-085849.png).",
        "extension.gif at 2x (3424x1780, frame 1) and the page's other three figures at native "
        "size in the AI-page zoom sheets (ledgers/_scheer/ai_zB.png)",
        "The page's only diagram is an execution-model activity diagram, and the page names that "
        "notation itself: \"If you drag and drop an adapter operation like e.g. REST, OData, SAP "
        "RFC Operation onto an activity diagram, the necessary extension is applied "
        "automatically.\" Its AI figures are the Administration's configuration and detail views "
        "of an AI agent - the agent is set up beside the process, and no process diagram is "
        "published on this page at all.",
        None, None,
        "If you drag and drop an adapter operation like e.g. REST, OData, SAP RFC Operation onto "
        "an activity diagram, the necessary extension is applied automatically."),

    # -- BPMN 2.0 published, AI mention not dismissible -> the researcher's call ---------------
    "/release-notes/pas-25-3-release-notes": (
        "UNCERTAIN", None,
        "BPMN 2.0 (the Designer's process canvas: start event, user task, exclusive gateway, end "
        "event, named sequence flows) in one figure, and the xUML activity diagram of the same "
        "example's operation in the lower half of that figure",
        "image-20250929-074728.png (1920x809): the ODataAdapter_Northwind example - above, a BPMN "
        "2.0 process with a start event, the tasks 'Show customer list', 'Show customer details' "
        "and 'Show orders', two exclusive gateways with the flows 'customer selected' / 'no "
        "customer selected ...', and an end event; below, the xUML activity diagram of the "
        "operation 'Get Data' with its Persisted/Local/Return bands. image-20251002-131703.png "
        "(1416x845): the Designer with AIAgent_InsuranceClaim_Example open - the CaseAgent's "
        "Prompt tab (System Prompt 'You are an insurance claim agent. ...', User Prompt, 'AI "
        "Service Provider Alias: OpenAI') and the Explorer's Implementation > Agents > CaseAgent > "
        "CaseAgentInterface > execute. The other two figures (image-20251008-120616.png, "
        "image-20250923-112152.png) are Administration and Designer UI.",
        "all 4 figures of the page at native size (image-20250929-074728.png 1920x809 and "
        "image-20251002-131703.png 1416x845 in full, the other two in the AI-page zoom sheet "
        "ledgers/_scheer/ai_zB.png)",
        "This page publishes both halves of the release's agentic-AI feature, in two different "
        "figures. The BPMN diagram (the OData example) contains no AI element; the AI element - "
        "the CaseAgent with its system and user prompt, bound to OpenAI - is shown as an agent "
        "asset of the AIAgent_InsuranceClaim_Example service. The release note frames the agent as "
        "part of the process: \"Designer Kubernetes: Integrate AI Agents Into Your Process Flow - "
        "This release supports agentic AI. You have the possibility to create AI agents and "
        "integrate them into your process execution.\" and \"New example for AI agent usage: "
        "AIAgent_InsuranceCase_Example\". That example's process model is not published on the "
        "page, so whether the agent sits inside a BPMN process cannot be settled from the figures "
        "- hence UNCERTAIN rather than E2, and record 004.",
        "004_release-notes-ai-agent-25-3",
        "This release-note page announces that AI agents can be integrated into the process "
        "execution and publishes (a) a BPMN 2.0 process diagram with no AI element (the OData "
        "example) and (b) a Designer screenshot of the AI agent CaseAgent of the "
        "AIAgent_InsuranceClaim_Example service with its System/User Prompt bound to OpenAI, plus "
        "'New example for AI agent usage: AIAgent_InsuranceCase_Example'. Does that example's "
        "published process model contain the AI agent as an element inside the process - as the "
        "tutorial's Insurance_Case_Process does (records 001-003) - and should this page therefore "
        "count as a page publishing an AI-enabled BPMN artefact? A reading of the page, and of the "
        "example itself if it is reachable, is needed to settle it.",
        "New example for parallel gateways in BPMN in combination with roles and user tasks: "
        "ParallelTasks_Onboarding_Example"),

    "/designer/latest/controls-panel": (
        "UNCERTAIN", None,
        "BPMN 2.0 (the Designer's process canvas; the figure's own Explorer names the process "
        "asset 'JanesFirstBPMN' and the canvas shows its start event, user task, gateway, service "
        "task and end event)",
        "controls_panel_default.png (1468x782): the Designer with JanesFirstBPMN open - start "
        "event, the user task 'James First User Task', the gateway 'James Gateway', the service "
        "task 'James First Service Task' and the end event, joined by 'James Relation_1' / 'James "
        "Relation_2' - beside the Controls panel; the validation area reads \"The activity diagram "
        "'James_FirstService_Task' does not do anything.\" The page's other six figures are panel "
        "icons and the additional-menu screenshot (controls_additional_menu.png).",
        "all 7 figures of the page: controls_panel_default.png at native size in the AI-page zoom "
        "sheet (ledgers/_scheer/ai_zA.png) and its Explorer tree again cropped at 3x "
        "(ledgers/_scheer/aipp/_crop_controls_panel_default.png), the rest in the AI-page contact "
        "sheets",
        "The page's BPMN figure shows a service with no AI element in it, but the page's own AI "
        "mention is about agents *in* the service whose export the panel triggers: \"the compiled "
        "agent configuration for each AI agent included in this service (one JSON file for each AI "
        "agent)\" and \"AI agents are available only on systems with Kubernetes setup. In a "
        "Docker ...\". The figure's Explorer (Base Types, Connectors, Process > JanesFirstBPMN, "
        "Forms, API, Implementation, Libraries) leaves Implementation collapsed, and that is where "
        "the Agents node sits in a service that has one (cf. record 004 fig 2) - so whether a "
        "service of this kind carries the agent inside its process cannot be read off the figure. "
        "That is hesitation, not a ground for exclusion, hence UNCERTAIN and record 005.",
        "005_controls-panel-agent-config-export",
        "The Controls panel page states that the service export contains the configuration of "
        "'each AI agent included in this service'. Its figure shows the BPMN process "
        "JanesFirstBPMN, with no AI element visible in the model and the Explorer's "
        "'Implementation' node collapsed. Does a service of this kind carry the AI agent as an "
        "element of its BPMN process, so that this page documents an AI-enabled process artefact - "
        "or is the agent only a service asset whose configuration the export happens to include? A "
        "reading of the page, and of the export documentation behind it, is needed.",
        "Use this option to access the service logs of the xUML service and the Angular "
        "Application server."),

    # -- BPMN 2.0 published, the only AI mention is a documentation link -> E2 ------------------
    "/designer/latest/troubleshooting": (
        "EXCLUDE", "E2-no-ai-element",
        "BPMN 2.0 (the Designer's process canvas, inside a UI screenshot)",
        "grafik-20250515-080253.png (1839x1076): the Designer with JanesFirstBPMN open - start "
        "event, 'James First User Task', 'James Gateway', 'James First Service Task', end event - "
        "under an 'Operation Error' banner, with the validation message \"The activity diagram "
        "'James_FirstService_Task' does not do anything.\" The page's other four figures are "
        "Designer UI (validation_panel.png, clear_compiler_cache.png, "
        "controls_export_support_data.png, export_compiled_service.png).",
        "all 5 figures of the page: grafik-20250515-080253.png in the AI-page zoom sheet "
        "(ledgers/_scheer/ai_zC.png) and its Explorer tree cropped at 3x, the rest in the AI-page "
        "contact sheets",
        "The BPMN model the page publishes (JanesFirstBPMN) contains no AI element. The page's "
        "only AI token is the name of a chapter in the Designer guide's own link list inside the "
        "article region - \"Validation Panel Error Handling AI Agents Executed Applications\" - "
        "which refers to the documentation chapter 'Error Handling AI Agents', not to anything "
        "inside the process shown. The AI mention is therefore dismissed, and the row is E2.",
        None, None,
        "Validation Panel Error Handling AI Agents Executed Applications"),

    "/help/troubleshooting-designer": (
        "EXCLUDE", "E2-no-ai-element",
        "BPMN 2.0 (the Designer's process canvas, inside a UI screenshot)",
        "grafik-20250515-080253.png (1839x1076) - the same file, byte for byte, as the one on "
        "/designer/latest/troubleshooting (sha1 0014c4927cdf): the Designer with JanesFirstBPMN "
        "open and an 'Operation Error' banner; plus validation_panel.png, clear_compiler_cache.png, "
        "controls_export_support_data.png, export_compiled_service.png.",
        "all 5 figures of the page (the diagram figure in the AI-page zoom sheet "
        "ledgers/_scheer/ai_zC.png, the rest in the AI-page contact sheets)",
        "The help space is the un-versioned twin of the designer space: this page publishes the "
        "same five figures as /designer/latest/troubleshooting, byte for byte (checked by content "
        "hash). The BPMN model (JanesFirstBPMN) contains no AI element, and the page's only AI "
        "token is the chapter name in the guide's link list - \"Validation Panel Error Handling AI "
        "Agents Executed Applications\" - i.e. the documentation chapter 'Error Handling AI "
        "Agents'. The row is E2 for the same reason as its designer twin. It is not E3: the same "
        "diagram is *not* recorded in the corpus (neither page produces a record), so there is no "
        "`duplicate_of` to name.",
        None, None,
        "Validation Panel Error Handling AI Agents Executed Applications"),

    "/designer/latest/deploying-a-service": (
        "EXCLUDE", "E2-no-ai-element",
        "BPMN 2.0 (the Designer's process canvas, inside a UI screenshot), shown above the xUML "
        "activity diagram of the same service's operation",
        "test_service.png (1478x844): the Designer with JanesFirstBPMN open - the start event "
        "'Start test', the user task 'Show test form' and the end event - above the activity "
        "diagram of the operation ('On Exit': Message / message_TestForm / Persisted / Local), "
        "with the validation messages \"The input parameter node 'message' ... has no outgoing "
        "flows\" and \"The activity diagram 'behavior_Show_test_form' does not do anything.\" The "
        "page's other nineteen figures are deployment UI: deployment_properties.png, "
        "select_deployment_target.png, enter_service_version.png, the button_* screenshots "
        "(deploy, administration, API, application, log analyzer), the test-form screenshots and "
        "the example application's start page.",
        "all 20 figures of the page: test_service.png at native size in the AI-page zoom sheet "
        "(ledgers/_scheer/ai_zC.png), the rest in the AI-page contact sheets (ai_s64.png, "
        "ai_s128.png)",
        "The BPMN model published here (JanesFirstBPMN) contains no AI element - it is the "
        "Designer's own example service, used to walk through the deployment steps. The page's "
        "only AI token is the Designer guide's chapter list in the article region (\"... Modeling "
        "APIs Using AI Agents Implementing Your Process ...\"), i.e. a documentation link, so the "
        "row is E2.",
        None, None,
        "Modeling Connectors Modeling BPMN Modeling Forms Modeling APIs Using AI Agents "
        "Implementing Your Process Sharing Designer Content"),

    # ---- the audit sample's diagram finds, re-coded from E0 to E1 (2026-09-25) ----------------
    # The screen's calibration pass (ledgers/_scheer_audit.py: every 9th page that has figures but
    # no diagram-named figure and no process word, all its figures downloaded and tiled) found 7
    # diagram figures on 5 pages, none of them BPMN. Those 5 pages were excluded mechanically as
    # "no diagram", which is what the audit was there to catch; they are re-coded here to E1 with
    # the notation named. None of the 5 mentions AI (the AI screen does not fire on any of them).

    "/academy/latest/building-a-new-service-structure-md18": (
        "EXCLUDE", "E1-not-bpmn",
        "xUML / Designer implementation diagram (start node, yellow action boxes, sequence arrows) "
        "- not BPMN 2.0: no pool, lane, event, gateway or task shape",
        "rename_gettitleservice_1.png (1311x1064): the Designer with the service's Implementation "
        "tree open next to the model canvas, on which a black start node leads to the action boxes "
        "'getTileService' and 'GetTitle' (arrows labelled), with the class/attribute panel beneath. "
        "rename_gettitleservice_2.png is the same canvas after the rename.",
        "both figures of the page at native size in the audit-sample zoom sheet "
        "(ledgers/_scheer/au_z1.png)",
        "The page's two figures are the implementation (xUML) view of the service the tutorial is "
        "renaming, not a BPMN process diagram: the nodes are the Designer's yellow action boxes "
        "joined by plain arrows from a black start node, and the page's own prose is about service "
        "structure and renaming. Found by the audit sample of the mechanically excluded pages.",
        None, None),

    "/business-modeler/latest/panels": (
        "EXCLUDE", "E1-not-bpmn",
        "Business Modeler canvas with an event-driven process chain (coloured event and function "
        "boxes joined by typed connectors) - a proprietary notation, not BPMN 2.0",
        "Pannels_Overview.png (1919x1046) and Closing_Pannels.png (1919x1046): the Business "
        "Modeler with an Event Driven Process Chain on the canvas - the purple 'Event' and green "
        "'Function' boxes (Triggered by: Event, Triggered by: Function), the orange 'Data' and "
        "'Organizational Unit' objects and their connectors - plus the model tree and the element "
        "palette (Event, Function, Rule, Process Interface, ...). Hiding_Pannels.png is the same "
        "UI with a panel hidden.",
        "all three figures of the page in the audit-sample contact sheet (ledgers/_scheer/au_s2.png) "
        "and Pannels_Overview.png / Closing_Pannels.png again at native size in "
        "ledgers/_scheer/au_z1.png",
        "The Business Modeler's canvas carries the model types it documents (event-driven process "
        "chain, value-added chain, ...), not BPMN: the page itself names the canvas \"the Canvas\" "
        "and its palette lists Event, Function, Rule, Process Interface, Data - BPMN's elements "
        "(pool, lane, gateway, start event) are not among them. The page teaches the panel UI. "
        "Found by the audit sample.",
        None, None),

    "/designer/latest/adapters": (
        "EXCLUDE", "E1-not-bpmn",
        "architecture / integration illustration (two labelled boxes joined by an arrow), not a "
        "process diagram and not BPMN 2.0",
        "connector_adapter.png (742x297): a red-bordered box 'xUML Service' containing a "
        "'REST Interface / Connector' circle, an orange arrow labelled 'Adapter' and a "
        "green-bordered box 'REST Service' with a service icon - the page's illustration of what "
        "an adapter sits between.",
        "the page's single figure connector_adapter.png at native size in the audit-sample zoom "
        "sheet (ledgers/_scheer/au_z1.png)",
        "The page is the adapter reference (which backends the Designer can reach, e.g. REST, "
        "OData, SAP RFC). Its one figure shows the relation between a service and a REST backend - "
        "boxes, an arrow and labels; there is no process, no event, no task and no flow. Found by "
        "the audit sample.",
        None, None),

    "/designer/latest/classtoxml": (
        "EXCLUDE", "E1-not-bpmn",
        "UML class diagram (classes with typed attributes and association arrows), not BPMN 2.0",
        "class_address_xml_mapping.png (944x193) and grafik-20240729-090728.png (522x163): UML "
        "class boxes - 'Address' with '+id: String', '+city' and '+street' as associations to the "
        "class 'String'; and 'XMLComposeOptions' with '+prolog: String [0..1]', '+timezone: "
        "String [0..1]', '+dateFormatString: String [0..1] = %F', '+encoding: String [0..1] = UTF8', "
        "'+rootName: String [0..1]', '+rootNamespace: String [0..1]'.",
        "both figures of the page at native size in the audit-sample zoom sheet "
        "(ledgers/_scheer/au_z1.png)",
        "The page is the reference for the classtoxml operation; its two figures are the UML "
        "classes whose objects the operation maps ('The operation takes any object ( anObject ) and "
        "tries to map it to an XML document.'). UML class notation, not BPMN. Found by the audit "
        "sample.",
        None, None),

    "/designer/latest/creating-an-implementation-factory": (
        "EXCLUDE", "E1-not-bpmn",
        "UML class diagram with stereotypes («implementationFactory», «implementation»), not BPMN "
        "2.0",
        "implementation_factory.png (737x473): the «implementationFactory» class 'FactoryClass' "
        "over the «implementation» class 'ImplementationInterface', with the subclasses "
        "'ImplementationA' (property1: Integer, operationA(parameter1: Integer): String) and "
        "'ImplementationB' (property1: String, propertyB: Float, ...), joined by generalisation "
        "arrows.",
        "the page's single figure implementation_factory.png at native size in the audit-sample "
        "zoom sheet (ledgers/_scheer/au_z1.png)",
        "The page explains the implementation-factory pattern in UML terms ('If you are familiar "
        "with the factory concept, and want to use it in your service model, you can do so using "
        "the Implementation Factory ...'), and its one figure is that pattern as a UML class "
        "diagram. No process notation is published. Found by the audit sample.",
        None, None),
}
