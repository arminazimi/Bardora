# Independent English Test Prep Agent

An open-source Agent Skill for preparation aligned with the TOEFL® test format that took effect on January 21, 2026.

> [!IMPORTANT]
> This is an independent learning project. It is not endorsed or approved by ETS. TOEFL and TOEFL iBT are registered trademarks of ETS. The project does not reproduce secure or copyrighted test questions, and its feedback is not an official ETS score.

> [!WARNING]
> The existing repository slug is a working identifier. Current ETS trademark guidance says ETS marks should not be incorporated into a product name, domain name, or similar identifier. Selecting an independent public brand and reviewing the final attribution are release blockers for v1.0.

## Project status

**Foundation v0.1.0 — in development.** The repository defines the product, its portable skill interface, the official-format task matrix, architecture, evaluation cases, and roadmap. Coaching content and scoring calibration will be added incrementally and must pass the documented evaluations before a stable release.

## What the skill will do

- Route learners to the correct Reading, Listening, Writing, or Speaking task type.
- Teach the format and strategy with original practice material.
- Give specific, evidence-based feedback and a prioritized next step.
- Separate coaching estimates from official ETS scores.
- Support a full diagnostic, focused practice, review, and progress tracking.

The 2026 format contains 12 task types across four sections. See the [task-type matrix](docs/toefl-2026-task-matrix.md) for the official names and source links.

## Repository map

```text
SKILL.md                              Agent entry point
docs/PRD.md                           Product requirements and MVP boundary
docs/architecture.md                  Portable architecture and contracts
docs/toefl-2026-task-matrix.md        ETS-sourced 2026 format matrix
docs/ROADMAP.md                       Delivery phases and completion criteria
references/feedback-contract.md       Shared coaching output contract
tests/cases/core.json                 Behavior-oriented evaluation cases
tests/test_repository_contract.py     Offline repository checks
```

## Use as an Agent Skill

Clone the repository into a location your agent can discover as a skill, or copy the repository folder into that agent's skills directory. Then invoke it explicitly:

```text
Use $toefl-ibt-2026-coach to give me a Writing diagnostic.
```

The skill is intentionally platform-neutral: it depends on readable Markdown and JSON, not a vendor SDK. Platform-specific adapters may be added later without changing the coaching contract.

## Validate locally

The contract tests use only the Python standard library:

```bash
python3 -m unittest discover -s tests -v
```

These tests validate packaging, source traceability, all 12 task types, evaluation-case coverage, and required safety language. They do not claim that AI-generated feedback is psychometrically equivalent to ETS scoring.

## Documentation

- [Product requirements](docs/PRD.md)
- [Architecture](docs/architecture.md)
- [TOEFL iBT 2026 task matrix](docs/toefl-2026-task-matrix.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

## License

Apache License 2.0. See [LICENSE](LICENSE).
