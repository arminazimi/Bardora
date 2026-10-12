# Roadmap

Each phase has a checkable exit condition. GitHub issues track the work; this file records the durable sequence and scope.

## 0 — Research and requirements

- [x] Define target users, MVP, exclusions, integrity boundaries, and success measures.
- [x] Record the January 2026 task types from official ETS sources.
- [ ] Review all product claims against the latest ETS publications before release.

**Exit:** PRD and source-cited task matrix are reviewed.

## 1 — Foundation v0.1.0

- [x] Define the portable skill entry point and coaching contract.
- [x] Define architecture, stable task IDs, and extension seams.
- [x] Add offline repository tests and core behavior cases.
- [x] Run independent behavior evaluations in at least one agent host.

**Exit:** clean-clone tests pass and the core loop satisfies representative evaluations.

## 2 — Writing v0.2.0

- [x] Implement Build a Sentence coaching and evaluations.
- [x] Implement Write an Email coaching and evaluations.
- [x] Implement Write for an Academic Discussion coaching and evaluations.
- [ ] Review feedback against public ETS guidance with human raters or qualified educators.

**Exit:** all Writing task modules pass behavior and originality checks.

## 3 — Speaking v0.3.0

- [ ] Implement Listen and Repeat coaching with audio-capability fallbacks.
- [ ] Implement Take an Interview coaching.
- [ ] Define pronunciation, fluency, and content evidence boundaries.
- [ ] Validate transcript-only limitation disclosures.

**Exit:** both Speaking modules behave safely with audio, transcript, and missing-modality inputs.

## 4 — Reading and Listening v0.4.0

- [x] Implement the three Reading task modules.
- [x] Implement the four Listening task modules.
- [x] Build an originality review for generated passages, scripts, and questions.
- [x] Test accessibility alternatives for audio-dependent practice.

**Exit:** all seven receptive-skill modules pass behavior, originality, and accessibility checks.

## 5 — Learning intelligence v0.5.0

- [ ] Define a privacy-preserving, opt-in learner-state schema.
- [ ] Add diagnostic assembly and study-plan generation.
- [ ] Add spaced-review recommendations and progress summaries.
- [ ] Test state portability across supported hosts.

**Exit:** learners can continue a plan without hidden or mandatory data collection.

## 6 — Quality and multi-platform release

- [ ] Add automated behavior runners for maintained agent hosts.
- [ ] Evaluate across proficiency levels and adversarial integrity requests.
- [ ] Complete accessibility, privacy, copyright, and trademark reviews.
- [ ] Select an independent brand and migrate the repository identifier.
- [ ] Publish installation guides and a versioned release checklist.

**Exit:** release gates pass in at least two maintained agent environments and the branding blocker is closed.

## 7 — Public v1.0.0

- [ ] Publish a signed/tagged release with reproducible validation results.
- [ ] Open contribution pathways and governance expectations.
- [ ] Document issue triage and format-update response time.
- [ ] Announce the release without implying ETS affiliation.

**Exit:** stable release is installable, documented, source-traceable, and supported by public evaluations.

## Community — ongoing

- [ ] Triage learner, teacher, and contributor feedback.
- [ ] Monitor official ETS changes and update facts with citations.
- [ ] Expand language accessibility and contributor coverage.
- [ ] Publish calibration limitations and evaluation regressions transparently.
