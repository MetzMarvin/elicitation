---
n: 010
record: 010
url: https://docs.flowx.ai/5.9/ai-platform/tutorials/customer-onboarding
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Does the corpus require BPMN 2.0 notation, or does a process this source publishes as a Mermaid flowchart whose node labels are BPMN element names (User Task, Send/Receive Message Task, Exclusive Gateway, End Event, a timer boundary event) with the AI step bound into it as a workflow call count as a BPMN process with an AI element inside it?
page_publishes: mermaid-process
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from a label read in the page's own diagram.
screenshot: 010_customer-onboarding.png
artefacts:
  - screenshot: 010_customer-onboarding.png
bpmn_evidence: |
  The page's "Architecture overview" publishes the whole onboarding process as a Mermaid `flowchart TD`
  whose node labels are BPMN element names (the page's own fenced source, read verbatim):
    "flowchart TD A(("Start")) --> B["User Task:<br/>Personal Information"] B --> C["User Task:<br/>Address
    Details"] C --> D["User Task:<br/>Employment & Income"] D --> E["User Task:<br/>Document Upload"] E
    --> F["Send Message Task:<br/>Start KYC Check"] F -. "Workflow:<br/>kycVerification" .-> F F -->
    G["Receive Message Task:<br/>KYC Result"] G --> H{"Exclusive Gateway:<br/>KYC Decision"} H --
    "PASSED" --> I["Generate Welcome Letter<br/>(Send/Receive Message)"] H -- "FAILED / REVIEW" -->
    J["User Task: Manual Review<br/>48h Timer Boundary"] J -- "APPROVED" --> I J -- "REJECTED" -->
    K(("End<br/>(Rejected)")) I --> L["Send Email Notification<br/>(Send/Receive Message)"] L -->
    M(("End<br/>(Success)"))"

  Rendered in the browser on 2026-09-25 the diagram is a live Mermaid `<svg class="flowchart">` whose
  `<g class="node ...">` labels are `Start`, `User Task:Personal Information`, `User Task:Address
  Details`, `User Task:Employment & Income`, `User Task:Document Upload`, `Send Message Task:Start KYC
  Check`, `Receive Message Task:KYC Result`, `Exclusive Gateway:KYC Decision`, `Generate Welcome
  Letter(Send/Receive Message)`, `User Task: Manual Review 48h Timer Boundary`, `End(Rejected)`,
  `Send Email Notification(Send/Receive Message)` and `End(Success)`, and whose edge labels include
  `Workflow:kycVerification`, `PASSED`, `FAILED / REVIEW`, `APPROVED` and `REJECTED` - read from the
  DOM, not from a picture.
  Every element of BPMN 2.0's core vocabulary appears in the labels - start and end events (the circles),
  four user tasks, a send message task and a receive message task, an exclusive gateway with its two
  outgoing conditions, a timer boundary event on a user task - and the page's prose names the same things:
  "An **exclusive gateway** that routes the process based on verification results", "The process follows a
  **collect-verify-decide** pattern. Customer data is gathered through a series of user task nodes, sent to
  a KYC service for verification, and then routed based on the result." The page publishes no `.bpmn` file,
  no BPMN XML and no Process Designer canvas: the process exists only as this Mermaid fence and as prose.
ai_evidence: |
  The AI step is bound into the process the way this source binds AI into BPMN everywhere - by delegation
  to a workflow. The diagram calls it directly: the send/receive pair is labelled "Start KYC Check" and
  "KYC Result" and carries the edge label 'Workflow: kycVerification'. The page states what that
  integration is: "A **KYC verification** integration that calls an external REST API via an integration
  workflow". The workflow it calls is the vendor's AI-native canvas - the notation this census records
  elsewhere as NOT BPMN - so whether the AI element is "inside the BPMN process" depends on whether a
  Mermaid process whose nodes are BPMN element names counts as the BPMN process at all. The same page
  lists what the process demonstrates: "Multi-step form collection, REST API integration via workflows,
  conditional branching, document generation, task assignment, notification sending".
note: |
  Read from the page's own published markdown twin
  (https://docs.flowx.ai/5.9/ai-platform/tutorials/customer-onboarding.md) and from the page as displayed
  in the browser (2026-09-25). The capture next to this record is a text render of the page's own fenced diagram source and of the sentences that name it, because the page publishes its process as Mermaid rather than as a diagram image (the same convention records 001 and 004 use). The page's 12 other fenced blocks are JSON payloads and JavaScript snippets (step inputs and
  outputs), not diagrams. This row is UNCERTAIN, not an exclusion, for the same reason record 001
  (`/5.9/ai-platform/tutorials/document-processing`) is: the process is complete and BPMN-shaped but is
  published as Mermaid rather than in BPMN 2.0 notation, and its AI element arrives by delegation to a
  workflow rather than as a node of its own - the corpus's notation rule decides whether it is an
  INCLUDE.
