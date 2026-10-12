import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TASK_IDS = {
    "reading.complete-the-words",
    "reading.read-in-daily-life",
    "reading.read-an-academic-passage",
    "listening.listen-and-choose-a-response",
    "listening.listen-to-a-conversation",
    "listening.listen-to-an-announcement",
    "listening.listen-to-an-academic-talk",
    "writing.build-a-sentence",
    "writing.write-an-email",
    "writing.academic-discussion",
    "speaking.listen-and-repeat",
    "speaking.take-an-interview",
}


class RepositoryContractTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_skill_has_valid_required_frontmatter(self):
        skill = self.read("SKILL.md")
        match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        frontmatter = match.group(1)
        self.assertRegex(frontmatter, r"(?m)^name: english-test-prep-coach$")
        self.assertRegex(frontmatter, r"(?m)^description: .+")
        self.assertNotIn("TODO", skill)

    def test_skill_references_resolve(self):
        skill = self.read("SKILL.md")
        links = re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", skill)
        self.assertGreaterEqual(len(links), 2)
        for link in links:
            self.assertTrue((ROOT / link).is_file(), f"Missing SKILL.md reference: {link}")

    def test_matrix_has_all_task_ids_and_official_sources(self):
        matrix = self.read("docs/toefl-2026-task-matrix.md")
        missing = sorted(task_id for task_id in TASK_IDS if f"`{task_id}`" not in matrix)
        self.assertEqual([], missing, f"Task matrix is missing: {missing}")
        self.assertGreaterEqual(matrix.count("https://www.ets.org/"), 2)
        self.assertIn("January 21, 2026", matrix)

    def test_every_task_has_a_behavior_case(self):
        cases = json.loads(self.read("tests/cases/core.json"))
        case_ids = {case["id"] for case in cases}
        self.assertEqual(set(), TASK_IDS - case_ids)
        for case in cases:
            self.assertTrue(case["request"].strip())
            self.assertGreaterEqual(len(case["expects"]), 3)

    def test_public_docs_disclose_independence_and_scoring_limit(self):
        combined = "\n".join(
            self.read(path)
            for path in ("README.md", "SKILL.md", "docs/PRD.md")
        ).lower()
        self.assertIn("not endorsed or approved by ets", combined)
        self.assertIn("not an official ets score", combined)

    def test_required_project_documents_exist(self):
        required = {
            "README.md",
            "SKILL.md",
            "LICENSE",
            "CONTRIBUTING.md",
            "docs/PRD.md",
            "docs/architecture.md",
            "docs/toefl-2026-task-matrix.md",
            "docs/ROADMAP.md",
            "references/feedback-contract.md",
            "tests/cases/core.json",
        }
        missing = sorted(path for path in required if not (ROOT / path).is_file())
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
