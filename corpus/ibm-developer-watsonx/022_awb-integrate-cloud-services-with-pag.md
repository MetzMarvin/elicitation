---
n: 923
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Integrate cloud services with Privileged Access Gateway (PAG) - the figure the page's own alt text calls a 'State Diagram' (a client-to-cloud connection picture with five numbered connectors)"
url: https://developer.ibm.com/tutorials/awb-integrate-cloud-services-with-pag/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's own alt text names its figure a 'State Diagram', but the drawing is a client-to-cloud connection picture: a 'Client' panel with an 'Openvpn client' box against an 'IBM cloud' panel holding a VPC with 'VPN service', 'PAG service', 'VSI host 1', 'VSI host 2' and a 'Cloud Object Storage bucket', joined by five numbered connectors that spell out the onboarding procedure ('1) Establish VPN tunnel to VPN service from client to access VPC resources', '2) Client establishes connection to PAG service through VPN tunnel', '3a.) Client interacts with PAG service ...', '4) PAG service pushes session recording to COS bucket', '5) Add IAM id of user to be onboarded directly to VSI hosts'). Its boxes are systems, so an architecture reading makes it E0-no-artefact; its numbered connectors order the steps of a procedure, so a process reading makes it a non-BPMN process figure. Should this page's one drawn figure enter the corpus? (The page carries 19 figure records and no other is named as a process by its alt text.)"
needs_visual_check: false
bpmn_evidence: "png, the page's own figure at full size (SHEET_Z0701, second tile; contact sheet SHEET_GAP0701, row 3 col 1). the page's own alt text calls it a 'State Diagram'. It draws a 'Client' panel holding an 'Openvpn client' box, and an 'IBM cloud' panel holding a 'VPC' with 'VPN service', 'PAG service', 'VSI host 1', 'VSI host 2' and a 'Cloud Object Storage bucket', joined by numbered connectors: '1) Establish VPN tunnel to VPN service from client to access VPC resources', '2) Client establishes connection to PAG service through VPN tunnel', '3a.) Client interacts with PAG service. Login to VSI, issue commands to VSI. VSI will start recording', '4) PAG service pushes session recording to COS bucket', '5) Add IAM id of user to be onboarded directly to VSI hosts'."
bpmn_evidence_quote: "PAG is one of the solutions offered under IBM Cloud Security Network Access Guidance."
ai_evidence: "there is no AI, LLM or agent element anywhere on the page and none drawn inside the figure: the page is about reaching VSI hosts through a VPN and a Privileged Access Gateway, and its figure's boxes are network services (Openvpn client, VPN service, PAG service, VSI hosts, Cloud Object Storage bucket). So this is the same code-list situation as records 003 and 017 - the artefact may be a process figure and E2-no-ai-element cannot be applied as written, because E2 requires quoting the AI mention being dismissed and there is none to quote."
ai_evidence_quote: "PAG is one of the solutions offered under IBM Cloud Security Network Access Guidance."
artefacts:
  screenshot: 022_923_state-diagram-pag-2.png
  assets: [022_923_state-diagram-pag-2.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/tutorials/awb-integrate-cloud-services-with-pag/` (api, ledger row n=923), figure `figs/923_state-diagram-pag-2`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own figure at full size (SHEET_Z0701, second tile; contact sheet SHEET_GAP0701, row 3 col 1). the page's own alt text calls it a 'State Diagram'. It draws a 'Client' panel holding an 'Openvpn client' box, and an 'IBM cloud' panel holding a 'VPC' with 'VPN service', 'PAG service', 'VSI host 1', 'VSI host 2' and a 'Cloud Object Storage bucket', joined by numbered connectors: '1) Establish VPN tunnel to VPN service from client to access VPC resources', '2) Client establishes connection to PAG service through VPN tunnel', '3a.) Client interacts with PAG service. Login to VSI, issue commands to VSI. VSI will start recording', '4) PAG service pushes session recording to COS bucket', '5) Add IAM id of user to be onboarded directly to VSI hosts'.

## AI evidence (why this is not an E2 exclusion)

there is no AI, LLM or agent element anywhere on the page and none drawn inside the figure: the page is about reaching VSI hosts through a VPN and a Privileged Access Gateway, and its figure's boxes are network services (Openvpn client, VPN service, PAG service, VSI hosts, Cloud Object Storage bucket). So this is the same code-list situation as records 003 and 017 - the artefact may be a process figure and E2-no-ai-element cannot be applied as written, because E2 requires quoting the AI mention being dismissed and there is none to quote.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
