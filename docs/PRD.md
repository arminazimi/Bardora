# Product Requirements Document

## Product

This repository is the working home of a worldwide, open-source Agent Skill for preparation aligned with the TOEFL iBT® test format effective January 21, 2026. It provides original practice, formative feedback, strategy, and structured improvement loops across all four sections.

An independent public brand must replace the current repository identifier before v1.0 because ETS trademark guidance restricts use of ETS marks in product and domain names.

## Problem

Learners need affordable practice that reflects the new task types, explains why an answer succeeds or fails, and turns feedback into a next attempt. Generic chat assistants often mix old and new formats, overstate scoring precision, or produce feedback without evidence.

## Users

- Independent learners at intermediate through advanced English levels.
- Teachers who want original practice and a consistent feedback structure.
- Contributors building task-specific coaching, rubrics, evaluations, and platform adapters.

The first release is English-first. The coach may explain concepts in the learner's preferred language while preserving English practice where the task requires it.

## Product principles

1. **Current:** task routing and format claims are traceable to official ETS sources.
2. **Formative:** every evaluation produces an actionable retry, not merely a score.
3. **Evidence-based:** feedback points to the learner response or supplied source material.
4. **Honest:** practice estimates and technical limitations are explicit.
5. **Original:** practice content does not copy secure or copyrighted ETS questions.
6. **Portable:** the core skill works without a proprietary SDK or service.
7. **Accessible:** useful basic coaching remains available without payment or account-specific features.

## MVP scope

### Included

- Routing for all 12 task types in the 2026 format.
- Task orientation, strategy, original practice, response feedback, and a targeted retry.
- Writing feedback from text.
- Speaking feedback from audio when supported, with transcript-only fallback.
- Reading and Listening practice using original source material.
- A full-format diagnostic plan assembled from task-level activities.
- Explicit non-affiliation, copyright, and score-estimate safeguards.
- Offline contract tests and behavior-oriented evaluation cases.

### Deferred

- Claims of official score equivalence or score prediction.
- Speech recognition, text-to-speech, user accounts, hosted storage, or analytics services.
- Automated spaced repetition and longitudinal learner models.
- A complete simulated test UI, payments, classrooms, or teacher dashboards.
- Reproduction or distribution of unlicensed ETS questions, passages, prompts, audio, transcripts, sample responses, answer keys, rubrics, directions, or graphics.

## Core user journeys

### Focused practice

The learner names a section or goal. The coach selects a current task type, explains the target, supplies original material, collects the answer, gives evidence-backed feedback, and requests a short retry.

### Response review

The learner supplies an answer and, when applicable, its prompt or source. The coach states what evidence is missing, evaluates only supported dimensions, prioritizes improvements, and offers a revised example or retry.

### Diagnostic

The coach confirms time and modality constraints, samples relevant task types, reports strengths and priorities by section, explains confidence limits, and proposes a study sequence. It does not infer a total official score from incomplete evidence.

## Functional requirements

| ID | Requirement | MVP acceptance |
|---|---|---|
| FR-1 | Recognize and route every current task type | All 12 official task types appear in the matrix and evaluation cases |
| FR-2 | Generate original practice | Output is newly authored and contains no claim of being an ETS item |
| FR-3 | Give evidence-based feedback | Each issue cites response evidence or a clearly stated omission |
| FR-4 | Prioritize improvement | Feedback includes no more than three ranked priorities and a retry |
| FR-5 | Handle missing modalities | Transcript-only Speaking feedback discloses what cannot be assessed |
| FR-6 | Communicate score uncertainty | Every numeric estimate names its scale and non-official status |
| FR-7 | Remain source-traceable | Changeable format facts link to official ETS sources |
| FR-8 | Support multilingual explanation | Explanations may follow learner preference without replacing required English production |

## Non-functional requirements

- **Portability:** Markdown/JSON core; no required vendor runtime.
- **Privacy:** core operation requires no persistent learner storage.
- **Maintainability:** task facts have one source of truth; conditional guidance sits behind references.
- **Testability:** repository and behavior contracts can be checked separately.
- **Accessibility:** do not make color, audio, or visual layout the only carrier of information.
- **Latency:** a focused text coaching turn should not require external services beyond the host model.

## Safety, legal, and integrity

- Present the project as independent and unaffiliated with ETS.
- Use ETS trademarks only to identify compatibility and learning context, following current ETS guidance.
- Link to official material rather than copying protected content.
- Decline requests for leaked, recalled, or live test questions and redirect to original practice.
- Avoid guarantees about admission, visa, academic, or official score outcomes.
- Obtain learner consent before any future persistent storage of responses or audio.

## Success measures

### Foundation v0.1.0

- Contract tests pass from a clean clone.
- All 12 task types are source-cited and covered by an evaluation case.
- The skill completes the feedback contract in representative text and transcript scenarios.
- No documentation implies ETS affiliation or official scoring.

### Before v1.0

- The project has an independent brand compatible with current ETS trademark guidance.
- Task-specific behavior evaluations pass at an agreed threshold.
- Human reviewers find feedback evidence-supported and actionable across proficiency levels.
- Accessibility and copyright review have no release-blocking findings.
- At least two supported agent environments can run the same core skill with no content fork.

## Open decisions

- What independent public brand should replace the working repository identifier?
- Which qualitative or numeric practice scale should be used per task after sufficient validation?
- Which audio capabilities are required for the first Speaking release?
- What opt-in, privacy-preserving learner-state format should support progress tracking?
- Which agent environments will receive maintained installation adapters for v1.0?

## Trademark notice

TOEFL and TOEFL iBT are registered trademarks of ETS in the United States and other countries. This project is not endorsed or approved by ETS.
