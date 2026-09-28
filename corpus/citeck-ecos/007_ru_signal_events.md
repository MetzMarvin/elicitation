---
n: 7
source: citeck-ecos
source_name: Citeck ECOS (citeck-ecos.readthedocs.io)
title: Сигналы — Citeck
url: https://citeck-ecos.readthedocs.io/ru/develop/settings_kb/processes/ecos_bpmn/editor/components/events/ecos_bpmn_components_signal.html
accessed: 2026-09-25
verdict: UNCERTAIN
row: 957
needs_human_ruling: true
question: null
needs_visual_check: true
bpmn_evidence: screenshot
bpmn_evidence_quote: "a BPMN canvas of the signal-event example whose many nested element labels are too small to check for an AI name"
ai_evidence: none readable at the available resolution - not verified
ai_evidence_quote: "unresolved"
artefacts:
  screenshot: corpus/citeck-ecos/007_ru_signal_events_bpmn_start_event_example.png
  assets:
    - 
  bpmn_xml: null
  archive: null
duplicate_of: null
access: public
capture_source: page asset (raw figure set, visual backstop pass)
capture_quality: poor
capture_width_px: 431x169
capture_method: downloaded from the docs page's _images directory
---

## What the page shows

Сигналы — Citeck. The backstop pass over the 765 raw figures of this source found this figure on the page:
a BPMN canvas of the signal-event example whose many nested element labels are too small to check for an AI name.

## Observations (description only, no interpretation)

The figure is BPMN 2.0 in notation (tasks, events and gateways in BPMN shapes) but no element
label can be read at the asset's own resolution, so neither the presence nor the absence of an
AI/LLM-labelled element inside the process can be established from the image.

Page text quoted in the census row: "Сигналы - События Citeck реализуются через сигналы. Каждый сигнал — глобальное событие, передающееся всем активным обработчикам."

## Notes for the researcher

The census excluded this row without a visual check of this figure. CLAUDE.md rule 5 makes an
unresolved image UNCERTAIN, never an exclusion, so the row is superseded rather than left as it
was. This is a readability limit, not a notation question: opening the live page and zooming past
the asset's own resolution is the only way to settle it.

**Researcher question (also in the ledger row):** 957_bpmn_start_event_example.png is certainly BPMN but its nested element labels cannot be read at the asset's own resolution, so the row's E0-no-artefact verdict is wrong and no AI verdict can be entered from the image. Is a single component example figure an artefact for the corpus (same question as row 368), and does it carry an AI element?
