# ETS source audit — 2026-10-12

## Scope and method

This audit checks `README.md`, `docs/PRD.md`, `docs/architecture.md`, `docs/toefl-2026-task-matrix.md`, `SKILL.md`, and `CONTRIBUTING.md` against current, first-party ETS sources only. It is a source and wording review, not legal advice.

## Executive result

**Format and scoring facts pass.** ETS confirms that the updated TOEFL iBT® test took effect on **January 21, 2026**; the repository lists all 12 task types with the correct names; its published section totals/times and task allocations match ETS; Reading and Listening are two-stage adaptive while Writing and Speaking are linear; and score reports use a 1–6 scale in half-point increments with transitional 0–120 overall-score reporting.

**Release is not trademark-ready.** The repository/product identifier `toefl-coach-ai` incorporates an ETS mark, which ETS expressly prohibits in product names and similar identifiers. The README and PRD already identify this blocker, but public-facing documents do not consistently follow ETS's first-use, generic-term, and notice rules. Copyright safeguards are directionally correct but should cover all ETS materials, not only questions.

## Verified claims

| Claim | Result | Official evidence |
|---|---|---|
| Updated format effective January 21, 2026 | Pass | ETS says the test update and 1–6 score reporting took effect on that date: [test content and structure](https://www.ets.org/toefl/test-takers/ibt/about/content.html), [understanding scores](https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html). |
| 12 task types and their names | Pass | The current ETS content page lists 3 Reading, 4 Listening, 3 Writing, and 2 Speaking task types with the same names used in the repository: [test content and structure](https://www.ets.org/toefl/test-takers/ibt/about/content.html). |
| Published section totals/times | Pass with wording improvement | ETS publishes Reading 50/30 minutes, Listening 47/29, Writing 12/23, and Speaking 11/8, while warning that time and items may vary as the test adapts: [test content and structure](https://www.ets.org/toefl/test-takers/ibt/about/content.html). ETS's teacher FAQ expresses these as “up to” totals: [Teacher FAQ](https://www.eu.ets.org/content/dam/ets-org/pdfs/toefl/teacher-faq.pdf). |
| Per-task allocations | Pass | The specification gives Reading 30, 5–15, 5–15; Listening 15–19, 10, 6–10, 8–16; Writing 10, 1, 1; and Speaking 7, 4: [2026 test blueprint and specifications](https://www.ets.org/content/dam/ets-org/pdfs/toefl/toefl-ibt-test-specifications-2026.pdf), pp. 4–7. |
| Adaptive and linear delivery | Pass | ETS explicitly describes Reading and Listening as two-stage adaptive and Writing and Speaking as linear: [2026 test blueprint and specifications](https://www.ets.org/content/dam/ets-org/pdfs/toefl/toefl-ibt-test-specifications-2026.pdf), blueprint note 5. |
| Machine- versus AI-scored task types | Pass as narrowly attributed | The blueprint classifies selected-response Reading/Listening and Build a Sentence as machine-scored, and constructed Writing/Speaking responses as AI-scored: [2026 test blueprint and specifications](https://www.ets.org/content/dam/ets-org/pdfs/toefl/toefl-ibt-test-specifications-2026.pdf), blueprint note 4 and section tables. The matrix correctly says this is what the blueprint describes and does not claim access to ETS scoring systems. |
| 1–6 scale, half-point increments, CEFR alignment | Pass | ETS confirms four section scores plus an overall score on the 1–6 scale in 0.5 increments, aligned with CEFR: [understanding scores](https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html). |
| Overall-score calculation | Pass | ETS says the overall score is the four-section average rounded to the nearest half band and provides tie examples: [score report FAQ](https://www.ets.org/toefl/test-takers/ibt/faq/score-reports.html). |
| Transitional 0–120 reporting | Pass | ETS says a comparable 0–120 overall score is included during the two-year transition after January 2026; ETS also describes the window as running through January 2028: [understanding scores](https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html), [2026 score-display explanation](https://www.ets.org/toefl/blog/understanding-toefl-ibt-score-displays.html). |
| No universal passing score; scores valid two years | Pass | Institutions set their own requirements: [understanding scores](https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html). Scores remain valid for two years: [sending scores](https://www.ets.org/toefl/test-takers/ibt/scores/send-scores.html). |

## Findings requiring changes

### High — repository/product identifier uses an ETS trademark

The GitHub slug `toefl-coach-ai` incorporates `TOEFL`, even though ETS says its marks may not be used in a company, brand, or product name, domain name, social username, website, or similar identifier. `README.md` and `docs/PRD.md` correctly disclose this as a release blocker; the blocker remains unresolved. Rename the repository and public product before v1.0, and keep the ETS mark only as informational compatibility text separated from the independent brand. See [ETS trademark guidelines](https://www.ets.org/legal/trademarks.html).

### Medium — trademark presentation is inconsistent across public documents

ETS requires the first and most prominent use of a mark to carry the registration symbol, be used as an adjective with an appropriate generic term, and be accompanied by a visible non-endorsement notice. `README.md` and `docs/PRD.md` use `TOEFL® test` on first use, but:

- `docs/toefl-2026-task-matrix.md` begins with “TOEFL iBT 2026” without `®` or the generic word “test”;
- `SKILL.md` first uses “TOEFL iBT test” without `®`;
- `CONTRIBUTING.md` first refers to “ETS” without a registration symbol or shared notice;
- the README notice says “TOEFL and TOEFL iBT are registered trademarks” without symbols and uses the marks as nouns.

Apply a consistent first-use form such as “TOEFL iBT® test” and the ETS-prescribed credit/non-endorsement wording wherever a document functions as a separate public web page. Have the final presentation reviewed against the current [ETS trademark guidelines](https://www.ets.org/legal/trademarks.html); ETS says the guidelines can change and describes advance review for distributed product materials.

### Medium — copyright safeguards are too question-centric

The README says the project does not reproduce “secure or copyrighted test questions,” and `CONTRIBUTING.md` bars recalled, leaked, or copied questions. ETS states that **all TOEFL materials** are copyright-protected and that reproduction requires a license; it also says TOEFL materials may not be posted to third-party websites. Broaden these safeguards to ETS passages, prompts, audio, transcripts, sample responses, answer keys, rubrics, graphics, directions, and other protected material—not only questions—and prefer links to official ETS pages. The PRD and SKILL already move in this direction, but the rule should be consistent. See the [ETS TOEFL licensing policy](https://www.ets.org/legal/permissions/licensing.html) and [permissions page](https://www.ets.org/legal/permissions.html).

### Low — section totals should not look guaranteed

`docs/toefl-2026-task-matrix.md` labels 50/47/12/11 as “Base items.” The current test-taker page publishes those totals but immediately says items and time may vary as the test adapts; the ETS teacher FAQ says “up to.” The matrix already includes a variability note, so the numbers are not false, but changing the column to “Published base / maximum items” (or adding “up to” in each adaptive row) would prevent readers from interpreting them as a guaranteed form length.

### Low — use the canonical specification URL

The matrix links to an `ets-india` copy of the specification. It is an official ETS-hosted document and the contents match, but the current English test-taker page links to the canonical `ets-org` asset. Replace the source URL with:

`https://www.ets.org/content/dam/ets-org/pdfs/toefl/toefl-ibt-test-specifications-2026.pdf`

This reduces regional-link fragility and makes provenance clearer.

### Low — distinguish pre-launch blueprint status from current facts

The specification itself says its details were subject to minor revision until launch. The current test-taker page confirms the 12 names and section totals after launch, but it does not expose every task-level allocation. Keep the blueprint attribution on task allocations and avoid presenting those ranges as an immutable promise. The matrix mostly does this already; adding “published blueprint target” rather than simply “Blueprint allocation” would be stronger.

## File-by-file disposition

| File | Disposition |
|---|---|
| `README.md` | Format facts pass. Keep the release blocker; broaden copyright language and normalize the trademark notice. |
| `docs/PRD.md` | Substantively passes. Broaden the protected-material examples and keep independent branding as a v1.0 blocker. |
| `docs/architecture.md` | Pass. Claims are architectural, appropriately cautious, and do not overstate ETS scoring equivalence. |
| `docs/toefl-2026-task-matrix.md` | Numerical/task facts pass. Fix first-use trademark form, canonical blueprint URL, and total/allocation labels. |
| `SKILL.md` | Coaching and scoring boundaries pass. Fix first-use trademark form and preserve original-material constraints. |
| `CONTRIBUTING.md` | Process passes. Broaden the prohibition from copied questions to all unlicensed ETS material and normalize first-use/notice handling. |

## Parent-agent checklist

- [x] Effective date verified: January 21, 2026.
- [x] All 12 official task names verified.
- [x] Published item totals, timings, task allocations, and delivery model verified.
- [x] 1–6 scoring, rounding, CEFR alignment, transition reporting, and score validity verified.
- [ ] **Fix before release:** rename `toefl-coach-ai` to an independent, non-ETS product/repository name. Tracked separately in [issue #17](https://github.com/arminazimi/toefl-coach-ai/issues/17).
- [x] **Fixed in issue #8:** use `TOEFL iBT® test` on first prominent use and standardize the non-endorsement credit.
- [x] **Fixed in issue #8:** expand copyright rules from “questions” to all unlicensed ETS materials.
- [x] **Fixed in issue #8:** change the blueprint link to the canonical `ets-org` URL.
- [x] **Fixed in issue #8:** relabel section totals and task allocations so adaptive variability and blueprint status are unmistakable.
- [x] Re-run repository contract tests after documentation changes: 7 tests passed.
- [ ] Recheck ETS trademark and format pages immediately before a public release.

## Issue #8 disposition

The foundation scope, exclusions, success measures, format facts, scoring facts, and current IP safeguards have been reviewed. All corrections within this issue's documentation scope were applied. The repository-name risk is intentionally not resolved here because choosing and migrating an independent public brand requires a product decision; it remains a release blocker in issue #17. The final pre-release source recheck remains a release procedure rather than a blocker for completing this dated foundation audit.
