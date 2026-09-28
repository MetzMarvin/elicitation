# The Digital Twin: The Living Core of the Case-Decision-Process Methodology — UNCERTAIN (trisotech)

url: https://www.trisotech.com/the-digital-twin-the-living-core-of-the-case-decision-process-methodology/
accessed: 2026-09-25
title: The Digital Twin: The Living Core of the Case-Decision-Process Methodology (blog, Stefaan Lambrecht)
record: 002

bpmn_evidence:
  No BPMN 2.0 artefact on the page. "custom-request-case-data.jpg" (1100x590, viewed at full size) is
  a CMMN case model: a case plan frame with a folder tab ("Business Fulfillment Case Handling"),
  rounded-rectangle stages (Eligibility, Acceptance, Solution Development, Solution Delivery,
  Closing) carrying sentry diamonds labelled Enabled / Completed / Terminated, a task ("Business
  Fulfillment Case Assessment", markers "> #"), and folded-corner case file items ("Process Case
  Input Data", "Incoming Case Data", "Customer Request Digital Twin"). Under the operator's ruling a
  CMMN artefact with no AI element inside the model is E1-not-bpmn.
  "sdmn-data-glue.jpg" (1100x432, viewed at full size) is an SDMN data-structure model: typed entity
  tables (tStructureInsuranceClaim, tStructureClaimData, tStructureClaimHandling,
  tStructureInsuranceClaimEligibility) joined by dashed arrows — a data model, not a decision table.
  Remaining figures: a data-centre render and a decision-table editor UI screenshot.

ai_evidence:
  The page's AI mentions are prose about who contributes to the case data, not elements shown inside
  a model: "Decision information — contributed by human experts, AI agents, or automated decision
  services." and "What is the next best action — for a person, a robot, or an AI agent?". No AI
  marker is visible inside either model in the figures.

screenshot: 002_the-digital-twin-cmmn-case-model.png
capture_quality: legible

question for the researcher (needs_human_ruling):
  SDMN scope. The CMMN case model on this page would be E1-not-bpmn under the standing ruling, but
  the page also publishes an SDMN data-structure model, and SDMN is a notation I cannot place
  (ruling 5 sends SDMN to UNCERTAIN). Is an SDMN data model in scope for the corpus? The page is
  kept as UNCERTAIN so nothing is lost either way; no AI element is visible inside either model.
