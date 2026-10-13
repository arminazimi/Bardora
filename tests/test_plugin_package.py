import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATHS = (
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
)


class PluginPackageTests(unittest.TestCase):
    def manifest(self, relative_path: str) -> dict:
        return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))

    def test_manifests_share_identity_and_version(self):
        manifests = [self.manifest(path) for path in MANIFEST_PATHS]
        self.assertEqual({"english-test-prep-coach"}, {item["name"] for item in manifests})
        self.assertEqual({"0.1.0"}, {item["version"] for item in manifests})
        for manifest in manifests:
            self.assertEqual("Apache-2.0", manifest["license"])
            self.assertEqual("Armin Azimi", manifest["author"]["name"])
            self.assertNotIn("TODO", json.dumps(manifest))

    def test_portable_manifest_and_host_adapters_exist(self):
        portable = self.manifest("plugin.json")
        codex = self.manifest(".codex-plugin/plugin.json")
        claude = self.manifest(".claude-plugin/plugin.json")
        self.assertEqual(
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            portable["$schema"],
        )
        self.assertEqual("./skills/", codex["skills"])
        self.assertEqual("English Test Prep Coach", codex["interface"]["displayName"])
        self.assertIn("keywords", claude)

    def test_plugin_entry_points_to_canonical_skill(self):
        entry = (ROOT / "skills" / "coach" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: coach", entry)
        self.assertIn("description:", entry)
        self.assertIn("](../../SKILL.md)", entry)
        self.assertIn("sole source of coaching behavior", entry)

    def test_archive_contains_runtime_sources_and_no_development_state(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_path = Path(temporary_directory) / "plugin.zip"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "build_plugin_archive.py"),
                    "--output",
                    str(archive_path),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            with zipfile.ZipFile(archive_path) as archive:
                names = set(archive.namelist())
                for required in (
                    "plugin.json",
                    ".codex-plugin/plugin.json",
                    ".claude-plugin/plugin.json",
                    "SKILL.md",
                    "skills/coach/SKILL.md",
                    "skills/toefl-writing-2026-coach/SKILL.md",
                    "docs/toefl-2026-task-matrix.md",
                    "references/feedback-contract.md",
                    "schemas/learner-state.v1.schema.json",
                    "LICENSE",
                    "NOTICE",
                ):
                    self.assertIn(required, names)
                self.assertFalse(any(name.startswith(".git/") for name in names))
                self.assertFalse(any(name.startswith("tests/") for name in names))
                self.assertFalse(any(name.startswith("evaluations/") for name in names))


if __name__ == "__main__":
    unittest.main()
