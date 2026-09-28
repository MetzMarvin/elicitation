---
n: 792
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: AI-assisted process and case modeling with Flowable Agentic Case Platform
url: https://www.flowable.com/blog/business/ai-assisted-process-and-case-modeling
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "Does this BPMN process contain an AI/LLM element inside it? The generated Order Process (Start Event - user task Enter Order Details - rocket-marked task Perform Credit Check - exclusive gateway Credit Score Check - user task Create Pre-Payment Task - Merge Gateway - user task Confirm Order - End Event) carries Perform Credit Check as a Service Registry Task (httpTask1) invoking operation performCreditCheck, whose model hierarchy entry is Credit Score Service > OpenAPI definition Types, but the Service model tab of that binding is never opened in any figure, so an AI-type service definition (the thing that decided n=787) cannot be ruled out."
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 diagram seen natively in the page asset image-2024-7-18_10-21-44.png ('Order Process' in Flowable Design): start event circle, user tasks with person icons 'Enter Order Details', 'Create Pre-Payment Task', 'Confirm Order', the task 'Perform Credit Check', exclusive gateways with X markers 'Credit Score Check' and 'Merge Gateway', and an end event circle; right panel 'BPMN-Diagram - General', Model Key orderProcessModel. bpmn_evidence_quote: 'BPMN-Diagram - General' / 'orderProcessModel' (labels read at native resolution)"
bpmn_evidence_quote: "BPMN-Diagram - General"
ai_evidence: "Not visible inside the process. The page's AI is the generator: the dialog 'Generate models for AI and import into app', whose Prompt field reads 'Generate an order process with typical steps, including a credit check through an online service which will return a score between 0 and 10 ...'. The only bound task, 'Perform Credit Check', is a Service Registry Task (httpTask1) invoking operation performCreditCheck, with the model hierarchy entry 'Credit Score Service > OpenAPI definition Types'; its Service model tab is never shown, so its service-definition type cannot be read."
ai_evidence_quote: "Generate models for AI and import into app" / "Service Registry Task" / "Perform Credit Check (httpTask1)" / "Credit Score Service" / "OpenAPI definition Types"
artefacts:
  screenshot: 169_able-com-blog-business-ai-assisted-process-and-case-modeling.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1920
capture_method: urllib download of https://images.ctfassets.net/chja9v5uur3u/7e4hMEtO7n7CIo7xcG3sa2/28e925fd4b66f5b9786a357484e2b945/image-2024-7-18_10-21-44.png?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (asset published by the page, the Order Process modeller screenshot); read natively at 2000 px in the visual pass
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** (no alt) | image-2024-7-18_10-21-44.png; (no alt) | image-2024-7-18_10-23-44__1_.png; iStock-1357180459 | fl_ai-early-access_iStock-1357180459_2.jpg
- **OCR labels of the captured figure:** Flowable | Editing | Workspaces | Default | OrderProcessv | Overview | Models | DESIGN | Order Process | Searchforaproperty | BPMN-Diagram-General | Model Key: | Filter byname | orderProcessModel | Create Pre- | Payment Task
- **Page text quote:** AI-assisted process and case modeling with Flowable Agentic Case Platform
- **Captured asset:** https://images.ctfassets.net/chja9v5uur3u/7e4hMEtO7n7CIo7xcG3sa2/28e925fd4b66f5b9786a357484e2b945/image-2024-7-18_10-21-44.png?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (1920x913)

## Sighted observations (visual pass elicitation-aa, shard s5, 2026-09-25)

Looked at all three content figures natively (the census capture among them); the two
2800x1576 Contentful promo illustrations and the iStock photo are the site-wide images
seen on the sibling posts of this shard.

- **Figure 1 - the AI generator, outside any process.** `2kXn8be1_image-2024-7-18_10-20-27.png`
  is the dialog **"Generate models for AI and import into app"**, tabs Generate / Generated
  apps, Templates (Process - "Generate a process fetching weather information from an online
  source", Process - "Generate a typical loan application process"), **Generator Name
  "Order Process"** and **Prompt** "Generate an order process with typical steps, including a
  credit check through an online service which will return a score between 0 and 10 and when
  the score is below 5, create an additional task for a pre-payment." This is AI that
  **authors** a model, which the brief puts outside the process.
- **Figure 2 - the generated BPMN 2.0 process.** `7e4hMEtO_image-2024-7-18_10-21-44.png`
  (the census capture) is Flowable Design on model **Order Process**: start event circle ->
  user task (person icon) **"Enter Order Details"** -> task **"Perform Credit Check"** (small
  marker in its top-left corner, the same **rocket** glyph seen on n=787) -> exclusive
  gateway (X) "Credit Score Check" -> user task **"Create Pre-Payment Task"** -> exclusive
  gateway "Merge Gateway" -> user task **"Confirm Order"** -> end event circle. The right
  panel is **"BPMN-Diagram - General"** (Model Key `orderProcessModel`, Name "Order Process",
  Creation date 6/27/2024), and the model hierarchy lists Order Process > **Credit Score
  Service** > **OpenAPI definition Types**, Confirm Order Form, Create Pre-Payment Task Form,
  Enter Order Details Form. The palette lists Start event / User task / Subprocess / Call
  activity / Case task / Exclusive gateway, with User task, Service task, Call activity,
  Exclusive gateway as favourites.
- **Figure 3 - the binding, and what it leaves open.** `56DAB7bX_image-2024-7-18_10-23-44__1_.png`
  is the **"Service Registry Task - Perform Credit Check (httpTask1)"** configuration, tabs
  **Service model / Operation / Input / Output / Error handling**; the visible tab is
  **Input**, mapping `${customerInformation.firstName}`, `.lastName`, `.street`, `.zipCode`,
  `.city`, `.country` to the `performCreditCheck` parameters (all typed String). The side text
  explains "A service registry model is a reusable model that describes how an external
  service or a custom script can be invoked to produce data".
- **Why UNCERTAIN rather than E2.** The page's AI is the model generator, and the only bound
  task's visible binding points at an external/OpenAPI service, which would make this a plain
  `E2-no-ai-element`. But the **Service model** tab - the one place that would show whether
  "Credit Score Service" is a service definition of type **"AI"**, exactly the evidence that
  decided n=787 - is never opened in any published figure, and the rocket marker on this task
  is the same glyph that marked the AI-bound tasks on n=787. Per CLAUDE.md an element whose
  implementation might be AI-bound but is not visible is UNCERTAIN, never E2, so the verdict
  is UNCERTAIN with the question above.
- **Nothing else on the page.** The post describes generating case models as well, but no
  CMMN figure is published here; only these three content figures exist.

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process. (Now settled by sight;
the remaining question is the service-definition type of "Credit Score Service".)
