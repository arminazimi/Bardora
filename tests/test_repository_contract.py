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

SECTION_ROWS = {
    "| Reading | 3 | 50 | 30 minutes | Two-stage adaptive |",
    "| Listening | 4 | 47 | 29 minutes | Two-stage adaptive |",
    "| Writing | 3 | 12 | 23 minutes | Linear |",
    "| Speaking | 2 | 11 | 8 minutes | Linear |",
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
        for expected_row in SECTION_ROWS:
            self.assertIn(expected_row, matrix)
        self.assertGreaterEqual(matrix.count("https://www.ets.org/"), 6)
        self.assertIn("January 21, 2026", matrix)
        self.assertIn("Published items (may vary)", matrix)
        self.assertIn("Published blueprint target", matrix)
        self.assertIn("content/dam/ets-org/", matrix)
        self.assertNotIn("content/dam/ets-india/", matrix)
        self.assertIn("1–6 scale in 0.5 increments", matrix)
        self.assertIn("two-year transition", matrix)
        self.assertIn("Scores are valid for two years", matrix)

    def test_every_task_has_a_behavior_case(self):
        cases = json.loads(self.read("tests/cases/core.json"))
        case_ids = {case["id"] for case in cases}
        self.assertEqual(set(), TASK_IDS - case_ids)
        for case in cases:
            self.assertTrue(case["request"].strip())
            self.assertGreaterEqual(len(case["expects"]), 3)

    def test_latest_behavior_evaluation_covers_every_case(self):
        cases = json.loads(self.read("tests/cases/core.json"))
        report = self.read("evaluations/core-behavior-2026-10-12.md")
        self.assertIn("Pass: 14 of 14 cases and 55 of 55 observable criteria", report)
        self.assertIn("## Limitations", report)
        for case in cases:
            self.assertIn(f"`{case['id']}`", report)

    def test_build_a_sentence_module_contract(self):
        skill = self.read("SKILL.md")
        module_path = "references/tasks/writing.build-a-sentence.md"
        module = self.read(module_path)
        cases = json.loads(self.read("tests/cases/build-a-sentence.json"))
        self.assertIn(f"]({module_path})", skill)
        self.assertEqual(5, len(cases))
        self.assertEqual(5, len({case["id"] for case in cases}))
        for heading in (
            "## Evidence required",
            "## Success dimensions",
            "## High-impact failure modes",
            "## Original-practice contract",
            "## Completion criterion",
        ):
            self.assertIn(heading, module)
        for case in cases:
            self.assertGreaterEqual(len(case["expects"]), 4)

        report = self.read("evaluations/build-a-sentence-2026-10-12.md")
        self.assertIn("Pass: 5 of 5 cases and 20 of 20 observable criteria", report)
        for case in cases:
            self.assertIn(f"`{case['id']}`", report)

    def test_complete_the_words_module_contract(self):
        skill = self.read("SKILL.md")
        module_path = "references/tasks/reading.complete-the-words.md"
        module = self.read(module_path)
        cases = json.loads(self.read("tests/cases/complete-the-words.json"))
        self.assertIn(f"]({module_path})", skill)
        self.assertEqual(5, len(cases))
        self.assertEqual(5, len({case["id"] for case in cases}))
        for heading in (
            "## Evidence required",
            "## Success dimensions",
            "## High-impact failure modes",
            "## Original-practice contract",
            "## Completion criterion",
        ):
            self.assertIn(heading, module)
        for case in cases:
            self.assertGreaterEqual(len(case["expects"]), 4)

    def test_new_receptive_task_module_contracts(self):
        skill = self.read("SKILL.md")
        modules = {
            "references/tasks/reading.read-in-daily-life.md": "tests/cases/read-in-daily-life.json",
            "references/tasks/reading.read-an-academic-passage.md": "tests/cases/read-an-academic-passage.json",
            "references/tasks/listening.listen-and-choose-a-response.md": "tests/cases/listen-and-choose-a-response.json",
        }
        headings = (
            "## Evidence required",
            "## Success dimensions",
            "## High-impact failure modes",
            "## Original-practice contract",
            "## Feedback boundary",
            "## Completion criterion",
        )
        for module_path, case_path in modules.items():
            with self.subTest(module=module_path):
                module = self.read(module_path)
                cases = json.loads(self.read(case_path))
                self.assertIn(f"]({module_path})", skill)
                self.assertEqual(5, len(cases))
                self.assertEqual(5, len({case["id"] for case in cases}))
                for heading in headings:
                    self.assertIn(heading, module)
                self.assertIn("do not copy or closely paraphrase ETS", module)
                for case in cases:
                    self.assertTrue(case["request"].strip())
                    self.assertGreaterEqual(len(case["expects"]), 4)

    def test_task_specific_behavior_requests_are_unique(self):
        case_files = sorted((ROOT / "tests" / "cases").glob("*.json"))
        seen = {}
        duplicates = []
        for case_file in case_files:
            for case in json.loads(case_file.read_text(encoding="utf-8")):
                request = case["request"].strip()
                if request in seen:
                    duplicates.append((request, seen[request], case_file.name))
                else:
                    seen[request] = case_file.name
        self.assertEqual([], duplicates)

    def test_public_docs_disclose_independence_and_scoring_limit(self):
        combined = "\n".join(
            self.read(path)
            for path in ("README.md", "SKILL.md", "docs/PRD.md")
        ).lower()
        self.assertIn("not endorsed or approved by ets", combined)
        self.assertIn("not an official ets score", combined)

    def test_ip_notice_covers_trademarks_and_protected_material(self):
        notice = self.read("NOTICE").lower()
        readme = self.read("README.md").lower()
        contributing = self.read("CONTRIBUTING.md").lower()
        self.assertIn("not endorsed or approved by ets", notice)
        self.assertIn("does not grant rights", notice)
        for protected_type in ("passages", "audio", "rubrics", "graphics"):
            self.assertIn(protected_type, readme)
            self.assertIn(protected_type, contributing)

    def test_required_project_documents_exist(self):
        required = {
            "README.md",
            "SKILL.md",
            "LICENSE",
            "NOTICE",
            "CONTRIBUTING.md",
            "docs/PRD.md",
            "docs/architecture.md",
            "docs/toefl-2026-task-matrix.md",
            "docs/ROADMAP.md",
            "evaluations/core-behavior-2026-10-12.md",
            "evaluations/build-a-sentence-2026-10-12.md",
            "references/feedback-contract.md",
            "references/tasks/reading.complete-the-words.md",
            "references/tasks/reading.read-in-daily-life.md",
            "references/tasks/reading.read-an-academic-passage.md",
            "references/tasks/listening.listen-and-choose-a-response.md",
            "references/tasks/writing.build-a-sentence.md",
            "tests/cases/core.json",
            "tests/cases/build-a-sentence.json",
            "tests/cases/complete-the-words.json",
            "tests/cases/read-in-daily-life.json",
            "tests/cases/read-an-academic-passage.json",
            "tests/cases/listen-and-choose-a-response.json",
        }
        missing = sorted(path for path in required if not (ROOT / path).is_file())
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
