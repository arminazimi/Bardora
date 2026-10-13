#!/usr/bin/env python3
"""Build a deterministic, skills-only plugin archive from canonical sources."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOP_LEVEL_FILES = (
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    "SKILL.md",
    "README.md",
    "LICENSE",
    "NOTICE",
)
SOURCE_DIRECTORIES = ("docs", "references", "schemas", "skills")
ZIP_TIMESTAMP = (2026, 1, 21, 0, 0, 0)


def package_files() -> list[Path]:
    files = [ROOT / relative_path for relative_path in TOP_LEVEL_FILES]
    for directory in SOURCE_DIRECTORIES:
        files.extend(path for path in (ROOT / directory).rglob("*") if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def build(output: Path) -> Path:
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    expected = ROOT / "dist" / f"{manifest['name']}-{manifest['version']}.zip"
    destination = output if output.is_absolute() else ROOT / output
    if str(output) == "dist":
        destination = expected
    destination.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source in package_files():
            relative = source.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("dist"),
        help="Archive path; the default uses dist/<name>-<version>.zip.",
    )
    args = parser.parse_args()
    print(build(args.output))


if __name__ == "__main__":
    main()
