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

- [x] Implement Listen and Repeat coaching with audio-capability fallbacks.
- [x] Implement Take an Interview coaching.
- [x] Define pronunciation, fluency, and content evidence boundaries.
- [x] Validate transcript-only limitation disclosures.

**Exit:** both Speaking modules behave safely with audio, transcript, and missing-modality inputs.

## 4 — Reading and Listening v0.4.0

- [x] Implement the three Reading task modules.
- [x] Implement the four Listening task modules.
- [x] Build an originality review for generated passages, scripts, and questions.
- [x] Test accessibility alternatives for audio-dependent practice.

**Exit:** all seven receptive-skill modules pass behavior, originality, and accessibility checks.

## 5 — Learning intelligence v0.5.0

- [x] Define a privacy-preserving, opt-in learner-state schema.
- [x] Add diagnostic assembly and study-plan generation.
- [x] Add spaced-review recommendations and progress summaries.
- [x] Test state portability across supported hosts.

**Exit:** learners can continue a plan without hidden or mandatory data collection.

## 6 — Quality and multi-platform release

- [ ] Add automated behavior runners for maintained agent hosts.
- [ ] Evaluate across proficiency levels and adversarial integrity requests.
- [ ] Complete accessibility, privacy, copyright, and trademark reviews.
- [ ] Select an independent brand and migrate the repository identifier.
- [ ] Publish installation guides and a versioned release checklist.
- [ ] Add security reporting, protected review rules, scanning, checksums, and release provenance.

**Exit:** release gates pass in at least two maintained agent environments and the branding blocker is closed.

## 7 — Public v1.0.0

- [ ] Publish a signed/tagged release with reproducible validation results.
- [ ] Open contribution pathways and governance expectations.
- [ ] Document issue triage and format-update response time.
- [ ] Announce the release without implying ETS affiliation.

**Exit:** stable release is installable, documented, source-traceable, and supported by public evaluations.

## 8 — Adoption and community v1.5

- [ ] Launch an independent multilingual website with clear installation paths and limitations.
- [ ] Add guided installation for maintained agent hosts.
- [ ] Establish maintainer governance, moderation, contribution ladders, and a teacher advisory circle.
- [ ] Publish a public evaluation dashboard and dated format-change watch.
- [ ] Add reviewed localization infrastructure and ethical sharing/referral loops.

**Exit:** learners and teachers can discover, install, trust, and improve the project without founder assistance.

## 9 — Hosted learner platform v2.0

- [ ] Build web-first onboarding with account-optional trial use.
- [ ] Define the age policy and complete child-privacy review before account launch.
- [ ] Add consented sync, export, deletion, recovery, and privacy-preserving product analytics.
- [ ] Implement adaptive planning, managed audio workflows, and original full-mock orchestration.
- [ ] Add accessible progress views, reminders, observability, cost controls, and incident response.
- [ ] Run a diverse learner pilot and establish activation, retention, learning, trust, and cost baselines.

**Exit:** pilots demonstrate repeat learning value and acceptable reliability, privacy, safety, accessibility, latency, and cost-to-serve.

## 10 — Educator platform and paid pilots v2.5

- [ ] Add teacher workspaces, assignments, review queues, cohorts, and learner-controlled sharing.
- [ ] Build original-content authoring and quality-review workflows.
- [ ] Define organization roles, audit history, retention controls, and support boundaries.
- [ ] Pilot with qualified teachers and a small, diverse set of schools.
- [ ] Test Free, Pro, Educator, and Institution packaging without weakening the free core.

**Exit:** educator pilots show repeat use, actionable learning value, manageable support demand, and no unresolved high-severity privacy or access-control findings.

## 11 — Sustainable Pro v3.0

- [ ] Launch transparent paid packages for hosted continuity, advanced computation, collaboration, administration, and support.
- [ ] Add trials, cancellation, refunds, regional pricing, scholarships, and user-controlled data export/deletion.
- [ ] Measure cost per completed learning loop, paid retention, support burden, and gross margin.
- [ ] Protect the free-core covenant and publish commercial-boundary changes.

**Exit:** revenue sustains the service without reducing free access, trust, or learning quality.

## 12 — Open ecosystem v4.0

- [ ] Publish an extension SDK and automated compatibility suite.
- [ ] Launch a verified registry for adapters, original content packs, evaluators, and classroom integrations.
- [ ] Define provenance, permissions, review levels, versioning, security reporting, and removal rules.
- [ ] Establish fair contributor and partner pathways with portable learner data.

**Exit:** third-party extensions can be discovered, verified, upgraded, and revoked without fragmenting learner safety or core compatibility.

## 13 — Global reference ecosystem

- [ ] Establish multilingual learner, teacher, accessibility, and research councils.
- [ ] Publish open evaluation protocols, longitudinal limitations, transparency reports, and format-change history.
- [ ] Validate learning outcomes through privacy-respecting research collaborations.
- [ ] Create independent educator certification without implying ETS authorization.
- [ ] Expand scholarships, nonprofit partnerships, and low-bandwidth access.

**Exit:** global leadership is supported by reproducible learning evidence, resilient governance, and community trust.

The strategic rationale, free/paid covenant, product layers, KPIs, and decision gates are defined in [Product strategy](PRODUCT-STRATEGY.md). Source-backed platform, IP, privacy, community, and security findings are in [Global ecosystem strategy research](research/ecosystem-strategy-2026-10-12.md).

## GitHub tracking

| Stage | Tracking issues |
|---|---|
| Human calibration | [#19](https://github.com/arminazimi/toefl-coach-ai/issues/19) |
| Trusted public v1 | [#14](https://github.com/arminazimi/toefl-coach-ai/issues/14), [#17](https://github.com/arminazimi/toefl-coach-ai/issues/17), [#7](https://github.com/arminazimi/toefl-coach-ai/issues/7) |
| Adoption and community v1.5 | [#20](https://github.com/arminazimi/toefl-coach-ai/issues/20) |
| Hosted learner platform v2.0 | [#21](https://github.com/arminazimi/toefl-coach-ai/issues/21) |
| Educator platform v2.5 | [#22](https://github.com/arminazimi/toefl-coach-ai/issues/22) |
| Sustainable Pro v3.0 | [#23](https://github.com/arminazimi/toefl-coach-ai/issues/23) |
| Open ecosystem v4.0 | [#24](https://github.com/arminazimi/toefl-coach-ai/issues/24) |
| Global reference ecosystem | [#25](https://github.com/arminazimi/toefl-coach-ai/issues/25) |

## Community — ongoing

- [ ] Triage learner, teacher, and contributor feedback.
- [ ] Monitor official ETS changes and update facts with citations.
- [ ] Expand language accessibility and contributor coverage.
- [ ] Publish calibration limitations and evaluation regressions transparently.
- [ ] Track activation, retained learning loops, verified retry improvement, and trust guardrails.
- [ ] Keep free-core quality and accessibility protected as hosted and paid products grow.
