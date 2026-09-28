# Candidate vendors and sources: decision table (Pass 1)

Application of the four inclusion criteria of `chapters/thesis/004_method.tex`,
Section `sec:method:vendor_sampling`, to every vendor/source considered, including the
ones ruled `OUT`. The `OUT` rows are part of the record: the thesis must report the
*application* of the sampling frame, and the researcher must be able to audit rejections.

**Date of application:** 2026-09-22, continued 2026-09-24. **Agent:** Claude (Opus) via Claude Code.
**Search record:** `search-protocol.md`. **Work orders:** `assignments/<slug>.md`.

## How to read the verdicts

- `QUALIFIES` - all four criteria satisfied on positive evidence.
- `UNCLEAR-NEEDS-RULING` - C2 and C3 are satisfied (or at least not failed on positive
  evidence), but C1 or C4 is `NO`/`UNCLEAR`. C1 and C4 are judgement calls that Pass 1 is
  not authorised to settle alone. These sources still get an assignment file with
  `provisional: true`, and a question in `OPERATOR-TODO.md`.
- `OUT` - only ever on positive evidence under C2 (the notation actually used is named) or
  C3 (paywall / sales gate / NDA shown, with no public equivalent).
- `PENDING-VERIFICATION` - **not a verdict.** The vendor was surfaced by a logged channel
  and looks promising, but no page was opened, so under the evidence rule no criterion can
  be scored. `?` in a criterion column means exactly that: unscored, not `UNCLEAR`.
  These rows deliberately have **no assignment file** - writing one would imply a recon pass
  that did not happen. Resolving them is the first action of any continuation.
- Access tiers: `public` | `free-account` | `paid-trial` | `blocked`. A free account is
  **not** a C3 failure; it is an access tier and a ruling for the researcher.

## Gate 1 outcome (operator rulings, 2026-09-24)

After the operator worked through `WORKLIST.md`, the 53 rows stand at:

| Outcome | n | Rows |
|---|---|---|
| QUALIFIES (to Pass 2) | 26 | 13 on positive evidence (Appian ruled out in Pass 2); 11 via the general C4 rule (B5–B7); IBM watsonx and Oracle via B3 |
| OUT (C1) | 16 | Signavio, ADONIS, Nintex, Celonis, Apache KIE, Operaton, Activiti, GBTEC, ARIS, iGrafx, OpenText, TIBCO, Comidor, Visual Paradigm, Cardanit, Modelio |
| OUT (C2) | 8 | Salesforce, ServiceNow, Pipefy, Kissflow, Power Automate (Pass 1 evidence); Pega, AgilePoint (operator canvas check); Appian (operator ruling 2026-09-25, during Pass 2: "too proprietary") |
| OUT (C4) | 1 | Imixs (operator checked: no second search channel) |
| OUT (scope, B4) | 1 | Miragon (Step 1 restricted to vendor sources) |
| WITHDRAWN | 1 | "Berger BPM" |

Rulings applied: B0 (a free account counts as C3), general C4 rule, B3 (process-to-agent
substitution counts as C1), B4 (vendors only), B9–B12, B14. The `C1` exclusions all rest on
the operator's rulings, not on Pass 1 verdicts. The per-row evidence below is unchanged.

## Decision table

| # | Source | Entry URL | C1 promotes AI-in-BPMN | C2 native BPMN 2.0 | C3 public | C4 enterprise presence | Verdict | Access | Population type | Size est. |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Camunda 8 (docs + blog) | https://docs.camunda.io/docs/components/agentic-orchestration/ai-agents/ | YES | YES | YES | YES | QUALIFIES | public | enumerable | ~60 AI-tagged posts + docs section |
| 2 | Camunda Marketplace | https://marketplace.camunda.com/listing | YES | YES | YES | YES | QUALIFIES | public | enumerable | 254 listings |
| 3 | UiPath Marketplace | https://marketplace.uipath.com/sitemap | YES | YES | YES | YES | QUALIFIES | public (listing pages) / free-account (Studio Web inspection) | enumerable | 2326 listings; 86 accelerators; 76 agent catalogue |
| 4 | UiPath Maestro (product docs) | https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/how-to-complex-process | YES | YES | YES | YES | QUALIFIES | public | enumerable | docs tree, ~40-60 BPMN pages |
| 5 | FireStart | https://www.firestart.com/en/ai-workflows | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | 28 AI use cases + 85 blog posts |
| 6 | IFS Cloud (techdocs) | https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/050_business_process_modeling/070_ifs_ai/ | YES | YES | YES | YES | QUALIFIES | public (JS bot challenge, ~10 s) | enumerable | BPA docs subtree, ~30-50 pages |
| 7 | Frends | https://docs.frends.com/frends-development/agentic-ai/intelligent-ai-connector | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | 976-line `llms.txt` docs index |
| 8 | IBM BAMOE | https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview | YES | YES | YES | YES | QUALIFIES | public | enumerable | "Integrating with AI" docs section + IBM Community posts |
| 9 | IBM Developer / watsonx Orchestrate | https://developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/ | UNCLEAR | YES | YES | YES | QUALIFIES (C1 via B3, operator 2026-09-24) | public | enumerable | tutorial index filtered by BPMN |
| 10 | Flowable | https://documentation.flowable.com/latest/reactmodel/bpmn/reference/ai-agent | YES | YES | YES | YES | QUALIFIES | public | enumerable | ~80 (BPMN reference + AI section + blog) |
| 11 | Bizagi | https://help.bizagi.com/platform/en/index.html?ai_agents_form_actions_sentiment_analysis.htm | YES | YES | YES | YES | QUALIFIES | public | enumerable | AI Hub docs branch, ~15 pages |
| 12 | Trisotech | https://www.trisotech.com/bpmn-user-tasks-for-humans-and-ai-agents/ | YES | YES | YES | YES | QUALIFIES | public | enumerable | 743 content pages (1625 sitemap entries, 882 release notes) |
| 13 | Scheer PAS | https://doc.scheer-pas.com/academy/latest/step-3-integrating-the-agent-to-the-process | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | AI tutorials + Designer "Using AI Agents", ~30 |
| 14 | ProcessMaker (now part of Decisions) | https://docs.processmaker.com/docs/add-a-genie-in-a-process | YES | YES | YES | YES | QUALIFIES | public | enumerable | docs Designer tree (FlowGenie, RAG, AI), ~40 |
| 15 | Bonitasoft (rebranded Ofelia) | https://documentation.ofelia.com/bonita/latest/process/ai-connector | YES | YES | YES | YES | QUALIFIES | public | enumerable | Bonita docs (AI connectors, process, getting-started) + ofelia.com product pages, ~35 |
| 16 | SAP Signavio | https://www.signavio.com/highlights/ai-agent-excellence/ | NO (agents governed, not hosted) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | ~30 (highlights + BPMN insights) |
| 17 | CIB seven | https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/ | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | docs manual + examples/tutorials section |
| 18 | FlowX.AI | https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | `ai-platform/using-agents` docs branch |
| 19 | LoyJoy | https://docs.loyjoy.com/bpmn/subprocesses/ai_agent/ | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | `docs.loyjoy.com/bpmn/` module tree |
| 20 | BOC Group (ADONIS) | https://www.boc-group.com/en/blog/bpm/how-adonis-elevates-ai-powered-bpm/ | NO (design-time only) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | blog + docs portal |
| 21 | Appian | https://docs.appian.com/suite/help/26.8/use-agents-in-a-process.html | YES | YES | YES | YES | OUT (C2), operator 2026-09-25 | public | enumerable | AI Agents docs branch, ~25 pages |
| 22 | Nintex | https://www.nintex.com/blog/technical-teams-document-complex-processes-with-bpmn/ | UNCLEAR | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | blog + Process Manager docs |
| 23 | Pegasystems | https://docs.pega.com/bundle/ai-pega/page/platform/gen-ai/agent-steps.html | YES | UNCLEAR (leans NO: Case Lifecycle stages/steps; BPMN import-only) | YES | YES | **OUT (C2)** (operator 2026-09-24) | public | enumerable | not established |
| 24 | Salesforce Flow (Flow Builder) | https://help.salesforce.com/s/articleView?id=platform.flow_ref_connectors.htm&type=5 | not scored | **NO** (Salesforce Flow Builder element/connector notation) | YES | YES | **OUT (C2)** | public | - | - |
| 25 | ServiceNow (Workflow Studio / Flow Designer) | https://www.servicenow.com/docs/r/build-workflows/workflow-studio/flow-logic.html | not scored | **NO** (trigger + action list + "flow logic" blocks) | YES | YES | **OUT (C2)** | public | - | - |
| 26 | Pipefy | https://help.pipefy.com/en/articles/614606-what-are-pipes | not scored | **NO** (pipe = kanban phases + cards) | YES | YES | **OUT (C2)** | public | - | - |
| 27 | Kissflow | https://kfdocs.kissflow.com/help/docs/reference/glossary/process | not scored | **NO** (sequential approval steps + parallel branches) | YES | YES | **OUT (C2)** | public | - | - |
| 28 | Microsoft Power Automate (cloud flows) | https://learn.microsoft.com/en-us/power-automate/flows-designer | not scored | **NO** (trigger/action cards; BPMN bridge deprecated 2026-07-14) | YES | YES | **OUT (C2)** | public | - | - |
| 29 | Celonis (Process Management, ex-Symbio) | https://www.celonis.com/platform/process-management | UNCLEAR ("AI-insertion points") | YES | PARTIAL (docs.celonis.com login-walled; developer portal public) | YES | **OUT (C1)** (operator 2026-09-24) | public / blocked (docs) | enumerable (developer portal) | not established |
| 30 | Aletyx (Kogito AI add-ons) | https://github.com/aletyx/aletyx-kogito-ai-addons/blob/main/README.md | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | GitHub repo + aletyx.ai resources, ~25 |
| 31 | Apache KIE upstream (jBPM / Kogito / Drools) | https://kie.apache.org/docs/10.2.x/drools/drools/pragmatic-ai/index.html | NO-leaning (ML in DMN/Drools, not BPMN) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | docs; expected yield ~0 |
| 32 | Operaton (Camunda 7 fork) | https://operaton.org/ | NO-leaning (MCP engine management only) | YES | YES | UNCLEAR | **OUT (C1)** (operator 2026-09-24) | public | enumerable | docs + blog; expected yield ~0 |
| 33 | Activiti (Alfresco / Hyland) | https://connect.hyland.com/t5/alfresco-forum/bringing-alfresco-content-and-workflows-into-the-ai-era-help-us/td-p/499497 | NO-leaning (no vendor AI-in-BPMN material found) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield ~0 |
| 34 | Imixs-Workflow (Imixs-AI, Open-BPMN) | https://blog.imixs.org/2026/01/17/ai-agents-vs-ai-augmented-workflows/ | YES | YES | YES | UNCLEAR | **OUT (C4)** (operator 2026-09-24, no 2nd channel) | public | enumerable | blog AI category + Imixs-AI docs, ~20 |
| 35 | GBTEC (BIC Process Design / Work Orchestrator, "Arty") | https://www.gbtec.com/company/news-article/arty-ai-enhanced-process-transformation/ | UNCLEAR (Arty design-time; "agentic automation" vague) | YES (Process Design) / ? (Work Orchestrator) | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | not established |
| 36 | Software AG / ARIS | https://aris.com/aris-ai-companion/ | NO-leaning (design-time + mining; BPM as AI governance) | YES (not quoted) | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield ~0 |
| 37 | iGrafx (Process360 Live, "Pia") | https://www.igrafx.com/pia-process-intelligence-assistant/ | NO-leaning (design-time: Pia generates BPMN) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield ~0 |
| 38 | Newgen (NewgenONE) | https://newgensoft.com/platform/process-automation/process-modeling/ | YES (marketing-level) | YES ("abstract and BPMN views") | YES (marketing) / ? (docs) | YES | QUALIFIES | public | not established | not established |
| 39 | Oracle (OIC Process Automation) | https://blogs.oracle.com/integration/the-future-of-oic-process-automation | UNCLEAR (agent-as-step AND BPMN-to-agent decomposition) | YES | YES | YES | QUALIFIES (C1 via B3, operator 2026-09-24) | public | enumerable | OIC blog + OPA docs, not established |
| 40 | OpenText (Process Automation, ex-AppWorks) | https://www.opentext.com/products/process-automation | NO-leaning (Developer Aviator = AI-assisted development) | ? (not quoted) | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | not established | expected yield ~0 |
| 41 | TIBCO (ActiveMatrix BPM / BusinessEvents) | https://docs.tibco.com/pub/amx-bpm/4.3.0/doc/html/bpmhelp/GUID-18D8D888-FCAE-417C-9682-32ADD11EBBAD.html | NO-leaning (no AI material in sweep) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield ~0 |
| 42 | Creatio | https://academy.creatio.com/guides/no-code-customization/bpm-tools/process-elements-reference/system-actions/call-creatio-ai-element | YES | YES | YES | YES | QUALIFIES | public | enumerable | Academy process-elements reference + AI section, ~30 |
| 43 | AgilePoint NX | https://documentation.agilepoint.com/1000/appbuilder/cloudenvShapeN8nInvokeAgent.html | YES | UNCLEAR ("optional set of properties for the BPMN standard") | YES | YES | **OUT (C2)** (operator 2026-09-24) | public | enumerable | AI activities in docs, ~15 |
| 44 | Comidor | https://www.comidor.com/intelligent-process-automation/ | UNCLEAR (generic AI/ML + BPM claims) | ? (not quoted) | YES | UNCLEAR | **OUT (C1)** (operator 2026-09-24) | public | enumerable | not established |
| 45 | Visual Paradigm | https://www.visual-paradigm.com/features/ai-bpmn-diagram-chatbot/ | NO-leaning (AI BPMN generator, design-time) | YES | YES | YES | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield ~0 |
| 46 | Cardanit | https://www.cardanit.com/blog/ai-bpmn-generator/ | NO-leaning (AI BPMN generator, design-time) | YES | YES | UNCLEAR | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield ~0 |
| 47 | Modelio | https://www.modelio.org/index.htm | NO (no AI material) | YES | YES | UNCLEAR | **OUT (C1)** (operator 2026-09-24) | public | enumerable | expected yield 0 |
| 48 | Miragon (Camunda consultancy) | https://miragon.io/blog/agent-skills-ai-nischen-domaenen-bpmn/ | UNCLEAR (this post design-time; AI-integration portfolio unopened) | YES (Camunda/Zeebe) | YES | UNCLEAR | **OUT (scope, B4)** (operator 2026-09-24) (and B4 scope) | public | enumerable | blog AI category, ~15 |
| 49 | "Berger BPM" | - (not identifiable) | ? | ? | ? | ? | **WITHDRAWN** (operator, 2026-09-24) | - | - | - |
| 50 | QuantumBPM | https://quantumbpm.com/blog/orchestrating-ai-agents-with-bpmn | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | blog (2 posts tagged "AI Agents"), ~10 |
| 51 | Flows for APEX (FlowQuest) | https://flowsforapex.org/latest/ai-service-task/ | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable | docs + flowquest.net posts + GitHub, ~15 |
| 52 | Atamya (Agentic PIM) | https://www.atamya.com/en/agentic-pim/ai-powered-workflows/ | YES | YES | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | not established | not established |
| 53 | Citeck ECOS | https://citeck-ecos.readthedocs.io/en/latest/general/AI_instruments/user_agents.html | YES (thin) | YES (thin) | YES | UNCLEAR | QUALIFIES (C4 via general rule, operator 2026-09-24) | public | enumerable (Read the Docs) | not established |

---

## Verification still open at the time of writing

*Updated 2026-09-24 after the Pass 1 continuation.* Every name below was surfaced by a
logged channel and is a **candidate, not a verdict**. Leaving them here rather than
dropping them is deliberate: an unverified candidate is recoverable, a silently
discarded one is not.

**Named in the method prompt:** all worked except **"Berger BPM"**, which could not be
identified (row 49, OPERATOR-TODO B13). Rows 13–15 and 23 are no longer
`PENDING-VERIFICATION`. There are now **zero** `PENDING-VERIFICATION` rows.

**Yielded by Channel 8 (competitor pages):** all worked (rows 24–29). Five are evidenced
C2 `OUT`s. Celonis turned out to be BPMN (row 29). Decisions is covered under
ProcessMaker (row 14).

**Traps found while probing (for anyone re-running these sweeps):**
- Kissflow and Pipefy both publish extensive BPMN *educational* content ("BPMN - An Ultimate
  Guide…", "What It Is and How to Build a BPMN Diagram"). That is SEO material *about* the
  standard, not a claim that the product uses it. A `site:` sweep reads it as C2 evidence,
  and it is not.
- The "agent" hits on TIBCO and ServiceNow are rule-engine and ITSM concepts, not AI.
- Google's index for docs.pega.com is stale. Several Celonis doc links silently redirect to
  a login.

**Surfaced by the Channel 3 grid, not in the original list, still not opened:**
BPMN Kit, Citeck ECOS, Atamya, ZeaProcess, Dragon1, JointJS, Tallyfy, Flows for APEX
(flowquest.net), Moxo, Lucidflow.ai, ba-copilot.com, MarvelX, QuantumBPM, Entoura,
processcamp.io, justflow.it, yourcompanyos.io, Sapiens Decision, Eraser.io, Lucid,
Microsoft Visio. (CIB seven, FlowX.ai, LoyJoy, BOC and Aletyx from this list have been
worked.) Several are diagramming tools (JointJS, Lucid, Eraser.io, Visio, Dragon1) and are
likely `UNCLEAR (C1 NO)` of the Visual Paradigm kind. QuantumBPM ("Orchestrating AI Agents
with BPMN") and Flows for APEX are the likeliest qualifiers.

**Practitioner / consultancy layer (Channel 6, barely started; depends on B4):**
BP3, codecentric, Incentro, CAP BPM, Miragon (now row 48), holisticon (new, "Agentic AI in
Camunda 8"), growwstacks, NTConsult, Buho Advisors, Five1, Datalaria, PwC (CH and IN),
Kompetenzzentrum KARL, redthunder.blog (Oracle), fintraining.org.ua.

**Academic pointers (Channel 7, not worked):**
`arxiv.org` "Agentic Business Process Management Systems"; BESSER-PEARL/agentic-bpmn;
BPMN Assistant (arXiv/MDPI); BPMN-Chatbot (CEUR); Nala2BPMN; LLM4BPMNGen (TUM);
"Conversational Business Process Modeling using LLMs" (dl.gi.de); "Large Process Models"
(HU Berlin, KI journal). Most of these are AI-generates-the-diagram tools rather than
AI-in-the-process, which makes them C1-relevant only if their tool citations lead back to
vendor material.

**Channels not worked at all:** 5 (G2 / Capterra directories), 7 (academic).

---

## Criteria evidence appendix

Verbatim quotes behind each verdict. `QUALIFIES` and `UNCLEAR-NEEDS-RULING` sources also
carry their evidence in their assignment file; it is repeated here so the decision table is
auditable on its own. Rows whose evidence is a search-result title rather than an opened
page are marked **[snippet only]** — those are not yet compliant with the evidence rule and
must be re-grounded before the thesis cites them.

**1 Camunda / 2 Camunda Marketplace** — C1: "The AI Agent connector is the primary Camunda
connector for building AI agents. It integrates an LLM with your BPMN process."
C2: "Camunda activates the corresponding BPMN activity in the ad-hoc sub-process."
C4: blog index lists "Camunda Recognized as a Visionary in Gartner BOAT Magic Quadrant
2026". Marketplace C1: "AI Agents — Implement enterprise-grade agents with governed
planning and memory"; catalogue shows "254 Results" anonymously.

**3 UiPath Marketplace / 4 UiPath Maestro** — C1: `/products/gen-ai` renders
"Agentenkatalog | 76 Ergebnisse" with listings of type "Agent-Vorlage". C2: Maestro docs
image `alt` "BPMN-Diagramm des Rechnungsbearbeitungsprozesses" and prose "Dies ist das
BPMN-Diagramm für den Prozess, den wir erstellen." C3: listing pages public, template
inspection needs a free tenant → `access: free-account`. **Ruling B0 (operator,
2026-09-24): a self-service free account satisfies C3.** UiPath stays `QUALIFIES`.

**5 FireStart** — C1: "AI-Powered Process Automation. Integrate AI seamlessly into your
workflows. OCR, NLP, classification, summaries". C2: "FireStart is built on BPMN 2.0 — the
international ISO standard for business process modeling (ISO 19510)." C4 UNCLEAR: "made in
Austria, hosted in the EU, built for DACH enterprises" → ruling B1.

**6 IFS Cloud** — C1: "The IFS AI Task is a purpose-built enhancement introduced for IFS
Workflows, enabling seamless integration of IFS Industrial AI use cases which support
LLMs". C2: "a collection of detailed guides teaching the reader the various intricacies of
BPMN and our extensions to BPMN."

**7 Frends** — C1: "In Frends, AI can be included in the Processes natively using
Intelligent AI Connector". C2: "BPMN 2.0 with AI Connector enables AI Orchestrations."
C4 UNCLEAR → ruling B2.

**8 IBM BAMOE** — C1/C2: "The AI Agent task (technology preview) in the BPMN Editor,
powered by Langflow, allows you to add AI Agents in the BPMN Workflows"; "Drag and drop the
AI Agent node from the palette."

**9 IBM Developer / watsonx** — C1 UNCLEAR: "using Bob skills to transform BPMN process
models into SOP-driven, fully tested, and deployable watsonx Orchestrate agents" — the BPMN
model is the input, not the host, of the AI. → ruling B3. C2: a literal `BPMN-order-process.bpmn`
exists in the companion repo **[snippet only — not opened]**.

**10 Flowable** — C1: "The AI Agent Task allows to execute an AI Agent of the type utility,
document, knowledge and external." C2 (placement evidence): that page sits inside the BPMN
element reference between "Adhoc Subprocess" and "Audit" — a first-class BPMN element.

**11 Bizagi** — C1: "With the Execute AI Agents in Form Actions feature, you can make use of
AI Agents in a Form in a running process." Nav also carries "Execute AI Agents from Activity
Actions" (the stronger, process-bound case) **[snippet only — not opened]**. C2 **[snippet
only]**: `bizagi.com` "BPMN 2.0 - A Standard for BPM platform development"; must be
re-grounded.

**12 Trisotech** — C1: "Modern workflow applications can assign tasks to humans, AI agents,
or AI agents operating under human supervision within the same orchestrated process."
C2: "…while maintaining transparency, governance, and execution control within BPMN
workflows." C4: Mayo Clinic / Dana-Farber / Intermountain case-study pages; the tooling
behind Bruce Silver's BPMN Method and Style.

**13 Scheer PAS: resolved 2026-09-24, UNCLEAR-NEEDS-RULING (C4 only).** The
Pass 1 suspicion was that the AI agents are bound to xUML rather than BPMN. **Both are
true, and the combination is the finding.** From Academy "Step 3: Integrating the Agent to
the Process": "You created the CaseAgent to execute process step Analyze customer request",
then "Click Analyze customer request to open its execution model… drag & drop the agent's
execute operation to the execution model". The figure on that page (1388×832, viewed)
shows a BPMN 2.0 diagram: a start event "Start insurance case auto-processing", a user task
"Enter insurance request", and a task "Analyze customer request". The task's execution
model (an xUML activity) holds the agent operation. The page points readers to "the
chapters Modeling BPMN and Implementing Your Process in the Designer Guide". The AI is
bound to a BPMN task through a separate implementation layer. That is structurally the
**delegated-binding** mode (as in UiPath), not a labelled AI task (as in Camunda). C1 YES,
C2 YES, C3 YES (docs anonymous; a cookie banner is present and was left untouched). **C4
UNCLEAR:** Scheer is an established DACH BPM company, but no customer-base evidence was read.
This falls under the general C4 rule proposed at B5–B7. The AI tutorial states "The AI
agent feature is only available in a Kubernetes setup" and "you need an account with an AI
service provider". Those are product prerequisites, not C3 gates.

**14 ProcessMaker: resolved 2026-09-24, QUALIFIES.** The AI element is a
**dedicated native node type** in the BPMN modeller, the same mode as IBM BAMOE and
Flowable.
- C1: "Add a Genie in a Process" (docs.processmaker.com): "Add a FlowGenie object from one
  of the following locations in Process Modeler"; "If your process has a Pool object, the
  FlowGenie object cannot be placed outside of the Pool". The page also says "Add boundary
  events", and it offers the loop modes "No Loop Mode Loop Multi-instance(Parallel)
  Multi-instance(Sequential)". Those are BPMN activity semantics applied to the AI node.
  "FlowGenie" confirms the node is an LLM call: "extract data using the vision model of
  OpenAI"; "Designers can add and link multiple Genies within their processes."
- C2: "Validate Your Process is BPMN 2.0 Compliant": "Before you deploy your Process model
  to production, ensure that it is BPMN 2.0 compliant".
- C3: docs anonymous. C4: established open-source BPM vendor, now under Decisions.
- Watch-out for Pass 2: "AI Generated Object", "AI Asset Generation" and "Create a Process
  from Text" are **design-time** (E2) pages in the same docs tree.

**15 Bonitasoft: resolved 2026-09-24, QUALIFIES.** The vendor has rebranded:
`bonitasoft.com` links land on `ofelia.com`, and `documentation.bonitasoft.com` redirects
to `documentation.ofelia.com/bonita/`.
- C1: "AI connectors" (Bonita docs): "Bonita AI connectors let you integrate advanced language
  models like OpenAI, Anthropic, Google Gemini, Mistral… into your business processes". Use
  cases: "Generate text content… Classify documents… Extract structured data". The product
  page (ofelia.com/product/bonita-bpm) says: "AI Connectors OpenAI & Mistral native + AI Agent
  Orchestrator" and "Secure LLM integration within deterministic workflows. AI output is
  strictly bounded by business rules".
- C2: "Process Diagram overview": "A process diagram is the representation in the Bonita
  studio of a group of processes (BPMN pools)". Items are added from "the BPMN elements
  menu".
- C3: docs anonymous. C4: a long-standing open-source BPM vendor.
- Promotion mode: Bonita connectors are attached to activities as implementation, so the
  AI is probably **not visible on the diagram**. That is delegated binding, as for UiPath
  and Scheer PAS. For Pass 2, expect `UNCERTAIN` rather than `E2` when a diagram shows plain
  tasks.
- The same product page also sells "Natural language -> BPMN modeling". That is
  design-time (E2).

**16 SAP Signavio**: **[snippet only,
no page opened]** (Signavio since resolved, see below; 14 and 15 are updated further down if resolved). Recorded as candidates, not verdicts. Signavio's AI material is
consistently process-*intelligence* and AI-driven modelling recommendations, which points at
C1 NO, but a `site:` result list is not evidence and no verdict is claimed.

**17 CIB seven** — C1/C2, and an unusually clean statement of the distinction the census
depends on. The page tabulates its two AI features side by side: "AI Agent Connector (this
doc) … **Runtime — executes during a process instance**" versus "Modeler 'BPMN AI Agent' /
wizard … **Design-time — helps you author BPMN**". Also: "Chat memory — keep a multi-turn
conversation across BPMN steps" and a "ProcessStarterTool [that] lets the agent launch a
CIB seven process by key". C4 UNCLEAR: Camunda 7 fork, DACH vendor, enterprise edition, but
no customer-base evidence read.

**18 FlowX.AI** — C1: "Trigger AI agents from BPMN workflow nodes for automated document
processing, decisions, and content generation." C2: "Add a Service Task node to your process
where you want to trigger the agent"; the docs also promise "AI-powered decisions at process
gateways". C4 UNCLEAR: banking-focused vendor, customer names not verified.

**19 LoyJoy** — C1: "The AI Agent module is LoyJoy's new component for building AI-driven
conversational experiences… The agent can operate iteratively, meaning it can call multiple
tools in sequence." C2: the page's own path is `/bpmn/subprocesses/ai_agent/` and it sits
under a "BPMN Modules" tree — the AI Agent is a BPMN sub-process type. C4 UNCLEAR:
conversational-commerce vendor, small.

**20 BOC Group (ADONIS)** — **C1 NO on positive evidence**: "Instead of relying entirely on
manual modelling and analysis, AI can assist by interpreting documentation, generating
initial process drafts, and helping users interact with process knowledge more easily." The
named capabilities are "AI-Assisted Process Modelling", "AI-Supported Process Analysis",
"Smarter Content Discovery" — all **design-time**. No AI element inside a running process
was found. C2 YES (ADONIS is a BPMN 2.0 modelling suite), C3 YES, C4 YES (established EU
BPM vendor). Per the sampling rules a C1 failure alone cannot produce `OUT`, so the verdict
is `UNCLEAR-NEEDS-RULING` and the source keeps a provisional assignment file. **My
recommendation is to exclude it at Gate 1** unless the "Let Your BPM Speak AI with MCP and
ADONIS" material turns out to put an agent inside a process — that page was not opened.

**20 BOC ADONIS: update 2026-09-24.** The MCP page is now opened. All three "Key MCP Use
Cases" (Smart navigator, Process optimizer, AI executor) are external agents consuming the
process repository. **C1 NO confirmed** (OPERATOR-TODO B8).

**16 SAP Signavio: update 2026-09-24.** The one-artefact check (q45) found no BPMN
diagram with an AI agent as lane or performer. Signavio's own agents (February 2026 release:
"Dashboard Analyzer Agent", "Process Content Recommender Agent") are Joule assistants about
the modelling work. The recommendation moves to rule out (OPERATOR-TODO B10).

**21 Appian** — C1: "Integrate your AI agents directly into your business workflows by
calling them from a process model… You can run an AI agent from any process model using the
Execute AI Agent smart service", plus the modelling instruction "drag the Execute AI Agent
smart service from the node palette onto the canvas". C2, from
`docs.appian.com/suite/help/26.8/process_modeling.html`: "Business Process Model Notation
(BPMN) is the standard by which anyone can graphically describe their business processes.
With Appian, that model isn't just the starting point for building your process, it is the
process." **C2 caveat for Pass 2:** the same page also says "Your BPMN standard diagram is
actually the perfect starting place for your Appian process model", which reads as a
*translation* from BPMN into Appian's own node palette. Whether a rendered Appian process
model is BPMN 2.0 notation or an Appian-specific notation is a live `E1-not-bpmn` risk at
artefact level and must be judged per diagram. C3: docs public; note "the capabilities
described on this page are included in Appian's advanced and premium capability tiers" —
that is a **licence** tier, not a documentation paywall, so it is not a C3 failure.

**22 Nintex** — C2 YES: "we are thrilled to introduce the addition of BPMN (business process
model and notation) process modeling capability to Nintex Process Manager" (blog, 9 Nov
2023). C1 UNCLEAR, and for a specific structural reason: the BPMN capability sits in
**Nintex Process Manager**, which is documentation-oriented, while the AI agents are
marketed under **Nintex Automation** ("See how Nintex orchestrates your people, systems,
and AI agents"), a separate, non-BPMN workflow product. The two may never meet in one
artefact. → ruling B9.

**23 Pegasystems** — **unresolved, and blocked rather than judged.** Every
`docs.pega.com` URL in Google's index that was opened returned "ERROR CODE: 404 Page Not
Found — We've been doing some housecleaning", including two different bundle paths for
"Configuring complex Processes" and one for "Introduction to Case Management". Pega's
documentation site has been restructured and the search index is stale, so C2 could not be
established either way. **This is the one row in the table where a genuine `OUT` is
plausible**: Pega's modelling surface is case-life-cycle and flow-shape based, and if it
turns out not to be BPMN 2.0, that is a C2 `OUT` with the notation named — the only kind of
hard rejection the sampling frame allows. It must be resolved from Pega's own on-site
documentation search, not from Google. See tooling gap C1.

**23 Pegasystems: update 2026-09-24, now UNCLEAR-NEEDS-RULING (C2).** Pega's on-site
search froze the renderer (tooling gap C1 still stands). But a fresh `site:docs.pega.com`
sweep returned live pages under the current `/bundle/platform/` and `/bundle/ai-pega/`
paths.
- **C1 YES**: "Agent Steps" (docs.pega.com, `/bundle/ai-pega/…/agent-steps.html`): "Agent
  Steps incorporate AI agents directly into your Case Type workflow. When a Case reaches an
  Agent Step, the assigned Agent performs the defined action in the background". A figure
  captioned "Agent Step in the Case lifecycle" is also present.
- **C2 UNCLEAR, leans NO, and deliberately not recorded as `OUT`.** Three pieces of
  evidence:
  1. BPMN is an **import** format that gets translated away. "Configuring Case Types"
     (Blueprint) says: "You can also create Case Types by uploading BPMN files with your
     existing business processes… click Save and Regenerate Case Lifecycle". The BPMN
     diagram becomes Pega "Stages and Steps".
  2. The detailed modeller uses Pega's own shape vocabulary. From "Assignment shapes in
     Processes" (Pega Platform '26, updated 2 July 2026): "Assignment shapes represent tasks
     that users complete in a Process", created "in Case Lifecycle Designer or by adding one
     of the Assignment shapes to a Process in Process Modeler". Shapes named on the page:
     Assignment, Assignment Service, and a robot-queue assignment. The string "BPMN" does
     not occur on the page.
  3. **Why this is not an `OUT`:** the Assignment shape icon on the page is a rounded green
     rectangle, which could equally be read as a BPMN task. I cannot name a non-BPMN
     notation with confidence. The sampling rules only allow a C2 `OUT` when the notation
     is named, and hesitation resolves upward. The question is for the researcher (B12):
     is Pega's Case Lifecycle / Process Modeler notation "native BPMN 2.0" in the C2 sense?

**16 SAP Signavio** — **C1 NO on positive evidence, and it is a different flavour of NO from
row 20.** From https://www.signavio.com/highlights/ai-agent-excellence/ (2026-09-23), the
four named capabilities are "Identify AI Agent Opportunities", "Design and Build AI Agents",
"Infuse Context into AI Agents", "Control Agentic Execution". The decisive sentence is
"Design and deploy AI agents **using the platform of your choice**" — Signavio explicitly
does **not** host the agent. Its role is to find where agents should go ("help you identify
where exactly in your processes you can gain the most value from leveraging AI agents") and
to govern them afterwards ("Mine AI agent behavior to ensure ongoing compliance").
C2 YES, emphatically: the site's own footer offers a "Free BPMN 2.0 and DMN 1.0 Poster" and
a "BPMN 2.0 Insights" section; Signavio is a BPMN-notation vendor of long standing.
C3 YES, C4 YES (SAP).

**The wrinkle that keeps this at `UNCLEAR` rather than a recommendation to reject:** one
capability line reads "Control your business process execution, carried out by your
employees and AI agents." A process model whose *performers* include AI agents is arguably
AI-in-BPMN at model level — closer to Trisotech's "BPMN user tasks for humans and AI agents"
(row 12, which qualifies) than to ADONIS's design-time assistance (row 20). That single
sentence is the difference between a rejection and an inclusion, and it was not chased to a
concrete artefact. → ruling B10.

**24 Salesforce Flow: OUT under C2** (Pass 1 continuation, 2026-09-24). The notation is
Salesforce's own Flow Builder element-and-connector model, not BPMN 2.0. Evidence from
"Flow Element Connectors" (help.salesforce.com): "A connector determines the path that a
flow takes at run time"; connector types are listed as "Decision outcome label… Identifies
which element to run when the criteria of a Decision element outcome are met", "Wait
configuration label", "Fault", "Loop—For each item", "Go To". The "Flow Builder Tour"
page describes the canvas as "Choose between Auto-Layout or Free-Form" and elements "such as
Create Records or Update Records". Neither page mentions BPMN. Neither page mentions a BPMN
import or export either. Salesforce's AI story is
real ("Einstein and Agentforce for Flow"), so the vendor would pass C1. It fails on
notation alone. **Scope of this OUT:** Flow Builder only. Salesforce Flow Orchestration
("Flow Builder for Flow Orchestration", stages/steps) was listed in the index but not
opened, so it is covered only as a Flow Builder surface.

**25 ServiceNow: OUT under C2** (2026-09-24). Workflow Studio flows are a trigger followed by
an ordered list of actions and "flow logic" blocks. The notation is not BPMN 2.0.
Evidence from "Workflow Studio flow logic" (Australia release, updated 12 March 2026): the
flow-logic palette is "If", "Make a decision", "For Each", "Do the following until", "Do the
following in parallel", "Try", "Wait for a duration", "Go back to", "End Flow". "Make a
decision" is described as "decision table branching logic… as an alternative to nested If,
Else If, or Else flow logic". That is block-structured control flow, not gateways and
sequence flows. The string "BPMN" does not occur anywhere in the rendered page, including
the full navigation tree. **Tooling note:** the page renders inside Fluid Topics shadow
DOM, so `document.body.innerText` returns ~350 characters. The text has to be read by
walking `shadowRoot`s.

**26 Pipefy: OUT under C2** (2026-09-24). A pipe is a column-based kanban process. It is not
BPMN. From "What are pipes" (help.pipefy.com): "Each pipe comprises phases which represent
the steps your team must accomplish"; "Use cards as items to be worked on, like
candidates, purchase orders, or tickets." "BPMN" does not occur on the page. **Trap
(same as Kissflow):** `site:pipefy.com BPMN` returns nine hits, all educational or SEO blog
content ("BPMN: What It Is and How to Build a BPMN Diagram", "Top 7 Business Process
Modeling Tools"). The anchor article was opened. It is content *about* the standard and
makes no claim that the product uses it.

**27 Kissflow: OUT under C2** (2026-09-24). Kissflow's process model is a sequential
approval-step workflow with parallel branches. From the product glossary (kfdocs.kissflow.com):
"A process is a structured workflow for getting tasks done in a specific order. It involves
initiating items within the process and moving them forward to subsequent steps in the
workflow involving approve, reject, withdraw, and reassign functionalities". Also:
"Parallel branches in workflows enable concurrent tasks or conditional routing based on form
data". Neither glossary page mentions BPMN. The BPMN material on `kissflow.com` is
educational SEO content (see the trap noted above). **Confidence note:** the glossary
describes the model in words, but no rendered workflow canvas was inspected. If the
researcher wants a visual confirmation, the Process builder help pages are the place to get
it.

**28 Microsoft Power Automate: OUT under C2** (2026-09-24). Cloud flows are built from
trigger and action **cards** on a canvas. From "Explore the cloud flows designer": "The
action or trigger card that is selected in your flow in the center of the page (the
canvas)". "BPMN" does not appear on the page. **The decisive evidence is a deprecation.**
The one BPMN bridge Microsoft had is being removed. From support.microsoft.com, "Design an
automated workflow in Visio [DEPRECATED]": "Effective July 14, 2026, the ability to map
BPMN shapes to Power Automate triggers and actions and export them as cloud flows will be
removed." Before that date, BPMN was a Visio *import* format translated into cards, never
the execution notation. The deprecation is a small market finding worth a sentence in the
thesis: an automation vendor has dropped its BPMN path during the same period in which
BPMN vendors added AI agents.

**29 Celonis: NOT an OUT. UNCLEAR-NEEDS-RULING** (2026-09-24). Listed above as a likely
C2 rejection because Celonis is known for process mining. **That expectation was wrong.**
- **C2 YES.** Celonis Process Management (the former Symbio modeller) is native BPMN 2.0.
  From developer.celonis.com "BPMN tasks": "The task types that are defined by BPMN are:
  none service send receive … user business role script". The page also maps each type to
  BPMN XML (`<serviceTask> ... </serviceTask>`).
- **C1 UNCLEAR.** From celonis.com/platform/process-management: "Enable strategic process
  management and define guardrails, outcomes, and AI-insertion points". The page also offers
  "generative AI process modeling", which is design-time and would count as E2. "AI-insertion
  points" in a to-be process model is the same wrinkle as Signavio's (row 16), and it was
  not chased to an artefact. A docs page titled "Adding Process Copilot to Process
  Orchestration steps" exists (Google result title) and would probably decide C1. It
  redirects to a login.
- **C3 PARTIAL.** `docs.celonis.com` redirects every page to `celonis.my.site.com/docs/s/login/`
  ("Celonis ID Login"). `developer.celonis.com` and the marketing site are anonymous.
  Whether a Celonis ID is a self-service free account (which would count as public under
  B0) was not established.
- C4 YES (Celonis is a large process-intelligence vendor).
→ ruling B11, blocker A4.

**30 Aletyx: UNCLEAR-NEEDS-RULING (C4)** (2026-09-24). Aletyx is the commercial successor
of the Red Hat jBPM/Kogito team. From the `aletyx-kogito-ai-addons` README (GitHub): "Kogito
add-ons that give BPMN processes first-class access to large-language-model capabilities
(task selection, prompt formulation, structured-output execution, tool calling, and
execution history) without leaking provider details into the process model." The modelling
instruction reads: "From the palette, expand the Custom Tasks → Aletyx AI category and drag
the Ad-hoc Intelligence task inside the ad-hoc subprocess. Add your other (human) tasks
inside the same ad-hoc subprocess. The AI task will orchestrate them." That is the
Camunda-style **AI orchestrating an ad-hoc sub-process** pattern, implemented as a custom
BPMN task (`.wid` work-item definition, display name "Ad-hoc Intelligence", category
"Aletyx AI"). C1 YES, C2 YES, C3 YES (public GitHub). **C4 UNCLEAR:** a small, young
vendor; the lineage is strong but no market-presence evidence was read. It falls under the
general C4 rule (B5–B7).

**31 Apache KIE upstream (jBPM / Kogito / Drools): UNCLEAR-NEEDS-RULING (C1)**
(2026-09-24). The only AI material on the upstream sites (`site:kie.apache.org OR
site:jbpm.org OR site:kie.org`, 10 results) is "Pragmatic AI: Integrating Machine Learning
with Drools": "you can integrate Machine Learning (ML) with Drools by using PMML files with
Decision Model and Notation (DMN) models". That is ML inside **DMN decisions**, not an AI
element in a BPMN process. It is C1 NO-leaning, and it cannot exclude on its own. The
upstream is recorded separately from Aletyx so that the downstream add-ons are not credited
to the Apache project. Recommendation: rule out at Gate 1, and note that the Kogito AI
capability lives in a vendor add-on (row 30), not in the upstream project. The same
DMN-vs-BPMN caveat applies to IBM BAMOE (row 8), whose AI Agent task is BPMN.

**32 Operaton: UNCLEAR-NEEDS-RULING (C1 NO-leaning, C4 UNCLEAR)** (2026-09-24). The home
page (operaton.org) describes a "Community-driven, Free Open-source BPMN Engine… the next
generation in line of Camunda, Activiti". Its only AI claim is "AI-enabled Manage Operaton
engines via MCP". That is AI operating *the engine*, not an AI element in a process.
`/roadmap` has no AI, LLM, agent or MCP mention. A broad Google query ("Operaton BPMN engine
AI OR LLM OR agent") returned Camunda, LoyJoy, codecentric and holisticon content, but no
Operaton AI material. Recommendation: rule out, and recheck in a later round (Camunda 7
forks may add a connector, as CIB seven did).

**33 Activiti: UNCLEAR-NEEDS-RULING (C1 NO-leaning)** (2026-09-24). Two sweeps (q24,
q25) found no vendor AI-in-BPMN material from Alfresco/Hyland. The one AI hit is a
community forum post (Hyland Connect, 17 July 2026) about feeding Alfresco content and
workflow data into RAG pipelines ("securely feeding Enterprise Content and Workflow data
into Vector Databases"). That is AI *about* workflow data, and it is written by a community
member, not the vendor. Recommendation: rule out.

**34 Imixs-Workflow: UNCLEAR-NEEDS-RULING (C4)** (2026-09-24). From "AI Agents vs.
AI-Augmented Workflows" (blog.imixs.org, 17 January 2026): "At Imixs we have already
published the Imixs-AI module, allowing you to integrate LLMs directly into your workflows…
The BPMN model defines which steps are carried out in which order. The LLM is a powerful
tool—but one that is called upon, not one that decides. It is integrated into the process
flow through BPMN annotations." The same post positions Imixs-Workflow as "based on the
BPMN 2.0 standard". The sweep (q26) found a dedicated AI series: "Imixs-AI - LLM Tool Calling"
(Feb 2026), "Introducing new Imixs AI Assistant Adapter" (Oct 2025), "Imixs-AI Version 1.1.0
Released" (Oct 2024), "Revolutionizing Business Process Management with AI" (Jun 2024), and
German "BPM im Zeitalter von KI" (imixs.com). **Possible new promotion mode:** the LLM binding
sits in BPMN *annotations/event configuration* rather than in a dedicated task type. C4
UNCLEAR: a small German open-source vendor. It falls under the general C4 rule.

**35 GBTEC: UNCLEAR-NEEDS-RULING (C1)** (2026-09-24; **replaces the captcha-voided 2026-09-22
sweep**). The re-run (q27) with full vocabulary returned 10 results. The Arty launch release
(9 April 2024) is design-time: "Arty features an AI Modeler® that instantly generates
process models in various notations with a simple command input"; "Arty serves as an AI
Copilot, offering real-time personalized recommendations". One sentence points further: "As
a 'Digital Worker,' Arty will collaborate side by side with process stakeholders ('Human
Workers'), facilitating… automated workflows". The PEX webinar page ("Workflow automation
powered by agentic AI", q28) speaks of "no-code AI and agentic automation" and "Arty, their
AI-powered automation assistant". It is vague on whether AI runs *inside* a Work
Orchestrator process. C2: GBTEC Process Design is a BPMN modeller ("BPMN 2.0 Leitfaden",
"Process modeling with BPMN 2.0" poster, both in the results). Whether **Work Orchestrator**,
the execution product with "Intelligent Document Processing", uses BPMN was not
established. The ruling hinges on one check: is there a Work Orchestrator workflow with an
AI/IDP step, and is it BPMN?

**36 Software AG / ARIS: UNCLEAR-NEEDS-RULING (C1 NO-leaning)** (2026-09-24; replaces the
voided sweep). "ARIS AI Companion" (aris.com): "With the ARIS AI Companion, you can take
your textual descriptions and seamlessly translate them into structured process models".
It also offers "AI-Based Search" and "AI Calculated Fields" in ARIS Process Mining. All of
this is design-time or mining. "BPM in the Age of AI" (aris.com/resources) frames the
role as "Agentic AI: BPM is evolving from an efficiency enabler to a governance framework
for AI and digital workers". That is AI **governed by** process models, not AI in them.
It is the same category as SAP Signavio and BOC ADONIS (see below). C2: ARIS supports
BPMN 2.0 alongside EPC. This is uncontested but **not quoted** from an opened page.
Recommendation: rule out, and add ARIS to the "AI about processes" category note.

**37 iGrafx: UNCLEAR-NEEDS-RULING (C1 NO-leaning)** (2026-09-24; replaces the voided
sweep). "Pia (Process Intelligence Assistant)": "Create fully functional process diagrams in
seconds with simple conversations or document uploads"; "Pia will create a BPMN 2.[0
diagram]"; "Empower employees of all technical skill levels to create process models – no
BPMN knowledge required." This is design-time generation (E2 territory), and it
simultaneously confirms C2. The rest of the 10-result sweep (q30) is process mining,
simulation, and Process360 Live release notes. Recommendation: rule out. It belongs to
the "AI about processes" category.

**38 Newgen: QUALIFIES, on marketing-level evidence** (2026-09-24; replaces the voided
sweep, which had returned 0 on the narrow phrase). "AI-first Process Modeling" page: "Build
orchestration-ready processes that connect AI agents, human teams, and enterprise systems."
The same page offers "Visually design simple to complex process models with both abstract
and BPMN views". The BPM platform page adds: "Orchestrate end-to-end enterprise processes
by unifying AI agents, business rules, human decisions, and enterprise systems". C4 YES
(listed enterprise vendor). **Caveat for Pass 2:** both pages are marketing. No
documentation or concrete artefact was reached, and whether Newgen's product docs are
public is unknown. The first Pass 2 action is to establish the population. If the only
public material is marketing copy without diagrams, the source may yield zero, and that is
a legitimate census result.

**39 Oracle (OIC Process Automation): UNCLEAR-NEEDS-RULING (C1)** (2026-09-24; replaces the
voided sweep). "The future of OIC Process Automation" (blogs.oracle.com, 10 September 2026)
describes both directions at once: "In customer estates today we see two patterns:
deterministic flows, which increasingly invoke an agent as a step, and probabilistic flows,
where the agent holds control. We expect both to converge on one architecture". It also says
agents change "what a process model is: no longer a description of the path, but a
description of the goal". On existing assets: "Most customers reading this have a body of
structured (BPMN) and dynamic (case-style) processes in production… a BPMN diagram always
mixed three concerns in one drawing". The post then gives a worked example: "Take a typical
BPMN model for supplier invoices." C2 YES (OIC Process Automation executes BPMN). The C1
question is the one already raised for IBM watsonx (B3). Agent-as-a-step inside a BPMN
flow is AI-in-BPMN. Decomposing BPMN into an agent architecture is
process-to-agent substitution. Oracle promotes both, so it is closer to qualifying than
IBM watsonx. The worked invoice example is a likely artefact and should be captured whatever
the ruling. → ruling B3 (extended to Oracle).

**40 OpenText: UNCLEAR-NEEDS-RULING (C1 NO-leaning, C2 unquoted)** (2026-09-24; replaces the
voided sweep). The Process Automation product page offers "Developer Aviator for low-code,
AI-assisted development" and "an AI-powered, low-code development platform". That is
design-time AI. The rest of the 10-result sweep (q34) is test automation and ITOM
("Context Insight Agent - ITOM" is an IT-ops agent, not a process element). BPMN does not
appear on the product page. The Workflow Modeler docs (developer.opentext.com) were not
opened. Recommendation: rule out, unless the Workflow Modeler docs show BPMN plus an AI
step.

**41 TIBCO: UNCLEAR-NEEDS-RULING (C1 NO-leaning)** (2026-09-24). C2 YES: the ActiveMatrix
BPM 4.3.0 help says "This release of TIBCO Business Studio… is based on the BPMN Version
2.[0]". C1: the 9-result sweep (q35) contains **no AI material at all**. The "agent" hits
("Adding and Configuring Process Agent Class", "BusinessEvents Process Orchestration") refer
to BusinessEvents inference agents, a rule-engine concept, not AI. That false friend should
be noted for anyone re-running the sweep. ActiveMatrix BPM is a legacy product line.
Recommendation: rule out.

**42 Creatio: QUALIFIES** (2026-09-24). C1: "Call Creatio.ai process element" (Creatio
Academy, under *process-elements-reference / system-actions*): "Use the Call Creatio.ai
business process element to integrate Creatio Sub-agents into any business process." It
also says: "When the business process activates the Call Creatio.ai element, the element
executes the following actions: Call and execute the requested skill… Receive response
from Creatio AI." This is a **dedicated native node type** (the BAMOE/Flowable/ProcessMaker
mode). C2: "Process Designer basics" describes BPMN gateway semantics ("Gateways that
activate one ore more outgoing flows depending on the gateway type: 'exclusive OR,'
'inclusive OR,' 'parallel AND'"). The Academy also has "Import *.BPMN files" and "Add a BPMN
business process to a section" (result titles). C3 YES, C4 YES (established CRM/BPM
vendor). Also noted: a community thread "Can Creatio.ai generate a complete Business
Process…" is design-time (E2).

**43 AgilePoint NX: UNCLEAR-NEEDS-RULING (C2)** (2026-09-24). C1 YES: the docs contain AI
process activities. "Invoke Agent (n8n) activity" is configured like any activity ("You can
configure whether this activity waits for other activities before it runs"). The result
list also shows "Image Classification - Initiate Subprocess activity", "OpenAI Compatible
LLM" and "AI Control Tower". C2 UNCLEAR: the glossary entry "BPMN properties" says "Each
activity has an optional set of properties for the BPMN standard". That suggests AgilePoint's
own activity shapes carry BPMN *attributes* rather than being drawn in BPMN notation. This
is a Pega-like question (B12). A screenshot of the process canvas would settle it.

**44 Comidor: UNCLEAR-NEEDS-RULING (C1, C4)** (2026-09-24). "Intelligent Process Automation"
(comidor.com) makes only generic claims: "By integrating BPM with RPA and AI/ML
technologies, organizations are able to build, automate and optimize end-to-end business
processes"; "To intelligently automate means to enhance BPM and RPA with AI and ML." No
concrete AI element inside a process model was found. The top result is a 2020 PDF ("RPA,
AI/ML combined with BPM"). C2 is not quoted. C4: a small vendor.

**45 Visual Paradigm: UNCLEAR-NEEDS-RULING (C1 NO-leaning)** (2026-09-24). "AI Chatbot for
BPMN Business Process Diagrams": "Describe your business workflow. Get a compliant BPMN 2.0
Business Process Diagram in seconds." This confirms C2, and the AI is purely
design-time. The whole 10-result sweep (q40) is AI diagram generation ("AI-assisted DFD",
"Conversational AI Diagramming", "Custom AI Endpoint"). Recommendation: rule out.

**46 Cardanit: UNCLEAR-NEEDS-RULING (C1 NO-leaning)** (2026-09-24). "AI in BPM: how
industries and business analysts can harness the power of AI BPMN generators" (21 October
2025): "An AI BPMN generator is an artificial intelligence–powered tool that helps create
Business Process Model and Notation (BPMN) diagrams automatically from text prompts". The
other sweep hits (q42) are also about AI for modelling and simulation ("The risks of using
AI for BPMN and Simulation"). Recommendation: rule out.

**47 Modelio: UNCLEAR-NEEDS-RULING (C1 NO)** (2026-09-24). The home page describes "The Open
Source Modeling Environment UML, BPMN, ArchiMate, SysML". There is no AI, LLM or agent
mention on the page, and the sweep (q41) returned the home page only. Recommendation: rule
out.

**48 Miragon: UNCLEAR-NEEDS-RULING, and a B4 scope case** (2026-09-24). Miragon is a German
Camunda consultancy, so it belongs to the practitioner layer rather than being a vendor.
The opened post, "Agent-Skills für BPMN & Zeebe" (18 June 2026), is about AI coding agents
that *write* BPMN/Zeebe artefacts, which is design-time. But the sweep (q43) also lists "AI
in der Prozessautomatisierung | 1-Tages-Training", "KI-Integration für Unternehmen",
"Miragon AI: Vom Cockpit zur Konversation" and "AI & BPMN: Modelle visuell sauber halten".
Those are not opened, and the training and portfolio pages are likely to show Camunda AI
agent processes. The disposition depends on the B4 ruling on practitioner sources.

**49 "Berger BPM": NOT IDENTIFIED.** The method prompt names "Berger BPM". A Google query
(`"Berger" BPM BPMN AI OR KI OR agent OR LLM`, q44) returned only academic papers (HU
Berlin "Large Process Models", TUM "Conversational Process Modelling", Springer). No vendor
by that name surfaced. **I did not guess a domain.** → operator question (OPERATOR-TODO
B13): which vendor was meant?

**50 QuantumBPM: UNCLEAR-NEEDS-RULING (C4)** (2026-09-24, Channel 3 grid name). "Orchestrating
AI Agents with BPMN: Durable, Auditable Agentic Workflows" (quantumbpm.com, 13 June 2026, by
the founder): "A single agent step is a service task. A reasoning loop is an ad-hoc
sub-process." It is explicit that its own engine executes this: "it's worth being exact
about how it works in QuantumBPM… When a token enters an ad-hoc sub-process, the engine parks
it and exposes the inner activities as separately triggerable steps." C1 YES, C2 YES
(ad-hoc sub-process, FEEL, sequence flows). C3 YES. C4 UNCLEAR: a young, small vendor. It is a third
independent instance of the *AI orchestrating an ad-hoc sub-process* pattern, after Camunda and
Aletyx.

**51 Flows for APEX: UNCLEAR-NEEDS-RULING (C4)** (2026-09-24, Channel 3 grid name). "AI Service
Task" (flowsforapex.org docs): "The Flows for APEX AI Service Task allows you to call
Generative AI Services as a workflow step… Add a Service Task into your BPMN diagram… convert
the task to a Service Task". Its documented use cases are "Generate Process Routing /
Recommended Course of Action" and "Generate Document". The *routing* use case is AI deciding
the path at a gateway. C1 YES, C2 YES (bpmn-js-style modeller, BPMN service task), C3 YES
(open source, GitHub). C4 UNCLEAR: an Oracle-APEX-community BPMN engine, maintained by
FlowQuest. The release post "Flows for APEX 26.1: adaptive workflow and AI-driven BPMN…"
(flowquest.net, May 2026) was not opened.

**52 Atamya: UNCLEAR-NEEDS-RULING (C4)** (2026-09-24, Channel 3 grid name). "AI-Powered
Workflows" (atamya.com): AI "operates directly from within the process itself – as a native
service task, orchestrated by a full-fledged BPMN engine"; "It's a BPMN service task – just
like 'Active Object,' 'Edit Attribute Value,' or 'Synch with Shopware'"; "AI does not only
generate content but prepares decisions directly in your workflow." C1/C2 YES. C4 UNCLEAR: a
German product-information-management (PIM) vendor. BPMN is embedded in a PIM product
rather than sold as a BPM suite.

**53 Citeck ECOS: UNCLEAR-NEEDS-RULING (C4; C1/C2 thin)** (2026-09-24). "Custom AI Agents"
(citeck-ecos.readthedocs.io) states agents are "Used in BPMN processes via POST
/api/ai-agent/execute". That is one sentence only, and the rest of the page is chat-routing
internals. C1/C2 lean YES, but the evidence is thin. C4 UNCLEAR: a small Alfresco/Flowable
integrator with its own ECOS platform.

**Opened on 2026-09-24 but not scored (session stopped by operator):**
- **ZeaProcess** (zeaprocess.com): "turns prompts, SOPs, and documents into governed,
  BPMN-ready process models" (design-time), **but** its product-palette mock-up lists "AI
  Agent Task" as an activity type next to Task, Approval and Decision. C1 is open.
- **Dragon1** (dragon1.com): a series of "AI BPMN … Process" pages (Sept–Oct 2025, e.g.
  "AI BPMN Customer Services Process", "current and future state"). These are video/diagram
  pages, and the page would not render for inspection. C1 is open.
- **BPMN Kit** (github.com/bpmnkit/monorepo): a TypeScript toolkit for Camunda 8 with "an AI
  design assistant" and docs for coding agents. That is design-time, so C1 is NO-leaning.
  It is a toolkit, not a vendor.

**Swept but not opened (q52–q54):** JointJS (an "AI Agent Builder" demo in a diagramming
library), Tallyfy ("BPMN patterns mapped to modern workflow tools", product likely
non-BPMN), Moxo ("BPMN 2.0 for ops: Designing for AI agent coordination", product
notation unknown). New names from the same results: aiprocess.design ("Agentic Process
Design"), BP3 blog "Upgrade Your BPM Strategy with AI Agents and BPMN".

### An emerging category the taxonomy may want

Several major BPMN vendors are **not** vendors with no AI story. Their AI capability sits
*around* the process rather than *inside* it:

- **AI that governs or mines agents running elsewhere:** SAP Signavio (row 16; "using the
  platform of your choice"), ARIS (row 36; BPM as "a governance framework for AI and digital
  workers"), and possibly Celonis (row 29).
- **AI that assists the modeller (design-time):** BOC ADONIS (20), iGrafx Pia (37), GBTEC Arty
  (35, partly), Visual Paradigm (45), Cardanit (46), OpenText Developer Aviator (40).

If the researcher rules these out, it is worth saying so explicitly in Section
`sec:pattern_taxonomy:sources` rather than silently omitting them. The finding would be that
the large pure-play BPMN *modelling* vendors in the sample (Signavio, ARIS, ADONIS, iGrafx)
all promote AI *about* processes rather than *in* them, and that AI-in-BPMN is promoted by
the *execution-engine* vendors (Camunda, Flowable, BAMOE, ProcessMaker, Creatio, Appian,
Bonita, Scheer PAS, UiPath). That is a finding about the market, and it is the kind of
result a criterion-based frame is supposed to surface.

### Promotion modes observed across the qualifying and near-qualifying rows

For the taxonomy chapter, as a starting hypothesis only (not a census result):

| Mode | Rows |
|---|---|
| Dedicated native AI node type in the BPMN palette | IBM BAMOE (8), Flowable (10), ProcessMaker FlowGenie (14), Creatio "Call Creatio.ai" (42), Appian "Execute AI Agent" smart service (21), IFS AI Task (6), Pega Agent Step (23, C2 open) |
| AI orchestrating an ad-hoc sub-process | Camunda (1, 2), Aletyx "Ad-hoc Intelligence" (30), LoyJoy (19, sub-process type) |
| Connector / implementation bound to an ordinary task (**delegated binding**, AI invisible on the diagram) | UiPath (3, 4), Scheer PAS xUML execution model (13), Bonita AI connectors (15), CIB seven connector (17), Frends (7), FlowX.AI service task (18), AgilePoint (43) |
| AI agents as task **performers** / lane participants | Trisotech (12), possibly SAP Signavio (16) |
| AI bound through model annotations / event configuration | Imixs (34), to verify |
| Process-to-agent substitution (BPMN as input to an agent) | IBM watsonx (9), Oracle OIC (39, both modes) |

---

## Note on `OUT` rows (updated 2026-09-24)

Pass 1 initially recorded **no `OUT` rows**. The continuation added **five evidenced C2
rejections**: Salesforce Flow (24), ServiceNow (25), Pipefy (26), Kissflow (27) and
Microsoft Power Automate (28). Each names the notation actually used, quoted from an opened
page.

Two expected rejections did **not** survive contact with the evidence, which shows the
frame at work in both directions:
- **Celonis** (29) was expected to be a process-mining tool with no BPMN. Its Process
  Management module is native BPMN 2.0, so it stays in as `UNCLEAR`.
- **Pega** (23) leans towards C2 `OUT`, but its shape icons could not be told apart from
  BPMN tasks with confidence, so it went to the researcher (B12) rather than being rejected.

No `OUT` under C3 has been recorded. Every vendor opened offered public documentation or
marketing material. The nearest case is Celonis, whose documentation is login-walled while
its developer portal is public.

**For the thesis:** the five C2 rejections are all *workflow-automation* platforms whose
AI stories are genuine (Agentforce, Now Assist, Copilot…) but whose process notation is
proprietary. That is exactly the discrimination C2 was designed to make. The Power Automate
deprecation of its Visio-BPMN export (effective 14 July 2026) is a small corroborating
market signal.
