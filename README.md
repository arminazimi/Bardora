# Independent English Test Prep Agent

An open-source Agent Skill for preparation aligned with the TOEFL iBT® test format that took effect on January 21, 2026.

> [!IMPORTANT]
> This is an independent learning project. TOEFL and TOEFL iBT are registered trademarks of ETS in the United States and other countries. This project is not endorsed or approved by ETS. It does not reproduce or distribute unlicensed ETS questions, passages, prompts, audio, transcripts, sample responses, answer keys, rubrics, directions, or graphics, and its feedback is not an official ETS score.

> [!WARNING]
> The existing repository slug is a working identifier. Current ETS trademark guidance says ETS marks should not be incorporated into a product name, domain name, or similar identifier. Selecting an independent public brand and reviewing the final attribution are release blockers for v1.0.

## Project status

**Task coaching implemented; release work continues.** The repository defines the product, portable skill interface, official-format task matrix, architecture, and task-specific coaching for Reading, Listening, Writing, and Speaking. Human calibration, learning intelligence, cross-platform validation, independent branding, and release gates remain before a stable release.

## What the skill does

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
docs/research/                         Dated official-source audits
docs/ROADMAP.md                       Delivery phases and completion criteria
references/feedback-contract.md       Shared coaching output contract
references/learning-intelligence.md   Diagnostics, plans, review, and progress
references/learner-state.md           Consent and portable-state lifecycle
schemas/learner-state.v1.schema.json  Host-neutral learner-state contract
skills/toefl-writing-2026-coach/      Exact vendored Writing implementation
evaluations/                           Dated behavior-evaluation reports
tests/cases/core.json                 Behavior-oriented evaluation cases
tests/test_repository_contract.py     Offline repository checks
```

## Use as an Agent Skill

Clone the repository into a location your agent can discover as a skill, or copy the repository folder into that agent's skills directory. Then invoke it explicitly:

```text
Use $english-test-prep-coach to give me a Writing diagnostic.
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
- [ETS official-source audit — October 12, 2026](docs/research/ets-source-audit-2026-10-12.md)
- [Core behavior evaluation — October 12, 2026](evaluations/core-behavior-2026-10-12.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

## License

Original project material is available under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). The license does not grant rights to ETS trademarks or copyrighted ETS material.
