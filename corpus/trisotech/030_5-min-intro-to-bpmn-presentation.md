# 5 Minute Intro to BPMN — INCLUDE (trisotech)

url: https://www.trisotech.com/5-min-intro-to-bpmn-presentation/
accessed: 2026-09-25
title: 5 Minute Intro to BPMN (presentation deck, 9 slides)
record: 030

bpmn_evidence:
  Slide 7 ("Visual Story of what needs to be done") is a BPMN 2.0 diagram, viewed at full size
  (2048x1152), carrying the BPMN logo and the annotation "**A single visual Knowledge Artefact for
  SMEs and for automation": a black-bordered pool labelled "External participant to the process", a
  start event ("Triggers a new process instance"), the tasks "External Service Task" (gear marker),
  "PMML Predictive Model Task" (P badge), "CQL Clinical Measure Task" (C badge) and "DMN Decision
  Task" (decision-table marker) in sequence, an exclusive gateway ("Routing behavior", annotated
  "Decision prior to routing"), the "CMMN Case Task" branch leading to an Intermediate Message Event
  ("External communication") and an End Event, the "BPMN Subprocess" branch (with the collapsed
  sub-process "+" marker) leading to a second End Event ("Different process outcomes"), and a Data
  Object attached to the sub-process by a dotted data association ("Data mapping", annotated
  "information required as input"). The slide's own footer defines the token semantics: "Token
  semantic: think of a token traversing a path from start to a desired outcome (end)".

ai_evidence:
  The AI element is a task inside the diagram: the "PMML Predictive Model Task" (P badge) between the
  external service task and the CQL clinical measure task. The page's own narration of this slide
  says so in words: "The gear marker here says that this is a service task … The next task is a PMML
  or Predictive Model task (an AI kind of task). Next, we have a CQL task."
  PMML (Predictive Model Markup Language) is the predictive-model interchange standard, so the task
  is an invocation of an ML model inside the process. The AI mention is not a roadmap statement or a
  documentation aside: it is the task itself.

screenshot: 030_5-min-intro-to-bpmn-bpmn-pmml-predictive-task.png
capture_quality: legible

note for the researcher:
  This is the clearest "AI task in a BPMN process" in the teaching material of this source, and the
  vendor labels it as such in prose ("an AI kind of task"). The video page that hosts the same talk
  is recorded separately as record 004 (UNCERTAIN, poster frame only); this record is the deck's own
  diagram, so the two are not duplicates. A reviewer who restricts "AI element" to LLM/generative
  elements rather than ML-model invocations should look at this one first: it is the boundary case.
