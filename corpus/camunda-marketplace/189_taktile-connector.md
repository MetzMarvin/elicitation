---
n: 189
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Taktile Connector
url: https://marketplace.camunda.com/apps/625827/taktile-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The published model's two Taktile calls are HTTP-JSON service tasks through the vendor's own element templates and nothing in the process file names AI, an LLM or a model; the AI claim lives one level out, in the page's description of the platform being called ('Taktile's AI Decision Platform', 'detect fraud using machine learning models'). Does a connector call into a vendor's AI/ML decisioning platform count as an AI element inside the process, or is this artefact E2-no-ai-element? Same boundary as the Amazon SageMaker connector (n=142) and the Kubeflow connector (n=169). The capture and the .bpmn are both in the corpus.
needs_visual_check: false
bpmn_evidence: BPMN published twice over: as a branded process diagram and as a downloadable .bpmn (process 'Taktile Integration Demo'). Read from the XML: none start event -> serviceTask 'Call decision' (templates Template_0bg8owh and io.camunda.connectors.HttpJson.v2, type io.camunda:http-json:1) -> serviceTask 'Get Taktile Result' (Template_1l3b6mi) -> exclusiveGateway -> 'approve credit' / 'reject credit application' -> none end events, plus a PENDING loop through a 5s timer back into 'Get Taktile Result'. The connector ships its own element templates ('Template_0bg8owh', 'Template_1l3b6mi') on top of the generic HTTP JSON connector. The published figure labels the first call 'Call async decision' while the file names it 'Call decision', so figure and file differ slightly in wording (the flow is the same).
bpmn_evidence_quote: "Call async decision"
ai_evidence: The process file itself names no AI: both Taktile tasks are HTTP-JSON calls through the vendor's own templates, and the page's own prose places the intelligence in the platform rather than in the model - 'Taktile's AI Decision Platform enables financial institutions to design, test, and deploy automated risk strategies', and 'you can automate KYC/KYB checks, detect fraud using machine learning models, and determine product eligibility in real time'. The connector's purpose is to weave that platform's decisions into the Camunda flow.
ai_evidence_quote: "detect fraud using machine learning models"
artefacts:
  screenshot: 189_taktile-connector.png
  archive: null
  bpmn_xml: 189_taktile-connector.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/625827/overview/img11669759107467081013-2x.png, 1100x313) and of the .bpmn reached through the listing's own Modeler import link; the image read natively at full size, the XML read directly
---

## What the page shows

Taktile Connector (Camunda Services GmbH, partner connector for Taktile's decisioning platform). A decision call placed in the flow: the process asks Taktile for a decision on a credit application, polls for the result, and branches to approval or rejection.

## Observations (description only, no interpretation)

- **AI activity - function:** none named in the artefact; the function is a risk decision produced by Taktile's platform, which the page markets as AI-driven ('adaptive decision-making', ML-based fraud detection).
- **AI activity - element type:** two HTTP-JSON serviceTask calls ('Call decision', 'Get Taktile Result') bound to the vendor's own element templates; no AI-labelled element, no agent element, no model field.
- **Authority - downstream:** the decision determines the branch - 'approve credit' or 'reject credit application' - so an external system's verdict decides the outcome of the application.
- **Authority - data:** not visible - the templates' payload fields are not shown in the capture and the file's configuration refers to template properties rather than literal values.
- **Authority - control:** the exclusive gateway after 'Get Taktile Result'; the polling loop with its 5s timer is a wait control, not a decision control.
- **Authority - control (human):** none drawn - both outcome branches are automated tasks with no user task or review step.
- **Input provenance:** the credit application whose data is sent to the decision call; the payload itself is not published.
- **Guards present:** the polling loop with a fixed 5s interval (a timeout guard is not visible) and the two-way approval gateway.
- **Prompt / model detail visible:** none - no prompt, model or provider appears anywhere; the page offers no model names either.

## Notes for the researcher

Same boundary as the ML-platform connectors (n=142 SageMaker, n=169 Kubeflow), with one difference worth weighing: here the calls carry a *decision* (approve/reject a credit application) rather than a control-plane operation, so the external system's judgement reaches the process outcome. Filed UNCERTAIN so the researcher rules once on connectors whose AI-ness is the called platform's claim rather than the artefact's.
