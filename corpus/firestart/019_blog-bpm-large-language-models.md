---
n: 403
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
title: BPM & Large Language Models - FireStart Ressourcen
url: https://www.firestart.com/blog/bpm-large-language-models
accessed: 2026-09-27
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: raster export of a BPMN 2.0 process diagram served by the page (task rectangles with type glyphs, diamond gateways, event circles)
bpmn_evidence_quote: "BPM-Prozess inkl. OpenAI-Aktivität"
ai_evidence: an activity bound to OpenAI sits inside the process and the LLM is addressed over an API
ai_evidence_quote: "In einem automatisierten Prozess kommunizieren wir mit dem LLM ueber eine API-Schnittstelle."
artefacts:
  screenshot: 019_blog-bpm-large-language-models.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1344
capture_method: the process export as the page serves it, downloaded once and re-encoded to png
---

## What the page shows

The diagram depicts customer inquiry: external form, OpenAI activity, quote proposal, Outlook notification. The page carries one process export, whose alt text reads "BPM-Prozess inkl. OpenAI-Aktivität".
The page states: "All das lässt sich zum Beispiel in der unternehmenseigenen Microsoft Azure OpenAI Umgebung realisieren, sodass die Daten dabei nur in den regionalen Datenzentren GDPR konform verarbeitet werden. Im Bereich der Klassifizierung bieten LLMs gegenüber klassischen Machine Learning und Deep Learning ..."

## Observations (description only, no interpretation)

- **AI activity - function:** "In einem automatisierten Prozess kommunizieren wir mit dem LLM ueber eine API-Schnittstelle."
- **AI activity - element type:** an activity bound to OpenAI sits inside the process and the LLM is addressed over an API
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed on the page
- **Prompt / model detail visible:** the page names the model and the integration (see the notes below)

## Notes for the researcher

BPMN 2.0 process export with an AI-bound task inside the process

