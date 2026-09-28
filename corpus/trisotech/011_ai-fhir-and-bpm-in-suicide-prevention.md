# AI, FHIR, and BPM+ in Suicide Prevention: From Early Detection to Coordinated Care (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/ai-fhir-and-bpm-in-suicide-prevention/
accessed: 2026-09-25
title: AI, FHIR, and BPM+ in Suicide Prevention: From Early Detection to Coordinated Care (webinar recording)
record: 011

bpmn_evidence:
  The artefact is the recording, and the recording could not be played without signing in.
  The page publishes one content image, the video's poster frame
  (011_ai-fhir-and-bpm-in-suicide-prevention-poster-frame.png), viewed at full size; no diagram
  is published on the page itself.
  The page's own notation sentence: "This session explores how AI-powered monitoring, BPM+ visual standards, and FHIR interoperability work together to detect suicidal ideation early and coordinate interventions across emergency departments, mental health specialists, and primary care."
  The same talk is also published as a slide deck at
  /ai-fhir-and-bpm-in-suicide-prevention-presentation/, judged separately on its own slides.
  The recording was not watched, because the player refuses to play it (see the gate below).

ai_evidence:
  "This session explores how AI-powered monitoring, BPM+ visual standards, and FHIR interoperability work together."

gate on the recording (why this one video of the 22 could not be inspected at all):
  The YouTube player returns, in its own words, "Viewer discretion is advised" and offers only
  "Watch on YouTube" - the embed's response to a video whose playback is gated on the viewer's
  account. On the embed route the element never loads a stream (`readyState` 0, `duration` NaN,
  `videoWidth` 0) on both https://www.youtube.com/embed/ and https://www.youtube-nocookie.com/embed/
  with the Referer header naming the embedding page; on the watch page the title resolves
  ("AI, FHIR, and BPM+ in Suicide Prevention: From Early Detection to Coordinated Care") but the
  player never becomes ready either, and the call that tried to start it had to be killed after
  120 s. Nothing was clicked: confirming a discretion/age gate is an access action, and no
  signed-in session was staged. This is recorded as an operator action (sources/OPERATOR-TODO.md P9)
  so that the frames can be captured later from a staged session; the row stays UNCERTAIN rather
  than BLOCKED because the page itself was fully screened and its artefact is a frame of a video
  that a session would reveal, exactly like the other 21 rows of this class.

screenshot: 011_ai-fhir-and-bpm-in-suicide-prevention-poster-frame.png
capture_quality: null

question for the researcher (needs_visual_check):
  The artefact is a video frame. This is the recording of the talk whose written version (the blog
  "Suicide Prevention with Modeling Tools") is already in the corpus as record 001 with a BPMN
  figure carrying an LLM task, so the recording may show more of the same models. The video is
  gated by "Viewer discretion is advised" and could not be seeked at all from an anonymous
  session, so unlike the other 21 video rows there are no frames to read here - only the poster
  frame. Either a staged signed-in session captures it (see OPERATOR-TODO P9), or the operator
  rules the recording family out of scope.
