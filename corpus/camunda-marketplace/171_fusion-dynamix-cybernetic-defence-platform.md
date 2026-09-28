---
n: 171
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Fusion Dynamix - Cybernetic Defence Platform
url: https://marketplace.camunda.com/apps/773510/fusion-dynamix---cybernetic-defence-platform
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN published as the listing's own overview asset - a Camunda Operate view of a running instance ('Process Instance: 2251799814612732', started 28/07/2026, duration '1H 5M'). Read natively: start event -> 'Capture carrier with issue' -> ad-hoc sub-process 'Supplier Logistics Helper Agent' (holding 'Request manual review of carrier sub suitability', 'Request Manual Review and Execution', 'Validate Carrier quality' and 'Additional Helper', with the ad-hoc '~' marker at its foot) -> 'Review action assessment' -> end event; the other published screenshots are the same listing's Operate 'Agentic Orchestration' views, which list the deployed process definitions 'Supplier Logistics Helper' (v1, v2) and 'Supplier Threat Detection AI Process' (v1, v2, ID 'SupplierThreatAIProcess').
bpmn_evidence_quote: "Supplier Logistics Helper Agent"
ai_evidence: Two layers. In the drawn process, the ad-hoc sub-process that carries the work is named 'Supplier Logistics Helper Agent' and holds 'helper' tasks - the same shape as Camunda's agentic ad-hoc containers elsewhere in this source. In the same listing's Operate views the deployed definitions include 'Supplier Threat Detection AI Process' (v1 and v2, ID 'SupplierThreatAIProcess'), i.e. an AI-named process in the same deployment. The page's own copy claims the capability: 'Agentic orchestration - Embed policy-defined rules into autonomous actions to enable cryptographically secure responses without losing human oversight'.
ai_evidence_quote: "Embed policy-defined rules into autonomous actions to enable cryptographically secure responses without losing human oversight"
artefacts:
  screenshot: 171_fusion-dynamix-cybernetic-defence-platform.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/773510/overview/img3607764769915555324-2x.png 1067x660 and screenshot/img12738043771582945950.png 1500x942, img17243952608095388440.png 1500x943); all read natively at full size (the 8 screenshots are published as 750/1500 px pairs); the remaining screenshots are the vendor's own dashboards, not process artefacts
---

## What the page shows

Blue Nebula's Fusion Dynamix - Cybernetic Defence Platform (partner blueprint, tagged BPMN). The listing publishes one BPMN process (an Operate instance view of a carrier-issue resilience flow built around an agent container) plus eight screenshots of the vendor's own resilience dashboards and Operate views.

## Observations (description only, no interpretation)

- **AI activity - function:** an agent container ('Supplier Logistics Helper Agent') in the drawn process, and an AI-named process definition ('Supplier Threat Detection AI Process') in the same deployment.
- **AI activity - element type:** an `adHocSubProcess` named as an agent, holding four tasks; no element-template binding and no model or provider is visible in the published views (the AI process itself is never drawn).
- **Authority - downstream:** 'Review action assessment' after the agent container, and the end event of the instance view.
- **Authority - data:** none drawn; the Operate view shows the instance id and duration only.
- **Authority - control:** none inside the drawn process - the agent container is a single step between 'Capture carrier with issue' and 'Review action assessment'.
- **Authority - control (human):** 'Review action assessment' - a user task after the agent container, i.e. a human step downstream of the agent.
- **Input provenance:** the carrier issue captured in the first task.
- **Guards present:** none drawn inside the process; the vendor's dashboard screenshots show SLA, cost and escalation configuration outside the model.
- **Prompt / model detail visible:** none - the published views show no model, provider, prompt or agent template.

## Notes for the researcher

The listing is tagged BPMN and does publish one real BPMN artefact, but the AI evidence is distributed: the agent container sits in the drawn process while the AI-named process appears only in the Operate lists. Flagged for judgement rather than recorded silently, because a reviewer could reasonably ask for a template binding on 'Supplier Logistics Helper Agent' before counting it, and because most of this listing's published images are the vendor's own dashboards rather than process artefacts.
