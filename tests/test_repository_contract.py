import json
import hashlib
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

VENDORED_WRITING_HASHES = {
    "SKILL.md": "6c9e7355567ceb3d2f05512fe6826a547d3690f29f161356c403f19bd6b864da",
    "agents/openai.yaml": "0d10b594ed66d7cfbc3552adbf44f876568addc2e37025a8a0f81b35668d2906",
    "references/academic-discussion-strategy.md": "64e38762a63955626a1657215e4cb08180451f29811c21a271e5d2985e535384",
    "references/academic-language-menus.md": "ac65ccdac743aa2a64e7c93ec00f1f26d109441ef564e276398738d99ffc0116",
    "references/coaching-workflow.md": "2c78dfdca3ea583e132fb06f91effff09ece60784a7f0e789a33c2d8c2157bd7",
    "references/email-strategy-and-language.md": "d074691f04f9591a814185501f1516d8a00554edbe4323e9e792fd1036ef1d65",
    "references/feedback-protocol.md": "4ea8bef27fdac7d905731694cf5768e820342a06c94a139b5cee4c01b2395e83",
    "references/high-score-calibration.md": "1eaef337602be5b05d0f6cd1cb1686a3376c6924423b10dce546a4149009cd73",
    "references/idea-bank.md": "1116bc4c9773e02b60df571f672fd4f7c270731b180ef4d6cdd8e204ddb7e7ec",
    "references/official-rubrics.md": "0cff238c692f74db7bdf891fcbb0b9d221a79bf66f05a588860c0785b8f2eec3",
    "references/sources.md": "bdd2fe21213ebd0b0bd57db34fe345d725d70a0d54bbb523f2ab37c0febc171f",
    "references/templates.md": "d075429cdcc685e565ce4a3642f3a1f3700b8fa94deb8dc15145b73dbf512cc8",
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
        module_path = "references/tasks/writing.build-a-sentence.md"
        module = self.read(module_path)
        cases = json.loads(self.read("tests/cases/build-a-sentence.json"))
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

    def test_write_an_email_module_contract(self):
        module_path = "references/tasks/writing.write-an-email.md"
        module = self.read(module_path)
        cases = json.loads(self.read("tests/cases/write-an-email.json"))
        self.assertEqual(5, len(cases))
        self.assertEqual(5, len({case["id"] for case in cases}))
        for heading in (
            "## Evidence required",
            "## Success dimensions",
            "## High-impact failure modes",
            "## Original-practice contract",
            "## Prepare and practice",
            "## Review and revise",
            "## Feedback boundary",
            "## Completion criterion",
        ):
            self.assertIn(heading, module)
        self.assertIn("not an official ETS score", module)
        for case in cases:
            self.assertGreaterEqual(len(case["expects"]), 4)

        report = self.read("evaluations/write-an-email-2026-10-12.md")
        self.assertIn("Pass: 5 of 5 cases and 20 of 20 observable criteria", report)
        for case in cases:
            self.assertIn(f"`{case['id']}`", report)

    def test_writing_routes_to_exact_vendored_skill(self):
        route = "skills/toefl-writing-2026-coach/SKILL.md"
        root_skill = self.read("SKILL.md")
        self.assertIn(f"]({route})", root_skill)
        self.assertIn("sole authoritative Writing implementation", root_skill)
        self.assertNotIn("](references/tasks/writing.build-a-sentence.md)", root_skill)
        self.assertNotIn("](references/tasks/writing.write-an-email.md)", root_skill)

        skill_root = ROOT / "skills" / "toefl-writing-2026-coach"
        actual_files = {
            path.relative_to(skill_root).as_posix()
            for path in skill_root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(set(VENDORED_WRITING_HASHES), actual_files)
        for relative_path, expected_hash in VENDORED_WRITING_HASHES.items():
            digest = hashlib.sha256((skill_root / relative_path).read_bytes()).hexdigest()
            self.assertEqual(expected_hash, digest, relative_path)

        vendored_skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", vendored_skill)
        self.assertGreaterEqual(len(links), 8)
        for link in links:
            self.assertTrue((skill_root / link).is_file(), link)

    def test_academic_discussion_evaluation_contract(self):
        cases = json.loads(self.read("tests/cases/academic-discussion.json"))
        self.assertEqual(5, len(cases))
        self.assertEqual(5, len({case["id"] for case in cases}))
        for case in cases:
            self.assertGreaterEqual(len(case["expects"]), 4)
        report = self.read("evaluations/academic-discussion-2026-10-12.md")
        self.assertIn("Pass: 5 of 5 cases and 20 of 20 observable criteria", report)
        for case in cases:
            self.assertIn(f"`{case['id']}`", report)

    def test_new_receptive_task_module_contracts(self):
        skill = self.read("SKILL.md")
        modules = {
            "references/tasks/reading.read-in-daily-life.md": "tests/cases/read-in-daily-life.json",
            "references/tasks/reading.read-an-academic-passage.md": "tests/cases/read-an-academic-passage.json",
            "references/tasks/listening.listen-and-choose-a-response.md": "tests/cases/listen-and-choose-a-response.json",
            "references/tasks/listening.listen-to-a-conversation.md": "tests/cases/listen-to-a-conversation.json",
            "references/tasks/listening.listen-to-an-announcement.md": "tests/cases/listen-to-an-announcement.json",
            "references/tasks/listening.listen-to-an-academic-talk.md": "tests/cases/listen-to-an-academic-talk.json",
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

    def test_listening_accessibility_contracts(self):
        modules = {
            "listening.listen-and-choose-a-response": "listen-and-choose-a-response",
            "listening.listen-to-a-conversation": "listen-to-a-conversation",
            "listening.listen-to-an-announcement": "listen-to-an-announcement",
            "listening.listen-to-an-academic-talk": "listen-to-an-academic-talk",
        }
        for task_id, stem in modules.items():
            with self.subTest(task=task_id):
                module = self.read(f"references/tasks/{task_id}.md").lower()
                cases = json.loads(self.read(f"tests/cases/{stem}.json"))
                case_ids = {case["id"] for case in cases}
                self.assertIn("## audio and accessibility paths", module)
                self.assertIn("transcript-only", module)
                self.assertRegex(module, r"screen[- ]reader")
                self.assertTrue(
                    any("accessibility" in case_id or "transcript" in case_id for case_id in case_ids)
                )

        report = self.read("evaluations/receptive-content-review-2026-10-12.md")
        self.assertIn("Pass with declared limits", report)
        self.assertIn("## Limitations", report)

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
            "evaluations/academic-discussion-2026-10-12.md",
            "evaluations/receptive-content-review-2026-10-12.md",
            "evaluations/write-an-email-2026-10-12.md",
            "references/feedback-contract.md",
            "references/tasks/reading.complete-the-words.md",
            "references/tasks/reading.read-in-daily-life.md",
            "references/tasks/reading.read-an-academic-passage.md",
            "references/tasks/listening.listen-and-choose-a-response.md",
            "references/tasks/listening.listen-to-a-conversation.md",
            "references/tasks/listening.listen-to-an-announcement.md",
            "references/tasks/listening.listen-to-an-academic-talk.md",
            "references/tasks/writing.build-a-sentence.md",
            "references/tasks/writing.write-an-email.md",
            "tests/cases/core.json",
            "tests/cases/build-a-sentence.json",
            "tests/cases/academic-discussion.json",
            "tests/cases/write-an-email.json",
            "tests/cases/complete-the-words.json",
            "tests/cases/read-in-daily-life.json",
            "tests/cases/read-an-academic-passage.json",
            "tests/cases/listen-and-choose-a-response.json",
            "tests/cases/listen-to-a-conversation.json",
            "tests/cases/listen-to-an-announcement.json",
            "tests/cases/listen-to-an-academic-talk.json",
            "scripts/check_originality.py",
        }
        missing = sorted(path for path in required if not (ROOT / path).is_file())
        self.assertEqual([], missing)


if __name__ == "__main__":
    unittest.main()
