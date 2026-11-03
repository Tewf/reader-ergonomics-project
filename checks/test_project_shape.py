"""Tests of checks/local/project_shape.py: each rule fails where it should and stays silent where it should not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""), REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
SPEC = importlib.util.spec_from_file_location("project_shape", REPOSITORY / "checks" / "local" / "project_shape.py")
project_shape = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(project_shape)

TOPIC = "**Shape:** [topic](https://example.org/shapes/topic.md)\n"
ROOT = ("# Job\n\nA job.\n\n**Shape:** [project](https://example.org/shapes/project.md)\n\n"
        "| Part | Summary |\n|---|---|\n" +
        "".join(f"| [{n}]({n}) | the {n} part |\n" for n in project_shape.DEFAULT_PARTS))
PARTS = {
    "problem.md": "# Problem\n\nThe problem.\n\n" + TOPIC + "\n**Problem:** How does one person finish a job well?\n",
    "scope.md": "# Scope\n\nThe scope.\n\n" + TOPIC + "\n| | What | Why |\n|---|---|---|\n| in | a | b |\n| out | c | d |\n",
    "review.md": "# Review\n\nThe review.\n\n" + TOPIC + "\n## Frame\n\n## Literature review\n\n## State of the art\n\n## Position\n",
    "baseline.md": "# Baseline\n\nThe baseline.\n\n" + TOPIC + "\n**Named baseline:** the six activities of a published process.\n\n"
                   "**Compared by:** paired jobs, counting round trips.\n",
    "plan.md": "# Plan\n\nThe plan.\n\n" + TOPIC + "\n## Steps\n\n## Decided first\n\n## For the person to decide\n",
    "trail.md": "# Trail\n\nThe trail.\n\n" + TOPIC +
                "\n| | What |\n|---|---|\n| Asked | a |\n| Found | b |\n| Produced | c |\n| Where it lives | d |\n",
}


class Check(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        self.write("job/README.md", ROOT)
        for name, text in PARTS.items():
            self.write(f"job/{name}", text)

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def write(self, path: str, text: str) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def run_check(self) -> list:
        return project_shape.check(self.root, {})

    def messages(self, severity: str = "error") -> list[str]:
        return [f.message for f in self.run_check() if f.kind == severity]

    def test_complete_project_passes(self) -> None:
        self.assertEqual(self.run_check(), [])

    def test_folder_without_the_declaration_is_ignored(self) -> None:
        self.write("job/README.md", "# Job\n\nA job.\n")
        (self.root / "job" / "plan.md").unlink()
        self.assertEqual(self.run_check(), [])

    def test_declaration_inside_a_skeleton_declares_nothing(self) -> None:
        self.write("job/README.md", "# Job\n\nA job.\n\n```markdown\n" + ROOT + "```\n")
        (self.root / "job" / "plan.md").unlink()
        self.assertEqual(self.run_check(), [])

    def test_relative_link_to_the_shape_declares_it(self) -> None:
        self.write("job/README.md", ROOT.replace("https://example.org/shapes/project.md", "../../project.md"))
        (self.root / "job" / "plan.md").unlink()
        self.assertTrue(any("lacks its part plan.md" in m for m in self.messages()))

    def test_another_shape_declares_nothing(self) -> None:
        self.write("job/README.md", ROOT.replace("shapes/project.md", "shapes/report.md"))
        (self.root / "job" / "plan.md").unlink()
        self.assertEqual(self.run_check(), [])

    def test_missing_part(self) -> None:
        (self.root / "job" / "scope.md").unlink()
        self.assertTrue(any("lacks its part scope.md" in m for m in self.messages()))

    def test_part_not_linked_from_the_root(self) -> None:
        self.write("job/README.md", ROOT.replace("| [trail.md](trail.md) | the trail.md part |\n", ""))
        self.assertTrue(any("does not link trail.md" in m for m in self.messages()))

    def test_part_without_the_topic_shape_line(self) -> None:
        self.write("job/plan.md", PARTS["plan.md"].replace(TOPIC, ""))
        self.assertTrue(any("announces the topic shape" in m for m in self.messages()))

    def test_problem_line_missing(self) -> None:
        self.write("job/problem.md", PARTS["problem.md"].replace("**Problem:**", "Problem:"))
        self.assertTrue(any("no line labelled Problem" in m for m in self.messages()))

    def test_problem_of_two_sentences_warns_only(self) -> None:
        self.write("job/problem.md", PARTS["problem.md"].replace("well?", "well? And what else is there?"))
        self.assertEqual(self.messages(), [])
        self.assertTrue(any("past one sentence" in m for m in self.messages("warning")))

    def test_scope_without_an_out_row(self) -> None:
        self.write("job/scope.md", PARTS["scope.md"].replace("| out | c | d |\n", ""))
        self.assertTrue(any("no 'out' row" in m for m in self.messages()))

    def test_scope_without_a_why_column(self) -> None:
        self.write("job/scope.md", PARTS["scope.md"].replace("| Why |", "| Note |"))
        self.assertTrue(any("Why column" in m for m in self.messages()))

    def test_review_without_a_step(self) -> None:
        self.write("job/review.md", PARTS["review.md"].replace("## Position\n", ""))
        self.assertTrue(any("step 'Position'" in m for m in self.messages()))

    def test_baseline_absent(self) -> None:
        self.write("job/baseline.md", PARTS["baseline.md"].replace("**Named baseline:**", "Baseline:"))
        self.assertTrue(any("names no baseline" in m for m in self.messages()))

    def test_baseline_placeholder(self) -> None:
        for placeholder in ("none", "TBD", "To be named", "<the baseline>", "N/A.", ""):
            with self.subTest(placeholder=placeholder):
                text = PARTS["baseline.md"].replace("the six activities of a published process.", placeholder)
                self.write("job/baseline.md", text)
                self.assertTrue(any("names no baseline" in m for m in self.messages()))

    def test_baseline_without_comparison_warns_only(self) -> None:
        self.write("job/baseline.md", PARTS["baseline.md"].replace("**Compared by:**", "Compared by:"))
        self.assertEqual(self.messages(), [])
        self.assertTrue(any("Compared by" in m for m in self.messages("warning")))

    def test_plan_without_decisions_of_the_person(self) -> None:
        self.write("job/plan.md", PARTS["plan.md"].replace("## For the person to decide\n", ""))
        self.assertTrue(any("For the person to decide" in m for m in self.messages()))

    def test_trail_without_where_it_lives(self) -> None:
        self.write("job/trail.md", PARTS["trail.md"].replace("| Where it lives | d |\n", ""))
        self.assertTrue(any("'where it lives' row" in m for m in self.messages()))

    def test_root_at_the_top_of_the_repository(self) -> None:
        shutil.rmtree(self.root / "job")
        self.write("README.md", ROOT)
        for name, text in PARTS.items():
            self.write(name, text)
        self.assertEqual(self.run_check(), [])


if __name__ == "__main__":
    unittest.main()
