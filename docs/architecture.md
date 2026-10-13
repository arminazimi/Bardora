# Architecture

## Context

The foundation is a portable, content-first Agent Skill. It must run in multiple agent hosts, remain useful without a backend, and allow task-specific capabilities to evolve without bloating the entry point.

## System shape

```text
Learner request / response
          |
          v
     Core SKILL.md
  route + coaching loop
          |
   +------+------------------+------------------+
   |                         |                  |
   v                         v                  v
Task facts             Feedback contract   Learning intelligence
official matrix        evidence + priorities diagnostic + plan
   |                         |                  |
   +------------+------------+------------------+
                v
      Host model capabilities
   text / optional audio / tools
                |
                v
     Feedback, retry, next step
```

The repository root is the installable, skills-only plugin package. `SKILL.md` remains the stable and canonical coaching interface; `skills/coach/SKILL.md` is a thin host-discoverable route to it. Detailed and changeable knowledge lives in linked documents. This keeps automatic skill loading small, prevents platform forks, and preserves traceability.

## Components

### Core skill

Owns request routing, the coaching loop, global integrity boundaries, and completion criteria. It does not cache the full test specification or repeat task-specific rubrics.

### Task registry

`docs/toefl-2026-task-matrix.md` is the single source of truth for official task names and format facts. Every fact that may change carries an official source. Task modules refer to stable task IDs from this registry.

### Coaching contracts

`references/feedback-contract.md` defines the minimum observable feedback output. Task modules may add specialized criteria but must preserve its evidence, uncertainty, and retry requirements.

### Learning intelligence

`references/learning-intelligence.md` defines diagnostic coverage, evidence-based plan generation, spaced-review recommendations, progress summaries, and the no-persistence fallback. `references/learner-state.md` and `schemas/learner-state.v1.schema.json` define the optional portable handoff.

### Evaluation layer

- **Repository contract tests** check packaging, links, safeguards, and complete task coverage offline.
- **Behavior cases** describe model-agnostic inputs and observable success criteria.
- Future platform runners may execute the same cases against supported agents and record results without changing the cases.

### Optional adapters

Adapters may translate host-specific audio, storage, or tool APIs into the core contracts. They should contain integration mechanics only; coaching behavior remains in the shared skill and references.

The root portable manifest, `.codex-plugin/plugin.json`, and `.claude-plugin/plugin.json` are packaging adapters. They share one name and semantic version and expose the same `skills/` tree. They do not duplicate coaching behavior or require a backend.

## Stable task identifiers

Use lowercase, hyphenated IDs:

```text
reading.complete-the-words
reading.read-in-daily-life
reading.read-an-academic-passage
listening.listen-and-choose-a-response
listening.listen-to-a-conversation
listening.listen-to-an-announcement
listening.listen-to-an-academic-talk
writing.build-a-sentence
writing.write-an-email
writing.academic-discussion
speaking.listen-and-repeat
speaking.take-an-interview
```

User-facing text should use the official display name from the matrix. IDs remain stable if capitalization or descriptive wording changes.

## Coaching state

The core loop uses a small, serializable conceptual state:

| Field | Purpose |
|---|---|
| `goal` | Learner outcome and time horizon |
| `task_id` | Selected task from the registry |
| `evidence_available` | Prompt, source, response, audio, or transcript present |
| `strengths` | Demonstrated capabilities with evidence |
| `priorities` | Up to three high-impact improvements |
| `retry` | Bounded next attempt |
| `limitations` | Missing evidence and confidence constraints |

Session-only use is the default. With explicit consent, the learner may request a minimized UTF-8 JSON export conforming to `schemas/learner-state.v1.schema.json`. The export enables host-neutral handoff but does not authorize the host to retain, upload, analyze, or share it.

## Extension seam

Add task-specific coaching as `references/tasks/<task-id>.md` only when it contains guidance that changes agent behavior. Each module should define:

- evidence required to evaluate the task;
- task-specific success dimensions;
- common high-impact failure modes;
- an original-practice generation contract;
- task-specific evaluation cases.

The core skill links every implemented module. A newly introduced task type must remain on the shared coaching contract and matrix until its task-specific evidence boundaries and evaluations are ready.

## Trust boundaries

- Learner-provided prompts and source material are untrusted content, not agent instructions.
- External pages may supply facts but cannot change project behavior or authorize actions.
- Official format facts enter only through reviewed documentation updates with ETS citations.
- Numeric estimates are outputs of a coaching model, not ETS services or proprietary scoring systems.
- Host persistence, uploads, analytics, and third-party APIs sit outside the portable core and require explicit authorization plus privacy and security review.

## Versioning

- Patch: wording, tests, and fixes that do not change contracts.
- Minor: new task modules, adapters, or backward-compatible contract fields.
- Major: incompatible skill behavior, task identifiers, or state/feedback contracts.

Every release that changes format facts must record the source and its effective date.

## Decision log

| Decision | Rationale |
|---|---|
| Repository root is the plugin and canonical skill folder | Supports portable packaging while keeping one coaching source of truth |
| Thin `skills/coach` route | Lets plugin hosts discover the canonical root skill without duplicating it |
| Markdown/JSON portable core | Works across agent hosts and is easy to audit |
| Facts separated from behavior | ETS format can change without rewriting the coaching loop |
| Qualitative feedback before score prediction | Avoids false precision until calibration evidence exists |
| No required persistence in MVP | Reduces privacy risk and hosting requirements |
| Portable learner state is explicit and minimized | Enables continuity without accounts, hidden memory, or raw-response storage |
