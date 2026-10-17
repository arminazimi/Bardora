# Plugin packaging

The repository root is the canonical, skills-only plugin package. The portable manifest and the Codex and Claude compatibility manifests share the same name and semantic version:

- `plugin.json` — portable Agent Plugin manifest;
- `.codex-plugin/plugin.json` — Codex compatibility and presentation metadata;
- `.claude-plugin/plugin.json` — Claude Code compatibility manifest.

The coaching behavior remains in the root `SKILL.md`. `skills/coach/SKILL.md` is a thin plugin entry point that loads that canonical file, so packaging does not create a second implementation. The complete Writing skill remains independently discoverable under `skills/toefl-writing-2026-coach/` and is still routed by the canonical coach.

## Build the local archive

Run:

```bash
python3 scripts/build_plugin_archive.py
```

The result is `dist/bardora-0.1.0.zip`. The archive is deterministic and contains only manifests, canonical coaching sources, documentation, schemas, and license files. Generated archives stay outside version control.

## Validate for Codex

Run the repository tests and the Codex plugin validator:

```bash
python3 -m unittest discover -s tests -v
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

The local marketplace and directory submission are release concerns. They are intentionally absent from v0.1.0 so the canonical package can be validated before an installation catalog points to it.

## Validate for Claude Code

With Claude Code installed, run:

```bash
claude plugin validate . --strict
claude --plugin-dir .
```

In that session, invoke `/bardora:coach` or make a relevant coaching request and verify model invocation. Use `/reload-plugins` after local edits.

## Version rule

Update all three manifests together. Packaging is complete only when their `name` and `version` values match, the repository tests pass, and both host validators accept the same archive.
