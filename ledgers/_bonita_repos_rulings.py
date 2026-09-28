#!/usr/bin/env python3
"""The repository group of the bonitasoft census (worker elicitation-6f).

The docs pages of the portal link to github.com/bonitasoft/* repositories. Those repositories
are where the vendor publishes *example processes that use an AI connector* - the artefact class
the assignment asks for - so they are a second, finite population group: one row per linked
repository, plus one row per `.bpmn`/`.proc` file found in one of them (see
ledgers/_bonita_repos.py for the enumeration and ledgers/_bonita_repos_screen.py for the fetch
and screen of every documentation file those repositories publish).

What this module holds is the class of each repository, established by reading its documentation:

  * `component`    - a connector / archetype / application / client repository: its documentation
                     is build steps, Maven coordinates and connector parameter tables. No process
                     artefact, no diagram, no figure but badges and logos.
  * `fork`         - a vendor fork of a third-party project (angular.js); no artefact.
  * `docs-source`  - the AsciiDoc sources of a documentation component whose rendered pages are
                     already rows of this same ledger (the portal rows); the repository adds no
                     diagram of its own.
  * `ai-connector` - a repository that ships an AI connector. Its documentation is connector
                     configuration; the example processes it ships are `.proc` files, enumerated
                     and ruled as their own rows (010, 011).
  * `bpmn-example` - a repository whose README publishes a real BPMN 2.0 diagram (bonita-examples:
                     the Loan Request process). Ruled E2: BPMN, no AI element inside it.
  * `labs-doc`     - the sources of the Labs documentation: its figures (bici_architecture, the
                     BPI dashboards) are the same files the portal rows already publish.

`CLASS` is the class per repository; `SPECIAL` carries the four repos whose verdict is not the
mechanical one, with their evidence; `PROCESS_FILES` carries the two AI demo processes.

A repository whose tree the public GitHub API would not return (404 = private or renamed, or a
`.git`-suffixed duplicate of a repository already counted) becomes a BLOCKED row and an entry in
notes/elicitation/sources/OPERATOR-TODO.md - never a silent gap.
"""
SPECIAL = {
    "bonita-examples": (
        "EXCLUDE", "E2-no-ai-element", "BPMN 2.0",
        "BPMN diagram (loan-request-diagram.png) - the Loan Request process the example "
        "application runs",
        "loan-request-diagram.png looked at in full (1259x408), fetched from the README that "
        "embeds it",
        "The repository's README publishes a real BPMN 2.0 diagram. Quoted from it: "
        "\"![Loan Request process diagram](loan-request-diagram.png)\". The figure is a Bonita "
        "Studio pool \"Loan Request\" with the lanes \"Requester\" and \"Validator\", a start "
        "event \"Start request\", the user tasks \"Review request\" and \"Sign contract\", an "
        "exclusive gateway \"isAccepted\", a service task \"Notify rejection\" and the end events "
        "\"Accepted\" / \"Rejected\". It carries no AI/LLM element inside the process: the "
        "README says of the one automatic task that \"this auto-task should have a connector on "
        "it, to notify the rejection (through email connector, for example)\" - an email "
        "connector, not an AI one - and the word AI appears nowhere in the repository's "
        "documentation.",
        False,
        "![Loan Request process diagram](loan-request-diagram.png)"),
    "bonita-labs-doc": (
        "EXCLUDE", "E1-not-bpmn", "an architecture box diagram and product-UI dashboards",
        "bici_architecture.png (an architecture box diagram) and the BPI dashboard screenshots "
        "(dashboards/process-overview.png, process-variant.png, process-compare.png, "
        "process-user-insights.png, cases.png, application-insights.png)",
        "bici_architecture.png looked at in full (910x551); the dashboards are the figures of "
        "the Labs portal pages already ruled in this ledger",
        "The repository is the AsciiDoc source of the Labs documentation, and the figures it "
        "publishes are the same files the portal rows of this ledger already carry. Quoted from "
        "its bici/architecture page: \"Bonita Intelligent Continuous Improvement (BICI) "
        "extracts data of the Bonita Database, transforms it, and stores documents in an "
        "Elasticsearch storage engine.\" The one diagram-shaped figure is an architecture box "
        "diagram - boxes \"Bonita Database\", \"BPM Engine\", \"REST API\", \"BICI REST API "
        "Ext.\", \"BICI Living Applications\", \"BICI Add-on\", \"Data Polling\", \"BICI API\" "
        "and \"Prediction model on reaching a goal\", with cylinders for the database and the "
        "storage engine and labelled arrows - not BPMN 2.0: no pools, lanes, events, gateways "
        "or sequence flows. The rest are BPI dashboard screenshots, i.e. product UI.",
        False,
        "Bonita Intelligent Continuous Improvement (BICI) extracts data of the Bonita Database, "
        "transforms it, and stores documents in an Elasticsearch storage engine."),
}

# The one repository whose documentation is a process artefact class of its own was looked at by
# eye; everywhere else the repository's own documentation (fetched and screened) settles it.
CLASS = {
    "angular.js": "fork",
    "bonita-connector-ai": "ai-connector",
    "bonita-connector-ai-agent": "ai-connector",
    "bonita-connector-mistral-ocr": "ai-connector",
    "bonita-examples": "bpmn-example",
    "bonita-labs-doc": "labs-doc",
    "bonita-cloud-doc": "docs-source",
}

CLASS_TEXT = {
    "component": (
        "The repository is a {kind} repository, and its documentation publishes no process "
        "artefact: no `.bpmn` or `.proc` file is in the tree (checked through the public GitHub "
        "API), no documentation file embeds a Mermaid, PlantUML or BPMN diagram, and the only "
        "images it references are badges and logos. Quoted from its README: \"{quote}\"."
    ),
    "fork": (
        "The repository is a vendor fork of a third-party project, not a process example: no "
        "`.bpmn` or `.proc` file is in the tree and its documentation references no diagram. "
        "Quoted from its README: \"{quote}\"."
    ),
    "docs-source": (
        "The repository holds the AsciiDoc sources of a documentation component whose rendered "
        "pages are already rows of this same ledger (the portal rows): its figures are the same "
        "files those rows carry and it publishes no `.bpmn` or `.proc` file of its own. Quoted "
        "from its README: \"{quote}\"."
    ),
    "ai-connector": (
        "The repository ships an AI connector, but its documentation publishes no process "
        "artefact: the README is connector configuration and parameters, it embeds no diagram, "
        "and the example processes the project ships are `.proc` files, enumerated and ruled as "
        "their own rows. Quoted from its README: \"{quote}\"."
    ),
}

# The two AI demo processes bonita-connector-ai publishes (its connector test resources). Both are
# Bonita `.proc` files, i.e. BPMN 2.0 XML with the vendor's extension namespaces.
PROCESS_FILES = {
    # (record stem, note, question, verdict). Both carry an AI connector on a service task, which
    # the census protocol puts deliberately in scope ("diagrams where the AI element is only visible
    # as a task *property* or implementation binding, not as a distinct BPMN element type",
    # prompts/02_source-census.md) - so both are INCLUDE, and the question field is kept only as a
    # record of what was asked before the orchestrator's ruling settled it.
    "bonita-connector-ai-anthropic/src/test/resources/AnthropicAIDemo-1.0.proc": (
        "010_anthropic-ai-demo-proc",
        "The repository ships the process as a Bonita `.proc` file, i.e. BPMN 2.0 XML: "
        "`<process:MainProcess xmi:id=\"_AiDemoMp01\" name=\"AnthropicAIDemo\" "
        "bonitaModelVersion=\"9\">` with a pool \"Anthropic AI Demo\", a lane \"Employee lane\", "
        "a start event \"Start\", the service task \"Ask Claude\", the connector \"Anthropic "
        "Ask\" (`definitionId=\"anthropic-ask\"`, `event=\"ON_ENTER\"`) and its parameters "
        "\"userPrompt\" = \"What is the capital of France? Answer with just the city name.\" and "
        "\"systemPrompt\" = \"You are a helpful assistant.\"",
        "The file is a test resource of the Anthropic connector module, so it is a worked "
        "example rather than a product artefact: does an AI connector demo process shipped in a "
        "connector repository count as a corpus item, or as binding evidence only?",
        "INCLUDE"),
    "bonita-connector-ai-azure/src/test/resources/AzureOpenAIDemo-1.0.proc": (
        "011_azure-openai-demo-proc",
        "The repository ships the process as a Bonita `.proc` file, i.e. BPMN 2.0 XML, the "
        "Azure OpenAI twin of the Anthropic demo: a pool with a lane, a start event, a service "
        "task carrying an AI connector and its prompt parameters - and, unlike the Anthropic "
        "demo, a user task \"Review Results\" after the AI step, i.e. the human review the "
        "protocol asks not to abstract away. Captured from the same repository, one row per "
        "process file.",
        "Same question as the Anthropic demo process: is an AI connector demo `.proc` shipped "
        "as a connector test resource a corpus item in its own right, or binding evidence?",
        "INCLUDE"),
}
