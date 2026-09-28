---
n: 169
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Kubeflow Connector
url: https://marketplace.camunda.com/apps/423548/kubeflow-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing is filed under the marketplace's 'AI Services' category and its connector drives Kubeflow, an ML platform, but the published canvas shows a single control-plane call ('Create Experiment', Kubeflow API 'Pipelines v1', namespace 'default-namespace') between a start and an end event, and the page's own prose names no AI, LLM or model. Is an ML-platform connector task an AI element inside the process, or is this E2-no-ai-element? Same boundary as the Amazon SageMaker connector (n=142), which was recorded UNCERTAIN for the same reason.
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, canvas with the properties panel open on the task); no .bpmn downloadable. Read natively: start event -> serviceTask 'Create Experiment' (selected, with the element-template glyph visible and the usual element actions around it) -> end event.
bpmn_evidence_quote: "Create Experiment"
ai_evidence: The listing's only AI signal is the marketplace's own category facet: the page carries 'AI Services' twice as an attribute tag and lists 'AI Services' under 'Associated Product Group Categories'. Its prose names no AI, LLM or model: 'The Kubeflow Connector allows processes to interact with Kubeflow pipelines.' The operation visible in the open properties panel is a control-plane call - template 'KUBEFLOW CONNECTOR' / 'Create Experiment', 'Kubeflow API: Pipelines v1', operation 'Create Experiment', namespace 'default-namespace' - while the page says the connector can also 'trigger pipelines both synchronously and asynchronously and consume their output in the subsequent steps of the process'. Kubeflow pipelines are ML workloads, but this artefact shows a pipeline-management call, not a model invocation.
ai_evidence_quote: "The Kubeflow Connector allows processes to interact with Kubeflow pipelines"
artefacts:
  screenshot: 169_kubeflow-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/423548/overview/img5614624664835834355-2x.png, 1100x614); native read at full size - a Camunda Web Modeler canvas with the task's properties panel open
---

## What the page shows

The Kubeflow Connector (viadee, outbound connector). The listing publishes one model in the Camunda Web Modeler, whose single service task calls the Kubeflow API; the page's feature list covers pipeline, experiment and run management (get, start, monitor) plus API version compatibility.

## Observations (description only, no interpretation)

- **AI activity - function:** none drawn. The task is a pipeline/experiment management call; the page says the connector can trigger pipelines, which would run ML workloads, but no such call is shown.
- **AI activity - element type:** one ordinary `serviceTask` labelled 'Create Experiment' bound to the vendor's Kubeflow connector template; no agent element, no ad-hoc container, no model slot.
- **Authority - downstream:** the end event - the published model has no branch after the connector call.
- **Authority - data:** the panel shows the namespace and experiment name fields; no data objects are drawn.
- **Authority - control:** none - no gateway in the published model.
- **Authority - control (human):** none in the model; the page's documentation link is an external GitHub README.
- **Input provenance:** the experiment parameters configured in the panel (name, description, HTTP headers).
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none - no model, prompt or inference configuration appears; the visible operation creates an experiment rather than invoking a model.

## Notes for the researcher

Recorded UNCERTAIN to keep one boundary decision in one place: an ML-platform connector whose visible operation is management rather than inference. The artefact itself is legible and complete, so this is not a capture-quality question - it is whether 'AI Services' as a catalogue facet, plus a platform that runs ML workloads, is enough when the drawn task calls the control plane.
