---
n: 0
url: https://doc.scheer-pas.com/release-notes/pas-25-3-release-notes
source: scheer-pas
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  This release-note page announces the agentic-AI feature as process integration and publishes
  two figures that carry the two halves separately: a BPMN 2.0 process diagram that contains no
  AI element (the OData example), and a Designer screenshot of the AI agent `CaseAgent` of the
  `AIAgent_InsuranceClaim_Example` service with its System/User Prompt bound to OpenAI. The page
  also announces "New example for AI agent usage: AIAgent_InsuranceCase_Example". Does that
  example's published process model contain the AI agent as an element inside the process (as the
  tutorial's Insurance_Case_Process does, records 001-003), and should this page therefore count
  as a page publishing an AI-enabled BPMN artefact - or is the agent here configured beside the
  process (an agent asset of the service) rather than inside the process flow? A reading of the
  page, and of the example itself if it is reachable, is needed to settle it.
bpmn_evidence: >-
  The page publishes BPMN 2.0 notation (fig 1 = captured): the `ODataAdapter_Northwind_E...`
  example open in the Designer's process editor - a start event (thin green circle), the tasks
  "Show customer list", "Show customer details", "Show orders", two exclusive gateways (diamonds
  with an X) with the outgoing flows labelled "customer selected" / "no customer selected ...",
  and an end event (thick red circle) - above the xUML activity diagram of the operation "Get
  Data". The page's own process language names BPMN directly: "New example for parallel gateways
  in BPMN in combination with roles and user tasks: ParallelTasks_Onboarding_Example".
ai_evidence: >-
  The AI element is published beside that diagram, not in it (fig 2 = captured): the Designer with
  the `AIAgent_InsuranceClaim_Example` open, its Explorer listing `Implementation > Agents >
  CaseAgent > CaseAgentInterface > execute (in: CaseRequest, out: AgentResponse)` and the agent's
  properties panel showing "System Prompt: You are an insurance claim agent. You get an email with
  an insurance claim from which you extract all necessary information regarding the case.", a
  "User Prompt" that extracts category/subject/requestText, and "AI Service Provider Alias:
  OpenAI". The release note frames this as process integration: "Designer Kubernetes: Integrate AI
  Agents Into Your Process Flow - This release supports agentic AI. You have the possibility to
  create AI agents and integrate them into your process execution." and, under Designer Examples,
  "New example for AI agent usage: AIAgent_InsuranceCase_Example".
artefacts:
  - screenshot: 004_release-notes-ai-agent-25-3_fig1.png
  - screenshot: 004_release-notes-ai-agent-25-3_fig2.png
capture_quality: legible
capture_width_px: 1920
---

## What the page shows

`PAS 25.3 Release Notes` is the version page on which the agentic-AI feature ships. Its four
figures, in document order, are:

- `image-20251008-120616.png` (1705x359) - the Administration's service list with the new detailed
  status labels (`running`, `Volume Failure`, `High Restart Count`, ...). UI, not a diagram.
- **fig 2 (captured)** `image-20251002-131703.png` (1416x845) - the Designer with
  `AIAgent_InsuranceClaim_Example` open: the `CaseAgent`'s `Prompt` tab, i.e. the AI element of
  this release, and its `AI Service Provider Alias`.
- `image-20250923-112152.png` (1450x408) - the `Idea_Management_Example` control panel with the
  "Enable Angular Build in Version 19" dropdown. UI.
- **fig 1 (captured)** `image-20250929-074728.png` (1920x809) - the `ODataAdapter_Northwind_E...`
  example: the BPMN process canvas on top, the operation's activity diagram below.

Fig 1 is the only diagram on the page, and it is unmistakably BPMN 2.0: start event, user-task
and service-task shapes carrying the person/gear markers, exclusive gateways as diamonds with an
X, named sequence flows, an end event. The lower half of the same figure is the *other* notation -
the xUML activity diagram of the operation `Get Data`, with its `Persisted (Read Only)` / `Local`
/ `Return` bands and pin-labelled action boxes - so both notations are visible side by side here,
which is what makes the page a useful calibration point for the corpus's notation calls.

## Observations

- The page publishes an AI element and a BPMN process, but **not in the same figure**: the agent
  (fig 2) is shown as a service asset with its prompt configuration; the process (fig 1) has no AI
  element anywhere in its flow.
- What the release note claims is stronger than what its figures show - "integrate them into your
  process execution" - and it names a shipped example (`AIAgent_InsuranceCase_Example`) whose
  process model is not published on this page. The tutorial's `Insurance_Case_Process` (records
  001-003) is the same class of artefact; this page is where the feature is announced.
- The page's AI mention is therefore *not* dismissible under E2: it is not about AI generating a
  diagram, AI on the roadmap, or AI in documentation - it is about the AI element being part of the
  process. Hence `UNCERTAIN` rather than an exclusion.

## Notes for the researcher

Both captured figures are byte copies of the page's own attachments
(`image-20250929-074728.png`, `image-20251002-131703.png`), so the pair can be read side by side.
The other two figures of the page were looked at in the AI-page contact sheets
(`ledgers/_scheer/ai_s0.png`, `ai_s192.png`) and are UI screenshots.
