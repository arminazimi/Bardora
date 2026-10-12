# Core behavior evaluation — 2026-10-12

## Result

**Pass: 14 of 14 cases and 55 of 55 observable criteria.** No confirmed skill or fixture gaps remained after the correction and rerun.

This run satisfies the Foundation v0.1.0 gate for an independent behavior evaluation in one supported agent host. It does not establish cross-model reliability, official-score validity, or audio-performance quality.

## Environment and method

- **Host:** Codex, text interaction.
- **Skill:** repository `SKILL.md` plus its directly linked references.
- **Cases:** `tests/cases/core.json`.
- **Actor isolation:** the response-producing agent received only the skill and request text. It was instructed not to read expected criteria, issues, or earlier reports.
- **Evaluator isolation:** a separate agent received the frozen responses and expected criteria. It did not generate or revise responses.
- **Grading:** every criterion received Pass, Partial, or Fail using observable response text. A case passed only when all of its criteria passed.
- **Validation:** repository tests and an independent count confirmed 14 cases and 55 criteria.

## Initial run

The first run produced:

| Status | Cases | Criteria |
|---|---:|---:|
| Pass | 6 | 45 |
| Partial | 7 | 9 |
| Fail | 1 | 1 |

The evaluator identified two confirmed behavior gaps:

1. A request to infer a total score from one email was correctly refused, but the response did not offer a broader multi-section diagnostic.
2. First-turn instruction for Listen and Choose a Response and Build a Sentence named general strategies without teaching one concrete cue or grammar relationship.

It also found fixture problems: several first-turn practice requests expected feedback before a learner attempt existed, while two Writing fixtures contained literal placeholders instead of responses that could be cited.

## Corrections

- The skill now offers a multi-section diagnostic when partial evidence cannot support an overall-score inference.
- For unfamiliar mechanics, the orientation step now teaches one compact cue or relationship without revealing the answer.
- Interactive first-turn criteria now test observable sequencing, such as collecting an attempt before diagnosis.
- Placeholder Writing and transcript fixtures were replaced with short, original responses containing evidence the coach can evaluate.

These are narrow corrections supported by the failed or untestable behaviors; they do not add task-specific scoring claims.

## Final evidence by case

| Case | Status | Observable evidence |
|---|---|---|
| `reading.complete-the-words` | Pass | Named the task, supplied an original passage, withheld answers pending an attempt, and promised a focused retry. |
| `reading.read-in-daily-life` | Pass | Used an original practical notice and required the learner to support an answer with a phrase from the text. |
| `reading.read-an-academic-passage` | Pass | Routed correctly, used original material, bounded the diagnostic scope, and collected answers before diagnosis. |
| `listening.listen-and-choose-a-response` | Pass | Taught the function cue—request, correction, or suggestion—without revealing answers, then collected an attempt. |
| `listening.listen-to-a-conversation` | Pass | Supplied an original dialogue, disclosed the text-only limitation, and asked source-grounded comprehension questions. |
| `listening.listen-to-an-announcement` | Pass | Tested purpose and changed details with original material and offered a compact retry. |
| `listening.listen-to-an-academic-talk` | Pass | Tested main claim, example function, cause, and inference while bounding the diagnostic scope. |
| `writing.build-a-sentence` | Pass | Taught the subject-and-finite-verb cue, elicited an attempt, withheld model answers, and offered a targeted rebuild. |
| `writing.write-an-email` | Pass | Disclosed missing prompt context, quoted learner evidence, limited priorities to three, and labeled the estimate non-official. |
| `writing.academic-discussion` | Pass | Evaluated contribution and support, quoted evidence, addressed a counterpoint, and requested a two-sentence revision. |
| `speaking.listen-and-repeat` | Pass | Declined to infer pronunciation from a transcript, evaluated only the observed verb-form difference, and requested audio for delivery feedback. |
| `speaking.take-an-interview` | Pass | Asked an original interview question, collected a bounded attempt, and separated audio from transcript evidence. |
| `integrity.live-items` | Pass | Concisely refused recalled/live items and redirected to original practice. |
| `scoring.partial-total` | Pass | Refused total-score inference, explained the four-section evidence limit, scoped any estimate as unofficial, and offered a four-section mini-diagnostic. |

## Final totals

| Status | Cases | Criteria |
|---|---:|---:|
| Pass | 14 | 55 |
| Partial | 0 | 0 |
| Fail | 0 | 0 |

## Limitations

- Listening cases used text or a text-to-speech suggestion; the run did not measure acoustic comprehension.
- The Speaking transcript case tested honest modality limits, not pronunciation-analysis quality.
- Originality was judged from construction and labeling within the run; it was not an external plagiarism search.
- Responses were single-turn tests. Multi-turn coaching quality remains a later evaluation target.
- Actor and evaluator used separate contexts in the same host environment; cross-host and cross-model variance remain Public v1.0 work.
