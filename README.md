<p align="center">
  <img src="assets/brand/bardora-lockup.svg" alt="Bardora — The modern art of English mastery." width="720">
</p>

# Bardora

**The modern art of English mastery.**

Bardora is an open-source Agent Skill for preparation aligned with the TOEFL iBT® test format that took effect on January 21, 2026.

> [!IMPORTANT]
> This is an independent learning project. TOEFL and TOEFL iBT are registered trademarks of ETS in the United States and other countries. This project is not endorsed or approved by ETS. It does not reproduce or distribute unlicensed ETS questions, passages, prompts, audio, transcripts, sample responses, answer keys, rubrics, directions, or graphics, and its feedback is not an official ETS score.

> [!WARNING]
> Bardora is the independent product name. The existing repository slug is a temporary technical identifier and will be migrated separately. Current ETS trademark guidance says ETS marks should not be incorporated into a product name, domain name, or similar identifier.

## Project status

**Task coaching, learning intelligence, and the v0.1.0 plugin package are implemented; host validation continues.** The repository defines the product, portable skill interface, official-format task matrix, architecture, task-specific coaching for Reading, Listening, Writing, and Speaking, and privacy-preserving progress continuity. Human calibration, installed cross-platform validation, independent public branding, and release gates remain before a stable release.

## What the skill does

- Route learners to the correct Reading, Listening, Writing, or Speaking task type.
- Teach the format and strategy with original practice material.
- Give specific, evidence-based feedback and a prioritized next step.
- Separate coaching estimates from official ETS scores.
- Support a full diagnostic, focused practice, review, and progress tracking.

The 2026 format contains 12 task types across four sections. See the [task-type matrix](docs/toefl-2026-task-matrix.md) for the official names and source links.

## Repository map

```text
plugin.json                           Portable plugin manifest
.codex-plugin/plugin.json             Codex adapter and presentation metadata
.claude-plugin/plugin.json            Claude Code adapter
SKILL.md                              Canonical coaching entry point
skills/coach/SKILL.md                 Thin plugin route to the canonical skill
docs/PRD.md                           Product requirements and MVP boundary
docs/architecture.md                  Portable architecture and contracts
docs/toefl-2026-task-matrix.md        ETS-sourced 2026 format matrix
docs/research/                         Dated official-source audits
docs/ROADMAP.md                       Delivery phases and completion criteria
docs/PRODUCT-STRATEGY.md              Open-core, growth, ecosystem, and paid strategy
docs/brand.md                         Brand identity, assets, palette, and usage
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
Use $bardora to give me a Writing diagnostic.
```

The skill is intentionally platform-neutral: it depends on readable Markdown and JSON, not a vendor SDK.

## Build as a Plugin

Build the same skills-only package for Codex and Claude Code:

```bash
python3 scripts/build_plugin_archive.py
```

See [plugin packaging and local validation](docs/PLUGIN-PACKAGING.md) for the manifest roles and platform-specific checks. The v0.1.0 package has no backend, account, analytics, or paid API dependency.

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
- [Global ecosystem strategy research — October 12, 2026](docs/research/ecosystem-strategy-2026-10-12.md)
- [Core behavior evaluation — October 12, 2026](evaluations/core-behavior-2026-10-12.md)
- [Roadmap](docs/ROADMAP.md)
- [Product and ecosystem strategy](docs/PRODUCT-STRATEGY.md)
- [Plugin packaging](docs/PLUGIN-PACKAGING.md)
- [Brand system](docs/brand.md)
- [Contributing](CONTRIBUTING.md)

## License

Original project material is available under the Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). The license does not grant rights to ETS trademarks or copyrighted ETS material.
