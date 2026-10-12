# Academic Discussion behavior evaluation — 2026-10-12

## Result

**Pass: 5 of 5 cases and 20 of 20 observable criteria.**

## Method

- **Host:** Codex, text interaction.
- **Implementation:** the exact vendored copy of the user-provided `toefl-writing-2026-coach` Skill under `skills/toefl-writing-2026-coach/`.
- **Cases:** `tests/cases/academic-discussion.json`.
- **Grading:** each frozen response below was checked against its four observable criteria. A case passed only when all four were present.
- **Scope:** this is a focused single-host run. It does not establish official-score validity, human-rater agreement, or cross-model reliability.

## Frozen responses and findings

### `academic-discussion.practice-setup`

> **Professor:** Should universities require first-year students to complete a short community project? **Lina:** Projects help students understand local needs and practice teamwork. **Omar:** Required service can take time away from demanding courses. Core claims: Lina—civic learning and teamwork; Omar—academic time cost. Viable routes: (1) **condition:** require a small project integrated into a course; (2) **combine:** preserve service benefits while limiting weekly hours; (3) **missing factor:** offer several project types so students can match schedules and skills. **Best fit:** condition → a course-linked project uses existing class time → for example, an engineering class could audit energy use in a community center → students gain practical experience without adding a separate weekly obligation. Outline: direct position → extend Lina → explain course integration → example and consequence → address Omar through the time limit → concise conclusion. Write your response first; I will not provide a full model yet.

**Pass (4/4):** supplies an original discussion, extracts both claims, offers three routes with a developed best fit, and withholds the model.

### `academic-discussion.complete-feedback`

> **Practice estimate: 3/5, solid; high confidence; not an official ETS score.** Position: present—small classes are preferred. Contribution: partial—the response mostly repeats Omar. Mechanism: partial—`Students can talk more` points toward participation but does not explain how it improves learning. Example: weak—`my friend ... liked it` reports preference rather than showing learning. Consequence: missing. The response is relevant and clear, but development is the decisive gap. ETS does not require naming both students; as coaching advice, Lina's efficiency point is a useful opportunity for a condition: keep lectures for content delivery and add smaller discussion sessions for application. Routes: **combine** both formats; **condition** use small groups only for complex topics; **cause–effect** participation → immediate feedback → corrected misunderstandings. Useful language: `active participation`, `clarify misconceptions`, `apply course concepts`, `efficient content delivery`, `small-group discussion`, `receive immediate feedback`. Revision: “I agree with Omar that small discussion classes can improve participation, but universities do not need to replace every lecture. A better approach is to combine efficient lectures with weekly small-group sessions. In those sessions, students can explain concepts, ask specific questions, and receive immediate feedback. For example, after a large economics lecture, a smaller class could analyze one real market case, helping students correct misunderstandings before an exam. This approach preserves the efficiency Lina values while giving students the active practice Omar recommends.” Drill: rewrite the original example as `situation → action → learning consequence` in three sentences.

**Pass (4/4):** gives a bounded estimate, maps evidence, separates the rubric from coaching opportunity, and supplies routes, language, revision, and drill.

### `academic-discussion.missing-source`

> I cannot judge relevance, interaction with the discussion, or complete task fulfillment without the professor's question and both student posts, so I would not assign a confident task score or infer a Writing section or total score. Observable strengths are a clear position and a plausible mechanism: practical experience comes from working with local organizations and solving real problems. The example remains general, and a specific role plus consequence would develop it further. Please provide the missing question and posts for reliable scoring.

**Pass (4/4):** states the unavailable judgments, analyzes observable writing, requests all missing source material, and avoids unsupported scoring.

### `academic-discussion.targeted-retry`

> `Online courses are convenient` is a claim, but it does not show how convenience produces a meaningful result. Use `claim → mechanism → example → consequence`: flexible access → students can study around a fixed obligation → a commuter reviews a recorded lesson after work → fewer missed lessons and steadier progress. Now write only two to four sentences developing your own version; do not write a full discussion response yet.

**Pass (4/4):** diagnoses the gap, supplies the four-link scaffold, sets a bounded retry, and withholds a complete response.

### `academic-discussion.student-reference-boundary`

> No. Naming both students is not an independent requirement in the public ETS rubric. The scoring focus is a relevant, clearly expressed, sufficiently developed contribution with controlled language. Engaging both viewpoints can make the response feel more like a genuine discussion when each reference adds a real function—such as extending, qualifying, or connecting an idea—but it is coaching advice, not an automatic scoring rule. A strong direct response should not be penalized solely because it does not name both students.

**Pass (4/4):** states the rubric boundary, centers actual scoring evidence, frames integration as optional coaching, and avoids inventing a mandate.

## Limitations

- Actor and criteria checking occurred in one host rather than isolated contexts.
- The run covers first-turn text behavior, not multi-turn retention or model variance.
- Numeric output is a coaching estimate on the public task scale, not an ETS score.
