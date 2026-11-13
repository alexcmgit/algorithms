#!/usr/bin/env python3
"""Build a deterministic solution inventory using only Python's standard library."""

import argparse
from collections import defaultdict
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import quote


START = "<!-- solution-stats:start -->"
END = "<!-- solution-stats:end -->"
LANGUAGES = {
    ".c": "C", ".cpp": "C++", ".cc": "C++", ".cxx": "C++",
    ".cs": "C#", ".dart": "Dart", ".go": "Go", ".java": "Java",
    ".js": "JavaScript", ".cjs": "JavaScript", ".mjs": "JavaScript",
    ".jl": "Julia", ".kt": "Kotlin", ".kts": "Kotlin", ".py": "Python",
    ".rkt": "Racket", ".rs": "Rust", ".rb": "Ruby", ".sql": "SQL",
    ".swift": "Swift", ".ts": "TypeScript",
}
COLLECTIONS = {
    "beecrowd": "BeeCrowd / URI", "uoj": "BeeCrowd / URI",
    "codegolf": "Code Golf", "coderbyte": "Coderbyte", "codewars": "Codewars",
    "ctfwgoogle": "Google CTF", "euler": "Project Euler",
    "hackerrank": "HackerRank", "leetcode": "LeetCode", "misc": "Miscellaneous",
    "mit": "MIT", "triage": "Triage / work in progress", "ubc": "UBC",
}


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def describe_source(filename):
    """Normalize the repository's folder and flat-file problem layouts."""
    path = PurePosixPath(filename)
    parts = path.parts
    if len(parts) < 3 or parts[0] not in COLLECTIONS:
        return None
    language = LANGUAGES.get(path.suffix.lower())
    stem = path.stem.lower()
    if not language or any(p.lower() in {"test", "tests", "__pycache__"} for p in parts[:-1]):
        return None
    if (stem in {"test", "playground", "conftest"}
            or stem.startswith(("test_", "test-", "playground"))
            or stem.endswith(("_test", "-test", ".test", ".spec"))):
        return None

    collection = "beecrowd" if parts[0] == "uoj" else parts[0]
    if collection == "beecrowd":
        slug = path.stem if parts[0] == "beecrowd" else parts[1]
        match = re.match(r"(\d+)(?:-|$)", slug)
        if not match:
            return None
        problem_id = match.group(1)
    elif collection in {"hackerrank", "codewars"}:
        slug = path.stem
        # The same challenge in different languages is one problem. Contests
        # keep their namespace so they cannot collide with regular challenges.
        namespace = "/".join(parts[2:-1]) if "contests" in parts[2:-1] else ""
        problem_id = f"{namespace}/{slug}" if namespace else slug
    else:
        slug = problem_id = parts[1]
    title = slug.replace("-", " ").replace("_", " ").strip().title()
    return {
        "key": f"{collection}/{problem_id}", "title": title,
        "collection": collection, "language": language, "path": filename,
    }


def source_history(root):
    """Read history once; generated reports never affect source activity dates."""
    raw = git(root, "log", "--format=%x1e%H%x00%cI", "--name-only", "-z",
              "--diff-merges=first-parent", "--no-renames", "--", *COLLECTIONS)
    latest = None
    by_path = {}
    for record in raw.decode("utf-8", errors="replace").split("\x1e")[1:]:
        fields = record.split("\0")
        commit, date = fields[:2]
        change = {"commit": commit, "date": date}
        for filename in fields[2:]:
            # git separates the commit header from its first pathname with LF.
            filename = filename.lstrip("\n")
            if describe_source(filename):
                if latest is None:
                    latest = change
                by_path.setdefault(filename, change)
    return latest, by_path


def build_stats(root):
    latest, history = source_history(root)
    filenames = git(root, "ls-files", "-z").decode("utf-8").split("\0")
    sources = []
    for filename in sorted(filenames):
        source = describe_source(filename)
        path = root / filename
        if source is None or path.is_symlink() or not path.is_file():
            continue
        code = path.read_text(encoding="utf-8", errors="replace")
        if not code.strip():
            continue
        source["nonblank_lines"] = sum(bool(line.strip()) for line in code.splitlines())
        sources.append(source)

    grouped = defaultdict(list)
    for source in sources:
        grouped[source["key"]].append(source)
    # Git log order is newest first, including when commits share a timestamp.
    history_order = {path: i for i, path in enumerate(history)}
    problems = []
    for key, entries in sorted(grouped.items()):
        paths_with_history = [s["path"] for s in entries if s["path"] in history]
        newest_path = min(paths_with_history, key=history_order.get, default=None)
        problems.append({
            "key": key, "title": entries[0]["title"],
            "collection": entries[0]["collection"],
            "languages": sorted({s["language"] for s in entries}),
            "solution_files": len(entries), "path": entries[0]["path"],
            "updated": history.get(newest_path),
        })

    languages = []
    for language in sorted({s["language"] for s in sources}):
        entries = [s for s in sources if s["language"] == language]
        languages.append({
            "name": language, "solution_files": len(entries),
            "problems": len({s["key"] for s in entries}),
            "nonblank_lines": sum(s["nonblank_lines"] for s in entries),
        })
    languages.sort(key=lambda row: (-row["solution_files"], row["name"]))
    collections = []
    for collection in sorted({s["collection"] for s in sources}):
        entries = [s for s in sources if s["collection"] == collection]
        collections.append({
            "key": collection, "name": COLLECTIONS[collection],
            "paths": sorted({PurePosixPath(s["path"]).parts[0] for s in entries}),
            "solution_files": len(entries), "problems": len({s["key"] for s in entries}),
            "languages": len({s["language"] for s in entries}),
        })
    collections.sort(key=lambda row: (-row["problems"], row["name"]))

    # Rank recent problems by commit order, without a wall-clock cutoff that
    # would force new generated commits simply because time passed.
    commit_order = {}
    for change in history.values():
        commit_order.setdefault(change["commit"], len(commit_order))
    recent = sorted(
        (p for p in problems if p["updated"]),
        key=lambda p: (commit_order[p["updated"]["commit"]], p["key"]),
    )[:10]
    return {
        "schema_version": 1,
        "totals": {
            "problems": len(problems), "solution_files": len(sources),
            "languages": len(languages), "collections": len(collections),
            "nonblank_lines": sum(s["nonblank_lines"] for s in sources),
            "multilingual_problems": sum(len(p["languages"]) > 1 for p in problems),
        },
        "latest_source_change": latest, "languages": languages, "collections": collections,
        "highlights": {
            "most_languages": sorted(
                (p for p in problems if len(p["languages"]) > 1),
                key=lambda p: (-len(p["languages"]), -p["solution_files"], p["key"]),
            )[:5],
            "recent": recent,
        },
    }


def escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(
        ">", "&gt;").replace("|", "&#124;").replace("[", "&#91;").replace(
        "]", "&#93;").replace("\n", " ")


def link(title, path):
    return f"[{escape(title)}](./{quote(path, safe='/')})"


def render_stats(stats):
    totals = stats["totals"]
    lines = [
        "## Solution stats", "",
        "| Problems with implementations | Solution files | Languages | Collections |",
        "| ---: | ---: | ---: | ---: |",
        f"| {totals['problems']:,} | {totals['solution_files']:,} | "
        f"{totals['languages']} | {totals['collections']} |", "",
        f"**{totals['multilingual_problems']:,} problems** have implementations in multiple languages. "
        f"The collection contains **{totals['nonblank_lines']:,} nonblank source lines** "
        "(including comments).", "",
    ]
    latest = stats["latest_source_change"]
    if latest:
        lines.extend([f"Latest source change: **{latest['date'][:10]}** "
                      f"(`{latest['commit'][:7]}`).", ""])
    lines.extend(["### Languages", "",
                  "| Language | Solution files | Problems | Share of files |",
                  "| --- | ---: | ---: | ---: |"])
    for row in stats["languages"]:
        share = row["solution_files"] / totals["solution_files"] * 100
        lines.append(f"| {row['name']} | {row['solution_files']:,} | {row['problems']:,} | {share:.1f}% |")
    lines.extend(["", "### Collections", "",
                  "| Collection | Problems | Solution files | Languages |",
                  "| --- | ---: | ---: | ---: |"])
    for row in stats["collections"]:
        links = " / ".join(link(path, path) for path in row["paths"])
        lines.append(f"| {row['name']} ({links}) | {row['problems']:,} | "
                     f"{row['solution_files']:,} | {row['languages']} |")
    lines.extend(["", "### Highlights", ""])
    if stats["languages"]:
        top = stats["languages"][0]
        lines.append(f"- Most-used language: **{top['name']}**, with {top['solution_files']:,} solution files.")
    if stats["collections"]:
        top = stats["collections"][0]
        lines.append(f"- Largest collection: **{top['name']}**, with {top['problems']:,} problems.")
    lines.extend(["", "Problems explored in the most languages:", "",
                  "| Problem | Collection | Languages | Solution files |",
                  "| --- | --- | --- | ---: |"])
    for problem in stats["highlights"]["most_languages"]:
        lines.append(f"| {link(problem['title'], problem['path'])} | "
                     f"{COLLECTIONS[problem['collection']]} | {', '.join(problem['languages'])} | "
                     f"{problem['solution_files']} |")
    lines.extend(["", "### Recently updated solutions", "",
                  "Dates refer to source commits, not report updates.", "",
                  "| Date | Problem | Collection | Languages |",
                  "| --- | --- | --- | --- |"])
    for problem in stats["highlights"]["recent"]:
        lines.append(f"| {problem['updated']['date'][:10]} | {link(problem['title'], problem['path'])} | "
                     f"{COLLECTIONS[problem['collection']]} | {', '.join(problem['languages'])} |")
    lines.extend([
        "", "Counts describe tracked, nonempty source files; they do not imply judge acceptance. "
        "Tests, playgrounds, and statement-only folders are excluded. BeeCrowd and URI entries "
        "with the same problem ID are counted together.", "",
        "[Counting rules and automation](docs/solution-stats.md) · "
        "[JSON report](stats/solutions.json)",
    ])
    return "\n".join(lines)


def update_readme(readme, report):
    block = f"{START}\n{report}\n{END}"
    if START not in readme and END not in readme:
        return readme.rstrip() + "\n\n" + block + "\n"
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(START) > readme.index(END):
        raise ValueError("README.md must contain exactly one ordered pair of solution-stats markers")
    before, rest = readme.split(START)
    _, after = rest.split(END)
    return before + block + after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        readme_path = root / "README.md"
        readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else (
            "# Algorithms\n\nCollection of all my DS/Algo solutions.\n")
        stats = build_stats(root)
        report = render_stats(stats)
        # Validate the marker pair before writing either generated file.
        updated = update_readme(readme, report)
        encoded = json.dumps(stats, indent=2, ensure_ascii=False) + "\n"
        readme_path.write_text(updated, encoding="utf-8")
        output = root / "stats" / "solutions.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded, encoding="utf-8")
        if summary_path := os.environ.get("GITHUB_STEP_SUMMARY"):
            # Keep the run summary compact; the linked README has the full report.
            summary = report.split("### Languages", 1)[0]
            repository = os.environ.get("GITHUB_REPOSITORY")
            if repository:
                server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
                summary += f"[Full report]({server}/{repository}/blob/main/README.md#solution-stats)\n"
            with open(summary_path, "a", encoding="utf-8") as stream:
                stream.write(summary)
        print(f"{stats['totals']['problems']} problems, {stats['totals']['solution_files']} solution files, "
              f"{stats['totals']['languages']} languages")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Could not generate solution stats: {error}\n")


if __name__ == "__main__":
    main()
