# Build a Sentence behavior evaluation — 2026-10-12

## Result

**Pass: 5 of 5 cases and 20 of 20 observable criteria.**

## Method

- **Host:** Codex, text interaction.
- **Inputs:** repository `SKILL.md`, `references/tasks/writing.build-a-sentence.md`, and each request in `tests/cases/build-a-sentence.json`.
- **Grading:** each frozen response below was checked against the four observable criteria for its case. A case passed only when all four criteria were present.
- **Scope:** this is a focused single-host run. It does not establish cross-model reliability or equivalence to ETS scoring.

## Frozen responses and findings

### `build-a-sentence.practice-setup`

> **Build a Sentence — cause and result.** Cue: a clause beginning with *because* gives the reason and must connect to a complete main clause. Arrange every chunk once: `because the new exhibit` / `attracted many visitors` / `the museum extended its hours`. Write one complete sentence; I will check it before showing an answer.

**Pass (4/4):** identifies the task, teaches a compact grammar cue, supplies an original solvable three-chunk item, and withholds the answer.

### `build-a-sentence.feedback`

> **Practice result: 0/1.** You used all three chunks once, but the contrast relationship is broken: *although* must introduce `it was raining`, not `the match continued`. Corrected sentence: **Although it was raining, the match continued until sunset.** Smallest fix: keep the full *although*-clause together and attach `until sunset` to `continued`. Retry—arrange every chunk once: `although the trail was steep` / `the hikers continued` / `without stopping`. Cue: keep the contrast clause intact.

**Pass (4/4):** checks the inventory, cites the broken relationship, corrects after the supplied attempt, and provides an original contrast retry.

### `build-a-sentence.valid-alternative`

> **Correct: 1/1.** `The students asked questions after the lecture ended.` is grammatical and uses both chunks exactly once. The main event is `the students asked questions`; the *after*-clause states when it happened. The clause could also appear first, so this valid order should not be rejected.

**Pass (4/4):** accepts the answer, confirms both chunks, explains the time relationship, and recognizes valid alternative order.

### `build-a-sentence.missing-evidence`

> I can check it, but I need two things: the complete set of chunks exactly as shown and your assembled sentence. Without both, I cannot determine correctness, so I will not guess or assign a score.

**Pass (4/4):** requests both required inputs, makes no correctness claim, and gives no invented score.

### `build-a-sentence.retry`

> Retry the same contrast pattern. Cue: keep the entire *although*-clause together, then connect it to a complete main clause. Arrange every chunk once: `although the store was closing` / `the cashier helped` / `the last customer`. Send your sentence and I will check it before revealing the answer.

**Pass (4/4):** targets contrast, uses an original three-chunk item, gives one cue, and withholds the solution.

## Limitations

- The actor and criterion check were completed in one host rather than isolated evaluator contexts.
- The run tests first-turn text behavior, not multi-turn retention or cross-model variance.
- Originality was checked against repository content and by fresh construction; no external similarity corpus was used.
