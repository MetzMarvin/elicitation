---
source: imixs
source_name: Imixs-Workflow (Imixs-AI module, Open-BPMN; blog.imixs.org, imixs.org, imixs.com)
source_type: open-source vendor blog + docs
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: NO (operator ruling 2026-09-24: checked, dropped; no 2nd channel)
access: public
population_type: enumerable
population_estimate: 20
effort: small
needs_logged_in_browser: false
status: OUT-C4 (operator ruling; not surveyed; kept for audit trail)
---

## Criteria evidence

- **C1 YES**: https://blog.imixs.org/2026/01/17/ai-agents-vs-ai-augmented-workflows/
  (2026-09-24): "At Imixs we have already published the Imixs-AI module, allowing you to
  integrate LLMs directly into your workflows." And: "It is integrated into the process flow
  through BPMN annotations."
- **C2 YES**: same post: "Imixs-Workflow is an open-source project for building
  transactional, secure, and transparent business applications based on the BPMN 2[.0
  standard]"; "The BPMN model defines which steps are carried out in which order."
- **C3 YES**: public blog and docs.
- **C4 UNCLEAR**: a small German open-source vendor. See the general C4 rule (B5–B7).

## Promotion mode (to verify in Pass 2)

The LLM binding is configured in the BPMN model's **annotations / event definitions**
(Imixs models are event-driven: tasks are states, events are transitions). If confirmed,
this is a distinct mode: **AI bound by model configuration on an event**, rather than by a
dedicated AI task type or by delegated implementation.

## Entry points

- The anchor blog post
- Google result titles (q26), **not opened**: "Imixs-AI - LLM Tool Calling"
  (2026/02/21), "Introducing new Imixs AI Assistant Adapter" (2025/10/02), "Imixs-AI
  Version 1.1.0 Released" (2024/10/13), "Revolutionizing Business Process Management with
  AI" (2024/06/14), "Open-BPMN - New Release!" (2026/03/21), "BPM im Zeitalter von KI"
  (imixs.com)
- `imixs.org/doc/...`: Imixs docs. An Imixs-AI section is likely. Find it via nav.

## Enumeration instructions

1. Enumerate the blog's archive or its AI category/tag (check for a `sitemap.xml` or tag
   index first).
2. Enumerate the Imixs-AI docs section and the `imixs/imixs-ai` GitHub repo (**not
   verified**; find it via links). Look for `.bpmn` example models.
3. Do not keyword-filter the blog archive.

## Artefact mechanics

- The blog uses ASCII-art flow diagrams in `<pre>` blocks (seen in the anchor post). Those
  are **not** BPMN; name them `E1-not-bpmn` ("ASCII flow sketch").
- Open-BPMN is Imixs's own Eclipse/VS Code BPMN modeller. Screenshots from it are genuine
  BPMN 2.0.

## Known gotchas

- The `claude-in-chrome` privacy filter may block text output. Strip URL-like tokens first.
- German-language content on imixs.com is in scope (banned reason: "not in English").

## Spot checks performed by Pass 1

- Anchor blog post: opened and quoted.

## RESUME

(empty)
