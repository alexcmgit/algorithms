"""Integration coverage for the stats generator; no solution code is executed."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import quote


GENERATOR = Path(__file__).with_name("solution_stats.py")
START = "<!-- solution-stats:start -->"
END = "<!-- solution-stats:end -->"


class SolutionStatsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.git("init", "--quiet")
        self.git("config", "user.name", "Stats Test")
        self.git("config", "user.email", "stats@example.invalid")
        self.write("README.md", f"# My solutions\n\nIntroduction.\n\n{START}\n{END}\n\nPersonal notes.\n")

    def git(self, *args, env=None):
        return subprocess.run(
            ["git", *args], cwd=self.root, env=env, text=True,
            check=True, capture_output=True,
        ).stdout.strip()

    def write(self, path, content="print('fixture')\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def commit(self, message="Add solutions", date="2024-01-02T12:00:00+00:00"):
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", message, env={
            **os.environ, "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date,
        })
        return self.git("rev-parse", "HEAD")

    def generate(self, success=True):
        result = subprocess.run(
            [sys.executable, str(GENERATOR), "--root", str(self.root)],
            text=True, capture_output=True,
            env={key: value for key, value in os.environ.items() if key != "GITHUB_STEP_SUMMARY"},
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            return json.loads((self.root / "stats/solutions.json").read_text())
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("marker", (result.stdout + result.stderr).lower())

    def outputs(self):
        return tuple((self.root / path).read_bytes() for path in (
            "README.md", "stats/solutions.json",
        ))

    def test_groups_problem_layouts_and_normalizes_languages(self):
        for path in (
            "beecrowd/c#/beginner/1001-extremely-basic.cs",
            "uoj/1001-extremely-basic/dart-2.18/solution1.dart",
            "uoj/1001-extremely-basic/dart-2.18/solution2.dart",
            "leetcode/example/dart/solution1/solution.dart",
            "leetcode/example/dart/solution2/solution.dart",
            "leetcode/example/node-18/solution.cjs",
            "hackerrank/python3/challenges/simple-sum.py",
            "codewars/python/value-of-x.py",
        ):
            self.write(path)
        self.commit()
        data = self.generate()
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["totals"], {
            "problems": 4, "solution_files": 8, "languages": 4,
            "collections": 4, "nonblank_lines": 8, "multilingual_problems": 2,
        })
        languages = {item["name"]: item for item in data["languages"]}
        self.assertEqual(languages["Dart"]["solution_files"], 4)
        self.assertEqual(languages["Dart"]["problems"], 2)
        self.assertEqual(languages["JavaScript"]["solution_files"], 1)
        collections = {item["key"]: item for item in data["collections"]}
        self.assertEqual(collections["beecrowd"]["problems"], 1)
        self.assertEqual(collections["beecrowd"]["solution_files"], 3)
        self.assertEqual(set(collections["beecrowd"]["paths"]), {"beecrowd", "uoj"})
        for problem in data["highlights"]["most_languages"]:
            self.assertEqual(problem["languages"], sorted(problem["languages"]))

    def test_ignores_support_files_empty_sources_and_untracked_work(self):
        self.write("leetcode/example/python/solution.py", "\nprint(1)\n\nprint(2)\n")
        for path in (
            "leetcode/example/python/test.py",
            "leetcode/example/dart/playground.dart",
            "leetcode/example/README.md",
            "leetcode/example/solution.yaml",
            ".github/scripts/helper.py",
            "docs/example.py",
            "uoj/9999-statement-only/README.md",
        ):
            self.write(path)
        self.write("leetcode/empty/python/solution.py", " \n\t\n")
        self.commit()
        self.write("leetcode/untracked/python/solution.py")
        data = self.generate()
        self.assertEqual(data["totals"]["problems"], 1)
        self.assertEqual(data["totals"]["solution_files"], 1)
        self.assertEqual(data["totals"]["nonblank_lines"], 2)

    def test_preserves_prose_and_encodes_source_links(self):
        path = "codewars/python/a # challenge.py"
        self.write(path)
        self.commit()
        self.generate()
        readme = (self.root / "README.md").read_text()
        self.assertTrue(readme.startswith(f"# My solutions\n\nIntroduction.\n\n{START}"))
        self.assertTrue(readme.endswith(f"{END}\n\nPersonal notes.\n"))
        self.assertIn(quote(path, safe="/"), readme)
        self.assertEqual(readme.count(START), 1)
        self.assertEqual(readme.count(END), 1)

    def test_deterministic_even_after_report_only_commit(self):
        self.write("leetcode/example/python/solution.py")
        source_commit = self.commit()
        data = self.generate()
        expected = self.outputs()
        self.generate()
        self.assertEqual(self.outputs(), expected)
        self.commit("Refresh stats", date="2024-02-03T12:00:00+00:00")
        self.generate()
        self.assertEqual(self.outputs(), expected)
        self.assertEqual(data["latest_source_change"]["commit"], source_commit)

    def test_latest_source_edit_updates_history(self):
        path = "leetcode/example/python/solution.py"
        self.write(path)
        self.commit()
        before = self.generate()
        self.write(path, "print('changed')\n")
        source_commit = self.commit("Improve implementation", "2024-03-04T12:00:00+00:00")
        after = self.generate()
        self.assertNotEqual(before["latest_source_change"], after["latest_source_change"])
        self.assertEqual(after["latest_source_change"]["commit"], source_commit)
        self.assertTrue(after["latest_source_change"]["date"].startswith("2024-03-04"))
        self.assertEqual(after["highlights"]["recent"][0]["updated"]["commit"], source_commit)

    def test_merge_resolution_is_recorded_as_latest_source_change(self):
        path = "leetcode/example/python/solution.py"
        self.write(path, "print('base')\n")
        self.commit()
        original_branch = self.git("branch", "--show-current")
        self.git("checkout", "-b", "feature")
        self.write(path, "print('feature')\n")
        self.commit("Feature implementation", "2024-02-01T12:00:00+00:00")
        self.git("checkout", original_branch)
        self.write(path, "print('main')\n")
        self.commit("Main implementation", "2024-03-01T12:00:00+00:00")
        with self.assertRaises(subprocess.CalledProcessError):
            self.git("merge", "--no-ff", "feature")
        self.assertIn(f"UU {path}", self.git("status", "--porcelain"))
        self.write(path, "print('resolved')\n")
        merge_commit = self.commit("Resolve implementations", "2024-04-01T12:00:00+00:00")

        data = self.generate()

        self.assertEqual(data["latest_source_change"]["commit"], merge_commit)
        self.assertEqual(data["highlights"]["recent"][0]["updated"]["commit"], merge_commit)

    def test_malformed_markers_leave_both_outputs_untouched(self):
        self.write("leetcode/example/python/solution.py")
        self.commit()
        self.generate()
        for malformed in (
            START, END, f"{START}\n{START}\n{END}",
            f"{START}\n{END}\n{END}", f"{END}\n{START}",
        ):
            with self.subTest(markers=malformed):
                self.write("README.md", f"Personal introduction.\n{malformed}\n")
                expected = self.outputs()
                self.generate(success=False)
                self.assertEqual(self.outputs(), expected)


if __name__ == "__main__":
    unittest.main()
