# Automatic solution stats

[Solution stats](../.github/workflows/solution-stats.yml) updates the generated section of [the README](../README.md) and [the JSON report](../stats/solutions.json) after commits to `main`.

The workflow waits **5 minutes** before checking out the repository or generating the report. A new push cancels the previous run and starts a fresh wait. For example, commits at 14:00, 14:02, and 14:04 produce one report update around 14:09, plus GitHub's queue and processing time. There is no scheduled run while the repository is idle.

This is a debounce: it batches report updates after a pause. GitHub still creates a workflow run for each push, and the waiting time consumes runner time. Continuous editing keeps postponing the update. Canceled runs in the Actions tab are expected.

## Change the delay or run immediately

In **Settings → Secrets and variables → Actions → Variables**, create a repository variable named `STATS_DEBOUNCE_SECONDS`. Use an integer between `0` and `900`; the default is `300`. For example, `600` waits 10 minutes.

For an immediate update, open **Actions → Solution stats → Run workflow**, select `main`, and leave **Generate immediately instead of waiting for the quiet period** checked. A manual run shares the same concurrency group as automatic runs, so a subsequent push still supersedes it.

## What gets published

The report reads tracked solution files and Git history. It does not execute solutions or infer that they pass an online judge. Counts and highlights describe the code present in the repository, including work in progress. Generated output stays stable when its underlying data is unchanged.

Only `README.md` and `stats/solutions.json` are staged for the bot commit, and a commit is made only when those files change. Text outside the README's generated markers is preserved. The workflow checks for new commits before publishing and uses a normal push, so it cannot overwrite a concurrent edit. If `main` advances, the newer workflow run handles the update.

The workflow uses the built-in `GITHUB_TOKEN` with `contents: write`; no extra secrets or external services are needed. Its bot push [does not trigger another push workflow](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#triggering-a-workflow-from-a-workflow). Repository or organization rules must allow this token to push to `main`; a rule requiring pull requests or forbidding workflow writes will reject publication.

## Counting rules

- A solution file is a tracked, nonempty source file in one of the recognized collection directories. Language comes from its extension; versioned folders and `.js`/`.cjs`/`.mjs` are grouped into the same language.
- Tests, playgrounds, symlinks, input/output fixtures, metadata, and statement-only folders do not count. Nonblank source lines include comments.
- BeeCrowd's flat filenames and `uoj` problem folders are matched by numeric problem ID, so those two collections are reported together.
- HackerRank and Codewars use the source filename to identify a problem across languages. HackerRank contests retain their namespace. Other collections use the problem folder directly under the collection directory; numbered solution variants count as separate files for the same problem.
- Recent updates come from source-file Git history. README edits, tests, and generated commits do not change those dates. The report uses no generation timestamp, so rerunning it against unchanged sources produces the same output.

The JSON report contains totals, breakdowns, and the same highlights as the README. To add a new collection or language, extend `COLLECTIONS` or `LANGUAGES` in [the generator](../.github/scripts/solution_stats.py). Keep the `<!-- solution-stats:start -->` and `<!-- solution-stats:end -->` markers in the README; everything between them is regenerated.

## Run locally

From a full clone, with Python 3 installed:

```sh
python3 -m unittest discover -s .github/scripts -p 'test_*.py'
python3 .github/scripts/solution_stats.py
```

The generator uses only Python's standard library and Git. Review the resulting README and JSON diff as usual.
