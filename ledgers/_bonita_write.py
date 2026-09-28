#!/usr/bin/env python3
"""Per-page rulings for the bonitasoft census (worker elicitation-6f).

RULINGS: url -> (verdict, reason, notation, artefacts_on_page, figures_looked_at, note,
                 record_stem, question [, evidence_override [, judgment]])

Only pages the screen flags (ledgers/_bonita_rows.py `tier()` == "judged") appear here; every
flagged page must appear, the build fails loudly otherwise. `reason` comes from the closed list
(E0-no-artefact, E1-not-bpmn, E2-no-ai-element, E3-duplicate), and the note carries the verbatim
quote the dismissal rests on.

`judgment` is True only where the verdict turned on what the pixels show (was this figure a BPMN
diagram? is an AI element visible inside it?). Where the page's own prose and figure names settle
it, the row is screen-decided and `judgment` stays False - the same convention as the scheer-pas
ledger. The eyeball pass over every judged page's figures is recorded in the ledger footer
(`figures_looked`) and in the calibration sample, not in `judgment`.
"""

ENUMERATION_NOTE = (
    "The docs portal publishes a sitemap index (https://documentation.ofelia.com/sitemap.xml) "
    "with one sitemap per doc component, each carrying an exact URL count; the marketing site "
    "does the same (https://www.ofelia.com/sitemap.xml, one <loc> per hreflang). Population = "
    "the `latest` version of all 7 doc components (bcd 9, bonita 374, cloud 30, labs 20, "
    "process-designer 41, test-toolkit 15, ui-builder 44 = 533) + the 20 paths published only "
    "under an older version (bonita/2024.2 applications/*, bonita/0/archives/*, ...) + the 254 "
    "English pages of www.ofelia.com (of 1067 <loc> total, the rest are the fr/es locales of the "
    "same pages) = %d pages. Everything was fetched and cached (ledgers/_bonita_crawl.py, ~1 "
    "request/s, HTML in ledgers/_bonita/pages/, index in ledgers/_bonita/index.json). `latest` "
    "resolves to 2026.2 (the page's git edit link names modules/.../2026.2); the other versions "
    "(2026.1 ... 2023.1, /next/, /0/) are a version facet of the same pages and are not counted "
    "twice. No keyword facet was used to narrow anything: every page's content region is screened "
    "for process and AI tokens and for diagram-bearing figures, and the pages that fire are "
    "judged by eye. Second, smaller population group: every GitHub repository linked from the "
    "docs pages that publishes example processes or README diagrams (ledgers/_bonita_repos.py, "
    "links extracted from the crawled pages, never guessed; trees read through the public GitHub "
    "API and cached in ledgers/_bonita/repos_trees.json), enumerated as one row per repository "
    "(53) plus one row per `.bpmn`/`.proc` file found in a tree = %d rows. Total population = "
    "%d rows."
)

RECORDS_WRITTEN = [
    "001_ai-anthropic-process-flow", "002_ai-azure-process-flow",
    "003_ai-cohere-process-flow", "004_ai-deepseek-process-flow",
    "005_ai-gemini-process-flow", "006_ai-groq-process-flow",
    "007_ai-mistral-process-flow", "008_ai-ollama-process-flow",
    "009_ai-openai-process-flow", "010_anthropic-ai-demo-proc",
    "011_azure-openai-demo-proc", "012_kyc-bpmn-diagram",
    "013_bonita-studio-ai-assistant-illu", "014_ofelia-workflow-card",
    "015_ofelia-agent-runtime-diagram", "016_ai-bpmn-generator-promo",
]

# --- corpus records as the single source of truth for the nine AI connector rows --------------
# The 9 docs rows and the 5 site rows carry a question and a verbatim evidence quote that also
# live in the corpus record (same page, same wording). Reading them back from the record file
# keeps the ledger and the record from drifting apart; the record is where the human reviewer
# reads them anyway.
import pathlib  # noqa: E402
import re  # noqa: E402

RECORD_DIR = pathlib.Path(__file__).resolve().parent.parent / "corpus" / "bonitasoft"


def record_field(stem, key):
    """Pull one `key: >-` YAML block out of corpus/bonitasoft/<stem>.md, unwrapped."""
    text = (RECORD_DIR / (stem + ".md")).read_text(encoding="utf-8")
    m = re.search(r"^%s: >-\n((?:[ \t]+.*\n)+)" % key, text, re.M)
    assert m, "no %s in %s" % (key, stem)
    return " ".join(m.group(1).split())

DUPLICATE_OF = {}
VISUAL_CHECK = {
    # The KYC record's capture is 1400x152 of a 2492x270 canvas whose export draws its text as
    # paths, so its labels were read from a half-scale raster. The verdict (UNCERTAIN) already
    # routes it to the researcher; the visual flag says the *image* is what to check.
    "https://www.ofelia.com/blog-article/the-power-of-automated-kyc-transforming-banking-and-"
    "insurance-e0c48": True,
}

RULINGS = {}

# --- note templates -------------------------------------------------------------------------
DESIGN_TIME = (
    "The page's figure is the Process Designer editor itself - a genuine BPMN 2.0 diagram on a "
    "drag-and-drop canvas (palette, pools/lanes, start and end events, tasks, gateways, "
    "sequence flows). The only AI on the page is the *design-time* generator: the editor's AI "
    "toolbar action and the \"Generate with AI\" dialog. Quoted: \"%s\" - that is AI producing "
    "the diagram, not an AI element inside the process, which is exactly the case the "
    "bonitasoft assignment records as E2 (\"Natural language -> BPMN modeling\" on the product "
    "page is design-time AI). No AI task, AI gateway or AI service task appears on the canvas."
)
STUDIO = (
    "The page's figures are Bonita Studio screenshots in which the process diagram is visible "
    "(%s) - BPMN 2.0 notation: a pool, a start event, user tasks, a gateway and end events. The "
    "page carries no AI mention at all (the AI screen does not fire on its content region), the "
    "diagram's activities are human tasks, and no service task appears that could carry an "
    "invisible AI-bound implementation. Quoted: \"%s\"."
)
NOT_BPMN = (
    "The page's diagram-shaped figure (%s) is not BPMN 2.0: it is %s. There are no pools, "
    "lanes, events, gateways or sequence flows - nothing in it is a process element. Quoted: "
    "\"%s\"."
)
NO_ARTEFACT = (
    "No process artefact on the page: the screen finds no BPMN marker, no .bpmn link and no "
    "figure whose name, alt or caption names a diagram; the figures are %s. The token that put "
    "the page on the judgement worklist is not an AI mention at all - it is \"%s\". Nothing to "
    "collect."
)
NO_ARTEFACT_AI = (
    "The page documents an AI connector but publishes no process artefact: no diagram, no image "
    "of one, no .bpmn or .proc file (figures: %s). The AI is described as connector "
    "configuration and parameter tables only. Quoted: \"%s\"."
)


def R(*t):
    return t


def _add(url, *t):
    assert url not in RULINGS, url
    RULINGS[url] = t


D = "https://documentation.ofelia.com"

# ================= docs: bonita component ===================================================
_add(D + "/bonita/latest/api/engine-api-overview", "EXCLUDE", "E1-not-bpmn",
     "architecture box diagram", "dev_overview_api_access.png (alt \"Diagram of API access options\")",
     "dev_overview_api_access.png looked at", NOT_BPMN % (
         "dev_overview_api_access.png",
         "an architecture box diagram - three nested boxes labelled \"Client application\", "
         "\"HTTP\" and \"Engine\"",
         "Diagram of API access options"), None, None, None, True)
_add(D + "/bonita/latest/api/rest-api-extension-archetype", "EXCLUDE", "E0-no-artefact", None,
     "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all",
         "prompt a terminal and enter the following command"), None, None, None, False)
_add(D + "/bonita/latest/api/rest-api-overview", "EXCLUDE", "E1-not-bpmn",
     "architecture box diagram", "rest_api_architecture_overview.png",
     "rest_api_architecture_overview.png looked at", NOT_BPMN % (
         "rest_api_architecture_overview.png",
         "an architecture box diagram - client icons joined by labelled arrows to the REST API, "
         "the Bonita Engine and a database",
         "diagram of architecture of a REST client integrated with Bonita"), None, None, None, True)
_add(D + "/bonita/latest/applications/ui-designer/customize-living-application-theme", "EXCLUDE",
     "E0-no-artefact", None, "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all",
         "prompt a terminal and enter the following command"), None, None, None, False)
_add(D + "/bonita/latest/bcd/", "EXCLUDE", "E1-not-bpmn",
     "DevOps/architecture illustration", "CI-CD-architecture-diagram-*.png (2)",
     "both CI-CD-architecture-diagram figures looked at", NOT_BPMN % (
         "CI-CD-architecture-diagram-application-deployment.png",
         "a DevOps architecture illustration - product logos (Bonita, Docker, Git, Kubernetes) "
         "joined by arrows around labelled stages, with an environment axis",
         "These deployment modes are illustrated in the diagram below"), None, None, None, True)
_add(D + "/bonita/latest/bonita-studio-docker-environment", "EXCLUDE", "E1-not-bpmn",
     "architecture / user-journey diagram (SVG)", "user-journey.svg, arch-diagram.svg",
     "SVG titles read from the source (\"User journey: open browser\", \"Architecture: browser "
     "connects to Nginx which routes to Guacamole\")", NOT_BPMN % (
         "arch-diagram.svg",
         "an architecture diagram - a browser connecting through Nginx to Guacamole, which "
         "streams the desktop; its own accessible name says so",
         "Architecture: browser connects to Nginx which routes to Guacamole which streams the "
         "desktop"), None, None, None, True)

# --- getting started: plain BPMN, no AI ------------------------------------------------------
_add(D + "/bonita/latest/getting-started/declare-business-variables", "EXCLUDE", "E2-no-ai-element",
     "Bonita Studio BPMN diagram (pool with the process visible behind the variable dialogs)",
     "select-process-pool.gif, declare-business-variable.gif, define-condition.gif",
     "the three figures looked at", None, None, None, True)
_add(D + "/bonita/latest/getting-started/declare-contracts", "EXCLUDE", "E2-no-ai-element",
     "Bonita Studio BPMN diagram behind the contract dialogs",
     "contract-MVC.PNG, declare-process-instantiation-contract.gif, declare-user-task-contract.gif, operation.png",
     "the four figures looked at", None, None, None, True)
_add(D + "/bonita/latest/getting-started/define-who-can-do-what", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram with lanes (diagrams-with-lanes.png) plus Studio screenshots",
     "diagrams-with-lanes.png, add-and-organize-lanes.gif, map-actor-to-lane.gif, "
     "configure-initiator-actor-filter.gif",
     "figures looked at; diagrams-with-lanes.png is a clean BPMN pool with two lanes",
     "diagrams-with-lanes.png, the actor-mapping and lane-mapping GIFs", None, None, None, True)
_add(D + "/bonita/latest/getting-started/draw-bpmn-diagram", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagrams (new-default-diagram.png, switch-from-parallel-to-exclusive-gateway.png, "
     "process-diagram-before-transitions-configured.png, transition-name-and-condition.gif)",
     "new-default-diagram.png, switch-from-parallel-to-exclusive-gateway.png, "
     "process-diagram-before-transitions-configured.png, transition-name-and-condition.gif",
     "figures looked at: a pool with Start1 -> Step1, and the leave-claim diagram with a "
     "gateway; human tasks and gateways only", None, None, None, True)
for _u, _looked in (
    ("/bonita/latest/identity/single-sign-on-with-kerberos", "kerberos-ad.png, kerberos-overview.png"),
    ("/bonita/latest/identity/single-sign-on-with-oidc", "oidc-overview.png"),
):
    _add(D + _u, "EXCLUDE", "E1-not-bpmn", "architecture box diagram", _looked,
         _looked + " looked at", NOT_BPMN % (
             _looked.split(",")[0].strip(),
             "an architecture box diagram - Domain Controller / Principal / Subject boxes or "
             "client, filter and portal boxes joined by labelled arrows", "Authentication over OIDC"),
         None, None, None, True)
_add(D + "/bonita/latest/pages-and-forms/customize-display-process-monitoring", "EXCLUDE",
     "E0-no-artefact", None, "pb-export.png, process-visu-fragment-variables.png, process-visu-page-fragment.png",
     "the three figures looked at: an export-button icon and two UI Designer screens",
     NO_ARTEFACT % (
         "an export-button icon and UI Designer page fragments, not process diagrams",
         "Export button"), None, None, None, True)
_add(D + "/bonita/latest/pages-and-forms/manage-control-in-forms", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram (leave_request_management_process.png) plus form screenshots",
     "leave_request_management_process.png and the Studio screenshot with the \"Leave request\" "
     "pool", "leave_request_management_process.png looked at: pool, start event, a task, an "
     "exclusive gateway and end events", None, None, None, True)
_add(D + "/bonita/latest/pages-and-forms/widgets", "EXCLUDE", "E0-no-artefact", None,
     "24 widget icon/preview images (input.png, currency-input.png, select.png, ...)",
     "a contact sheet of the widget images", NO_ARTEFACT % (
         "UI Designer widget icons and previews, one per widget",
         "Documents that are not previewable are prompted to be downloaded"), None, None, None, False)

# --- connectors -------------------------------------------------------------------------------
_add(D + "/bonita/latest/process/actor-filter-archetype", "EXCLUDE", "E1-not-bpmn",
     "package/class overview diagram", "connector-def-xsd-overview.png, connector-impl-xsd-overview.png",
     "both looked at", NOT_BPMN % (
         "connector-def-xsd-overview.png",
         "a package / class overview diagram - nested boxes listing element names and "
         "attributes with inheritance edges",
         "Connector definition xsd overview"), None, None, None, True)
_add(D + "/bonita/latest/process/connector-archetype", "EXCLUDE", "E1-not-bpmn",
     "package/class overview diagram", "connector-def-xsd-overview.png, connector-impl-xsd-overview.png",
     "both looked at", NOT_BPMN % (
         "connector-def-xsd-overview.png",
         "a package / class overview diagram - nested boxes listing element names and "
         "attributes with inheritance edges",
         "Connector definition xsd overview"), None, None, None, True)
_add(D + "/bonita/latest/process/connector-archetype-tutorial", "EXCLUDE", "E0-no-artefact", None,
     "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all",
         "prompt a terminal and enter the following command"), None, None, None, False)
_add(D + "/bonita/latest/process/connect ors-index".replace(" ", ""), "EXCLUDE", "E0-no-artefact",
     None, "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all", "Combine the power of AI and Process Automation"),
     None, None, None, False)
_add(D + "/bonita/latest/process/ai-connector", "EXCLUDE", "E1-not-bpmn",
     "integration/architecture flow diagram (alt: \"AI Connectors flux\") + provider logos",
     "ai-connectors.png (zoomed) and the nine provider logos",
     "ai-connectors.png zoomed to 922x293 native: boxes \"My Process\", \"AI Connector\", a "
     "cloud labelled HTTPS, \"AI Chat completion\", \"Internal OCR\", arrows labelled \"LLM "
     "Request\" / \"LLM Response\"",
     "The AI is visible in the figure, but the figure is not a BPMN diagram: it is an "
     "integration/architecture flow diagram (boxes, a cloud icon and labelled arrows), with no "
     "pool, lane, event, gateway or sequence flow - so the AI element is not *inside a process*. "
     "Quoted: \"AI connectors support three operations\".", None, None, None, True)
for _slug in ("ai-agent-connector", "mistral-ocr-connector"):
    _add(D + "/bonita/latest/process/" + _slug, "EXCLUDE", "E0-no-artefact", None, "no figures",
         "no figures on the page", NO_ARTEFACT_AI % (
             "none - the page has no figures at all",
             "The Bonita AI Agent Orchestrator connectors let you execute AI agents with "
             "tool-use capabilities" if _slug == "ai-agent-connector"
             else "extract text, structured fields, tables, and classify documents using "
                  "Mistral AI vision models"), None, None, None, False)
for _p in ("adobe-sign-connector", "telegram-connector", "zendesk-connector"):
    _add(D + "/bonita/latest/process/" + _p, "EXCLUDE", "E0-no-artefact", None, "no figures",
         "no figures on the page", NO_ARTEFACT % (
             "none - the page has no figures at all",
             {"adobe-sign-connector": "HTTP Code Behavior 200/201 Success",
              "telegram-connector": "Send Message",
              "zendesk-connector": "Zendesk subdomain"}[_p]), None, None, None, False)

# --- the nine AI connector pages: prose "Process flow" binds a service task to an AI connector --
_AI_FLOWS = {
    "ai-anthropic-connector": (
        "A scanned identity document is uploaded to the process A service task uses the Ask "
        "connector with the document attached Claude analyzes both text and visual elements"),
    "ai-azure-connector": (
        "An expense report is submitted through a Bonita form A service task uses the Extract "
        "connector to parse the document"),
    "ai-cohere-connector": (
        "A compliance officer submits a question about internal policies A service task attaches "
        "relevant policy documents and uses the Ask connector"),
    "ai-deepseek-connector": (
        "A batch of support tickets or reports is collected in the process A service task uses "
        "the Ask connector to generate structured summaries"),
    "ai-gemini-connector": (
        "An invoice document is uploaded or received via email A service task uses the Extract "
        "connector to parse the invoice"),
    "ai-groq-connector": (
        "A user opens a human task form with complex data entry requirements As the user fills "
        "fields, a service task calls Groq for instant validation and suggestions"),
    "ai-mistral-connector": (
        "An HR document containing employee personal data is uploaded A service task uses the "
        "Extract connector to parse the document"),
    "ai-ollama-connector": (
        "Developer configures a connector in Bonita Studio with Ollama Prompts and JSON schemas "
        "are tested locally with instant feedback"),
    "ai-openai-connector": (
        "A support ticket is created with customer information and issue description A service "
        "task uses the Ask connector to generate an email draft"),
}
for _i, (_slug, _flow) in enumerate(sorted(_AI_FLOWS.items()), 1):
    _stem = "%03d_%s-process-flow" % (_i, _slug.replace("-connector", ""))
    _add(D + "/bonita/latest/process/" + _slug, "UNCERTAIN", None, None,
         "no figures (the page publishes no image of the process at all)",
         "checked the page's own content region and every figure reference",
         "The page's \"Use cases\" section walks a process through in words: \"" + _flow +
         "\" - the AI connector is the implementation of a service task, which is the delegated-"
         "binding class the assignment puts in scope, but the page publishes no diagram of that "
         "process. Record written with the binding quoted; verdict UNCERTAIN per the source's "
         "rule \"a plain task whose surrounding text binds it to an AI connector is UNCERTAIN "
         "with the binding quoted, never E2\".", _stem,
         record_field(_stem, "question"), record_field(_stem, "ai_evidence"))

# --- process pages with real BPMN ------------------------------------------------------------
_add(D + "/bonita/latest/process/diagram-tasks", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram (leave_request_management_process_tasklist.png) + tasklist screenshots",
     "leave_request_management_process_tasklist.png", "figure looked at: a pool with a start "
     "event, a task, a gateway and end events", None, None, None, True)
_add(D + "/bonita/latest/process/optimize-user-tasklist", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram (leave_request_management_process_tasklist.png) + tasklist screenshots",
     "leave_request_management_process_tasklist.png", "figure looked at: pool, start event, "
     "task, gateway, end events", None, None, None, True)
_add(D + "/bonita/latest/process/gateways", "EXCLUDE", "E2-no-ai-element",
     "three BPMN fragments (parallel, exclusive and inclusive gateway)",
     "papde_pm_diag_gateways_parallel_gate.png, papde_pm_diag_gateways_exclusive_gate.png, "
     "papde_pm_diag_gateways_inclusive_gate.png",
     "all three looked at: Start -> Step1/Step2 -> gateway -> Step3/Step4 in Studio", None, None,
     None, True)
_add(D + "/bonita/latest/process/web-service-connector-overview", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram (webservice_diagram.png) - a tutorial process whose activity is bound to a "
     "web service, not to an AI connector", "webservice_diagram.png",
     "figure looked at: pool, Start1, three user tasks, a text annotation, End1", None, None,
     None, True)
_add(D + "/bonita/latest/process/web-service-tutorial", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram (webservice_diagram.png)", "webservice_diagram.png", "figure looked at: the "
     "same tutorial process, tasks bound in the text to the SOAP web service connector",
     None, None, None, True)

# --- runtime ---------------------------------------------------------------------------------
_add(D + "/bonita/latest/runtime/admin-application-process-list", "EXCLUDE", "E0-no-artefact",
     None, "admin-application-process-list.png",
     "figure looked at: the Administrator Application process list table",
     NO_ARTEFACT % ("a portal process list table", "Bonita Administrator Application Process list"),
     None, None, None, True)
_add(D + "/bonita/latest/runtime/bonita-docker-installation", "EXCLUDE", "E0-no-artefact", None,
     "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all", "it also deactivates the HTTP API"), None, None,
     None, False)
_add(D + "/bonita/latest/runtime/engine-architecture-overview", "EXCLUDE", "E1-not-bpmn",
     "layered architecture diagram", "dev_arch_engine_architecture_simple.png",
     "figure looked at: three coloured horizontal bands labelled APIs / BPM services / Generic "
     "services", NOT_BPMN % (
         "dev_arch_engine_architecture_simple.png",
         "a layered architecture diagram - three coloured horizontal bands labelled APIs, BPM "
         "services and Generic services",
         "engine architecture diagram"), None, None, None, True)
_add(D + "/bonita/latest/runtime/execution-sequence-states-and-transactions", "EXCLUDE",
     "E1-not-bpmn", "state-transition diagram of the task lifecycle",
     "user_task_details.png, user_task_execution_with_connector.png, "
     "user_task_execution_without_connector.png", "all three zoomed and looked at",
     NOT_BPMN % (
         "user_task_execution_with_connector.png",
         "a state-transition diagram of the user task lifecycle (Initializing / Ready / "
         "Completing Boundary / Completed boxes with transaction brackets) - the page's own alt "
         "calls it \"Diagram of the states and transactions when a user task with connectors is "
         "executed\"", "Diagram of the details of user task execution"), None, None, None, True)
_add(D + "/bonita/latest/runtime/hardware-and-software-requirements", "EXCLUDE", "E0-no-artefact",
     None, "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all", "A JDK ( not a JRE ) 17 is required"), None,
     None, None, False)
_add(D + "/bonita/latest/runtime/overview-of-bonita-bpm-in-a-cluster", "EXCLUDE", "E1-not-bpmn",
     "deployment architecture diagram", "cluster_structure.png", "figure looked at",
     NOT_BPMN % (
         "cluster_structure.png",
         "a deployment architecture diagram - a Client box over a Load Balancer over three "
         "App Server / Portal / Engine boxes over an Engine Database",
         "Cluster structure diagram"), None, None, None, True)
_add(D + "/bonita/latest/runtime/reporting-app", "EXCLUDE", "E1-not-bpmn",
     "reporting application dashboards", "reporting-app-process-selection-page.png, "
     "reporting-app-process-historical-data-page.png, reporting-app-human-tasks-page.png",
     "figures looked at: the Reporting application's process table, charts and task table",
     NOT_BPMN % (
         "reporting-app-process-historical-data-page.png",
         "a reporting dashboard - bar charts and tables over historical case data, not a process "
         "diagram", "Process selection"), None, None, None, True)
_add(D + "/bonita/latest/runtime/user-process-list", "EXCLUDE", "E2-no-ai-element",
     "Bonita Studio process diagram visible in Actor-mapping.png / Set-as-initiator.png, plus "
     "portal screenshots", "Actor-mapping.png, Set-as-initiator.png, user_process_list.png",
     "figures looked at: the Studio diagram with the actor-mapping and initiator panels",
     None, None, None, True)
_add(D + "/bonita/latest/runtime/user-task-list", "EXCLUDE", "E0-no-artefact", None,
     "tasklist-elements.png, tasklist-popup.png, tasklist-settings-and-tabs.png, tasklist-fullpage.png",
     "figures looked at: User Application task list, task form popup and settings screens",
     NO_ARTEFACT % ("User Application task list and form screenshots", "User task list"), None,
     None, None, True)
_add(D + "/bonita/latest/share-a-repository-on-github", "EXCLUDE", "E0-no-artefact", None,
     "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all",
         "a dialog might prompt to ask for an identity"), None, None, None, False)
_add(D + "/bonita/latest/software-extensibility/custom-library-development", "EXCLUDE",
     "E0-no-artefact", None, "no figures", "no figures on the page", NO_ARTEFACT % (
         "none - the page has no figures at all",
         "jacoco-maven-plugin"), None, None, None, False)
_add(D + "/cloud/latest/manage/ldap-configuration", "EXCLUDE", "E1-not-bpmn",
     "cloud architecture diagram", "ldap-config-diagram.png", "figure looked at",
     NOT_BPMN % (
         "ldap-config-diagram.png",
         "a cloud architecture diagram - a Bonita Cloud box joined to a BPM/Engine box and an "
         "LDAP server on the customer network, with a \"trusted relation\" arrow",
         "ldap config diagram"), None, None, None, True)

# --- labs: BICI / BPI ------------------------------------------------------------------------
_add(D + "/labs/latest/bici/configure", "EXCLUDE", "E0-no-artefact", None,
     "configuration_polling_status.png, configuration_process_configuration.png",
     "figures looked at: BICI configuration panels and tables",
     NO_ARTEFACT % ("BICI configuration panels, not diagrams", "BICI LA Configuration Polling"),
     None, None, None, True)
_add(D + "/labs/latest/bici/architecture", "EXCLUDE", "E1-not-bpmn",
     "an architecture box diagram (bici_architecture.png, alt \"Bonita Intelligent Continuous "
     "Improvement Add-on Architecture\")",
     "bici_architecture.png looked at (910x551): boxes for the Bonita Database, the BICI "
     "connection pool, Elasticsearch and the two Living Applications, joined by arrows",
     "The page's only artefact is a deployment architecture diagram: it shows components "
     "(database, connection pool, Elasticsearch storage, REST APIs, two Living Applications) "
     "and data flow between them, not a process. Quoted from the page: \"Bonita Intelligent "
     "Continuous Improvement (BICI) extracts data of the Bonita Database, transforms it, and "
     "stores documents in an Elasticsearch storage engine.\" The page carries no AI mention at "
     "all, so this is not a case for E2 - the dismissal rests on the notation.", None, None,
     None, False)
_add(D + "/labs/latest/bici/monitoring", "EXCLUDE", "E1-not-bpmn", "monitoring dashboards",
     "monitoring_home_on_time.png, monitoring_case_execution_details.png, "
     "monitoring_analytics_case_indicators.png, monitoring_analytics_task_indicators.png",
     "figures looked at: dashboard tiles, tables, a pie chart and bar charts",
     "The page's artefact is a monitoring dashboard, not a diagram: tiles, tables, a pie chart "
     "and bar charts of case and task indicators. The AI is a product feature applied to the "
     "dashboards - quoted: \"The artificial intelligence algorithm applies a prediction to each "
     "case: its likelihood to finish within the target duration\" - i.e. a prediction column on "
     "the dashboard, not an AI element inside a process model. Quoted: \"BICI LA Monitoring\".",
     None, None, None, True)
_add(D + "/labs/latest/bici/overview", "EXCLUDE", "E0-no-artefact", None,
     "bici_logo.png, bici_project_name.png",
     "figures looked at: two logos/wordmarks", NO_ARTEFACT_AI % (
         "two logos (the Bonita ICI logo and the project wordmark), no diagram",
         "This Lab project is a proof-of-concept that validates the value of artificial "
         "intelligence (AI) in the field of operations management"), None, None, None, True)
for _u in ("/labs/latest/bpi/dashboards/", "/labs/latest/bpi/dashboards/process-compare",
           "/labs/latest/bpi/dashboards/process-overview",
           "/labs/latest/bpi/dashboards/process-user-insights"):
    _add(D + _u, "EXCLUDE", "E1-not-bpmn", "Business Process Intelligence dashboards",
         "process-overview.png, process-variant.png, process-user-insights.png, process-compare.png, cases.png",
         "figures looked at: donut charts, case-trend charts and tables of variants and cases",
         NOT_BPMN % (
             "process-variant.png",
             "a dashboard table of process variants (cases with objectives failed, duration "
             "stats, flow nodes per case) - and process-overview.png is a donut chart over a "
             "case-trend chart over a table; neither has pools, lanes, events or flows",
             "Process compare dashboard"), None, None, None, True)
_add(D + "/labs/latest/bpi/spo", "EXCLUDE", "E1-not-bpmn", "BPI product card / settings screens",
     "card-spo.png, import-page.png, configure-email.gif",
     "figures looked at: a product card with a \"Generate Smart Process Overview\" button, an "
     "import modal and an email-settings panel",
     "The AI feature (Smart Process Overview) appears as a *button on a product card* and in "
     "the prose - \"Smart Process Overview (SPO) harnesses the power of AI to provide a concise "
     "yet insightful summary of your process execution\" - while the page's artefacts are a "
     "product card and settings panels, and the dashboard pages it belongs to are tables and "
     "charts. No BPMN diagram, so nothing with an AI element inside a process. Quoted: "
     "\"Generate Smart Process Overview\".", None, None, None, True)

# --- Process Designer -------------------------------------------------------------------------
_PD = D + "/process-designer/latest"
_PD_E2 = (
    "", "/", "/getting-started/generate-a-diagram-with-ai", "/getting-started/interface-overview",
    "/release-notes", "/user-guide/ai-generation", "/user-guide/bpmn-elements",
    "/user-guide/diagram-versioning", "/user-guide/editing-diagrams", "/user-guide/managing-diagrams",
    "/how-tos/generate-a-process-from-text",
)
for _p in _PD_E2[1:]:
    _add(_PD + _p, "EXCLUDE", "E2-no-ai-element", "Process Designer BPMN canvas",
         "editor-overview.png / ai-generation-dialog.png / home-dashboard.png (BPMN thumbnail)",
         "figures looked at in the contact sheets and zoomed where needed "
         "(home-dashboard.png zoomed to 1440x900: its \"Employee Onboarding Process\" card holds "
         "a BPMN diagram thumbnail: Start -> Process Task -> End plus an Approve task)",
         DESIGN_TIME % "You work entirely in your browser: build diagrams on a drag-and-drop "
         "canvas, generate a first draft from a plain-language description using AI",
         None, None,
         "You work entirely in your browser: build diagrams on a drag-and-drop canvas, generate "
         "a first draft from a plain-language description using AI", False)
_PD_E0 = (
    "/administration/administration", "/administration/ai-quota", "/administration/application-settings",
    "/administration/license-management", "/administration/logging", "/administration/manage-labels",
    "/administration/permissions-and-roles", "/administration/user-management", "/faq",
    "/get-support", "/getting-started/create-your-first-diagram", "/getting-started/getting-started",
    "/how-tos/how-tos", "/installation/configuration", "/installation/docker-installation",
    "/installation/first-time-setup", "/installation/installation", "/user-guide/export-and-import",
    "/user-guide/process-simulation", "/user-guide/user-guide",
)
for _p in _PD_E0:
    _add(_PD + _p, "EXCLUDE", "E0-no-artefact", None,
         "admin-panel.png / login.png / create-user-dialog.png / no figures",
         "figures looked at where present: administration panels, sign-in page and dialogs",
         NO_ARTEFACT % (
             "administration and sign-in screens (the administration panel, group and user lists, "
             "quota and settings dialogs, the sign-in page) or the page has no figures at all",
             "manage roles and permissions, users, groups, application settings, AI quota"),
         None, None, None, False)

# --- test toolkit / UI builder ----------------------------------------------------------------
_add(D + "/test-toolkit/latest/quick-start", "EXCLUDE", "E2-no-ai-element",
     "BPMN diagram (quick-start-process.png) plus a report screenshot",
     "quick-start-process.png, quick-start-report.png",
     "figures looked at: a pool with a start event, tasks, a gateway and end events - and a "
     "report screenshot containing the same diagram as a thumbnail",
     STUDIO % ("quick-start-process.png (alt \"Quick start process example\")",
               "Test your process with the Bonita Test Toolkit"), None, None, None, True)
_add(D + "/ui-builder/latest/development/configure-static-app-urls", "EXCLUDE", "E0-no-artefact",
     None, "configure-app-static-url.png, configure-page-static-url.png",
     "figures looked at: UI Builder settings panels",
     NO_ARTEFACT % ("UI Builder settings panels, not diagrams",
                    "you will be prompted to choose a different one"), None, None, None, True)
_add(D + "/ui-builder/latest/getting-started/interact-with-your-bonita-process", "EXCLUDE",
     "E0-no-artefact", None, "get-process.gif, bind-data.gif, test-instantiate.gif",
     "figures looked at: UI Builder process-list, data-binding and instantiation screens",
     NO_ARTEFACT % ("UI Builder screens with a process *list*, not a process diagram",
                    "get-process"), None, None, None, True)
_add(D + "/ui-builder/latest/how-tos/how-to-handle-document", "EXCLUDE", "E0-no-artefact", None,
     "file-picker-setting.png", "figure looked at: a UI Builder file-picker settings panel",
     NO_ARTEFACT % ("a UI Builder settings panel", "a download prompt will appear"), None, None,
     None, True)
_add(D + "/ui-builder/latest/release-notes", "EXCLUDE", "E0-no-artefact", None,
     "uib-help-section-release-date.png", "figure looked at: a help-panel screenshot",
     NO_ARTEFACT % ("a help-panel screenshot with a release date", "X-Bonita-Client-Ip"),
     None, None, None, True)

# ================= www.ofelia.com (the marketing site) =======================================
# The 132 judged site pages are generated by `_bonita_sitegen.py` from its MAP of page ->
# (exclusion code | record stem). Their rulings, duplicates and record stems are merged in
# here so the build sees one RULINGS table for the whole source. The 5 UNCERTAIN site pages
# (012-016) are the reason the merge is not just "add 127 exclusions": those rows carry a
# question and evidence read from the corpus record, exactly like the nine docs rows.
import _bonita_site_rulings as _site  # noqa: E402

_dup = set(RULINGS) & set(_site.SITE_RULINGS)
assert not _dup, "docs/site URL collision: %s" % sorted(_dup)
RULINGS.update(_site.SITE_RULINGS)
DUPLICATE_OF.update(_site.SITE_DUPLICATE_OF)
RECORDS_WRITTEN += [s for s in _site.SITE_RECORDS_WRITTEN if s not in RECORDS_WRITTEN]

# ================= calibration re-codings =====================================================
# Found by the calibration pass over the *mechanically* excluded pages (_bonita_audit.py sample 7:
# every 7th mechanical page that has figures or an AI/proc token, 63 pages / 126 figures, looked
# at in a contact sheet). Four of those pages carry a figure that is a real diagram but not BPMN,
# so their mechanical E0 ("no artefact at all") was wrong in kind: the artefact is there, it is
# just not BPMN 2.0. They are re-coded E1 with the notation named. All four verdicts are
# unchanged (the corpus wants BPMN + AI, and none of these is BPMN); what changes is the ledger's
# claim about what is on the page.
_add(D + "/bcd/latest/", "EXCLUDE", "E1-not-bpmn",
     "a CI/CD pipeline diagram (bcd_capabilities.png, alt \"Bonita Continuous Delivery "
     "Capabilities\")",
     "bcd_capabilities.png looked at (1004x503): a Living App repository cylinder, then Checkout "
     "Repository -> Build Living App -> Deploy Living App -> Test Living App, with a Bonita "
     "Platform box above",
     "The page's only figure is a deployment-pipeline diagram: boxes and arrows for the build "
     "stages, not BPMN 2.0 - no pools, lanes, events, gateways or sequence flows. Quoted from "
     "the page: \"we are moving to a new deployment mode that no longer relies on the \\\"BCD\\\" "
     "mechanism as you know it\". The page carries no AI mention.", None, None, None, True)
_add(D + "/bonita/latest/bonita-overview/project-structure", "EXCLUDE", "E1-not-bpmn",
     "a radial concept map (bonita-project-elements.png, alt \"bonita project elements\")",
     "bonita-project-elements.png looked at (665x491): one grey \"Bonita Automation Project\" "
     "circle with Processes, Data, Identity Management, Extensions and Living Applications "
     "around it",
     "The page's only figure is an overview graphic of the project's concepts, not a process "
     "model: it has no events, tasks, gateways or sequence flows. The word BPMN appears on the "
     "page only in a table that *describes* the elements of a project - quoted: \"Diagrams BPMN "
     "diagram that describes your business processes\" - which names the notation without "
     "publishing a diagram in it. The page carries no AI mention.", None, None, None, True)
_add(D + "/bonita/latest/data/data-management", "EXCLUDE", "E1-not-bpmn",
     "a GraphQL schema graph (uid_graphql_voyager.png) plus two UI Designer screenshots",
     "uid_graphql_voyager.png looked at (1000x688): the GraphQL Voyager window, a Type list on "
     "the left and linked type boxes (com_company_model_ExpenseReport, ...Line, ...LineQuery) "
     "with their fields on the right",
     "The page's diagram is a data-model graph, and the page itself names the notation: \"we are "
     "using the graphql-voyager tool, which represents a GraphQL\" ... \"A graphical view of the "
     "relationships between business objects (with their attributes) is displayed in a new tab "
     "of your browser.\" A GraphQL schema graph is not BPMN 2.0. The page carries no AI "
     "mention.", None, None, None, False)
_add(D + "/ui-builder/latest/git/resolve-merge-conflicts", "EXCLUDE", "E1-not-bpmn",
     "two Git diagrams (seperate-conflicts-git.png, alt \"seperate conflicts git\"; "
     "remote-conflicts.png, alt \"remote conflicts\")",
     "both looked at: seperate-conflicts-git.png (1326x458) draws a Staging branch and a Feature "
     "branch as chains of commits converging on a \"Merge Conflict\" marker; "
     "remote-conflicts.png draws remote and local branch boxes with two developers and a "
     "conflict marker",
     "The page's figures are version-control diagrams - commit chains, branch lines and merge "
     "conflict markers - not BPMN 2.0. Quoted from the page: \"Resolving these conflicts is "
     "necessary to merge branches successfully.\" The page carries no AI mention.", None, None,
     None, True)

# ================= tuple-shape repair =========================================================
# Fifteen rows above were written one argument short, so their trailing `judgment` flag landed in
# the `evidence` slot and their `note` was left empty. `_bonita_shape_fix.py` restates them in the
# full shape and documents what each one rests on. Nothing about the verdicts changes.
import _bonita_shape_fix as _shape  # noqa: E402

_RESHAPED = _shape.apply(RULINGS, D)
assert _RESHAPED == 15, "expected 15 reshaped rows, got %d" % _RESHAPED
