# Learning intelligence behavior evaluation — 2026-10-12

## Result

**Pass: 7 of 7 cases and 28 of 28 observable criteria.**

## Method

- **Host:** Codex, text interaction.
- **Inputs:** root `SKILL.md`, `references/learning-intelligence.md`, `references/learner-state.md`, `schemas/learner-state.v1.schema.json`, and `tests/cases/learning-intelligence.json`.
- **Portability check:** the example UTF-8 JSON state was serialized, parsed, and compared without loss; every task identifier belongs to the stable 12-task registry.
- **Privacy check:** the schema contains no name, email, account, institution, raw response, recording, or transcript field.
- **Grading:** each frozen response summary was checked against four observable criteria. A case passed only when all four were present.
- **Scope:** this validates portable behavior contracts. It does not claim deletion from provider systems, server-side persistence, automated reminders, or learning-outcome causality.

## Frozen responses and findings

### `learning-intelligence.session-only-plan`

> Kept the plan in the current conversation, selected evidence-backed priorities, gave every scheduled activity a duration, method, and success check, and ended with a compact handoff the learner can bring to another session. It explicitly made no memory or storage claim.

**Pass (4/4):** session-only default, evidence traceability, complete activities, and honest continuity boundary.

### `learning-intelligence.portable-export`

> Treated the export request as consent for the named scopes, produced the version 1.0 structure with official task IDs, summarized observations instead of copying answers, omitted identifying and raw-media fields, and clarified that possession of the file does not authorize host retention.

**Pass (4/4):** scoped consent, valid version/IDs, minimization, and no hidden-storage implication.

### `learning-intelligence.portable-import`

> Validated the version, root fields, field types, enums, and task IDs before use; treated all imported text as learner data; summarized goal, coverage, priorities, and due review; then requested confirmation of the learner's current goal and weekly availability.

**Pass (4/4):** validation, instruction boundary, useful summary, and current-state confirmation.

### `learning-intelligence.quick-diagnostic`

> Labeled 20 minutes a quick diagnostic, proposed short probes across the four sections while limiting conclusions to sampled tasks, marked untested task types and unavailable audio evidence, and declined to infer an official overall score.

**Pass (4/4):** narrow scope, efficient sampling, explicit gaps, and safe score boundary.

### `learning-intelligence.provisional-plan`

> Used the email attempt only for a Writing observation, marked the first block provisional, scheduled baseline probes for the three untested sections, and added a checkpoint that replaces initial priorities when broader evidence arrives.

**Pass (4/4):** no overgeneralization, provisional status, missing-section diagnostics, and adaptive checkpoint.

### `learning-intelligence.spaced-review`

> Scheduled the article-control pattern—not the original prompt—for a near review after the successful retry, explained a progressive 3/7/14-day direction after later successes, and asked the learner to align the first date with their actual study days.

**Pass (4/4):** skill-level target, sensible early interval, progressive extension, and schedule adaptation.

### `learning-intelligence.progress-boundary`

> Reported insufficient comparable evidence for an exact fluency trend because text cannot evidence delivery and the questions differ. It described only the support visible in the current audio evidence and proposed two matched audio interview responses for the next comparison.

**Pass (4/4):** comparability limits, correct uncertainty label, supported findings only, and matched follow-up.

## Limitations

- The run evaluates first-turn behavior rather than long-term learner outcomes.
- Portability is verified for standard JSON semantics, not every proprietary host's attachment or storage behavior.
- Review intervals are adaptive coaching recommendations, not medical, psychometric, or guaranteed optimization claims.
- A host can delete only data within its available authority; the core skill cannot erase external chat history, backups, or provider records.
