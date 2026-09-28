# Search protocol (Pass 1, vendor sampling frame)

Reproducibility record for the grey-literature search behind the vendor sampling frame
(`chapters/thesis/004_method.tex`, Section `sec:method:vendor_sampling`; guidance per
Garousi et al. 2019).

- **Agent model:** Claude (Opus) via Claude Code
- **Browser tooling:** `claude-in-chrome` MCP (extension attached to the operator's Chrome
  profile), not `chrome-devtools-mcp`. Logged here because `SETUP.md` specifies the CDP
  server; the extension was what was actually available in this session.
- **Search engine used for all engine sweeps: Google** (`https://www.google.com/search?q=...&hl=en`).
  DuckDuckGo and Bing were tested first on the same probe query and rejected - see the
  engine note at the end of Channel 3. No hosted `WebSearch` tool was used; every result
  page was retrieved in the browser session, per `SETUP.md` §1.
- **Dates:** all work 2026-09-22 unless a row says otherwise; continuation queries q1-q44 on 2026-09-24.
- **Screening unit:** "results screened" = result titles+snippets read on the result page,
  not pages opened. Pages opened are recorded in `candidate-vendors.md` as evidence URLs.

## Channel index

| # | Channel | Status | Saturation statement |
|---|---|---|---|
| 1 | Seed set re-verification | worked | saturated: all 7 seed sources re-opened live |
| 2 | BPMN-engine / BPM-suite vendor list | worked (2026-09-24) | saturated for the named list: every named vendor opened except "Berger BPM" (unidentifiable); captcha-voided sweeps re-run. ~20 grid-discovered names still unopened (see `candidate-vendors.md`) |
| 3 | Search-engine query grid | worked | saturated: full 6x6 cell grid; last 4 cells produced no new AI-in-BPMN-runtime vendor |
| 4 | Marketplaces and template catalogues | worked | saturated for the three catalogues reached; SAP Business Accelerator Hub and the Bizagi/Appian/Pega/ProcessMaker galleries NOT reached |
| 5 | Software directories (G2, Capterra) | **NOT WORKED** | no queries issued |
| 6 | Practitioner and community channels | **barely started** | names harvested from Channel 3 only; no channel-native search |
| 7 | Academic pointers | **NOT WORKED** | names harvested from Channel 3 only; no citations followed |
| 8 | Competitor / "alternatives" pages | worked | saturated on one publisher: pages 2 and 3 yielded zero new names. Not saturated across publishers. All 7 yielded names opened 2026-09-24 (5 C2 `OUT`, Celonis `UNCLEAR`, Decisions = ProcessMaker) |

---

## Channel 1 - Seed set re-verification

Seed sources carried over from the discarded July 2026 round
(`sources/known-positives.md`): Camunda, IBM watsonx Orchestrate, IBM BAMOE, IFS Cloud,
Frends, UiPath (Maestro + Marketplace), FireStart. Each was re-opened live rather than
assumed to still qualify.

| Date | Source | URL opened | Outcome |
|---|---|---|---|
| 2026-09-22 | Camunda | `docs.camunda.io/docs/components/agentic-orchestration/ai-agents/` and `camunda.com/blog/2025/05/benefits-bpmn-ai-agents/` | still qualifies; AI Agent connector + ad-hoc sub-process confirmed live |
| 2026-09-22 | Camunda Marketplace | `marketplace.camunda.com/listing` | 254 listings; split out as its own source |
| 2026-09-22 | FireStart | `firestart.com/en/ai-workflows`, `/en/solutions?ai=1`, `/en/platform-overview`, `/en/use-cases/vertragsanalyse-ki`, `/en/ai-blog` | **site redesigned since July 2026**; the known-positive diagram is no longer on the AI-workflows page. C1/C2 still hold; C4 raised as a ruling |
| 2026-09-22 | IBM Developer (watsonx Orchestrate) | `developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/` | live, updated 26 July 2026; C1 raised as a ruling (BPMN-to-agent, not AI-in-BPMN) |
| 2026-09-22 | IBM BAMOE | `ibm.com/docs/en/ibamoe/9.3.x?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview` | still qualifies; dedicated AI Agent BPMN node type confirmed |
| 2026-09-22 | IFS Cloud | `docs.ifs.com/.../070_ifs_ai/` and `.../050_business_process_modeling/` | still qualifies; IFS AI Task confirmed; JS bot challenge noted |
| 2026-09-22 | Frends | `docs.frends.com/frends-development/agentic-ai/intelligent-ai-connector` + `llms.txt` | still qualifies; C4 raised as a ruling |
| 2026-09-22 | UiPath Maestro docs | `docs.uipath.com/maestro/.../how-to-complex-process` | still qualifies; served in German |
| 2026-09-22 | UiPath Marketplace | `marketplace.uipath.com/sitemap`, `/products/accelerators`, `/products/gen-ai` | still qualifies; **`/listings` index now 404s**, catalogue restructured since July 2026 |

**Saturation:** all seven seed sources re-verified against live pages; none was assumed.
Two had materially changed since July 2026 (FireStart redesign, UiPath Marketplace
restructure), which is itself the justification for re-verifying rather than assuming.

---

## Channel 2 - BPMN-engine and BPM-suite vendors

Per-vendor check: does the vendor have a public, named AI-in-BPMN feature, and is the
promoted artefact BPMN 2.0?

Method: a `site:<domain>` sweep per vendor, then the best-looking page opened for a
verbatim quote. A `site:` sweep alone is **not** treated as sufficient for a verdict.

| Date | Vendor | Entry URL opened | Outcome |
|---|---|---|---|
| 2026-09-22 | Flowable | `documentation.flowable.com/latest/reactmodel/bpmn/reference/ai-agent` | QUALIFIES — AI Agent Task is a first-class element in the BPMN reference |
| 2026-09-22 | Bizagi | `help.bizagi.com/platform/en/index.html?ai_agents_form_actions_sentiment_analysis.htm` | QUALIFIES — AI Hub branch; "Execute AI Agents from Activity Actions" exists |
| 2026-09-22 | Trisotech | `trisotech.com/bpmn-user-tasks-for-humans-and-ai-agents/` | QUALIFIES — humans / AI agents / supervised AI agents as BPMN user-task performers |
| 2026-09-22 | SAP Signavio | `site:` sweep only, no page opened | all AI hits are process-*intelligence* / AI-driven modelling recommendations, not AI in a process. Needs a page open before a verdict |
| 2026-09-22 | Scheer PAS | `site:` sweep only, no page opened | AI Agent tutorials exist but appear bound to xUML services, not BPMN. Needs a page open |
| 2026-09-22 | ProcessMaker | `site:` sweep only, no page opened | "Make Your Tools and AI Agents Work as One" + a free BPMN 2.0 modeller. Needs a page open |
| 2026-09-22 | Bonitasoft | `site:` sweep only, no page opened | "Bonita BPM – AI-Powered BPA Platform", "Ofelia" AI orchestration. Needs a page open |
| 2026-09-22 | GBTEC | `site:` sweep only | 5 results, all AI-transformation marketing; no AI-in-BPMN artefact surfaced |
| 2026-09-22 | Software AG ARIS | `site:` sweep only | 2 results, process-intelligence framing |
| 2026-09-22 | iGrafx | `site:` sweep only | 3 results; "QuickMap — Create Process Maps without needing to Draw" is AI-generates-diagram |
| 2026-09-22 | Newgen | `site:` sweep only | 0 results on the phrase sweep |
| 2026-09-22 | Oracle | `site:` sweep only | OIC Process Automation + "AI Agent Loop" blog posts; relationship to BPMN unverified |
| 2026-09-22 | OpenText | `site:` sweep only | 0 results on the phrase sweep |
| 2026-09-22 | Nintex | `site:` sweep only | 4 results, all community posts; "Nintex Process Manager MCP" is the closest |
| 2026-09-22 | Appian / Pega | `site:` sweep returned 0 | **sweep was rate-limited, result not trustworthy** — must be re-run |
| 2026-09-23 | CIB seven | `docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/` | QUALIFIES on C1/C2; C4 raised as ruling B5. Vendor itself labels runtime vs design-time AI |
| 2026-09-23 | FlowX.AI | `docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration` | QUALIFIES on C1/C2; C4 raised as ruling B6 |
| 2026-09-23 | LoyJoy | `docs.loyjoy.com/bpmn/subprocesses/ai_agent/` | QUALIFIES on C1/C2; C4 raised as ruling B7 |
| 2026-09-23 | BOC Group (ADONIS) | `boc-group.com/en/blog/bpm/how-adonis-elevates-ai-powered-bpm/` | **C1 NO on positive evidence** — all named AI capabilities are design-time. Ruling B8 |
| 2026-09-24 | Pegasystems | `docs.pega.com/bundle/ai-pega/page/platform/gen-ai/agent-steps.html`, `…/blueprint/…/blueprint-case-types.html`, `…/platform/…/assignment-shapes-processes.html` | C1 YES; C2 UNCLEAR (BPMN import-only, Case Lifecycle + Pega shapes). Ruling B12. On-site search froze renderer |
| 2026-09-24 | Scheer PAS | `doc.scheer-pas.com/academy/latest/step-3-integrating-the-agent-to-the-process` | C1/C2 YES (BPMN task → xUML execution model → agent operation, delegated binding); C4 UNCLEAR |
| 2026-09-24 | ProcessMaker | `docs.processmaker.com/docs/add-a-genie-in-a-process` | QUALIFIES — FlowGenie native BPMN node (pool, boundary events, multi-instance) |
| 2026-09-24 | Bonitasoft / Ofelia | `documentation.ofelia.com/bonita/latest/process/ai-connector` | QUALIFIES — LLM connectors in BPMN processes; vendor rebranded to Ofelia |

**2026-09-24 continuation: query log (Google, real tab navigation, `#search` presence and
captcha regex checked on every query; no blocker encountered).**

Google now wraps result links in opaque `/goto?url=<token>` redirects, so the target URL
cannot be read from the `href`. Results were followed by clicking the extracted `<a>`
element, and the landing URL was read from `location` afterwards.

| # | Query | Results | Opened |
|---|---|---|---|
| q1 | `site:help.salesforce.com "Flow Builder" canvas elements` | 10 | Flow Builder Tour |
| q2 | `site:help.salesforce.com "Flow Elements" reference` | 10 | Flow Element Connectors |
| q3 | `site:servicenow.com "Workflow Studio" flow designer actions subflows "flow logic"` | 10 | Flow logic |
| q4 | `site:help.pipefy.com pipe phases cards kanban` | 9 | What are pipes |
| q5 | `site:pipefy.com BPMN` | 9 | What It Is and How to Build a BPMN Diagram (SEO trap) |
| q6 | `site:helpdoc.kissflow.com process workflow steps branch` | 0 | — (**guessed host**, recorded as an error; real host is `kfdocs.kissflow.com`) |
| q7 | `kissflow help process workflow builder "parallel branch"` | 9 | Parallel branch; then glossary Process, Step (extracted links) |
| q8 | `site:learn.microsoft.com power automate cloud flow designer "trigger" "actions" canvas` | 10 | Explore the cloud flows designer |
| q9 | `site:learn.microsoft.com OR site:support.microsoft.com Visio BPMN "Power Automate" export` | 10 | Design an automated workflow in Visio [DEPRECATED] |
| q10 | `site:celonis.com BPMN` | 9 | CPM BPMN reference (login wall), BPMN tasks (developer portal) |
| q11 | `site:celonis.com "AI agent" "process model" OR BPMN OR orchestration` | 10 | Adding Process Copilot… (login wall), Design Processes |
| q12 | `site:docs.pega.com BPMN` | 10 | Configuring Case Types (Blueprint); Configuring complex Processes (404) |
| q13 | `site:docs.pega.com "Process Modeler" shapes flow` | 10 | Assignment shapes in Processes |
| q14 | `site:docs.pega.com "agent" step "Case Lifecycle" GenAI` | 10 | Agent Steps |
| q15 | `site:doc.scheer-pas.com "AI agent" BPMN` | 9 | AI Tutorials → Tutorial 1 → Step 3 (nav links) |
| q16 | `site:docs.processmaker.com BPMN AI` | 9 | Modeling Objects; Validate Your Process is BPMN 2.0 Compliant |
| q17 | `site:docs.processmaker.com "AI agent" OR "GenAI" OR "RAG" task process` | 10 | Add a Genie in a Process → FlowGenie |
| q18 | `site:documentation.bonitasoft.com OR site:bonitasoft.com AI agent BPMN process` | 10 | Bonita BPM – AI-Powered BPA Platform (ofelia.com) |
| q19 | `site:documentation.bonitasoft.com AI connector OpenAI OR Mistral OR LLM` | 10 | AI connectors |
| q20 | `site:documentation.bonitasoft.com OR site:documentation.ofelia.com "Process Diagram overview"` | ≥1 | Process Diagram overview |
| q21 | `jBPM OR Kogito OR Aletyx BPMN "AI agent" OR LLM OR langchain4j` | 10 | aletyx-kogito-ai-addons README (GitHub) |
| q22 | `site:kie.apache.org OR site:jbpm.org OR site:kie.org AI OR LLM OR agent BPMN` | 10 | Pragmatic AI (Drools/DMN) |
| q23 | `Operaton BPMN engine AI OR LLM OR agent` | 8 | operaton.org home, then /roadmap (nav link) |
| q24 | `Activiti BPMN "AI" OR LLM OR agent Alfresco OR Hyland` | 10 | — (no AI hit to open) |
| q25 | `site:activiti.org OR site:hyland.com Activiti OR "Process Automation" AI agent BPMN` | 10 | Hyland Connect forum post (RAG) |
| q26 | `site:imixs.org OR site:imixs.com AI OR LLM BPMN` | 9 | AI Agents vs. AI-Augmented Workflows |
| q27 | `site:gbtec.com BPMN AI OR KI OR agent OR LLM OR copilot` | 10 | Arty launch release |
| q28 | `site:gbtec.com "Work Orchestrator" AI OR KI OR agent OR LLM` | 10 | PEX agentic webinar page; IDP page |
| q29 | `site:aris.com OR site:softwareag.com ARIS BPMN "AI agent" OR agentic OR LLM OR copilot` | 10 | ARIS AI Companion; BPM in the Age of AI |
| q30 | `site:igrafx.com BPMN AI OR agent OR agentic OR LLM` | 10 | Pia |
| q31 | `site:newgensoft.com BPMN AI OR agent OR agentic OR LLM OR GenAI` | 4 | BPM platform page; Process Modeling page |
| q32 | `site:docs.oracle.com "Process Automation" OR "Integration" BPMN "AI agent" OR GenAI OR LLM` | 0 | — (results container present, no captcha: a genuine zero, attributed to over-constrained query) |
| q33 | `Oracle Integration "Process Automation" BPMN "AI agent"` | 9 | The future of OIC Process Automation |
| q34 | `site:opentext.com BPMN "AI" OR agent OR Aviator process automation` | 10 | Process Automation product page |
| q35 | `site:tibco.com BPMN AI OR agent OR agentic OR LLM` | 9 | ActiveMatrix BPM "Process Design - BPMN" |
| q36 | `site:academy.creatio.com BPMN "AI agent" OR "AI Skill" OR Copilot business process` | 2 | — (too narrow; re-issued as q37) |
| q37 | `Creatio business process designer AI agent element BPMN` | 9 | Call Creatio.ai process element; Process Designer basics |
| q38 | `site:agilepoint.com BPMN AI OR agent OR agentic OR GenAI activity` | 10 | Invoke Agent (n8n) activity; BPMN properties |
| q39 | `site:comidor.com BPMN AI OR agent OR agentic OR LLM` | 9 | Intelligent Process Automation |
| q40 | `site:visual-paradigm.com BPMN "AI agent" OR agentic OR LLM task` | 10 | AI Chatbot for BPMN |
| q41 | `site:modelio.org OR site:modeliosoft.com BPMN AI OR LLM OR agent` | 1 | modelio.org home |
| q42 | `site:cardanit.com BPMN AI OR agent OR LLM` | 9 | AI in BPM: … AI BPMN generators |
| q43 | `site:miragon.io OR site:miragon.de BPMN AI OR agent OR LLM OR KI` | 10 | Agent-Skills für BPMN & Zeebe |
| q44 | `"Berger" BPM BPMN AI OR KI OR agent OR LLM` | 9 | — (only academic results; vendor not identified) |
| q45 | `site:signavio.com OR site:community.sap.com Signavio BPMN "AI agent" lane OR "service task" OR performer` | 10 | February 2026 release post (B10 check) |
| q46 | `site:boc-group.com ADONIS MCP AI` | 10 | Let Your BPM Speak AI with MCP and ADONIS (B8 check) |
| q47 | `site:quantumbpm.com BPMN AI agent` | 4 | Orchestrating AI Agents with BPMN |
| q48 | `"Flows for APEX" BPMN AI OR LLM OR agent` | 8 | AI Service Task (docs) |
| q49 | `"BPMN Kit" AI agent` | 9 | bpmnkit/monorepo README |
| q50 | `Citeck ECOS BPMN AI agent` | 9 | Custom AI Agents (Read the Docs) |
| q51 | `Atamya BPMN AI agent` | 9 | AI-Powered Workflows |
| q52 | `ZeaProcess BPMN AI` | 8 | zeaprocess.com home |
| q53 | `Dragon1 BPMN AI agent` | 9 | AI BPMN Customer Services Process (did not render) |
| q54 | `JointJS BPMN AI agent` / `Tallyfy BPMN AI agent` / `Moxo BPMN AI agent workflow` | 9 / 9 / 8 | — (stopped by operator before opening) |

**Session end, 2026-09-24:** the operator stopped the grid-name pass as diminishing returns.
Still-unopened grid names are listed in `candidate-vendors.md`.

**Channel 2 status after this continuation:** every vendor named in the method prompt now
has at least one opened page and a recorded verdict, except "Berger BPM" (not identifiable,
OPERATOR-TODO B13). The six captcha-voided sweeps (GBTEC, ARIS, iGrafx, Newgen, Oracle,
OpenText) were re-run with full vocabulary (`AI OR agent OR agentic OR LLM OR copilot`,
plus `KI` for German vendors). **Two of those six changed materially:** Newgen now qualifies
(the voided sweep had returned 0), and Oracle is a strong `UNCLEAR`. Both would have been
lost if the voided zeros had been treated as findings. **Saturation for the named list:
reached.** Saturation for the channel as a whole is not claimed: vendors outside the named
list were only found through Channels 3 and 8.

**CAPTCHA artefact - the most important methodological note in this file.**

Partway through the Channel 2 sweeps, Google began serving a CAPTCHA interstitial. The
agent did not detect it: queries were being issued with `fetch()` from an already-open
google.com tab, and a challenge page returns **HTTP 200 with no `#search` block**, which the
parser reported as *zero results*. Zero results were then recorded for cibseven.org,
flowx.ai, loyjoy.com and boc-group.com.

**The operator solved the CAPTCHA by hand in the browser.** The identical queries then
returned 10 results each, and three of those four vendors (CIB seven, FlowX.AI, LoyJoy)
turned out to have explicit, strong AI-in-BPMN material and are now `UNCLEAR-NEEDS-RULING`
sources with assignment files. Three qualifying sources were within one un-rerun query of
being silently lost.

Consequences, all of which bind any future run:

1. **A zero-result `site:` sweep is not evidence of absence.** It must be treated as
   `BLOCKED` until re-issued after the block clears - exactly as shared rules section 9
   requires for a captcha, and never as a finding.
2. **`fetch()`-based search hides blockers.** It converts a captcha into a silent empty
   result. Real tab navigation renders the challenge visibly. Pass 2 should navigate, or
   must explicitly test for the presence of the results container and raise a blocker when
   it is missing. An earlier session note that attributed these zeros to rate limiting was
   wrong; the cause was a captcha, confirmed by the operator.
3. **The vendor verdicts recorded during the blocked window are void.** GBTEC, Software AG
   ARIS, iGrafx, Newgen, Oracle, OpenText, Nintex, Appian and Pega were all swept in or near
   that window on a single narrow phrase. Their rows are logged as *unverified*, and none of
   them is a rejection.

**Saturation: NOT reached for this channel.** Fifteen of the ~30 named vendors have only a
`site:`-sweep signal and no opened page, and four sweeps (Appian, Pega, CIB seven, FlowX.ai,
LoyJoy, BOC) returned 0 results at a point where Google was demonstrably rate-limiting —
those zeros are artefacts of the tooling, not findings. See the recall assessment in the
final report.

---

## Channel 3 - Search-engine query grid

Grid: {`BPMN`} x {`AI agent`, `LLM`, `agentic`, `AI task`, `copilot`, `GenAI`} x
{`tutorial`, `docs`, `blog`, `template`, `marketplace`, `example`}, plus `site:` variants.

| Date | Engine | Query string | Results screened | New vendor names yielded | Note |
|---|---|---|---|---|---|
| 2026-09-22 | DuckDuckGo (`duckduckgo.com/?q=`) | `BPMN "AI agent" docs` | 7 (4 organic, 3 ads) | BPMN Kit, CIB seven | engine yielded only 3-4 organic results and German-localised ads; abandoned as the primary engine |
| 2026-09-22 | DuckDuckGo HTML (`html.duckduckgo.com/html/?q=`) | `BPMN "AI agent" docs` | 4 | (none new) | static endpoint returned the same 3 organic results; abandoned |
| 2026-09-22 | Bing (`bing.com/search?q=`) | `BPMN "AI agent" docs` | 10 | (none new) | Bing silently dropped the quoted phrase and returned generic "what is BPMN" pages; abandoned |
| 2026-09-22 | Google (`google.com/search?q=&hl=en`) | `BPMN "AI agent" docs` | 9 | CIB seven, BPMN Kit, FlowX.ai, LoyJoy, ba-copilot.com | engine honoured the phrase; adopted as the grid engine |
| 2026-09-22 | Google | `BPMN "AI agent" tutorial` | 6 | Lucidflow.ai, Scheer PAS | |
| 2026-09-22 | Google | `BPMN "AI agent" blog` | 9 | BP3, Incentro, Moxo, Flowable, IBM community | |
| 2026-09-22 | Google | `BPMN "AI agent" template` | 7 | (none new) | |
| 2026-09-22 | Google | `BPMN "AI agent" marketplace` | 9 | Camunda Marketplace, BOC Group (ADONIS), AWS Marketplace | |
| 2026-09-22 | Google | `BPMN "AI agent" example` | 8 | (none new) | |
| 2026-09-22 | Google | `BPMN "LLM" tutorial` | 7 | BESSER, LLM4BPMNGen (TUM), growwstacks | mostly AI-generates-the-diagram, not AI-in-the-process |
| 2026-09-22 | Google | `BPMN "LLM" docs` | 9 | Eraser.io, BPMN Assistant (arXiv/MDPI) | |
| 2026-09-22 | Google | `BPMN "LLM" blog` | 9 | bpmn.io, JointJS, Imixs (Open-BPMN), processcamp.io | |
| 2026-09-22 | Google | `BPMN "LLM" template` | 9 | Nala2BPMN, BPMN-Chatbot (CEUR), Mestro | |
| 2026-09-22 | Google | `BPMN "LLM" marketplace` | 9 | OPACA, lobehub, BAMOE Developer Tools (VS Code marketplace) | |
| 2026-09-22 | Google | `BPMN "LLM" example` | 9 | Conversational BPM (dl.gi.de) | |
| 2026-09-22 | Google | `BPMN "agentic" tutorial` | 8 | IBM Developer, Camunda Academy, UiPath Academy | |
| 2026-09-22 | Google | `BPMN "agentic" docs` | 9 | Flowable (Multi-agent Orchestration in CMMN and BPMN), UiPath Maestro, agentic BPMS (arXiv) | |
| 2026-09-22 | Google | `BPMN "agentic" blog` | 9 | codecentric, MarvelX, QuantumBPM, PwC India | |
| 2026-09-22 | Google | `BPMN "agentic" template` | 8 | Entoura, the-main-thread (GO-BPMN), BESSER-PEARL/agentic-bpmn | |
| 2026-09-22 | Google | `BPMN "agentic" marketplace` | 9 | ABBYY Marketplace, Form.io, CAP BPM, REAL GAIN, UiPath Marketplace | |
| 2026-09-22 | Google | `BPMN "agentic" example` | 7 | (none new) | |
| 2026-09-22 | Google | `BPMN "AI task" tutorial` | 7 | IBM BAMOE Gen AI Task, Flowable Utility Agent | |
| 2026-09-22 | Google | `BPMN "AI task" docs` | 9 | Citeck ECOS, Atamya | |
| 2026-09-22 | Google | `BPMN "AI task" blog` | 9 | Buho Advisors, gmart.in | |
| 2026-09-22 | Google | `BPMN "AI task" template` | 8 | Tallyfy, Kompetenzzentrum KARL | |
| 2026-09-22 | Google | `BPMN "AI task" marketplace` | 9 | yourcompanyos.io | |
| 2026-09-22 | Google | `BPMN "AI task" example` | 8 | (none new) | |
| 2026-09-22 | Google | `BPMN "copilot" docs` | 9 | Microsoft Visio | Camunda BPMN Copilot is AI-generates-diagram, not AI-in-process |
| 2026-09-22 | Google | `BPMN "copilot" example` | 7 | (none new) | |
| 2026-09-22 | Google | `BPMN "copilot" tutorial` | 0 | (none) | Google returned no parsed organic block for this cell |
| 2026-09-22 | Google | `BPMN "copilot" blog` | 9 | justflow.it, ifib.de | |
| 2026-09-22 | Google | `BPMN "copilot" template` | 8 | Latenode | |
| 2026-09-22 | Google | `BPMN "copilot" marketplace` | 9 | Lucidchart, VS Code Business Automation Tools | |
| 2026-09-22 | Google | `BPMN "GenAI" tutorial` | 9 | SAP Community, flowquest.net (Flows for APEX), Aletyx | |
| 2026-09-22 | Google | `BPMN "GenAI" docs` | 9 | Pega GenAI Blueprint, ZeaProcess, ARIS, Datalaria | |
| 2026-09-22 | Google | `BPMN "GenAI" blog` | 9 | Five1, processcentric.ch, PwC CH | |
| 2026-09-22 | Google | `BPMN "GenAI" template` | 9 | Dragon1, Trisotech, fratch.io | |
| 2026-09-22 | Google | `BPMN "GenAI" marketplace` | 9 | Sapiens Decision, GBTEC, BOC ADONIS MCP, TechTarget list | |
| 2026-09-22 | Google | `BPMN "GenAI" example` | 9 | Lucid community | |

**Grid saturation (cross-product cells):** the 6x6 cell grid was worked in full. The last
12 cells (`copilot` and `GenAI` rows) yielded almost exclusively *AI-generates-the-diagram*
tools rather than AI-inside-the-process vendors, and the final 4 cells produced no new
vendor with an AI-in-BPMN *runtime* story. Organic-result depth was ~7-9 per query
(Google's first page); `site:` variants per vendor domain are logged in Channel 2 rather
than repeated here.

**Engine note:** three engines were tested on the same probe query before the grid was
run. Google was the only one that honoured quoted phrases and returned topically relevant
results; DuckDuckGo returned 3-4 organic results, Bing dropped the phrase. All Google
queries were issued from a live google.com tab in the operator's Chrome profile, with
`hl=en`, and the organic result block (`#search a h3` + `cite`) parsed from the returned
document.

---

## Channel 4 - Marketplaces and template catalogues

| Date | Catalogue | URL | Enumerable? | Notes |
|---|---|---|---|---|
| 2026-09-22 | UiPath Marketplace | `marketplace.uipath.com/sitemap` | YES - decisive | 2671 anchors, **2326 unique `/listings/` paths** enumerable from one page. `/listings` index itself 404s |
| 2026-09-22 | UiPath accelerators facet | `marketplace.uipath.com/products/accelerators` | YES | "86 Ergebnisse" |
| 2026-09-22 | UiPath agent catalogue facet | `marketplace.uipath.com/products/gen-ai` | YES | "76 Ergebnisse" |
| 2026-09-22 | Camunda Marketplace | `marketplace.camunda.com/listing` | YES | "254 Results", `?page=N&locale=en-US`, ~12/page. AppDirect platform - look for its JSON `totalCount` |
| 2026-09-22 | FireStart use-case catalogue | `firestart.com/en/solutions?ai=1` | YES, with a caveat | "28 Use Cases gefunden" with the AI facet; platform page claims "65+ Use Cases" unfiltered. **Use-case pages are absent from `sitemap.xml`** (0 of 417) - client-rendered only |

**Saturation: partial.** The three catalogues reached were worked to an exact count. **Not
reached:** SAP Business Accelerator Hub, and the Bizagi / Appian / Pega / ProcessMaker
template galleries named in the method prompt. Those are a known gap, not a saturation
claim.

---

## Channel 5 - Software directories

*No queries were issued in this channel.* G2 and Capterra category listings for
"Business Process Management", "Workflow Automation" and "BPMN tools" were not consulted.
This is the single largest deliberate gap in the Pass 1 record and is reported as such.

| Date | Directory | Category URL | Results screened | New vendor names yielded |
|---|---|---|---|---|

---

## Channel 6 - Practitioner and community channels

No channel-native searching was performed (no Camunda forum search, no CamundaCon talk
index, no consultancy-site sweeps). The practitioner names below were **harvested as a
by-product of the Channel 3 grid**, which is a much weaker instrument for this population
because a general web search ranks vendor content above practitioner content.

Names harvested: BP3, codecentric, Incentro, CAP BPM, Miragon, growwstacks, Buho Advisors,
Five1, Datalaria, PwC (CH, IN), Kompetenzzentrum KARL, processcamp.io, QuantumBPM, MarvelX,
Entoura, ba-copilot.com, Lucidflow.ai, the-main-thread.com, flowquest.net, justflow.it.
Also seen: `forum.camunda.io` and `forum.bpmn.io` threads, and a Camunda forum post
"Accelerating Development of Business Processes Using AI".

| Date | Channel | URL / query | Results screened | New vendor names yielded |
|---|---|---|---|---|

---

## Channel 7 - Academic pointers

*No citations were followed.* Academic items surfaced incidentally by the Channel 3 grid,
listed here so the next run has a starting point: "Agentic Business Process Management
Systems" (arXiv), "BPMN Assistant: An LLM-Based Approach" (arXiv / MDPI),
BESSER-PEARL/agentic-bpmn (GitHub), "Introducing the BPMN-Chatbot" (CEUR), Nala2BPMN,
LLM4BPMNGen (TUM), "Conversational Business Process Modeling using LLMs" (dl.gi.de),
"Large Language Models to Enhance Business Process..." (arXiv), "A Framework for LLM-Based
Conceptual Modeling" (isys.uni-klu.ac.at), KM4ESG (CEUR), OPACA BPMN Editor.

**Important caveat:** the great majority of this academic material is about LLMs
*generating or simplifying* BPMN diagrams, not about AI elements executing inside a process.
It is therefore C1-relevant only where a paper's tool citations lead back to vendor
material. Do not assume this channel is rich for this thesis's question.

| Date | Source | URL | Tools named | New vendor names yielded |
|---|---|---|---|---|

---

## Channel 8 - Competitor / "alternatives" pages

Worked 2026-09-23. Three competitor pages opened.

| Date | Vendor page | URL | Competitors enumerated | New vendor names yielded |
|---|---|---|---|---|
| 2026-09-23 | ProcessMaker/Decisions | `processmaker.com/blog/top-10-camunda-competitors-and-alternatives/` -> redirects to `decisions.com/blog/...` | ProcessMaker, Appian, Pega, Bizagi, Nintex, Salesforce, ServiceNow, Pipefy, Kissflow, Microsoft Power Automate | Salesforce, ServiceNow, Pipefy, Kissflow, Power Automate, Decisions |
| 2026-09-23 | ProcessMaker/Decisions | `.../top-10-bizagi-competitors-and-alternatives/` | ProcessMaker, Nintex, Pipefy, Kissflow, Camunda, Pega, Bonitasoft, Appian, Salesforce Flow, ServiceNow | (none new) |
| 2026-09-23 | ProcessMaker/Decisions | `.../top-10-appian-alternatives-and-competitors/` | ProcessMaker, Pega, Camunda, Nintex, Bizagi, ServiceNow, Pipefy, Kissflow | (none new) |

Also linked from those pages, not opened: "Top 10 Nintex Competitors and Alternatives",
"Top 10 Celonis Competitors and Alternatives" (yields the name **Celonis**).

**Saturation: reached, with a caveat.** The second and third pages produced **zero** new
vendor names. All three enumerate the same closed set. The caveat is that all three pages
come from **one publisher**, so this is saturation of one vendor's competitive worldview,
not of the market. A page from a different publisher (e.g. a Camunda- or Trisotech-authored
comparison) would be a genuinely independent probe and has not been run.

**Two substantive findings from this channel:**

1. **ProcessMaker now redirects to `decisions.com`.** Every `www.processmaker.com/blog/...`
   URL opened on 2026-09-23 resolved to `decisions.com/blog/...` with the content intact.
   ProcessMaker appears to have been acquired by or merged into Decisions. The method prompt
   names ProcessMaker as a candidate vendor; that name now points at a different corporate
   entity, which the thesis should reflect if ProcessMaker is carried into the sample.
2. **The new names are mostly C2-rejection candidates, and none was verified.** Salesforce
   Flow, ServiceNow Flow Designer, Pipefy, Kissflow and Microsoft Power Automate are
   workflow tools with proprietary notations; Celonis is process mining, not orchestration.
   A C2 `OUT` requires **naming the notation actually used**, on an opened page. That
   evidence was not gathered, so **no `OUT` is recorded for any of them**. They sit in the
   open-verification list. Kissflow was probed one level further: it publishes extensive
   BPMN *educational* content ("BPMN - An Ultimate Guide to Business Process Model and
   Notation"), which is SEO material about the standard and is **not** a claim that its
   product uses BPMN - a trap worth flagging, because a naive sweep reads it as C2 evidence.

| Date | Vendor page | URL | Competitors enumerated | New vendor names yielded |
|---|---|---|---|---|
