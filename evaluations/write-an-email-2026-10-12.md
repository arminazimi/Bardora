# Write an Email behavior evaluation — 2026-10-12

## Result

**Pass: 5 of 5 cases and 20 of 20 observable criteria.**

## Method

- **Host:** Codex, text interaction.
- **Inputs:** repository `SKILL.md`, `references/feedback-contract.md`, `references/tasks/writing.write-an-email.md`, and each request in `tests/cases/write-an-email.json`.
- **Source design:** the task module adapts the function-first workflow, register controls, scenario language, holistic rubric use, and revision protocol from the user-provided `toefl-writing-2026-coach` Skill.
- **Grading:** each frozen response below was checked against its four observable criteria. A case passed only when all four were present.
- **Scope:** this is a focused single-host run and does not establish official-score validity or cross-model reliability.

## Frozen responses and findings

### `write-an-email.practice-setup`

> **Write an Email practice.** Recipient: the academic-program coordinator; relationship: student to staff member; register: neutral-professional. Your seminar was moved to the same time as a required laboratory orientation. Email the coordinator to: (1) explain the scheduling conflict, (2) describe how it affects your participation, and (3) request one realistic alternative. Plan with `purpose → facts → impact → action → polite close`. Write your email first; I will not show a model until after your attempt.

**Pass (4/4):** identifies audience and register, supplies three requirements, gives the functional checklist, and withholds the model.

### `write-an-email.complete-feedback`

> **Practice estimate: 4/5, borderline; medium confidence; not an official ETS score.** All three requirements are present: `train stopped` explains the cause, `cannot begin project` gives the impact, and `Could I attend Friday session instead?` makes a specific request. The decisive weakness is language control, not task coverage. Fix first: `I miss yesterday workshop` → `I missed yesterday's workshop` (past event and possessive); `when train stopped` → `when my train was delayed` (natural phrasing); `begin project` → `begin my project` (article/determiner). Useful toolkit: `mandatory workshop`, `train delay`, `lab access`, `alternative session`, `attend the Friday session`, `complete the requirement`. Grammar controls: past simple for the missed event; articles and possessives before singular count nouns. Revised email: “Dear Ms. Lee, I am writing because I missed yesterday's mandatory workshop when my train was delayed. Since completing the workshop is required for lab access, I cannot begin my project yet. Would it be possible for me to attend the Friday session instead? Thank you for your help. Sincerely, Amir.” Retry: rewrite the opening and impact sentences without looking at the revision.

**Pass (4/4):** maps the requirements with evidence, labels a bounded estimate, preserves facts while correcting language, and supplies the toolkit, revision, and retry.

### `write-an-email.missing-prompt`

> The purpose and request are observable, but without the prompt I cannot reliably judge whether every required bullet was covered, so I would not assign a confident task score or infer a Writing section or total score. The email clearly reports the room conflict and asks for another room. Language priorities are `We need to meet every Tuesday` and `because the competition is soon`; the request would be stronger as `Could you please confirm an available room for next Tuesday at 4 p.m.?` Send the original prompt or its bullet requirements for reliable task-fulfillment scoring.

**Pass (4/4):** states the coverage limit, analyzes observable features, requests missing requirements, and avoids unsupported scoring.

### `write-an-email.targeted-retry`

> `Please solve this quickly` does not name the action, and `quickly` adds urgency without a supported deadline. Use this frame: `Could you please [specific action] by [relevant time]?` Retry only the request sentence—for example, name what the recipient should confirm, repair, send, or schedule and use a deadline only if the prompt supports it. Do not rewrite the rest of the email yet.

**Pass (4/4):** identifies both gaps, gives an actionable frame, requests a sentence-only retry, and withholds a full rewrite.

### `write-an-email.register-revision`

> The invitation is clear, but `Dear Esteemed Colleague`, `hereby`, and repeated `esteemed` are too formal for a close classmate. Preserve the invitation as: `Hi Maya, would you like to join our study session?` Register should follow the relationship; friendly, direct language is more natural here than institutional wording.

**Pass (4/4):** diagnoses the relationship mismatch, preserves meaning, supplies a concise revision, and explains the register choice.

## Limitations

- The responses and criteria were checked within one host rather than isolated actor and evaluator contexts.
- The run tests first-turn text behavior, not multi-turn memory or cross-model variance.
- Numeric output is a coaching estimate on the public task scale, not an ETS score.
